---
name: ziliaoku-cluster
description: 每周爆文聚类（Prompt-B）。对一周结构化提取数据做行业 / 结构 / 公式三维聚类 + 封面维度 + 趋势对比，输出 data/clusters/{week}.json，并把 universal 骨架与公式追加到 formulas.md。This skill should be used weekly after ziliaoku-extract has processed the week's gated posts.
agent_created: true
---

# ziliaoku-cluster — 聚类（Prompt-B）

## Purpose
把单篇提取的结构化数据，聚合成可复用的"行业规律 / 结构模板 / 标题公式 / 封面模式"，并对比上周趋势。这是资料库从"一堆爆文"变成"可套用的规律"的关键一步。

## When to use
- 每周一次（建议周一），输入本周全部 `data/extracted/{日期}.jsonl` 条目。

## 输入
- 本周所有 `data/extracted/{YYYY-MM-DD}.jsonl` 行。
- `formulas.md`（已有公式，避免重复，新公式去重后追加）。
- `image-styles.md`（封面模式追加目标）。

## 输出契约（冻结）
主输出 `data/clusters/{week}.json`（如 `2026-W28`）：

```json
{
  "week": "2026-W28",
  "industry_clusters": [
    { "industry": "行业名", "count": 12, "top_title_types": ["痛点型","数字型"], "top_emotions": ["焦虑","获得感"], "common_topics": ["..."] }
  ],
  "structure_clusters": [
    { "template": "痛点场景 → 翻转 → 方法3步 → 结果证明 → 行动号召", "count": 8, "cross_industry": 3, "universal": false }
  ],
  "title_formulas": [
    { "formula": "{人群}别再{错误行为}了，{正确做法}后我{结果}", "applicable_industries": ["AI工具","副业"], "emotion": "爽感", "instances": 5 }
  ],
  "cover_patterns": [
    { "type": "大字报封面", "text_ratio": "标题占图60%", "color_tendency": "高饱和纯色底" }
  ],
  "trend_vs_last_week": {
    "rising_industries": ["..."], "cooling_industries": ["..."],
    "rising_structures": ["..."], "cooling_structures": ["..."],
    "rising_emotions": ["..."], "cooling_emotions": ["..."]
  },
  "weak_signals": ["标注支撑数<3的结论，如 '短视频拆解 弱信号(2篇)'"]
}
```

副输出（追加，不覆盖）：
- `universal: true` 的结构骨架与去重后的标题公式 → 追加到 `formulas.md`（核心资产，只增不删，按周标注）。
- `cover_patterns` 归纳的 2–3 种高频封面模式 → 追加到 `image-styles.md`。

## 聚类维度（冻结）
- **维度1 行业聚类**：按 `industry` 分组，给出爆文数、最高频 `title_type` 与 `emotion`、共性话题。
- **维度2 结构聚类**：`structure` 相似归类，给出结构模板、次数、跨行业数。**跨行业 ≥ 3 次标记 `"universal": true`**（最有价值输出，宁缺毋滥）。
- **维度3 公式提炼**：合并相似 `title_formula`，去重后标注适用行业、情绪、实例数。
- **维度4 封面模式**（新增）：从 `cover_desc` 非空的记录中归纳 2–3 种高频封面模式（构图类型、文字占比、色彩倾向）。
- **趋势对比**：对比上周（读上一 `data/clusters/{上周}.json`）升温 / 退潮的行业、结构、情绪各前 3。

## 硬性要求
- 每个结论**必须标注支撑数量**；样本 < 3 标"弱信号"。
- `universal` 骨架宁缺毋滥，跨行业 < 3 次的不要标 universal。
- 公式去重后再追加 `formulas.md`，避免重复堆积。

## 工具依赖
纯 LLM 判断，不需外部工具。当前环境即可运行。
