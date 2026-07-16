---
title: "Vincent Yang (@m1ssuo)"
author: "Vincent Yang"
platform: X/Twitter
source: SoPilot热帖
published: "Fri, 10 Jul 2026 04:05:52 GMT"
viral_probability: "100%，预测浏览量:72000，预测评论浏览量:700"
predicted_views: "72000，预测评论浏览量:700"
original_url: "https://x.com/m1ssuo/status/2075431284118307061"
sopilot_link: "https://sopilot.net/hot-tweets?tweetId=2075431284118307061"
collected: "2026-07-10"
---

砸壳让 Claude 分析了一下。

它的实际工作流程是这样的（业界叫 "soft ask / 预授权"）：
1. App 先弹自己那个自定义弹窗（自绘的、带营销文案、"允许 / 不允许"按钮是仿系统样式的自定义按钮）；
2. 只有你点了它自定义的"允许"，App 才会去真正调用系统的 UNUserNotificationCenter.requestAuthorization，这时才弹出真正无法改文案的 iOS 系统弹窗。

这么做的目的：iOS 的真实系统授权弹窗一个 App
