---
week: 2026-W28
date: 2026-07-08
reviewer: AI Agent (ziliaoku-review / Prompt-Review)
status: 框架就绪，真实发布数据待回填
---

# 周复盘 — 2026-W28

> 本文件为 ziliaoku 流水线第 ⑨ 步 review 的周复盘模板。
> 真实发布数据由用户观察后回填（人工卡点），不预填、不画饼。

## 一、本周流量数据（待用户回填）
| 指标 | 数值 |
|---|---|
| 发布篇数 | 1（半自动：AI 写稿 + 人点发布） |
| 发布链接 | https://www.xiaohongshu.com/explore/6a4e09e5000000001503ddf1 |
| 阅读量 | ___ |
| 互动量（赞藏评） | ___ |
| 涨粉 | ___ |
| 评论区是否扣"工作流" | ___ |
| 平台标注"可能含AI生成内容" | 是（正文被标，非封面） |

## 二、选题命中复盘
- 本周选用选题：T21（引流·全自动发帖3个真坑）
- 选题来源：AiToEarn 拆解（signal 通道接入）
- 命中判断：待数据（引流钩子"扣工作流"是否带来互动）

## 三、红线 / 合规自检
- publish_check 初检：`pass=false`（绝对化"最容易"）→ 改"很容易" → 复检 `pass=true` ✅
- 正文被平台标 AI：印证"去 AI 味"规则需强化（规整符号+黑话密度是主因），已固化进 draft SKILL.md
- 字数红线：正文 1143→719 字压缩，合规 ✅
- 画饼句式：原"等测顺了补踩坑"已删除，改为"只陈述已发生事实" ✅

## 四、流程健康度
| 步骤 | 状态 |
|---|---|
| ① collect | ✓ |
| ② gate | ✓（55 collect，AiToEarn 补 signal） |
| ③ extract | ✓（55/55 铺满） |
| ④ cluster | ✓（1 universal + 5 公式 + 3 封面） |
| ⑤ signal | ✓（AiToEarn 进信号） |
| ⑥ topics | ✓（23 选题，漏斗 11/7/5） |
| ⑦ draft | ✓（2 成品 + 去AI味/不画饼固化） |
| ⑧ image | △（内置 ImageGen demo，即梦待 Key） |
| ⑨ review | △（框架就绪，缺真实数据闭环） |

## 五、下周调整建议（待数据后填）
- ___
- ___

## 六、待办（跨周）
- [ ] 接即梦 Key 让配图生产级（imagery_jimeng.py 已就绪）
- [ ] 观察 T21 帖数据，回填本节一/五
- [ ] 铺开更多选题出稿（extract 已就绪，可直接挑 T 出 draft）
- [ ] E 标题分平台（draft 已加 platform 参数，formula 平台特化待补）
