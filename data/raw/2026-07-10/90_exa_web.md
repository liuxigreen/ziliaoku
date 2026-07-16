---
title: "Claude Code 進階究極手冊：官方完整技巧 × 大神實戰用法（2026 最新版・含舊指令勘誤） | DataAgent"
platform: 网页/公众号
source: Exa搜索
search_query: "Claude Code 使用技巧"
url: "https://www.idataagent.com/2026/06/30/claude-code-advanced-ultimate-guide-2026/"
published: "2026-06-29T17:25:15.000Z"
collected: "2026-07-10"
---


這篇是把 Anthropic 官方《Claude Code 進階使用者技巧》逐條無遺漏整理，再疊上十位以上公認大神的真實工作流（每招都附原始出處），最後標出官方文件已經改掉、照舊教學會打到無效指令的地方。目標只有一個：讓你看完這一篇，就握有目前最完整、且最新最正確的 Claude Code 進階地圖。
...
全文分五部：A 心法（為什麼這樣用）→ B 官方核心技巧（原文 16 節全收）→ C 大神實戰（點名 + 招式 + 出處）→ D 社群工作流與避坑 → E 速查表。指令請以`code.claude.com/docs`為準——Claude Code 改版很快，本文已盡量對齊到 ~v2.1.19x。
...
### 1. 把 Claude Code 當「會自己驗證的工程隊」，不是自動補完
...
### 2. 驗證迴圈（Validation）＝品質的第一槓桿
...
- 後端／函式：跑`tests`、`build`、type-check、lint。
- 前端／網頁：裝 Claude Code Chrome 擴充（`code.claude.com/docs/en/chrome`），或用桌面版內建瀏覽器自動開測試伺服器——「如果你請工程師做網站卻不讓他開瀏覽器，成品會好看嗎？」
- 改完隨手`/simplify`：在任何 prompt 後面接`/simplify`，它會平行開多個 agent 同時檢查「可重用性、品質、效率、是否符合 CLAUDE.md」。
...
### 3. 用最強模型 + 思考力，反而更快
...
思考力／Effort 等級：`/effort high|xhigh|max|auto`（也可`--effort `或`effortLevel`設定）。日常用`high`，複雜 agent 工作切`xhigh`，最難的除錯／架構決策用`max`。
...
- ⚠️ 勘誤：舊教學的「think / think hard / think harder」分級已不是有效關鍵字，現在只剩`ultrathink`仍被辨識；真正的旋鈕是`/effort`。用`Option+T`切換是否常駐思考。
...
### 4. 平行作戰：同時跑多個 Claude
...
- 把`.claude/worktrees/`加進`.gitignore`（官方建議），用根目錄`.worktreeinclude`（gitignore 語法）把`.env`等檔複製進每個 worktree；
- 每個 agent 用不同 port／DB：`vite --port $((5173 + IDX))`、各自`DATABASE_URL=…_featureX`，否則多開會互撞；
- node_modules 各自`install`（最穩）或用 pnpm 內容定址 store。
...
### 5. 先計畫再動工：Plan Mode
...
1. 編排工具（懶得手刻就用）：`smtg-ai/claude-squad`（tmux+worktree，`brew install claude-squad`）、`devflowinc/uzi`（自動配 port、`uzi prompt --agents claude:2 "…"`）、`coderabbitai/git-worktree-runner`（postCreate 自動`npm install`）、`kbwo/ccmanager`（免 tmux 的 TUI session 管理）。
2. 進 plan mode → 反覆精修計畫 → 切到 auto-accept edits → 執行。
3. 雙 Claude 互審：一個寫計畫，另一個當資深工程師 review。
4. 出問題立刻切回 plan mode 重新規劃，不要在執行中途硬拗。
5. session 會自動命名，也可`claude --name "auth-refactor"`預設。
6. 看計畫的好工具：`Ctrl+G`把計畫開進`$EDITOR`再決定是否放行。Boris Cherny 的口訣：「如果你能用一句話描述這個 diff，就跳過 plan。」
...
### 6. Prompt 心法：不接受第一版
...
### 7. CLAUDE.md 與記憶系統：複利工程（Composite Engineering）
...
- 組織政策層（managed）→ 使用者層`~/.claude/CLAUDE.md`→ 專案層`./CLAUDE.md`或`./.claude/CLAUDE.md`→ 本地層`./CLAUDE.local.md`（gitignored，仍完整支援）。
- `@path`匯入其他檔（最多 4 跳）：`See @README for overview and @package.json for npm commands.`
...
自動記憶：`/memory`設定內建記憶系統，跨 session 自動存偏好／糾正／模式，寫到`~/.claude/projects/ /memory/`。
...
### 8. 指令、Skills、Subagents
...
- ⚠️ 重大變動：自訂 slash command 已與 Skills 合併——`.claude/commands/x.md`與`.claude/skills/x/SKILL.md`都會產生`/x`（舊的`commands/`仍可用）。
- slash command 可內嵌 bash 預先算好資訊（如`!`git status``）省一次模型呼叫；需在 frontmatter 用`allowed-tools: Bash(...)`放行。
...
Subagents（`.claude/agents/`）：每個`.md`一個專家，可設名稱／顏色／工具集／權限模式／模型。frontmatter 只有`name`和`description`必填；`description`寫「何時該派它」會驅動自動委派（加「use proactively」更容易被自動叫用）。
...
- 用`claude --agent ReadOnly`啟動；`/agents`互動管理（即時生效不必重啟）。
- runtime 借力：在請求後面加「use sub-agents」把零碎工作丟給 subagent，保持主 agent 的 context 乾淨。
- Code review agent 隊：PR 一開，自動派一隊 agent 各管一塊（邏輯錯誤、安全、效能回歸）貼 inline 評論。Anthropic 自家就是先為自己做這個——工程師產出暴增後，review 反而成了瓶頸。
...
### 9. Hooks：生命週期自動化
...
| 事件 | 用途 |
| --- | --- |
| `SessionStart` | 每次啟動動態載入內容 |
| `PreToolUse` | 記錄每一條 bash 指令 |
| `PostToolUse` | 寫檔後自動 format，避免 CI 掛掉 |
| `PermissionRequest` | 把權限提示轉到 Slack/WhatsApp/Opus 審 |
| `Stop` | 對長任務跑確定性檢查，或叫 Claude 繼續 |
| `PreCompact`/`PostCompact` | 壓縮前後重新注入關鍵指令 |
...
🆕 現行 hook 事件已大幅擴充（`UserPromptSubmit`、`SubagentStart`、`PostToolUseFailure`、`TaskCompleted`…），handler`type`除了`command`還有`http`、`prompt`（用 Haiku 當 LLM 把關）、`mcp_tool`。退出碼 2＝阻擋並把 stderr 餵回 Claude；`/hooks`是唯讀檢視。
...
### 10. 權限與安全
...
`/permissions`預先核可：把安全指令加白名單、入團隊`.claude/settings.json`。這是「完全取代直接跳過權限」的建議做法——少打擾、可稽核。支援 wildcard：`"Bash(bun run *)"`、`"Edit(/docs/**)"`。
...
長時間無人值守：用`Stop` hook 做確定性檢查，或在沙箱裡用`--permission-mode=dontAsk`/`--dangerously-skip-permissions`避免被卡住。
...
### 11. 排程與重複任務
...
- `/loop`（本地，最多 3 天）：`/loop 5m /babysit`（自動處理 review/rebase/顧 PR）、`/loop 30m /slack-feedback`、`/loop 1h /pr-pruner`。
- `/schedule`（雲端，關電腦也跑）：`/schedule 每天看昨天之後 ship 的所有 PR、據此更新文件，用 Slack MCP 把變更貼到 #docs-update`。
- 把常用工作流做成 skill + loop，威力最大。
...
### 12. 行動與遠端遙控
...
### 13. 工具整合（MCP）
...
⚠️ 安全：官方明講「連接前先確認你信任這個 server；會抓外部內容的 server 有 prompt injection 風險」。DB 用唯讀憑證、PAT 用細粒度權限、`project` scope 的`.mcp.json`首次使用會要你核可。
...
### 14. 打造你的環境
...
### 15. SDK 與多 repo
...
`--bare`加速約 10×：`claude -p`（SDK）預設會搜尋本地 CLAUDE.md/設定/MCP；非互動用途明確指定`--system-prompt`/`--mcp-config`/`--settings`並加`--bare`，跳過自動探索、CI 可重現。
...
### 16. 成本優化（進階者的省 token 心法）
...
`、`/
...
| 領域 | 關鍵指令 |
| --- | --- |
| 平行 | `claude --worktree`、`--tmux`、`/batch`、subagent`isolation: worktree` |
| 規劃 | `Shift+Tab`（plan mode）、`/effort max`、`Ctrl+G`、`claude --name` |
| 記憶 | `CLAUDE.md`、`@path`匯入、`/memory`、PR 裡`@claude` |
| 驗證 | Chrome 擴充、`/simplify`、桌面內建瀏覽器 |
| 自動化 | `.claude/skills/`、`.claude/agents/`、`--agent`、「use sub-agents」 |
| Hooks | `PostToolUse`、`Stop`、`PreCompact`、`PermissionRequest` |
| 權限 | `/permissions`（wildcard）、`--enable-auto-mode`、`/sandbox` |
| 排程 | `/loop`（本地）、`/schedule`（雲端） |
| 遠端 | `--teleport`、`/remote-control`、手機 app、iMessage 外掛 |
| 客製 | `/statusline`、`/color`、`/voice`、`/keybindings`、`/config` |
| SDK/多 repo | `claude -p --bare`、`--add-dir`、`--fork-session` |
| 看花費 | `/usage`（headless：`--output-format json`→`total_cost_usd`） |

---

