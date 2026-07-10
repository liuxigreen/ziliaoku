# 编排层 dispatcher（run.md）

> 意图 → 段序列 映射。复用 9 段冻结 I/O，不破契约。
> 设计原则（用户定）：**整个流程不能太复杂，每一个环节都必须对"起号涨粉"有用；没用的不跑。**

## 你能说的一句话（意图 → 系统跑什么）

| 意图 | 跑哪几段 | 产出 |
| --- | --- | --- |
| "起个新号 / 新平台" | 冷启动流程（见下） | 定位 + 对标 + 草稿储备，进入首发 |
| "今天出一篇小红书 / 公众号" | 日常出稿短回路 | 1 篇可发稿 + 封面 |
| "周复盘" | `review` | 漏斗诊断 + 下周选题权重 |
| "补点素材" | `collect` → `gate` →（周级 `extract`→`cluster`） | 新爆文 / 风向标入库 |

## 日常最短回路（最常跑，只 4 段）

`topics`(勾选) → `draft` → `image` → `publish`

- `gate` 的 `publish_check` 在发布前自动卡红线（第二道护栏）。
- 这 4 段**每天都有用**；`collect` / `extract` / `cluster` 是**周级补给**，不每天跑——避免"堆料不涨粉"（专家团审计结论：算力别堆在采集囤料上）。

## 冷启动流程（新号 / 新平台，按 docs/publish_calendar.md 的 30 天节奏）

1. 定位：`account.md`（定位句 + 红线 + 变现路径）
2. 对标：`collect` + `gate`(signal) + 填 `docs/benchmark_accounts.md`（账号级模式库）
3. 草稿储备：`topics` + `draft` 的"出稿前简报"
4. 首轮发布：`topics` → `draft` → `image` → `publish`
5. 模式放大：`review` → `topics`（改写有效角度）
6. 复盘聚焦：`review`

## 周级补给（不每天跑）

`collect` → `gate` → `extract` → `cluster` → `signal` → `topics`

- 每周 1 次，喂选题库；日常出稿不依赖它实时跑。

## 多平台路由（platform 参数）

- **xhs（小红书）**：`draft(platform=xhs)` → `image(3:4)` → `publish`（半自动填稿，人点发布）
- **wechat（公众号）**：`draft(platform=wechat)` → `ziliaoku-publish-gzh`（封面用 **cover-anchor-system/ponyo** 出 2.35:1 + 摸鱼绿排版 + 复制链接；正文插图用 **ian-xiaohei** 小黑图）→ 用户粘贴进公众号后台（不碰后台、不自动发布）
- **x（推特，预留）**：`draft(platform=x)` → `publish(x)`；开通账号后接 `vendor/launch-pack/skills/x-twitter-cold-start-expert/references/cold-start-framework.md` 的 7 天计划

## 效果回填闭环（topic_id）

每个选题带 `topic_id`（见 `topics` 输出）；`draft` 成稿 frontmatter 携带同一 `topic_id`；`review` 按 `topic_id` 归因发布数据。闭环断点已连通，能知道"哪篇选题带了多少量"。

## 触发方式

- 人工：按本文件调各 skill（或直接让我"按 run.md 出一篇"）。
- 自动化：`automation` 可定时跑 `collect` 每日 + `review` 每周；冷启动 / 出稿仍由人触发（账号安全握自己手里）。
