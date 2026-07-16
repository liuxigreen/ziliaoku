---
title: "ruvnet/ruflo"
author: "ruvnet"
platform: github
source: github_api
source_type: github_discovery
source_platform: github
stars: 63612
forks: 7499
language: "TypeScript"
topics: "agentic-ai, agentic-framework, agentic-workflow, agents, ai-agents, ai-assistant, ai-coding, ai-skills, autonomous-agents, claude-code"
description: "🌊 The leading agent meta-harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, RAG integration, and native Claude Code / Codex / Hermes and many more Integrated"
pushed_at: "2026-07-08T19:15:42Z"
url: "https://github.com/ruvnet/ruflo"
collected: "2026-07-09"
---

# ruvnet/ruflo

> 🌊 The leading agent meta-harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, RAG integration, and native Claude Code / Codex / Hermes and many more Integrated

**Stars**: 63612 ｜ **Forks**: 7499 ｜ **Language**: TypeScript ｜ **最近活跃**: 2026-07-08T19:15:42Z

## README

<div align="center">

[![Ruflo Banner](ruflo/assets/ruflo-small.jpeg)](https://cognitum.one/agentic-engineering)
[![Agentics Foundation Banner](docs/assets/sv-summit.png)](https://agentics.org/siliconvalley/?UTM=GH-RuFlo-SV)


<!-- Try Ruflo — the 4 badges first-time visitors actually act on -->
[![Try the UI Beta — flo.ruv.io](https://img.shields.io/badge/_Try_the_UI_Beta-flo.ruv.io-6366f1?style=for-the-badge&logoColor=white&logo=svelte)](https://flo.ruv.io/)
[![npm version (ruflo)](https://img.shields.io/npm/v/ruflo?label=npx%20ruflo&style=for-the-badge&logo=npm&color=cb3837)](https://www.npmjs.com/package/ruflo)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Star on GitHub](https://img.shields.io/github/stars/ruvnet/claude-flow?style=for-the-badge&logo=github&color=gold)](https://github.com/ruvnet/claude-flow)

<!-- Ecosystem strip (collapsed visually with flat-square) -->
[![Goal Planner](https://img.shields.io/badge/_Goal_Planner-goal.ruv.io-8b5cf6?style=flat-square&logoColor=white&logo=react)](https://goal.ruv.io/)
[![Live Agents](https://img.shields.io/badge/_Live_Agents-goal.ruv.io%2Fagents-10b981?style=flat-square&logoColor=white&logo=react)](https://goal.ruv.io/agents)
[![🕸️ RuVector Agentic DB](https://img.shields.io/badge/RuVector_Agentic-DB-06b6d4?style=flat-square&logoColor=white&logo=graphql)](https://github.com/ruvnet/ruvector)
[![Ecosystem downloads](https://img.shields.io/badge/ecosystem%20downloads-8.1M%2B-blue?style=flat-square&logo=npm)](https://github.com/ruvnet/ruflo/blob/main/data/clone-data.proof.json)
[![Git clones (14d)](https://img.shields.io/badge/git%20clones%2014d-106k-blueviolet?style=flat-square&logo=github)](https://github.com/ruvnet/ruflo/blob/main/data/clone-data.ledger.json)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Plugin-D97757?style=flat-square&logoColor=white&logo=anthropic)](https://github.com/ruvnet/claude-flow)
[![Codex Plugin](https://img.shields.io/badge/Codex-Plugin-412991?style=flat-square&logoColor=white&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0yMi4yODIgOS44MjFhNS45ODUgNS45ODUgMCAwIDAtLjUxNi00LjkxIDYuMDQ2IDYuMDQ2IDAgMCAwLTYuNTEtMi45QTYuMDY1IDYuMDY1IDAgMCAwIDQuOTgxIDQuMThhNS45ODUgNS45ODUgMCAwIDAtMy45OTggMi45IDYuMDQ2IDYuMDQ2IDAgMCAwIC43NDMgNy4wOTcgNS45OCA1Ljk4IDAgMCAwIC41MSA0LjkxMSA2LjA1MSA2LjA1MSAwIDAgMCA2LjUxNSAyLjlBNS45ODUgNS45ODUgMCAwIDAgMTMuMjYgMjRhNi4wNTYgNi4wNTYgMCAwIDAgNS43NzItNC4yMDYgNS45OSA1Ljk5IDAgMCAwIDMuOTk4LTIuOSA2LjA1NiA2LjA1NiAwIDAgMC0uNzQ3LTcuMDczek0xMy4yNiAyMi40M2E0LjQ3NiA0LjQ3NiAwIDAgMS0yLjg3Ni0xLjA0bC4xNDItLjA4IDQuNzc4LTIuNzU4YS43OTUuNzk1IDAgMCAwIC4zOTMtLjY4MXYtNi43MzdsMi4wMiAxLjE2OGEuMDcxLjA3MSAwIDAgMSAuMDM4LjA1MnY1LjU4M2E0LjUwNCA0LjUwNCAwIDAgMS00LjQ5NSA0LjQ5NHpNMy42IDE4LjMwNGE0LjQ3IDQuNDcgMCAwIDEtLjUzNS0zLjAxNGwuMTQyLjA4NSA0Ljc4MyAyLjc1OWEuNzcxLjc3MSAwIDAgMCAuNzgxIDBsNS44NDMtMy4zNjl2Mi4zMzJhLjA4LjA4IDAgMCAxLS4wMzMuMDYyTDkuNzQgMTkuOTVhNC41IDQuNSAwIDAgMS02LjE0LTEuNjQ2ek0yLjM0IDcuODk2YTQuNDg1IDQuNDg1IDAgMCAxIDIuMzY2LTEuOTczVjExLjZhLjc2Ni43NjYgMCAwIDAgLjM4OC42NzdsNS44MTUgMy4zNTQtMi4wMiAxLjE2OGEuMDc2LjA3NiAwIDAgMS0uMDcyIDBsLTQuODMtMi43ODZBNC41MDQgNC41MDQgMCAwIDEgMi4zNCA3Ljg3MnptMTYuNTk3IDMuODU1LTUuODMzLTMuMzg3IDIuMDE2LTEuMTY1YS4wNzYuMDc2IDAgMCAxIC4wNzEgMGw0LjgzIDIuNzkxYTQuNDk0IDQuNDk0IDAgMCAxLS42NzYgOC4xMDR2LTUuNjc3YS43OS43OSAwIDAgMC0uNDA3LS42Njd6bTIuMDEtMy4wMjMtLjE0MS0uMDg1LTQuNzc0LTIuNzgyYS43NzYuNzc2IDAgMCAwLS43ODUgMEw5LjQwOSA5LjIzVjYuODk3YS4wNjYuMDY2IDAgMCAxIC4wMjgtLjA2Mmw0LjgzLTIuNzg3YTQuNDk5IDQuNDk5IDAgMCAxIDYuNjggNC42NnpNOC4zMDcgMTIuODYzbC0yLjAyLTEuMTY0YS4wOC4wOCAwIDAgMS0uMDM4LS4wNTdWNi4wNzRhNC40OTkgNC40OTkgMCAwIDEgNy4zNzYtMy40NTRsLS4xNDIuMDgtNC43NzggMi43NThhLjc5NS43OTUgMCAwIDAtLjM5My42ODJ6bTEuMDk3LTIuMzY2IDIuNjAyLTEuNSAyLjYwNyAxLjV2Mi45OTlsLTIuNTk3IDEuNS0yLjYwNy0xLjVaIi8%2BPC9zdmc%2B)](https://www.npmjs.com/package/@claude-flow/codex)

# Ruflo

**An agent meta-harness for Claude Code and Codex.**

</div>

> **Agent = Model + Harness.** The model writes; the harness gives it tools, memory, loops, sandboxes, and controls so it can actually work. **Ruflo is the harness** — the execution layer around Claude Code and Codex that adds 100+ specialized agents, coordinated swarms, self-learning memory, federated comms across machines, and enterprise security guardrails. So agents don't just run, they collaborate.

One `npx ruflo init` gives Claude Code a nervous system: agents self-organize into swarms, learn from every task, remember across sessions, and — with federation — securely talk to agents on other machines without leaking data. You keep writing code. Ruflo handles the coordination.

```
Self-Learning / Self-Optimizing Agent Architecture

User --> Ruflo (CLI/MCP) --> Router --> Swarm --> Agents --> Memory --> LLM Providers
                          ^                           |
                          +---- Learning Loop <-------+
```

> **New to Ruflo?** You don't need to learn 314 MCP tools or 26 CLI commands. After `init`, just use Claude Code normally — the hooks system automatically routes tasks, learns from successful patterns, and coordinates agents in the background.

<details>
<summary><strong>📖 Background — where the name comes from</strong></summary>

> Claude Flow is now Ruflo — named by [`rUv`](https://ruv.io), who loves Rust, flow states, and building things that feel inevitable. The "Ru" is the rUv. The "flo" is working until 3am. Underneath, powered by [`Cognitum.One`](https://cognitum.one/?RuFlo) agentic architecture, running a supercharged Rust-based AI engine, embeddings, memory, and plugin system.

</details>

---

![Ruflo Plugins](./ruflo-plugins.gif)

## Quick Start

There are **two different install paths** with very different surface areas. Pick based on what you need (#1744):

| | **Claude Code Plugin** | **CLI install (`npx ruflo init`)** |
|---|---|---|
| What it gives you | Slash commands + a few skills + agent definitions per-plugin | Full Ruflo loop — 98 agents, 60+ commands, 30 skills, MCP server, hooks, daemon |
| Files in your workspace | **Zero** | `.claude/`, `.claude-flow/`, `CLAUDE.md`, helpers, settings |
| MCP server registered | **No** (`memory_store`, `swarm_init`, etc. unavailable to Claude) | Yes |
| Hooks installed | No | Yes |
| Best for | Try a single plugin's commands without committing to the full install | Production use — everything works as documented |

### Path A — Claude Code Plugins (lite, slash commands only)

```bash
# Add the marketplace
/plugin marketplace add ruvnet/ruflo

# Install core + any plugins you need
/plugin install ruflo-core@ruflo
/plugin install ruflo-swarm@ruflo
/plugin install ruflo-rag-memory@ruflo
/plugin install ruflo-neural-trader@ruflo
```

This adds slash commands and agent definitions only. The Ruflo MCP server is NOT registered, so `memory_store`, `swarm_init`, `agent_spawn`, etc. won't be callable from Claude. For the full loop, use Path B below.

<details>
<summary><strong>🔌 All 35 plugins</strong></summary>

#### Core & Orchestration

| Plugin | What it does |
|--------|-------------|
| [**ruflo-core**](plugins/ruflo-core/README.md) | Foundation — server, health checks, plugin discovery |
| [**ruflo-swarm**](plugins/ruflo-swarm/README.md) | Coordinate multiple agents as a team |
| [**ruflo-autopilot**](plugins/ruflo-autopilot/README.md) | Let agents run autonomously in a loop |
| [**ruflo-loop-workers**](plugins/ruflo-loop-workers/README.md) | Schedule background tasks on a timer |
| [**ruflo-workflows**](plugins/ruflo-workflows/README.md) | Reusable multi-step task templates |
| [**ruflo-federation**](plugins/ruflo-federation/README.md) | Agents on different machines collaborate securely |

#### Memory & Knowledge

| Plugin | What it does |
|--------|-------------|
| [**ruflo-agentdb**](plugins/ruflo-agentdb/README.md) | Fast vector database for agent memory |
| [**ruflo-rag-memory**](plugins/ruflo-rag-memory/README.md) | Smart retrieval — hybrid search, graph hops, diversity ranking |
| [**ruflo-rvf**](plugins/ruflo-rvf/README.md) | Save and restore agent memory across sessions |
| [**ruflo-ruvector**](plugins/ruflo-ruvector/README.md) | [`ruvector`](https://npmjs.com/package/ruvector) — GPU-accelerated search, Graph RAG, 103 tools |
| [**ruflo-knowledge-graph**](plugins/ruflo-knowledge-graph/README.md) | Build and traverse entity relationship maps |

#### Intelligence & Learning

| Plugin | What it does |
|--------|-------------|
| [**ruflo-intelligence**](plugins/ruflo-intelligence/README.md) | Agents learn from past successes and get smarter |
| [**ruflo-graph-intelligence**](plugins/ruflo-graph-intelligence/) | Sublinear graph reasoning — PageRank, delta updates, complexity-aware execution (ADR-123) |
| [**ruflo-daa**](plugins/ruflo-daa/README.md) | Dynamic agent behavior and cognitive patterns |
| [**ruflo-ruvllm**](plugins/ruflo-ruvllm/README.md) | Run local L
