---
title: "Claude Code tips for terminal users (from a senior dev)"
author: "Marmelab"
platform: Reddit
source: agent-reach reddit
source_type: aggregator_discovery
source_platform: reddit
subreddit: "r/ClaudeAI"
score: 1129
comments: 109
url: "https://www.reddit.com/r/ClaudeAI/comments/1tbwwel/claude_code_tips_for_terminal_users_from_a_senior/"
published: "2026-05-13"
query_track: "赛道1-AI工具"
collected: "2026-07-07"
---

# Claude Code tips for terminal users (from a senior dev)

**作者**：Marmelab（r/ClaudeAI）｜ **赞**：1129 ｜ **评论**：109

I've been using Claude Code heavily in the terminal for the past 6+ months (as a Linux user you don't get the luxury of a dedicated Claude desktop app lol). But tbh what might seem like a constraint at first, really isn't (at least from my experience). If anything, it forced me to dig deeper into what Claude Code actually offers beyond the basic chat loop. And over time, I realized I'd been barely scratching the surface of what it can do.

Here are 5 hidden commands (or at least ones I completely missed at the beginning) that transformed my daily workflow:

* **Customize your statusline with** `/statusline`: I personally like having a persistent status bar that gives me key info at a glance, and this command adds exactly that at the bottom of your terminal. You can ask Claude to put whatever you want in it (model, branch, context % etc.).
* **Run shell commands with** `!`: You can run any shell command directly from the chat by prefixing it with `!`. The output stays in the conversation, so you can follow up without copy-pasting. Press `Ctrl+B` while a `!` command is running to send (long-running) commands to the background.
* **Mention files with @:** Type `@` \+ filename to trigger path autocomplete. This is way faster than letting Claude wander around your repo looking for the right file.
* **Expand your working context with** `/add-dir`: Add another directory to the session. Perfect for projects split across multiple repos.
* **Start a side conversation with** `/btw`: Ask a quick question without interrupting Claude's current task. For longer side discussions, you can use `/branch` to spin off a new session instead.

Tbh none of this is anything super fancy. But still, these small things have removed a lot of friction for me. Which commands are you guys using?
