# ziliaoku（资料库 · AI 内容选题工作流）

本地内容采集与选题资料库。由采集脚本拉取各渠道的爆文 / 深度文章，产出结构化 Markdown 进入 `data/raw/{YYYY-MM-DD}/`，供后续「提取 → 聚类 → 成稿 → 复审」阶段使用。

> 当前由 WorkBuddy 接管维护（原在 `D:\.qoderworkcn\topic-workflow\` 本地运行，代码托管于 `github.com/liuxigreen/ziliaoku`）。

## 目录结构

| 路径 | 说明 |
|------|------|
| `scripts/collect.py` | 采集主脚本（SoPilot RSS + Exa 搜索） |
| `config/mcporter.json` | mcporter（Exa MCP）配置 |
| `data/raw/{date}/` | 原始采集结果（Markdown + `_summary.json`） |
| `data/extracted/{date}.jsonl` | 提取阶段产出（待实现 / 由 AI 代理填充） |
| `data/clusters/` | 聚类结果（待实现） |
| `data/titles_pool.jsonl` | 标题池 |
| `output/posts/` | 成稿输出（待实现） |
| `reviews/` | 人工 / AI 复审（待实现） |
| `keywords.md` | Exa 搜索关键词 |
| `account.md` | 账号人设与变现路径 |
| `formulas.md` / `image-styles.md` | 标题公式库 / 配图风格库 |
| `watchlist.md` / `missed.md` / `lessons.md` | 作者监控 / 漏网追踪 / 踩坑记录 |

## 本地部署 / 运行

1. 准备 Python 3.12+，创建并激活虚拟环境：
   ```bash
   python -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. 运行采集：
   ```bash
   python scripts/collect.py
   ```
   结果输出到 `data/raw/{今天日期}/`，并生成 `_summary.json`。

## 外部依赖

- **feedparser**（Python 包）：解析 SoPilot RSS，已列入 `requirements.txt`。
- **mcporter + Exa MCP**：`collect.py` 通过 `mcporter call exa.web_search_exa` 做全网语义搜索。
  `config/mcporter.json` 目前只配了 `baseUrl`，**还需在 mcporter 中配置 Exa API Key** 才能生效；未配置时该渠道会静默跳过（不影响 SoPilot 源）。
- **OpenCLI / Firecrawl MCP / 各平台渠道**：`lessons.md` 记录了联调状态（YouTube、小红书、B站、X、Reddit 等），
  但当前 `collect.py` 尚未接入，只实现了 SoPilot + Exa 两条源。
- **SoPilot RSS**：`https://sopilot.net/rss/hottweets`，历史出现过 502 不稳定，脚本已做容错。

## 当前进度 / 缺口

- ✅ **采集阶段（collect）** 已实现并跑通。
- ❌ **提取 / 聚类 / 成稿 / 复审** 四个下游阶段目前没有脚本，相关目录为空；原设计由 AI 代理（Prompt-B）填充。
- ⚠️ `collect.py` 硬编码了 Windows 路径（`C:\Program Files\nodejs\mcporter.cmd`），非 Windows 环境需改为可配置。
