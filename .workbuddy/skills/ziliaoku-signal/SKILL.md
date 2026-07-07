---
name: ziliaoku-signal
description: 风向标通道（Prompt-S）。处理 ziliaoku-gate 判为 signal 的 GitHub / 工具类条目，提炼为选题风向信号而非爆文，写入 data/signals/{week}.json，不进入爆文库聚类。This skill should be used on signal-verdict items (typically from the GitHub / 工具类 discovery route) to capture early trends.
agent_created: true
---

# ziliaoku-signal — 风向标通道（Prompt-S）

## Purpose
`ziliaoku-gate` 对 GitHub / 工具类条目判 `signal` 时，它们不是"爆文"（README 是产品文档），但是**高价值的选题风向信号**（star 周增 > 1000 或解决的问题一句话能说清）。本技能把这类条目提炼成可追的趋势信号，走独立通道，不污染爆文库聚类。

## When to use
- `ziliaoku-gate` 输出 `verdict: "signal"` 的条目。
- 每周一次汇总本周 signal 条目。

## 输入
- gate 结论中 `verdict: "signal"` 的篇目（含其 `reusable_core`、`source_platform=github` 等）。
- 原 `data/raw/{日期}/*.md` 的 `star` / 描述 / 问题陈述。

## 输出契约（冻结，写入 data/signals/{week}.json）
```json
{
  "week": "2026-W28",
  "signals": [
    {
      "source": "github | hn | 其他",
      "item": "项目/工具名 或 话题",
      "why_signal": "star周增>1000 / 解决的问题一句话能说清",
      "action_hint": "可做的选题方向（一句话）",
      "evidence": "具体数据或原句"
    }
  ]
}
```

## 硬性要求
- signal 条目**不进入** `data/extracted/` 爆文库，也不参与 `ziliaoku-cluster` 的爆文聚类。
- 但 signal 可作为 `ziliaoku-topics` 的"工具向 / 蹭热点"选题来源之一（在 topics 阶段引用，不混入爆文公式库）。
- 每个 signal 必须带 `evidence`（具体 star 数 / 原句），空话信号不收。

## 工具依赖
纯 LLM 判断，不需外部工具。当前环境即可运行。
