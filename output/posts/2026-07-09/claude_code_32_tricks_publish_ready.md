---
final_title: "让AI自己提问，返工少一半"
platform: 小红书
content_angle: 信息差干货型
source_type: 译介
original_title: "32 Tricks to Level Up Claude Code in 16 Mins"
original_author: "Nate Herk | AI Automation"
original_url: "https://www.youtube.com/watch?v=jqoFP9QapXI"
original_lang: en
tags: ["ClaudeCode", "AI编程", "AI工具", "效率工具", "程序员日常", "内容创作"]
cta: "你用 Claude Code 最常被哪一步卡住？评论区聊聊，我挑几个说说是怎么回事。"
collected: "2026-07-09"
---

用 Claude Code 半年，直到刷到 Nate Herk 那期"32 个技巧"，才惊觉自己一直在裸奔。

说实话，大部分人（包括之前的我）把它当"高级补全"用——丢句需求就等它吐代码。结果不是它不行，是用错了。这期是英语一手实操，我看完整个人清醒了，扒出最该抄的 3 个：

**1）先让它问够，再让它动**
进 plan mode，明确告诉它："连续问我问题，直到你 95% 确信懂我要啥。"对齐这一步省下的返工，比你想象的多。我踩过坑：没对齐就开干，同一个功能改了三回。

**2）把"自检"写进待办清单**
别等它交付才验收。让它每做完一项，自己截图看一眼、开 DevTools 查报错。质量检查直接焊进执行计划，它就不是"写完丢给你挑刺"，而是"写完自己先过一遍"。

**3）上下文快炸就压，换活就清**
对话到 60% 左右打 /compact 压缩历史；彻底换任务用 /clear 重开。还有条铁律：别把整个代码库塞进对话，只给当前任务要的。噪音越少它越聪明——这点太多人忽略。

顺手记两个小习惯：每次开老项目先 /init，它会扫一遍生成 CLAUDE.md 当项目 cheat sheet，不用每轮重新讲背景；/statusline 能在终端底部挂个小仪表盘，看剩余上下文和花费，避免"上下文腐烂"。

说点我的不同意见：视频里 sub-agents 并行那段很酷，但我劝新手先别碰。先把"对齐 + 自检"这两个习惯练成本能，比追花活实在。稳的玩法永远是——AI 跑流程，人盯关键节点。

你用 Claude Code 最常被哪一步卡住？评论区聊聊，我挑几个说说是怎么回事。
