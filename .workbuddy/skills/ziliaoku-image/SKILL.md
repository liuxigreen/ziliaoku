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
