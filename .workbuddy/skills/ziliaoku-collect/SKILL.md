---
name: ziliaoku-collect
description: 爆文采集层编排技能（发现 + 抓取）。从 NewsNow / 今日热榜 / SoPilot / watchlist 四个发现入口发现爆文候选，并用 firecrawl / agent-reach / SoPilot RSS 抓取全文，写入 data/raw/{YYYY-MM-DD}/。This skill should be used when the user wants to run the daily or weekly collection of viral posts for the ziliaoku topic library, or when onboarding a new collection source.
agent_created: true
---

# ziliaoku-collect — 采集层编排（发现 + 抓取）

## Purpose
把各平台的爆文 / 深度文采集进 `data/raw/{日期}/`，作为下游「质检 → 提取 → 聚类 → 选题库 → 成稿 → 配图 → 周复盘」流水线唯一的原材料入口。

## When to use
- 用户说"跑采集 / 采一波 / 抓今天的爆文 / 更新资料库"。
- 周复盘决定新增发现入口时，按本技能的入口契约接入。

## 架构原则（冻结，不可变通）
1. **发现与抓取分离**：三个聚合站（NewsNow / 今日热榜 / SoPilot）只负责"发现有什么"（标题 + 源平台 + 链接）。**禁止把聚合页摘要当正文入库**。
2. **聚合站只出现在发现层**：抓全文一律交给 firecrawl / agent-reach。
3. **热榜标题本身 = 免费标题公式样本库**：未抓全文的标题直接进 `data/titles_pool.jsonl`，与正文库分开。

## 发现入口（冻结为 4 个，上限 6）

### 入口1 NewsNow（newsnow.busiyi.world）— 每日 1 次，中文全景
- 覆盖：知乎、微博、B站、虎扑、V2EX 等聚合。
- 用法：firecrawl 抓聚合页 → 提取条目（标题 + 源平台 + 链接）→ 按 `keywords.md` 赛道词初筛（标题含赛道词或明显 AI / 工具相关）→ 命中的抓原文全文。
- 重点子源：V2EX（一手技术讨论）、知乎（长文拆解）。
- 低优子源：微博、虎扑（热闹多干货少，只取标题进 `titles_pool.jsonl`，不抓全文）。

### 入口2 今日热榜（tophub.today/c/tech）— 每日 1 次，技术风向主入口
- 覆盖：GitHub Trending、Product Hunt、Hacker News 及常规平台。
- 用法：直接抓此页提取条目（已聚合好，省去多次单独抓取）。
- 筛选：GitHub 条目记录 star 及描述；HN > 200 分；PH 当日 Top 10。
- 命中的抓原文（GitHub 抓 README；HN 抓原链 + 前 5 条高赞评论）。

### 入口3 SoPilot（sopilot.net/zh/hot-tweets）— 每日 1 次，X 爆帖
- 用法：抓热帖列表 → 按赛道相关性初筛 → 命中的用 firecrawl 抓推文全文（含长文 Article，已验证可穿透）。
- 与入口4互补：SoPilot 管"陌生爆帖发现"，watchlist 管"已知作者跟踪"；SoPilot 中连续 2 次出现的作者 → 自动提名进 `watchlist.md` 候选。

### 入口4 作者监控（watchlist.md）— 每周 2 次
- X 作者 + 公众号名单定向抓最新文章（公众号走搜狗微信）。
- 维护规则：命中 +1、连续 4 周零命中移出、高命中作者的互动对象提名候选。

### 关键词搜索降级为补充
- 仅公众号（搜狗微信）保留关键词搜索，每周 1 次，赛道词用「AI 工具实操 / AI 视频」（副业词已删）。

## 抓取方式
- 正文全文：`firecrawl`（`scrape` / `search`）或 `agent-reach`（小红书已移除；YouTube / Reddit 等）。
- X 爆帖：`SoPilot RSS`（已验证，见 `scripts/collect.py`）+ firecrawl 穿透长文。
- 公众号：搜狗微信入口 + firecrawl。

## 输出契约（冻结）
每个采集结果写成 `data/raw/{YYYY-MM-DD}/{序号}_{platform}.md`，**头部 frontmatter 必须齐全**，供 `ziliaoku-gate` 读取：

```markdown
---
title: "原标题"
author: "作者/账号"
platform: "x|wechat|github|hn|v2ex|zhihu|bilibili|..."
source: "NewsNow|今日热榜|SoPilot|watchlist|wechat_search"
source_type: "aggregator_discovery|watchlist|wechat_search"
source_platform: "v2ex|zhihu|github|hn|x|wechat|..."
url: "原文链接"
published: "发布日期"
collected: "YYYY-MM-DD"
---
全文 / 正文
```

## 工具依赖（待接入，当前环境未连线）
- firecrawl MCP：连接器状态 `disconnected`，需用户在 WorkBuddy 连接并配 Key。
- agent-reach：本环境未安装，按安装文档部署。
- SoPilot RSS：已通（`feedparser`），`scripts/collect.py` 已实现。
- 搜狗微信 / GitHub / HN：经 firecrawl 或官方页。

## 与 collect.py 的关系
`scripts/collect.py` 当前实现「SoPilot RSS + Exa 搜索」两条源。本技能接管后，采集编排应以本技能的 4 入口契约为准；`collect.py` 可作为 SoPilot 源的实现保留，其余入口待接工具后补齐。

## 稳定性规则（冻结）
- 三个聚合站均为第三方，可能改版 / 失效：每次抓取校验"提取条目数 > 10"，低于则告警并回退到该入口的自建抓取（GitHub / HN 有官方页可直抓），失效事件记 `lessons.md`。
- 每周目标：40–60 篇。
