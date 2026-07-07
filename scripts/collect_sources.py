#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
爆文采集脚本 v3 — Reddit + YouTube（agent-reach / opencli + yt-dlp）
输出：data/raw/{YYYY-MM-DD}/{序号}_{platform}.md（与现有 schema 对齐）

频率纪律（用户强调）：
- Reddit 每条 query 之间 sleep 6s（opencli 驱动浏览器，防限频）
- YouTube 每个视频之间 sleep 5s，每个 query 之间 sleep 8s
- 单条 opencli 调用超时 90s；yt-dlp 字幕超时 150s

YouTube 字幕方案（v3 重大修正）：
- ❌ opencli `transcript` 适配器实测超时/返回空，已弃用。
- ✅ 改用 yt-dlp + cookies.txt 抓字幕（用户已登录 YouTube，导出 cookie 即可）。
- 按视频「原始语言」(yt-dlp 的 language 字段) 优先选字幕轨，原始语言缺失再 zh→en 兜底。
- 无 cookies.txt 时自动降级：YouTube 走 opencli 发现（无字幕），不阻断采集。

cookies.txt 配置（一次性）：
- 浏览器装「Get cookies.txt LOCALLY」扩展 → 打开 youtube.com → 导出 cookies.txt
- 存到项目根目录 D:/WorkBuddyProjects/ziliaoku/cookies.txt（已 gitignore）
- 之后每次运行自动带 cookie，字幕全量抓取。
- 备选：关掉 Chrome 后运行 `yt-dlp --cookies-from-browser chrome ...`（Chrome 运行时会锁 Cookie 库，复制失败）。
"""

import os
import re
import sys
import json
import time
import tempfile
import subprocess
from datetime import datetime, timezone, timedelta
from pathlib import Path

try:
    import yaml
except ImportError:
    print("[ERR] PyYAML 缺失，请装在 agent-reach venv")
    sys.exit(1)

# ── 路径 ──────────────────────────────────────────
WORKFLOW_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = WORKFLOW_DIR / "data" / "raw"
OPENCLI = r"C:\Program Files\nodejs\node_global\opencli.cmd"
YT_DLP = r"C:\Users\liuxi\.agent-reach-venv\Scripts\yt-dlp.exe"
COOKIES = WORKFLOW_DIR / "cookies.txt"          # 一次性导出，已 gitignore

# ── 频率控制 ──────────────────────────────────────
REDDIT_QUERY_GAP = 6      # query 之间
YT_VIDEO_GAP = 5          # 视频之间
YT_QUERY_GAP = 8          # query 之间
CALL_TIMEOUT = 90
YT_SUB_TIMEOUT = 150

# ── 字幕语言 ──────────────────────────────────────
# 用户强调「设置原始语言」：fetch 时优先用视频原始 language 字段，
# 下列为缺失时的兜底偏好顺序（中文优先，因多数中文 AI 实操内容价值高）。
YT_SUB_LANGS = "zh.*,zh-Hans.*,zh-CN.*,en.*,en-US.*,en-GB.*"
YT_SUB_PREFER = ["zh-Hans", "zh-CN", "zh", "en-US", "en-GB", "en"]

# ── 查询（对齐 keywords.md 六赛道，AI 向）─────────
# (query, 赛道标签)
REDDIT_QUERIES = [
    ("Claude Code workflow tips",        "赛道1-AI工具"),
    ("n8n automation workflow tutorial", "赛道1-AI工具/自动化"),
    ("ComfyUI image generation workflow","赛道2-AI创作"),
    ("AI video generation Sora Kling",   "赛道2-AI视频"),
    ("AI side hustle passive income",    "赛道4-副业"),
    ("AI content creation strategy",     "赛道3-自媒体"),
]
REDDIT_LIMIT = 4

YT_QUERIES = [
    ("Claude Code 教程",       "赛道1-AI工具"),
    ("ComfyUI 工作流",         "赛道2-AI创作"),
    ("AI 短视频 即梦 可灵",     "赛道2-AI视频"),
    ("n8n 自动化 工作流",       "赛道1/4-自动化"),
    ("小红书 起号 实操",        "赛道3-自媒体"),
    ("AI 副业 真实案例",        "赛道4-副业"),
]
YT_LIMIT = 2


def get_today_str():
    tz = timezone(timedelta(hours=8))
    return datetime.now(tz).strftime("%Y-%m-%d")


def get_today_dir():
    d = RAW_DIR / get_today_str()
    d.mkdir(parents=True, exist_ok=True)
    return d


def existing_files_count(out_dir: Path) -> int:
    return len(list(out_dir.glob("*.md")))


def load_seen_urls(out_dir: Path) -> set:
    """扫描已有 raw，收集 url 字段，避免重复采集"""
    seen = set()
    for f in out_dir.glob("*.md"):
        try:
            txt = f.read_text(encoding="utf-8")
        except Exception:
            continue
        m = re.search(r"^url:\s*\"?([^\"\n]+)\"?", txt, re.MULTILINE)
        if m:
            seen.add(m.group(1).strip())
    return seen


def ytdlp_cookie_args():
    return ["--cookies", str(COOKIES)] if COOKIES.exists() else []


def run_opencli(args: list, timeout: int = CALL_TIMEOUT) -> str:
    try:
        r = subprocess.run(
            [OPENCLI] + args,
            capture_output=True, text=True, shell=True, timeout=timeout
        )
        return r.stdout or ""
    except subprocess.TimeoutExpired:
        return ""
    except Exception as e:
        print(f"  [opencli-error] {e}")
        return ""


def run_ytdlp(args: list, timeout: int = YT_SUB_TIMEOUT) -> subprocess.CompletedProcess:
    """yt-dlp 是真实 exe，用 shell=False 避免路径空格引号问题"""
    return subprocess.run([YT_DLP] + args, capture_output=True, text=True,
                          shell=False, timeout=timeout)


def parse_yaml_list(text: str):
    """把 opencli 的 yaml 输出解析为 list[dict]；失败/错误块返回 []"""
    text = text.strip()
    if not text:
        return []
    try:
        data = yaml.safe_load(text)
    except Exception:
        return []
    if isinstance(data, dict):
        if data.get("ok") is False:
            return []
        return [data]
    if isinstance(data, list):
        return [x for x in data if isinstance(x, dict)]
    return []


def parse_field_value_list(text: str) -> dict:
    """opencli `video -f yaml` 返回 [{field,value},...] 形式，转 dict"""
    out = {}
    cur = None
    for line in text.splitlines():
        if line.startswith("- field:"):
            cur = line.split("field:", 1)[1].strip()
            out[cur] = ""
        elif line.startswith("  value:"):
            if cur is not None:
                out[cur] = line.split("value:", 1)[1].strip()
    return out


def utc_to_beijing(utc_sec: float) -> str:
    try:
        dt = datetime.fromtimestamp(float(utc_sec), tz=timezone(timedelta(hours=8)))
        return dt.strftime("%Y-%m-%d")
    except Exception:
        return "N/A"


def fmt_upload_date(s) -> str:
    """yt-dlp upload_date = YYYYMMDD → YYYY-MM-DD"""
    s = str(s or "")
    if len(s) == 8 and s.isdigit():
        return f"{s[:4]}-{s[4:6]}-{s[6:8]}"
    return s or "N/A"


def strip_vtt(text: str) -> str:
    """去掉 WEBVTT 头/时间戳行/序号，保留字幕正文"""
    lines = []
    for ln in text.splitlines():
        s = ln.strip()
        if not s:
            continue
        if s == "WEBVTT":
            continue
        if "-->" in s:
            continue
        if re.match(r"^\d+$", s):
            continue
        lines.append(s)
    return "\n".join(lines)


def fetch_subtitle(url: str, prefer_lang: str = None) -> str:
    """
    用 yt-dlp + cookies.txt 抓字幕。
    优先 prefer_lang（视频原始语言），缺失按 YT_SUB_PREFER 兜底。
    返回纯字幕文本；失败返回 ""。
    """
    if not COOKIES.exists():
        return ""
    tmp = tempfile.mkdtemp(prefix="yt_sub_")
    args = ytdlp_cookie_args() + [
        "--no-warnings", "--skip-download",
        "--write-auto-subs", "--write-subs",
        "--sub-langs", YT_SUB_LANGS,
        "--sub-format", "vtt",
        "-o", f"{tmp}/%(id)s.%(ext)s",
        url,
    ]
    try:
        r = run_ytdlp(args, timeout=YT_SUB_TIMEOUT)
    except subprocess.TimeoutExpired:
        print("    [sub] 超时")
        return ""
    if r.returncode != 0:
        err = (r.stderr or "")[:200]
        print(f"    [sub] 失败: {err}")
        return ""
    vtts = list(Path(tmp).glob("*.vtt"))
    if not vtts:
        return ""
    # 选轨：原始语言优先
    pref = ([prefer_lang] if prefer_lang else []) + YT_SUB_PREFER
    chosen = None
    for lang in pref:
        for v in vtts:
            if v.stem.endswith(lang):
                chosen = v
                break
        if chosen:
            break
    if not chosen:
        chosen = vtts[0]
    text = strip_vtt(chosen.read_text(encoding="utf-8", errors="ignore"))
    return text


# ── Reddit 采集 ───────────────────────────────────
def collect_reddit(out_dir: Path, seen: set, start_idx: int):
    print(f"\n[Reddit] 开始，{len(REDDIT_QUERIES)} 个 query × {REDDIT_LIMIT} 条")
    count = 0
    idx = start_idx
    for q, track in REDDIT_QUERIES:
        print(f"  → reddit search: {q}  [{track}]")
        raw = run_opencli(["reddit", "search", q, "-f", "yaml", "--limit", str(REDDIT_LIMIT)])
        posts = parse_yaml_list(raw)
        if not posts:
            print("    (无数据/解析失败，跳过)")
            time.sleep(REDDIT_QUERY_GAP)
            continue
        for p in posts:
            url = (p.get("url") or "").strip()
            if url and url in seen:
                continue
            if url:
                seen.add(url)
            title = (p.get("title") or "Unknown").strip()
            author = (p.get("author") or "unknown").strip()
            sub = (p.get("subreddit") or "").strip()
            score = p.get("score", "")
            comments = p.get("comments", "")
            created = utc_to_beijing(p.get("created_utc", 0))
            selftext = (p.get("selftext") or "").strip()
            selftext = re.sub(r"\n{3,}", "\n\n", selftext)
            if len(selftext) > 6000:
                selftext = selftext[:6000] + "\n\n…(截断)"
            idx += 1
            fname = f"{idx:02d}_reddit_{sub.replace('r/','')}.md"
            content = f"""---
title: "{title.replace(chr(34), "'")}"
author: "{author}"
platform: Reddit
source: agent-reach reddit
source_type: aggregator_discovery
source_platform: reddit
subreddit: "{sub}"
score: {score}
comments: {comments}
url: "{url}"
published: "{created}"
query_track: "{track}"
collected: "{get_today_str()}"
---

# {title}

**作者**：{author}（{sub}）｜ **赞**：{score} ｜ **评论**：{comments}

{selftext}
"""
            (out_dir / fname).write_text(content, encoding="utf-8")
            count += 1
        print(f"    采到 {len(posts)} 条（累计 {count}）")
        time.sleep(REDDIT_QUERY_GAP)
    print(f"[Reddit] 完成，新增 {count} 条")
    return count


# ── YouTube 采集（yt-dlp + cookies，原始语言字幕）──
def collect_youtube(out_dir: Path, seen: set, start_idx: int):
    cookie_args = ytdlp_cookie_args()
    if cookie_args:
        print(f"\n[YouTube] 开始（yt-dlp + cookies，原始语言字幕），"
              f"{len(YT_QUERIES)} query × {YT_LIMIT} 视频")
    else:
        print(f"\n[YouTube] 开始（无 cookies.txt → opencli 发现降级，无字幕），"
              f"{len(YT_QUERIES)} query × {YT_LIMIT} 视频")
    count = 0
    idx = start_idx
    for q, track in YT_QUERIES:
        print(f"  → youtube: {q}  [{track}]")
        items = []
        if cookie_args:
            # 全量走 yt-dlp（搜索+元数据+原始语言）
            r = run_ytdlp(cookie_args + ["--no-warnings", "-j",
                                         f"ytsearch{YT_LIMIT}:{q}"],
                          timeout=120)
            for line in (r.stdout or "").splitlines():
                line = line.strip()
                if not line:
                    continue
                try:
                    items.append(json.loads(line))
                except Exception:
                    continue
        else:
            # 降级：opencli 发现（无字幕）
            raw = run_opencli(["youtube", "search", q, "-f", "yaml",
                               "--limit", str(YT_LIMIT)])
            items = parse_yaml_list(raw)

        if not items:
            print("    (无数据/解析失败，跳过)")
            time.sleep(YT_QUERY_GAP)
            continue

        for it in items:
            if cookie_args:
                vid = it.get("id") or ""
                url = it.get("webpage_url") or f"https://www.youtube.com/watch?v={vid}"
                title = (it.get("title") or "Unknown").strip()
                channel = (it.get("channel") or it.get("uploader") or "").strip()
                views = it.get("view_count", "")
                likes = it.get("like_count", "")
                duration = it.get("duration", "")
                published = fmt_upload_date(it.get("upload_date", ""))
                desc = (it.get("description") or "").strip()
                keywords = it.get("tags") or []
                language = it.get("language") or None
            else:
                url = (it.get("url") or "").strip()
                if url and url in seen:
                    continue
                if url:
                    seen.add(url)
                title = (it.get("title") or "Unknown").strip()
                channel = (it.get("channel") or "").strip()
                views = (it.get("views") or "").strip()
                likes = ""
                duration = (it.get("duration") or "").strip()
                published = (it.get("published") or "").strip()
                desc = ""
                keywords = []
                language = None

            if url and url in seen:
                continue
            if url:
                seen.add(url)

            desc = re.sub(r"\n{3,}", "\n\n", desc)
            kw_str = ", ".join([str(k) for k in keywords if k])[:200]

            # 字幕（yt-dlp + cookies，原始语言优先）
            sub_ok = False
            transcript = ""
            if cookie_args:
                transcript = fetch_subtitle(url, language)
                if transcript and len(transcript) > 30:
                    sub_ok = True
            if sub_ok:
                body = f"# 字幕正文（原始语言：{language or 'auto'}）\n\n{transcript[:8000]}"
            else:
                body = (f"# 视频描述（字幕不可用，降级）\n\n{desc[:4000]}\n\n"
                        f"**关键词**：{kw_str}")

            idx += 1
            safe_ch = re.sub(r"[^\w一-龥]", "", channel)[:12] or "yt"
            fname = f"{idx:02d}_yt_{safe_ch}.md"
            content = f"""---
title: "{title.replace(chr(34), "'")}"
author: "{channel}"
platform: YouTube
source: yt-dlp + cookies
source_type: aggregator_discovery
source_platform: youtube
channel: "{channel}"
views: "{views}"
likes: "{likes}"
duration: "{duration}"
published: "{published}"
video_id: "{vid if cookie_args else ''}"
url: "{url}"
keywords: "{kw_str.replace(chr(34), "'")}"
subtitle_language: "{language or 'N/A'}"
subtitle_available: {str(sub_ok).lower()}
query_track: "{track}"
collected: "{get_today_str()}"
---

{body}
"""
            (out_dir / fname).write_text(content, encoding="utf-8")
            count += 1
            print(f"    ✓ {title[:30]} | 字幕:{sub_ok} lang:{language}")
            time.sleep(YT_VIDEO_GAP)
        time.sleep(YT_QUERY_GAP)
    print(f"[YouTube] 完成，新增 {count} 条")
    return count


def backfill_youtube_subs(out_dir: Path):
    """已有 yt_*.md 补全字幕（需 cookies.txt）。保留 frontmatter，重写正文。"""
    if not COOKIES.exists():
        print("[backfill] 缺少 cookies.txt，无法抓字幕。请先导出 cookie。")
        return 0
    files = sorted(out_dir.glob("*_yt_*.md"))
    print(f"\n[backfill] 补全 {len(files)} 个 YouTube 文件字幕（cookies 已就位）")
    done = 0
    for f in files:
        txt = f.read_text(encoding="utf-8")
        m = re.search(r"^url:\s*\"?([^\"\n]+)\"?", txt, re.MULTILINE)
        if not m:
            continue
        url = m.group(1).strip()
        # 取原始语言
        lm = re.search(r"^subtitle_language:\s*\"?([^\"\n]+)\"?", txt, re.MULTILINE)
        lang = lm.group(1).strip() if lm else None
        if lang in ("N/A", "", "None"):
            lang = None
        transcript = fetch_subtitle(url, lang)
        if not transcript or len(transcript) <= 30:
            print(f"    ~ 跳过（无字幕）{f.name}")
            continue
        # 拆 frontmatter / body
        parts = txt.split("\n---\n", 1)
        if len(parts) != 2:
            continue
        fm, _ = parts
        new_fm = re.sub(r"subtitle_available:.*", "subtitle_available: true",
                        fm)
        new_body = f"# 字幕正文（原始语言：{lang or 'auto'}）\n\n{transcript[:8000]}"
        f.write_text(new_fm + "\n---\n\n" + new_body, encoding="utf-8")
        done += 1
        print(f"    ✓ 补全 {f.name} ({len(transcript)} 字)")
        time.sleep(2)
    print(f"[backfill] 完成，补全 {done} 条")
    return done


def write_summary(out_dir: Path):
    files = sorted(out_dir.glob("*.md"))
    summary = {
        "date": get_today_str(),
        "total_files": len(files),
        "output_dir": str(out_dir),
        "files": [f.name for f in files],
        "generated_by": "scripts/collect_sources.py",
        "note": "本 summary 由脚本实时统计实际文件生成，修复旧版路径/命名不一致 bug",
    }
    (out_dir / "_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def main():
    backfill = "--backfill-subs" in sys.argv
    print("=" * 50)
    print(f"爆文采集 v3 — Reddit + YouTube — {get_today_str()}")
    print("=" * 50)
    out_dir = get_today_dir()
    print(f"输出目录: {out_dir}")

    if backfill:
        backfill_youtube_subs(out_dir)
        write_summary(out_dir)
        return

    seen = load_seen_urls(out_dir)
    print(f"已存在去重 URL 数: {len(seen)}")
    start_idx = existing_files_count(out_dir)
    print(f"起始编号: {start_idx + 1}")

    n_r = collect_reddit(out_dir, seen, start_idx)
    n_y = collect_youtube(out_dir, seen, start_idx + n_r)

    write_summary(out_dir)
    print(f"\n{'='*50}")
    print(f"采集完成: Reddit +{n_r}  YouTube +{n_y}  →  {out_dir}")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
