---
name: ziliaoku-extract
description: 爆文结构化提取（Prompt-A）。对一篇已过质检闸门（verdict 为 collect / hack_only / signal）的爆文，提取 title / title_type / title_formula / hook / structure / emotion / industry 等结构化字段，追加写入 data/extracted/{日期}.jsonl。This skill should be used after ziliaoku-gate, on each gated post, to produce the structured data that ziliaoku-cluster consumes.
agent_created: true
---

# ziliaoku-extract — 结构化提取（Prompt-A）

## Purpose
把一篇自然语言爆文拆成可 machine-readable 的结构化字段，作为聚类与选题库算法的输入。逐篇执行，每批建议 5 篇。

## When to use
- `ziliaoku-gate` 给出 `collect` / `hack_only` / `signal` 的篇目，逐篇提取。
- 每周集中提取本周全部过闸篇目。

## 输入
- `data/raw/{YYYY-MM-DD}/{序号}_{platform}.md`（已过闸）。
- 其 gate 结论（`verdict` 与 `reusable_core`）作为提取时的重点参考。

## 输出契约（冻结，追加到 data/extracted/{YYYY-MM-DD}.jsonl，每行一个 JSON）
```json
{
  "source_file": "data/raw/{YYYY-MM-DD}/{序号}_{platform}.md",
  "verdict": "collect | hack_only | signal",
  "title": "原标题",
  "title_type": "痛点型 | 数字型 | 对比型 | 稀缺型 | 共鸣型 | 资源型 | 反常识型",
  "title_formula": "抽象成可填空公式，如 '{人群}别再{错误行为}了，{正确做法}后我{结果}'",
  "hook": "开头前3句原文",
  "hook_technique": "钩子手法（反差自曝 / 直接甩结果 / 提问戳痛点 等）",
  "structure": "结构骨架，箭头串联：痛点场景 → 翻转 → 方法3步 → 结果证明 → 行动号召",
  "emotion": "焦虑 | 好奇 | 共鸣 | 爽感 | 获得感",
  "industry": "行业/赛道（一个词）",
  "target_audience": "目标人群（一句话）",
  "value_promise": "向读者承诺了什么（一句话）",
  "why_viral": "爆的核心原因（具体到手法或情绪，禁止'内容优质'式废话）",
  "cover_desc": "若有封面/首图：描述其构图、文字排版、颜色（无则填 null）"
}
```

## 硬性要求
- `title_formula` **必须可填空复用**；所有字段基于原文，**禁止脑补**。
- `why_viral` 必须具体到手法或情绪，禁止"内容优质""选题好"等空话。
- `cover_desc` 字段为新增：采集时顺手记录爆款封面长什么样，喂给 `ziliaoku-image` 的配图系统与 `formulas.md` / `image-styles.md`。
- `verdict` 为 `signal` 的条目仍提取，但标记后由 `ziliaoku-signal` 走风向标通道，不进爆文库聚类。

## 工具依赖
纯 LLM 判断，不需外部工具。当前环境即可运行。
