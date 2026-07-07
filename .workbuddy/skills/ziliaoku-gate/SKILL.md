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
- **GitHub 条目**：README 是产品文档不是爆文，不走常规四条标准，改判"选题信号"——`star` 周增 > 1000 或解决的问题一句话能说清 → 直接 `verdict: "signal"`（第四种结果，进风向标层走 `ziliaoku-signal`，不进爆文库）。
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
