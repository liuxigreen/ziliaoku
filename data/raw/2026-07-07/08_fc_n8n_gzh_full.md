---
title: "10分钟搭建n8n自动写公众号：0基础保姆级实操，全流程拆解"
author: "莎姐"
platform: 公众号
source: Firecrawl scrape
url: "https://mp.weixin.qq.com/s/omrAmluJswAupBzTgJ5XGw"
published: "2025-10-16"
collected: "2026-07-07"
verdict: "collect"
reusable_core: "n8n自动写公众号完整流水线：trigger→AI Agent生成内容→code节点排版→生图API→上传封面→发送草稿箱"
---

# 10分钟搭建n8n自动写公众号：0基础保姆级实操，全流程拆解

作者：莎姐（莎姐聊AI）
发布：2025年10月16日

这篇实操只做一件事：用n8n在10分钟内搭起一条"自动写公众号"的流水线。0基础可以做，不需要写代码(AI写)。全文带你完成：选题→AI生成文稿和封面→正文排版→上传草稿。最后点击"执行"，就能让第一篇自动化生成的文章出现在你的公众号后台。

## 流程梳理
写公众号的流程：标题，文章内容，封面图片。
- 标题和文章内容都可以通过大模型来生成
- 封面图片可以通过生图模型来完成

## 安装节点
安装第三方微信公众号社区节点（n8n-nodes-wechat-officialaccount）

## 生成文章内容
1. 添加trigger节点，输入文章主题
2. 添加AI Agent节点，根据主题生成文章内容和标题、生图提示词
3. 添加DeepSeek大模型（也可换GPT、Gemini等）
4. 配置输出格式：文章内容和标题，生图提示词

## 内容排版
用code节点对生成内容进行排版，代码可让AI帮忙生成。

## 生成封面
选用Doubao-Seedream-4.0生图模型。
通过HTTP节点调用API：
```
POST https://ark.cn-beijing.volces.com/api/v3/images/generations
model: doubao-seedream-4-0-250828
```
将生图提示词拖入节点，执行后生成图片URL。
用HTTP节点将图片URL转为file数据。

## 上传封面
添加上传图片节点，配置AppID和AppSecret。
获取方式：公众号后台→设置开发→开发接口管理。
IP白名单填写n8n服务器IP地址。

## 上传文章到草稿箱
添加发送草稿箱节点。文章内容包括：标题、内容和封面。
运行三次，生成三次草稿。

## 结语
从"输入主题"到"草稿生成"的完整链路已跑通：自动生成封面、文案结构清晰、基本排版自动完成。
需要精细化的地方：AI生成内容质量、去除AI味——需要提示词辅助。
只要可以自动上传到草稿箱，剩下的就是对内容、标题、封面、排版的精进。

## 作者其他n8n系列文章
- n8n x PostgreSQL数据库 打造数据自动化
- n8n x Notion 效率神器
- n8n+AI打造内容生产机
- n8n保姆级教程：Code节点4种用法
- n8n × 豆包 4.0：批量自动化生图
- n8n×Docker×Playwright：小红书自动上传避坑指南
- n8n实战：5分钟搞定小红书图文笔记工作流
- n8n踩坑血泪史
- n8n核心节点类型保姆级指南
- n8n进阶实战：AI新闻机器人升级版
- n8n保姆级教程：10分钟搭建自动推送新闻机器人
