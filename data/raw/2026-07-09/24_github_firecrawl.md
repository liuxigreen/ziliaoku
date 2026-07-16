---
title: "firecrawl/firecrawl"
author: "firecrawl"
platform: github
source: github_api
source_type: github_discovery
source_platform: github
stars: 147933
forks: 8482
language: "TypeScript"
topics: "ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown"
description: "The API to search, scrape, and interact with the web at scale. 🔥"
pushed_at: "2026-07-09T01:49:21Z"
url: "https://github.com/firecrawl/firecrawl"
collected: "2026-07-09"
---

# firecrawl/firecrawl

> The API to search, scrape, and interact with the web at scale. 🔥

**Stars**: 147933 ｜ **Forks**: 8482 ｜ **Language**: TypeScript ｜ **最近活跃**: 2026-07-09T01:49:21Z

## README

<h3 align="center">
  <a name="readme-top"></a>
  <img
    src="https://raw.githubusercontent.com/firecrawl/firecrawl/main/img/firecrawl_logo.png"
    height="200"
  >
</h3>

<div align="center">
  <a href="https://github.com/firecrawl/firecrawl/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/firecrawl/firecrawl" alt="License">
  </a>
  <a href="https://pepy.tech/project/firecrawl-py">
    <img src="https://static.pepy.tech/badge/firecrawl-py" alt="Downloads">
  </a>
  <a href="https://GitHub.com/firecrawl/firecrawl/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/firecrawl/firecrawl.svg" alt="GitHub Contributors">
  </a>
  <a href="https://firecrawl.dev">
    <img src="https://img.shields.io/badge/Visit-firecrawl.dev-orange" alt="Visit firecrawl.dev">
  </a>
</div>

<div>
  <p align="center">
    <a href="https://twitter.com/firecrawl">
      <img src="https://img.shields.io/badge/Follow%20on%20X-000000?style=for-the-badge&logo=x&logoColor=white" alt="Follow on X" />
    </a>
    <a href="https://www.linkedin.com/company/104100957">
      <img src="https://img.shields.io/badge/Follow%20on%20LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Follow on LinkedIn" />
    </a>
    <a href="https://discord.gg/firecrawl">
      <img src="https://img.shields.io/badge/Join%20our%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Join our Discord" />
    </a>
  </p>
</div>

---

# **🔥 Firecrawl**

**The API to search, scrape, and interact with the web at scale. 🔥** The web context API to find sources, extract content, and turn it into clean Markdown or structured data your agents can ship with. Open source and available as a [hosted service](https://firecrawl.dev/?ref=github).

_Pst. Hey, you, join our stargazers :)_

<a href="https://github.com/firecrawl/firecrawl">
  <img src="https://img.shields.io/github/stars/firecrawl/firecrawl.svg?style=social&label=Star&maxAge=2592000" alt="GitHub stars">
</a>

---

## Why Firecrawl?

- **Industry-leading reliability**: Covers 96% of the web, including JS-heavy pages — no proxy headaches, just clean data ([see benchmarks](https://www.firecrawl.dev/blog/the-worlds-best-web-data-api-v25))
- **Blazingly fast**: P95 latency of 3.4s across millions of pages, built for real-time agents and dynamic apps
- **LLM-ready output**: Clean markdown, structured JSON, screenshots, and more — spend fewer tokens, build better AI apps
- **We handle the hard stuff**: Rotating proxies, orchestration, rate limits, JS-blocked content, and more — zero configuration
- **Agent ready**: Connect Firecrawl to any AI agent or MCP client with a single command
- **Media parsing**: Parse and extract content from web-hosted PDFs, DOCX, and more
- **Actions**: Click, scroll, write, wait, and press before extracting content
- **Open source**: Developed transparently and collaboratively — [join our community](https://github.com/firecrawl/firecrawl)

---

## Feature Overview

**Core Endpoints**

| Feature | Description |
|---------|-------------|
| [**Search**](#search) | Search the web and get full page content from results |
| [**Scrape**](#scrape) | Convert any URL to markdown, HTML, screenshots, or structured JSON |
| [**Interact**](#interact) | Scrape a page, then interact with it using AI prompts or code |

**More**

| Feature | Description |
|---------|-------------|
| [**Agent**](#agent) | Automated data gathering, just describe what you need |
| [**Crawl**](#crawl) | Scrape all URLs of a website with a single request |
| [**Map**](#map) | Discover all URLs on a website instantly |
| [**Batch Scrape**](#batch-scrape) | Scrape thousands of URLs asynchronously |

---

## Quick Start

Sign up at [firecrawl.dev](https://firecrawl.dev) to get your API key. Try the [playground](https://firecrawl.dev/playground) to test it out.

### Search

Search the web and get full content from results.

```python
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR_API_KEY")

search_result = app.search("firecrawl", limit=5)
```

<details>
<summary><b>Node.js / cURL / CLI</b></summary>

**Node.js**
```javascript
import { Firecrawl } from 'firecrawl';

const app = new Firecrawl({apiKey: "fc-YOUR_API_KEY"});

app.search("firecrawl", { limit: 5 })
```

**cURL**
```bash
curl -X POST 'https://api.firecrawl.dev/v2/search' \
-H 'Authorization: Bearer fc-YOUR_API_KEY' \
-H 'Content-Type: application/json' \
-d '{
  "query": "firecrawl",
  "limit": 5
}'
```

**CLI**
```bash
firecrawl search "firecrawl" --limit 5
```
</details>

Output:
```json
[
  {
    "url": "https://firecrawl.dev",
    "title": "Firecrawl",
    "markdown": "Turn websites into..."
  },
  {
    "url": "https://docs.firecrawl.dev",
    "title": "Firecrawl Docs",
    "markdown": "# Getting Started..."
  }
]
```

### Scrape

Get LLM-ready data from any website — markdown, JSON, screenshots, and more.

```python
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR_API_KEY")

result = app.scrape('firecrawl.dev')
```

<details>
<summary><b>Node.js / cURL / CLI</b></summary>

**Node.js**
```javascript
import { Firecrawl } from 'firecrawl';

const app = new Firecrawl({ apiKey: "fc-YOUR_API_KEY" });

app.scrape('firecrawl.dev')
```

**cURL**
```bash
curl -X POST 'https://api.firecrawl.dev/v2/scrape' \
-H 'Authorization: Bearer fc-YOUR_API_KEY' \
-H 'Content-Type: application/json' \
-d '{
  "url": "firecrawl.dev"
}'
```

**CLI**
```bash
firecrawl scrape https://firecrawl.dev
firecrawl https://firecrawl.dev --only-main-content
```
</details>

Output:
```
# Firecrawl

Firecrawl helps AI systems search, scrape, and interact with the web.

## Features
- Search: Find information across the web
- Scrape: Clean data from any page
- Interact: Click, navigate, and operate pages
- Agent: Autonomous data gathering
```

### Interact

Scrape a page, then interact with it using AI prompts or code.

```python
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR_API_KEY")

result = app.scrape("https://amazon.com")
scrape_id = result.metadata.scrape_id

app.interact(scrape_id, prompt="Search for 'mechanical keyboard'")
app.interact(scrape_id, prompt="Click the first result")
```

<details>
<summary><b>Node.js / cURL / CLI</b></summary>

**Node.js**
```javascript
import { Firecrawl } from 'firecrawl';

const app = new Firecrawl({apiKey: "fc-YOUR_API_KEY"});

const result = await app.scrape("https://amazon.com");

await app.interact(result.metadata.scrapeId, {
  prompt: "Search for 'mechanical keyboard'"
});
await app.interact(result.metadata.scrapeId, {
  prompt: "Click the first result"
});
```

**cURL**
```bash
# 1. Scrape the page
curl -X POST 'https://api.firecrawl.dev/v2/scrape' \
-H 'Authorization: Bearer fc-YOUR_API_KEY' \
-H 'Content-Type: application/json' \
-d '{"url": "https://amazon.com"}'

# 2. Interact with the page (use scrapeId from step 1)
curl -X POST 'https://api.firecrawl.dev/v2/scrape/SCRAPE_ID/interact' \
-H 'Authorization: Bearer fc-YOUR_API_KEY' \
-H 'Content-Type: application/json' \
-d '{"prompt": "Search for mechanical keyboard"}'
```

**CLI**
```bash
firecrawl scrape https://amazon.com
firecrawl interact exec --prompt "Search for 'mechanical keyboard'"
firecrawl interact exec --prompt "Click the first result"
```
</details>

Output:
```json
{
  "success": true,
  "output": "Keyboard available at $100",
  "liveViewUrl": "https://liveview.firecrawl.dev/..."
}
```

---

## Power Your Agent

Connect Firecrawl to any AI agent or MCP client in minutes.

### Skill

Give your agent easy access to real-time web data with one command.

```bash
npx -y firecrawl-cli@latest init --all --browser
```

Restart your agent after installing. Works with [Claude Code](https://claude.ai/code), [Antigravity](https://antigravity.google), [OpenCode](https://opencode.ai), and more.

### MCP

Connect any MCP-compatible client to the web in seconds.

```json
{
  "mcpServers": {
    "firecrawl-mcp": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "fc-YOUR_API_KEY"
      }
    }
  }
}
```

### Agent Onboarding

Are you an AI agent? Fetch this skill to sign up your user, get an API key, and start building with Firecrawl.

```bash
curl -s https://firecrawl.dev/agent-onboarding/SKILL.md
```

See the [Skill + CLI documentation](https://docs.firecrawl.dev/sdks/cli) for all available commands. For MCP, see [firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server).

---

## More Endpoints

### Agent

**The easiest way to get data from the web.** Describe what you need, and our AI agent searches, navigates, and retrieves it. No URLs required.

Agent is the evolution of our `/extract` endpoint: faster, more reliable, and doesn't require you to know the URLs upfront.
```bash
curl -X POST 'https://api.firecrawl.dev/v2/agent' \
  -H 'Authorization: Bearer fc-YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '
