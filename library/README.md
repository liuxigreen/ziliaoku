# 资料库（产品级）

这里是 **对外订阅的成品资料库**，是整个 ziliaoku 项目的核心资产（订阅产品 99–299 元/年）。

## 三层结构

| 层 | 目录 | 谁来维护 | 用途 |
|---|---|---|---|
| 流水线中间产物 | `data/` | 脚本（agent-reach / firecrawl / SoPilot） | raw 采集、extracted、clusters、signals |
| 成稿 | `output/` | `ziliaoku-draft` 技能 | 待发布的帖子草稿 `output/posts/{date}/` |
| **成品资料库（本目录）** | `library/` | **你（人工勾选收口）** | 精选选题 + 可复用素材，订阅用户最终看到的就是这层 |

## 每周收口 SOP

1. `ziliaoku-topics` 产出 `output/topics_{week}.md`（本周候选选题库）。
2. 你**人工勾选**本周要保留的选题（人工卡点之一）。
3. 精选进 `library/topics/{week}.md`，并在文首用 frontmatter 标 `status: published/pending`、`tier: 免费/会员`。
4. 顺手把好用的**标题公式 / 封面风格**沉淀回根目录资产：
   - 标题公式 → `formulas.md` / `titles_pool.jsonl`
   - 封面风格 → `image-styles.md`
   - 信号样本 → `data/signals/`

> 原则：**脚本只负责"铺货"，人负责"选品"**。库的质量 = 你每周勾选的眼光。

## 用 Obsidian 看 / 维护本库

1. 安装 [Obsidian](https://obsidian.md)（免费、本地优先、不上云）。
2. `File → Open folder as vault`，选 `D:\WorkBuddyProjects\ziliaoku`（整个项目当 vault）。
3. `Settings → Files & Links`：**关闭 "Use [[Wikilinks]]"**，改用 Markdown 链接——
   这样 `[[ ]]` 语法不会漏进脚本要解析的 `.md` 文件。
4. 本库所有 `.md` 都带 YAML frontmatter（title/author/platform/verdict…），
   Obsidian 原生当作 **Properties** 读，可直接按属性筛选、排序、做关系图。
5. 起点看 `library/index.md`（总索引 / 图谱入口）。

> `.obsidian/` 配置已写进 `.gitignore`，不会污染 git 版本库。

## 目录

- `topics/` — 成品选题库，按周归档（`{week}.md`），每周从 `output/topics_{week}.md` 收口。
- `index.md` — 总索引（MOC），Obsidian 图谱入口。
