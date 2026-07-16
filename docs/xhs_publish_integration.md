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
| 1 | 半自动填稿 | `publish_pipeline.py --preview` / `--save-draft` | 替代 opencli 卡死发布链路 | **已跑通（2026-07-09）** |
| 2 | 周复盘数据回填 | `cdp_publish.py content-data` → CSV | `ziliaoku-review` 填真实指标 | 待实测（未跑过） |
| 3 | 评论维护（读取） | `get-notification-mentions` / `get-feed-detail` | 人工评论参考，不自动刷 | 待实测（未跑过） |
| 4 | decode 抓小红书正文 | `search-feeds` / `get-feed-detail` | `ziliaoku-decode` 一手源补充 | 待实测（firecrawl 抓不到 xhs 正文） |

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

## 七、实测记录（2026-07-09 跑通半自动填稿）
> 环境：`D:\tools\XiaohongshuSkills`（项目外，不进 ziliaoku git），独立 `.venv`（managed 3.13.12 + `requests`/`websockets`）；Chrome 固定 `xhs_profile` + 9222 端口常驻。账号=小号「画画的北北」。

### 7.1 跑通结论
- **半自动填稿已跑通**：`publish_pipeline.py --save-draft --title-file ... --content-file ... --images ...` 能把标题、正文、封面图、话题标签**全部填进**创作者中心编辑器（话题标签会被自动识别为真实 `#话题`，非纯文本）。
- **发布动作人手动**：用户在我们填好后，在 PC 窗口点操作栏按钮、再到手机创作中心发布。账号安全握自己手里。

### 7.2 关键修复（重要，否则按钮永远点不到）
- **"存草稿"按钮当前版本文案是「暂存离开」**，不是"存草稿"。原 `_get_draft_button_rect` 搜 `存草稿/存为草稿/保存草稿` 全部 miss。已加 `暂存离开` 关键词。
- **可见性判断 bug**：原代码用 `node.offsetParent !== null` 判可见，但发布操作栏是 `position: fixed`，**fixed 元素 `offsetParent` 恒为 `null`** → 按钮永远被判"不可见"。已改为 `getComputedStyle`（display/visibility/opacity）+ 包围盒 `width/height > 0` 判断，并放宽候选选择器（含 `a` / `div[class*='button']` / `span[class*='button']`）。
- 配套加固：`_click_draft` 轮询延长到 **3 分钟** + 每次滚动页面触发 React 懒挂载；失败则 `Page.captureScreenshot` 存 `draft_fallback.png` 兜底让你手动点。
- 改动文件：`D:\tools\XiaohongshuSkills\scripts\cdp_publish.py`（**项目外，不进 git，重装仓库需重打这两处**）。

### 7.3 其他实测约束
- **标题 ≤ 20 字（硬限制）**：超了发布页红字提示 `21/20`，必须卡在 20 字内（实测把 "AI写的东西都一个味？Reddit老运营拆透了真相" 21字 改为 "Reddit老运营：AI写的东西都一个味" 20字）。
- **长图作单图可行**：竖版 1080×~2400 长图当一张图上传正常，是译介帖"图承载"的标准载体。
- **登录态持久化**：固定 `xhs_profile` + 9222 后，登录 cookie 落在磁盘，不开新窗口、重启电脑也在；登录缓存约 12h，过期重扫一次即可。用完建议 `--kill` 关工具 Chrome 释放端口。

### 7.4 调用示例（填稿 + 存草稿）
```
& "D:\tools\XiaohongshuSkills\.venv\Scripts\python.exe" `
  "D:\tools\XiaohongshuSkills\scripts\publish_pipeline.py" `
  --save-draft --title-file <title.txt> --content-file <content.txt> `
  --images <longimage.png>
```
正文文件末行若写 `#话题 #标签 ...`，pipeline 会自动识别并选为真实话题标签（不用手点）。

### 7.5 草稿箱不在手机同步（2026-07-09 用户实测）
- **现象**：CDP 半自动填稿走的是 **web 版创作者中心**（creator.xiaohongshu.com），存草稿后（「暂存离开」）草稿落在 **web 草稿箱**；在手机 App「我 → 草稿」里**看不到**。
- **根因**：小红书 web 创作者中心草稿箱 与 手机 App 本地草稿是**两套存储**，历史上不互相同步（带 web 上传图的草稿尤甚）。这跟工具有关，是平台行为。
- **结论与做法**：半自动发布的"发布"动作**必须在 PC web 创作者中心完成**（填好的草稿在那儿，人点「发布」即可）。这反而契合"账号安全握自己手里"人设——发布决策权一直在人、在 PC 上。
- **若坚持手机发布**：要么在手机浏览器开 creator.xiaohongshu.com 操作（体验差），要么上手机 App 自动化（脆弱+风控高，不推荐）。当前链路不追求手机发布。
- **长文笔记（2026-07-09 提出）**：部分深读类内容（如 ECC 神库、Claude Code 技巧）适合做成**长文笔记**（正文即全文，不依赖长图）。当前 XiaohongshuSkills 工具只支持「上传图文 / 上传视频」两种 tab，**没有「长文」tab**；若账号有长文入口，需扩展 `_click_long_text_tab` 才能一键填稿。长文正文版内容可直接产出 markdown（`output/posts/.../*_longform.md`），人手动贴进长文编辑器也行。
