[Skip to content](https://github.com/darkzOGx/youtube-automation-agent#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/darkzOGx/youtube-automation-agent) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/darkzOGx/youtube-automation-agent) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/darkzOGx/youtube-automation-agent) to refresh your session.Dismiss alert

{{ message }}

[darkzOGx](https://github.com/darkzOGx)/ **[youtube-automation-agent](https://github.com/darkzOGx/youtube-automation-agent)** Public

- [Notifications](https://github.com/login?return_to=%2FdarkzOGx%2Fyoutube-automation-agent) You must be signed in to change notification settings
- [Fork\\
382](https://github.com/login?return_to=%2FdarkzOGx%2Fyoutube-automation-agent)
- [Star\\
1.5k](https://github.com/login?return_to=%2FdarkzOGx%2Fyoutube-automation-agent)


master

[**1** Branch](https://github.com/darkzOGx/youtube-automation-agent/branches) [**0** Tags](https://github.com/darkzOGx/youtube-automation-agent/tags)

[Go to Branches page](https://github.com/darkzOGx/youtube-automation-agent/branches)[Go to Tags page](https://github.com/darkzOGx/youtube-automation-agent/tags)

Go to file

Code

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| ## Latest commit<br>[![darkzOGx](https://avatars.githubusercontent.com/u/128010917?v=4&size=40)](https://github.com/darkzOGx)[darkzOGx](https://github.com/darkzOGx/youtube-automation-agent/commits?author=darkzOGx)<br>[Update builder information in README](https://github.com/darkzOGx/youtube-automation-agent/commit/f5cf4f159915cd7e725e8badcb06b5a8a5a73606)<br>Open commit detailssuccess<br>3 days agoJul 4, 2026<br>[f5cf4f1](https://github.com/darkzOGx/youtube-automation-agent/commit/f5cf4f159915cd7e725e8badcb06b5a8a5a73606) · 3 days agoJul 4, 2026<br>## History<br>[8 Commits](https://github.com/darkzOGx/youtube-automation-agent/commits/master/) <br>Open commit details<br>[View commit history for this file.](https://github.com/darkzOGx/youtube-automation-agent/commits/master/) 8 Commits |
| [.github/workflows](https://github.com/darkzOGx/youtube-automation-agent/tree/master/.github/workflows "This path skips through empty directories") | [.github/workflows](https://github.com/darkzOGx/youtube-automation-agent/tree/master/.github/workflows "This path skips through empty directories") | [v2.1: Wire in real AI generation, fix startup/scheduler crashes, secu…](https://github.com/darkzOGx/youtube-automation-agent/commit/003104ec58e3458feff0994dc4a17a8b044648b2 "v2.1: Wire in real AI generation, fix startup/scheduler crashes, secure the API  - Wire AITextService (previously dead code) into strategy, script, and SEO   agents: AI-first generation with template fallback when no provider key - Fix startup crash: add missing sharp dependency, drop unused jimp - Create missing automation_events table; every scheduled task threw on logging - Fix double-insert PK violation in generateContent; saveProductionData now   upserts and returns the id - Publishing: stream the real video file and refuse to upload placeholders;   fix publish-queue removal; default privacy public -> private - API: optional x-api-key auth on mutating routes, request validation,   1mb body limit; remove unused JWT_SECRET - Remove fabricated statistics from script templates - Fix analytics dislikeCount (removed from YouTube API) and NaN guards - Delete dead auth flows (authenticate.js stub, simple-auth.js OOB flow),   dead deps (cron), broken npm scripts (workflow:*, db:init) - Stop tracking generated data/ artifacts; ignore output dirs - Add ESLint (flat config, 0 errors) and GitHub Actions CI (lint + test) - Fix env vars being set to the string \"undefined\"; clear health-check   interval on stop; document ffmpeg prerequisite  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>") | last weekJul 2, 2026 |
| [agents](https://github.com/darkzOGx/youtube-automation-agent/tree/master/agents "agents") | [agents](https://github.com/darkzOGx/youtube-automation-agent/tree/master/agents "agents") | [v2.1: Wire in real AI generation, fix startup/scheduler crashes, secu…](https://github.com/darkzOGx/youtube-automation-agent/commit/003104ec58e3458feff0994dc4a17a8b044648b2 "v2.1: Wire in real AI generation, fix startup/scheduler crashes, secure the API  - Wire AITextService (previously dead code) into strategy, script, and SEO   agents: AI-first generation with template fallback when no provider key - Fix startup crash: add missing sharp dependency, drop unused jimp - Create missing automation_events table; every scheduled task threw on logging - Fix double-insert PK violation in generateContent; saveProductionData now   upserts and returns the id - Publishing: stream the real video file and refuse to upload placeholders;   fix publish-queue removal; default privacy public -> private - API: optional x-api-key auth on mutating routes, request validation,   1mb body limit; remove unused JWT_SECRET - Remove fabricated statistics from script templates - Fix analytics dislikeCount (removed from YouTube API) and NaN guards - Delete dead auth flows (authenticate.js stub, simple-auth.js OOB flow),   dead deps (cron), broken npm scripts (workflow:*, db:init) - Stop tracking generated data/ artifacts; ignore output dirs - Add ESLint (flat config, 0 errors) and GitHub Actions CI (lint + test) - Fix env vars being set to the string \"undefined\"; clear health-check   interval on stop; document ffmpeg prerequisite  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>") | last weekJul 2, 2026 |
| [config](https://github.com/darkzOGx/youtube-automation-agent/tree/master/config "config") | [config](https://github.com/darkzOGx/youtube-automation-agent/tree/master/config "config") | [v2.0: Update all AI models to current (June 2026) and rewrite README](https://github.com/darkzOGx/youtube-automation-agent/commit/c9864b947b6ac8193b46a241fc11d5ea0e0d2007 "v2.0: Update all AI models to current (June 2026) and rewrite README  - OpenAI: GPT-5.5/Instant, GPT Image 2, gpt-4o-mini-tts (SDK v4 -> v6) - Google: Gemini 3.5 Flash/Pro (@google/genai v2.9) - ElevenLabs: Eleven v3 - Replicate: Wan 2.7 I2V replaces Stable Video Diffusion - Fix deprecated OpenAI v3 SDK patterns in credential testing - Dynamic year in content strategy agent - Revamped setup wizard with TTS service picker - Developer-focused README with Mermaid diagrams  Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>") | 3 weeks agoJun 20, 2026 |
| [dashboard](https://github.com/darkzOGx/youtube-automation-agent/tree/master/dashboard "dashboard") | [dashboard](https://github.com/darkzOGx/youtube-automation-agent/tree/master/dashboard "dashboard") | [Initial commit: YouTube Automation Agent](https://github.com/darkzOGx/youtube-automation-agent/commit/3ea1b524c0a729a7ebd49f3f64ad11fed626222a "Initial commit: YouTube Automation Agent  Complete automated YouTube channel management system with: - 7 specialized AI agents for content creation - Support for OpenAI and Google Gemini (FREE option) - 24/7 automation capabilities - Dashboard for monitoring and control - No coding required - setup wizard included  All API keys and credentials have been removed for security. Users need to add their own credentials using the provided templates.  🤖 Generated with [Claude Code](https://claude.ai/code)  Co-Authored-By: Claude <noreply@anthropic.com>") | 11 months agoAug 14, 2025 |
| [database](https://github.com/darkzOGx/youtube-automation-agent/tree/master/database "database") | [database](https://github.com/darkzOGx/youtube-automation-agent/tree/master/database "database") | [v2.1: Wire in real AI generation, fix startup/scheduler crashes, secu…](https://github.com/darkzOGx/youtube-automation-agent/commit/003104ec58e3458feff0994dc4a17a8b044648b2 "v2.1: Wire in real AI generation, fix startup/scheduler crashes, secure the API  - Wire AITextService (previously dead code) into strategy, script, and SEO   agents: AI-first generation with template fallback when no provider key - Fix startup crash: add missing sharp dependency, drop unused jimp - Create missing automation_events table; every scheduled task threw on logging - Fix double-insert PK violation in generateContent; saveProductionData now   upserts and returns the id - Publishing: stream the real video file and refuse to upload placeholders;   fix publish-queue removal; default privacy public -> private - API: optional x-api-key auth on mutating routes, request validation,   1mb body limit; remove unused JWT_SECRET - Remove fabricated statistics from script templates - Fix analytics dislikeCount (removed from YouTube API) and NaN guards - Delete dead auth flows (authenticate.js stub, simple-auth.js OOB flow),   dead deps (cron), broken npm scripts (workflow:*, db:init) - Stop tracking generated data/ artifacts; ignore output dirs - Add ESLint (flat config, 0 errors) and GitHub Actions CI (lint + test) - Fix env vars being set to the string \"undefined\"; clear health-check   interval on stop; document ffmpeg prerequisite  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>") | last weekJul 2, 2026 |
| [mcp](https://github.com/darkzOGx/youtube-automation-agent/tree/master/mcp "mcp") | [mcp](https://github.com/darkzOGx/youtube-automation-agent/tree/master/mcp "mcp") | [Initial commit: YouTube Automation Agent](https://github.com/darkzOGx/youtube-automation-agent/commit/3ea1b524c0a729a7ebd49f3f64ad11fed626222a "Initial commit: YouTube Automation Agent  Complete automated YouTube channel management system with: - 7 specialized AI agents for content creation - Support for OpenAI and Google Gemini (FREE option) - 24/7 automation capabilities - Dashboard for monitoring and control - No coding required - setup wizard included  All API keys and credentials have been removed for security. Users need to add their own credentials using the provided templates.  🤖 Generated with [Claude Code](https://claude.ai/code)  Co-Authored-By: Claude <noreply@anthropic.com>") | 11 months agoAug 14, 2025 |
| [schedules](https://github.com/darkzOGx/youtube-automation-agent/tree/master/schedules "schedules") | [schedules](https://github.com/darkzOGx/youtube-automation-agent/tree/master/schedules "schedules") | [v2.1: Wire in real AI generation, fix startup/scheduler crashes, secu…](https://github.com/darkzOGx/youtube-automation-agent/commit/003104ec58e3458feff0994dc4a17a8b044648b2 "v2.1: Wire in real AI generation, fix startup/scheduler crashes, secure the API  - Wire AITextService (previously dead code) into strategy, script, and SEO   agents: AI-first generation with template fallback when no provider key - Fix startup crash: add missing sharp dependency, drop unused jimp - Create missing automation_events table; every scheduled task threw on logging - Fix double-insert PK violation in generateContent; saveProductionData now   upserts and returns the id - Publishing: stream the real video file and refuse to upload placeholders;   fix publish-queue removal; default privacy public -> private - API: optional x-api-key auth on mutating routes, request validation,   1mb body limit; remove unused JWT_SECRET - Remove fabricated statistics from script templates - Fix analytics dislikeCount (removed from YouTube API) and NaN guards - Delete dead auth flows (authenticate.js stub, simple-auth.js OOB flow),   dead deps (cron), broken npm scripts (workflow:*, db:init) - Stop tracking generated data/ artifacts; ignore output dirs - Add ESLint (flat config, 0 errors) and GitHub Actions CI (lint + test) - Fix env vars being set to the string \"undefined\"; clear health-check   interval on stop; document ffmpeg prerequisite  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>") | last weekJul 2, 2026 |
| [utils](https://github.com/darkzOGx/youtube-automation-agent/tree/master/utils "utils") | [utils](https://github.com/darkzOGx/youtube-automation-agent/tree/master/utils "utils") | [v2.1: Wire in real AI generation, fix startup/scheduler crashes, secu…](https://github.com/darkzOGx/youtube-automation-agent/commit/003104ec58e3458feff0994dc4a17a8b044648b2 "v2.1: Wire in real AI generation, fix startup/scheduler crashes, secure the API  - Wire AITextService (previously dead code) into strategy, script, and SEO   agents: AI-first generation with template fallback when no provider key - Fix startup crash: add missing sharp dependency, drop unused jimp - Create missing automation_events table; every scheduled task threw on logging - Fix double-insert PK violation in generateContent; saveProductionData now   upserts and returns the id - Publishing: stream the real video file and refuse to upload placeholders;   fix publish-queue removal; default privacy public -> private - API: optional x-api-key auth on mutating routes, request validation,   1mb body limit; remove unused JWT_SECRET - Remove fabricated statistics from script templates - Fix analytics dislikeCount (removed from YouTube API) and NaN guards - Delete dead auth flows (authenticate.js stub, simple-auth.js OOB flow),   dead deps (cron), broken npm scripts (workflow:*, db:init) - Stop tracking generated data/ artifacts; ignore output dirs - Add ESLint (flat config, 0 errors) and GitHub Actions CI (lint + test) - Fix env vars being set to the string \"undefined\"; clear health-check   interval on stop; document ffmpeg prerequisite  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>") | last weekJul 2, 2026 |
| [.env.example](https://github.com/darkzOGx/youtube-automation-agent/blob/master/.env.example ".env.example") | [.env.example](https://github.com/darkzOGx/youtube-automation-agent/blob/master/.env.example ".env.example") | [v2.1: Wire in real AI generation, fix startup/scheduler crashes, secu…](https://github.com/darkzOGx/youtube-automation-agent/commit/003104ec58e3458feff0994dc4a17a8b044648b2 "v2.1: Wire in real AI generation, fix startup/scheduler crashes, secure the API  - Wire AITextService (previously dead code) into strategy, script, and SEO   agents: AI-first generation with template fallback when no provider key - Fix startup crash: add missing sharp dependency, drop unused jimp - Create missing automation_events table; every scheduled task threw on logging - Fix double-insert PK violation in generateContent; saveProductionData now   upserts and returns the id - Publishing: stream the real video file and refuse to upload placeholders;   fix publish-queue removal; default privacy public -> private - API: optional x-api-key auth on mutating routes, request validation,   1mb body limit; remove unused JWT_SECRET - Remove fabricated statistics from script templates - Fix analytics dislikeCount (removed from YouTube API) and NaN guards - Delete dead auth flows (authenticate.js stub, simple-auth.js OOB flow),   dead deps (cron), broken npm scripts (workflow:*, db:init) - Stop tracking generated data/ artifacts; ignore output dirs - Add ESLint (flat config, 0 errors) and GitHub Actions CI (lint + test) - Fix env vars being set to the string \"undefined\"; clear health-check   interval on stop; document ffmpeg prerequisite  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>") | last weekJul 2, 2026 |
| [.gitignore](https://github.com/darkzOGx/youtube-automation-agent/blob/master/.gitignore ".gitignore") | [.gitignore](https://github.com/darkzOGx/youtube-automation-agent/blob/master/.gitignore ".gitignore") | [v2.1: Wire in real AI generation, fix startup/scheduler crashes, secu…](https://github.com/darkzOGx/youtube-automation-agent/commit/003104ec58e3458feff0994dc4a17a8b044648b2 "v2.1: Wire in real AI generation, fix startup/scheduler crashes, secure the API  - Wire AITextService (previously dead code) into strategy, script, and SEO   agents: AI-first generation with template fallback when no provider key - Fix startup crash: add missing sharp dependency, drop unused jimp - Create missing automation_events table; every scheduled task threw on logging - Fix double-insert PK violation in generateContent; saveProductionData now   upserts and returns the id - Publishing: stream the real video file and refuse to upload placeholders;   fix publish-queue removal; default privacy public -> private - API: optional x-api-key auth on mutating routes, request validation,   1mb body limit; remove unused JWT_SECRET - Remove fabricated statistics from script templates - Fix analytics dislikeCount (removed from YouTube API) and NaN guards - Delete dead auth flows (authenticate.js stub, simple-auth.js OOB flow),   dead deps (cron), broken npm scripts (workflow:*, db:init) - Stop tracking generated data/ artifacts; ignore output dirs - Add ESLint (flat config, 0 errors) and GitHub Actions CI (lint + test) - Fix env vars being set to the string \"undefined\"; clear health-check   interval on stop; document ffmpeg prerequisite  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>") | last weekJul 2, 2026 |
| [LICENSE](https://github.com/darkzOGx/youtube-automation-agent/blob/master/LICENSE "LICENSE") | [LICENSE](https://github.com/darkzOGx/youtube-automation-agent/blob/master/LICENSE "LICENSE") | [Initial commit: YouTube Automation Agent](https://github.com/darkzOGx/youtube-automation-agent/commit/3ea1b524c0a729a7ebd49f3f64ad11fed626222a "Initial commit: YouTube Automation Agent  Complete automated YouTube channel management system with: - 7 specialized AI agents for content creation - Support for OpenAI and Google Gemini (FREE option) - 24/7 automation capabilities - Dashboard for monitoring and control - No coding required - setup wizard included  All API keys and credentials have been removed for security. Users need to add their own credentials using the provided templates.  🤖 Generated with [Claude Code](https://claude.ai/code)  Co-Authored-By: Claude <noreply@anthropic.com>") | 11 months agoAug 14, 2025 |
| [README.md](https://github.com/darkzOGx/youtube-automation-agent/blob/master/README.md "README.md") | [README.md](https://github.com/darkzOGx/youtube-automation-agent/blob/master/README.md "README.md") | [Update builder information in README](https://github.com/darkzOGx/youtube-automation-agent/commit/f5cf4f159915cd7e725e8badcb06b5a8a5a73606 "Update builder information in README  Removed reference to ConstructionBids.ai from the README.") | 3 days agoJul 4, 2026 |
| [eslint.config.js](https://github.com/darkzOGx/youtube-automation-agent/blob/master/eslint.config.js "eslint.config.js") | [eslint.config.js](https://github.com/darkzOGx/youtube-automation-agent/blob/master/eslint.config.js "eslint.config.js") | [v2.1: Wire in real AI generation, fix startup/scheduler crashes, secu…](https://github.com/darkzOGx/youtube-automation-agent/commit/003104ec58e3458feff0994dc4a17a8b044648b2 "v2.1: Wire in real AI generation, fix startup/scheduler crashes, secure the API  - Wire AITextService (previously dead code) into strategy, script, and SEO   agents: AI-first generation with template fallback when no provider key - Fix startup crash: add missing sharp dependency, drop unused jimp - Create missing automation_events table; every scheduled task threw on logging - Fix double-insert PK violation in generateContent; saveProductionData now   upserts and returns the id - Publishing: stream the real video file and refuse to upload placeholders;   fix publish-queue removal; default privacy public -> private - API: optional x-api-key auth on mutating routes, request validation,   1mb body limit; remove unused JWT_SECRET - Remove fabricated statistics from script templates - Fix analytics dislikeCount (removed from YouTube API) and NaN guards - Delete dead auth flows (authenticate.js stub, simple-auth.js OOB flow),   dead deps (cron), broken npm scripts (workflow:*, db:init) - Stop tracking generated data/ artifacts; ignore output dirs - Add ESLint (flat config, 0 errors) and GitHub Actions CI (lint + test) - Fix env vars being set to the string \"undefined\"; clear health-check   interval on stop; document ffmpeg prerequisite  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>") | last weekJul 2, 2026 |
| [index.js](https://github.com/darkzOGx/youtube-automation-agent/blob/master/index.js "index.js") | [index.js](https://github.com/darkzOGx/youtube-automation-agent/blob/master/index.js "index.js") | [v2.1: Wire in real AI generation, fix startup/scheduler crashes, secu…](https://github.com/darkzOGx/youtube-automation-agent/commit/003104ec58e3458feff0994dc4a17a8b044648b2 "v2.1: Wire in real AI generation, fix startup/scheduler crashes, secure the API  - Wire AITextService (previously dead code) into strategy, script, and SEO   agents: AI-first generation with template fallback when no provider key - Fix startup crash: add missing sharp dependency, drop unused jimp - Create missing automation_events table; every scheduled task threw on logging - Fix double-insert PK violation in generateContent; saveProductionData now   upserts and returns the id - Publishing: stream the real video file and refuse to upload placeholders;   fix publish-queue removal; default privacy public -> private - API: optional x-api-key auth on mutating routes, request validation,   1mb body limit; remove unused JWT_SECRET - Remove fabricated statistics from script templates - Fix analytics dislikeCount (removed from YouTube API) and NaN guards - Delete dead auth flows (authenticate.js stub, simple-auth.js OOB flow),   dead deps (cron), broken npm scripts (workflow:*, db:init) - Stop tracking generated data/ artifacts; ignore output dirs - Add ESLint (flat config, 0 errors) and GitHub Actions CI (lint + test) - Fix env vars being set to the string \"undefined\"; clear health-check   interval on stop; document ffmpeg prerequisite  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>") | last weekJul 2, 2026 |
| [modern-auth.js](https://github.com/darkzOGx/youtube-automation-agent/blob/master/modern-auth.js "modern-auth.js") | [modern-auth.js](https://github.com/darkzOGx/youtube-automation-agent/blob/master/modern-auth.js "modern-auth.js") | [Initial commit: YouTube Automation Agent](https://github.com/darkzOGx/youtube-automation-agent/commit/3ea1b524c0a729a7ebd49f3f64ad11fed626222a "Initial commit: YouTube Automation Agent  Complete automated YouTube channel management system with: - 7 specialized AI agents for content creation - Support for OpenAI and Google Gemini (FREE option) - 24/7 automation capabilities - Dashboard for monitoring and control - No coding required - setup wizard included  All API keys and credentials have been removed for security. Users need to add their own credentials using the provided templates.  🤖 Generated with [Claude Code](https://claude.ai/code)  Co-Authored-By: Claude <noreply@anthropic.com>") | 11 months agoAug 14, 2025 |
| [oauth-server.js](https://github.com/darkzOGx/youtube-automation-agent/blob/master/oauth-server.js "oauth-server.js") | [oauth-server.js](https://github.com/darkzOGx/youtube-automation-agent/blob/master/oauth-server.js "oauth-server.js") | [Initial commit: YouTube Automation Agent](https://github.com/darkzOGx/youtube-automation-agent/commit/3ea1b524c0a729a7ebd49f3f64ad11fed626222a "Initial commit: YouTube Automation Agent  Complete automated YouTube channel management system with: - 7 specialized AI agents for content creation - Support for OpenAI and Google Gemini (FREE option) - 24/7 automation capabilities - Dashboard for monitoring and control - No coding required - setup wizard included  All API keys and credentials have been removed for security. Users need to add their own credentials using the provided templates.  🤖 Generated with [Claude Code](https://claude.ai/code)  Co-Authored-By: Claude <noreply@anthropic.com>") | 11 months agoAug 14, 2025 |
| [package-lock.json](https://github.com/darkzOGx/youtube-automation-agent/blob/master/package-lock.json "package-lock.json") | [package-lock.json](https://github.com/darkzOGx/youtube-automation-agent/blob/master/package-lock.json "package-lock.json") | [v2.1: Wire in real AI generation, fix startup/scheduler crashes, secu…](https://github.com/darkzOGx/youtube-automation-agent/commit/003104ec58e3458feff0994dc4a17a8b044648b2 "v2.1: Wire in real AI generation, fix startup/scheduler crashes, secure the API  - Wire AITextService (previously dead code) into strategy, script, and SEO   agents: AI-first generation with template fallback when no provider key - Fix startup crash: add missing sharp dependency, drop unused jimp - Create missing automation_events table; every scheduled task threw on logging - Fix double-insert PK violation in generateContent; saveProductionData now   upserts and returns the id - Publishing: stream the real video file and refuse to upload placeholders;   fix publish-queue removal; default privacy public -> private - API: optional x-api-key auth on mutating routes, request validation,   1mb body limit; remove unused JWT_SECRET - Remove fabricated statistics from script templates - Fix analytics dislikeCount (removed from YouTube API) and NaN guards - Delete dead auth flows (authenticate.js stub, simple-auth.js OOB flow),   dead deps (cron), broken npm scripts (workflow:*, db:init) - Stop tracking generated data/ artifacts; ignore output dirs - Add ESLint (flat config, 0 errors) and GitHub Actions CI (lint + test) - Fix env vars being set to the string \"undefined\"; clear health-check   interval on stop; document ffmpeg prerequisite  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>") | last weekJul 2, 2026 |
| [package.json](https://github.com/darkzOGx/youtube-automation-agent/blob/master/package.json "package.json") | [package.json](https://github.com/darkzOGx/youtube-automation-agent/blob/master/package.json "package.json") | [v2.1: Wire in real AI generation, fix startup/scheduler crashes, secu…](https://github.com/darkzOGx/youtube-automation-agent/commit/003104ec58e3458feff0994dc4a17a8b044648b2 "v2.1: Wire in real AI generation, fix startup/scheduler crashes, secure the API  - Wire AITextService (previously dead code) into strategy, script, and SEO   agents: AI-first generation with template fallback when no provider key - Fix startup crash: add missing sharp dependency, drop unused jimp - Create missing automation_events table; every scheduled task threw on logging - Fix double-insert PK violation in generateContent; saveProductionData now   upserts and returns the id - Publishing: stream the real video file and refuse to upload placeholders;   fix publish-queue removal; default privacy public -> private - API: optional x-api-key auth on mutating routes, request validation,   1mb body limit; remove unused JWT_SECRET - Remove fabricated statistics from script templates - Fix analytics dislikeCount (removed from YouTube API) and NaN guards - Delete dead auth flows (authenticate.js stub, simple-auth.js OOB flow),   dead deps (cron), broken npm scripts (workflow:*, db:init) - Stop tracking generated data/ artifacts; ignore output dirs - Add ESLint (flat config, 0 errors) and GitHub Actions CI (lint + test) - Fix env vars being set to the string \"undefined\"; clear health-check   interval on stop; document ffmpeg prerequisite  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>") | last weekJul 2, 2026 |
| [setup.js](https://github.com/darkzOGx/youtube-automation-agent/blob/master/setup.js "setup.js") | [setup.js](https://github.com/darkzOGx/youtube-automation-agent/blob/master/setup.js "setup.js") | [v2.1: Wire in real AI generation, fix startup/scheduler crashes, secu…](https://github.com/darkzOGx/youtube-automation-agent/commit/003104ec58e3458feff0994dc4a17a8b044648b2 "v2.1: Wire in real AI generation, fix startup/scheduler crashes, secure the API  - Wire AITextService (previously dead code) into strategy, script, and SEO   agents: AI-first generation with template fallback when no provider key - Fix startup crash: add missing sharp dependency, drop unused jimp - Create missing automation_events table; every scheduled task threw on logging - Fix double-insert PK violation in generateContent; saveProductionData now   upserts and returns the id - Publishing: stream the real video file and refuse to upload placeholders;   fix publish-queue removal; default privacy public -> private - API: optional x-api-key auth on mutating routes, request validation,   1mb body limit; remove unused JWT_SECRET - Remove fabricated statistics from script templates - Fix analytics dislikeCount (removed from YouTube API) and NaN guards - Delete dead auth flows (authenticate.js stub, simple-auth.js OOB flow),   dead deps (cron), broken npm scripts (workflow:*, db:init) - Stop tracking generated data/ artifacts; ignore output dirs - Add ESLint (flat config, 0 errors) and GitHub Actions CI (lint + test) - Fix env vars being set to the string \"undefined\"; clear health-check   interval on stop; document ffmpeg prerequisite  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>") | last weekJul 2, 2026 |
| [test.js](https://github.com/darkzOGx/youtube-automation-agent/blob/master/test.js "test.js") | [test.js](https://github.com/darkzOGx/youtube-automation-agent/blob/master/test.js "test.js") | [v2.1: Wire in real AI generation, fix startup/scheduler crashes, secu…](https://github.com/darkzOGx/youtube-automation-agent/commit/003104ec58e3458feff0994dc4a17a8b044648b2 "v2.1: Wire in real AI generation, fix startup/scheduler crashes, secure the API  - Wire AITextService (previously dead code) into strategy, script, and SEO   agents: AI-first generation with template fallback when no provider key - Fix startup crash: add missing sharp dependency, drop unused jimp - Create missing automation_events table; every scheduled task threw on logging - Fix double-insert PK violation in generateContent; saveProductionData now   upserts and returns the id - Publishing: stream the real video file and refuse to upload placeholders;   fix publish-queue removal; default privacy public -> private - API: optional x-api-key auth on mutating routes, request validation,   1mb body limit; remove unused JWT_SECRET - Remove fabricated statistics from script templates - Fix analytics dislikeCount (removed from YouTube API) and NaN guards - Delete dead auth flows (authenticate.js stub, simple-auth.js OOB flow),   dead deps (cron), broken npm scripts (workflow:*, db:init) - Stop tracking generated data/ artifacts; ignore output dirs - Add ESLint (flat config, 0 errors) and GitHub Actions CI (lint + test) - Fix env vars being set to the string \"undefined\"; clear health-check   interval on stop; document ffmpeg prerequisite  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>") | last weekJul 2, 2026 |
| View all files |

## Repository files navigation

# YouTube Automation Agent

[Permalink: YouTube Automation Agent](https://github.com/darkzOGx/youtube-automation-agent#youtube-automation-agent)

## What's New in v2.1

[Permalink: What's New in v2.1](https://github.com/darkzOGx/youtube-automation-agent#whats-new-in-v21)

- **Real AI generation wired in** — the Content Strategy, Script Writer, and SEO agents now call your configured AI provider (OpenAI, OpenRouter, Kimi, MiMo, GLM, or Gemini) for topics, scripts, titles, descriptions, and tags. If no provider key is set, they fall back to the built-in templates so the pipeline still runs.
- **API protection** — set `API_KEY` in `.env` and the mutating endpoints (`POST /generate`, `POST /publish/:id`) require a matching `x-api-key` header. Request bodies are validated and size-limited.
- **Safer publishing** — default privacy is now `private` (set `DEFAULT_PRIVACY_STATUS=public` to opt in), and the uploader streams the real video file — it refuses to upload placeholder assets from simulated runs.
- **Startup and scheduler fixes** — added the missing `sharp` dependency (the app previously crashed on boot), created the missing `automation_events` table (every scheduled task previously threw on logging), fixed the double-insert in the content pipeline, and fixed the publish-queue removal.
- **No more fabricated statistics** — template scripts no longer invent numbers like "90% of people…".
- **Cleaner repo** — removed two dead OAuth flows (`authenticate.js`, `simple-auth.js` used Google's long-deprecated OOB flow), dead dependencies (`cron`, `jimp`), broken npm scripts, and committed build artifacts. Added ESLint (`npm run lint`) and GitHub Actions CI.

## What's New in v2.0

[Permalink: What's New in v2.0](https://github.com/darkzOGx/youtube-automation-agent#whats-new-in-v20)

- **Model upgrades across the board** — GPT-5.5 / GPT-5.5 Instant replace GPT-4-turbo, GPT Image 2 replaces DALL-E 3, Gemini 3.5 Flash/Pro replace Gemini 1.x, ElevenLabs Eleven v3 replaces v1, Wan 2.7 replaces Stable Video Diffusion
- **OpenAI SDK v6** — upgraded from v4, along with `@google/genai` v2.9, `replicate` v1.4, `googleapis` v173
- **Revamped setup wizard** — new TTS service picker (OpenAI TTS / ElevenLabs / Azure), ElevenLabs credential setup, updated model selection menus
- **Fixed deprecated API patterns** — OpenAI v3 SDK calls in credential testing replaced with v4+ patterns
- **Dynamic year in content strategy** — no more hardcoded "2025" in trend analysis prompts
- **README rewrite** — developer-focused docs with Mermaid architecture diagrams, no fluff

* * *

Fully automated YouTube channel management system. AI agents handle content strategy, scriptwriting, thumbnail generation, SEO, publishing, and analytics — end to end, on a daily schedule.

## Built by

[Permalink: Built by](https://github.com/darkzOGx/youtube-automation-agent#built-by)

[@darkzOGx](https://github.com/darkzOGx). Solo builder shipping AI automation and developer tools.

Find me on [X](https://x.com/darkzOGx) and [laderalabs.io](https://laderalabs.io/).

If this saves you time, a star helps it reach more developers.

## Architecture

[Permalink: Architecture](https://github.com/darkzOGx/youtube-automation-agent#architecture)

Render

feedback loop

Content Strategy Agent

Script Writer Agent

Thumbnail Designer Agent

SEO Optimizer Agent

Production Management Agent

Publishing & Scheduling Agent

Analytics & Optimization Agent

Loading

```
graph TD
    A[Content Strategy Agent] --> B[Script Writer Agent]
    B --> C[Thumbnail Designer Agent]
    B --> D[SEO Optimizer Agent]
    C --> E[Production Management Agent]
    D --> E
    E --> F[Publishing & Scheduling Agent]
    F --> G[Analytics & Optimization Agent]
    G -->|feedback loop| A
```

## How It Works

[Permalink: How It Works](https://github.com/darkzOGx/youtube-automation-agent#how-it-works)

Each agent handles one stage of the pipeline:

| Agent | Role |
| --- | --- |
| **Content Strategy** | Analyzes YouTube trends, identifies topics, plans content calendar |
| **Script Writer** | Generates scripts with hooks, storytelling, CTAs |
| **Thumbnail Designer** | Creates thumbnails, runs A/B variations |
| **SEO Optimizer** | Keywords, titles, descriptions, tags |
| **Production** | Coordinates TTS audio, image assets, video assembly |
| **Publishing** | Uploads, schedules, manages playlists |
| **Analytics** | Tracks performance, feeds insights back to strategy |

## AI Providers

[Permalink: AI Providers](https://github.com/darkzOGx/youtube-automation-agent#ai-providers)

All OpenAI-compatible providers work out of the box — the system auto-configures the SDK base URL. Pick one, or use OpenRouter to access everything through a single key.

Render

Router

OpenRouter

300+ models

Direct

OpenAI

GPT-5.5

Gemini

3.5 Flash/Pro

Kimi

K2.6

MiMo

V2.5 Pro

GLM

GLM-5

YouTube Automation Agent

Loading

```
graph LR
    subgraph Direct
        OA[OpenAI<br/>GPT-5.5]
        GM[Gemini<br/>3.5 Flash/Pro]
        KM[Kimi<br/>K2.6]
        MM[MiMo<br/>V2.5 Pro]
        GL[GLM<br/>GLM-5]
    end
    subgraph Router
        OR[OpenRouter<br/>300+ models]
    end
    Direct --> YAA[YouTube Automation Agent]
    Router --> YAA
```

| Provider | Models | Base URL | Cost |
| --- | --- | --- | --- |
| **OpenAI** | GPT-5.5, GPT-5.5 Instant | `api.openai.com/v1` | ~$0.05–0.20/video |
| **OpenRouter** | 300+ (GPT, Claude, Gemini, Kimi, GLM, etc.) | `openrouter.ai/api/v1` | varies by model |
| **Google Gemini** | Gemini 3.5 Flash, 3.5 Pro | via `@google/genai` SDK | free tier available |
| **Kimi (Moonshot AI)** | Kimi K2.6, K2.5 | `api.moonshot.ai/v1` | ~80% cheaper than GPT-5.5 |
| **MiMo (Xiaomi)** | MiMo V2.5 Pro, V2.5 | `api.xiaomimimo.com/v1` | competitive |
| **GLM (Zhipu AI)** | GLM-5, GLM-5.1 | `api.z.ai/api/paas/v4/` | ~$1/M input tokens |

Additional integrations: Anthropic Claude (`claude-opus-4-8`), ElevenLabs (Eleven v3 TTS), Replicate (Wan 2.7 video), local models via Ollama, any OpenAI-compatible endpoint.

## Quick Start

[Permalink: Quick Start](https://github.com/darkzOGx/youtube-automation-agent#quick-start)

```
git clone https://github.com/darkzOGx/youtube-automation-agent.git
cd youtube-automation-agent
npm install
cp .env.example .env
cp config/credentials.example.json config/credentials.json
npm run setup   # interactive credential wizard
npm start
```

Dashboard runs at `http://localhost:3456`.

### Prerequisites

[Permalink: Prerequisites](https://github.com/darkzOGx/youtube-automation-agent#prerequisites)

- Node.js 18+
- [FFmpeg](https://ffmpeg.org/download.html) on your PATH (used for video assembly and audio muxing)
- Google account (YouTube Data API — free)
- At least one AI provider key (OpenAI or Gemini) — without one, agents fall back to template-based generation

## Configuration

[Permalink: Configuration](https://github.com/darkzOGx/youtube-automation-agent#configuration)

### API Keys

[Permalink: API Keys](https://github.com/darkzOGx/youtube-automation-agent#api-keys)

#### YouTube Data API (required, free)

[Permalink: YouTube Data API (required, free)](https://github.com/darkzOGx/youtube-automation-agent#youtube-data-api-required-free)

1. Create a project in [Google Cloud Console](https://console.cloud.google.com/)
2. Enable **YouTube Data API v3**
3. Create an OAuth 2.0 client (Desktop app)
4. Save the JSON as `config/credentials.json`

#### OpenAI

[Permalink: OpenAI](https://github.com/darkzOGx/youtube-automation-agent#openai)

1. Get a key from [platform.openai.com](https://platform.openai.com/)
2. Set `OPENAI_API_KEY` in `.env`

#### OpenRouter (easiest — one key, all models)

[Permalink: OpenRouter (easiest — one key, all models)](https://github.com/darkzOGx/youtube-automation-agent#openrouter-easiest--one-key-all-models)

1. Get a key from [openrouter.ai/keys](https://openrouter.ai/keys)
2. Set `OPENROUTER_API_KEY` in `.env`

#### Google Gemini

[Permalink: Google Gemini](https://github.com/darkzOGx/youtube-automation-agent#google-gemini)

1. Get a key from [Google AI Studio](https://aistudio.google.com/)
2. Set `GEMINI_API_KEY` in `.env`

#### Kimi / MiMo / GLM

[Permalink: Kimi / MiMo / GLM](https://github.com/darkzOGx/youtube-automation-agent#kimi--mimo--glm)

| Provider | Get key at | Env var |
| --- | --- | --- |
| Kimi (Moonshot AI) | [platform.kimi.ai](https://platform.kimi.ai/) | `MOONSHOT_API_KEY` |
| MiMo (Xiaomi) | [mimo.mi.com](https://mimo.mi.com/) | `MIMO_API_KEY` |
| GLM (Zhipu AI) | [z.ai](https://z.ai/) | `GLM_API_KEY` |

### Environment Variables

[Permalink: Environment Variables](https://github.com/darkzOGx/youtube-automation-agent#environment-variables)

```
# AI provider — pick one (or use OpenRouter for access to all)
OPENAI_API_KEY=sk-...
# OPENROUTER_API_KEY=sk-or-...
# GEMINI_API_KEY=...
# MOONSHOT_API_KEY=...
# MIMO_API_KEY=...
# GLM_API_KEY=...

# Optional: premium TTS
# ELEVENLABS_API_KEY=...
# ELEVENLABS_VOICE_ID=...

# Optional: AI video generation
# REPLICATE_API_KEY=...

# App config
NODE_ENV=production
PORT=3456
CHANNEL_NAME=Your Channel Name
TARGET_AUDIENCE=Your target audience
YOUTUBE_REGION=US
DEFAULT_PRIVACY_STATUS=private

# Optional: protect mutating API routes (POST /generate, /publish)
# API_KEY=some-long-random-string
```

## Automation Schedule

[Permalink: Automation Schedule](https://github.com/darkzOGx/youtube-automation-agent#automation-schedule)

Render

06:0007:0008:0009:0010:0011:0012:0013:0014:0015:0016:0017:0018:0019:0020:0021:0022:0023:00Generate content (strategy + script + thumbnail + SEO) Process publishing queue Collect analytics Run optimizations ContentPublishingAnalyticsDaily Pipeline

Loading

```
gantt
    title Daily Pipeline
    dateFormat HH:mm
    axisFormat %H:%M

    section Content
    Generate content (strategy + script + thumbnail + SEO) :06:00, 2h

    section Publishing
    Process publishing queue :crit, 08:00, 14h

    section Analytics
    Collect analytics     :09:00, 1h
    Run optimizations     :22:00, 1h
```

The scheduler runs automatically after `npm start`. Content generation at 06:00, publishing queue processed every 15 minutes, analytics at 09:00, optimization at 22:00. Weekly strategy reviews run on Sundays.

## API

[Permalink: API](https://github.com/darkzOGx/youtube-automation-agent#api)

```
# health check
curl http://localhost:3456/health

# generate a video on demand (send x-api-key if API_KEY is set in .env)
curl -X POST http://localhost:3456/generate \
  -H "Content-Type: application/json" \
  -H "x-api-key: $API_KEY" \
  -d '{"topic": "Top 10 Life Hacks", "style": "list"}'

# view schedule
curl http://localhost:3456/schedule

# get analytics
curl http://localhost:3456/analytics

# publish a specific content item
curl -X POST http://localhost:3456/publish/:contentId
```

## Production Pipeline

[Permalink: Production Pipeline](https://github.com/darkzOGx/youtube-automation-agent#production-pipeline)

Render

Video Assembly

fallback

fallback

Wan 2.7 I2V

Playwright Slideshow

Simulation

Image Generation

fallback

GPT Image 2

Simulation

Audio Generation

fallback

fallback

ElevenLabs v3

OpenAI TTS

Simulation

FFmpeg Mux

Final Video

Loading

```
flowchart LR
    subgraph TTS["Audio Generation"]
        direction TB
        EL[ElevenLabs v3] -.->|fallback| OA[OpenAI TTS]
        OA -.->|fallback| SIM1[Simulation]
    end

    subgraph IMG["Image Generation"]
        direction TB
        GPT[GPT Image 2] -.->|fallback| SIM2[Simulation]
    end

    subgraph VID["Video Assembly"]
        direction TB
        WAN[Wan 2.7 I2V] -.->|fallback| PW[Playwright Slideshow]
        PW -.->|fallback| SIM3[Simulation]
    end

    TTS --> MIX[FFmpeg Mux]
    IMG --> VID
    VID --> MIX
    MIX --> OUT[Final Video]
```

Each stage has graceful fallbacks. If a paid API key isn't configured, the system simulates that step so the rest of the pipeline still runs.

## Extending

[Permalink: Extending](https://github.com/darkzOGx/youtube-automation-agent#extending)

### Custom AI provider

[Permalink: Custom AI provider](https://github.com/darkzOGx/youtube-automation-agent#custom-ai-provider)

```
// utils/ai-service.js
const Anthropic = require('@anthropic-ai/sdk');

class ClaudeAIService {
  constructor(apiKey) {
    this.client = new Anthropic({ apiKey });
  }
  async generateContent(prompt) {
    const message = await this.client.messages.create({
      model: 'claude-opus-4-8',
      max_tokens: 1024,
      messages: [{ role: 'user', content: prompt }]
    });
    return message.content[0].text;
  }
}
```

### Custom content types

[Permalink: Custom content types](https://github.com/darkzOGx/youtube-automation-agent#custom-content-types)

```
// agents/content-strategy-agent.js
const contentTypes = {
  'podcast': {
    duration: '10-15 minutes',
    style: 'conversational',
    thumbnail: 'podcast-style'
  },
};
```

## Project Structure

[Permalink: Project Structure](https://github.com/darkzOGx/youtube-automation-agent#project-structure)

```
youtube-automation-agent/
├── agents/          # one file per agent
├── config/          # credentials, example configs
├── database/        # SQLite schema and access layer
├── data/            # generated content and assets
├── schedules/       # cron-based automation
├── utils/           # AI service wrappers, logging, credential management
├── .github/         # CI workflow (lint + tests on every push/PR)
└── index.js         # Express server + agent initialization
```

## Troubleshooting

[Permalink: Troubleshooting](https://github.com/darkzOGx/youtube-automation-agent#troubleshooting)

| Problem | Fix |
| --- | --- |
| YouTube API quota exceeded | Check quotas in Google Cloud Console; reduce posting frequency |
| Content generation failed | Verify API keys and credits; check `logs/` |
| Publishing failed | Re-authenticate YouTube OAuth tokens; check video format |

Enable debug logging:

```
NODE_ENV=development DEBUG_MODE=true npm start
```

## More Tools by darkzOGx

[Permalink: More Tools by darkzOGx](https://github.com/darkzOGx/youtube-automation-agent#more-tools-by-darkzogx)

If this was useful, check out:

- [darkzloop](https://github.com/darkzOGx/darkzloop): terminal agent runner that turns any LLM into a disciplined software engineer (FSM control, model-agnostic, BYO auth)
- [darkzBOX](https://github.com/darkzOGx/darkzBOX): open-source Instantly.ai clone with smart automated email replies
- [open-sales-researcher](https://github.com/darkzOGx/open-sales-researcher): autonomous B2B company research. Works with Claude Code, Cursor, Copilot.
- [darkzseo](https://github.com/darkzOGx/darkzseo): SEO tooling

## Contributing

[Permalink: Contributing](https://github.com/darkzOGx/youtube-automation-agent#contributing)

1. Fork the repo
2. Create a feature branch
3. Make changes and add tests
4. Submit a PR

```
git clone <your-fork>
cd youtube-automation-agent
npm install
npm run lint   # must pass — CI runs this on every PR
npm test
```

## License

[Permalink: License](https://github.com/darkzOGx/youtube-automation-agent#license)

MIT — see [LICENSE](https://github.com/darkzOGx/youtube-automation-agent/blob/master/LICENSE).

## Acknowledgments

[Permalink: Acknowledgments](https://github.com/darkzOGx/youtube-automation-agent#acknowledgments)

- [OpenAI](https://openai.com/) — GPT-5.5, GPT Image 2, GPT-4o-mini-tts
- [OpenRouter](https://openrouter.ai/) — unified multi-model API
- [Google](https://ai.google.dev/) — YouTube Data API, Gemini 3.5
- [Moonshot AI](https://www.moonshot.ai/) — Kimi K2.6
- [Xiaomi](https://mimo.mi.com/) — MiMo V2.5
- [Zhipu AI](https://z.ai/) — GLM-5
- [ElevenLabs](https://elevenlabs.io/) — Eleven v3 TTS
- [Replicate](https://replicate.com/) — Wan 2.7 video generation
- [ConstructionBids.ai](https://constructionbids.ai/) \- AI scans every federal, state & local public works bid and matches you to contracts you'll win.

* * *

> This tool is for legitimate content creation. Comply with [YouTube's Terms of Service](https://www.youtube.com/t/terms) and Community Guidelines.

## About

🎬 Fully automated YouTube channel management with AI agents. Creates, optimizes & publishes videos 24/7. Works with FREE Gemini API or OpenAI. No coding required!


[github.com/darkzOGx/youtube-automation-agent#readme](https://github.com/darkzOGx/youtube-automation-agent#readme "https://github.com/darkzOGx/youtube-automation-agent#readme")

### Topics

[nodejs](https://github.com/topics/nodejs "Topic: nodejs") [javascript](https://github.com/topics/javascript "Topic: javascript") [automation](https://github.com/topics/automation "Topic: automation") [youtube-api](https://github.com/topics/youtube-api "Topic: youtube-api") [openai](https://github.com/topics/openai "Topic: openai") [seo-optimization](https://github.com/topics/seo-optimization "Topic: seo-optimization") [content-automation](https://github.com/topics/content-automation "Topic: content-automation") [youtube-channel](https://github.com/topics/youtube-channel "Topic: youtube-channel") [content-strategy](https://github.com/topics/content-strategy "Topic: content-strategy") [ai-agents](https://github.com/topics/ai-agents "Topic: ai-agents") [thumbnail-generator](https://github.com/topics/thumbnail-generator "Topic: thumbnail-generator") [youtube-bot](https://github.com/topics/youtube-bot "Topic: youtube-bot") [video-generation](https://github.com/topics/video-generation "Topic: video-generation") [content-creation](https://github.com/topics/content-creation "Topic: content-creation") [youtube-uploader](https://github.com/topics/youtube-uploader "Topic: youtube-uploader") [ai-powered](https://github.com/topics/ai-powered "Topic: ai-powered") [youtube-automation](https://github.com/topics/youtube-automation "Topic: youtube-automation") [social-media-automation](https://github.com/topics/social-media-automation "Topic: social-media-automation") [free-tool](https://github.com/topics/free-tool "Topic: free-tool") [google-gemini](https://github.com/topics/google-gemini "Topic: google-gemini")

### Resources

[Readme](https://github.com/darkzOGx/youtube-automation-agent#readme-ov-file)

### License

[MIT license](https://github.com/darkzOGx/youtube-automation-agent#MIT-1-ov-file)

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/darkzOGx/youtube-automation-agent).

[Activity](https://github.com/darkzOGx/youtube-automation-agent/activity)

### Stars

**1.5k**
stars


### Watchers

**16**
watching


### Forks

[**382**\\
forks](https://github.com/darkzOGx/youtube-automation-agent/forks)

[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FdarkzOGx%2Fyoutube-automation-agent&report=darkzOGx+%28user%29)

## [Releases](https://github.com/darkzOGx/youtube-automation-agent/releases)

No releases published

## [Packages\  0](https://github.com/users/darkzOGx/packages?repo_name=youtube-automation-agent)

No packages published

## [Contributors\  2](https://github.com/darkzOGx/youtube-automation-agent/graphs/contributors)

- [![@claude](https://avatars.githubusercontent.com/u/81847?s=64&v=4)](https://github.com/claude)[**claude** Claude](https://github.com/claude)
- [![@darkzOGx](https://avatars.githubusercontent.com/u/128010917?s=64&v=4)](https://github.com/darkzOGx)[**darkzOGx** Haithum Abdelfattah](https://github.com/darkzOGx)

## Languages

- [JavaScript94.6%](https://github.com/darkzOGx/youtube-automation-agent/search?l=javascript)
- [HTML5.4%](https://github.com/darkzOGx/youtube-automation-agent/search?l=html)

You can’t perform that action at this time.