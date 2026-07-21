---
name: ziliaoku-dual-publish
description: ziliaoku 双平台（小红书·打工人北北 / 公众号·小木）发文流水线唯一真相源。覆盖选题→双版本成稿→双方配图→公众号排版→脱钩校验→发布→台账→git 的全步骤与完整资产清单。当用户说"发一篇/写文章/双平台/根据分析选题发/小红书公众号"时加载，防止漏掉任一资产（尤其公众号封面图+正文插图）。agent_created: true
---

# ziliaoku 双平台发文流水线（唯一真相源）

> 痛点：步骤多、跨会话易忘。本 skill 是**单点真相源**——每次发文前加载，按「完整资产清单」逐项打勾，缺一项都不算完。

## 铁律（不可破）
- **双版本各自独立、互不引用、不互相引流**。小红书署名=打工人北北，公众号署名=小木（硬编码，正文里绝不许混）。
- **只存草稿 / 手动发布，绝不自动群发**。
- 发布前必过**脱钩校验**（见下）。
- 造物矩阵 GitHub 雷达 = **手动选题参考源，不接自动管线**。

## 完整资产清单（每篇必须产出，缺一不可）

### A. 小红书（打工人北北）
1. `*_xhs.md`：标题 ≤20 字、正文 ≤500 字、emoji 分点、结尾 CTA 提问引导、5 个 #话题。
   - 禁：含「公众号」「小木」、含 🤖 AI 指令块。
2. 封面 `xhs_cover_*_3x4.png`：1080×1440，PIL 叠中文（msyhbd.ttc），品牌胶囊「打工人北北」。
3. 2-3 张文字卡片 `xhs_card*_*_3x4.png`：PIL，承载分点/动作。
4. （发布）opencli 草稿：`scripts/publish_xhs_draft.py`（走 node，正文作位置参数；`--content` 不被识别）。
   - ⚠️ 主 profile `4tvh3uwd` 浏览器桥接常断 → 报 `BROWSER_CONNECT` 时改用 `XHS_PROFILE=kzbaq3xs` 兜底。

### B. 公众号（小木）
1. `*_wechat.md`：2500-3500 字、6 章节、文末「给 AI 的极简指令」块（🤖 行 + · 行）、「我是小木」签名、结尾 CTA。
   - 禁：含「小红书」「打工人北北」。
2. **封面图 / 头图 `gzh_header_*_*.png`：900×383（2.35:1），PIL 叠中文标题 + 「小木」胶囊。← 公众号发文的必填项（订阅列表/分享卡片缩略图），缺了不能发。**
3. **N 张正文插图 `gzh_assets/illustrations/NN-*.png`：16:9 白底手绘「小黑」风，走 `ian-xiaohei-illustrations` skill（ImageGen，单张 ~5-10 积分）。放认知锚点段落后。← 极易漏，每次显式核对。**
4. 排版：`gen_*.py`（复用 `scripts/gzh_publish/gzh_style.py`）→ `_排版.html` → `make_preview.py` → `_预览.html`（摸鱼绿）。
5. （发布）个人号无 API：用户复制 `_预览.html` 文字粘后台 + 上传封面图/插图到图片库手动插入（**不能靠复制 HTML 的 `<img>` 过去**）。

## 流程步骤
1. **选题**：基于账号复检结论（公众号吃避坑/实测/个人经历；小红书吃避坑+强钩子+老外来源/数字+评论引导）。造物矩阵雷达定题后手动翻找 git 链接。
2. **写双版本 md**（各自守禁则）。
3. **配图**：PIL 生成双方封面/卡片/头图；ImageGen 生成公众号正文插图（ian-xiaohei-illustrations）。
4. **公众号排版**：gzh_style → make_preview。
5. **脱钩校验**（脚本或手查）：
   - 小红书 md 不含「公众号」「小木」「🤖」；≤500 字。
   - 公众号 md 不含「小红书」「打工人北北」；含 🤖 AI 指令块 + 「我是小木」签名。
   - 封面 <200KB（>1MB 触发 base64 限制，压成 JPG 质量 85）。
6. **发布**：小红书 opencli 草稿（kzbaq3xs 兜底）；公众号交付 `_预览.html` + 图资产，用户手动。
7. **台账**：北北 `output/monitoring/2026-07-14/账号分析_打工人北北.md` + 小木 `output/monitoring/2026-07-16/账号分析_小木.md` 各追加一行。
8. **git**：`git add` 新文章目录 + 双台账 → commit → pull --rebase → push。
9. **交付预览（发图给用户，必做）**：所有资产生成 + 脱钩校验通过后，**用 present_files 把 小红书封面 + 公众号头图/封面 + 正文插图（小黑）发出来给用户预览**。每篇都必须"发"出来看，不能只在 repo 里生成完就结束——这是用户明确要求的收尾动作（曾发生过只发 skill/清单、漏发实际图的情况）。

## 已知坑（每次对照）
- `4tvh3uwd` 桥接断 → 小红书发布切 `kzbaq3xs`。
- opencli `publish` **不识 `--content`**，正文必须作位置参数传给 `publish_xhs_draft.py`。
- 封面 >1MB 触发 base64 上限 → 压 JPG <200KB。
- 公众号插图**不能靠复制 HTML `<img>`**，必须后台上传拿 CDN 链接再插。
- D 盘 repo 大文件偶尔会话间丢失 → 提交后若 missing 用 `git restore <path>`。
- 小红书发布前先确认 `4tvh3uwd` Chrome 已开 + OpenCLI 扩展已连。

## 参考资产（照抄改词）
- 流水线脚本：`scripts/gzh_publish/gzh_style.py`、`make_preview.py`。
- 范例：`output/posts/2026-07-20/local_first_coding/`（gen_assets.py / gen_*_html.py 可复制改词）、`output/posts/2026-07-21/ai_slower_smarter/`（含 ian-xiaohei 插图目录）。
- 子技能：`ian-xiaohei-illustrations`（公众号插图）、`ziliaoku-xhs-publish`（小红书草稿）。
- 台账：北北 / 小木 两文件（写稿前先读防断链）。
