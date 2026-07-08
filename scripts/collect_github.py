#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub 内容源采集脚本 — 三路通道
  1) trending  : github.com/trending 抓「增长速度快的」库 → 风向标 signal（data/signal/）
  2) topic     : 发现高 star AI 库 + 抓 README → 正文 collect 源（data/raw/，阈值默认 2000★）
  3) watch     : 读取 data/github_watchlist.md 用户个人收藏库 → 绕过阈值，直接 collect
接入依据：reviews/2026-07-08_github_source.md + 用户 2026-07-08 指令（加风向标/增长快/个人收藏/2000阈值）

频率纪律（GitHub API 匿名限速：core 60/h，search 10/min）：
- trending 走 HTML 刮取（无 API 消耗）；topic/watch 走 API，每库 sleep 2s，每日 1 次足够。
- 用户个人收藏库数量有限，不会触限速。
"""
import argparse
import json
import re
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

WORKFLOW_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = WORKFLOW_DIR / "data" / "raw"
SIGNAL_DIR = WORKFLOW_DIR / "data" / "signal"
WATCHLIST = WORKFLOW_DIR / "data" / "github_watchlist.md"
TOKEN_FILE = WORKFLOW_DIR / "config" / "github_token.txt"   # 含登录态，已被 .gitignore 屏蔽
API_BASE = "https://api.github.com"
# GitHub API 强制要求 Accept header，否则 403。curl 默认带 Accept:*/* 故能用，urllib 必须显式加。
UA = {
    "User-Agent": "Mozilla/5.0 (compatible; ziliaoku-collect/1.0)",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}

# 默认配置（可用命令行覆盖）
TOPICS = ["ai-agents", "rag", "prompt-engineering", "llm", "agentic-ai"]
TOP_N = 8
MIN_STARS = 2000          # 用户指令：2000 以上作为高 star 正文源门槛
ACTIVE_DAYS = 180
SIGNAL_MIN_GAIN = 50      # 风向标：当日/周新增 star 超过此值才值得报

AI_KEYWORDS = ["ai", "agent", "llm", "gpt", "clip", "video", "image", "diffusion",
               "rag", "prompt", "model", "ml", "deep", "neural", "automation",
               "workflow", "assistant", "chatbot", "embedding", "fine-tun", "agentic"]


def get_today_str():
    tz = timezone(timedelta(hours=8))
    return datetime.now(tz).strftime("%Y-%m-%d")


def get_today_dir():
    d = RAW_DIR / get_today_str()
    d.mkdir(parents=True, exist_ok=True)
    return d


def gh_json(url):
    req = Request(url, headers=UA)
    try:
        with urlopen(req, timeout=20) as r:
            return json.loads(r.read().decode("utf-8"))
    except HTTPError as e:
        if e.code == 403:
            print(f"  [github-api] 403 限速: {url}")
        else:
            print(f"  [github-api] HTTP {e.code}: {url}")
        return None
    except URLError as e:
        print(f"  [github-api] 网络错误: {e}")
        return None


def load_token(cli_token):
    """Token 解析优先级：命令行 --token > 环境变量 GITHUB_TOKEN > config/github_token.txt
    绝不回显、绝不以任何方式写入版本库（.gitignore 已屏蔽文件）。"""
    if cli_token:
        return cli_token.strip()
    env = __import__("os").environ.get("GITHUB_TOKEN")
    if env:
        return env.strip()
    if TOKEN_FILE.exists():
        return TOKEN_FILE.read_text(encoding="utf-8").strip()
    return None


def gh_json_auth(url, token):
    """带 token 的 GitHub API 调用（用于读取 /user/starred 等需授权的端点）。"""
    headers = dict(UA)
    headers["Authorization"] = f"Bearer {token}"
    req = Request(url, headers=headers)
    try:
        with urlopen(req, timeout=20) as r:
            return json.loads(r.read().decode("utf-8"))
    except HTTPError as e:
        if e.code == 401:
            print("  [github-auth] 401 Token 无效或权限不足（需 read:user 权限）")
        elif e.code == 403:
            print("  [github-auth] 403 限速或 token 权限不足")
        else:
            print(f"  [github-auth] HTTP {e.code}: {url}")
        return None
    except URLError as e:
        print(f"  [github-auth] 网络错误: {e}")
        return None


def fetch_text(url):
    req = Request(url, headers=UA)
    try:
        with urlopen(req, timeout=20) as r:
            return r.read().decode("utf-8", errors="ignore")
    except Exception:
        return ""


def fetch_readme(full, branch):
    owner, repo = full.split("/")
    for name in ("README.md", "readme.md", "Readme.md"):
        txt = fetch_text(
            f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{name}"
        )
        if txt and len(txt) > 100:
            return txt
    return ""


def fetch_readme_auth(full, branch, token):
    """带 token 的 README 抓取（走 raw.githubusercontent，附带 Authorization 头部，
    享受 5000/h 鉴权额度，避免匿名限速）。"""
    owner, repo = full.split("/")
    hdr = dict(UA)
    if token:
        hdr["Authorization"] = f"Bearer {token}"
    for name in ("README.md", "readme.md", "Readme.md"):
        url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{name}"
        req = Request(url, headers=hdr)
        try:
            with urlopen(req, timeout=20) as r:
                txt = r.read().decode("utf-8", errors="ignore")
            if txt and len(txt) > 100:
                return txt
        except Exception:
            continue
    return ""


def days_since(iso):
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        return (datetime.now(timezone.utc) - dt).days
    except Exception:
        return 9999


def is_ai_related(desc, topics):
    blob = (desc + " " + " ".join(topics)).lower()
    return any(k in blob for k in AI_KEYWORDS)


# ─────────────────────────── 1) trending（风向标/增长快） ───────────────────────────
def collect_trending(out_signal_dir, since="daily", top=None):
    period_label = {"daily": "今日", "weekly": "本周"}.get(since, since)
    url = f"https://github.com/trending?since={since}"
    html = fetch_text(url)
    if not html:
        print(f"  [trending] 刮取失败: {url}")
        return 0
    articles = re.findall(
        r'<article[^>]*class="[^"]*Box-row[^"]*"[^>]*>(.*?)</article>',
        html, re.S)
    entries = []
    for a in articles:
        # 提取仓库 owner/repo：抓首个形如 href="/owner/repo" 的链接，跳过 login/stargazers 等
        repo = None
        for m in re.finditer(r'href="/(?!login|stargazers|forks|fork|subscribe|watch|explore|topics)[^"/]+/[^"/]+"', a):
            cand = m.group(0).strip('"').lstrip('href="/').rstrip('/')
            if cand.count("/") == 1 and "/" in cand:
                repo = cand
                break
        if not repo or repo.count("/") != 1:
            continue
        m_desc = re.search(r'<p[^>]*>(.*?)</p>', a, re.S)
        desc = re.sub(r"<[^>]+>", "", m_desc.group(1)).strip() if m_desc else ""
        m_gain = re.search(r"([\d,]+)\s+stars\s+(today|this week)", a)
        gain = int(m_gain.group(1).replace(",", "")) if m_gain else 0
        m_stars = re.search(r"/stargazers\"[^>]*>.*?</svg>\s*([\d,]+)", a, re.S)
        stars = int(m_stars.group(1).replace(",", "")) if m_stars else 0
        entries.append({"repo": repo, "stars": stars, "gain": gain,
                        "gain_period": since, "desc": desc})
    # 按增长量排序，取增长最快的
    entries.sort(key=lambda e: e["gain"], reverse=True)
    if top:
        entries = entries[:top]

    out_signal_dir.mkdir(parents=True, exist_ok=True)
    fpath = out_signal_dir / f"{get_today_str()}_github_trending_{since}.jsonl"
    kept = []
    for e in entries:
        if e["gain"] < SIGNAL_MIN_GAIN:
            continue
        entry = {
            "source": "github_trending",
            "source_type": "signal",
            "repo": e["repo"],
            "url": f"https://github.com/{e['repo']}",
            "stars": e["stars"],
            "gain": e["gain"],
            "gain_period": e["gain_period"],
            "period_label": period_label,
            "description": e["desc"],
            "ai_related": is_ai_related(e["desc"], []),
            "reason": f"GitHub {period_label}增长最快 (+{e['gain']}★)",
            "collected": get_today_str(),
        }
        kept.append(entry)
    with open(fpath, "w", encoding="utf-8") as f:
        for e in kept:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    print(f"[trending] {since}: 刮到 {len(entries)} 个，报告 {len(kept)} 个增长快信号 → {fpath}")
    for e in kept[:10]:
        print(f"    ↗ {e['repo']}  +{e['gain']}★ ({period_label})  {e['stars']}★总  {'[AI]' if e['ai_related'] else ''}")
    return len(kept)


# ─────────────────────────── 2) topic（高 star 正文源） ───────────────────────────
def collect_topic(out_dir, start_idx, topics, top_n, min_stars):
    print(f"\n[GitHub] 发现高 star 库，topics={topics}, TOP_N={top_n}, MIN_STARS={min_stars}")
    count = 0
    idx = start_idx
    # 去重：跳过本目录已存在的同库（防同日重采，如跨 topic 重复 / 重跑）
    seen = {p.name.split("_github_", 1)[1].replace(".md", "")
            for p in out_dir.glob("*_github_*.md")}
    for topic in topics:
        q = f"topic:{topic}"
        url = f"{API_BASE}/search/repositories?q={q}&sort=stars&order=desc&per_page={top_n}"
        data = gh_json(url)
        if not data or "items" not in data:
            print(f"  ~ topic {topic} 无数据/限速，跳过")
            time.sleep(3)
            continue
        for item in data["items"]:
            full = item.get("full_name", "")
            stars = item.get("stargazers_count", 0)
            pushed = item.get("pushed_at", "")
            desc = item.get("description") or ""
            lang = item.get("language") or ""
            if full in seen:
                continue
            if stars < min_stars:
                continue
            if days_since(pushed) > ACTIVE_DAYS:
                continue
            seen.add(full)
            repo = gh_json(f"{API_BASE}/repos/{full}")
            branch = (repo or {}).get("default_branch", "main")
            readme_text = fetch_readme(full, branch)
            if not readme_text:
                readme_text = fetch_readme(full, "main") or fetch_readme(full, "master")
            if not readme_text or len(readme_text) < 100:
                print(f"    ~ {full} 无 README 或太短，跳过")
                time.sleep(2)
                continue
            idx += 1
            repo_name = full.split("/")[-1]
            fname = f"{idx:02d}_github_{repo_name}.md"
            content = f"""---
title: "{full}"
author: "{full.split('/')[0]}"
platform: github
source: github_api
source_type: github_discovery
source_platform: github
stars: {stars}
forks: {item.get('forks_count', 0)}
language: "{lang}"
topics: "{', '.join(item.get('topics', [])[:10])}"
description: "{desc.replace(chr(34), "'")}"
pushed_at: "{pushed}"
url: "https://github.com/{full}"
collected: "{get_today_str()}"
---

# {full}

> {desc}

**Stars**: {stars} ｜ **Forks**: {item.get('forks_count', 0)} ｜ **Language**: {lang} ｜ **最近活跃**: {pushed}

## README

{readme_text[:9000]}
"""
            (out_dir / fname).write_text(content, encoding="utf-8")
            count += 1
            print(f"    ✓ {full} ({stars}★, {lang})")
            time.sleep(2)
        time.sleep(3)
    print(f"[GitHub] topic 完成，新增 {count} 条")
    return count


# ─────────────────────────── 3) watch（个人收藏库，绕过阈值） ───────────────────────────
def collect_watch(out_dir, start_idx):
    if not WATCHLIST.exists():
        print(f"  [watch] 收藏库文件不存在: {WATCHLIST}")
        return 0
    lines = [l.strip() for l in WATCHLIST.read_text(encoding="utf-8").splitlines()]
    repos = []
    for l in lines:
        if not l or l.startswith("#"):
            continue
        note = ""
        if "#" in l:
            l, note = l.split("#", 1)
            note = note.strip()
        l = l.strip().rstrip("/")
        l = re.sub(r"^https?://github\.com/", "", l).strip()
        if l.count("/") == 1:
            repos.append((l, note))
    print(f"\n[watch] 个人收藏库: 解析到 {len(repos)} 个")
    count = 0
    idx = start_idx
    # 去重：跳过本目录已存在的同库
    seen = {p.name.split("_github_", 1)[1].replace(".md", "")
            for p in out_dir.glob("*_github_*.md")}
    for full, note in repos:
        repo = gh_json(f"{API_BASE}/repos/{full}")
        if not repo:
            print(f"    ~ {full} 拉不到元数据，跳过")
            time.sleep(2)
            continue
        stars = repo.get("stargazers_count", 0)
        branch = repo.get("default_branch", "main")
        desc = repo.get("description") or ""
        lang = repo.get("language") or ""
        pushed = repo.get("pushed_at", "")
        readme_text = fetch_readme(full, branch)
        if not readme_text:
            readme_text = fetch_readme(full, "main") or fetch_readme(full, "master")
        idx += 1
        repo_name = full.split("/")[-1]
        fname = f"{idx:02d}_github_{repo_name}.md"
        content = f"""---
title: "{full}"
author: "{full.split('/')[0]}"
platform: github
source: github_watchlist
source_type: github_curated
source_platform: github
stars: {stars}
forks: {repo.get('forks_count', 0)}
language: "{lang}"
description: "{desc.replace(chr(34), "'")}"
pushed_at: "{pushed}"
curated_note: "{note.replace(chr(34), "'")}"
url: "https://github.com/{full}"
collected: "{get_today_str()}"
---

# {full}

> {desc}

**Stars**: {stars} ｜ **Forks**: {repo.get('forks_count', 0)} ｜ **Language**: {lang} ｜ **最近活跃**: {pushed}

**用户收藏备注**: {note}

## README

{readme_text[:9000]}
"""
        (out_dir / fname).write_text(content, encoding="utf-8")
        count += 1
        print(f"    ✓ {full} ({stars}★, {lang}) {('— ' + note) if note else ''}")
        time.sleep(2)
    print(f"[watch] 完成，新增 {count} 条（个人收藏，绕过 star 阈值）")
    return count


def is_offtopic(desc, topics, name):
    """强信号判定：web3/加密/代理/VPN/eSIM/ZK/区块链语言 等明显偏离
    'AI 实操 / 内容工作流 / 工具推荐' 定位的，直接 discard。"""
    t = f"{desc} {' '.join(topics)} {name}".lower()
    OFF = ["web3", "defi", "crypto", "ethereum", "solana", "vless", "trojan",
           "shadowsocks", "esim", "zk ", "zero-knowledge", "nft", "src20",
           "erc20", " mint", "perp", "smart contract", "blockchain", "sway",
           "react-day-picker", "proof-of", "sismo", "space and time"]
    return any(k in t for k in OFF)


def collect_starred(out_dir, start_idx, token):
    """从当前登录用户的 GitHub Starred 列表拉取收藏库 → 相关性筛选 → 符合的 collect。
    - 端点 GET /user/starred（需 read:user 权限的 token）；token 鉴权额度 5000/h。
    - 直接复用 starred 返回的元数据，不再额外调 /repos/{full}（省 API）。
    - README 抓取走 gh_json_auth（带 token，不触匿名 60/h 限速）。
    - 强偏离定位的（web3/代理/eSIM/ZK 等）判 discard，不抓 README、不入 raw。"""
    if not token:
        print("  [starred] 未提供 token（--token / GITHUB_TOKEN / config/github_token.txt），跳过")
        return 0
    print(f"\n[starred] 读取你的 GitHub Starred 列表（需 read:user 权限）")
    all_repos = []
    page = 1
    while True:
        url = f"{API_BASE}/user/starred?per_page=100&page={page}"
        data = gh_json_auth(url, token)
        if not isinstance(data, list) or not data:
            break
        all_repos.extend(data)
        if len(data) < 100:
            break
        page += 1
        time.sleep(1)
    print(f"  [starred] 共拉到 {len(all_repos)} 个 starred 库")

    count = 0
    idx = start_idx
    discarded = []
    seen = {p.name.split("_github_", 1)[1].replace(".md", "")
            for p in out_dir.glob("*_github_*.md")}
    for item in all_repos:
        full = item.get("full_name", "")
        if not full or full in seen:
            continue
        stars = item.get("stargazers_count", 0)
        branch = item.get("default_branch", "main")
        desc = item.get("description") or ""
        lang = item.get("language") or ""
        pushed = item.get("pushed_at", "")
        topics = item.get("topics", []) or []
        if is_offtopic(desc, topics, full):
            discarded.append((full, stars, desc[:60]))
            continue
        readme_text = fetch_readme_auth(full, branch, token) or \
                      fetch_readme_auth(full, "main", token) or \
                      fetch_readme_auth(full, "master", token)
        idx += 1
        repo_name = full.split("/")[-1]
        fname = f"{idx:02d}_github_{repo_name}.md"
        content = f"""---
title: "{full}"
author: "{full.split('/')[0]}"
platform: github
source: github_starred
source_type: github_curated
source_platform: github
stars: {stars}
forks: {item.get('forks_count', 0)}
language: "{lang}"
description: "{desc}"
pushed_at: "{pushed}"
url: "https://github.com/{full}"
collected: "{get_today_str()}"
curated_note: "用户 GitHub Starred 收藏库（人工背书，相关性筛选后保留）"
---

# {full}

> {desc}

**Stars**: {stars} ｜ **Forks**: {item.get('forks_count', 0)} ｜ **Language**: {lang} ｜ **最近活跃**: {pushed}

## README

{readme_text or '(README 抓取失败)'}
"""
        (out_dir / fname).write_text(content, encoding="utf-8")
        count += 1
        print(f"    ✓ {full} ({stars}★, {lang})")
        seen.add(full)
        time.sleep(1)

    # 写一份筛选报告，便于用户核查被丢弃项
    rep = outlib / "starred_filter_report.md" if False else out_dir.parent / "gate" / f"starred_filter_{get_today_str()}.md"
    rep.parent.mkdir(parents=True, exist_ok=True)
    lines = ["---", f"date: {get_today_str()}", "source: github_starred_filter", "---", "",
             f"# Starred 筛选报告（{get_today_str()}）", "",
             f"Starred 总数: {len(all_repos)} ｜ 保留 collect: {count} ｜ 丢弃: {len(discarded)}", "",
             "## 保留（collect 入库）", "- 见 data/raw/{date}/ 下 source_type=github_curated 的 .md", "",
             "## 丢弃（强偏离 AI/内容/工具 定位）"]
    for f, s, d in sorted(discarded, key=lambda x: -x[1]):
        lines.append(f"- {f} ({s}★) — {d}")
    rep.write_text("\n".join(lines), encoding="utf-8")

    print(f"[starred] 完成：保留 {count} 条，丢弃 {len(discarded)} 条 → 报告 {rep}")
    return count


def write_summary(out_dir):
    files = sorted(out_dir.glob("*.md"))
    summary = {
        "date": get_today_str(),
        "total_files": len(files),
        "output_dir": str(out_dir),
        "files": [f.name for f in files],
        "generated_by": "scripts/collect_github.py",
        "note": "含 GitHub 高 star 库 README 采集（signal+collect 双通道）",
    }
    (out_dir / "_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["trending", "topic", "watch", "starred", "all"],
                    default="all", help="采集通道：trending=风向标/增长快, topic=高star正文, watch=个人收藏列表, starred=你的 GitHub Starred 全部")
    ap.add_argument("--topics", default=",".join(TOPICS),
                    help="逗号分隔的 GitHub topic，如 ai-agents,rag")
    ap.add_argument("--top-n", type=int, default=TOP_N)
    ap.add_argument("--min-stars", type=int, default=MIN_STARS)
    ap.add_argument("--since", choices=["daily", "weekly"], default="daily",
                    help="trending 周期")
    ap.add_argument("--top-trending", type=int, default=20,
                    help="trending 最多报告几个")
    ap.add_argument("--from-starred", action="store_true",
                    help="把你的 GitHub Starred 全部收藏库拉进来（需 token）")
    ap.add_argument("--token", default=None,
                    help="GitHub PAT（也可放环境变量 GITHUB_TOKEN 或 config/github_token.txt，三者均不进版本库）")
    args = ap.parse_args()
    token = load_token(args.token)
    topics = [t.strip() for t in args.topics.split(",") if t.strip()]

    print("=" * 50)
    print(f"GitHub 采集 — {get_today_str()} — mode={args.mode}")
    print("=" * 50)

    if args.mode in ("trending", "all"):
        collect_trending(SIGNAL_DIR, since=args.since, top=args.top_trending)

    if args.mode in ("topic", "watch", "starred", "all"):
        out_dir = get_today_dir()
        start_idx = len(list(out_dir.glob("*.md")))
        if args.mode in ("topic", "all"):
            collect_topic(out_dir, start_idx, topics, args.top_n, args.min_stars)
            start_idx = len(list(out_dir.glob("*.md")))
        if args.mode in ("watch", "all"):
            collect_watch(out_dir, start_idx)
        if args.mode == "starred" or args.from_starred:
            collect_starred(out_dir, start_idx, token)
        write_summary(out_dir)
        print(f"\n采集完成: GitHub → {out_dir}")


if __name__ == "__main__":
    main()
