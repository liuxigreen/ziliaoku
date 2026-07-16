# 选题库 2026-W28（7/7–7/13）

> 生成链路：collect(93篇) → gate(69 collect + 24 signal) → extract(69) → cluster(2026-W28) → signal(24) → **topics(本文件)**
> 素材主源：14 篇带字幕英文 YouTube 源头（Claude Code / ComfyUI / AI视频 / n8n / 内容增长 / 副业）+ Reddit 实操帖 + X 标题公式样本 + GitHub 神库（ECC 22万★ 等）
> 人设：用 AI Agent 做内容工作流的实操博主（实操/接地气/不画饼）
> 红线：不提收益数字、不绝对化、不硬引流。标题候选已压 ≤20 字。

## 选题清单（20 个）

### 蹭热点 / 高优先（排前）

```json
{
  "id": "T01",
  "topic": "译介 Claude Code 32 个实操技巧（数字型爆款结构）",
  "title_candidates": ["让AI自己提问，返工少一半", "Claude Code 32招我留这5个", "用Claude Code半年才懂的坑"],
  "hook_draft": "用 Claude Code 半年，直到刷到那期「32个技巧」才发现自己一直在裸奔。",
  "structure_ref": "钩子自曝 → 核心3点 → 我的不同意见 → 提问式CTA",
  "evidence": "84_yt_NateHerkAIAu.md（2.2万字字幕，32 tricks 分 beginner/intermediate/advanced）",
  "fit_score": 9,
  "fit_dimensions": {"喜欢":5, "擅长":5, "难复制":4, "风口上升":5},
  "urgency": "常青",
  "monetization_role": "引流"
}
```

```json
{
  "id": "T02",
  "topic": "GitHub 神库盘点：Claude Code harness 优化系统（22万★）",
  "title_candidates": ["这个22万星库治好了我的AI焦虑", "Claude Code玩家都该存的库", "我扒了22万★的Agent harness"],
  "hook_draft": "收藏夹吃灰的 GitHub 库很多，但这个 22 万星的 Agent harness 我是真用上了。",
  "structure_ref": "问题陈述 → 库能解决什么 → 我怎么用 → 自取提示",
  "evidence": "21_github_ECC.md（stars:227482，Claude Code/Codex harness 性能优化）",
  "fit_score": 8,
  "fit_dimensions": {"喜欢":4, "擅长":4, "难复制":5, "风口上升":5},
  "urgency": "蹭热点(3天内发)",
  "monetization_role": "引流"
}
```

```json
{
  "id": "T03",
  "topic": "从 20 条 X 爆帖提炼的小红书标题公式",
  "title_candidates": ["我扒了20条爆帖的标题套路", "爆款标题就这3种结构", "标题不会起？抄这20个模板"],
  "hook_draft": "标题决定打开率，这话听腻了。我直接扒了 20 条爆帖，把套路拆给你。",
  "structure_ref": "痛点 → 公式3种 → 套用示例 → 清单自取",
  "evidence": "data/raw/2026-07-09 中 20 篇 X/Twitter 样本（标题公式库来源）",
  "fit_score": 9,
  "fit_dimensions": {"喜欢":5, "擅长":4, "难复制":5, "风口上升":5},
  "urgency": "常青",
  "monetization_role": "引流"
}
```

### 引流型（共 10，其余）

```json
{
  "id": "T04",
  "topic": "译介 AI 视频生成工具（Kling/Jimeng 类）实操",
  "title_candidates": ["AI视频工具我测了这5个", "新手做AI视频从哪上手", "别乱买课，先试这俩工具"],
  "hook_draft": "想做 AI 视频又怕踩坑？我把几个主流工具都跑了一遍。",
  "structure_ref": "钩子 → 工具横评 → 我的用法 → 提问CTA",
  "evidence": "88_yt_AIVideoSchool.md（5.4万字字幕，AI video generation 教程）",
  "fit_score": 8,
  "fit_dimensions": {"喜欢":4, "擅长":4, "难复制":4, "风口上升":5},
  "urgency": "常青",
  "monetization_role": "引流"
}
```

```json
{
  "id": "T05",
  "topic": "译介 n8n 自动化工作流入门（接地气版）",
  "title_candidates": ["用n8n把我重复活干没了", "自动化工作流新手别绕路", "n8n入门我就看这一期"],
  "hook_draft": "每天重复点同样的按钮？我用 n8n 把那些活全塞给机器了。",
  "structure_ref": "场景痛点 → 工作流截图 → 节点讲解 → 模板自取",
  "evidence": "YT_QUERIES「n8n automation workflow」命中英文源头（待 extract 深读）",
  "fit_score": 8,
  "fit_dimensions": {"喜欢":4, "擅长":4, "难复制":4, "风口上升":5},
  "urgency": "常青",
  "monetization_role": "引流"
}
```

```json
{
  "id": "T06",
  "topic": "译介 ComfyUI 工作流（给非技术人）",
  "title_candidates": ["ComfyUI我没学代码也跑通", "小白用ComfyUI做图流程", "这张图是ComfyUI跑的"],
  "hook_draft": "听到 ComfyUI 就头大？我零基础也跑通了，节点图给你画好。",
  "structure_ref": "畏难钩子 → 节点图拆解 → 我的配置 → 自取",
  "evidence": "86_yt_SebastianKam.md（3.4万字字幕，ComfyUI workflow）",
  "fit_score": 7,
  "fit_dimensions": {"喜欢":4, "擅长":3, "难复制":4, "风口上升":4},
  "urgency": "常青",
  "monetization_role": "引流"
}
```

```json
{
  "id": "T07",
  "topic": "译介内容创作增长教程（Patrick Dang / Wholesale Ted）",
  "title_candidates": ["我做自媒体踩的坑都在这里", "内容涨粉就这3件事", "别瞎更，先看这套增长法"],
  "hook_draft": "更了一堆没人看？我把两个增长大佬的方法揉成自己的了。",
  "structure_ref": "自曝踩坑 → 增长3步 → 我的落地 → 提问CTA",
  "evidence": "92_yt_WholesaleTed.md / 93_yt_PatrickDang.md（副业+内容增长源头）",
  "fit_score": 8,
  "fit_dimensions": {"喜欢":4, "擅长":4, "难复制":4, "风口上升":5},
  "urgency": "常青",
  "monetization_role": "引流"
}
```

```json
{
  "id": "T08",
  "topic": "译介文案写作技巧（Joanna Wiebe 转化文案）",
  "title_candidates": ["文案别自嗨，学这句写法", "我改了标题点击翻倍", "好文案就一个秘密"],
  "hook_draft": "写文案最容易自嗨。我跟转化文案大佬学了一招，立马不一样。",
  "structure_ref": "痛点 → 写法公式 → 前后对比 → 自取",
  "evidence": "91_yt_JoannaWiebe.md（1.4万字字幕，copywriting）",
  "fit_score": 7,
  "fit_dimensions": {"喜欢":4, "擅长":3, "难复制":4, "风口上升":4},
  "urgency": "常青",
  "monetization_role": "引流"
}
```

```json
{
  "id": "T09",
  "topic": "译介副业案例拆解（ModernMillie 17万字字幕）",
  "title_candidates": ["普通人副业就这几种路", "我研究的副业模型长这样", "别信暴富，看真实副业"],
  "hook_draft": "副业帖十篇九篇是割韭菜。我找了个讲真方法的源头拆给你。",
  "structure_ref": "反割韭钩子 → 模型拆解 → 我的判断 → 提问CTA",
  "evidence": "90_yt_ModernMillie.md（17.4万字字幕，side hustle case study）",
  "fit_score": 7,
  "fit_dimensions": {"喜欢":4, "擅长":3, "难复制":4, "风口上升":4},
  "urgency": "常青",
  "monetization_role": "引流"
}
```

```json
{
  "id": "T10",
  "topic": "用 AI Agent 搭内容工作流（自身复盘，引流向）",
  "title_candidates": ["我把内容生产拆成工作流", "AI Agent帮我管素材库", "一周内容我半天搞定"],
  "hook_draft": "别人追一个个工具，我把它们串成了工作流，省下的时间真不少。",
  "structure_ref": "钩子 → 工作流全景 → 哪段最值 → 提问CTA",
  "evidence": "自身 ziliaoku 项目实跑（collect→gate→extract→topics 已通）",
  "fit_score": 8,
  "fit_dimensions": {"喜欢":5, "擅长":5, "难复制":4, "风口上升":4},
  "urgency": "常青",
  "monetization_role": "引流"
}
```

### 信任型（共 6）

```json
{
  "id": "T11",
  "topic": "我踩过的 Claude Code 坑（Reddit 实操 + 自身）",
  "title_candidates": ["Claude Code把我坑惨的3次", "这些Claude Code雷我替你踩了", "别像我一样乱用Agent"],
  "hook_draft": "Claude Code 很强，但用错方式真的会崩。我踩的坑你别再踩。",
  "structure_ref": "自曝翻车 → 3个坑 → 怎么避 → 复盘",
  "evidence": "53_reddit_ClaudeAI.md（2325赞/333评，6个月 hardcore use）+ 自身实跑",
  "fit_score": 9,
  "fit_dimensions": {"喜欢":5, "擅长":5, "难复制":4, "风口上升":4},
  "urgency": "常青",
  "monetization_role": "信任"
}
```

```json
{
  "id": "T12",
  "topic": "半自动发帖工作流完整拆解",
  "title_candidates": ["我的半自动发帖是怎么搭的", "账号安全我握自己手里", "自动化发布我为什么不全交"],
  "hook_draft": "全自动发布听着香，但账号安全不能赌。我把流程拆成半自动。",
  "structure_ref": "认知反差 → 流程节点 → 哪步人工 → 复盘",
  "evidence": "docs/xhs_publish_integration.md（XiaohongshuSkills 半自动已跑通）",
  "fit_score": 8,
  "fit_dimensions": {"喜欢":5, "擅长":5, "难复制":5, "风口上升":4},
  "urgency": "常青",
  "monetization_role": "信任"
}
```

```json
{
  "id": "T13",
  "topic": "译介长图是怎么做的（Pillow 竖版）",
  "title_candidates": ["我的长图是代码画的", "一张图承载全文理解", "不买模板，我用脚本出图"],
  "hook_draft": "别人花几十块买长图模板，我写了段脚本，一次出图随便改。",
  "structure_ref": "钩子 → 脚本思路 → 效果对比 → 自取提示",
  "evidence": "scripts/gen_longimage_reddit.py + gen_longimage_claude_code.py（已验证）",
  "fit_score": 7,
  "fit_dimensions": {"喜欢":4, "擅长":4, "难复制":5, "风口上升":3},
  "urgency": "常青",
  "monetization_role": "信任"
}
```

```json
{
  "id": "T14",
  "topic": "我的选题库是怎么搭的（ziliaoku 复盘）",
  "title_candidates": ["我的选题库长这样", "素材不再散一地", "用git管选题库真香"],
  "hook_draft": "素材东存西存最后吃灰。我把它变成了一个能检索的库。",
  "structure_ref": "痛点 → 库的形态 → 怎么用 → 复盘",
  "evidence": "ziliaoku 项目（raw/gate/extracted/clusters 全链路已通）",
  "fit_score": 7,
  "fit_dimensions": {"喜欢":4, "擅长":4, "难复制":5, "风口上升":3},
  "urgency": "常青",
  "monetization_role": "信任"
}
```

```json
{
  "id": "T15",
  "topic": "采集流水线实跑复盘（一天跑通9段）",
  "title_candidates": ["我的一天内容流水线", "从采集到出稿我咋跑的", "9段流水线我跑给你看"],
  "hook_draft": "采集到出稿听起来长，其实一天能跑完。我把每段交代清楚。",
  "structure_ref": "全景 → 每段耗时 → 哪段最值 → 复盘",
  "evidence": "本链路实跑（collect→gate→extract→cluster→signal→topics）",
  "fit_score": 7,
  "fit_dimensions": {"喜欢":4, "擅长":4, "难复制":5, "风口上升":3},
  "urgency": "常青",
  "monetization_role": "信任"
}
```

```json
{
  "id": "T16",
  "topic": "为什么我不搞全自动（观点文）",
  "title_candidates": ["全自动内容我劝你别碰", "AI跑流程人盯节点", "内容别全交给Agent"],
  "hook_draft": "全网都在喊全自动内容生产，我反而不建议，原因很实在。",
  "structure_ref": "观点直给 → 3个理由 → 我的做法 → 提问",
  "evidence": "自身踩坑 + 半自动实跑结论（账号安全握自己手里）",
  "fit_score": 8,
  "fit_dimensions": {"喜欢":5, "擅长":4, "难复制":4, "风口上升":4},
  "urgency": "常青",
  "monetization_role": "信任"
}
```

### 转化型（共 4，高获得感资源型）

```json
{
  "id": "T17",
  "topic": "Claude Code cheat sheet（/init CLAUDE.md 模板）",
  "title_candidates": ["Claude Code速查表收好", "我的CLAUDE.md模板", "这几个斜杠命令天天用"],
  "hook_draft": "Claude Code 命令太多记不住？我把天天用的整理成一张表。",
  "structure_ref": "钩子 → 清单（命令+场景） → 我的配置 → 自取",
  "evidence": "84_yt_NateHerkAIAu.md（/init /compact /clear /statusline 等）",
  "fit_score": 8,
  "fit_dimensions": {"喜欢":4, "擅长":4, "难复制":5, "风口上升":4},
  "urgency": "常青",
  "monetization_role": "转化"
}
```

```json
{
  "id": "T18",
  "topic": "爆款标题公式清单（可复用模板）",
  "title_candidates": ["20个标题模板直接抄", "标题公式我整理好了", "起名困难症救星清单"],
  "hook_draft": "起标题卡壳？我把能套的公式全列成清单，缺的时候翻。",
  "structure_ref": "钩子 → 公式清单（分类） → 套用示例 → 自取",
  "evidence": "data/titles_pool.jsonl + 20篇 X 样本 + formulas.md",
  "fit_score": 9,
  "fit_dimensions": {"喜欢":5, "擅长":4, "难复制":5, "风口上升":5},
  "urgency": "常青",
  "monetization_role": "转化"
}
```

```json
{
  "id": "T19",
  "topic": "内容工作流 Prompt 模板库",
  "title_candidates": ["我的内容Prompt模板", "工作流Prompt直接抄", "这几个Prompt天天用"],
  "hook_draft": "内容工作流的灵魂是 Prompt。我把跑顺的模板整理出来了。",
  "structure_ref": "钩子 → 模板清单（场景→Prompt） → 用法 → 自取",
  "evidence": "ziliaoku 流水线 9 段技能（gate/extract/cluster/topics 等）",
  "fit_score": 7,
  "fit_dimensions": {"喜欢":4, "擅长":4, "难复制":5, "风口上升":3},
  "urgency": "常青",
  "monetization_role": "转化"
}
```

```json
{
  "id": "T20",
  "topic": "英文源译介 SOP（可复用流程）",
  "title_candidates": ["我是怎么译介英文内容的", "英文好内容搬运的正确姿势", "译介流程我固化了"],
  "hook_draft": "看到好英文内容想分享，但全搬运没灵魂。我固化了一套译介法。",
  "structure_ref": "钩子 → SOP 步骤 → 我的理解怎么加 → 自取",
  "evidence": "模式B译介（draft SKILL）+ 14篇英文YT源头实跑",
  "fit_score": 8,
  "fit_dimensions": {"喜欢":5, "擅长":5, "难复制":5, "风口上升":4},
  "urgency": "常青",
  "monetization_role": "转化"
}
```

## 漏斗配比校验
- 引流：T01–T10 = **10** ✓（目标 10）
- 信任：T11–T16 = **6** ✓（目标 6）
- 转化：T17–T20 = **4** ✓（目标 4）
- 资源型/获得感（冷启动"给"型）：T03/T17/T18/T19/T20 等 ≥5 ✓
- 蹭热点前置：T02（ECC 22万★）标「蹭热点(3天内)」已在前排 ✓

## 周排期（2026-W28，假设已过养号期，稳定更新）

| 星期 | 平台 | 选题ID | 类型 | 套用公式 | 时段 | 备注 |
|---|---|---|---|---|---|---|
| 周一 | 小红书 | T01 | 引流 | 数字型 | 19:30 | Claude Code 32招译介首发 |
| 周二 | 小红书 | T11 | 信任 | 自曝翻车 | 12:30 | 踩坑复盘，建专业感 |
| 周三 | 公众号 | T03 | 引流 | 标题公式 | 21:00 | 标题模板长文 |
| 周四 | 小红书 | T02 | 引流(蹭热点) | 神库盘点 | 19:30 | ECC 22万★ 趁热 |
| 周五 | 小红书 | T18 | 转化 | 清单型 | 12:30 | 标题公式清单（资源型） |
| 周六 | 小红书 | T16 | 信任 | 观点反差 | 21:00 | 为什么不全自动 |
| 周日 | 公众号 | T20 | 转化 | SOP型 | 19:30 | 译介SOP，种草订阅 |

约束核对：小红书本周 5 篇（3-4 偏上，可接受）；同平台间隔 ≥48h ✓；转化型(T18/T20)不连续 ✓；养号期若未过则压缩到 ≤3 篇/周且不挂外链不提私域。

> 排期只是建议，最终发布由你终审拍板。
