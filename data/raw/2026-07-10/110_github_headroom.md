---
title: "headroomlabs-ai/headroom"
author: "headroomlabs-ai"
platform: github
source: github_api
source_type: github_discovery
source_platform: github
stars: 58234
forks: 4301
language: "Python"
topics: "agent, ai, anthropic, claude-code, compression, context-engineering, context-window, cursor, fastapi, langchain"
description: "Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 60-95% fewer tokens, same answers. Library, proxy, MCP server."
pushed_at: "2026-07-10T06:18:06Z"
url: "https://github.com/headroomlabs-ai/headroom"
collected: "2026-07-10"
---

# headroomlabs-ai/headroom

> Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 60-95% fewer tokens, same answers. Library, proxy, MCP server.

**Stars**: 58234 ｜ **Forks**: 4301 ｜ **Language**: Python ｜ **最近活跃**: 2026-07-10T06:18:06Z

## README

<div align="center"><pre>
  ██╗  ██╗███████╗ █████╗ ██████╗ ██████╗  ██████╗  ██████╗ ███╗   ███╗
  ██║  ██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║
  ███████║█████╗  ███████║██║  ██║██████╔╝██║   ██║██║   ██║██╔████╔██║
  ██╔══██║██╔══╝  ██╔══██║██║  ██║██╔══██╗██║   ██║██║   ██║██║╚██╔╝██║
  ██║  ██║███████╗██║  ██║██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║
  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝
              The context compression layer for AI agents
</pre></div>

<p align="center"><strong>60–95% fewer tokens (for JSON data), 15-20% fewer tokens (for coding agents) · library · proxy · MCP · content-aware compressors · local-first · reversible</strong></p>

<p align="center">
  <a href="https://github.com/chopratejas/headroom/actions/workflows/ci.yml"><img src="https://github.com/chopratejas/headroom/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://app.codecov.io/gh/chopratejas/headroom"><img src="https://codecov.io/gh/chopratejas/headroom/graph/badge.svg" alt="codecov"></a>
  <a href="https://pypi.org/project/headroom-ai/"><img src="https://img.shields.io/pypi/v/headroom-ai.svg" alt="PyPI"></a>
  <a href="https://www.npmjs.com/package/headroom-ai"><img src="https://img.shields.io/npm/v/headroom-ai.svg" alt="npm"></a>
  <a href="https://huggingface.co/chopratejas/kompress-v2-base"><img src="https://img.shields.io/badge/model-Kompress--v2--base-yellow.svg" alt="Model: Kompress-v2-base"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-blue.svg" alt="License: Apache 2.0"></a>
  <a href="https://headroom-docs.vercel.app/docs"><img src="https://img.shields.io/badge/docs-online-blue.svg" alt="Docs"></a>
</p>

<p align="center">
  <a href="https://headroom-docs.vercel.app/docs">Docs</a> ·
  <a href="#get-started-60-seconds">Install</a> ·
  <a href="#proof">Proof</a> ·
  <a href="#agent-compatibility-matrix">Agents</a> ·
  <a href="https://discord.gg/yRmaUNpsPJ">Discord</a> ·
  <a href="llms.txt">llms.txt</a>
</p>

<p align="center"><sub>
  <b>AI agents / LLMs:</b> read <a href="llms.txt"><code>/llms.txt</code></a> here, or fetch <a href="https://headroom-docs.vercel.app/llms.txt">the live index</a> / <a href="https://headroom-docs.vercel.app/llms-full.txt">full docs blob</a>.
</sub></p>

---
<p align="center"><a href="https://trendshift.io/repositories/20881" target="_blank"><img src="https://trendshift.io/api/badge/repositories/20881" alt="chopratejas%2Fheadroom | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a></p>

Headroom compresses everything your AI agent reads — tool outputs, logs, RAG chunks, files, and conversation history — before it reaches the LLM. Same answers, fraction of the tokens.

<p align="center">
  <img src="HeadroomDemo-Fast.gif" alt="Headroom in action" width="820">
  <br/><sub>Live: 10,144 → 1,260 tokens — same FATAL found.</sub>
</p>

## What it does

- **Library** — `compress(messages)` in Python or TypeScript, inline in any app
- **Proxy** — `headroom proxy --port 8787`, zero code changes, any language
- **Agent wrap** — `headroom wrap claude|codex|copilot|cursor|aider|opencode|cline|continue|goose|openhands|openclaw|vibe` in one command; undo with `headroom unwrap <tool>`
- **MCP server** — `headroom_compress`, `headroom_retrieve`, `headroom_stats` for any MCP client
- **Cross-agent memory** — shared store across Claude, Codex, Gemini, auto-dedup
- **`headroom learn`** — mines failed sessions, writes corrections to `CLAUDE.local.md` (default, gitignored) or `CLAUDE.md` / `AGENTS.md` / `GEMINI.md`
- **Output token reduction** — trims what the model *writes back* (not just what you send): drops ceremony/restated code and skips deep "thinking" on routine steps. See [Output token reduction](#output-token-reduction-cut-what-the-model-writes-back).
- **Reversible (CCR)** — originals are cached for retrieval on demand

## How it works (30 seconds)

```
 Your agent / app
   (Claude Code, Cursor, Codex, LangChain, Agno, Strands, your own code…)
        │   prompts · tool outputs · logs · RAG results · files
        ▼
    ┌────────────────────────────────────────────────────┐
    │  Headroom   (runs locally — your data stays here)  │
    │  ────────────────────────────────────────────────  │
    │  CacheAligner  →  ContentRouter  →  CCR            │
    │                    ├─ SmartCrusher   (JSON)        │
    │                    ├─ CodeCompressor (AST)         │
    │                    └─ Kompress-v2-base (text, HF)  │
    │                                                    │
    │  Cross-agent memory  ·  headroom learn  ·  MCP     │
    └────────────────────────────────────────────────────┘
        │   compressed prompt  +  retrieval tool
        ▼
 LLM provider  (Anthropic · OpenAI · Bedrock · …)
```

- **ContentRouter** — detects content type, selects the right compressor
- **SmartCrusher / CodeCompressor / Kompress-v2-base** — compress JSON, AST, or prose
- **CacheAligner** — stabilizes prefixes so provider KV caches actually hit
- **CCR** — stores originals locally; LLM calls `headroom_retrieve` if it needs them

→ [Architecture](https://headroom-docs.vercel.app/docs/architecture) · [CCR reversible compression](https://headroom-docs.vercel.app/docs/ccr) · [Kompress-v2-base model card](https://huggingface.co/chopratejas/kompress-v2-base)

## Get started (60 seconds)

```bash
# 1 — Install
uv tool install "headroom-ai[all]"      # Install `headroom` CLI as a global tool in self-contained virtual env
pip install "headroom-ai[all]"          # Python — ships the `headroom` CLI
npm install headroom-ai                 # TypeScript SDK only — no `headroom` CLI

# 2 — Pick your mode  (the `headroom` commands below come from the uv or pip install)
headroom wrap claude                    # wrap a coding agent
headroom proxy --port 8787              # drop-in proxy, zero code changes
# or: from headroom import compress      # inline library

# 3 — Verify setup and see the savings
headroom doctor                         # health check — confirms routing is working
headroom perf
headroom dashboard                      # live savings dashboard (proxy must be running)
```

To use headroom, it is recommended you launch a wrapped agent session each time so that all necessary setup is completed. When wrapping a coding agent, headroom starts a local proxy, sets up an MCP server that provides tools such as rtk and tokensave, and launches a coding agent session configured to proxy requests to headroom. 

The `headroom` CLI ships **only** via the PyPI package. The npm `headroom-ai` is the TypeScript SDK — a library you import (`import { compress } from 'headroom-ai'`), not a CLI, so it provides no `headroom` command.

Granular extras: `[proxy]`, `[mcp]`, `[ml]`, `[code]`, `[memory]`, `[vector]` (optional HNSW backend — needs a C++ toolchain, not in `[all]`), `[relevance]`, `[image]`, `[agno]`, `[langchain]`, `[evals]`, `[pytorch-mps]` (Apple-GPU memory-embedder offload — set `HEADROOM_EMBEDDER_RUNTIME=pytorch_mps`). Requires **Python 3.10+**.

### Codex / global install

If Codex or another MCP client cannot inherit a shell `PATH` reliably, install Headroom as a persistent uv tool and point the client at the absolute binary path:

```bash
uv tool install "headroom-ai[all]"
command -v headroom
```

Then use the returned path in MCP config:

```toml
[mcp_servers.headroom]
command = "/absolute/path/from/command-v/headroom"
args = ["mcp", "serve"]
```

`command = "headroom"` only works when the client starts with a `PATH` that already includes the uv tool directory.

## Proof

**Savings on real agent workloads:**

| Workload                      | Before | After  | Savings |
|-------------------------------|-------:|-------:|--------:|
| Code search (100 results)     | 17,765 |  1,408 | **92%** |
| SRE incident debugging        | 65,694 |  5,118 | **92%** |
| GitHub issue triage           | 54,174 | 14,761 | **73%** |
| Codebase exploration          | 78,502 | 41,254 | **47%** |

**Accuracy preserved on standard benchmarks:**

| Benchmark  | Category | N   | Baseline | Headroom | Delta      |
|------------|----------|----:|---------:|---------:|------------|
| GSM8K      | Math     | 100 |    0.870 |    0.870 | **±0.000** |
| TruthfulQA | Factual  | 100 |    0.530 |    0.560 | **+0.030** |
| SQuAD v2   | QA       | 100 |        — |  **97%** | 19% compression |
| BFCL       | Tools    | 100 |        — |  **97%** | 32% compression |

Reproduce: `python -m headroom.evals suite --tier 1` · [Full benchmarks & methodology](https://headroom-docs.vercel.app/docs/benchmarks)

## Output token reduction (cut what the model writes back)

Everything above shrinks the prompt you **send**. But you also pay for every
token the model **writes back** — and on Opus-class models output costs 5× input.
A lot of that output is waste: "Great, let me…" preambles, re-printing code you
just showed it, and deep "think
