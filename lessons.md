# 踩坑记录

> 每次任务把踩坑和新路由写在这里。

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
