---
name: ziliaoku-collect
description: 爆文采集层编排技能（发现 + 抓取 + 信号）。从 NewsNow / 今日热榜 / SoPilot / watchlist / Reddit 五个发现入口发现爆文候选，从 小红书 信号源抽取标题公式与封面模式，并用 firecrawl / agent-reach(opencli) / Jina Reader / SoPilot RSS 抓取全文，写入 data/raw/{YYYY-MM-DD}/ 与 data/titles_pool.jsonl、data/image-styles 信号库。This skill should be used when the user wants to run the daily or weekly collection of viral posts for the ziliaoku topic library, or when onboarding a new collection source.
agent_created: true
---

# ziliaoku-collect — 采集层编排（发现 + 抓取 + 信号）

## Purpose
把各平台的爆文 / 深度文 / 信号采集进流水线唯一的原材料入口：
- **正文** → `data/raw/{日期}/`（供下游 质检→提取→聚类→选题库→成稿→配图→周复盘）
- **标题公式** → `data/titles_pool.jsonl`（与正文库分开，喂 Prompt-B 提炼标题公式）
- **封面模式** → `data/image-styles/`（喂 ziliaoku-image 配图）

## When to use
- 用户说"跑采集 / 采一波 / 抓今天的爆文 / 更新资料库 / 营业一波"。
- 周复盘决定新增发现入口时，按本技能的入口契约接入。

## 架构原则（冻结，不可变通）
1. **发现与抓取分离**：聚合站（NewsNow / 今日热榜 / SoPilot / Reddit）只负责"发现有什么"（标题 + 源平台 + 链接）。**禁止把聚合页摘要当正文入库**。
2. **聚合站只出现在发现层**：抓全文一律交给 firecrawl / agent-reach(opencli) / Jina Reader。
3. **热榜标题 = 免费标题公式样本库**：所有平台热榜标题直接进 `data/titles_pool.jsonl`，与正文库分开。
4. **信号源 ≠ 正文源**：小红书只抽标题公式 + 封面模式（进 titles_pool / image-styles），**不抓正文**（内容在图里，抓不到也抓不全；正文走微信 / YouTube / B站更划算）。

## 发现入口（5 个，上限 6，留 1 空位）

### 入口1 NewsNow（newsnow.busiyi.world）— 中文全景
- 频率：每日 1 次
- 覆盖：知乎、微博、B站、虎扑、V2EX 等聚合
- 用法：firecrawl 抓聚合页 → 提取条目（标题+源平台+链接）→ 按 `keywords.md` 赛道词初筛
- V2EX、知乎 → agent-reach / Jina 抓全文 → 走质检
- 微博、虎扑 → 只取标题进 `titles_pool.jsonl`，不抓全文

### 入口2 今日热榜（tophub.today/c/tech）— 技术风向
- 频率：每日 1 次
- 覆盖：GitHub Trending、Product Hunt、Hacker News
- 用法：firecrawl 抓此页提取条目（已聚合好，省去多次单独抓取）
- 筛选：GitHub star 周增 > 1000 或一句话说清 → verdict: signal（走 Prompt-S，不进爆文库）；HN > 200 分；PH 当日 Top 10
- 命中抓原文（GitHub 抓 README；HN 抓原链 + 前 5 条高赞评论）

### 入口3 SoPilot（sopilot.net/zh/hot-tweets）— X 爆帖
- 频率：每日 1 次（RSS: https://sopilot.net/rss/hottweets）
- 用法：RSS 抓取 → 赛道初筛 → 命中用 firecrawl 抓推文全文（含长文 Article，已验证可穿透）
- 抓全文工具：firecrawl `scrape` 可穿透 X 推文 / 文章 URL（抗反爬，已验证可读）；agent-reach `opencli twitter` 为备用读者。注意 firecrawl keyless 层 `scrape`/`search`/`interact` 可用，`crawl` 需升级 Key，故以"具体 URL 的 scrape + search 搜"为主，不依赖 crawl。
- 与入口4配合：SoPilot 管"陌生爆帖发现"，watchlist 管"已知作者跟踪"；SoPilot 中连续 2 次出现的作者 → 自动提名进 `watchlist.md` 候选
- ⚠️ **空壳防护（2026-07-08 修正）**：若 firecrawl 不可达/限流导致抓不到推文全文，该命中**只进 `data/titles_pool.jsonl`（标题信号），绝不写无正文的 raw 文件**。之前产生的 `sopilot_x` 类空壳（只有标题/链接无正文）已清理——发现与抓取分离纪律下，没抓到全文的聚合命中不应占用 raw 正文库。

### 入口4 作者监控（watchlist.md）— 定向跟踪
- 频率：每周 2 次
- 覆盖：X 作者 + 公众号名单（公众号走搜狗微信）
- 维护：命中 +1、连续 4 周零命中移出、高命中作者的互动对象提名候选

### 入口5 Reddit（r/LocalLLaMA, r/StableDiffusion 等）— 英文深水区
- 频率：每周 1 次
- 用法：agent-reach reddit 抓取 → 翻译摘要 → 走质检
- 价值：大量"还没热但马上会热"的一手实测，是抢首发的金矿

### GitHub API 源（三通道：trending 风向标 + topic 高 star 正文 + watch 个人收藏）

> 接入依据：reviews/2026-07-08_github_source.md + 用户 2026-07-08 指令（加风向标/增长快/个人收藏/2000阈值）。GitHub 比公众号友好：README 无反爬可直接抓，api.github.com 匿名拿 star/pushed_at 信号（无需 Key）。用户确认：高 star 库的 README 介绍写得好、是优质内容源；且用户自己收藏了很多库，应单独成一路。

- **发现**：
  - trending：`github.com/trending?since=daily|weekly` 抓「增长速度快的」库（HTML 刮取，无 API 消耗）→ 出**风向标 signal**（进 `data/signal/`）。
  - topic：`api.github.com/search/repositories?q=topic:ai-agents&sort=stars`（topic 可配：ai-agents / rag / prompt-engineering / llm / agentic-ai），匿名限速 60/h，无需 Key。
  - watch：读 `data/github_watchlist.md`（用户个人收藏库，每行一个 repo + 备注）→ 绕过 star 阈值直接 collect。
- **信号**：`stargazers_count`（社区热度背书）+ `pushed_at`（近期活跃度）+ **trending 当日/周新增 star（增长速度快慢）**。高 star 且近期活跃 = 工具在涨；trending 上榜 = 正在涨。
- **抓取**：`api.github.com/repos/{full}` 拿 `default_branch` → `raw.githubusercontent.com/{owner}/{repo}/{branch}/README.md` 抓正文（无反爬，远优于公众号）。
- **三通道分工（不占 6 发现入口，挂在 signal / 今日热榜增强）**：
  - **① trending 风向标**（增长速度快的）：刮 `github.com/trending?since=daily`，按当日新增 star 排序，新增 ≥50★ 的库 → **`signal`**（写 `data/signal/{日期}_github_trending_daily.jsonl`，进 Prompt-S 风向标，**不进爆文库**）。这是"什么工具正在火"的实时雷达。
  - **② topic 高 star 正文**：高 star(≥**2000**) + 近期活跃(pushed_at 近 180 天) + README 讲「怎么用/适用场景/有代码示例」→ **`collect`**（进爆文库做「神库推荐 / 工具盘点」选题，自带 star 数字背书）。
  - **③ watch 个人收藏**（用户人工背书）：`data/github_watchlist.md` 里的库，**绕过 star 阈值**直接 collect（用户亲自认可 = 最高质量信号）。备注写进 frontmatter `curated_note`。
  - 例外：纯公告 / release / 无介绍代码库 → `signal`/`discard`；软广卖课 → `discard`。
- **脚本**：`scripts/collect_github.py`
  - 风向标：`python scripts/collect_github.py --mode trending --since daily`
  - 高 star 正文：`python scripts/collect_github.py --mode topic --topics ai-agents,rag --top-n 8 --min-stars 2000`
  - 个人收藏：`python scripts/collect_github.py --mode watch`（读 `data/github_watchlist.md`）
  - 全跑：`python scripts/collect_github.py --mode all`
  - 频率：每日 1 次，`--mode all` 单日一次不触 API 限速。

## 发现增强：RSSHub（推荐，更稳的发现格式）

把 NewsNow / 今日热榜 这类"HTML 聚合页"升级为**稳定 RSS**，是搜索层最该做的一处加固：
- RSSHub 能给知乎 / 微博 / B站 / GitHub Trending / Hacker News / Product Hunt（及部分 X 路由）生成 RSS，feed 格式稳定，**不怕聚合站改版**（契合"稳定性规则：提取条目数 > 10 校验"，失效即告警）。
- 接入：把 RSSHub feed URL 直接喂 agent-reach 的 RSS 渠道（feedparser 已装），与 SoPilot RSS 同源处理。
- 实例：公共 `rsshub.app`（有速率限制，先用着）；要稳可自托管（Docker 一条命令，生产建议自托管）。
- 路由示例（按需取）：GitHub Trending `https://rsshub.app/github/trending/daily`、Hacker News `https://rsshub.app/hackernews/...`、Product Hunt `https://rsshub.app/producthunt/...`、B站 `https://rsshub.app/bilibili/...`、知乎 `https://rsshub.app/zhihu/...`
- **不是第 6 个发现入口**（仍守 ≤6 纪律），而是让入口1/2 的发现格式从"HTML 抓取"升级为"RSS"，更稳、更易校验。

## 搜索执行：关键词驱动查询库（让搜索层可执行，不止靠聚合站发现）

发现层靠聚合站"被动发现"；这一层用 keywords.md 赛道词**主动搜索**深水区内容（抢首发）。工具已就位：firecrawl `search`（免 Key）/ agent-reach opencli（reddit / twitter）/ Jina。

### firecrawl search（keyless 可用；注意 keyless 不支持 `crawl`，用 `scrape` 抓具体 URL + `search` 搜）
对齐 W1–W4 周轮转，每周跑对应查询（每词 1 次，limit 10）：
- W1：搜索 "AI写作 去AI味 教程" / "ChatGPT Claude 实测 对比" / "ComfyUI 工作流 小红书"
- W2：搜索 "n8n 自动化 实战" / "Dify 工作流 搭建" / "小红书 起号 实操 涨粉"
- W3：搜索 "可灵 即梦 Sora 实测" / "AI副业 真实案例 一人公司" / "AI做短视频 教程"
- W4：搜索 "Cursor AI编程 教程" / "AI工具 横评 合集" / "效率工具 清单 免费"
- 通投：搜索 "AI Agent 工作流 MCP" / "AI 提示词 写作模板"

### agent-reach 深水区搜索（英文一手实测，抢首发金矿）
- Reddit：`opencli reddit search "AI agent workflow n8n" -f yaml --limit 15` / `opencli reddit search "ComfyUI workflow" -f yaml`
- X：`opencli twitter search "AI写作 去AI味" -f yaml --limit 15`（复用 Chrome 登录态，抓热帖 + thread）
- 命中 X 长文 / 文章 URL → firecrawl `scrape` 穿透抓全文（firecrawl 抗 X 反爬，已验证可读推文 / 文章）。

## 信号源（独立流，非发现入口）：小红书

### 角色：信号源（非正文源）
- **只抽**：标题公式、钩子手法、封面模式、排版套路 → 进 `data/titles_pool.jsonl` + `data/image-styles/`
- **不抽**：正文（小红书内容在图 / 视频里，抓不到也抓不全；且后续发布平台含小红书，研究自己平台的爆款公式比抓别人正文更有用）
- 后端：agent-reach → `opencli xiaohongshu`（复用 Chrome 登录态）
- 前置：需装 **OpenCLI Chrome 扩展** + **Chrome 已登录 xiaohongshu**（见 工具依赖）

### 采集命令（opencli，安全，不抓正文）
```bash
# 按赛道关键词搜笔记，取标题 + 封面 + 互动数据（信号，不抓正文）
opencli xiaohongshu search "AI写作去AI味" -f yaml --limit 20
# 看某作者 / 话题的 feed 标题流
opencli xiaohongshu feed --type user --id <user_id> -f yaml
```
- 取 `note_title` / `cover_url` / `likes` / `collects` / `tags` → 写 `data/titles_pool.jsonl`：
```json
{"title":"笔记标题","platform":"xiaohongshu","likes":数字,"collects":数字,"date":"日期","topic_tags":["标签"],"cover_url":"封面链接","source":"xiaohongshu_signal"}
```
- 封面 URL 另存 `data/image-styles/{date}_xhs_covers.jsonl`（供 ziliaoku-image 提炼封面模式）
### 频率：每周 2~3 次（与 watchlist 同节奏），仅更新信号库，不进正文质检流

### ★ 拆平台爆款（结构化解构，涨粉命门，2026-07-08 新增）
> **为什么做**：知道"写什么选题"不够，得知道"在小红书/公众号这个写法灵不灵"。竞品 7 步的第 2 步就是**拆目标平台自家低粉高赞爆款的结构**——这是涨粉的命门。咱们原本只抽标题公式，缺"结构/开头/标签"的完整解构。本环节补足。

- **选样**：从上面信号里挑 `likes`/`collects` 明显高于同赛道同期、且作者粉丝低的笔记（低粉高赞 = 公式可复制，非人设红利）。每次取 Top 5~10。
- **解构（LLM 步骤，不抓正文，只用标题+开头预览+标签+互动）**：对每篇拆出
  1. 标题公式（套用 `titles_pool` 七类之一并标注）
  2. 开头 3 句结构（钩子怎么抛）
  3. 内容骨架（段落逻辑，如"痛点→反常识→步骤→证据→互动"）
  4. 话题标签组合（大流量+垂类配比）
  5. 封面模式（从 `image-styles` 已存）
- **产物** → 写 `data/xhs_winning_structures.jsonl`（与 `titles_pool` 并列，供 `ziliaoku-draft` 当 `structure_ref` 的真实平台样本）：
```json
{"platform":"xiaohongshu","note_title":"原笔记标题","title_formula":"痛点型","opening_3":"开头3句骨架（脱敏摘要）","skeleton":"痛点→反常识→3步→证据→互动","tags":["标签1","标签2"],"engagement":{"likes":数字,"collects":数字},"source":"xiaohongshu_deconstruct"}
```
- **公众号同源**：搜狗微信搜到的同赛道高赞文章，用 WebFetch 抓"标题+开头2段+小标题结构"（不抓全文），同样解构进 `xhs_winning_structures.jsonl`（`platform:"wechat"`）。
- ⚠️ 只解构"结构/公式"，绝不搬运原文句子（守红线 + 版权）。

## 抓取方式（fetch layer，当前环境实测）
- 正文全文：`firecrawl` `scrape`（具体 URL，含 X 推文 / 文章，抗反爬）/ `search`（搜）/ `agent-reach` opencli（X / Reddit / B站）
- X 爆帖发现：`SoPilot RSS`（已验证，`scripts/collect.py`）+ 命中用 firecrawl `scrape` 穿透长文
- 公众号：搜狗微信入口 + firecrawl `scrape`
- 任意网页：`Jina Reader`（`curl https://r.jina.ai/URL`）作 firecrawl 降级
- 发现增强：`RSSHub` 生成的 RSS → agent-reach RSS 渠道（更稳，替代 HTML 抓 NewsNow / 今日热榜）
- 小红书：仅信号（标题 + 封面），不抓正文
- ⚠️ firecrawl keyless 限制：`scrape` / `search` / `interact` 可用；`crawl` / `extract` 需升级 Key。故以"具体 URL 的 scrape + search 搜"为主，不依赖 crawl 整站。

## 输出契约（冻结）
### 正文
每个采集结果写成 `data/raw/{YYYY-MM-DD}/{序号}_{platform}.md`，**头部 frontmatter 必须齐全**，供 `ziliaoku-gate` 读取：
```markdown
---
title: "原标题"
author: "作者/账号"
platform: "x|wechat|github|hn|v2ex|zhihu|bilibili|reddit|..."
source: "NewsNow|今日热榜|SoPilot|watchlist|reddit|wechat_search"
source_type: "aggregator_discovery|watchlist|reddit|wechat_search"
source_platform: "v2ex|zhihu|github|hn|x|wechat|reddit|..."
url: "原文链接"
published: "发布日期"
collected: "YYYY-MM-DD"
---
全文 / 正文
```
### 信号（小红书）
`data/titles_pool.jsonl`（标题公式）+ `data/image-styles/{date}_xhs_covers.jsonl`（封面模式），格式见上。

## 工具依赖（当前环境实测状态，2026-07-07）
- ✅ **agent-reach v1.5.0 已装**（venv: `C:\Users\liuxi\.agent-reach-venv`），`doctor` 实测 **10/15 渠道可用**：
  - ✅ GitHub（gh，完整）/ V2EX（公开 API）/ RSS（feedparser）/ 任意网页（Jina Reader）
  - ✅ X/Twitter、Reddit、B站、Facebook、Instagram、**小红书**（均经 OpenCLI，复用 Chrome 登录态）
  - [X] YouTube：yt-dlp 未装（中文 YouTube 普遍无字幕，暂用 `opencli youtube` 元数据 + 英文字幕，非紧要）
  - [X] 全网语义搜索（Exa via mcporter）：mcporter 已装但 Exa 未 `config add`，需 `mcporter config add exa https://mcp.exa.ai/mcp`
- ✅ SoPilot RSS：feedparser，`scripts/collect.py` 已实现
- ✅ **RSSHub（发现增强，可选）**：把知乎/微博/B站/GitHub Trending/HN/PH 生成稳定 RSS，喂 agent-reach RSS 渠道。公共实例 `rsshub.app`（有限流），生产建议 Docker 自托管。让入口1/2 从 HTML 抓取升级为 RSS，更稳。
- ✅ **firecrawl MCP（keyless 托管层，免 API Key）**：已加进 `~/.workbuddy/.mcp.json`（type http, url `https://mcp.firecrawl.dev/v2/mcp`）。可用工具：`scrape`（抓单页）/ `search`（搜索）/ `interact`；`crawl`/`extract` 需升级付费 Key（采集层暂不需要）。作 NewsNow / 今日热榜 / 公众号 / SoPilot 长文抓取主路径。
- ⏳ **小红书实战**：doctor 显示 opencli 可用，但拉真实数据需 OpenCLI Chrome 扩展已装 + Chrome 登录 xiaohongshu

## 与 collect.py 的关系
`scripts/collect.py` 当前实现「SoPilot RSS + Exa 搜索」两条源。本技能接管后，采集编排以本技能契约为准；`collect.py` 保留为 SoPilot 源实现，其余入口 / 信号源待接工具后由本技能统一编排（后续可扩展为 `collect.py` 支持多源驱动）。

## 稳定性规则（冻结）
- 聚合站可能改版 / 失效：每次抓取校验"提取条目数 > 10"，低于则告警并回退自建抓取（GitHub / HN 有官方页），失效事件记 `lessons.md`
- 小红书信号源失效（登录态过期 / 扩展未装）：告警，跳过该源，不阻断其他入口
- 每周目标：正文 40–60 篇 + 标题信号 30–50 条 + 封面信号 20–30 张
