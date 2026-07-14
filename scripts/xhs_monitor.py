#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小红书数据回馈飞轮 (xhs_monitor)
================================
发布后跑一遍：拉取创作者数据 → 存档 raw json → 生成复盘报告 md。
这是「采集→发布→数据回馈→内容矩阵调优」飞轮的最后一段，
把 opencli 现成的创作者数据命令封装成可复用的复盘动作。

用法:
    python scripts/xhs_monitor.py                 # 拉今天数据 + 生成报告
    python scripts/xhs_monitor.py --compare       # 额外对比上一次存档，算增量
    python scripts/xhs_monitor.py --date 2026-07-14

依赖:
    opencli (--profile kzbaq3xs 已登录小红书创作者中心)
    pip install 无第三方依赖 (标准库)
"""
import subprocess, json, os, sys, datetime, argparse

PROFILE = "kzbaq3xs"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_BASE = os.path.join(ROOT, "output", "monitoring")


_OPENCLI = None


def _locate_opencli():
    """opencli 装在 npm 全局目录，Python 子进程默认 PATH 找不到，用绝对路径。"""
    p = r"C:\Program Files\nodejs\node_global\opencli.cmd"
    if os.path.exists(p):
        return p
    import shutil
    for c in ("opencli.cmd", "opencli"):
        if shutil.which(c):
            return c
    return "opencli"


def run(cmd):
    global _OPENCLI
    if _OPENCLI is None:
        _OPENCLI = _locate_opencli()
    full = [_OPENCLI] + list(cmd[1:])
    s = " ".join(f'"{x}"' if " " in x else x for x in full)
    p = subprocess.run(s, capture_output=True, text=True, shell=True)
    if p.returncode != 0:
        print(f"[WARN] {s} 失败: {p.stderr[:200]}", file=sys.stderr)
        return None
    return p.stdout


def pull(date_str):
    out_dir = os.path.join(OUT_BASE, date_str)
    os.makedirs(out_dir, exist_ok=True)
    cmds = {
        "profile": ["opencli", "--profile", PROFILE, "xiaohongshu", "creator-profile", "-f", "json"],
        "notes":   ["opencli", "--profile", PROFILE, "xiaohongshu", "creator-notes", "-f", "json"],
        "stats":   ["opencli", "--profile", PROFILE, "xiaohongshu", "creator-stats", "-f", "json"],
    }
    raw = {}
    for k, c in cmds.items():
        out = run(c)
        if out:
            raw[k] = out
            with open(os.path.join(out_dir, f"{k}.json"), "w", encoding="utf-8") as f:
                f.write(out)
    return out_dir, raw


def prev_dir(date_str):
    """找最近一次早于 date_str 的存档目录"""
    if not os.path.isdir(OUT_BASE):
        return None
    dirs = sorted(d for d in os.listdir(OUT_BASE) if d < date_str)
    return os.path.join(OUT_BASE, dirs[-1]) if dirs else None


def analyze(raw, prev_raw=None):
    notes = json.loads(raw.get("notes") or "[]")
    stats = json.loads(raw.get("stats") or "[]")
    profile_list = json.loads(raw.get("profile") or "[]")
    profile = {row.get("field"): row.get("value") for row in profile_list}
    rep = {"profile": profile, "notes": [], "stats": stats, "issues": [], "prev": None}

    # 笔记明细 + 互动率
    for n in notes:
        v = n.get("views", 0) or 0
        lk = n.get("likes", 0) or 0
        cc = n.get("collects", 0) or 0
        cm = n.get("comments", 0) or 0
        interact = lk + cc + cm
        rate = round(interact / v * 100, 1) if v else 0
        rep["notes"].append({**n, "interact": interact, "rate": rate})

    # 诊断
    total_comments = sum(n.get("comments", 0) or 0 for n in notes)
    if total_comments == 0:
        rep["issues"].append(("致命", "全部笔记评论数=0。小红书算法把评论率当核心推流信号，0 互动会触发停止推流死循环。必须人工破 0。"))
    for n in rep["notes"]:
        if (n.get("views", 0) or 0) >= 50 and (n.get("comments", 0) or 0) == 0:
            rep["issues"].append(("高", f"《{n['title']}》观看 {n['views']} 但 0 评论，内容没激发表达欲，需加互动钩子。"))
    # 简介检查
    bio = (profile.get("Bio") or "").strip()
    if len(bio) < 15:
        rep["issues"].append(("中", f"账号简介过短（当前：{bio!r}）。访客进主页看不到清晰人设，关注转化低。定稿卡要求 4 行简介。"))

    # 对比上次
    if prev_raw:
        pnotes = json.loads(prev_raw.get("notes") or "[]")
        pstats = {s["metric"]: s for s in json.loads(prev_raw.get("stats") or "[]")}
        cstats = {s["metric"]: s for s in stats}
        def tot(metric):
            return (cstats.get(metric, {}) or {}).get("total", 0)
        def ptot(metric):
            return (pstats.get(metric, {}) or {}).get("total", 0)
        rep["prev"] = {
            "followers": profile.get("Followers"),
            "d_views": tot("观看数 (views)") - ptot("观看数 (views)"),
            "d_likes": tot("点赞数 (likes)") - ptot("点赞数 (likes)"),
            "d_collects": tot("收藏数 (collects)") - ptot("收藏数 (collects)"),
            "d_followers": profile.get("Followers", 0) - (prev_profile_followers(prev_raw)),
        }
    return rep


def prev_profile_followers(prev_raw):
    try:
        plist = json.loads(prev_raw.get("profile") or "[]")
        d = {row.get("field"): row.get("value") for row in plist}
        return d.get("Followers", 0) or 0
    except Exception:
        return 0


def render(rep, date_str):
    lines = []
    p = rep["profile"]
    lines.append(f"# 小红书复盘报告 · {date_str}\n")
    lines.append(f"> 账号：**{p.get('Name')}** ｜ 粉丝 {p.get('Followers')} ｜ 获赞收藏 {p.get('Likes & Collects')} ｜ 等级 {p.get('Creator Level')}（{p.get('Level Progress')}）\n")

    if rep["prev"]:
        pv = rep["prev"]
        lines.append(f"## 较上次增量\n")
        lines.append(f"- 粉丝：{pv['followers']}（Δ{pv['d_followers']:+d}）")
        lines.append(f"- 观看：Δ{pv['d_views']:+d} ｜ 点赞：Δ{pv['d_likes']:+d} ｜ 收藏：Δ{pv['d_collects']:+d}\n")

    lines.append("## 笔记明细（按发布时间倒序）\n")
    lines.append("| # | 标题 | 日期 | 观看 | 点赞 | 收藏 | 评论 | 互动率 |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
    for i, n in enumerate(rep["notes"], 1):
        lines.append(f"| {i} | {n.get('title','')} | {n.get('date','')} | {n.get('views',0)} | {n.get('likes',0)} | {n.get('collects',0)} | {n.get('comments',0)} | {n.get('rate',0)}% |")
    lines.append("")

    lines.append("## 7 日趋势\n")
    for s in rep["stats"]:
        lines.append(f"- **{s['metric']}**：总量 {s['total']} ｜ 趋势 `{s['trend']}`")
    lines.append("")

    lines.append("## 诊断\n")
    if not rep["issues"]:
        lines.append("暂无严重问题 ✅")
    else:
        for sev, msg in rep["issues"]:
            emoji = {"致命": "🚨", "高": "⚠️", "中": "🔸", "低": "🔹"}.get(sev, "•")
            lines.append(f"- {emoji} **[{sev}]** {msg}")
    lines.append("")

    lines.append("## 建议动作\n")
    lines.append("1. **破 0 评论**：自己（或小号）在每篇笔记评论区起头提问，制造可聊信号。")
    lines.append("2. **补简介**：按定稿卡把简介改成 4 行人设版，提升主页关注转化。")
    lines.append("3. **盯 CTR**：封面点击率 <8% 的笔记，换封面重发或优化标题钩子。")
    lines.append("4. **回流内容矩阵**：把本篇结论（哪类标题/封面带来互动）回填内容矩阵，指导下一篇选题。")
    lines.append("")
    lines.append("---")
    lines.append(f"_生成于 {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} · 数据源 opencli creator-*_")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    ap.add_argument("--compare", action="store_true")
    args = ap.parse_args()

    out_dir, raw = pull(args.date)
    prev = prev_dir(args.date)
    prev_raw = None
    if (args.compare or True) and prev:
        try:
            prev_raw = {k: open(os.path.join(prev, f"{k}.json"), encoding="utf-8").read()
                        for k in ("profile", "notes", "stats")}
        except Exception:
            prev_raw = None

    rep = analyze(raw, prev_raw)
    md = render(rep, args.date)
    md_path = os.path.join(out_dir, "复盘报告.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"[OK] raw json + 复盘报告已生成:\n  {out_dir}")
    print(f"  报告: {md_path}")
    # 终端摘要
    print("\n=== 诊断速览 ===")
    for sev, msg in rep["issues"]:
        print(f"  [{sev}] {msg}")


if __name__ == "__main__":
    main()
