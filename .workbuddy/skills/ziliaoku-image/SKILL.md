---
name: ziliaoku-image
description: 配图提示词生成（Prompt-F）。基于 ziliaoku-draft 产出的 final_title 与 image_briefs，逐张生成中文图像生成提示词（一图一信息 + 风格锚定 + 3:4 + 负面约束），首选即梦 API 出图（支持中文渲染），输出到 output/posts/{日期}/。This skill should be used after ziliaoku-draft, to turn image briefs into concrete generation prompts.
agent_created: true
---

# ziliaoku-image — 配图（Prompt-F）

## Purpose
把 `ziliaoku-draft` 的 `image_briefs` 翻译成可落地的图像生成提示词，并与 `image-styles.md` 的风格库强绑定。强调"一图一信息"和**中文文字稳定渲染**。

## When to use
- `ziliaoku-draft` 产出 `image_briefs` 后，说"出图 / 配图 / 生成封面"。
- **译介帖的"图承载"**：`ziliaoku-draft` 走「模式 B 译介英文」时，说"出长图 / 渲染译介长图"——此时出的是**竖版长图**（全部翻译 + 我的理解），不是 3:4 封面。

## 输入
- `final_title` + `image_briefs`（来自 draft 输出）。
- `image-styles.md`（选定风格 A / B / C 的描述）。
- 小红书封面信号库 `data/image-styles/{date}_xhs_covers.jsonl`（提炼封面模式参考，来自 ziliaoku-collect 小红书信号源）。

## 输出契约（冻结，逐张写入 output/posts/{YYYY-MM-DD}/，每张一个提示词块）
对每张图输出一段中文图像生成提示词，必须包含 5 个部分：
```
1. 画面主体：这张图传达的一个核心信息（从 image_brief 提取，一图一信息，禁止塞多点）
2. 文字内容：图上要渲染的确切文字（≤15字/处，最多2处文字区）
3. 风格锚定：引用 image-styles.md 的具体风格描述（构图 + 配色 + 字体感觉）
4. 尺寸：3:4 竖版（小红书 / 公众号封面）
5. 负面约束：不要多余英文、不要乱码文字、不要水印、不要过度装饰元素
```

## 生成方式（用户 2026-07-08 决策更新）
> 用户决策：**不装 ComfyUI**；**生图走内置 ImageGen 能力（对话多模态），暂不配即梦 Key**。即梦作为可选中文渲染升级，待用户配 Key 时再启用。

- **当前首选：ImageGen 内置能力**（对话内多模态生图，中文渲染可用，零额外 Key、随调随用）。
  - draft 出稿后直接由 ImageGen 按本技能提示词逐张出 3:4 封面/配图。
  - 出图后压缩到 <500KB（Pillow resize 宽 720 + JPEG q85 ≈ 117KB），再交给发布器（避免大图 payload 拖垮 CDP 桥接，之前 opencli 踩过此坑）。
  - 中文文字若抖动：走"ImageGen 出无文字底图 + 程序化叠字（PIL 写字）"兜底。
- **可选升级：即梦 API（Dreamina，中文渲染更稳）**——仅当用户后续配 `DREAMINA_API_KEY` 时启用，作封面文字清晰度升级，非必选。
- **不启用：ComfyUI（localhost:8189）**——用户明确不装。

## 译介长图（Pillow 渲染，区别于 ImageGen 封面）
> 仅在 `ziliaoku-draft` 走「模式 B 译介英文」、需要"图承载"全部翻译 + 理解时启用。此图是**信息图**，不是营销封面，故不走 ImageGen，而用脚本精准排版（保证中英文不糊、分节清晰）。

- **渲染脚本（可复用模板）**：`scripts/gen_longimage_reddit.py`（已实跑产出 `1080×~2400` 长图）。换素材时只改脚本里的 `blocks` 列表（每行 `("kind", "text")`，kind ∈ `title/h/body/quote/note/src/sep`），无需重写排版逻辑。
- **字体**：优先 `C:\Windows\Fonts\msyh.ttc`（Microsoft YaHei）；粗体 `msyhbd.ttc`；兜底 `simhei.ttf` / `simsun.ttc`。
- **尺寸**：宽 `1080`，竖版自适应高度；单图上传小红书即可（实测长图作单图可行）。
- **排版纪律**：CJK 单字 + 英文词分词自动换行；章节用 `h` + `sep` 分隔；引用原文用 `quote`、我的理解用 `note` 区分视觉层级；底部 `src` 标注来源（译介 + 个人理解，非原帖立场）。
- **注意**：长图标题与发布页 `final_title` 可不同（长图标题可更长更完整），但都守"不提私有内部系统"红线。

## 封面与插图技能路由（2026-07-10 接入 ponyo + ian-xiaohei）

本段是 image 阶段"封面/插图选型"前置——先决定用哪套模板，再走下面"生成方式"出图。两套精华已入项目 `.workbuddy/skills/`。

### 封面 → cover-anchor-system（ponyo 精华）
- 位置：`.workbuddy/skills/cover-anchor-system/`（SKILL.md + references/）。
- 方法论：**信息密度 × 视觉锚点**——封面要 3 秒让人决定点不点，不是"好看"。
- 流程：
  1. 读 `references/template-formulas.md` 选模板（冲突型/数字型/截图型/情绪型 + 涂鸦/阳光拼贴两生活风）；AI 工具/干货类默认**数字型**或**冲突型**。
  2. 读 `references/finished-cover-prompts.md` 拿对应模板的成品提示词结构（画布/中文文案/锚点位置/字重层级/配色/约束）。
  3. 按 ponyo 输出规范给：模板类型+理由、锚点位置、配色(HEX)、字重层级、生图提示词。
  4. 旧封面要改？读 `references/cover-diagnosis-checklist.md` 打分（信息密度/视觉锚点/缩略图可读性）出改版提示词。
- **平台尺寸**：小红书 3:4(1080×1440)、公众号头图 2.35:1(900×383)、公众号次图 1:1(500×500)。
- **中文叠字铁律不变**：ponyo 原版让 AI 出"成品带字封面"，但实测生图引擎写中文必乱码 → 仍按本技能"生成方式"的**无字生图 + PIL 叠中文**纪律执行（提示词写 `NO text`，标题后期 PIL 叠）。ponyo 提供模板/锚点/配色方法论，文字仍后期叠。
- **punk-cover 降为备用**：封面首选 ponyo；punk-cover（`~/.workbuddy/skills/Punk-Skill/skills/punk-cover`）作为风格备选（要商业杂志/黑红剪影等特定风时再用）。

### 正文插图 → ian-xiaohei-illustrations（小黑精华）
- 位置：`.workbuddy/skills/ian-xiaohei-illustrations/`（SKILL.md + references/）。
- 用途：公众号长文/小红书长图的**正文内插图**（不是封面），把文章认知锚点（判断/流程/隐喻）画成 16:9 白底手绘小黑图。
- 流程：
  1. 读 `references/style-dna.md`（风格 DNA：纯白/手绘/留白/红橙蓝批注/禁忌）+ `references/xiaohei-ip.md`（小黑形象动作库）。
  2. 读 `references/composition-patterns.md` 选结构类型（Workflow/前后对比/概念隐喻/方法分层等），从当前文章**重新发明隐喻**，不照抄案例。
  3. 按 `references/prompt-template.md` 单张生成提示词（16:9/纯白/小黑承担核心动作/最多5-8处中文标注/不写类型标题）。
  4. 生成后按 `references/qa-checklist.md` 检查（小黑是否装饰化/画面太满/像PPT/中文错字/左上角标题）。
- 一篇文章默认 4-8 张，短文 1-3 张；够用就好，别做成画册。
- **中文标注越短越稳**：小黑图里中文用 PIL 叠或让生图引擎写极少量（≤8字/处），多了必乱。

### 与 ziliaoku-publish-gzh 的关系
- 公众号封面由 `ziliaoku-publish-gzh` 第①步统一调本路由的 ponyo 出 2.35:1；正文插图由本技能直接出（draft 阶段 image_briefs 标注"插图"的走 ian）。

## 硬性要求
- 一图一信息：禁止在一张图里塞多个核心信息。
- 文字 ≤ 15 字 / 处，最多 2 处文字区。
- 必须引用 `image-styles.md` 的具体风格（构图 + 配色 + 字体感觉），不凭空发明风格；优先参考小红书封面信号库提炼的当红封面模式。
- 成品与文案同目录 `output/posts/{YYYY-MM-DD}/`。

## 工具依赖
- **ImageGen 内置能力**：当前实跑生图走此（零额外依赖）。
- 即梦 API（Dreamina）：可选升级，用户配 `DREAMINA_API_KEY` 后启用（中文渲染更稳）。
- ComfyUI（localhost:8189）：不装。
- Pillow（压缩封面至 <500KB，防 CDP payload 拖垮）：managed venv 已装（12.3.0）。
