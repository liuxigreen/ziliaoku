# 采集与发现策略 v5

> 核心原则：从"关键词撒网"改为"聚合站发现 + 定向抓全文"
> 聚合站负责"发现有什么"，agent-reach/firecrawl 负责"抓到全文"
> 热榜标题本身是免费的标题公式样本库，单独存入 titles_pool.jsonl

---

## 一、入口数量纪律

发现层入口固定上限 **6 个**（现有 5 个，留 1 个空位）。
新增入口的唯一依据：周复盘中现有入口连续两周出现明确缺口（某类高价值内容反复靠用户人肉发现、系统漏掉）。
**禁止因为"感觉不够"而加入口**——每加一个入口，质检、去重、复盘的负担都在涨。

---

## 二、五个发现入口

### 入口1：NewsNow（newsnow.busiyi.world）— 中文全景
- **频率**：每日 1 次
- **覆盖**：知乎、微博、B站、虎扑、V2EX 等聚合
- **用法**：抓取聚合页 → 提取条目（标题+源平台+链接）→ 按 keywords.md 赛道词初筛
- **抓取策略**：
  - V2EX、知乎 → 用 agent-reach 或 Jina Reader 抓全文 → 走质检
  - 微博、虎扑 → 只取标题进 titles_pool.jsonl，不抓全文

### 入口2：今日热榜（tophub.today/c/tech）— 技术风向
- **频率**：每日 1 次
- **覆盖**：GitHub Trending、Product Hunt、Hacker News 及常规平台
- **用法**：抓此页提取条目，省去多次单独抓取
- **筛选规则**：
  - GitHub 条目：star 周增 > 1000 或解决的问题一句话能说清 → verdict: signal（走 Prompt-S，不进爆文库）
  - Hacker News：> 200 分 → 抓原文+前5条高赞评论
  - Product Hunt：当日 Top 10 → 抓产品描述和讨论

### 入口3：SoPilot（sopilot.net/zh/hot-tweets）— X 爆帖
- **频率**：每日 1 次（通过 RSS: https://sopilot.net/rss/hottweets）
- **覆盖**：X/Twitter 中文圈爆帖，含爆火概率预测
- **用法**：RSS 抓取 → 按赛道相关性初筛 → 命中的抓推文全文（含长文 Article）
- **与入口4配合**：SoPilot 管"陌生爆帖发现"，watchlist 管"已知作者跟踪"
  - SoPilot 中连续 2 次出现的作者 → 自动提名进 watchlist 候选

### 入口4：作者监控（watchlist.md）— 定向跟踪
- **频率**：每周 2 次
- **覆盖**：X 作者 + 公众号名单
- **用法**：定向抓 watchlist 中作者的最新内容
- **维护规则**：命中+1、连续 4 周零命中移出、高命中作者的互动对象提名候选

### 入口5：Reddit（r/LocalLLaMA, r/StableDiffusion）— 英文深水区
- **频率**：每周 1 次
- **覆盖**：Reddit AI 相关 subreddit 周榜高赞帖
- **用法**：agent-reach 抓取 → 翻译摘要 → 走质检
- **价值**：大量"还没热但马上会热"的一手实测，是抢首发的金矿

### 保留空位：第6入口
- 仅在周复盘中连续两周发现明确缺口时启用
- 候选：即刻（AI 风向早期信号源）、公众号榜单站

---

## 三、平台角色分工（关键认知）

| 平台 | 角色 | 抓什么 | 不抓什么 |
|------|------|--------|----------|
| 公众号（搜狗微信） | 深度正文源（**副业类除外**） | 长文全文 → 走 Prompt-A 拆结构 | 副业/搞钱类（软广率80%，2026-07-07验证，仅抽标题公式进 titles_pool） |
| YouTube | 深度正文源 | 字幕当正文 → 走 Prompt-A | 纯新闻播报类 |
| X/Twitter | 深度正文源 + 信号源 | 长 thread 全文 + 热帖标题 | 纯转发无观点 |
| Reddit | 深度正文源 | 长帖 + 高赞评论 | 提问帖无回答 |
| 小红书 | **信号源（非正文源）** | 标题公式、钩子手法、封面模式 | 正文（内容在图里，抓不到） |
| B站 | 信号源 + 备用正文源 | 标题、播放数据、字幕（如有） | 纯娱乐向 |
| 热榜标题（所有平台） | 标题公式样本库 | 标题文本 → titles_pool.jsonl | 不抓全文 |

---

## 四、热榜标题采集规则（titles_pool.jsonl）

热榜标题是免费的标题公式样本库，与正文库分开存储。

**采集范围**：所有聚合站和搜索结果中的标题（无论是否抓全文）
**存储格式**：
```json
{"title": "标题文本", "platform": "来源平台", "likes": 数字, "date": "日期", "topic_tags": ["标签"]}
```
**用途**：喂给 Prompt-B 聚类时提炼标题公式，不进入正文质检流程

---

## 五、关键词表（辅助筛选，非主要发现手段）

关键词表仍在搜索补充、初筛过滤时使用，但不再是主要发现手段。

### 赛道词（定方向）
- 赛道1：AI工具与效率（主场，权重最高）
- 赛道2：AI视频与AI创作（主场，用户有一手实操）
- 赛道3：自媒体运营（主场）
- 赛道4：副业与搞钱（**降级：仅标题公式信号源，不进 collect 正文库**）— 验证：reviews/2026-07-07_wechat_filter.md 显示副业类公众号软广率80%、collect率0%，正文营养极低，只抽标题公式进 titles_pool
- 赛道5：泛职场（拓流量，按需开启）
- 赛道6：图文金句（跨平台套利源，按需开启）

### 工具/模型名称层（搜这些出干货概率最高）

**大模型/对话AI**：ChatGPT、GPT-4o、GPT-5、Claude、Claude 4、Gemini、DeepSeek、Kimi、通义千问、豆包、Grok、WorkBuddy、Copilot、Perplexity、秘塔搜索

**图像生成**：Midjourney、DALL-E、Stable Diffusion、ComfyUI、FLUX、即梦AI、Ideogram、Leonardo AI、Adobe Firefly

**视频生成**：可灵AI（Kling）、即梦（Dreamina）、Sora、Veo、Runway、Pika、Seedance、海螺AI、Luma、Gen-3

**写作/办公AI**：Notion AI、Gamma、Napkin AI、Kimi写作、秘塔写作猫、WPS AI、飞书智能伙伴

**编程/开发AI**：Cursor、GitHub Copilot、Windsurf、Replit、Lovable、Bolt.new、v0.dev、Claude Code、Devin

**自动化/工作流**：n8n、Zapier、Make（Integromat）、Dify、Coze（扣子）、AI Agent、MCP协议

**剪辑/音频AI**：剪映AI、CapCut、Opus Clip、Descript、HeyGen、ElevenLabs、Suno

### 场景词层（组合搜索用）

**写作场景**：ChatGPT写文案、Claude写长文、AI写小红书、AI去AI味、提示词写作模板
**生图场景**：Midjourney教程、ComfyUI工作流、AI做小红书封面、FLUX写实风格
**视频场景**：可灵AI教程、即梦生视频、AI做短视频、Sora实测、Seedance教程
**编程/搭建**：Cursor编程教程、AI做网站、n8n自动化、Dify工作流搭建
**效率场景**：AI办公提效、AI做PPT、AI整理资料、AI会议纪要

### 内容形式词（精准定位爆文形式）

**教程类**：保姆级教程、手把手教程、从0到1、新手入门
**实测/对比类**：实测、亲测、横评对比、VS、哪个好
**避坑类**：踩坑、避坑、别再XX了、劝退、真相、翻车
**资源/清单类**：合集、清单、工具箱、模板、免费、收藏级
**复盘/结果类**：复盘、一个月、从XX到XX、逆袭、涨粉
**反常识/观点类**：被低估、90%的人不知道、误区、冷知识

### 排除词（搜到直接跳过）
- 卖课文：「限时优惠」「原价XX」「扫码领取」「加老师微信」
- 水文：「赋能」「抓手」「闭环」「底层逻辑」（连用两个=水文）
- 过时文：发布时间 > 30天且无持续互动
- 广告文：全文都在推一个产品且无实操内容

---

## 六、每周轮转计划

| 周次 | 激活赛道 | 重点搜索词方向 |
|------|----------|---------------|
| W1 | 赛道1+2 | ChatGPT/Claude实测 + AI写作去AI味 + ComfyUI教程 |
| W2 | 赛道1+3 | n8n/Dify工作流 + 小红书起号实操 + 爆款标题公式 |
| W3 | 赛道2 + 赛道4(仅标题公式) | 可灵/即梦/Sora实测 + 一人公司 + 副业标题公式抽提 |
| W4 | 赛道1+5 | Cursor/AI编程 + AI工具横评合集 + 效率工具清单 |

每周复盘时由 weekly-reviewer 输出增删建议，动态调整。

---

## 七、稳定性与复盘联动

- 三个聚合站均为第三方，可能改版或失效：每次抓取校验"提取条目数 > 10"，低于则告警并回退到该入口的自建抓取（GitHub/HN 有官方页可直抓），失效事件记 lessons.md
- 周复盘（weekly-reviewer）新增两项：
  - 各入口产出质量：collect 率按 source_platform 分组统计，连续两周 collect 率 < 20% 的入口降低扫描频率
  - discard 率总体 > 60% 连续两周 → 调上游初筛词，不是调严质检
