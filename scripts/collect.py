#!/usr/bin/env python3
"""
爆文采集脚本 — 每日自动运行
数据源：SoPilot RSS (X爆帖) + Exa搜索 (公众号/网页)
输出：data/raw/{YYYY-MM-DD}/{序号}_{来源}.md
"""

import os
import sys
import json
import re
import subprocess
from datetime import datetime, timezone, timedelta
from pathlib import Path

# ── 配置 ──────────────────────────────────────────
WORKFLOW_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = WORKFLOW_DIR / "data" / "raw"

# SoPilot RSS
SOPILOT_RSS = "https://sopilot.net/rss/hottweets"

# Exa 搜索关键词（从 keywords.md 工具名+场景词层精选，每周可调整）
EXA_QUERIES = [
    # 赛道1: AI工具 — 具体工具名+场景
    "ChatGPT vs Claude 写作 实测",
    "Cursor AI编程 教程 实操",
    "n8n 自动化工作流 搭建 教程",
    "ComfyUI 工作流 生图 教程",
    # 赛道2: AI视频/创作
    "可灵AI 即梦 Sora 实测 对比",
    "AI剪辑 短视频 教程",
    # 赛道3: 自媒体运营
    "小红书 起号 实操 复盘",
    "公众号 涨粉 运营 干货",
    # 赛道4: 副业
    "AI副业 普通人 真实 踩坑",
    "AI接单 变现 实操",
    # 热点追踪
    "AI去AI味 提示词 写作",
    "Claude Code 使用技巧",
]

# mcporter 路径（Windows 下需要完整路径）
NODE_DIR = r"C:\Program Files\nodejs"
MCPORTER = os.path.join(NODE_DIR, "mcporter.cmd") if os.name == "nt" else "mcporter"

# 确保 PATH 包含 Node.js
_env = os.environ.copy()
_env["PATH"] = NODE_DIR + os.pathsep + _env.get("PATH", "")


def get_today_str():
    """返回北京时间的今天日期字符串"""
    tz = timezone(timedelta(hours=8))
    return datetime.now(tz).strftime("%Y-%m-%d")


def get_today_dir():
    """创建并返回今天的 raw 目录"""
    today = get_today_str()
    d = RAW_DIR / today
    d.mkdir(parents=True, exist_ok=True)
    return d


def existing_files_count(out_dir: Path) -> int:
    """统计目录下已有文件数，用于编号"""
    return len(list(out_dir.glob("*.md")))


# ── 源1: SoPilot RSS ────────────────────────────────

def collect_sopilot(out_dir: Path):
    """从 SoPilot RSS 抓 X/Twitter 爆帖"""
    print("[SoPilot] 抓取 X 爆帖 RSS...")
    try:
        import feedparser
    except ImportError:
        print("[SoPilot] feedparser 未安装，跳过")
        return 0

    feed = feedparser.parse(SOPILOT_RSS)
    if not feed.entries:
        print("[SoPilot] RSS 无数据")
        return 0

    start_idx = existing_files_count(out_dir)
    count = 0

    for i, entry in enumerate(feed.entries):
        title = entry.get("title", "Unknown")
        link = entry.get("link", "")
        pub_date = entry.get("published", "")
        desc = entry.get("description", "")

        # 从描述中提取互动数据和原推链接
        metrics = {}
        original_url = ""
        for line in desc.split("\n"):
            line = line.strip()
            if line.startswith("原推链接:"):
                original_url = line.replace("原推链接:", "").strip()
            if "❤️" in line or "👀" in line:
                metrics["raw"] = line

        # 提取爆火概率
        viral_prob = ""
        pred_views = ""
        prob_match = re.search(r"预测爆火概率[:：](\S+)", desc)
        if prob_match:
            viral_prob = prob_match.group(1)
        views_match = re.search(r"预测浏览量[:：](\S+)", desc)
        if views_match:
            pred_views = views_match.group(1)

        # 清理描述，去掉 SoPilot 元数据行，保留正文
        clean_desc = "\n".join(
            line for line in desc.split("\n")
            if not any(skip in line for skip in [
                "❤️", "预测爆火概率", "预测浏览量", "预测评论", "原推链接"
            ])
        ).strip()

        filename = f"{start_idx + count + 1:02d}_sopilot_x.md"
        filepath = out_dir / filename

        content = f"""---
title: "{title}"
author: "{title.split('(')[0].strip() if '(' in title else title}"
platform: X/Twitter
source: SoPilot热帖
published: "{pub_date}"
viral_probability: "{viral_prob}"
predicted_views: "{pred_views}"
original_url: "{original_url}"
sopilot_link: "{link}"
collected: "{get_today_str()}"
---

{clean_desc}
"""
        filepath.write_text(content, encoding="utf-8")
        count += 1

    print(f"[SoPilot] 采集 {count} 条爆帖")
    return count


# ── 源2: Exa 搜索 ──────────────────────────────────

def collect_exa(out_dir: Path, queries: list = None):
    """通过 mcporter + Exa 搜索公众号/网页深度文章"""
    print("[Exa] 搜索公众号/网页深度文章...")
    if queries is None:
        queries = EXA_QUERIES

    start_idx = existing_files_count(out_dir)
    count = 0
    seen_urls = set()

    for query in queries:
        print(f"  搜索: {query}")
        try:
            # 调用 mcporter
            cmd = [
                MCPORTER, "call",
                f'exa.web_search_exa(query: "{query}", numResults: 3)'
            ]
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=30,
                encoding="utf-8", errors="replace", env=_env
            )
            output = result.stdout

            if not output.strip():
                print(f"  [{query}] 无结果")
                continue

            # 解析 mcporter 输出（Title/URL/Published 块）
            articles = parse_mcporter_output(output)

            for article in articles:
                url = article.get("url", "")
                if not url or url in seen_urls:
                    continue
                seen_urls.add(url)

                # 跳过非中文/非相关内容
                title = article.get("title", "")
                if not title or len(title) < 5:
                    continue

                filename = f"{start_idx + count + 1:02d}_exa_web.md"
                filepath = out_dir / filename

                highlights = article.get("highlights", "")
                pub_date = article.get("published", "N/A")

                content = f"""---
title: "{title}"
platform: 网页/公众号
source: Exa搜索
search_query: "{query}"
url: "{url}"
published: "{pub_date}"
collected: "{get_today_str()}"
---

{highlights}
"""
                filepath.write_text(content, encoding="utf-8")
                count += 1

            # 避免请求太快
            import time
            time.sleep(1)

        except subprocess.TimeoutExpired:
            print(f"  [{query}] 超时，跳过")
        except Exception as e:
            print(f"  [{query}] 错误: {e}")

    print(f"[Exa] 采集 {count} 篇文章")
    return count


def parse_mcporter_output(output: str) -> list:
    """解析 mcporter call 的输出为文章列表"""
    articles = []
    current = {}

    for line in output.split("\n"):
        line = line.strip()
        if line.startswith("Title:"):
            if current:
                articles.append(current)
            current = {"title": line[6:].strip()}
        elif line.startswith("URL:"):
            current["url"] = line[4:].strip()
        elif line.startswith("Published:"):
            current["published"] = line[10:].strip()
        elif line.startswith("Author:"):
            current["author"] = line[7:].strip()
        elif line.startswith("Highlights:"):
            current["highlights"] = line[11:].strip()
        elif current and "highlights" in current:
            # 多行 highlights
            current["highlights"] += "\n" + line

    if current:
        articles.append(current)

    return articles


# ── 主流程 ──────────────────────────────────────────

def main():
    print(f"{'='*50}")
    print(f"爆文采集 — {get_today_str()}")
    print(f"{'='*50}")

    out_dir = get_today_dir()
    print(f"输出目录: {out_dir}")

    total = 0

    # 源1: SoPilot
    total += collect_sopilot(out_dir)

    # 源2: Exa
    total += collect_exa(out_dir)

    print(f"\n{'='*50}")
    print(f"采集完成: 共 {total} 篇 → {out_dir}")
    print(f"{'='*50}")

    # 输出采集摘要
    summary = {
        "date": get_today_str(),
        "total": total,
        "output_dir": str(out_dir),
        "files": [f.name for f in sorted(out_dir.glob("*.md"))]
    }
    summary_path = out_dir / "_summary.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    return total


if __name__ == "__main__":
    sys.exit(0 if main() > 0 else 1)
