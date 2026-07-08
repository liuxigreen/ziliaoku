---
name: ziliaoku-gate
description: 爆文资料库入库质检闸门（Prompt-A0 / topic-library-gate）。对一篇已采集的爆文判断其是否值得进入选题资料库，输出 collect / hack_only / signal / discard 四态 verdict 与 reusable_core。This skill should be used after ziliaoku-collect and before ziliaoku-extract, to gate every raw post before it enters extraction.
agent_created: true
---

# ziliaoku-gate — 入库质检（Prompt-A0 / topic-library-gate）

## Purpose
在采集与提取之间设一道闸门：爆文的数字表现（发布≤14天、点赞>2000、粉丝<5000 等）已由采集层机判达标，本技能只判断**内容层面的可复用性**——它爆的原因能不能被抽象成公式 / 结构 / 钩子手法。不过闸的不进入 `ziliaoku-extract` 提取。

## When to use
- 每采集到一篇爆文，过闸一次。
- 批量处理：逐篇调用，不过闸的不进入提取。

## 输入
读取 `data/raw/{YYYY-MM-DD}/{序号}_{platform}.md` 的 frontmatter 与正文。frontmatter 必须含：
- `source_type`: `aggregator_discovery | watchlist | wechat_search`
- `source_platform`: `v2ex | zhihu | github | hn | x | wechat | ...`

## 输出契约（冻结，JSON）
对每篇输出一个 JSON 对象（可追加到 `data/extracted/` 前的临时 gate 结果，或直接作为该篇的质检结论）：

```json
{
  "file": "data/raw/{YYYY-MM-DD}/{序号}_{platform}.md",
  "verdict": "collect | hack_only | signal | discard",
  "reason": "一句话，引用内容中的具体证据，禁止'质量不高'式空话",
  "reusable_core": "最值得偷的一个东西（collect / hack_only / signal 时填，一句话）",
  "from_comments": true
}
```

## 收录标准（全部满足才收 collect）
1. **爆因可迁移**：爆的原因能抽象成方法（公式 / 结构 / 钩子），换个人、换个话题也能复用。
2. **有明确目标人群和价值承诺**：能一句话说清"写给谁、给了什么"。
3. **有正文实体**：有可拆解的行文结构，不是纯靠图片 / 视频 / 评论区撑起来的壳。
4. **一手性**：作者是"做了这件事的人"（有截图 / 数据 / 命令 / 踩坑细节）。转述型内容即使爆了也最高判 `hack_only`。

## 新信源特别规则
- **GitHub 条目（三通道，2026-07-08 升级）**：
  - **watch 个人收藏**（`source_type: github_curated`，来自 `data/github_watchlist.md`）：用户人工背书 = 最高质量信号，**无条件 `verdict: "collect"`**（绕过 star 阈值）。`curated_note` 作为 reusable_core 的重要来源。
  - **topic 高 star 正文**（`source_type: github_discovery`）：高 star(≥**2000**) + 近期活跃(pushed_at 近 180 天) + README 讲「怎么用 / 适用场景 / 有代码示例」→ **`verdict: "collect"`**（进 `ziliaoku-extract` 做「神库推荐 / 工具盘点」选题，自带 star 数字背书）。
  - **trending 风向标**（`source_type: github_trending`，来自 `data/signal/`）：本就是 signal 通道产物，**不进爆文库**，下游 `ziliaoku-signal` 直接消费；如某 trending 库同时 README 质量极高且 ≥2000★，可升级为 collect（由 signal 技能二次判定）。
  - 纯公告 / release / 无介绍代码库 / 软广卖课 → `signal` 或 `discard`。
  - ⚠️ README 常有营销腔（leading / superior），extract 时须去营销化、落实操；守红线：不写收益数字、不绝对化。
- **HN / V2EX 帖**：高赞评论可能比正文值钱，质检时正文 + 前 5 条高赞评论一起判，评论中的一手经验可单独收（标 `"from_comments": true`）。
- **热榜标题（未抓全文的）**：不走质检，直接进 `data/titles_pool.jsonl`（纯标题样本库，供聚类提炼公式用，与正文库分开）。

## 直接丢弃（命中任意一条 → discard）
- 爆因不可复制：人设红利、名人效应、独家信源。
- 纯情绪宣泄 / 站队：无结构可拆。
- 时效死内容：绑定具体日期 / 版本 / 活动（蹭法有价值则判 `hack_only`）。
- 融资新闻、公司八卦、无实测转述、"AI 将改变 XX"展望文。
- 软广伪装干货（价值承诺最终导向购买）。
- 同一账号本周已收录 2 篇。

## 硬性要求
- `reason` 禁止写"质量不高"这类空话，必须指出命中哪条标准 / 哪条丢弃规则。
- 拿不准的判 `collect`：宁可库里多一篇平庸的，不错杀一篇有用的；下游聚类（样本 < 3 标弱信号）和周复盘（公式权重增减）负责去伪存真。入口闸门只拦明显的垃圾，拦太狠会把样本量饿死。
- `hack_only` 是中间态：热点本身会过期但"蹭法"是公式，值得单独收（只提取手法，不进爆文库）。

## 工具依赖
纯 LLM 判断，不需外部工具。当前环境即可运行（用 `data/raw/2026-07-07/` 现有样本即可实测）。

## 与周复盘联动
`ziliaoku-review` 统计各入口 `collect` 率（按 `source_platform` 分组）与总体 `discard` 率；`discard` 率 > 60% 连续两周 → 调上游初筛词，不是调严质检。

## ★ 发布前合规自检（publish_check 模式，2026-07-08 新增）
> **为什么做**：入库质检（上面四态）管"值不值得收"，但不管"发出去会不会被限流"。竞品 7 步第 6 步有独立"合规检查 Prompt"扫绝对化/收益承诺/硬引流。咱们红线散在 `account.md` + `draft` 去AI味规则里，缺一道**发布前的自动红线扫描关卡**。限流=掉粉，这道关比入库关更贴近"涨粉"目标。

- **触发**：`ziliaoku-draft` 出稿后、用户终审前，必经一次 `publish_check`。
- **输入**：`output/posts/{日期}/{slug}.md`（成稿 draft 的 `final_title` + `body` + `cta` + `tags`）。
- **检查清单**（逐条扫，命中即列）：
  1. **绝对化用语**：最 / 第一 / 唯一 / 全网 / 必 / 一定 / 100% / 绝对 / 史上
  2. **收益承诺 / 数字**：具体金额、收益数字、"月入 X""赚 X 元""X 天见效"（除非是引用他人案例且标注）
  3. **硬引流**：直接留微信 / 私信我 / 加我 / 主页有链接（合规应为提问式 `cta`，不直给联系方式）
  4. **AI 味残留**：开头套话（"在当今时代/随着AI发展"）、禁用词（赋能/抓手/闭环/颗粒度/底层逻辑）、单句过长（>25字）、无口语化/无个人经历细节
  5. **平台合规**：小红书违禁词（诱导点赞/关注、医疗断言等）、公众号夸大（标题党）
- **合规替代表**（命中即按表给替换词，不只报错；`issues[].suggest` 优先取此表）：
  | 红线词类型 | 示例 | 合规替换 |
  |---|---|---|
  | 绝对化 | 最 / 第一 / 唯一 / 全网 | 我试过的 / 目前见过 / 相对（去绝对化）|
  | 强断言 | 必 / 一定 / 100% / 绝对 | 通常 / 大概率 / 我这边是 |
  | 收益数字 | 月入X / 赚X元 / X天见效 | 删；或改"有朋友做到过，非承诺"并标注引用 |
  | 硬引流 | 私信我 / 加我微信 / 主页有链接 | 提问式 cta："你们用哪套？评论区聊聊" |
  | AI套话 | 在当今时代 / 随着AI发展 | 直接进主题，砍套话 |
  | 黑话 | 赋能 / 抓手 / 闭环 / 颗粒度 | 大白话：帮忙 / 重点 / 全流程 / 细节 |
- **输出**（JSON，写 `data/gate/{日期}_publish_check.jsonl`，每条成稿一行）：
```json
{
  "file": "output/posts/{日期}/{slug}.md",
  "pass": false,
  "issues": [
    {"type":"绝对化","hit":"第一支AI笔","suggest":"改为'我试过的第一支'或去掉'第'"},
    {"type":"硬引流","hit":"主页有微信","suggest":"改为提问式 cta，不直给联系方式"}
  ],
  "verdict": "修改后过 | 重写开头"
}
```
- **硬性要求**：`pass=false` 且有 `issues` 时，**不许发布**，退回 `draft` 改；改完复检直到 `pass=true`。这是人工终审之外的第二道自动护栏。
- ⚠️ 本模式不替代人工终审（红线：自动化的是检查，不是决策权）；它只把明显踩线处标出来，最终发布仍由用户拍板。
