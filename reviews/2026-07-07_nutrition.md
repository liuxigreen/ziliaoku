# 采集营养诊断报告 · 2026-07-07

> 目的：验证「采集筛选」环节 —— 看资料库内容营养够不够、AI 相关性/宽度够不够。
> 方法：对 `data/raw/2026-07-07/` 全部 50 篇跑 `ziliaoku-gate` 四态质检（脚本 `scripts/screen_gate.py`，结论存 `data/gate/2026-07-07.jsonl`）。

## 一、总览

| 指标 | 数值 |
|---|---|
| 采集总数 | 50 篇 |
| **collect（收录）** | **37（74%）** |
| hack_only（仅收手法） | 3（6%） |
| discard（丢弃） | 10（20%） |
| discard 率 | 20%（远低于 gate 警戒线 60%，说明采集源质量整体 OK） |

**结论：营养足够，宽度也够（覆盖 AI工具/创作/自媒体/副业 四赛道 + X 模型解读）。** 不是"采了一堆垃圾"，而是"采得不错但有几个漏点要补"。

## 二、分平台营养

| 平台 | collect/总 | 评价 |
|---|---|---|
| Reddit | 19/24（79%） | **最佳源**。24 篇全是带 selftext 的一手经验帖（Claude Code 实战体系、n8n 工作流、AI 视频横评、副业收入结构）。几篇软广/水帖已 discard。 |
| X/SoPilot | 12/18（67%） | **有漏点**。真实推文正文已采到（宝玉 Anthropic Fable5 解读、Baye Computer Use、Phoenix Yin Terminal-Bench 排行），但混了 ~4 个明确炒股/财经号。 |
| 公众号/exa/fc | 4/4（100%） | 真实文章/教程，可拆解。 |
| YouTube | 2/2（100%，另 2 篇 artifact/空） | 元数据稳；1 条完整字幕（Kevin Stratvert 3006 词）成功，1 条字幕抓取失败。 |

## 三、发现的 4 个漏点（按优先级）

### 🔴 P0 — X/SoPilot 混入财经/炒股号（离题）
SoPilot「热帖」不过滤领域，本批 18 篇里 **4 篇是明确炒股/财经号**，不在我们 AI 六赛道：
- `06_外汇交易员`、`18_川沐stock`、`20_华尔街观察`、`22_Summer在交易`
- 已判 discard。但**根因在采集层没按 AI 关键词过滤**。
- **修法**：`collect_sources.py` 的 SoPilot 解析后加一步 AI 相关性初筛（标题/正文匹配 `keywords.md` 赛道词 + 排除「美股/外汇/交易/A股/ETF」等黑名单词），命中才写 raw。

### 🟡 P1 — Reddit 软广/水帖/离题漏进
- `31_AiAutomations`：软广伪装（结尾导 kadirx.io 外链，score 仅 25）→ discard
- `35_deadbydaylight`：游戏公司用 GenAI 的行业新闻，离题 → discard
- `42_SoraAi` / `49_ContentCreators`：产品展望文 / 低质提问帖 → discard
- **修法**：Reddit 采集加 score 地板（如 < 50 直接标 suspect，进 gate 时重点查软广）；加「软广外链」「离题游戏/影视」规则。

### 🟡 P1 — YouTube 字幕抓取不稳定（1/2 失败）
- 本批 `07_kevinstratvert` 字幕成功（opencli transcript），`06_techwithtim` 返回空。
- **根因**：opencli `transcript` 适配器时好时坏（手动测还超时过）。
- **修法（你已同意）**：导出 `cookies.txt` 后改走 `yt-dlp --cookies`（更稳定），并按视频原始语言优先选轨。cookie 文件已加 `.gitignore`。

### 🟢 P2 — SoPilot 缺互动数据
- SoPilot 只给 `viral_probability`/`predicted_views`，没有真实点赞/评论数，frontmatter 缺 `score`。不影响入库，但周复盘按 `source_platform` 统计 collect 率时 X 维度会偏弱。
- **修法**：采集时把 `viral_probability` 归一进 `engagement_proxy` 字段，周复盘可读。

## 四、宽度评估（AI 相关性）

| 六赛道 | 覆盖 | 备注 |
|---|---|---|
| 赛道1 AI工具 | ✅ 强 | Reddit Claude Code/n8n + X 模型解读 |
| 赛道2 AI创作 | ✅ 中 | Reddit SD/Krea/AI视频横评 |
| 赛道3 自媒体 | ✅ 中 | Reddit AI voice agent / $900/day creator |
| 赛道4 副业 | ✅ 强 | Reddit 被动收入/side hustle 多篇一手 |
| 赛道5 职场 | ⚠️ 弱 | 仅 Reddit "jobs truth" 1 篇，需补 LinkedIn/职场号 |
| 赛道6 金句 | ⚠️ 弱 | 当前无专门采集，靠成稿阶段从爆文提炼 |

**宽度结论**：AI 硬核（工具/创作/副业）够宽；**职场/金句偏薄**，下轮采集加 LinkedIn（需 cookie）+ 金句类账号。

## 五、下一步

1. **你做**：① 导出 YouTube `cookies.txt` 到项目根（破字幕关）；② WorkBuddy 连接器点 `firecrawl-mcp` 信任（抓 X 长文/穿透用）。
2. **我做**（你确认后）：按 P0/P1 改 `collect_sources.py`（X 加 AI 关键词过滤 + Reddit score 地板 + 软广/离题规则），重跑一轮把营养率再拉高。
3. 通过后把本轮（含 gate 筛查 + 营养报告）与之前未推送的 commit 一起 push 到 GitHub，资料库正式营业。
