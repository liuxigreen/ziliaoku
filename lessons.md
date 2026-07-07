# 踩坑记录

> 每次任务把踩坑和新路由写在这里。

---

## 2026-07-07 渠道联调与 YouTube 字幕

### 踩坑（v3 验证，2026-07-07 晚）
1. **opencli `youtube transcript` 适配器实测不可用**：加 `--lang zh-Hans` 仍 `TIMEOUT 60s`，中文/英文视频均返回空。已弃用，改 yt-dlp 抓字幕。
2. **yt-dlp 撞 YouTube 反爬墙**（"Sign in to confirm you're not a bot"）：需 cookies。裸 `--cookies-from-browser chrome` 在 Chrome 运行时失败——Windows 锁住 Cookie 数据库（`AppData\Local\Google\Chrome\User Data\Default\Network\Cookies`），复制报错。
3. **解法 = cookies.txt（一次性）**：浏览器装「Get cookies.txt LOCALLY」扩展 → 打开 youtube.com → 导出 cookies.txt 存项目根（已 gitignore）。yt-dlp `--cookies cookies.txt` 稳定绕过反爬抓字幕。
4. **原始语言字幕**：yt-dlp 返回 `language` 字段即视频原始语言，fetch 时优先选该轨，缺失按 zh-Hans→zh→en 兜底（用户强调"设置原始语言"）。
5. **SoPilot RSS 不稳定**：curl 502，feedparser 0 条，需容错回退。

### 新路由
1. **YouTube 字幕稳定路径 = yt-dlp + cookies.txt**（见 `scripts/collect_sources.py` v3）。搜索/元数据也走 yt-dlp `-j`（带 cookie），一次拿全字段（description/like_count/tags/language）。
2. **Reddit OpenCLI 可用（免登录直出真实帖）**：`opencli reddit search "query" -f yaml --limit N`，已验证 r/AI_Agents 等。
3. **YouTube 搜索/元数据**：`opencli youtube search` + `opencli youtube video` 走浏览器登录态也可用，但字幕必须 yt-dlp+cookies。

### 渠道最终状态（WorkBuddy 环境，去重后）
- ✅ YouTube（搜索+元数据+**字幕 via yt-dlp+cookies，原始语言优先**）
- ✅ Reddit（OpenCLI 搜索，免登录）
- ✅ X/Twitter、小红书、B站、Facebook、Instagram（OpenCLI，复用 Chrome 登录态）
- ✅ GitHub（gh CLI）/ V2EX（公开 API）/ RSS（feedparser）/ 任意网页（Jina + Firecrawl keyless）
- ✅ Firecrawl MCP（keyless：scrape/search/interact）
- ❌ LinkedIn / 雪球 / 小宇宙播客（未配置）

---

## 2026-07-07 Day 1 环境搭建

### 踩坑
1. **Windows 默认 Python 是 Store 空壳**：`C:\Users\liuxi\AppData\Local\Microsoft\WindowsApps\python.exe` 只是跳转 Microsoft Store，不是真 Python。用 `winget install Python.Python.3.12` 装到 `C:\Users\liuxi\AppData\Local\Programs\Python\Python312\`
2. **Node.js v16 太老**：mcporter、opencli 都要求 >=18 甚至 >=20。用 `winget install OpenJS.NodeJS.LTS` 升到 v24 LTS
3. **npm allow-scripts 拦截**：新版 npm 默认阻止 postinstall 脚本，需 `npm config set allow-scripts "@jackwener/opencli:*"` 放行
4. **PowerShell 变量在 Git Bash 里被吞**：`$cfg = 'xxx'` 这种写法在 bash→powershell 传递时 `$cfg` 被 bash 消费。解决：写成 .ps1 文件用 `powershell -ExecutionPolicy Bypass -File` 执行
5. **mcporter config 路径**：mcporter config 写入当前目录 `config/mcporter.json`，确保在 topic-workflow 目录运行

### 关键路径
- Python venv：`C:\Users\liuxi\.agent-reach-venv`
- agent-reach 激活：`source C:/Users/liuxi/.agent-reach-venv/Scripts/activate`
- Node.js：`/c/Program Files/nodejs`（需 export PATH 加入）
- OpenCLI Chrome 扩展（待手动安装）：https://chromewebstore.google.com/detail/opencli/ildkmabpimmkaediidaifkhjpohdnifk

### 当前渠道状态（6/15 可用）
- ✅ YouTube、V2EX、RSS、全网语义搜索、任意网页、B站
- ⏳ 小红书：需装 OpenCLI Chrome 扩展 + 登录
- ⏳ GitHub：需装 gh CLI（非紧急）

---

## 2026-07-07 WorkBuddy 接管环境重连（当前真实状态）

> 以下是 WorkBuddy 环境下的实测状态，区别于上方早期 qoderwork 环境的记录。本轮只动了 collect / image 两个技能，纯 LLM 技能未改。

### 环境结论
- **agent-reach v1.5.0 已装**（venv: `C:\Users\liuxi\.agent-reach-venv`，Python 3.12.10），`doctor` 实测 **10/15 渠道可用**。
- **firecrawl MCP 已接入（keyless 托管层，免 API Key）**：`~/.workbuddy/.mcp.json` 已加 `firecrawl-mcp`（type http, url `https://mcp.firecrawl.dev/v2/mcp`）。可用 `scrape`/`search`/`interact`；`crawl`/`extract` 需升级 Key（采集层暂不需要）。
- **小红书 opencli 可用但需登录态**：doctor 显示 `opencli xiaohongshu` ✅，实际拉数据需 OpenCLI Chrome 扩展已装 + Chrome 登录 xiaohongshu。
- **Exa via mcporter 待 config add**：mcporter 已装，需 `mcporter config add exa https://mcp.exa.ai/mcp`。

### 渠道最终状态（11/15 可用，WorkBuddy 环境）
- ✅ GitHub（gh CLI 完整）/ V2EX（公开 API）/ RSS（feedparser）/ 任意网页（Jina Reader：`curl https://r.jina.ai/URL`）
- ✅ X/Twitter、Reddit、B站、Facebook、Instagram、**小红书**（均经 OpenCLI，复用 Chrome 登录态）
- ✅ Firecrawl MCP（**keyless 托管层，免 API Key**：`scrape`/`search`/`interact` 可用；`crawl`/`extract` 需升级 Key）
- ✅ YouTube：yt-dlp + cookies.txt 抓字幕（原始语言优先）；opencli transcript 弃用（实测超时）
- [X] 全网语义搜索（Exa via mcporter）：未 `config add`
- ❌ LinkedIn / 雪球 / 小宇宙播客（未配置）

### 本轮决策（用户，基于 X 帖子 @Eejoylove 起号手册印证）
1. **ComfyUI 不装** → 配图改走 **即梦 API（Dreamina）**（支持中文渲染），已更新 `ziliaoku-image` SKILL。
2. **firecrawl + agent-reach 要装**：agent-reach 已就位；firecrawl 已接 **keyless 托管 MCP（免 API Key）**。
3. **小红书请回作信号源**（非正文源）：只抽标题公式 + 封面模式，进 `titles_pool.jsonl` / `image-styles/`，不抓正文。已更新 `ziliaoku-collect` SKILL。
4. **资料库最重要，要有营业**：发布平台后续可能含小红书 + 公众号，但选题库是核心，需持续运行采集。
5. **先从第一个工作流 skill（collect / 搜索）优化** → 本轮已完成 collect SKILL 重构（5 发现入口 + 小红书信号流 + 真实 fetch 层）。
