# 教程：RSS + AI 每日简报自动部署（GitHub Actions 版）

> 配套文章：《算法喂你的都是二手货？我搭了个一手信息源》
> 本文是 **AI 可读的技术附录**，记录完整部署步骤、配置项、自定义方法与已知坑。
> 目标：未来任何 AI 会话或人类读者，读此文件即可完整复现，无需重新推导。

---

## 1. 概述

### 解决什么问题
- 信息流算法只喂你二手、同质化内容
- 想每天自动聚合一手英文信源（Hacker News / Reddit / 科技媒体 / GitHub Trending），按相关度排序成简报

### 方案
- Python 脚本抓 RSS → 关键词评分 → 去重 → 生成 Markdown 日报
- **GitHub Actions 每天北京 8:00 自动跑**，不需要自己的服务器，电脑关机也照跑
- 结果自动 commit 回仓库 `output/rss_briefs/YYYY-MM-DD_ai_daily_brief.md`

### 成本
- GitHub Actions 免费额度 2000 分钟/月，本脚本每次约 30 秒~2 分钟，绰绰有余
- 无服务器、无域名、无数据库费用

---

## 2. 前置条件

| 条件 | 说明 |
|------|------|
| GitHub 账号 | 仓库 `liuxigreen/ziliaoku`（或你自己的任意仓库） |
| 本地 Git | 已配置 SSH/HTTPS 且能 push |
| Python 3.13 | **仅本地测试用**；云端用 Actions 自带的 Python |
| 依赖 `feedparser` | 工作流里自动 `pip install`，本地测试需手动装 |

本地装依赖（可选，仅为了本地预览）：
```bash
cd D:\WorkBuddyProjects\ziliaoku
.venv\Scripts\python.exe -m pip install feedparser
```

---

## 3. 文件结构

```
ziliaoku/
├── tools/rss_daily_brief/
│   ├── config.py          # 信源 + 评分参数（改这里）
│   ├── generate_brief.py  # 主脚本（抓取→过滤→评分→去重→生成md）
│   └── requirements.txt   # 依赖声明
├── .github/workflows/
│   └── rss-daily-brief.yml # 定时任务定义
└── output/rss_briefs/      # 生成的日报（自动 commit，可 gitignore 也可留）
```

---

## 4. 部署步骤（逐条可复制）

### 4.1 把文件放进仓库
三个源文件 + 一个工作流文件，内容见仓库对应路径（直接 clone 本仓库即可获得）。

### 4.2 提交并推送
```bash
cd D:\WorkBuddyProjects\ziliaoku
git add tools/rss_daily_brief/ .github/workflows/ output/rss_briefs/
git commit -m "feat: RSS+AI 每日简报系统 (GitHub Actions 定时抓取)"
git push
```

### 4.3 验证云端能跑
```bash
# 手动触发一次（需 gh CLI 且已 gh auth login）
gh workflow run rss-daily-brief.yml
# 查看运行结果
gh run list --workflow=rss-daily-brief.yml
gh run watch <run_id> --exit-status
```
或不装 gh：GitHub 仓库 → Actions → RSS AI Daily Brief → Run workflow。

### 4.4 确认日报已生成并回写
```bash
git pull
ls output/rss_briefs/
# 应看到 2026-XX-XX_ai_daily_brief.md
```

---

## 5. 配置说明（config.py）

| 参数 | 类型 | 作用 | 默认值 |
|------|------|------|--------|
| `FEEDS` | dict | 信源 `{名称: RSS_URL}`，脚本按顺序抓取 | 14 个英文源 |
| `SOURCE_WEIGHTS` | dict | 来源质量权重，乘到评分上（越高越优先） | HN=1.5, LocalLLaMA=1.4, ... |
| `KEYWORDS` | list | 标题/摘要命中即加分的关键词（小写） | ai/llm/gpt/agent/tool/workflow... |
| `LOOKBACK_HOURS` | int | 只抓过去 N 小时内的文章 | 36 |
| `TOP_N` | int | 精选区展示篇数 | 8 |
| `REQUEST_TIMEOUT` | int | 单次请求超时（秒） | 20 |
| `USER_AGENT` | str | 请求头 UA（部分源拒绝默认 UA） | 自定义 bot UA |

### 评分公式
```
单篇得分 = (关键词命中数) × (来源权重) + 时效加分
时效加分：6h 内 +2，12h 内 +1
```
最终按得分降序，取 Top N + 按来源分组展示。

---

## 6. 自定义

### 加一个信源
编辑 `config.py` 的 `FEEDS`：
```python
"My Blog": "https://myblog.com/feed.xml",
```
若想加权，在 `SOURCE_WEIGHTS` 加同名键：
```python
"My Blog": 1.3,
```

### 改评分侧重
编辑 `KEYWORDS` 列表，例如加 `"agentic"`、`"mcp"`、`"rag"` 等。

### 改推送时间
编辑 `.github/workflows/rss-daily-brief.yml`：
```yaml
schedule:
  - cron: '0 0 * * *'   # 每天 UTC 00:00 = 北京 08:00
```
时间换算（GitHub 用 UTC）：
- 北京 7:00 → `0 23 * * *`（前一天 23 点 UTC）
- 北京 8:00 → `0 0 * * *`
- 北京 9:00 → `0 1 * * *`

### 本地试运行（不依赖云端）
```bash
cd D:\WorkBuddyProjects\ziliaoku\tools\rss_daily_brief
..\..\.venv\Scripts\python.exe generate_brief.py --hours 48
```

---

## 7. 已知坑 / 排错

| 现象 | 原因 | 处理 |
|------|------|------|
| 某些 Reddit 版返回 0 篇（r/OpenAI、r/singularity 等） | Reddit 对非浏览器 UA 限速，或 RSS 端点变动 | 核心源（LocalLLaMA/ML）正常；可换 `.json` 端点或加 OAuth，不影响整体 |
| AI News / MarkTechPost 报 `mismatched tag` | 源站 XML 格式错误 | 脚本已 try/except 跳过，打印 ❌ 但继续跑其他源 |
| Actions 不 commit 回仓库 | 缺写权限 | 工作流已加 `permissions: contents: write` |
| cron 时间不对 | GitHub 用 UTC 不是北京时 | 北京 8 点 = UTC 0 点（见 §6） |
| push 被拒 | 分支保护规则 | 本仓库用 `master` 默认分支；若开保护需调规则或走 PR |
| 抓取超时/网络错 | 部分源偶发不可达 | 脚本逐源 try/except，单源失败不影响其他 |

---

## 8. 后续升级路线（待用户触发）

1. **真·AI 摘要**：在 `generate_brief.py` 接 LLM API（DeepSeek / OpenAI 兼容格式），把提取式摘要（取前 2 句）换成 API 调用；key 存 GitHub Secrets（`AI_API_KEY` + `AI_BASE_URL`），脚本读 `os.environ` 判断是否启用。
2. **GitHub Pages 网页版**：Action 加一步把 md → html 部署到 Pages，得到可分享网址 `https://<user>.github.io/ziliaoku/`。
3. **飞书 / 钉钉 / Telegram 推送**：Action 加一步 POST webhook 或 Bot API，每天自动弹到手机/群。

---

## 9. 关联代码（仓库内路径）

- 主脚本：`tools/rss_daily_brief/generate_brief.py`
- 配置：`tools/rss_daily_brief/config.py`
- 依赖：`tools/rss_daily_brief/requirements.txt`
- 工作流：`.github/workflows/rss-daily-brief.yml`
- 产出示例：`output/rss_briefs/2026-07-16_ai_daily_brief.md`

---

*本文为「技术文章配套 AI 可读附录」标杆样例。后续符合要求的文章（技术 how-to / 译介实测复现）均按此格式留附录于 `docs/tutorials/`。*
