# ziliaoku 流水线技能索引

本目录是「爆文选题工作流」各阶段的 **WorkBuddy 技能（SKILL.md）**，接口已冻结，按下方顺序串成全自动流水线。人工只保留三个卡点：每周选题勾选、发布前终审、周复盘填数据。

## 流水线顺序

| # | 技能 | 对应 Prompt | 输入 | 输出 | 依赖 |
|---|------|------------|------|------|------|
| 1 | `ziliaoku-collect` | 采集层 | keywords.md / watchlist.md | `data/raw/{date}/*.md` | firecrawl / agent-reach / SoPilot RSS（部分待接） |
| 2 | `ziliaoku-gate` | Prompt-A0 | raw md（含 source_type/source_platform） | verdict: collect/hack_only/signal/discard | 纯 LLM ✅ |
| 3 | `ziliaoku-extract` | Prompt-A | 过闸 raw md | `data/extracted/{date}.jsonl` | 纯 LLM ✅ |
| 4 | `ziliaoku-cluster` | Prompt-B | 本周 extracted | `data/clusters/{week}.json` + formulas.md | 纯 LLM ✅ |
| 4b | `ziliaoku-signal` | Prompt-S | gate 判 signal 的条目 | `data/signals/{week}.json` | 纯 LLM ✅ |
| 5 | `ziliaoku-topics` | Prompt-C | clusters + formulas + account | `output/topics_{week}.md` | 纯 LLM ✅ |
| 6 | `ziliaoku-draft` | Prompt-E | 一条选题 + account | `output/posts/{date}/` | 纯 LLM ✅ |
| 7 | `ziliaoku-image` | Prompt-F | draft 的 image_briefs + image-styles | 图像提示词（同目录） | ComfyUI / 即梦（待接） |
| 8 | `ziliaoku-review` | Prompt-D | 本周发布数据 + gate 统计 | `reviews/{week}.md` | 纯 LLM ✅ |

## 数据流

```
采集(collect) → 质检(gate) ─┬→ collect/hack_only → 提取(extract) → 聚类(cluster) → 选题库(topics) → 成稿(draft) → 配图(image) → 发布 → 周复盘(review)
                            └→ signal → 风向标(signal) ────────────────┘（作工具向/蹭热点选题来源）
```

## 设计原则（冻结，不可变通）
- **发现与抓取分离**：聚合站只"发现"，firecrawl/agent-reach 才"抓全文"；聚合页摘要禁止当正文入库。
- **入口数量纪律 ≤ 6**：现 4（NewsNow/今日热榜/SoPilot/watchlist）+ Reddit = 5，留 1 空位；新增入口唯一依据 = 周复盘连续两周明确缺口。
- **质检拿不准判 collect**：入口闸门只拦明显垃圾，去伪存真交给聚类与周复盘。
- **小红书已从采集源移除**（信噪比低）；标题公式来源改为公众号爆文 + X 爆帖 + 热榜标题本身。
- **信号第四态**：GitHub/工具类条目判 `signal` 走风向标通道，不进爆文库聚类。
- **人工卡点**：任何内容上线前必须经用户终审——自动化的是生产和排期，不是决策权。

## 当前可立即运行（纯 LLM，不需外部工具）
gate / extract / cluster / signal / topics / draft / review 七个技能当前环境即可按接口实测。
采集（缺 firecrawl/agent-reach）、配图（缺 ComfyUI/即梦）需接工具后实跑。
