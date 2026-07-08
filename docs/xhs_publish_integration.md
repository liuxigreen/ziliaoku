# 小红书半自动发布接入方案（white0dew/XiaohongshuSkills）

> 评估来源：https://github.com/white0dew/XiaohongshuSkills （3139★，基于 Chrome DevTools Protocol 的小红书自动化工具，支持 OpenClaw/Codex/CC 等 Agent 调用）
> 决策前提（用户 2026-07-08 明确）：**保持半自动——AI 写稿 + 人手动点发布，不接自动发布**；**生图走内置 ImageGen 能力，暂不配即梦 Key**。

## 一、这个仓库有什么（与我们流程相关的能力）
- `publish_pipeline.py --preview`：填好标题/正文/图片，**只填不点发布**（有窗口预览模式）—— 正是"半自动"终态。
- `cdp_publish.py content-data`：抓取笔记基础信息表（曝光/观看/点赞/收藏/评论），**导出 CSV** —— 直接喂我们的 `ziliaoku-review` 周复盘。
- `cdp_publish.py search-feeds` / `get-feed-detail`：搜索笔记 + 抓详情（含 `--load-all-comments`）—— 补 firecrawl 抓不到小红书正文的缺口，辅助 `ziliaoku-decode`。
- `get-notification-mentions` / `post-comment-to-feed` / `respond-comment`：评论与 @ 通知抓取 + 发评/回评 —— 接"评论维护"需求（纯读取/人工发，不脚本自动刷评）。
- 多账号 Cookie 隔离、登录态缓存 12h、适配 2026-02/03 创作者中心 DOM 改版（比我们之前的 opencli 发布链路更稳，opencli 有 `files` 属性重定义 bug 卡死）。

## 二、接入原则（守我们红线，不破坏冻结接口）
1. **不接自动发布**：绝不使用 `--headless` 自动点发布。只用 `--preview` 填好，人最后手动点。账号安全握自己手里（人设：实操、接地气、不画饼）。
2. **生图走 ImageGen（内置能力）**：不配即梦 Key。draft 出稿后由 ImageGen 生封面/配图，压缩到 <500KB 再交给发布器（避免大图 payload 拖垮 CDP 桥接，我们之前踩过这个坑）。
3. **数据抓取是主价值**：`content-data` 抓真实曝光/点赞回填 `reviews/{week}.md`，解决 review "真实数据待回填"硬伤；评论抓取只读取不自动刷。
4. **独立部署，不污染项目 git**：该仓库是独立 Python 工具（有自己的 requirements.txt / venv），**clone 到项目外**（如 `D:\tools\XiaohongshuSkills`），不作为子模块进 `ziliaoku` 仓库。ziliaoku 的 git 纯文本结构不变。

## 三、四处对接点
| # | 对接点 | 用仓库的什么 | 进我们哪段 | 状态 |
|---|---|---|---|---|
| 1 | 半自动填稿 | `publish_pipeline.py --preview` | 替代 opencli 卡死发布链路 | 待 clone 实测 |
| 2 | 周复盘数据回填 | `cdp_publish.py content-data` → CSV | `ziliaoku-review` 填真实指标 | 待 clone 实测 |
| 3 | 评论维护（读取） | `get-notification-mentions` / `get-feed-detail` | 人工评论参考，不自动刷 | 待 clone 实测 |
| 4 | decode 抓小红书正文 | `search-feeds` / `get-feed-detail` | `ziliaoku-decode` 一手源补充 | 待 clone 实测（firecrawl 抓不到 xhs 正文） |

## 四、部署步骤（待用户确认后执行）
1. `git clone https://github.com/white0dew/XiaohongshuSkills.git D:\tools\XiaohongshuSkills`（项目外，不进 ziliaoku git）。
2. 独立 venv 装依赖：`python -m venv D:\tools\XiaohongshuSkills\.venv` + `pip install -r requirements.txt`（Python 3.10+，我们环境 3.12/3.13 满足）。
3. 首次登录：`python scripts/chrome_launcher.py` 有窗口扫码（用养号小号，不碰主号）。
4. 跑通 `--preview` 填稿 → 人手动点发布；跑通 `content-data` 抓数据回填 review 模板。
5. 把调用方式固化进本项目 `docs/account_ops_sop.md` 的"发布"节 + 更新 `ziliaoku-image` 技能备注（生图走 ImageGen）。

## 五、风控与纪律（仓库自身警告，必须守）
- 平台风控/限流/封号风险真实存在；仅测试号验证、控制频率、人工复核最终内容。
- 半自动（人点发布）风险最低；绝不开 `--headless` 全自动。
- 评论只读取 + 人工发，不脚本批量刷评（避免触发风控 + 守"账号安全握自己手里"人设）。

## 六、结论
**能接入，且契合半自动终态**。最大价值不是发布（我们本来就不自动发），而是：
- **content-data 真实数据回填 review**（解决复盘空模板硬伤）；
- **search-feeds/get-feed-detail 抓小红书爆款正文**（补 decode 一手源，firecrawl 抓不到 xhs）；
- **--preview 稳定填稿**（替代 opencli 卡死链路，适配 2026 改版）。

生图按用户决策走 ImageGen 内置能力，即梦暂不配。
