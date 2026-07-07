---
title: "I Spent 2000 Hours Coding With LLMs in 2025. Here are my Favorite Claude Code Usage Patterns"
author: "agenticlab1"
platform: Reddit
source: agent-reach reddit
source_type: aggregator_discovery
source_platform: reddit
subreddit: "r/ClaudeAI"
score: 570
comments: 442
url: "https://www.reddit.com/r/ClaudeAI/comments/1q3t579/i_spent_2000_hours_coding_with_llms_in_2025_here/"
published: "2026-01-04"
query_track: "赛道1-AI工具"
collected: "2026-07-07"
---

# I Spent 2000 Hours Coding With LLMs in 2025. Here are my Favorite Claude Code Usage Patterns

**作者**：agenticlab1（r/ClaudeAI）｜ **赞**：570 ｜ **评论**：442

Contrary to popular belief, LLM assisted coding is an unbelievably difficult skill to master.

Core philosophy: Any issue in LLM generated code is solely due to YOU. Errors are traceable to improper prompting or improper context engineering. Context rot (and lost in the middle) impacts the quality of output heavily, and does so very quickly.

Here are the patterns that actually moved the needle for me. I guarantee you haven't heard of at least one:

1. **Error Logging System** \- Reconstructing the input-output loop that agentic coding hides from you. Log failures with the exact triggering prompt, categorize them, ask "what did I do wrong." Patterns emerge.
2. **/Commands as Lightweight Local Apps** \- Slash commands are secretly one of the most powerful parts of Claude Code. I think of them as Claude as a Service, workflows with the power of a SaaS but way quicker to build.
3. **Hooks for Deterministic Safety** \- dangerously-skip-permissions + hooks that prevent dangerous actions = flow state without fear.
4. **Context Hygiene** \- Disable autocompact. Add a status line mentioning the % of context used. Compaction is now done when and how YOU choose. Double-escape time travel is the most underutilized feature in Claude Code.
5. **Subagent Control** \- Claude Code consistently spawns Sonnet/Haiku subagents even for knowledge tasks. Add "Always launch opus subagents" to your global CLAUDE.md. Use subagents way more than you think for big projects. Orchestrator + Subagents >> Claude Code vanilla.
6. **The Reprompter System** \- Voice dictation → clarifying questions → structured prompt with XML tags. Prompting at high quality without the friction of typing.

I wrote up a 16 page google doc with more tips and details, exact slash commands, code for a subagent monitoring dashboard, and a quick reference table. Comment 'interested' if you want it.
