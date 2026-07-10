---
name: ziliaoku-publish-gzh
description: 公众号发布编排（封面 + 排版 + 预览链接）。把 draft(platform=wechat) 的成稿接成"可复制链接发公众号"的完整产物——封面图用 cover-anchor-system(ponyo) 封面系统出、正文用摸鱼绿排版生成器出、预览页带"复制到公众号"按钮。用户打开链接复制即可贴公众号后台。This skill should be used when the intent is "发公众号 / 出公众号稿"。
agent_created: true
---

# ziliaoku-publish-gzh — 公众号发布编排

## Purpose
把 `draft(platform=wechat)` 的成稿，变成"打开链接→复制→贴公众号"就能发的完整产物。
解决两件事：① 公众号**封面图**按品牌规范出（不再随手 16:9）；② 正文按**摸鱼绿排版**出、带一键复制按钮（和之前 gzh_ecc 流程一致，已搬进项目 `scripts/gzh_publish/`）。

> 账号安全：本技能只产出"封面图 + 排版预览链接"，**不碰公众号后台、不自动发布**。用户自己复制粘贴。

## When to use
- run.md 的意图 "发公众号 / 出公众号稿" 触发。
- 输入：`draft(platform=wechat)` 的成稿（通常是 `output/posts/{日期}/{slug}_wechat.md`）。

## 三段流程（每一步都有用，不多跑）

### ① 封面图（用 cover-anchor-system / ponyo 精华）
- 调项目级技能 **cover-anchor-system**（`.workbuddy/skills/cover-anchor-system/`，ponyo「信息密度 × 视觉锚点」封面系统精华，2026-07-10 接入；替代之前的 punk-cover）。
- 工作流（按 ponyo 方法论，不要自己手搓 ImageGen prompt）：
  1. 读 `references/template-formulas.md` 选模板：公众号 AI 工具/干货文默认**数字型**（大号数字锚点×色块分割×悬念副标题）或**冲突型**（反直觉标题×强对比色）；诊断旧封面读 `references/cover-diagnosis-checklist.md`。
  2. 读 `references/finished-cover-prompts.md` 拿对应模板的成品提示词结构（画布/锚点位置/字重层级/配色 HEX/约束）。
  3. 确认平台比例：**公众号 = 2.35:1**（900×383）。
  4. 编译融合提示词：按 ponyo 输出规范给 模板类型+理由 / 锚点位置 / 配色(HEX) / 字重层级 / 生图提示词。存 `output/posts/{日期}/cover-assets/{slug}/prompts/cover.md`。
  5. 调 **ImageGen** 出图：
     - **`size: 1410x600`**（2.35:1 直出），`quality: high`。
     - **图内不放文字**：提示词写明 `NO text / NO letters / NO words`——ponyo 原版让 AI 出"成品带字"，但实测生图引擎写中文必乱码，标题绝不能交给生图引擎。
- **PIL 叠中文标题**（生图后必做，保证文字 100% 清晰不乱）：
  - 左侧做渐隐底（off-white alpha 0→238），保证文字区干净。
  - 用 **SimHei 黑体**（`C:\Windows\Fonts\simhei.ttf`）写主标题+副标题+顶部标签+底部徽章；主标题关键词可用品牌色点色。
  - 参考脚本：`output/posts/2026-07-10/punk-assets/punk-cover/awesome-llm-apps/add_title.py`（可复用，目录名改 cover-assets）。
  - 存 `output/posts/{日期}/cover-assets/{slug}/cover.png`（2.35:1 中文成品图）。
- **punk-cover 降为备用**：要商业杂志头版/黑红剪影等特定风时，可改回 `~/.workbuddy/skills/Punk-Skill/skills/punk-cover`（其自定义风格也可注入摸鱼绿品牌色）。默认走 ponyo。
- 约束：单张大图、标题可读、无假刊头/Logo/股票大屏/廉价财经模板。

### ② 正文排版（摸鱼绿生成器）
- 脚本在 `scripts/gzh_publish/`：`gzh_style.py`（通用样式库）+ `make_preview.py`（包预览页）。
- 每篇公众号稿对应一个 `gen_{slug}_html.py`（数据驱动：COVER/PARTS/章节内容写死在脚本里，套 `gzh_style`）。
  - 已有示例：`gen_awesome_html.py`（awesome-llm-apps 合集）。新文章复制它改名改内容即可。
- 跑 `gen_{slug}_html.py` → 出 `scripts/gzh_publish/{slug}_gzh_排版_摸鱼绿(moyu-green).html`。
- 跑 `make_preview.py {slug}_gzh_排版_摸鱼绿(moyu-green).html` → 包成带"📋 复制到公众号"按钮的 `_预览.html`。
- 正文顶部自带**文字封面卡**（build_cover），与 ① 的封面图互补；封面图单独传公众号后台"封面图"字段。
- **正文插图**（可选）：长文可插入 ian-xiaohei 小黑 16:9 插图（由 `ziliaoku-image` 路由出），让正文有记忆点。插图存 `output/posts/{日期}/illustrations/{slug}/`，在 gen 脚本里用 `<img>` 引用。

### ③ 预览链接
- 在 `scripts/gzh_publish/` 起本地服务：`python -m http.server 8766 --bind 127.0.0.1`。
- 给 URL：`http://127.0.0.1:8766/{slug}_gzh_排版_摸鱼绿(moyu-green)_预览.html`。
- 用户打开 → 点"📋 复制到公众号"（或 Ctrl+A/Ctrl+C）→ 进 `mp.weixin.qq.com` 新图文 → 正文粘贴 → 封面图单独传 ① 出的 2.35:1 图 → 发布。

## 与冻结接口的关系
- 不修改 9 段任何 I/O 契约；本技能是 `publish` 在 **wechat 通道**的具体实现（编排层）。
- `image` 阶段的"公众号封面"职责由本技能第①步（cover-anchor-system/ponyo）承担，run.md 的 wechat 路由指向本技能。

## 硬性要求
- 封面必须 2.35:1（900x383），不得 16:9 直接当封面。
- 默认封面走 ponyo（cover-anchor-system）；punk-cover 为风格备选。
- 绝不自动发布、绝不要求用户交 appid/secret（不用 wechat-publisher 草稿箱那条）。
