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

## 生成方式（冻结，2026-07-07 修订）
> 用户决策：**不装 ComfyUI**，配图改走 **即梦 API（Dreamina）**。

- **首选：即梦 API（Dreamina，支持中文渲染）**。
  - 即梦对中文文字渲染较稳定，可直接出带文字的 3:4 封面，零本地依赖、随调随用。
  - 调用前需用户配 `DREAMINA_API_KEY` 并确认花费；提示词第 2 部分的"文字内容"直接交给即梦渲染。
  - 若即梦渲染的中文仍有抖动：走"即梦出无文字底图 + 程序化叠字（PIL / Canvas 写字）"兜底——底图由即梦生成，叠字用脚本，复用下方叠字规划，不再依赖 ComfyUI。
- **备选（仅当用户后续自建 ComfyUI 时）**：本地 ComfyUI（localhost:8189）出无文字底图 + 程序化叠字。当前默认不启用。

## 硬性要求
- 一图一信息：禁止在一张图里塞多个核心信息。
- 文字 ≤ 15 字 / 处，最多 2 处文字区。
- 必须引用 `image-styles.md` 的具体风格（构图 + 配色 + 字体感觉），不凭空发明风格；优先参考小红书封面信号库提炼的当红封面模式。
- 成品与文案同目录 `output/posts/{YYYY-MM-DD}/`。

## 工具依赖（待接入）
- 即梦 API（Dreamina）：需用户配 Key 并确认花费（首选）。
- ComfyUI（localhost:8189）：用户不装，仅作可选兜底。
- 当前环境可生成"提示词 + 叠字规划"，实跑生图需即梦 API 连线（或用户自建 ComfyUI）。
