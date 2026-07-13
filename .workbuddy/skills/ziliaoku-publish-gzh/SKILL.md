---
name: ziliaoku-publish-gzh
description: 【已冻结·2026-07-13】公众号发布编排。排版已改调开源 gzh-design-skill；本 skill 仅保留封面(ponyo)与编排约定，正文排版不再自研。This skill should be used when the intent is "发公众号 / 出公众号稿"。
agent_created: true
status: frozen
---

# ziliaoku-publish-gzh — 公众号发布编排（已冻结，排版改调开源）

> **2026-07-13 状态**：用户决策——发布/排版端改用开源，**自研排版重复造轮子且不如开源**。
> 本 skill 冻结为「编排层 + 封面约定」，不再自研 HTML 排版。正文排版一律交 **gzh-design-skill**（用户级 `~/.workbuddy/skills/gzh-design-skill`）。

## 分工（新架构）

| 职责 | 谁做 | 说明 |
|------|------|------|
| 封面图（2.35:1） | **保留本项目 cover-anchor-system / ponyo** | 我们的资产，开源无同款；公众号 + 小红书 3:4 封面都用它 |
| 正文排版 → 公众号 HTML | **改调 gzh-design-skill** | 6 主题（含摸鱼绿）+ 主题生成器 + 双关卡校验 + 一键复制 |
| 小红书图文排版 | **ponyo 3:4 封面 + ian 插图 + PIL 拼版** | 小红书不粘 HTML，靠出图；生图 key 以后再说 |
| 一稿多发 / 小红书改写 | **wewrite（`wewrite-rewrite`）** | 内容级真改，过原创度门（wewrite 依赖 Claude/OpenClaw 环境） |
| 起号/运营/复盘 | **xiaohongshu-ops-skill** | 推荐流/账号/选题/复盘/爆款复刻 |

## When to use
- run.md 意图 "发公众号 / 出公众号稿" 触发。
- 输入：`draft(platform=wechat)` 的成稿（`output/posts/{日期}/{slug}_wechat.md`）。

## 流程（薄编排，不重造）

### ① 封面图（保留 ponyo）
- 调项目级 **cover-anchor-system**（`.workbuddy/skills/cover-anchor-system/`，ponyo 方法论）。
- 公众号 = 2.35:1（900×383）；小红书 = 3:4（1080×1440）。
- **图内不放文字**，标题用 PIL 叠（SimHei），保证清晰不乱码。
- 约束：单张大图、标题可读、无假刊头/Logo/廉价财经模板。

### ② 正文排版 → 交 gzh-design-skill（不再自研）
- 把成稿 Markdown 交给 **gzh-design-skill**：
  - 题材 → 主题：教程/测评/清单/工具盘点/方法论 → **摸鱼绿**（默认）；对比/创意评测 → 摸鱼票据。
  - 它会读 `references/theme-{标识}.md` 组件库出 HTML，跑 `validate_gzh_html.py` 双关卡校验，包带「复制到公众号」按钮的 `_预览.html`。
- 我们不再维护 `scripts/gzh_publish/` 的摸鱼绿生成器（冻结，旧产物可作参考不删）。

### ③ 预览链接
- gzh-design-skill 产出 `_预览.html`，用户打开 → 点「复制」→ 公众号编辑器粘贴；封面图单独传 ① 出的图。
- 本地预览起服务：`python -m http.server 8766 --bind 127.0.0.1`（如仍需）。

## 与冻结接口的关系
- 不修改 9 段 I/O 契约；本 skill 是 `publish` 在 **wechat 通道**的编排层，排版实现已外移到 gzh-design-skill。
- `image` 阶段"公众号封面"职责仍由 cover-anchor-system/ponyo 承担。

## 硬性要求
- 封面必须按比例（公众号 2.35:1 / 小红书 3:4），不得 16:9 直接当封面。
- 正文排版一律走 gzh-design-skill，不要再手搓 HTML。
- 绝不自动发布、绝不要求用户交 appid/secret。
