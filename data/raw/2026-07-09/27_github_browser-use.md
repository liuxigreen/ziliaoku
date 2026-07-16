---
title: "browser-use/browser-use"
author: "browser-use"
platform: github
source: github_api
source_type: github_discovery
source_platform: github
stars: 103767
forks: 11463
language: "Python"
topics: "ai-agents, ai-tools, browser-automation, browser-use, llm, playwright, python"
description: "🌐 Make websites accessible for AI agents. Automate tasks online with ease."
pushed_at: "2026-07-08T18:36:55Z"
url: "https://github.com/browser-use/browser-use"
collected: "2026-07-09"
---

# browser-use/browser-use

> 🌐 Make websites accessible for AI agents. Automate tasks online with ease.

**Stars**: 103767 ｜ **Forks**: 11463 ｜ **Language**: Python ｜ **最近活跃**: 2026-07-08T18:36:55Z

## README

<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/2ccdb752-22fb-41c7-8948-857fc1ad7e24">
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/774a46d5-27a0-490c-b7d0-e65fcbbfa358">
  <img alt="Shows a black Browser Use Logo in light color mode and a white one in dark color mode." src="https://github.com/user-attachments/assets/2ccdb752-22fb-41c7-8948-857fc1ad7e24"  width="full">
</picture>

<div align="center">
    <picture>
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/9955dda9-ede3-4971-8ee0-91cbc3850125">
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/6797d09b-8ac3-4cb9-ba07-b289e080765a">
    <img alt="The AI browser agent." src="https://github.com/user-attachments/assets/9955dda9-ede3-4971-8ee0-91cbc3850125"  width="400">
    </picture>
</div>

<div align="center">
<a href="https://cloud.browser-use.com?utm_source=github&utm_medium=readme-badge-downloads"><img src="https://media.browser-use.tools/badges/package" height="48" alt="Browser-Use Package Download Statistics"></a>
</div>

---

<div align="center">
<a href="#demos"><img src="https://media.browser-use.tools/badges/demos" alt="Demos"></a>
<img width="16" height="1" alt="">
<a href="https://docs.browser-use.com"><img src="https://media.browser-use.tools/badges/docs" alt="Docs"></a>
<img width="16" height="1" alt="">
<a href="https://browser-use.com/posts"><img src="https://media.browser-use.tools/badges/blog" alt="Blog"></a>
<img width="16" height="1" alt="">
<a href="https://browsermerch.com"><img src="https://media.browser-use.tools/badges/merch" alt="Merch"></a>
<img width="100" height="1" alt="">
<a href="https://github.com/browser-use/browser-use"><img src="https://media.browser-use.tools/badges/github" alt="Github Stars"></a>
<img width="4" height="1" alt="">
<a href="https://x.com/intent/user?screen_name=browser_use"><img src="https://media.browser-use.tools/badges/twitter" alt="Twitter"></a>
<img width="4" height="1" alt="">
<a href="https://link.browser-use.com/discord"><img src="https://media.browser-use.tools/badges/discord" alt="Discord"></a>
<img width="4" height="1" alt="">
<a href="https://cloud.browser-use.com?utm_source=github&utm_medium=readme-badge-cloud"><img src="https://media.browser-use.tools/badges/cloud" height="48" alt="Browser-Use Cloud"></a>
</div>

</br>

**[Browser Use CLI 3.0 is here.](#-cli)** Give your coding agent a browser it can use reliably.

🌤️ Want to skip the setup? Use our <b>[cloud](https://cloud.browser-use.com?utm_source=github&utm_medium=readme-skip-setup)</b> for faster, scalable, stealth-enabled browser automation!

🤖 Give our docs to your coding agent: [llms-full.txt](https://docs.browser-use.com/llms-full.txt)

# 👋 Human Quickstart

**1. Install Browser Use (Python>=3.11):**
```bash
uv add browser-use
# or: pip install browser-use
```

**2. [Optional] Get your API key from [Browser Use Cloud](https://cloud.browser-use.com/new-api-key?utm_source=github&utm_medium=readme-quickstart-api-key):**
```
# .env
BROWSER_USE_API_KEY=your-key
# GOOGLE_API_KEY=your-key
# ANTHROPIC_API_KEY=your-key
```

**3. Run your first agent:**

**Python Script:**
```python
import asyncio

from browser_use import Agent, BrowserProfile, ChatBrowserUse

async def main():
    agent = Agent(
        task="Find the number of stars of the browser-use repo",
        llm=ChatBrowserUse(model='openai/gpt-5.5'),
        # llm=ChatBrowserUse(model='bu-2-0'),  # Browser Use's optimized model
        # llm=ChatOpenAI(model='gpt-5.5'),
        # llm=ChatAnthropic(model='claude-opus-4-8'),  # Sonnet also works well.
    )
    history = await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
```

Check out the [library docs](https://docs.browser-use.com/open-source/introduction) and the [cloud docs](https://docs.cloud.browser-use.com?utm_source=github&utm_medium=readme-cloud-docs) for more!

<br/>

# Open Source vs Cloud

<picture>
  <source media="(prefers-color-scheme: light)" srcset="static/accuracy_by_model_light.png">
  <source media="(prefers-color-scheme: dark)" srcset="static/accuracy_by_model_dark.png">
  <img alt="BU Bench V1 - LLM Success Rates" src="static/accuracy_by_model_light.png" width="100%">
</picture>

We benchmark Browser Use across 100 real-world browser tasks. Full benchmark is open source: **[browser-use/benchmark](https://github.com/browser-use/benchmark)**.

**Use the Open-Source Agent**
- You need [custom tools](https://docs.browser-use.com/customize/tools/basics) or deep code-level integration
- We recommend pairing with our [cloud browsers](https://docs.browser-use.com/open-source/customize/browser/remote) for leading stealth, proxy rotation, and scaling
- Or self-host the open-source agent fully on your own machines

**Use the [Fully-Hosted Cloud Agent](https://cloud.browser-use.com?utm_source=github&utm_medium=readme-hosted-agent) (recommended)**
- Much more powerful agent for complex tasks (see plot above)
- Easiest way to start and scale
- Best stealth with proxy rotation and captcha solving
- 1000+ integrations (Gmail, Slack, Notion, and more)
- Persistent filesystem and memory

<br/>

# Demos


### 📋 Form-Filling
#### Task = "Fill in this job application with my resume and information."
![Job Application Demo](https://github.com/user-attachments/assets/57865ee6-6004-49d5-b2c2-6dff39ec2ba9)
[Example code ↗](https://github.com/browser-use/browser-use/blob/main/examples/use-cases/apply_to_job.py)


### 🍎 Grocery-Shopping
#### Task = "Put this list of items into my instacart."

https://github.com/user-attachments/assets/a6813fa7-4a7c-40a6-b4aa-382bf88b1850

[Example code ↗](https://github.com/browser-use/browser-use/blob/main/examples/use-cases/buy_groceries.py)


### 💻 Personal-Assistant.
#### Task = "Help me find parts for a custom PC."

https://github.com/user-attachments/assets/ac34f75c-057a-43ef-ad06-5b2c9d42bf06

[Example code ↗](https://github.com/browser-use/browser-use/blob/main/examples/use-cases/pcpartpicker.py)


<br/>

# 💻 CLI

**Browser Use CLI 3.0** lets your agents do work for you online with our highest accuracy yet. It is powered by [Browser Harness](https://github.com/browser-use/browser-harness), and it applies what we learned about [agent harnesses](https://browser-use.com/posts/bitter-lesson-agent-harnesses) and [agent frameworks](https://browser-use.com/posts/bitter-lesson-agent-frameworks): the latest models do best when you give them freedom, rather than abstracting away complexity. We provide your agents with a direct, dependable surface for acting in the browser.

```bash
browser-use <<'PY'
new_tab("https://example.com")
print(page_info())
PY
```

The CLI allows your agent to control the browser via Python, and it manages the browser in the background.

### Agent Skill

For Claude Code, Codex, and other agents, paste this prompt into your agent:

```text
Install or upgrade browser-use to the latest stable version with uv using Python 3.12, register the skill from `browser-use skill`, and connect it to my browser. Follow https://github.com/browser-use/browser-use if setup or connection fails.
```

<br/>

## Integrations, hosting, custom tools, MCP, and more on our [Docs ↗](https://docs.browser-use.com)

<br/>

# FAQ

<details>
<summary><b>What's the best model to use?</b></summary>

We optimized **ChatBrowserUse()** specifically for browser automation tasks. On avg it completes tasks 3-5x faster than other models with SOTA accuracy.

For pricing and other LLM providers, see our [supported models documentation](https://docs.browser-use.com/supported-models).
</details>

<details>
<summary><b>Can I use Claude / GPT / Gemini through ChatBrowserUse?</b></summary>

Yes. `ChatBrowserUse` accepts provider-prefixed model ids, so a single `BROWSER_USE_API_KEY` reaches all of them — no separate OpenAI/Anthropic/Google keys required:

```python
from browser_use import Agent, ChatBrowserUse

llm = ChatBrowserUse(model='anthropic/claude-sonnet-4-6')  # or 'openai/gpt-5.5', 'google/gemini-3-pro'
agent = Agent(task='...', llm=llm)
```

For the best speed and cost we still recommend the default `bu-*` models.
</details>

<details>
<summary><b>Should I use the Browser Use system prompt with the open-source preview model?</b></summary>

Yes. If you use `ChatBrowserUse(model='browser-use/bu-30b-a3b-preview')` with a normal `Agent(...)`, Browser Use still sends its default agent system prompt for you.

You do **not** need to add a separate custom "Browser Use system message" just because you switched to the open-source preview model. Only use `extend_system_message` or `override_system_message` when you intentionally want to customize the default behavior for your task.

If you want the best default speed/accuracy, we still recommend the newer hosted `bu-*` models. If you want the open-source preview mod
