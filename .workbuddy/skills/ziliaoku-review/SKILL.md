---
name: ziliaoku-review
description: 周复盘（Prompt-D）。分析本周发布数据（小眼睛/点赞/收藏/评论/涨粉），更新 formulas.md 与 image-styles.md 权重，输出 reviews/{week}.md，并联动各入口 collect 率与 discard 率。This skill should be used weekly after publishing, to close the loop and tune the upstream pipeline.
agent_created: true
---

# ziliaoku-review — 周复盘（Prompt-D）

## Purpose
用真实发布数据反哺流水线：哪条好（强化其公式 / 封面）、哪条差（定位是选题 / 执行 / 门面问题）、关键词怎么调、入口质量如何。这是"先冻结接口、让缺口自己暴露"的收口环节。

## When to use
- 每周一次（建议周日），用户填入本周发布数据后。

## 输入
- 本周发布数据：标题、选题 ID、套用公式、小眼睛 / 点赞 / 收藏 / 评论 / 涨粉。
- `formulas.md`、`image-styles.md`（待更新权重）。
- `ziliaoku-gate` 本周统计：各入口 `collect` 率（按 `source_platform` 分组）、总体 `discard` 率。
- `keywords.md`（待增删建议）。

## 输出契约（冻结，写入 reviews/{week}.md）
```markdown
# 周复盘 {week}

## 1. 最好1条
- 公式/结构 → formulas.md 权重 +1
- 封面风格 → image-styles.md 标注"验证有效"

## 2. 最差1条
- 问题归类（三选一）：选题问题(evidence弱) / 执行问题(文案) / 门面问题(标题或首图)
- 依据：...（首图点击差和文案差是两种病，分开治）

## 3. keywords.md 增删建议
- ...

## 4. 账号档案微调
- （连续2周同类差才调向，单周不动）

## 5. 入口质量联动
- 各入口 collect 率（按 source_platform）：...
- 总体 discard 率：... ；若 >60% 连续两周 → 调上游初筛词，不是调严质检
```

## 硬性要求
- 最好 / 最差各只取 1 条，且必须给依据，禁止"感觉"。
- 最差条必须明确是**选题 / 执行 / 门面**三者之一，不混谈。
- `discard` 率 > 60% 连续两周 → 结论是"调上游初筛词"，**不是**把质检改严。
- 账号档案连续 2 周同类差才微调，单周波动不动。

## 副作用（执行时同步更新）
- 好条对应的公式 → `formulas.md` 该条权重 +1。
- 好条封面风格 → `image-styles.md` 标注"验证有效"。
- 增删建议 → 经用户确认后改 `keywords.md`。

## 工具依赖
纯 LLM 分析，不需外部工具。当前环境即可运行。
