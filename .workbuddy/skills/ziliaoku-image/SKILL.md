---
name: ziliaoku-image
description: 配图提示词生成（Prompt-F）。基于 ziliaoku-draft 产出的 final_title 与 image_briefs，逐张生成中文图像生成提示词（一图一信息 + 风格锚定 + 3:4 + 负面约束），含 ComfyUI 叠字方案，输出到 output/posts/{日期}/。This skill should be used after ziliaoku-draft, to turn image briefs into concrete generation prompts.
agent_created: true
---

# ziliaoku-image — 配图（Prompt-F）

## Purpose
把 `ziliaoku-draft` 的 `image_briefs` 翻译成可落地的图像生成提示词，并与 `image-styles.md` 的风格库强绑定。强调"一图一信息"和**中文文字稳定渲染**的叠字方案。

## When to use
- `ziliaoku-draft` 产出 `image_briefs` 后，说"出图 / 配图 / 生成封面"。

## 输入
- `final_title` + `image_briefs`（来自 draft 输出）。
- `image-styles.md`（选定风格 A / B / C 的描述）。

## 输出契约（冻结，逐张写入 output/posts/{YYYY-MM-DD}/，每张一个提示词块）
对每张图输出一段中文图像生成提示词，必须包含 5 个部分：
```
1. 画面主体：这张图传达的一个核心信息（从 image_brief 提取，一图一信息，禁止塞多点）
2. 文字内容：图上要渲染的确切文字（≤15字/处，最多2处文字区）
3. 风格锚定：引用 image-styles.md 的具体风格描述（构图 + 配色 + 字体感觉）
4. 尺寸：3:4 竖版（小红书）
5. 负面约束：不要多余英文、不要乱码文字、不要水印、不要过度装饰元素
```

## 生成方式（冻结）
- **首选：本地 ComfyUI（localhost:8189，用户已有，零成本）**。
  - **关键**：AI 直接渲染中文文字目前仍不稳定 → 改为"生成无文字底图 + 程序化叠字"（PIL / Canvas 写字，字体位置由提示词第 2 部分的文字区规划决定）。此方案质量稳定 100%，且复用用户 ComfyUI 现成能力。
- **备选**：支持中文渲染的生图模型（如即梦 API），需用户确认花费。

## 硬性要求
- 一图一信息：禁止在一张图里塞多个核心信息。
- 文字 ≤ 15 字 / 处，最多 2 处文字区。
- 必须引用 `image-styles.md` 的具体风格（构图 + 配色 + 字体感觉），不凭空发明风格。
- 成品与文案同目录 `output/posts/{YYYY-MM-DD}/`。

## 工具依赖（待接入）
- ComfyUI（localhost:8189）：用户本机服务，沙箱当前够不到，需在本机执行叠字脚本。
- 即梦 API（备选）：需用户配 Key 并确认花费。
- 当前环境可生成"提示词 + 叠字规划"，但**不能实跑生图**（无 ComfyUI / 即梦连线）。
