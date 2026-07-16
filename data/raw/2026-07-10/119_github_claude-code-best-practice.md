---
title: "shanraisshan/claude-code-best-practice"
author: "shanraisshan"
platform: github
source: github_api
source_type: github_discovery
source_platform: github
stars: 62373
forks: 6242
language: "HTML"
topics: "agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude"
description: "from vibe coding to agentic engineering - practice makes claude perfect"
pushed_at: "2026-07-10T06:12:38Z"
url: "https://github.com/shanraisshan/claude-code-best-practice"
collected: "2026-07-10"
---

# shanraisshan/claude-code-best-practice

> from vibe coding to agentic engineering - practice makes claude perfect

**Stars**: 62373 ｜ **Forks**: 6242 ｜ **Language**: HTML ｜ **最近活跃**: 2026-07-10T06:12:38Z

## README

# claude-code-best-practice
from vibe coding to agentic engineering - practice makes claude perfect

![updated with Claude Code](https://img.shields.io/badge/updated_with_Claude_Code-Jul%2010%2C%202026%209%3A42%20AM%20PKT-white?style=flat&labelColor=555) <a href="https://github.com/shanraisshan/claude-code-best-practice/stargazers"><img src="https://img.shields.io/github/stars/shanraisshan/claude-code-best-practice?style=flat&label=%E2%98%85&labelColor=555&color=white" alt="GitHub Stars"></a><br>

[![Best Practice](!/tags/best-practice.svg)](best-practice/) [![Implemented](!/tags/implemented.svg)](implementation/) [![Orchestration Workflow](!/tags/orchestration-workflow.svg)](orchestration-workflow/orchestration-workflow.md) [![Claude](!/tags/claude.svg)](https://code.claude.com/docs) [![Boris](!/tags/boris-cherny.svg)](#-tips-and-tricks) [![Community](!/tags/community.svg)](#-subscribe) ![Click on these badges below to see the actual sources](!/tags/click-badges.svg)<br>
<img src="!/tags/a.svg" height="14"> = Agents · <img src="!/tags/c.svg" height="14"> = Commands · <img src="!/tags/s.svg" height="14"> = Skills

<p align="center">
  <img src="!/claude-jumping.svg" alt="Claude Code mascot jumping" width="120" height="100"><br>
  <a href="https://github.com/trending"><img src="!/root/github-trending-day.svg" alt="GitHub Trending #1 Repository Of The Day"></a>
</p>

<p align="center">
  <img src="!/root/supported-label.svg" alt="Supported by:" height="34">&nbsp;&nbsp;<a href="https://disrupt.com/?utm_source=github&utm_campaign=shayan_claude_code_best_practice"><img src="!/root/supported-disrupt.svg" alt="Disrupt.com — Ventures Reimagined" height="34"></a>&nbsp;&nbsp;<a href="https://claudekit.cc/?utm_source=github&utm_medium=sponsorship&utm_campaign=shayan_claude_code_best_practice"><img src="!/root/supported-claudekit.svg" alt="ClaudeKit — Production-ready skills and workflows" height="34"></a>
</p>

<p align="center">
  <img src="!/root/boris-slider.gif" alt="Boris Cherny on Claude Code" width="600"><br>
  Boris Cherny on X (<a href="https://x.com/bcherny/status/2007179832300581177">tweet 1</a> · <a href="https://x.com/bcherny/status/2017742741636321619">tweet 2</a> · <a href="https://x.com/bcherny/status/2021699851499798911">tweet 3</a>)
</p>

> [!TIP]
> Visit the [**How to Use**](#how-to-use) section to take full advantage of this repo.

## 🧠 CONCEPTS

| Feature | Location | Description |
|---------|----------|-------------|
| <img src="!/tags/a.svg" height="14"> [**Subagents**](https://code.claude.com/docs/en/sub-agents) | `.claude/agents/<name>.md` | [![Best Practice](!/tags/best-practice.svg)](best-practice/claude-subagents.md) [![Implemented](!/tags/implemented.svg)](implementation/claude-subagents-implementation.md) |
| <img src="!/tags/c.svg" height="14"> [**Commands**](https://code.claude.com/docs/en/slash-commands) | `.claude/commands/<name>.md` | [![Best Practice](!/tags/best-practice.svg)](best-practice/claude-commands.md) [![Implemented](!/tags/implemented.svg)](implementation/claude-commands-implementation.md) |
| <img src="!/tags/s.svg" height="14"> [**Skills**](https://code.claude.com/docs/en/skills) | `.claude/skills/<name>/SKILL.md` | [![Best Practice](!/tags/best-practice.svg)](best-practice/claude-skills.md) [![Implemented](!/tags/implemented.svg)](implementation/claude-skills-implementation.md) [Official Skills](https://github.com/anthropics/skills/tree/main/skills) · [Skills for Mono-repos](reports/claude-skills-for-larger-mono-repos.md) |
| [**Workflows**](https://code.claude.com/docs/en/common-workflows) | [`.claude/commands/weather-orchestrator.md`](.claude/commands/weather-orchestrator.md) | [![Orchestration Workflow](!/tags/orchestration-workflow.svg)](orchestration-workflow/orchestration-workflow.md) |
| [**Hooks**](https://code.claude.com/docs/en/hooks) | `.claude/hooks/` | [![Best Practice](!/tags/best-practice.svg)](https://github.com/shanraisshan/claude-code-hooks) [![Implemented](!/tags/implemented.svg)](https://github.com/shanraisshan/claude-code-hooks) [Guide](https://code.claude.com/docs/en/hooks-guide) |
| [**MCP Servers**](https://code.claude.com/docs/en/mcp) | `.claude/settings.json`, `.mcp.json` | [![Best Practice](!/tags/best-practice.svg)](best-practice/claude-mcp.md) [![Implemented](!/tags/implemented.svg)](.mcp.json) |
| [**Plugins**](https://code.claude.com/docs/en/plugins) | distributable packages | [Marketplaces](https://code.claude.com/docs/en/discover-plugins) · [Create Marketplaces](https://code.claude.com/docs/en/plugin-marketplaces) |
| [**Settings**](https://code.claude.com/docs/en/settings) | `.claude/settings.json` | [![Best Practice](!/tags/best-practice.svg)](best-practice/claude-settings.md) [![Implemented](!/tags/implemented.svg)](.claude/settings.json) [Permissions](https://code.claude.com/docs/en/permissions) · [Model Config](https://code.claude.com/docs/en/model-config) · [Output Styles](https://code.claude.com/docs/en/output-styles) · [Sandboxing](https://code.claude.com/docs/en/sandboxing) · [Keybindings](https://code.claude.com/docs/en/keybindings) · [Auto Mode Config](https://code.claude.com/docs/en/auto-mode-config) |
| [**Status Line**](https://code.claude.com/docs/en/statusline) | `.claude/settings.json` | [![Best Practice](!/tags/best-practice.svg)](https://github.com/shanraisshan/claude-code-status-line) [![Implemented](!/tags/implemented.svg)](.claude/settings.json) |
| [**Memory**](https://code.claude.com/docs/en/memory) | `CLAUDE.md`, `.claude/rules/`, `~/.claude/rules/`, `~/.claude/projects/<project>/memory/` | [![Best Practice](!/tags/best-practice.svg)](best-practice/claude-memory.md) [![Implemented](!/tags/implemented.svg)](CLAUDE.md) [Auto Memory](https://code.claude.com/docs/en/memory) · [Auto Memory Deep-dive](reports/claude-agent-memory.md) · [Rules](https://code.claude.com/docs/en/memory#organize-rules-with-clauderules) |
| [**Checkpointing**](https://code.claude.com/docs/en/checkpointing) | automatic (file-edit tracking) |  |
| [**CLI Startup Flags**](https://code.claude.com/docs/en/cli-reference) | `claude [flags]` | [![Best Practice](!/tags/best-practice.svg)](best-practice/claude-cli-startup-flags.md) [Interactive Mode](https://code.claude.com/docs/en/interactive-mode) · [Env Vars](https://code.claude.com/docs/en/env-vars) |
| **AI Terms** | | [![Best Practice](!/tags/best-practice.svg)](https://github.com/shanraisshan/claude-code-codex-cursor-gemini/blob/main/reports/ai-terms.md) |
| [**Best Practices**](https://code.claude.com/docs/en/best-practices) | | [Prompt Engineering](https://github.com/anthropics/prompt-eng-interactive-tutorial) · [Extend Claude Code](https://code.claude.com/docs/en/features-overview) |

### 🔥 Hot

| Feature | Location | Description |
|---------|----------|-------------|
| [**Ultrareview**](https://code.claude.com/docs/en/ultrareview) ![beta](!/tags/beta.svg) | `/code-review ultra`, `claude ultrareview [target]` | [Tasks tracking](https://code.claude.com/docs/en/ultrareview#track-a-running-review) |
| [**Devcontainers**](https://code.claude.com/docs/en/devcontainer) | `.devcontainer/` |  |
| [**Channels**](https://code.claude.com/docs/en/channels) ![beta](!/tags/beta.svg) | `--channels`, plugin-based | [Reference](https://code.claude.com/docs/en/channels-reference) |
| [**Ultraplan**](https://code.claude.com/docs/en/ultraplan) ![beta](!/tags/beta.svg) | `/ultraplan` |  |
| [**No Flicker Mode**](https://code.claude.com/docs/en/fullscreen) ![beta](!/tags/beta.svg) | `/tui fullscreen`, `CLAUDE_CODE_NO_FLICKER=1` | [![Best Practice](!/tags/best-practice.svg)](https://x.com/bcherny/status/2039421575422980329) |
| [**Auto Mode**](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode) ![beta](!/tags/beta.svg) | `--permission-mode auto`, `Shift+Tab` | [![Best Practice](!/tags/best-practice.svg)](https://x.com/claudeai/status/2036503582166393240) [Blog](https://claude.com/blog/auto-mode) |
| [**Power-ups**](best-practice/claude-power-ups.md) | `/powerup` | [![Best Practice](!/tags/best-practice.svg)](best-practice/claude-power-ups.md) |
| [**Fast Mode**](https://code.claude.com/docs/en/fast-mode) ![beta](!/tags/beta.svg) | `/fast`, `"fastMode": true` |  |
| [**Advisor**](https://code.claude.com/docs/en/advisor) ![beta](!/tags/beta.svg) | `/advisor`, `advisorModel`, `--advisor` | [Blog](https://claude.com/blog/the-advisor-strategy) |
| [**Computer Use**](https://code.claude.com/docs/en/computer-use) ![beta](!/tags/beta.svg) | `computer-use` MCP server | [Desktop](https://code.claude.com/docs/en/desktop#let-claude-use-your-computer) |
| [**Agent SDK**](https://code.claude.com/docs/en/agent-sdk/overview) | `npm` / `pip` package | [Quickstart](https://code.claude.com/docs/en/agent-sdk/quickstart) · [Examples](https://github.com/anthropics/claude-agent-sdk-demos) |
| [**Ralph Wiggum Loop**](https://github.com/anthropics/claude-code/tree/main/plugins/ralph-wiggum) | plugin | [![Best Practice](!/tags/bes
