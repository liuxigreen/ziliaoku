# 系统架构 vs 开源接管（2026-07-13 定稿）

## 决策背景
用户对比 8 个开源库后定调：**发布/排版/起号运营这三块开源已成熟，自研重复造轮子且不如人家；但采集壁垒（opencli 免费直采 X/Reddit/YT/GitHub）开源没有、替代不了，是核心护城河。** 故：开源接管发布/排版/起号端，自研聚焦采集+选题。

## 9 段流水线 ↔ 实现方（新）

| 段 | 原实现 | 新实现（2026-07-13） | 动作 |
|----|--------|----------------------|------|
| collect（采集） | opencli 免费直采 | **不变**（X/Reddit/YT/GitHub） | ✅ 保留（壁垒） |
| gate / signal / cluster / topics | 自研 9 段 | **不变** | ✅ 保留（方法论资产） |
| extract / decode | 自研 | **不变** | ✅ 保留 |
| draft（写作） | 自研 ziliaoku-draft | 自研保留；可借鉴 wewrite 风格学习 | ✅ 保留 |
| image（配图） | cover-anchor(ponyo) + ian-xiaohei | **不变**（我们的资产） | ✅ 保留 |
| publish（公众号排版） | ziliaoku-publish-gzh 自研 | **gzh-design-skill**（开源，用户级） | 🔁 冻结自研，改调开源 |
| publish（小红书图文） | 无独立 skill | ponyo 3:4 + ian + PIL 拼版（暂）；xiaohongshu-ops-skill 封面生成待 key | 🆕 自有顶替 |
| 起号/运营/复盘 | 空缺（review 空壳） | **xiaohongshu-ops-skill**（开源，用户级） | 🆕 补上 |
| 一稿多发改写 | 无 | **wewrite**（`wewrite-rewrite`，开源，用户级） | 🆕 补上（依赖 Claude/OpenClaw 环境） |

## 已安装的开源（用户级 `~/.workbuddy/skills/`）
- `gzh-design-skill`（2k★）：公众号排版引擎，6 主题含摸鱼绿 + 主题生成器 + 双关卡校验 + 一键复制。
- `xiaohongshu-ops-skill`（2.1k★）：小红书运营助手——推荐流/账号/选题/复盘/爆款复刻 + 自动发布（高危，小号先试）。
- `wewrite`（2.8k★）：公众号全流程 + 小红书改写。注意：其 skill 是 Claude/OpenClaw 范式，在本 agent 需适配或在其原生环境用。

## 冻结 / 保留明细
- **冻结（不再维护，旧产物不删）**：`ziliaoku-publish-gzh` 的排版部分（SKILL.md 已改写为编排层+封面约定）；`scripts/gzh_publish/` 摸鱼绿生成器作历史参考。
- **保留（我们的资产，开源无同款）**：`cover-anchor-system`(ponyo) 封面系统、`ian-xiaohei-illustrations` 插图、`ziliaoku-collect` 采集（opencli 免费直采）。
- **待接 key 再说**：xiaohongshu-ops-skill 的 nano banana 封面生成（需 gemini key）；或接本 agent 生图模型。

## 红线（不变）
- 绝不自动发布主号；自动发布仅限小号/测试号验证（XiaohongshuSkills / xiaohongshu-ops-skill 的自动发布）。
- 批量采集/评论点赞属平台风控高危，开源支持也要小号先试。
- 公众号发布只出稿+预览，用户自己复制粘贴，不交 appid/secret。
