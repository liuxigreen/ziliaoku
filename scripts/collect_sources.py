#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
爆文采集脚本 v3 — Reddit + YouTube（agent-reach / opencli 直采，含 transcript 字幕）
输出：data/raw/{YYYY-MM-DD}/{序号}_{platform}.md（与现有 schema 对齐）

频率纪律（用户强调）：
- Reddit 每条 query 之间 sleep 6s（opencli 驱动浏览器，防限频）
- YouTube 每个视频之间 sleep 5s，每个 query 之间 sleep 8s
- 单条 opencli 调用超时 90s；yt-dlp 字幕超时 150s

YouTube 字幕方案（v3.1 — opencli transcript 直采）：
- ✅ 主路径：opencli `youtube transcript`（agent 工具直采，无需 cookies，实测返回完整字幕 YAML）。
- 之前误判「transcript 超时/返回空」根因是 opencli 输出为 UTF-16，旧解码器按 GBK 解成乱码/空；
  现 _decode_output 按 BOM 检测 UTF-16 后已正常（实测 68KB 字幕，见 scripts/_verify_transcript.py）。
- 🔁 兜底：yt-dlp + cookies.txt（仅当 opencli 失败且用户已导出 cookies.txt 时走），保留不删。
- 结论：默认零配置即可采字幕，cookies.txt 不再是必选项。
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

# Windows GBK 编码防护：管道输出时 ✓ 等符号会抛 UnicodeEncodeError。强制 utf-8。
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

try:
    import yaml
except ImportError:
    print("[ERR] PyYAML 缺失，请装在 agent-reach venv")
    sys.exit(1)

# ── 路径 ──────────────────────────────────────────
WORKFLOW_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = WORKFLOW_DIR / "data" / "raw"
OPENCLI = r"C:\Program Files\nodejs\node_global\opencli.cmd"

# opencli 浏览器复用参数：persistent=跨命令复用同一浏览器(不新开窗口)，
# keep-tab=false=命令结束关掉该 tab(不累积)，window=foreground 可见(已验证稳定)。
# 默认不传时 opencli 走 ephemeral，每次都开一整套新 Chrome 窗口。
BROWSER_PERSIST_ARGS = ["--site-session", "persistent", "--keep-tab", "false", "--window", "foreground"]
YT_DLP = r"C:\Users\liuxi\.agent-reach-venv\Scripts\yt-dlp.exe"
COOKIES = WORKFLOW_DIR / "cookies.txt"          # 一次性导出，已 gitignore
YT_WATCHLIST = WORKFLOW_DIR / "data" / "youtube_watchlist.md"  # 订阅源头频道，优先于关键词泛搜

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
    ("AI side hustle passive income",    "信号源-副业标题公式"),  # 降级：副业不实采正文，仅信号参考
    ("AI content creation strategy",     "赛道3-自媒体"),
]
REDDIT_LIMIT = 4

# YouTube 采集原则（用户 2026-07-09 强调）：找源头，不采搬运。
# 中文 YouTube 多为搬运，真正源头一般是英语原创 → 查询词一律用英文（命中英语原创频道），
# 中文搬运由 classify_origin() 标记 suspect_repost 降权。订阅频道见 youtube_watchlist.md。
YT_QUERIES = [
    ("Claude Code workflow tips",        "赛道1-AI工具"),
    ("ComfyUI image generation workflow","赛道2-AI创作"),
    ("AI video generation Sora Kling",   "赛道2-AI视频"),
    ("n8n automation workflow tutorial", "赛道1/4-自动化"),
    ("content creator growth strategy",  "赛道3-自媒体"),
    ("AI side hustle one person business", "信号源-副业标题公式"),  # 降级：副业不实采正文，仅信号参考
]
YT_LIMIT = 2


def classify_origin(title: str, language: str | None) -> tuple[str, str]:
    """判别视频是英语源头还是疑似中文搬运。返回 (origin_flag, lang_hint)。
    - english_source：源头优先（英语原创，找源头命中）
    - suspect_repost：疑似中文搬运，降权
    - unknown：无法判定
    yt-dlp 有 language 字段时优先用；opencli 降级路径靠标题 CJK 占比启发式。
    """
    if language:
        lang = language.lower()
        if lang.startswith("zh"):
            return ("suspect_repost", "zh")
        if lang.startswith("en"):
            return ("english_source", "en")
    if title:
        cjk = len(re.findall(r"[一-鿿]", title))
        ratio = cjk / max(len(title.strip()), 1)
        if ratio < 0.15:
            return ("english_source", "en")
        if ratio > 0.4:
            return ("suspect_repost", "zh")
        return ("unknown", "mixed")
    return ("unknown", "unknown")


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


def _decode_output(b: bytes) -> str:
    """opencli 输出为 UTF-16 LE（带 BOM），必须按 BOM 判断解码，否则 GBK/UTF-8 都会乱码。
    无 BOM 的按 UTF-8 解，失败再 replace。"""
    if not b:
        return ""
    if b[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return b.decode("utf-16", errors="replace")
    try:
        return b.decode("utf-8")
    except Exception:
        return b.decode("utf-8", errors="replace")


def run_opencli(args: list, timeout: int = CALL_TIMEOUT) -> str:
    try:
        r = subprocess.run(
            [OPENCLI] + args + BROWSER_PERSIST_ARGS,
            capture_output=True, shell=True, timeout=timeout
        )
        return _decode_output(r.stdout)
    except subprocess.TimeoutExpired:
        return ""
    except Exception as e:
        print(f"  [opencli-error] {e}")
        return ""


def run_ytdlp(args: list, timeout: int = YT_SUB_TIMEOUT) -> subprocess.CompletedProcess:
    """yt-dlp 是真实 exe，用 shell=False 避免路径空格引号问题"""
    return subprocess.run([YT_DLP] + args, capture_output=True, text=True,
                          encoding="utf-8", errors="replace",
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


def fetch_transcript_opencli(url: str, prefer_lang: str = None) -> str:
    """opencli `youtube transcript` 直采字幕（agent 工具，无需 cookies）。
    返回纯字幕文本（合并各段 text，丢弃时间戳/章节标记）；失败返回 ""。
    """
    args = ["youtube", "transcript", url, "-f", "yaml", "--mode", "grouped"]
    if prefer_lang:
        args += ["--lang", prefer_lang]
    raw = run_opencli(args, timeout=YT_SUB_TIMEOUT)
    if not raw:
        return ""
    segs = parse_yaml_list(raw)
    if not segs:
        return ""
    parts = []
    for s in segs:
        t = (s.get("text") or "").strip()
        if t:
            parts.append(t)
    return "\n".join(parts)


def fetch_subtitle_ytdlp(url: str, prefer_lang: str = None) -> str:
    """
    兜底：yt-dlp + cookies.txt 抓字幕（仅当 opencli 失败且用户已导出 cookies.txt 时走）。
    优先 prefer_lang（视频原始语言），缺失按 YT_SUB_PREF 兜底。
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


def fetch_transcript(url: str, prefer_lang: str = None) -> str:
    """抓字幕总入口：主路径 opencli transcript（agent 工具直采，无需 cookies），
    兜底 yt-dlp + cookies.txt（可选）。返回纯字幕文本；失败返回 ""。"""
    txt = fetch_transcript_opencli(url, prefer_lang)
    if txt and len(txt) > 30:
        return txt
    if COOKIES.exists():
        return fetch_subtitle_ytdlp(url, prefer_lang)
    return ""


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


# ── YouTube 采集（opencli 直采：搜索发现 + transcript 字幕，无需 cookies）──
def collect_youtube(out_dir: Path, seen: set, start_idx: int):
    print(f"\n[YouTube] 开始（opencli 直采：搜索发现 + transcript 字幕），"
          f"{len(YT_QUERIES)} query × {YT_LIMIT} 视频")
    count = 0
    idx = start_idx
    for q, track in YT_QUERIES:
        print(f"  → youtube: {q}  [{track}]")
        raw = run_opencli(["youtube", "search", q, "-f", "yaml",
                           "--limit", str(YT_LIMIT)])
        items = parse_yaml_list(raw)
        if not items:
            print("    (无数据/解析失败，跳过)")
            time.sleep(YT_QUERY_GAP)
            continue

        for it in items:
            url = (it.get("url") or "").strip()
            if not url or url in seen:
                continue
            title = (it.get("title") or "Unknown").strip()
            channel = (it.get("channel") or "").strip()
            views = (it.get("views") or "").strip()
            duration = (it.get("duration") or "").strip()
            published = (it.get("published") or "").strip()
            seen.add(url)

            # 字幕：opencli transcript 主路径，yt-dlp+cookies 兜底
            sub_ok = False
            transcript = fetch_transcript(url, None)
            if transcript and len(transcript) > 30:
                sub_ok = True

            if sub_ok:
                body = f"# 字幕正文（来源：opencli transcript）\n\n{transcript[:8000]}"
            else:
                body = (f"# 视频信息（字幕不可用，降级）\n\n"
                        f"**频道**：{channel}\n**时长**：{duration}\n**观看**：{views}\n\n"
                        f"（opencli transcript 未返回字幕，可后续用 --backfill-subs 重试）")

            origin_flag, lang_hint = classify_origin(title, None)
            idx += 1
            safe_ch = re.sub(r"[^\w一-龥]", "", channel)[:12] or "yt"
            fname = f"{idx:02d}_yt_{safe_ch}.md"
            vid = ""
            m = re.search(r"[?&]v=([\w-]+)", url)
            if m:
                vid = m.group(1)
            content = f"""---
title: "{title.replace(chr(34), "'")}"
author: "{channel}"
platform: YouTube
source: opencli youtube
source_type: aggregator_discovery
source_platform: youtube
channel: "{channel}"
views: "{views}"
duration: "{duration}"
published: "{published}"
video_id: "{vid}"
url: "{url}"
subtitle_source: "opencli-transcript"
subtitle_available: {str(sub_ok).lower()}
origin_flag: "{origin_flag}"
lang_hint: "{lang_hint}"
query_track: "{track}"
collected: "{get_today_str()}"
---

{body}
"""
            (out_dir / fname).write_text(content, encoding="utf-8")
            count += 1
            print(f"    ✓ {title[:30]} | 字幕:{sub_ok}")
            time.sleep(YT_VIDEO_GAP)
        time.sleep(YT_QUERY_GAP)
    print(f"[YouTube] 完成，新增 {count} 条")
    return count


def collect_youtube_watchlist(out_dir: Path, seen: set, start_idx: int):
    """按订阅频道(youtube_watchlist.md)优先抓源头视频，优先于关键词泛搜找源头。
    订阅的频道默认是源头（英语原创），标题明显中文搬运也仍入库但标记。
    发现+字幕均走 opencli（无需 cookies）。
    """
    if not YT_WATCHLIST.exists():
        print("\n[YouTube-WL] 无 youtube_watchlist.md，跳过订阅采集")
        return 0
    entries = []
    for line in YT_WATCHLIST.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in re.split(r"\s*\|\s*", line)]
        handle = parts[0]
        track = parts[1] if len(parts) > 1 else "订阅源头"
        if not handle:
            continue
        entries.append((handle, track))
    if not entries:
        print("\n[YouTube-WL] watchlist 为空，跳过")
        return 0

    print(f"\n[YouTube-WL] 订阅频道采集（opencli 直采），{len(entries)} 个频道")
    count = 0
    idx = start_idx
    for handle, track in entries:
        print(f"  → channel: {handle}  [{track}]")
        # opencli 搜 @handle（YouTube 搜 @handle 多返回该频道视频）
        raw = run_opencli(["youtube", "search", handle, "-f", "yaml",
                           "--limit", "3"])
        items = parse_yaml_list(raw)

        if not items:
            print("    (无数据/解析失败，跳过)")
            time.sleep(YT_QUERY_GAP)
            continue

        for it in items:
            url = (it.get("url") or "").strip()
            if not url or url in seen:
                continue
            seen.add(url)
            title = (it.get("title") or "Unknown").strip()
            channel = (it.get("channel") or it.get("uploader") or handle).strip()
            language = it.get("language") or None
            origin_flag, lang_hint = classify_origin(title, language)
            # 订阅频道默认源头；unknown 也按源头处理（用户亲自订阅=已背书）
            if origin_flag == "unknown":
                origin_flag = "english_source"

            # 字幕：opencli transcript 主路径，yt-dlp+cookies 兜底
            sub_ok = False
            transcript = fetch_transcript(url, language)
            if transcript and len(transcript) > 30:
                sub_ok = True
            if sub_ok:
                body = (f"# 字幕正文（来源：opencli transcript，{lang_hint}）\n\n"
                        f"{transcript[:8000]}")
            else:
                desc = (it.get("description") or "").strip()
                body = (f"# 视频描述（字幕不可用，降级，{lang_hint}）\n\n{desc[:4000]}")

            idx += 1
            safe_ch = re.sub(r"[^\w一-龥]", "", channel)[:12] or "ytwl"
            fname = f"{idx:02d}_ytwl_{safe_ch}.md"
            content = f"""---
title: "{title.replace(chr(34), "'")}"
author: "{channel}"
platform: YouTube
source: youtube_watchlist
source_type: watchlist
source_platform: youtube
channel: "{channel}"
url: "{url}"
subtitle_source: "opencli-transcript"
subtitle_available: {str(sub_ok).lower()}
origin_flag: "{origin_flag}"
lang_hint: "{lang_hint}"
query_track: "{track}"
collected: "{get_today_str()}"
---

{body}
"""
            (out_dir / fname).write_text(content, encoding="utf-8")
            count += 1
            print(f"    ✓ {title[:30]} | origin:{origin_flag} 字幕:{sub_ok}")
            time.sleep(YT_VIDEO_GAP)
        time.sleep(YT_QUERY_GAP)
    print(f"[YouTube-WL] 完成，新增 {count} 条")
    return count


def backfill_youtube_subs(out_dir: Path):
    """已有 yt_*/ytwl_* 文件补全字幕（opencli transcript 主路径，yt-dlp+cookies 兜底）。
    保留 frontmatter，重写正文为字幕正文。"""
    files = sorted(out_dir.glob("*_yt_*.md")) + sorted(out_dir.glob("*_ytwl_*.md"))
    print(f"\n[backfill] 补全 {len(files)} 个 YouTube 文件字幕（opencli transcript）")
    done = 0
    for f in files:
        txt = f.read_text(encoding="utf-8")
        m = re.search(r"^url:\s*\"?([^\"\n]+)\"?", txt, re.MULTILINE)
        if not m:
            continue
        url = m.group(1).strip()
        transcript = fetch_transcript(url, None)
        if not transcript or len(transcript) <= 30:
            print(f"    ~ 跳过（无字幕）{f.name}")
            continue
        # 拆 frontmatter / body
        parts = txt.split("\n---\n", 1)
        if len(parts) != 2:
            continue
        fm, _ = parts
        if re.search(r"^subtitle_available:", fm, re.MULTILINE):
            fm = re.sub(r"subtitle_available:.*", "subtitle_available: true", fm)
        else:
            fm += "\nsubtitle_available: true"
        if re.search(r"^subtitle_source:", fm, re.MULTILINE):
            fm = re.sub(r"subtitle_source:.*", 'subtitle_source: "opencli-transcript"', fm)
        else:
            fm += '\nsubtitle_source: "opencli-transcript"'
        new_body = f"# 字幕正文（来源：opencli transcript）\n\n{transcript[:8000]}"
        f.write_text(fm + "\n---\n\n" + new_body, encoding="utf-8")
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
    n_wl = collect_youtube_watchlist(out_dir, seen, start_idx + n_r)
    n_y = collect_youtube(out_dir, seen, start_idx + n_r + n_wl)

    write_summary(out_dir)
    print(f"\n{'='*50}")
    print(f"采集完成: Reddit +{n_r}  YouTube +{n_y}  →  {out_dir}")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
