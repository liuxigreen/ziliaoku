#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
X/Twitter 内容源采集脚本 — 走 opencli Edge 登录态免费直采（2026-07-13 打通）

  search : 按赛道关键词搜高互动帖 → 正文 collect 源（data/raw/）
  watch  : 读 data/x_watchlist.md 盯人（优质作者最新推文）→ 正文 collect 源

免费直采依据：opencli 引擎（C:\\Users\\liuxi\\.opencli）内置 twitter CLI，走本机 Edge
浏览器登录态（cookie），不消耗 firecrawl / agentkey 付费额度。firecrawl 仅留作兜底。

前置（一次性，已完成）：
- Edge 已装 opencli Browser Bridge 扩展并登录 x.com（账号 @AdelaideMilne1）
- Edge 的 profile alias = edge（contextId wwwrh6sz）；Chrome 是 kzbaq3xs（登小红书）
- ⚠️ 两个 profile 同时连着，twitter 子命令必须显式 --profile edge，否则报
  BROWSER_CONNECT: Multiple Browser Bridge profiles

用法：
  python scripts/collect_twitter.py --mode search \
      --queries "AI agent workflow,MCP servers,Claude Code tips" --top-n 5
  python scripts/collect_twitter.py --mode watch            # 读 data/x_watchlist.md
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

# Windows GBK 编码防护：管道/重定向输出时 stdout 默认 GBK，✓/↗ 等符号会抛
# UnicodeEncodeError 中断脚本。强制 utf-8（Python 3.7+）。
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

WORKFLOW_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = WORKFLOW_DIR / "data" / "raw"
TITLES_POOL = WORKFLOW_DIR / "data" / "titles_pool.jsonl"
WATCHLIST = WORKFLOW_DIR / "data" / "x_watchlist.md"

DEFAULT_PROFILE = "edge"


def resolve_opencli():
    """定位 opencli 可执行文件。Windows 下全局命令是 opencli.cmd，
    subprocess 用 list 调用时找不到裸 opencli，须显式给 .cmd 全路径。"""
    for name in ("opencli", "opencli.cmd", "opencli.exe"):
        p = shutil.which(name)
        if p:
            return p
    # 兜底：Node 全局目录常见位置
    candidates = [
        Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "nodejs" / "node_global" / "opencli.cmd",
        Path(os.environ.get("APPDATA", "")) / "npm" / "opencli.cmd",
    ]
    for c in candidates:
        if c.exists():
            return str(c)
    return "opencli"


OPENCLI = resolve_opencli()

# 高互动阈值：超过则标题进 titles_pool 作为信号（英文源头一手信号）
SIGNAL_MIN_LIKES = 300
SIGNAL_MIN_VIEWS = 20000

# 软广/卖课过滤词：命中则只进 titles_pool 不入正文（分流纪律）
SOFT_AD_PAT = re.compile(
    r"(comment\s+['\"]?\w+['\"]?\s+(and\s+)?i'?ll\s+(dm|send))|"
    r"(评论\s*\S+\s*(送|领))|(私信\s*\S+\s*(送|领))|(link in bio)|(点赞关注)",
    re.I,
)


def get_today_str():
    tz = timezone(timedelta(hours=8))
    return datetime.now(tz).strftime("%Y-%m-%d")


def get_today_dir():
    d = RAW_DIR / get_today_str()
    d.mkdir(parents=True, exist_ok=True)
    return d


def run_twitter(args, profile):
    """调 opencli twitter 子命令，返回解析后的 JSON（list）。失败返回 []。"""
    cmd = [OPENCLI, "--profile", profile, "twitter"] + args + ["-f", "json"]
    try:
        proc = subprocess.run(
            cmd, capture_output=True, text=True, encoding="utf-8", timeout=120
        )
    except FileNotFoundError:
        print(f"  [opencli] 找不到 opencli 命令，请确认已全局安装并在 PATH 中")
        return []
    except subprocess.TimeoutExpired:
        print(f"  [opencli] 超时: {' '.join(args)}")
        return []
    out = (proc.stdout or "").strip()
    if not out:
        err = (proc.stderr or "").strip()
        print(f"  [opencli] 无输出: {' '.join(args)}  {err[:200]}")
        return []
    # 输出可能带日志前缀，截取首个 [ 到末尾的 ]
    lb, rb = out.find("["), out.rfind("]")
    if lb == -1 or rb == -1:
        print(f"  [opencli] 非 JSON 输出: {out[:200]}")
        return []
    try:
        data = json.loads(out[lb:rb + 1])
        return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        print(f"  [opencli] JSON 解析失败: {out[:200]}")
        return []


def as_int(v):
    try:
        return int(str(v).replace(",", ""))
    except Exception:
        return 0


def is_soft_ad(text):
    return bool(SOFT_AD_PAT.search(text or ""))


def sanitize(s):
    return (s or "").replace('"', "'").replace("\n", " ").strip()


def slug_author(author):
    return re.sub(r"[^A-Za-z0-9_]", "", author or "unknown") or "unknown"


def write_tweet_md(out_dir, idx, tw, source_type, query=None):
    author = tw.get("author", "unknown")
    text = tw.get("text", "")
    likes = as_int(tw.get("likes"))
    views = as_int(tw.get("views"))
    fname = f"{idx:02d}_x_{slug_author(author)}.md"
    quoted = tw.get("quoted_tweet") or {}
    quoted_block = ""
    if quoted and quoted.get("text"):
        quoted_block = (
            f"\n## 引用推文（@{quoted.get('author', '')}）\n\n> "
            f"{quoted.get('text', '').strip()}\n\n{quoted.get('url', '')}\n"
        )
    content = f"""---
title: "{sanitize(text)[:70]}"
author: "{author}"
platform: x
source: twitter
source_type: {source_type}
source_platform: x
url: "{tw.get('url', '')}"
tweet_id: "{tw.get('id', '')}"
published: "{tw.get('created_at', '')}"
collected: "{get_today_str()}"
likes: {likes}
views: {views}
has_media: {str(tw.get('has_media', False)).lower()}
media_urls: "{', '.join(tw.get('media_urls', []) or [])}"
query: "{sanitize(query) if query else ''}"
bio: "{sanitize(tw.get('bio', ''))}"
---

# @{author}

> {sanitize(tw.get('bio', ''))}

**Likes**: {likes} ｜ **Views**: {views} ｜ **发布**: {tw.get('created_at', '')} ｜ **链接**: {tw.get('url', '')}

## 正文

{text}
{quoted_block}"""
    (out_dir / fname).write_text(content, encoding="utf-8")
    return fname


def append_title_signal(tw, source_type, query=None):
    """高互动帖标题进 titles_pool.jsonl 作信号。"""
    text = tw.get("text", "")
    # 取首个有意义（非纯链接/非空）的行作标题，避免 t.co 短链当标题
    first_line = ""
    for ln in text.strip().splitlines():
        ln = ln.strip()
        if ln and not re.fullmatch(r"https?://\S+", ln):
            first_line = ln[:120]
            break
    if not first_line:
        first_line = text.strip().split("\n", 1)[0][:120]
    entry = {
        "platform": "x",
        "title": first_line,
        "author": tw.get("author", ""),
        "likes": as_int(tw.get("likes")),
        "views": as_int(tw.get("views")),
        "url": tw.get("url", ""),
        "date": get_today_str(),
        "source": source_type,
    }
    if query:
        entry["query"] = query
    with open(TITLES_POOL, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def is_high_engagement(tw):
    return as_int(tw.get("likes")) >= SIGNAL_MIN_LIKES or \
           as_int(tw.get("views")) >= SIGNAL_MIN_VIEWS


def collect_search(out_dir, start_idx, queries, top_n, profile):
    idx = start_idx
    collected, signals = 0, 0
    seen_ids = set()
    for q in queries:
        print(f"\n[search] «{q}» (top-by-engagement {top_n})")
        tweets = run_twitter(
            ["search", q, "--product", "top", "--limit", "20",
             "--top-by-engagement", str(top_n)],
            profile,
        )
        for tw in tweets:
            tid = tw.get("id")
            if not tid or tid in seen_ids:
                continue
            seen_ids.add(tid)
            text = tw.get("text", "")
            # 软广/卖课 → 只进标题信号，不入正文
            if is_soft_ad(text):
                append_title_signal(tw, "twitter_search_softad", q)
                signals += 1
                print(f"    ~ 软广只取标题: @{tw.get('author')} ({as_int(tw.get('likes'))}♥)")
                continue
            idx += 1
            fname = write_tweet_md(out_dir, idx, tw, "twitter_search", q)
            collected += 1
            print(f"    ✓ @{tw.get('author')} ({as_int(tw.get('likes'))}♥ / {as_int(tw.get('views'))}👁) → {fname}")
            if is_high_engagement(tw):
                append_title_signal(tw, "twitter_search", q)
                signals += 1
    print(f"\n[search] 完成：入正文 {collected} 条，标题信号 {signals} 条")
    return collected


def load_watchlist():
    """读 data/x_watchlist.md，每行一个 handle（@可省），# 后为备注/注释行跳过。"""
    if not WATCHLIST.exists():
        print(f"  [watch] watchlist 不存在: {WATCHLIST}")
        print(f"          先创建并填入优质作者（每行一个，如 @0xCodez）")
        return []
    handles = []
    for line in WATCHLIST.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or line.startswith(">"):
            continue
        note = ""
        if "#" in line:
            line, note = line.split("#", 1)
        h = line.strip().lstrip("@").strip()
        if h:
            handles.append((h, note.strip()))
    return handles


def collect_watch(out_dir, start_idx, top_n, profile):
    handles = load_watchlist()
    if not handles:
        return 0
    print(f"\n[watch] watchlist 作者 {len(handles)} 个")
    idx = start_idx
    collected, signals = 0, 0
    for handle, note in handles:
        print(f"\n[watch] @{handle} {('— ' + note) if note else ''}")
        tweets = run_twitter(
            ["tweets", "--username", handle, "--limit", "10",
             "--top-by-engagement", str(top_n)],
            profile,
        )
        for tw in tweets:
            text = tw.get("text", "")
            if is_soft_ad(text):
                append_title_signal(tw, "twitter_watch_softad")
                signals += 1
                continue
            idx += 1
            fname = write_tweet_md(out_dir, idx, tw, "twitter_watchlist")
            collected += 1
            print(f"    ✓ ({as_int(tw.get('likes'))}♥ / {as_int(tw.get('views'))}👁) → {fname}")
            if is_high_engagement(tw):
                append_title_signal(tw, "twitter_watchlist")
                signals += 1
    print(f"\n[watch] 完成：入正文 {collected} 条，标题信号 {signals} 条")
    return collected


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["search", "watch"], default="search")
    ap.add_argument("--queries",
                    default="AI agent workflow,MCP servers,Claude Code tips",
                    help="逗号分隔的搜索词（search 模式）")
    ap.add_argument("--top-n", type=int, default=5,
                    help="每词/每人按互动取前 N 条")
    ap.add_argument("--profile", default=DEFAULT_PROFILE,
                    help="opencli Browser Bridge profile（默认 edge = 登 X 的 Edge）")
    args = ap.parse_args()

    print("=" * 50)
    print(f"X/Twitter 采集 — {get_today_str()} — mode={args.mode} — profile={args.profile}")
    print("=" * 50)

    out_dir = get_today_dir()
    start_idx = len(list(out_dir.glob("*_x_*.md")))

    if args.mode == "search":
        queries = [q.strip() for q in args.queries.split(",") if q.strip()]
        collect_search(out_dir, start_idx, queries, args.top_n, args.profile)
    else:
        collect_watch(out_dir, start_idx, args.top_n, args.profile)

    print(f"\n采集完成: X/Twitter → {out_dir}")


if __name__ == "__main__":
    main()
