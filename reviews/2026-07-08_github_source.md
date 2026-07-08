# GitHub 作为内容源 · 实测与接入设计（2026-07-08）

> 用户观察：高 star 库的 README 介绍写得很不错，适合当内容源。
> 结论：成立。GitHub 比公众号友好得多，且能同时当「信号源」和「正文素材源」。

## 一、实测三件事（全部成功）

### 1. README 能否抓到且质量好？✅
- 抓 `langchain-ai/langchain` 主页 README：完整拿到标题、一句话定位、Quickstart 代码、生态列表、6 大使用理由、资源区。
- 结构清晰、有可复现代码、有适用场景——**是高质量技术内容源材料**。
- 关键优势：**GitHub README 无反爬验证码**（对比公众号点全文就弹验证），WebFetch 直接拿。

### 2. 高 star 库怎么被发现？✅
- GitHub Topic 页按 star 排序可稳定抓取：`github.com/topics/ai-agents?o=desc&s=stars`
- 实测列出 top 20：affaan-m/ECC(227k) → firecrawl(147k) → langchain(141k) → gemini-cli(106k) → browser-use(103k) → microsoft/ai-agents-for-beginners(68.8k) …（62k~227k）
- 发现层完全可行，且自带「社区投票的热度」背书。

### 3. star 数等结构化信号能否拿？✅（无需 Key）
- `api.github.com/repos/{owner}/{repo}` 匿名可调用（限速 60/h，采集频率低够用）
- 返回：`stargazers_count` / `forks_count` / `description` / `language` / `pushed_at`
- 实测：n8n 195.5k★（今日还在推）、langchain 141k★、llama_index 50.7k★、autogen 59.5k★
- `pushed_at` 是极好的「近期活跃度」信号，可算「star 暴涨/近期活跃」。

## 二、接入 pipeline 的设计

### 通道归属（不破坏入口≤6 纪律）
- GitHub **本就在 signal 风向标通道设计里**（GitHub/工具类走 Prompt-S）。
- 用户提出 README 是优质正文素材 → 升级为 **「signal 发现 + collect 正文」双通道**：
  - **发现/监控层（signal）**：定时扫 `ai-agents` / `ai-agent-framework` 等话题页 + API 拿 star/pushed_at → 发现「什么工具在涨/近期活跃」→ 进风向标。
  - **正文素材层（collect）**：当某高 star 库 README 质量高、契合「AI 实操/推荐好工具」定位 → 抓 README 进 Prompt-A 做「神库推荐/工具盘点」类选题。
- **GitHub 不占 6 个发现入口**——它挂在 signal 通道下当默认源，符合原设计，不触发「新增入口需周复盘缺口」纪律。

### 抓取层
- README：`WebFetch` 抓 `github.com/{owner}/{repo}` 或 raw `raw.githubusercontent.com/.../README.md`（干净无噪声）。
- 发现：WebFetch 抓 Topic 页 + `curl api.github.com`（无需 Key）。

### 质检（gate 四态）判定建议
| 条件 | verdict |
|---|---|
| 高 star + 近期活跃(pushed_at 新) + README 讲「怎么用/适用场景」 | `collect`（进 Prompt-A，做工具盘点选题） |
| 纯公告/release/无介绍代码库 | `signal` 或 `discard` |
| 软广/卖课/营销腔过重无实操 | `discard`（extract 时去营销化也行，但优先 discard） |

### 标题公式（可进 titles_pool）
- 「XX(高 star 库) 是什么 / 为什么 140k 人都在用 / 3 分钟上手」
- 自带 star 数字背书，但需守红线：不写「月入/收益」，不绝对化。

## 三、风险与纪律
- ⚠️ README 常有营销腔（leading/superior），extract 时须去营销化、落实操。
- ⚠️ 入口数≤6 纪律：GitHub 走 signal 通道，不新增发现入口。
- ⚠️ api.github.com 匿名 60/h 限速，采集频率要低（每日 1 次扫话题足够）。

## 四、待确认（用户拍板后落地）
1. 是否把 GitHub 正式接成 collect 正文源（还是仅保留 signal）？
2. 若接 collect：我写 `scripts/collect_github.py`（Topic 页发现 + API 信号 + README 抓取），并改 `ziliaoku-collect` / `ziliaoku-gate` 技能加 GitHub 分支。
3. 监控哪些 Topic：`ai-agents` 起步，是否加 `rag` / `prompt-engineering` / `llm`？
