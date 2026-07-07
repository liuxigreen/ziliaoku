# 踩坑记录

> 每次任务把踩坑和新路由写在这里。

---

## 2026-07-07 渠道联调与 YouTube 字幕

### 踩坑
1. **YouTube 字幕必须加 `--lang` 参数**：`opencli youtube transcript URL` 不加 `--lang en` 会报 "Caption URL returned empty response"。正确用法：`opencli youtube transcript URL --lang en -f md`
2. **中文 YouTube 频道普遍无字幕**：手动字幕和自动字幕都没有。中文视频只能靠 `opencli youtube video` 拿元数据（描述+章节+关键词）
3. **英文字幕有时不稳定**：可能是 rate limit，同一条视频有时成功有时失败
4. **yt-dlp 在 Windows 上被 YouTube 反爬拦截**：需要 cookies 但 Chrome cookie 数据库被 Chrome 锁定，复制需管理员权限。放弃 yt-dlp，改用 opencli youtube
5. **SoPilot RSS 不稳定**：curl 返回 502，feedparser 返回 0 条。需要容错回退方案
6. **Chrome cookie 文件位置**：`~\AppData\Local\Google\Chrome\User Data\Default\Network\Cookies`（注意 Network 子目录），Chrome 运行时锁定该文件

### 新路由
1. **Firecrawl MCP 已装**：作为自定义 MCP 添加到 `qoderwork.settings.connector.custom`，26 个工具可用（scrape/search/crawl/map/extract/agent/monitor + arXiv + GitHub）
2. **GitHub gh CLI 已认证**：`liuxigreen` 账号，可搜索仓库和 issue
3. **Reddit OpenCLI 可用**：`opencli reddit search "query" -f yaml --limit N`，已验证 r/ClaudeCode 和 r/ClaudeAI 搜索
4. **YouTube 搜索**：`opencli youtube search "query" -f yaml --limit N`，可获取播放量、时长、频道等元数据

### 渠道最终状态（11/15 可用）
- ✅ YouTube（搜索+元数据+英文字幕）
- ✅ GitHub（gh CLI 搜索仓库/issue）
- ✅ Reddit（OpenCLI 搜索）
- ✅ 小红书（OpenCLI 搜索/笔记/评论/Feed）
- ✅ B站（OpenCLI 搜索/视频/字幕/排行）
- ✅ X/Twitter（OpenCLI 搜索/文章/用户帖子）
- ✅ Facebook、Instagram（OpenCLI，需 Chrome 登录）
- ✅ V2EX（公开 API）
- ✅ RSS（feedparser）
- ✅ 全网语义搜索（Exa via mcporter）
- ✅ 任意网页（Jina Reader + Firecrawl scrape）
- ✅ Firecrawl MCP（scrape/search/crawl/extract/agent/monitor）
- ❌ LinkedIn（未配置）
- ❌ 雪球（需登录 cookie）
- ❌ 小宇宙播客（需 ffmpeg）
- ❌ GitHub CLI（已装但 agent-reach 未识别，直接用 gh 命令）

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
