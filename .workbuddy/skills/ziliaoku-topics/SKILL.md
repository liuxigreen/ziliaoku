---
name: ziliaoku-topics
description: 每周选题库生成（Prompt-C）。基于本周聚类结果 data/clusters/{week}.json + formulas.md + account.md，生成 20 个选题，输出 output/topics_{week}.md。This skill should be used weekly after ziliaoku-cluster has produced the week's cluster report.
agent_created: true
---

# ziliaoku-topics — 选题库生成（Prompt-C）

## Purpose
把聚类出的"规律"翻译成**人能直接选、能直接写的选题**。每个选题自带标题候选、钩子草稿、结构参考与证据，让用户勾选时 5 分钟搞定。

## When to use
- 每周一次（建议周一），紧接 `ziliaoku-cluster` 之后。

## 输入
- `data/clusters/{week}.json`（行业 / 结构 / 公式 / 趋势）。
- `formulas.md`（标题公式库，套用并标注来源公式）。
- `account.md`（账号人设、红线、变现路径，选题须贴合）。
- 可选：`data/signals/{week}.json`（风向标，作为工具向 / 蹭热点来源）。

## 输出契约（冻结，写入 output/topics_{week}.md，内含 20 个选题的 JSON 块）
每个选题：
```json
{
  "topic": "选题一句话",
  "title_candidates": ["标题1", "标题2"],
  "hook_draft": "开头前3句草稿",
  "structure_ref": "推荐结构骨架（优先 universal）",
  "evidence": "依据：哪几篇爆文 / 哪个升温趋势",
  "fit_score": 8,
  "urgency": "蹭热点(3天内发) | 常青"
}
```

## 硬性要求
- **无 `evidence` 不许出现**任何选题——每个选题必须能追到爆文或趋势。
- `fit_score` < 6 不输出。
- 至少 5 个为**资源型 / 获得感**（冷启动"给"型内容，利于涨粉）。
- **蹭热点排在前**，其余按 `fit_score` 降序。
- 标题候选须**套用 `formulas.md` 公式**并标注来源公式（如「套用公式#3」）。
- 选题须贴合 `account.md` 人设与红线（不提收益数字、不用绝对化用语、不硬引流）。

## 工具依赖
纯 LLM 判断，不需外部工具。当前环境即可运行。
