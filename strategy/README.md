# 策略层（strategy）— launch-pack 上游索引

> 本目录是 ziliaoku 的「起号战略层」。上游方法论来自 [launch-pack](https://github.com/chenjin-cmd/agent-skills-launch-pack_)（已 `git clone` 到 `vendor/launch-pack/`，并在 `.gitignore` 排除，便于刷新）。
> 原则：**直接引用上游 playbook，不复制大段文本**，保持可随上游更新。我们只在 `docs/` 下做「融合 + 适配自己漏斗」的二次加工。

## 平台状态

| 平台 | 状态 | 上游 playbook 路径 | 在我们体系里的角色 |
| --- | --- | --- | --- |
| `xhs`（小红书） | **主用** | `vendor/launch-pack/skills/xiaohongshu-account-launch-expert/references/launch-playbook.md` | 引流主阵地 |
| `wechat`（公众号） | **主用** | `vendor/launch-pack/skills/wechat-account-launch-expert/references/launch-playbook.md` | 深读 / 信任蓄水 |
| `x-twitter` | **预留** | `vendor/launch-pack/skills/x-twitter-cold-start-expert/references/cold-start-framework.md` | 用户计划扩展，待开通账号后接入 |
| `douyin`（抖音） | 预留 | `vendor/launch-pack/skills/douyin-account-launch-expert/references/launch-playbook.md` | 暂不入 |
| `channels`（视频号） | 预留 | `vendor/launch-pack/skills/channels-account-launch-expert/references/launch-playbook.md` | 暂不入 |

## 上游 playbook 章节速查（以小红书为例）

| 章节 | 内容 | 我们对接点 |
| --- | --- | --- |
| §9 对标账号筛选 | 对标记录表（10 字段） | `docs/benchmark_accounts.md` |
| §10 选题库 | 任务分类 + 优势来源打分 | `ziliaoku-topics`（任务分类已降为可选备注） |
| §11 笔记简报模板 | 出稿前 12 模块 brief | `docs/brief_template.md` |
| §12 起号日历 | 30 天分阶段 | `docs/publish_calendar.md` |
| §13 数据诊断 | 按失败环节诊断表 | `ziliaoku-review` |

公众号 playbook 对应：§4 对标系统、§5 选题库、§9 首个 30 天起号日历、§10 指标诊断、§11 风险规则与合规替代。

## 与 ziliaoku 流水线的对接

- **topics**：选题任务分类参考 §10；每周组合完整性用我们自己的 `monetization_role` 漏斗配比（引流10/信任6/转化4）。
- **draft**：出稿前简报模板参考 §11（见 `docs/brief_template.md`）。
- **gate**：合规替代参考 wechat §11「高风险诉求 → 处理方式」决策表（见 `ziliaoku-gate` 的 `publish_check`）。
- **review**：数据诊断参考 §13 / wechat §10。
- **冷启动节奏**：`docs/publish_calendar.md`（融合 xhs §12 + wechat §9）。
- **对标拆解**：`docs/benchmark_accounts.md`（融合 xhs §9 + wechat §4）。

## 刷新上游

```bash
cd vendor/launch-pack && git pull
```
