#!/usr/bin/env python3
"""
RSS + AI 每日简报生成器
=========================
从多个英文信息源抓取 RSS，按关键词相关度评分排序，
生成一份当日 AI/工具/工作流领域的日报 Markdown。

用法:
    python generate_brief.py            # 生成今天的日报
    python generate_brief.py --hours 48 # 自定义回看窗口

GitHub Actions 每天北京时间 8:00 自动执行，电脑关机也照跑。
"""

import os
import re
import sys
import time
import hashlib
from datetime import datetime, timedelta, timezone
from collections import defaultdict
from urllib.parse import urlparse

import feedparser

# 同目录导入
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import (
    FEEDS, SOURCE_WEIGHTS, KEYWORDS,
    LOOKBACK_HOURS, TOP_N, REQUEST_TIMEOUT, USER_AGENT,
)


# ============================================
# 工具函数
# ============================================

def now_utc():
    return datetime.now(timezone.utc)

def now_beijing():
    return datetime.now(timezone(timedelta(hours=8)))

def parse_entry_date(entry):
    """尝试多种字段解析文章发布时间，返回 UTC datetime 或 None。"""
    for field in ("published_parsed", "updated_parsed"):
        t = getattr(entry, field, None)
        if t:
            try:
                return datetime(*t[:6], tzinfo=timezone.utc)
            except Exception:
                pass
    # fallback: 字符串解析
    for field in ("published", "updated"):
        val = entry.get(field, "")
        if val:
            try:
                from email.utils import parsedate_to_datetime
                dt = parsedate_to_datetime(val)
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                return dt
            except Exception:
                pass
    return None

def normalize_title(title):
    """标题归一化用于去重。"""
    t = re.sub(r"[^\w\s]", "", title.lower().strip())
    t = re.sub(r"\s+", " ", t)
    return t

def clean_html(text):
    """去掉 HTML 标签，截取纯文本。"""
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def extract_summary(text, max_len=200):
    """提取摘要：取前 1-2 句。"""
    text = clean_html(text)
    if not text:
        return ""
    # 按句号分割，取前 2 句
    sentences = re.split(r'(?<=[.!?])\s+', text)
    summary = " ".join(sentences[:2])
    if len(summary) > max_len:
        summary = summary[:max_len].rsplit(" ", 1)[0] + "..."
    return summary

def extract_tags(title, summary):
    """从标题和摘要中提取标签。"""
    text = (title + " " + summary).lower()
    tags = []
    tag_map = {
        "LLM": ["llm", "large language model", "gpt", "chatgpt", "claude", "gemini", "llama"],
        "Agent": ["agent", "agentic", "multi-agent"],
        "开源": ["open source", "open-source", "opensource", "github"],
        "RAG": ["rag", "retrieval"],
        "微调": ["fine-tune", "fine-tuning", "fine tune", "lora"],
        "工具": ["tool", "workflow", "automation", "no-code"],
        "编程": ["coding", "copilot", "cursor", "ide", "programming"],
        "模型": ["model", "training", "inference", "benchmark"],
        "API": ["api", "sdk", "framework"],
    }
    for tag, keywords in tag_map.items():
        if any(kw in text for kw in keywords):
            tags.append(tag)
    return tags[:4]  # 最多 4 个标签


# ============================================
# 核心逻辑
# ============================================

def fetch_all_feeds():
    """抓取所有信源，返回 (source_name, entries) 列表。"""
    results = []
    for name, url in FEEDS.items():
        try:
            print(f"  抓取: {name} ...", end=" ", flush=True)
            feed = feedparser.parse(
                url,
                request_headers={"User-Agent": USER_AGENT},
            )
            if feed.bozo and not feed.entries:
                print(f"❌ 解析失败: {feed.bozo_exception}")
                results.append((name, []))
                continue
            print(f"✅ {len(feed.entries)} 篇")
            results.append((name, feed.entries))
        except Exception as e:
            print(f"❌ 网络错误: {e}")
            results.append((name, []))
        # 礼貌延迟，避免被 ban
        time.sleep(0.5)
    return results

def filter_and_score(entries, source_name, cutoff_time):
    """过滤日期 + 评分，返回 scored article 列表。"""
    scored = []
    for entry in entries:
        # 日期过滤
        pub_date = parse_entry_date(entry)
        if pub_date and pub_date < cutoff_time:
            continue  # 太旧，跳过

        title = entry.get("title", "")
        if not title:
            continue

        summary_raw = entry.get("summary", "") or entry.get("description", "")
        link = entry.get("link", "")

        # 关键词评分
        text = (title + " " + clean_html(summary_raw)).lower()
        kw_score = sum(1 for kw in KEYWORDS if kw in text)

        # 来源加权
        source_weight = SOURCE_WEIGHTS.get(source_name, 1.0)
        final_score = kw_score * source_weight

        # 时效性加分（越新越高，6h 内额外 +2，12h 内 +1）
        if pub_date:
            hours_ago = (now_utc() - pub_date).total_seconds() / 3600
            if hours_ago < 6:
                final_score += 2
            elif hours_ago < 12:
                final_score += 1

        scored.append({
            "title": title,
            "link": link,
            "summary": extract_summary(summary_raw),
            "source": source_name,
            "score": final_score,
            "pub_date": pub_date,
            "tags": extract_tags(title, summary_raw),
            "title_norm": normalize_title(title),
        })

    return scored

def deduplicate(articles):
    """按标题归一化去重，保留评分高的。"""
    seen = {}
    for art in articles:
        key = art["title_norm"]
        if len(key) < 10:
            continue  # 太短的标题不做去重
        if key not in seen or art["score"] > seen[key]["score"]:
            seen[key] = art
    # 也加入没去重上的短标题文章
    for art in articles:
        if len(art["title_norm"]) < 10 and art["title_norm"] not in seen:
            seen[art["title_norm"]] = art
    return list(seen.values())

def generate_markdown(articles, stats):
    """生成日报 Markdown。"""
    beijing_time = now_beijing()
    date_str = beijing_time.strftime("%Y-%m-%d")

    # 排序
    articles.sort(key=lambda x: x["score"], reverse=True)
    top_articles = articles[:TOP_N]

    # 统计标签分布
    all_tags = defaultdict(int)
    for art in articles:
        for tag in art["tags"]:
            all_tags[tag] += 1
    top_tags = sorted(all_tags.items(), key=lambda x: -x[1])[:6]

    # 按来源分组
    by_source = defaultdict(list)
    for art in articles:
        by_source[art["source"]].append(art)

    lines = []
    lines.append(f"# AI 日报 | {date_str}")
    lines.append("")
    lines.append(f"> 自动抓取 {stats['total_sources']} 个英文信息源，筛选过去 {LOOKBACK_HOURS}h 的 AI/工具/工作流相关内容。")
    lines.append(f"> 生成时间: {beijing_time.strftime('%Y-%m-%d %H:%M')} (北京时间)")
    lines.append("")

    # 概览
    lines.append("## 今日概览")
    lines.append("")
    lines.append(f"| 指标 | 数值 |")
    lines.append(f"|------|------|")
    lines.append(f"| 抓取文章 | {stats['total_fetched']} 篇 |")
    lines.append(f"| 时间窗内 | {stats['total_in_window']} 篇 |")
    lines.append(f"| 去重后 | {len(articles)} 篇 |")
    lines.append(f"| 信源数 | {stats['total_sources']} 个 |")
    lines.append(f"| 成功抓取 | {stats['sources_ok']} 个 |")
    if top_tags:
        lines.append(f"| 热门标签 | {' · '.join(f'{t}({c})' for t, c in top_tags)} |")
    lines.append("")

    # Top N
    if top_articles:
        lines.append(f"## Top {len(top_articles)}（按相关度排序）")
        lines.append("")
        for i, art in enumerate(top_articles, 1):
            tags_str = " ".join(f"`#{t}`" for t in art["tags"]) if art["tags"] else ""
            lines.append(f"### {i}. [{art['title']}]({art['link']})")
            lines.append(f"- **来源**: {art['source']}  ")
            if art["pub_date"]:
                time_str = art["pub_date"].astimezone(timezone(timedelta(hours=8))).strftime("%H:%M")
                lines.append(f"- **时间**: {time_str} (北京时间)  ")
            if art["summary"]:
                lines.append(f"- **摘要**: {art['summary']}  ")
            if tags_str:
                lines.append(f"- **标签**: {tags_str}")
            lines.append("")

    # 按来源分组
    lines.append("## 按来源分组")
    lines.append("")
    for source in sorted(by_source.keys(), key=lambda s: -len(by_source[s])):
        arts = by_source[source]
        lines.append(f"### {source} ({len(arts)} 篇)")
        lines.append("")
        for art in arts[:10]:  # 每个来源最多展示 10 篇
            tags_str = f" {' '.join(f'`#{t}`' for t in art['tags'])}" if art["tags"] else ""
            lines.append(f"- [{art['title']}]({art['link']}){tags_str}")
        if len(arts) > 10:
            lines.append(f"- ...还有 {len(arts) - 10} 篇")
        lines.append("")

    # 页脚
    lines.append("---")
    lines.append("*由 RSS + AI 自动生成 | `tools/rss_daily_brief` | GitHub Actions 每日定时执行*")
    lines.append("")

    return "\n".join(lines)


# ============================================
# 主函数
# ============================================

def main():
    hours = LOOKBACK_HOURS
    if "--hours" in sys.argv:
        idx = sys.argv.index("--hours")
        if idx + 1 < len(sys.argv):
            hours = int(sys.argv[idx + 1])

    beijing_time = now_beijing()
    date_str = beijing_time.strftime("%Y-%m-%d")
    print(f"{'='*50}")
    print(f"RSS + AI 每日简报 - {date_str}")
    print(f"回看窗口: {hours}h")
    print(f"{'='*50}")
    print()

    # 1. 抓取
    print("[1/4] 抓取 RSS 信源...")
    feed_results = fetch_all_feeds()

    # 2. 过滤 + 评分
    print()
    print("[2/4] 过滤日期 + 评分...")
    cutoff = now_utc() - timedelta(hours=hours)
    all_articles = []
    total_fetched = 0
    sources_ok = 0
    for source_name, entries in feed_results:
        total_fetched += len(entries)
        if entries:
            sources_ok += 1
        scored = filter_and_score(entries, source_name, cutoff)
        all_articles.extend(scored)
        if scored:
            print(f"  {source_name}: {len(scored)} 篇在时间窗内")

    # 3. 去重
    print()
    print("[3/4] 去重...")
    before_dedup = len(all_articles)
    articles = deduplicate(all_articles)
    print(f"  去重前: {before_dedup} -> 去重后: {len(articles)}")

    # 4. 生成 Markdown
    print()
    print("[4/4] 生成日报...")
    stats = {
        "total_fetched": total_fetched,
        "total_in_window": before_dedup,
        "total_sources": len(FEEDS),
        "sources_ok": sources_ok,
    }
    markdown = generate_markdown(articles, stats)

    # 保存
    output_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        "output", "rss_briefs"
    )
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{date_str}_ai_daily_brief.md")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown)

    print()
    print(f"{'='*50}")
    print(f"完成! 日报已保存:")
    print(f"  {output_file}")
    print(f"  共 {len(articles)} 篇文章, Top {min(TOP_N, len(articles))} 精选")
    print(f"{'='*50}")

    return output_file


if __name__ == "__main__":
    main()
