---
name: ziliaoku-draft
description: 成稿（Prompt-E）。把 ziliaoku-topics 选出的一条选题扩写为可发布的小红书文案，含硬性去AI味规则，输出 output/posts/{日期}/。This skill should be used after the user picks topics from the weekly topic library and wants a ready-to-publish draft.
agent_created: true
---

# ziliaoku-draft — 成稿（Prompt-E）

## Purpose
从选题到成品文案：把 `ziliaoku-topics` 里用户勾选的选题，写成严格按结构骨架展开、且**去AI味**的小红书正文，并产出配图简报供 `ziliaoku-image` 使用。

## When to use
- 用户从 `output/topics_{week}.md` 勾选选题后，说"写这条 / 出稿 / 成稿"。

## 输入
- 一条选题（含 `title_candidates`、`hook_draft`、`structure_ref`、`evidence`、`fit_score`）。
- `account.md` 人设与红线。

## 输出契约（冻结，写入 output/posts/{YYYY-MM-DD}/{slug}.md 或同目录 JSON）
```json
{
  "final_title": "终稿标题（≤20字，从 candidates 中选优并打磨，保留数字和钩子词）",
  "body": "正文（600-800字，严格按 structure_ref 骨架展开）",
  "tags": ["5-8个话题标签，混合：1-2个大流量标签 + 3-4个精准垂类标签"],
  "cta": "结尾互动引导一句（提问式，禁止'关注我'式硬引流）",
  "image_count": 4,
  "image_briefs": [
    "图1封面：核心结论大字",
    "图2：步骤1截图示意"
  ]
}
```

## 去AI味规则（写作时强制执行，不可省略）
- 开头 3 句禁用"在当今时代 / 随着AI发展"式套话，直接进钩子。
- 每 200 字至少一处口语化表达（"说实话"、"我踩过这个坑"、"别问我怎么知道的"）。
- 加入 1 处具体的个人经历细节（从 `account.md` 人设推导，**禁止编造具体收益数字**）。
- 短句为主，单句 ≤ 25 字，段落 ≤ 3 行。
- 禁用词：赋能、抓手、闭环、颗粒度、底层逻辑（**连用两个立即重写**）。

## 硬性要求
- `body` 必须严格按 `structure_ref` 骨架展开，不得自由发挥丢结构。
- `cta` 必须是提问式互动，**禁止"关注我"式硬引流**（踩 `account.md` 红线）。
- **honor `monetization_role`**（选题自带，来自 `ziliaoku-topics`）：
  - 若为 `转化`：正文须是强资源型（直接给可复用模板 / 清单 / Prompt，不藏私），`cta` 用**软钩子**（如"这类清单我每周都在整理"）替代硬引流；**绝不可提订阅价格、不可直给微信 / 链接**。
  - 若为 `引流`：`cta` 偏涨粉互动（提问 / 投票 / "你踩过这坑吗"）。
  - 若为 `信任`：`cta` 偏经验交流（"你是怎么处理的？评论区聊聊"）。
  - 所有类型都守 `account.md` 红线（不提收益数字 / 不绝对化 / 不硬引流）。
- `image_briefs` 每张一信息，供 `ziliaoku-image` 逐张生成提示词。

## 工具依赖
纯 LLM 写作，不需外部工具。当前环境即可运行。成品发布前必须经用户终审（红线：自动化的是生产与排期，不是决策权）。
