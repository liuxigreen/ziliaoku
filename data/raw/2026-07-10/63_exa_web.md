---
title: "n8n 工作流自动化从入门到实战 — 朝花夕拾"
platform: 网页/公众号
source: Exa搜索
search_query: "n8n 自动化工作流 搭建 教程"
url: "https://aprilzz.com/tutorials/n8n-workflow-automation/"
published: "2026-05-09T11:22:18.000Z"
collected: "2026-07-10"
---


n8n 工作流自动化从入门到实战 — 朝花夕拾
...
原文来源： n8n— 开源工作流自动化平台，支持 400+ 应用集成和 AI 节点，是 Zapier 和 Make 的自托管替代方案。
...
n8n 是什么
...
n8n 是开源的工作流自动化工具，用可视化节点编辑器把不同服务连接起来。当 A 应用发生某事件时，自动触发 B 应用的某操作。支持超过 400 种集成，包括 GitHub、Slack、Notion、Google Sheets、Telegram 等主流服务。
...
代码节点 — 除了可视化节点，还可以写 JavaScript/Python 处理复杂逻辑
...
工作流 — 内置 LangChain 节点，可以把
...
M 接入工作流
...
触发器丰富 — 定时触发、Webhook、事件驱动、手动执行等多种方式。
...
Docker（最简单）
...
```
docker volume create n8n_data
docker run -it --rm \
-v n8n_data:/home/node/.n8n \
-p 5678:5678 \
-e N8N_BASIC_AUTH_ACTIVE=true \
-e N8N_BASIC_AUTH_USER=admin \
-e N8N_BASIC_AUTH_PASSWORD=password \
n8nio/n8n
```
...
访问`http://localhost:5678`即可使用。
...
```
npm install n8n -g
n8n start
```
...
Docker Compose（生产推荐）
...
```
version: "3"
services:
n8n:
image: n8nio/n8n
ports:
- "5678:5678"
volumes:
- ~/.n8n:/home/node/.n8n
environment:
- N8N_BASIC_AUTH_ACTIVE=true
- N8N_BASIC_AUTH_USER=admin
- N8N_BASIC_AUTH_PASSWORD=password
```
...
## 创建第一个工作流
...
场景：GitHub 新 Issue 自动发 Slack 通知
...
1. 点击 "Add Workflow"
2. 添加 GitHub Trigger 节点，选择 "New Issue" 事件，配置仓库
3. 添加 Slack 节点，选择 "Send Message" 操作
4. 连接两个节点，在 Slack 消息内容中引用 GitHub 的 issue title 和 url
5. 点击 "Save" 和 "Activate"
...
现在每当指定仓库有新 Issue，Slack 频道会自动收到通知。
...
## 常用节点介绍
...
- Set — 设置固定值或变量
- Code — 写 JS/Python 处理数据
- Function — 批量处理输入数据
- IF — 条件分支
- Merge — 合并多个分支的数据
...
- HTTP Request — 调用任意 REST API
- Webhook — 接收外部 HTTP 请求
- Schedule Trigger — 定时执行（Cron 语法）
- Wait — 延迟执行
...
AI 节点
...
- OpenAI Chat Model — 调用 GPT
- Embeddings — 文本向量化
- Vector Store — 向量数据库操作
- Agent — LangChain Agent
...
## 实战：AI 内容摘要工作流
...
一个更复杂的例子：自动监控 RSS 源，用 AI 摘要后发到 Notion。
...
1. Schedule Trigger — 每天早上 8 点执行
2. RSS Read — 获取指定 RSS 源的最新文章
3. HTTP Request — 抓取文章全文
4. OpenAI — 生成摘要（提示词："用 3 句话总结这篇文章的核心观点"）
5. Notion — 创建数据库条目，标题 + 摘要 + 原文链接
...
整个工作流 5 个节点，不需要写代码。
...
n8n 是工作流自动化领域最成熟的开源方案之一。它的节点编辑器直观好用，代码节点又保留了灵活性，自托管模式让数据完全可控。如果你每月在 Zapier 上的花费超过了服务器成本，迁移到 n8n 几乎总是更划算的选择。
...
### n8n 入门指南：2026 年搭建你的第一个 AI Agent 工作流
...
从零开始学习 n8n——开源的工作流自动化平台。本文将教你如何搭建 AI Agent 工作流，连接 LLM、API 和 400+ 服务。2026年5月16日

---

