---
title: GitHub starred/高star 库筛选报告
date: 2026-07-08
type: github_screening
---

# GitHub 收藏库筛选报告（2026-07-08）

## 处理动作
- 原始采集：74 个 `_github_*.md`（含重复跑 + 用户 starred 拉取）。
- 去重：4 个（ECC/firecrawl/seedance-2.0/autoclip 各被采两次），保留首次。
- 离题/灰产/空壳剔除：16 个（见下）。
- 最终保留：54 个，已重编号 `01_github_*.md` ~ `54_github_*.md`（连续无碰撞）。
- 同步重建：`data/gate/2026-07-08.jsonl`（55 条 collect：54 github + 1 竞品 x）、`data/raw/2026-07-08/_summary.json`。

## 剔除名单（16，含理由）
- FreeDomain / sub2api / chatgpt2api / OmniRoute / 9router / free-claude-code / awesome-free-llm-apis / CLIProxyAPI：免费API中转/白嫖/号池类，灰色且偏离人设
- gmail-account-creator：批量注册工具，灰色
- AiToEarn / MoneyPrinterV2："用AI赚钱"调性，踩红线（不提收益）
- daily_stock_analysis：股票分析，离题
- duanju / AI-Chat-Assistant：空壳/star极低且与内容工作流无关
- pua（PIP能动性skill）/ teaBASE（模糊开发cockpit）：离题

## 保留分布（54）
### AI Agent/框架（11）
01_github_ECC.md、02_github_hermes-agent.md、04_github_langchain.md、05_github_gemini-cli.md、10_github_dify.md、11_github_open-webui.md、14_github_deer-flow.md、15_github_agency-agents.md、39_github_Agent-Reach.md、43_github_claw-code.md、54_github_autoresearch.md
### 内容创作/视频（25）
06_github_seedance-2.0.md、07_github_autoclip.md、08_github_react-bits.md、12_github_OpenCut.md、13_github_fish-speech.md、16_github_LivePortrait.md、17_github_InstantID.md、18_github_hyperframes.md、19_github_huobao-drama.md、20_github_VoxCPM.md、22_github_video-subtitle-remover.md、23_github_chengfeng-videocut-skills.md、24_github_OpenMontage.md、25_github_OmniVoice-Studio.md、26_github_headroom.md、32_github_video-use.md、34_github_AI-Content-Studio.md、35_github_ponytail.md、44_github_MoneyPrinterTurbo.md、46_github_NarratoAI.md、47_github_social-auto-upload.md、48_github_KrillinAI.md、49_github_FunClip.md、50_github_Jellyfish.md、51_github_VideoLingo.md
### 抓取/数据（3）
03_github_firecrawl.md、36_github_crawl4ai.md、38_github_cli.md
### 语音/图像（0）

### Agent技能/Prompt（10）
09_github_cangjie-skill.md、21_github_claude-code-best-practice.md、27_github_cc-thinking-skills.md、28_github_follow-builders.md、30_github_huashu-design.md、40_github_talk-normal.md、41_github_nuwa-skill.md、42_github_gbrain.md、52_github_awesome-openclaw.md、53_github_gstack.md
### 其他AI工具（5）
29_github_codex-token-skills.md、31_github_AiCMO-Marketing-Prompt-Collection.md、33_github_Rapid-MLX.md、37_github_Understand-Anything.md、45_github_youtube-shorts-pipeline.md

## 与流水线对接
- 这 54 个库均为 `collect` 级，下游 `ziliaoku-extract` 抽「是什么/怎么用/适用场景」→ `cluster` 聚类 → `topics` 生成「神库推荐/工具盘点」选题。
- starred 是用户人工背书的强信号，比 trending 更贴本人赛道；后续每周可 `python scripts/collect_github.py --mode starred` 增量同步。
- watch 个人收藏（`data/github_watchlist.md`）仍保留 seedance-2.0 / autoclip 两条作为常驻标杆。
