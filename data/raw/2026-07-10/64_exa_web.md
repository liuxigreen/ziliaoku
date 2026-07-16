---
title: "n8n 中文入门教程完整版（2025 最新）-N8N大学"
platform: 网页/公众号
source: Exa搜索
search_query: "n8n 自动化工作流 搭建 教程"
url: "https://www.n8ndx.com/271.html"
published: "N/A"
collected: "2026-07-10"
---


阅读收获： ① 10 分钟完成 n8n 本地安装；

② 运行第一个「RSS → 翻译 → 邮件」自动化工作流；

③ 掌握 4 个核心节点与 3 种触发方式；

④ 学会调试与常见报错排查。
...
本文基于 n8n v1.110 社区版与 Windows / macOS / Docker 三平台实测，所有命令可直接复制。
...
n8n（发音 /ˈneɪtɪn/）是开源的「工作流自动化」工具，定位对标 Zapier、Make，但完全免费、可自建。核心特点：
...
- 节点式可视化：拖拽即用，无需写代码即可连接 350+ 外部服务。
- 自托管：数据不出本地，支持 Docker、npm、Kubernetes 等多种部署方式。
- 开源可扩展：用 TypeScript 编写自定义节点，公司可二开。
...
## 2. 零依赖安装：3 条命令启动 n8n
...
官方提供 3 种最常见方式，按自己环境任选其一。以下命令均于 2025-10-30 实测通过。
...
### 2.1 Windows（PowerShell）
...
```
# 1) 安装 Node.js 22（已装可跳过）
winget install OpenJS.NodeJS

# 2) 一键运行（自带数据库，数据存在 %USERPROFILE%.n8n）
npx n8n@latest
...
# 3) 浏览器访问
start http://localhost:5678
```
...
### 2.2 macOS（Homebrew）
...
```
# 1) 装 Node
brew install node
...
# 2) 运行
npx n8n@latest
```
...
### 2.3 Docker（推荐 Linux / NAS / 云服务器）
...
```
docker run -d --name n8n
-p 5678:5678
-v ~/.n8n:/home/node/.n8n
--restart unless-stopped
docker.n8n.io/n8nio/n8n:latest
```
...
首次启动约需 1-3 分钟下载镜像，看到「Editor is now accessible via …」即成功。
...
## 3. 第一次打开控制台：界面速览
...
左侧边栏
...
- ☰ Workflows：工作流列表
- ⚡ Executions：运行历史
- 📦 Credentials：集中管理 API 密钥 / 密码
...
## 4. 10 分钟做出「RSS 摘要 + 翻译 + 邮件」工作流
...
目标：每天 08:00 把「Hacker News RSS」前 5 条标题翻译成中文，发到 QQ 邮箱。
...
### 步骤 1：创建空白工作流
...
点击左上角「+ New Workflow」→ 进入画布。
...
### 步骤 2：添加触发器
...
- 右上角「Settings」→ 可切换中文界面（Settings > Language > 简体中文）。
- 搜索并拖拽 Schedule Trigger 节点
- Rule → Every Day, 08:00
...
### 步骤 3：获取 RSS
...
- 添加 RSS Read 节点，与触发器连线
- URL 填入`https://hnrss.org/newest?points=10`
- Limit → 5
- 点击「Test step」确认能抓到标题列表。
...
### 步骤 4：调用大模型翻译（以 DeepSeek 为例）
...
Body (JSON):
...
```
{  "model": "deepseek-chat",  "messages": [    {"role": "system", "content": "把下面英文标题翻译成中文，返回纯文本，每行一条："},    {"role": "user", "content": "{{$node["RSS Read"].json["title"].join("n")}}"}  ]}
```
...
- 添加 HTTP Request 节点
- Method: POST
- URL:`https://api.deepseek.com/v1/chat/completions`
- Headers:`Authorization: Bearer {{$credentials.deepseekApiKey}}`
...
### 步骤 5：发送邮件
...
- 添加 Send Email 节点
- SMTP Host →`smtp.qq.com`/ Port 465 (SSL)
- User → 你的 QQ 邮箱，Password → QQ 邮箱授权码
- Subject:`HN 日报 {{$today}}`
- Text:`{{$node["HTTP Request"].json["choices"][0]["message"]["content"]}}`
...
### 步骤 6：保存并激活
...
1. 点击右上角「Save」→ 填写工作流名称：HN-Daily-ZH
2. 切换「Inactive」→「Active」；激活后触发器才会按计划运行。
...
完成！明早 8 点即可收到第一封自动翻译邮件。
...
## 5. 4 个高频节点详解
...
| 节点 | 作用 | 必会参数 |
| --- | --- | --- |
| Function / Code | 写 JS 脚本转换数据 | `items[0].json.xxx = ...` |
| HTTP Request | 调用任意 REST API | Method、URL、Headers、Body |
| Merge | 把两条分支的数据按字段合并 | Mode：Append / Multiplex / Keep Key Matches |
| Set | 新增/修改字段，方便下游使用 | Fields → Name & Value |
...
## 6. 触发器怎么选？
...
- Manual Trigger：调试必用，生产环境可关闭。
- Schedule：定时跑批，最小粒度 1 分钟。
- Webhook：实时响应外部系统；URL 格式`https://你的域名/webhook/工作流UUID`。
- On App Events（第三方服务）：需要先在 Credentials 里完成 OAuth 授权。
...
## 7. 调试技巧与常见报错
...
1. 节点红框→ 点开节点看「Error」标签；常见 401 / 403 先检查 Credentials 是否过期。
2. 数据为空→ 用「Execute node」单步运行，确认上游是否返回 items。
3. 时区错误→ Schedule 默认 UTC，可在环境变量加`GENERIC_TIMEZONE=Asia/Shanghai`。
4. 内存占用高→ 大量文件时改用「Split In Batches」节点分块处理。
...
## 8. 下一步：官方文档 + 社区资源
...
- 官方文档（中英双语）： https://docs.n8n.io
- 中文实战合集（CSDN）： n8n 系列教程 @Lilith [^11^]
- 节点市场： community nodes，装完需重启 n8n。
- GitHub 讨论区： n8n/discussions，官方开发者在线答疑。
...
🎉 至此，你已拥有可运行的 n8n 环境 + 第一个自动化工作流。后续可尝试接入企业微信、Notion、Google Sheets 等节点，逐步把日常重复操作全部自动化。如果遇到问题，先去官方论坛搜索错误文本，90% 已有解决方案。祝自动化愉快！

