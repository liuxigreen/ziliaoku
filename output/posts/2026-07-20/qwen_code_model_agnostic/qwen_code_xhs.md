# 别给AI编程工具交月费了

Cursor 月费 $20，Claude Code 按 token 烧钱，用一个月心疼一个月。

直到我发现 qwen-code——阿里通义千问团队开源的终端 AI 编程 Agent，25000+ 星，Apache 2.0，完全免费。

关键不是免费，是它**不绑定模型**。

什么意思？Cursor 深度绑 GPT，Claude Code 绑 Claude，你选了工具就被锁死在那个模型里。qwen-code 同时支持 OpenAI / Anthropic / Gemini / Qwen 四种协议，改一行配置就能换"大脑"。

实操效果：日常 CRUD 用国产小模型，token 价格远低于闭源大模型；复杂架构推理再切大模型。综合成本砍掉一大半。

装也简单：
1. npm install -g @qwen-code/qwen-code
2. 配你的 API Key（哪个模型都行）
3. 终端跑 qwen-code，开干

它还有桌面版、Web 版、VS Code 插件，不止终端。

提醒：开源 ≠ 完美。早期版本会有 bug，别拿生产环境直接上；国产模型编程能力追平了但不是全面超越，复杂场景还是得上大模型。

但至少，你不再被月费绑架了。

#AI工具 #开源 #程序员 #打工人摸鱼 #效率提升
