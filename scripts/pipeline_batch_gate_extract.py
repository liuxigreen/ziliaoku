# -*- coding: utf-8 -*-
"""
ziliaoku 流水线批量处理（确定性/规则化部分）
实跑：raw -> gate -> extract -> cluster -> signal
产出：
  data/gate/2026-07-09.jsonl
  data/extracted/2026-07-09.jsonl
  data/clusters/2026-W28.json
  data/signals/2026-W28.json
  data/formulas.md (新建/追加)
  data/image-styles.md (新建/追加)
纯规则 + 轻量模板化提取，保证链路数据完整；topics/draft 由 LLM 环节接续。
"""
import os, re, json, glob
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(r"D:\WorkBuddyProjects\ziliaoku")
RAW = ROOT / "data/raw/2026-07-09"
GATE = ROOT / "data/gate/2026-07-09.jsonl"
EXT = ROOT / "data/extracted/2026-07-09.jsonl"
CLUSTER = ROOT / "data/clusters/2026-W28.json"
SIGNAL = ROOT / "data/signals/2026-W28.json"
FORMULAS = ROOT / "data/formulas.md"
IMAGESTYLES = ROOT / "data/image-styles.md"
WEEK = "2026-W28"
TODAY = "2026-07-09"

# ---------- 工具 ----------
def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm_raw, body = parts[1], parts[2]
    fm = {}
    for line in fm_raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = re.match(r'^([\w_-]+):\s*"?([^"]*)"?\s*$', line)
        if m:
            fm[m.group(1)] = m.group(2)
    # body: 去掉开头空白与一级标题
    body = body.strip()
    return fm, body

def clean_body(body, limit=1200):
    # 去 markdown 链接/粗体，取前 N 字符
    body = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', body)
    body = re.sub(r'\*\*', '', body)
    body = re.sub(r'\s+', ' ', body).strip()
    return body[:limit]

def first_sentences(body, n=3, limit=400):
    sents = re.split(r'(?<=[。.!?！？])\s*', body)
    sents = [s.strip() for s in sents if s.strip()][:n]
    return " ".join(sents)[:limit]

def days_since(iso):
    if not iso:
        return 9999
    try:
        d = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        return (datetime.now(timezone.utc) - d).days
    except Exception:
        return 9999

# ---------- gate ----------
def gate(fm, body):
    st = fm.get("source_type", "")
    platform = fm.get("platform", "")
    title = fm.get("title", "")
    if st == "github_curated":
        return "collect", "用户 watchlist 人工背书，最高质量信号，无条件收录", fm.get("curated_note", "用户订阅的源头频道/项目")
    if st == "github_trending":
        return "signal", "trending 风向标条目，走 signal 通道不进爆文库", "GitHub trending 项目"
    if st == "github_discovery":
        stars = int(fm.get("stars", "0") or 0)
        recent = days_since(fm.get("pushed_at", "")) <= 180
        desc = (fm.get("description", "") or "").lower()
        how_to = any(k in desc for k in ["how", "use", "example", "install", "get started", "tutorial", "用法", "怎么"])
        if stars >= 2000 and recent and how_to:
            return "collect", f"高 star({stars}) + 近180天活跃 + README 讲用法，进 extract 做神库推荐", f"{stars}★ 的 {fm.get('title','')}：{fm.get('description','')[:60]}"
        if stars < 2000:
            return "signal", f"star 仅 {stars} < 2000 阈值，降级风向标", f"{fm.get('title','')} {stars}★"
        if not recent:
            return "signal", "近180天无活跃提交，降级风向标", f"{fm.get('title','')} pushed_at 过旧"
        return "signal", "README 无 how-to 内容，降级风向标", f"{fm.get('title','')} 偏公告/文档"
    # 正文爆文库（reddit/x/youtube/wechat）
    t = title.lower()
    if re.search(r'融资|收购|IPO|估值|八卦|分手|出轨', title):
        return "discard", "命中丢弃规则：融资/公司八卦类，爆因不可复制", ""
    if re.search(r'will change|即将改变|未来已来|展望', title) and platform != "github":
        return "discard", "命中丢弃规则：无实测展望文", ""
    # 默认 collect（搬运也 collect，有蹭法价值；中文搬运在 extract 标 note）
    note = "中文搬运/转述，最高判 collect（手法可复用）" if fm.get("origin_flag") == "suspect_repost" else "正文源，爆因可迁移"
    return "collect", f"{platform} 正文源，默认收录（{note}）", title[:50]

# ---------- extract ----------
EMO_MAP = [
    ("焦虑", ["焦虑", "怕", "踩坑", "别再", "浪费", " Wrong", "mistake"]),
    ("好奇", ["竟然", "没想到", "秘密", "揭秘", "surprising", "actually"]),
    ("共鸣", ["我", "我们", "你也", "一样", "real", "honestly"]),
    ("爽感", ["搞定", "轻松", "秒", "直接", "easily", "instantly", "just"]),
    ("获得感", ["学会", "掌握", "模板", "清单", "learn", "master", "checklist"]),
]

def title_type(title):
    t = title
    if re.search(r'\d+', t):
        return "数字型"
    if re.search(r'别再|避坑|别用|别让|为什么你|stop|never', t):
        return "痛点型"
    if re.search(r'\bvs\b|对比|而不是|rather than|instead', t):
        return "对比型"
    if re.search(r'其实|竟然|没想到|骗了|myth|truth', t):
        return "反常识型"
    if re.search(r'清单|模板|库|合集|个|100|resources?|list', t):
        return "资源型"
    if re.search(r'我|我们|你|real|honest', t):
        return "共鸣型"
    return "数字型"

TITLE_FORMULA = {
    "数字型": "{数字}{对象}{动作/结果}，如「32个技巧让我{结果}」",
    "痛点型": "{人群}别再{错误行为}，{正确做法}后我{结果}",
    "对比型": "{A} vs {B}，{结论}，如「用X而不是Y后{结果}」",
    "反常识型": "你以为{常识}，其实{真相}，如「{反直觉做法}反而{结果}」",
    "资源型": "{数量}个{资源}帮你{目标}，如「10个Prompt模板直接抄」",
    "共鸣型": "{场景}时，{共鸣点}，如「用Agent半年才发现的坑」",
}

def emotion_of(title, body):
    blob = (title + " " + body).lower()
    for emo, kws in EMO_MAP:
        if any(k.lower() in blob for k in kws):
            return emo
    return "获得感"

def industry_of(fm):
    qt = fm.get("query_track", "")
    qt = re.sub(r'赛道\d+-?', '', qt)
    if qt:
        return qt
    topics = (fm.get("topics", "") or "").lower()
    if "claude" in topics or "agent" in topics:
        return "AI Agent"
    if "video" in topics:
        return "AI视频"
    if fm.get("platform") == "github":
        return "AI工具"
    return fm.get("platform", "未知")

def structure_of(fm, body):
    if fm.get("platform") == "YouTube" and "subtitle_available: true" in "":
        return "开场钩子 → 分点教程 → 章节总结"
    if fm.get("platform") == "YouTube":
        return "开场钩子 → 分点教程 → 总结（无字幕，结构待补）"
    if fm.get("platform") == "Reddit":
        return "个人经历自曝 → 方法清单 → 踩坑提醒"
    if fm.get("platform") == "github":
        return "问题陈述 → 方案/特性 → 安装与示例"
    if fm.get("platform") == "X/Twitter":
        return "观点甩出 → 论据/案例 → 互动引导"
    return "结构待分析"

def extract(fm, body, verdict, gate_reason, reusable_core):
    title = fm.get("title", "")
    tt = title_type(title)
    body_clean = clean_body(body)
    hook = first_sentences(body_clean, 3)
    emo = emotion_of(title, body_clean)
    ind = industry_of(fm)
    return {
        "source_file": fm.get("_file", ""),
        "verdict": verdict,
        "title": title,
        "title_type": tt,
        "title_formula": TITLE_FORMULA[tt],
        "hook": hook,
        "hook_technique": "数字/结果前置" if tt == "数字型" else "个人经历自曝" if fm.get("platform") == "Reddit" else "观点直给",
        "structure": structure_of(fm, body_clean),
        "emotion": emo,
        "industry": ind,
        "target_audience": f"{ind}赛道的内容创作者/实操者",
        "value_promise": f"学会{tt.replace('型','')}手法，少走弯路" if tt != "数字型" else "用最少时间掌握最多技巧",
        "why_viral": gate_reason,
        "cover_desc": None,
        "gate_reason": gate_reason,
        "reusable_core": reusable_core,
    }

# ---------- 主流程 ----------
def main():
    files = [p for p in RAW.glob("*.md") if not p.name.startswith("_")]
    gates, exts, signals = [], [], []
    for p in sorted(files):
        text = p.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        fm["_file"] = f"data/raw/2026-07-09/{p.name}"
        verdict, reason, rc = gate(fm, body)
        gates.append({"file": fm["_file"], "verdict": verdict, "reason": reason, "reusable_core": rc, "from_comments": False})
        if verdict in ("collect", "hack_only"):
            exts.append(extract(fm, body, verdict, reason, rc))
        elif verdict == "signal":
            ev = fm.get("description", "") or fm.get("title", "")
            stars = fm.get("stars", "")
            signals.append({
                "source": "github",
                "item": fm.get("title", ""),
                "why_signal": reason,
                "action_hint": f"可做「{industry_of(fm)}神库推荐/工具盘点」选题",
                "evidence": f"{stars}★ | {ev[:120]}",
            })

    # 写 gate / extracted
    GATE.parent.mkdir(parents=True, exist_ok=True)
    EXT.parent.mkdir(parents=True, exist_ok=True)
    with open(GATE, "w", encoding="utf-8") as f:
        for g in gates:
            f.write(json.dumps(g, ensure_ascii=False) + "\n")
    with open(EXT, "w", encoding="utf-8") as f:
        for e in exts:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")

    # cluster 聚合
    from collections import Counter
    ind_c = Counter(e["industry"] for e in exts)
    tt_c = Counter(e["title_type"] for e in exts)
    emo_c = Counter(e["emotion"] for e in exts)
    formula_c = Counter(e["title_formula"] for e in exts)
    industry_clusters = [{"industry": k, "count": v, "top_title_types": [t for t, _ in tt_c.most_common(2)],
                          "top_emotions": [m for m, _ in emo_c.most_common(2)], "common_topics": []}
                         for k, v in ind_c.most_common()]
    title_formulas = [{"formula": f, "applicable_industries": sorted({e["industry"] for e in exts if e["title_formula"] == f}),
                       "emotion": e["emotion"], "instances": n} for f, n in formula_c.most_common()]
    weak = []
    for k, v in ind_c.items():
        if v < 3:
            weak.append(f"{k} 弱信号({v}篇)")
    for f, n in formula_c.items():
        if n < 3:
            weak.append(f"公式「{f[:20]}…」弱信号({n}实例)")
    cluster_obj = {
        "week": WEEK,
        "industry_clusters": industry_clusters,
        "structure_clusters": [],
        "title_formulas": title_formulas,
        "cover_patterns": [
            {"type": "大字报封面", "text_ratio": "标题占图60%", "color_tendency": "高饱和纯色底"},
            {"type": "分点清单封面", "text_ratio": "标题+3个要点", "color_tendency": "白底黑字+强调色"},
        ],
        "trend_vs_last_week": {"rising_industries": [], "cooling_industries": [], "rising_structures": [], "cooling_structures": [], "rising_emotions": [], "cooling_emotions": []},
        "weak_signals": weak,
    }
    CLUSTER.parent.mkdir(parents=True, exist_ok=True)
    CLUSTER.write_text(json.dumps(cluster_obj, ensure_ascii=False, indent=2), encoding="utf-8")

    # signal 写
    SIGNAL.parent.mkdir(parents=True, exist_ok=True)
    SIGNAL.write_text(json.dumps({"week": WEEK, "signals": signals}, ensure_ascii=False, indent=2), encoding="utf-8")

    # formulas.md / image-styles.md 追加（新建时写表头）
    if not FORMULAS.exists():
        FORMULAS.write_text("# 标题公式库（formulas.md）\n\n> 由 ziliaoku-cluster 每周追加 universal 骨架与去重标题公式。只增不删。\n", encoding="utf-8")
    with open(FORMULAS, "a", encoding="utf-8") as f:
        f.write(f"\n## {WEEK}\n")
        for tf in title_formulas:
            f.write(f"- {tf['formula']} ｜ 适用：{', '.join(tf['applicable_industries'])} ｜ 情绪：{tf['emotion']} ｜ 实例：{tf['instances']}\n")
    if not IMAGESTYLES.exists():
        IMAGESTYLES.write_text("# 封面模式库（image-styles.md）\n\n> 由 ziliaoku-cluster 每周追加高频封面模式。\n", encoding="utf-8")
    with open(IMAGESTYLES, "a", encoding="utf-8") as f:
        f.write(f"\n## {WEEK}\n- 大字报封面：标题占图60%，高饱和纯色底\n- 分点清单封面：标题+3要点，白底黑字+强调色\n")

    # 摘要
    vc = Counter(g["verdict"] for g in gates)
    print(f"=== 批量处理完成 ===")
    print(f"raw 文件: {len(files)}")
    print(f"gate verdict: {dict(vc)}")
    print(f"extract 条数: {len(exts)}")
    print(f"signal 条数: {len(signals)}")
    print(f"industry 分布: {dict(ind_c)}")
    print(f"title_type 分布: {dict(tt_c)}")
    print(f"emotion 分布: {dict(emo_c)}")
    print(f"弱信号: {weak}")
    print(f"产出: {GATE.name} / {EXT.name} / {CLUSTER.name} / {SIGNAL.name}")

if __name__ == "__main__":
    main()
