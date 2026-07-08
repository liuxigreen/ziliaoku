---
name: ziliaoku-decode
description: 爆款内容拆解（横切技能）。用户提供/我们精选一篇爆款文章原文链接（小红书/公众号/视频均可），firecrawl 抓全文后 LLM 拆解它为什么爆（钩子类型/结构走法/情绪触发点/可复用写法/标题公式），追加写入 data/winning_cases.jsonl，供 ziliaoku-draft 成稿时借鉴。This skill should be used when the user says "拆解这篇爆款" or during weekly review to decode our own best posts back into the library.
agent_created: true
---

# ziliaoku-decode — 爆款内容拆解（横切技能）

## Purpose
把一篇"爆款内容"拆成可 machine-readable 的**写作知识**：它为什么爆、钩子怎么设、结构怎么走、踩了什么情绪点、哪段写法能复用。产出 `data/winning_cases.jsonl`，喂给 `ziliaoku-draft` 在成稿时引用，让账号"从爆款学写爆款"，而不是死用 4 段模板。

本技能与 `ziliaoku-extract`（拆 Git 工具 README）对称：extract 拆"工具"，decode 拆"内容/写法"。两者都进资料库，但 decode 的产物是**写作方法论资产**，供 draft 直接引用。

## When to use
- 用户甩来一篇爆款原文链接，说"拆解这篇 / 看看它为什么爆 / 这写法能学吗"。
- 周复盘时，把本周**自家**表现最好的帖子回拆进库（`reference_for: 自身复盘`），形成"自家爆款 → 写作知识 → 下篇更好"的闭环。
- 选题会上，为某类选题找可借鉴的写法样本。

## 输入
- 原文链接（用户提供 / 我们精选），平台不限：小红书 / 公众号 / 视频 / X / 其他。
- 若链接不可抓取（付费墙/登录墙），则要求用户提供正文文本，禁止脑补抓取不到的内容。

## 抓取（工具依赖，按平台选型，firecrawl 额度省着用）
- **Reddit 域名（reddit.com / old.reddit.com）走 `opencli reddit`**：firecrawl 对 reddit 直抓返回 403、search 也不带正文，实测不可用。改用 `opencli reddit read <post-id> -f md`（单帖+评论全文，免登录）或 `opencli reddit search "query" -f json`（搜内容型帖）。抓取结果存 `data/raw/reddit_<sub>_<id>_*.md` 即可喂 decode。
- **X/Twitter 长文优先 `opencli twitter`**（复用 Chrome 登录态，免费）；仅 firecrawl 能穿透的 Article 才用 `scripts/firecrawl_client.py` `scrape`。
- **公众号 / 视频 / 陌生 URL 才走 `scripts/firecrawl_client.py`**（firecrawl 付费额度，留给 opencli 抓不到的源；严禁用 firecrawl 抓 reddit 等 opencli 已覆盖的源，浪费额度）。
- 抓不到正文时**停下问用户要文本**，绝不编造。

## 输出契约（冻结，追加到 data/winning_cases.jsonl，每行一个 JSON）
```json
{
  "source_url": "原文链接",
  "platform": "小红书 | 公众号 | 视频 | X | 其他",
  "title": "原标题",
  "decoded_at": "2026-07-08",
  "why_viral": "爆的核心原因（具体到手法或情绪，禁止'内容优质'式废话）",
  "hook_type": "钩子类型（痛点共鸣/结果展示/认知反差/信息差/身份认同/热点反问）",
  "hook_line": "原文第一句/钩子原文（一句）",
  "structure_walk": "结构走法，箭头串联：钩子 → 翻转 → 方法N步 → 结果 → 互动",
  "emotion_triggers": ["焦虑", "好奇", "获得感"],
  "reusable_pattern": "可复用写法模板（抽象成可填空，如'先甩一个反常识结论，再用3个真实案例撑住'）",
  "title_formula": "标题可填空公式（如'{人群}{动作}后，{反转结论}'）",
  "fit_niche": "是否适配我们 niche（AI Agent 工作流）：适配点一句话；不适配填 null",
  "reference_for": "适合喂给哪类成稿（工具拆解/爆款方法论/自身复盘）"
}
```

## 硬性要求
- `why_viral` / `reusable_pattern` / `title_formula` 必须**可复用、可填空**，禁止"选题好""内容优质"等空话。
- 所有字段基于**原文抓取/用户提供文本**，禁止脑补数据或情绪。
- `reference_for` 必须落到我们三类内容之一（工具拆解/爆款方法论/自身复盘），否则这条 case 对账号无用，不收。
- `fit_niche` 为 null 的 case 仍收（作为跨领域写法样本），但 draft 引用时仅借鉴写法、不套主题。
- 与 `ziliaoku-extract` 区分：extract 拆的是"工具/项目"（进 extracted 爆文库），decode 拆的是"内容写法"（进 winning_cases 写作库）；两者不混库。

## 接 ziliaoku-draft 的方式
- draft 成稿前读 `data/winning_cases.jsonl` 近 10 条；若选题的 `content_angle` / `reference_for` 与某条 case 匹配，优先借鉴其 `reusable_pattern` 与 `hook_type`，融入 `structure_ref`，不套死 4 段模板。
- 借鉴的是"写法骨架"，不是抄内容；仍守去 AI 味 / 不画饼 / 开头多样性铁律。

## 工具依赖
- 抓取：firecrawl（已接 Key）；拆解：纯 LLM。当前环境即可运行。
