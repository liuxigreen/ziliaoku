---
title: "Claude Code 32 招 · 公众号配图提示词"
based_on: "wewrite-visual 方法论（~/.workbuddy/skills/wewrite/skills/wewrite-visual/references/visual-prompts.md）"
source_article: "../2026-07-11/claude_code_32tips_wechat.md"
generated: 2026-07-13
note: |
  本套提示词按 wewrite-visual 的「实体提取 → 风格锚定 → 封面3组 → 内文按类型」流程产出。
  wewrite 的 image-gen CLI 在我们环境跑不了，故只出提示词，你可直接拿去：
    - 封面：ponyo / 即梦 / 本 agent 生图（2.35:1 公众号头图）
    - 内文：即梦 / 本 agent 生图（16:9）；或对应本项目已有 ian 小黑手绘（ian_01=CLAUDE.md错题本、ian_02=子代理并行）
  提示词末尾都挂了视觉锚点，保证封面+内文视觉一致。
---

## 实体提取（硬规则：每条提示词 ≥2 个实体）

- 产品/技术：**Claude Code**、**CLAUDE.md**、`/init`、`Plan Mode`、`/context`、`/compact`、子代理(subagent)、Haiku、Opus
- 场景：终端窗口、代码库扫描、多窗口并行、深夜写代码
- 数据点：**32 招**、16 分钟、**90% 返工**、**60% compact**、**95% 确信**、大半年
- 概念：上下文腐烂(context rot)、错题本、肌肉记忆、速查卡

## 视觉锚点（封面确认后提取，内文全部复用）

```
视觉锚点：
- 色板：主色 #059669（emerald，呼应摸鱼绿排版主题） + 辅色 #1E293B（深石板灰） + 点缀 #F59E0B（琥珀，代表 Claude 暖橙/警示）
- 风格关键词：flat illustration, minimalist, bold clean outlines, warm-tech editorial
- 画面调性：中性偏暖（不冷冰冰的科技蓝）
```

---

## 封面图（3 组差异化创意）

### 封面创意 A：裸奔 vs 全副武装（直觉冲击型）

- 视觉描述：画面左右分割。左边一个开发者赤手面对巨大空白终端，头顶飘着「只会对话式让 AI 写代码」的灰字气泡；右边另一个开发者背后悬浮着一本发光的 CLAUDE.md 速查卡，身边围着 3 个半透明子代理小窗口在并行干活，脚下踩着 `/init` `/compact` 的踏板。中间一道细光带把两边分开，右侧明显更稳。
- 色调：#059669 主 + #1E293B 辅 + #F59E0B 点缀（右侧发光）
- 构图：16:9 横版，左右分栏对比，右侧 1/3 留白放标题
- 文字区域：右侧干净空间，放「Claude Code 32 招」
- AI 绘图提示词：
  "Split-screen illustration, left side a developer barehanded facing an empty terminal with a grey speech bubble saying 'just chat with AI to code', right side a calm developer with a glowing CLAUDE.md cheat-sheet behind him and three translucent subagent windows working in parallel, a light band dividing them, right side clearly more stable, flat illustration minimalist bold clean outlines warm-tech editorial, color palette emerald green #059669 dark slate #1E293B amber accent #F59E0B, 16:9 aspect ratio, clean space on right third for text overlay, no text no letters no words"
- 适配工具建议：即梦（中文理解好，对比隐喻强）

### 封面创意 B：深夜终端前的淡定（氛围渲染型）

- 视觉描述：深夜，一个开发者坐在终端前喝咖啡，屏幕泛着 emerald 冷光，周围漂浮着 3–4 个半透明的子代理窗口（有的在调研、有的在跑测试），像安静的小团队围着主理人。氛围松弛、专业，不焦虑。背景是暖暗房间里的台灯光晕。
- 色调：#1E293B 主（暗环境） + #059669 屏幕光 + #F59E0B 台灯暖点
- 构图：16:9 横版，开发者居中偏左，右侧 1/3 留白放标题
- 文字区域：右侧干净空间
- AI 绘图提示词：
  "Late night, a developer sitting relaxed at a terminal drinking coffee, screen glowing emerald, surrounded by three or four translucent subagent windows doing research and running tests like a quiet small team around the lead, cozy professional calm atmosphere, warm desk lamp halo in dark room, flat illustration minimalist bold clean outlines warm-tech editorial, palette dark slate #1E293B emerald screen #059669 amber lamp #F59E0B, 16:9 aspect ratio, clean space on right third for text overlay, no text no letters no words"
- 适配工具建议：Midjourney（氛围光影更细腻）

### 封面创意 C：32 招四宫格（信息图表型）

- 视觉描述：一个干净的网格，分成 4 个色块，分别标（用图标不用字）地基/上下文/协作/规模化 四类，中央一个大大的「32」数字，周围散落 `/init` `Plan Mode` `子代理` 的小图标。一眼看懂「32 招按四块归类」。
- 色调：#059669 主 + #1E293B 辅 + #F59E0B 强调数字
- 构图：16:9 横版，中央大字 32，四周网格，底部留白放标题
- 文字区域：底部干净空间
- AI 绘图提示词：
  "Clean grid infographic divided into four colored blocks representing four categories of Claude Code techniques, a large number 32 in the center, small icons of init command plan mode subagent scattered around, flat illustration minimalist bold outlines warm-tech editorial, palette emerald #059669 dark slate #1E293B amber accent #F59E0B, 16:9 aspect ratio, clean space at bottom for text overlay, no text no letters no words"
- 适配工具建议：即梦 / 文心一格（信息图结构稳）

---

## 内文配图（4 张，避开已有的 ian_01 / ian_02）

### 配图 1：位于「开头归类段（第 13 行）」之后

- 类型：infographic
- 对应内容：32 招按「地基 → 上下文 → 协作 → 规模化」四块重新归类

```
Layout: grid (2x2)
Zones:
  - Zone 1: 地基 — 图标：/init 生成 CLAUDE.md 速查卡
  - Zone 2: 上下文 — 图标：/context 体检 + /compact 瘦身
  - Zone 3: 协作 — 图标：子代理并行 + 95% 确信再动手
  - Zone 4: 规模化 — 图标：自定义技能 + 错题本
Labels: 32 招、四块分类名（用图标不用字）
Colors: #059669 主 + #1E293B 辅 + #F59E0B 点缀
Style: flat illustration minimalist bold clean outlines warm-tech editorial, clean infographic, no text
Aspect: 16:9
```
- 备选方案：Unsplash 搜 "infographic grid categories productivity"

### 配图 2：位于「二、上下文」第 4 招（/context）段后

- 类型：infographic
- 对应内容：上下文腐烂——/context 把「谁在吃 token」拆成百分比（系统提示/文件/MCP）

```
Layout: radial
Zones:
  - Zone 1（中心）: 一个臃肿的上下文窗口，里面漂着文件块/MCP块/系统提示块
  - Zone 2（外圈占比条）: 系统提示 35% / 文件内容 40% / MCP 服务 25%（用长度不用数字标签）
  - Zone 3: 一个「瘦身」箭头指向 compact 后的精简窗口
Labels: token 黑洞、体检、瘦身（图标化）
Colors: #059669 主 + #1E293B 辅 + #F59E0B 警示
Style: flat illustration minimalist bold clean outlines warm-tech editorial, clean infographic, no text
Aspect: 16:9
```
- 备选方案：Unsplash 搜 "data usage breakdown chart"

### 配图 3：位于「四、规模化」第 9 招（自定义技能）段后

- 类型：scene
- 对应内容：把重复活固化成技能 = 给 AI 攒「肌肉记忆」

```
Focal Point: 一个开发者把一张写好的提示词卡片塞进标有 .claude/skills 的抽屉，抽屉里已经叠了好几张
Atmosphere: 明亮整洁的工作台，晨光
Mood: 踏实、积累感
Color Temperature: warm（与锚点一致）
Style: flat illustration minimalist bold clean outlines warm-tech editorial, no text no letters
Aspect: 16:9
```
- 备选方案：Unsplash 搜 "organized desk drawer cards workspace"

### 配图 4：位于「我的不同意见：别贪多」段后

- 类型：comparison
- 对应内容：你用 AI 写 Demo vs 高手在榨它的判断力（裸奔 vs 带装备）

```
Left Side — 只会写 Demo:
  - 赤手面对终端
  - 收藏一堆技巧继续裸奔
Right Side — 榨判断力:
  - 背着 CLAUDE.md 速查卡
  - 子代理小队并行
Divider: 一道 emerald 光带
Colors: 左 #1E293B 灰、右 #059669 绿、#F59E0B 强调
Style: flat illustration minimalist bold clean outlines warm-tech editorial, split layout, no text
Aspect: 16:9
```
- 备选方案：Unsplash 搜 "versus comparison two paths"

---

## 使用说明

1. **封面**：三选一拿去生图（建议先试创意 A，对比隐喻最贴「你用 AI 写 Demo，高手在榨判断力」这个核心钩子）。生图后裁 2.35:1 头图。
2. **内文**：配图 1/2/3/4 是新增位；源稿已有的 `ian_01`（CLAUDE.md 错题本）、`ian_02`（子代理并行）继续用 ian 小黑手绘，不重生。
3. **视觉一致**：所有提示词都挂了同一套色板+风格，生出来的图会像「一个号」的。
4. **避坑**：AI 生图别让它写字（已加 no text），标题/标签用 PIL 或排版工具后期叠。
