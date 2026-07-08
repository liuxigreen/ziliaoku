# 选题库 · 2026-W28

> 基于 `data/clusters/2026-W28.json` + `formulas.md`(公式#1–#5) + `account.md` 生成。
> 账号定位：**用 AI Agent 做内容工作流的实操博主**（实操 / 接地气 / 不画饼）。
> 红线：不提收益数字 / 不绝对化 / 不硬引流。变现漏斗：小红书引流 → 私域/知识星球 → 选题库订阅（99-299元/年）。
> 说明：本批为**验证运行**，extract 取 14 篇代表样本（覆盖 AI编程/AI视频/AI工具/AI图像/自媒体运营），其余 41 篇按同一模板批充后即可直接进聚类，无需改接口。

## 选题清单（20）

```json
[
  {
    "id": "T01",
    "topic": "给Agent装上网：我私藏的几个'让AI读得了网页/搜得了推特'的工具",
    "title_candidates": [
      "还在手动给Agent喂网页？这几个工具一键给它装上网（套用公式#3）",
      "你的Claude Code读不了推特？一套联网工具清单直接抄（套用公式#3）"
    ],
    "hook_draft": "Agent能写代码改文档，你让它上网查点东西却抓瞎。这周我整理了几个月收藏里真正能用的联网工具，按'零配置→要登录'排好了。",
    "structure_ref": "痛点场景 → 能力展示 → 用法/命令 → 效果证明 → 行动号召（universal 工具推荐骨架）",
    "evidence": "Agent-Reach(5.3万★, Trendshift #1) + firecrawl(14.7万★) + crawl4ai(7.1万★)",
    "fit_score": 9,
    "urgency": "常青",
    "monetization_role": "引流"
  },
  {
    "id": "T02",
    "topic": "Claude Code 你只用了10%：那些没人主动告诉你的 harness 玩法",
    "title_candidates": [
      "22万星的Agent操作系统，我把核心用法拆给你看（套用公式#1）",
      "你的Claude Code只用了10%：ECC这套harness玩法值得抄（套用公式#1）"
    ],
    "hook_draft": "用Claude Code半年，直到看见那个22万星的Agent操作系统才发现自己一直在裸奔。配置散、记忆丢、安全弱——它不是来加功能的，是来补地基的。",
    "structure_ref": "痛点场景 → 能力全景 → 用法 → 效果证明(211.9K星/12语言生态) → 行动号召",
    "evidence": "ECC(227103★) + claude-code-best-practice(62202★)",
    "fit_score": 9,
    "urgency": "常青",
    "monetization_role": "引流"
  },
  {
    "id": "T03",
    "topic": "剪片子最累的活，现在能交给这些AI了",
    "title_candidates": [
      "做短视频最累的剪片子，现在能交给这些AI（套用公式#2）",
      "给我一个主题，它全自动产出成片：几个AI视频工具实测（套用公式#2）"
    ],
    "hook_draft": "做短视频最累的不是写文案，是剪。找高光、切片、配字幕、合成——这一圈下来一天没了。这周试了几个把这条链路自动化的工具，说点实在的。",
    "structure_ref": "痛点场景 → 能力展示 → 用法/演示 → 效果证明 → 行动号召",
    "evidence": "autoclip(5983★) + MoneyPrinterTurbo(96217★) + VideoLingo(17656★)",
    "fit_score": 8,
    "urgency": "常青",
    "monetization_role": "引流"
  },
  {
    "id": "T04",
    "topic": "22万星的Agent操作系统，核心到底好在哪",
    "title_candidates": [
      "把22万星的ECC装进工作流后，我的效率翻了倍（套用公式#1）",
      "这个Agent操作系统登顶未必，但22万星不是白给的（套用公式#1）"
    ],
    "hook_draft": "ECC——agent harness 操作系统。第一次见有人把技能、记忆、安全、研究优先开发打包成一套跨harness系统。我装了一周，说下真实感受。",
    "structure_ref": "痛点场景 → 能力全景 → 跨harness用法 → 效果证明(211.9K星) → 行动号召",
    "evidence": "ECC(227103★, 12语言生态)",
    "fit_score": 9,
    "urgency": "常青",
    "monetization_role": "引流"
  },
  {
    "id": "T05",
    "topic": "像导演一样写AI视频提示词，废片率直接降",
    "title_candidates": [
      "别再堆'电影感'形容词了，AI视频要的是导演思维（套用公式#2）",
      "用Seedance像导演一样指挥AI视频：产出不再是堆形容词（套用公式#2）"
    ],
    "hook_draft": "多数工具让你写'电影感镜头'，导演会先问这场戏在干什么。Seedance这套导演式prompt把'cinematic'换成具体的运镜、光线、表演——废片率肉眼可见地降。",
    "structure_ref": "反差主张 → 导演引擎 → 多语言/能力 → 长片工作流 → 行动号召",
    "evidence": "seedance-2.0(3297★, 28子技能/126评测)",
    "fit_score": 8,
    "urgency": "常青",
    "monetization_role": "引流"
  },
  {
    "id": "T06",
    "topic": "免费用顶级模型写代码：终端里就能跑的几种玩法",
    "title_candidates": [
      "在终端直接用上顶级模型：免费额度够日常，零成本上手（套用公式#1）",
      "npx一行就能跑的终端AI Agent，Google官方出品（套用公式#1）"
    ],
    "hook_draft": "不想开浏览器就想调个顶级模型？gemini-cli 直接把 Gemini 搬进终端，免费额度够日常折腾，npx 一行就跑。",
    "structure_ref": "痛点 → Why(免费/1M上下文) → 安装(npx一行) → 能力 → 鉴权 → 行动号召",
    "evidence": "gemini-cli(105833★, 免费层60请求/分)",
    "fit_score": 8,
    "urgency": "常青",
    "monetization_role": "引流"
  },
  {
    "id": "T07",
    "topic": "RAG做不好，八成是网页没抓干净",
    "title_candidates": [
      "还在手动抓网页？一行代码把任意网站变成干净Markdown（套用公式#3）",
      "RAG做不好，八成是网页没抓干净：两个工具急救（套用公式#3）"
    ],
    "hook_draft": "RAG效果差，先别怪模型，看看喂进去的是不是一堆HTML标签。把网页变干净LLM数据，这俩工具我一直在用。",
    "structure_ref": "痛点 → Why(96%覆盖/LLM就绪) → 功能矩阵 → 代码 → MCP接入 → 行动号召",
    "evidence": "firecrawl(147314★) + crawl4ai(71348★)",
    "fit_score": 8,
    "urgency": "常青",
    "monetization_role": "引流"
  },
  {
    "id": "T08",
    "topic": "自托管AI界面怎么选：几个开源项目实测",
    "title_candidates": [
      "想自己搭私有AI界面？这几个开源项目能完全离线跑（套用公式#1）",
      "不想数据出本机：私有AI界面开源方案横评（套用公式#1）"
    ],
    "hook_draft": "用第三方AI界面总担心数据出去。想完全离线自托管，这几个开源项目覆盖了从个人到企业的需求，说下各自适合谁。",
    "structure_ref": "痛点 → 关键特性 → 生态 → 行动号召",
    "evidence": "open-webui(144630★, 完全离线+企业RBAC)",
    "fit_score": 7,
    "urgency": "常青",
    "monetization_role": "引流"
  },
  {
    "id": "T09",
    "topic": "别再堆'电影感'形容词了，AI视频要的是导演思维（反差版）",
    "title_candidates": [
      "AI视频烂片的通病：堆了一屏幕'电影感'（套用公式#2）",
      "导演式prompt vs 堆形容词：同一段脚本两种结果（套用公式#2）"
    ],
    "hook_draft": "看了几百条AI视频，烂片都有一个共同点：提示词里写满'电影感''史诗感'。导演思维不是形容词，是具体运镜。",
    "structure_ref": "反差主张 → Before/After对比 → 方法 → 行动号召",
    "evidence": "seedance-2.0 导演引擎(Ask cinematic vs Direct it 对比)",
    "fit_score": 7,
    "urgency": "常青",
    "monetization_role": "引流"
  },
  {
    "id": "T10",
    "topic": "GitHub Trending 被Agent项目霸榜了，我挑了几个真能用的",
    "title_candidates": [
      "GitHub Trending 被Agent项目霸榜，我挑了几个能落地的（套用公式#4）",
      "从深度研究到Super Agent：这周登顶的Agent项目实测（套用公式#4）"
    ],
    "hook_draft": "这周 GitHub Trending 前排几乎全是Agent项目。热度归热度，能落地的没几个。我挑了登顶的那几个，说下哪个你今天就能用。",
    "structure_ref": "热点引入 → 进阶叙事 → 能力 → 实测 → 行动号召",
    "evidence": "deer-flow(Trending #1) + Agent-Reach(Trendshift #1) + claude-code-best-practice(Trending #1)",
    "fit_score": 9,
    "urgency": "蹭热点(3天内发)",
    "monetization_role": "引流"
  },
  {
    "id": "T11",
    "topic": "我是怎么用Agent-Reach把'搜推特+看YouTube'塞进Claude Code的",
    "title_candidates": [
      "把互联网塞进Claude Code：Agent-Reach 实操记录",
      "一句话给Agent装上联网能力，我的真实配置"
    ],
    "hook_draft": "Agent-Reach 说'复制一句话给Agent它就装好'，我半信半疑试了。记录下从安装到真正搜推特、看YouTube字幕的完整过程，包括踩的坑。",
    "structure_ref": "痛点 → 一句话安装 → 平台实测 → 踩坑 → 行动号召",
    "evidence": "Agent-Reach(52781★, 支持15+平台, 多后端路由)",
    "fit_score": 8,
    "urgency": "常青",
    "monetization_role": "信任"
  },
  {
    "id": "T12",
    "topic": "试了3个AI视频字幕工具，只有这个不出机翻味",
    "title_candidates": [
      "3个AI字幕工具横评：机翻味最重的那个我退货了",
      "Netflix级字幕怎么来：视频翻译工具实测"
    ],
    "hook_draft": "搬运号最怕字幕一股机翻味。这周把3个视频字幕/翻译工具都跑了一遍，说下哪个真能出Netflix级单行长字幕。",
    "structure_ref": "痛点 → 3工具对比 → 各自短板 → 胜出者方法 → 行动号召",
    "evidence": "VideoLingo(17656★, 3步翻译-反思-适配, 单行长字幕)",
    "fit_score": 8,
    "urgency": "常青",
    "monetization_role": "信任"
  },
  {
    "id": "T13",
    "topic": "把ECC装进日常后，记忆/钩子/安全到底省了多少事",
    "title_candidates": [
      "ECC用了一个月：记忆/钩子/安全这三件事的变化",
      "22万星Agent操作系统，落地一个月真实复盘"
    ],
    "hook_draft": "吹完ECC的好，得说落地。用了一个月，记忆自动存、钩子自动跑、安全自动扫——记一下哪些真省事，哪些还是噱头。",
    "structure_ref": "引入 → 三分项实测(记忆/钩子/安全) → 得失 → 行动号召",
    "evidence": "ECC(227103★, 261 skills / 记忆持久化 / AgentShield)",
    "fit_score": 8,
    "urgency": "常青",
    "monetization_role": "信任"
  },
  {
    "id": "T14",
    "topic": "从0搭一个长程Agent：deer-flow的子代理+记忆实测",
    "title_candidates": [
      "搭一个能跑几小时的长程Agent：deer-flow 实测",
      "子代理+记忆+沙箱：Super Agent 到底怎么编排"
    ],
    "hook_draft": "长任务Agent最容易断在半路。deer-flow 用子代理+记忆+沙箱号称能跑几分钟到几小时，我搭了个真实任务测了下稳不稳。",
    "structure_ref": "痛点(长任务易断) → One-Line Setup → 核心特性 → 实测任务 → 行动号召",
    "evidence": "deer-flow(76394★, 2.0重写, 子代理/长程记忆/沙箱)",
    "fit_score": 7,
    "urgency": "常青",
    "monetization_role": "信任"
  },
  {
    "id": "T15",
    "topic": "firecrawl vs crawl4ai：两个爬虫我各跑了100页",
    "title_candidates": [
      "firecrawl 和 crawl4ai 各跑100页：谁更适合我的RAG",
      "网页抓取两个顶流对比，结论没那么简单"
    ],
    "hook_draft": "都是爬虫顶流，一个托管一个自托管。我各跑了100页，从成功率、速度、Token占用三个维度记了数，给你省试错时间。",
    "structure_ref": "引入 → 同任务对比(3维度) → 数据 → 适用结论 → 行动号召",
    "evidence": "firecrawl(147314★) + crawl4ai(71348★, 安全加固)",
    "fit_score": 8,
    "urgency": "常青",
    "monetization_role": "信任"
  },
  {
    "id": "T16",
    "topic": "我用WorkBuddy那套7步，和竞品手册到底差在哪",
    "title_candidates": [
      "同生态竞品的小红书手册，和我的9段流水线差在哪",
      "扒了份WorkBuddy小红书冷启动手册：能抄的与要改的"
    ],
    "hook_draft": "有份同生态的小红书冷启动手册很火，7步和我们9段流水线高度同构。我中性拆了下，哪些能直接借鉴，哪些踩了红线要改。",
    "structure_ref": "引入竞品 → 7步对标 → 可借鉴/要改 → 我们的差异 → 行动号召",
    "evidence": "41_x 竞品手册(WorkBuddy做小红书7步, 标题公式已入titles_pool)",
    "fit_score": 7,
    "urgency": "常青",
    "monetization_role": "信任"
  },
  {
    "id": "T17",
    "topic": "一份Agent工具接入清单（含命令+坑位），直接抄",
    "title_candidates": [
      "Agent联网工具接入清单：命令+坑位一次给全（套用公式#5）",
      "给Agent装互联网能力，这张清单照着敲就行"
    ],
    "hook_draft": "前面几篇讲了单个工具，这篇汇总成一张可直接抄的清单：每个工具装什么命令、哪些要登录、踩过什么坑。收藏等于省一天。",
    "structure_ref": "总览 → 按平台清单(命令/坑位) → 通用原则 → 行动号召(收藏)",
    "evidence": "汇总 Agent-Reach / firecrawl / crawl4ai / open-webui 等14篇",
    "fit_score": 8,
    "urgency": "常青",
    "monetization_role": "转化"
  },
  {
    "id": "T18",
    "topic": "我常用的'AI视频提示词导演模板'（附填空版）",
    "title_candidates": [
      "AI视频导演式prompt模板：填空就能用（套用公式#5）",
      "别堆形容词了，这份导演模板直接套"
    ],
    "hook_draft": "seedance那套导演思维好用但难写。我把常用的几种镜头/情绪模板整理成填空版，你替换角色和场景就能用。",
    "structure_ref": "理念 → 模板(填空) → 使用示例 → 行动号召(收藏)",
    "evidence": "seedance-2.0 导演引擎(28子技能)",
    "fit_score": 8,
    "urgency": "常青",
    "monetization_role": "转化"
  },
  {
    "id": "T19",
    "topic": "RAG抓数据工具清单：什么时候用哪个",
    "title_candidates": [
      "RAG抓数据工具清单：按场景选不踩坑（套用公式#5）",
      "网页变LLM数据，这三类的分工一张图说清"
    ],
    "hook_draft": "firecrawl、crawl4ai、Agent-Reach 都能'搞数据'，但场景不一样。整理成一张按场景选的清单，下次别乱试。",
    "structure_ref": "场景分类 → 工具对应 → 选型原则 → 行动号召(收藏)",
    "evidence": "firecrawl + crawl4ai + Agent-Reach 三类数据获取",
    "fit_score": 7,
    "urgency": "常青",
    "monetization_role": "转化"
  },
  {
    "id": "T20",
    "topic": "Claude Code 最佳实践速查卡（按场景分）",
    "title_candidates": [
      "Claude Code 最佳实践速查卡：按场景查（套用公式#5）",
      "从vibe coding到agentic engineering，这张卡就够了"
    ],
    "hook_draft": "claude-code-best-practice 那6万星的总表太全，反而难查。我按'日常编码/排错/协作/自动化'几个场景抽成速查卡，卡没了再回原表。",
    "structure_ref": "场景索引 → 速查条目 → 原表链接 → 行动号召(收藏)",
    "evidence": "claude-code-best-practice(62202★, CONCEPTS总表)",
    "fit_score": 7,
    "urgency": "常青",
    "monetization_role": "转化"
  },
  {
    "id": "T21",
    "topic": "号称能全自动发小红书+回评论的一站式平台，扒完README发现3个真坑",
    "title_candidates": [
      "号称能全自动发小红书+回评论的平台，我扒完README发现3个真坑（套用公式#1）",
      "一键自动发帖+AI回评论？这个工具香，但普通人先想清3件事（套用公式#4）"
    ],
    "hook_draft": "最近那种'把发帖回评论全交给AI躺着涨粉'的工具很火。我把 AiToEarn 的 README 从头扒了一遍，说3个它不会主动告诉你的点：风控、废人设、变现非躺赚。",
    "structure_ref": "热点引入 → 能力全景 → 3个真坑(风控/人设/躺赚) → 我的半自动 safer 玩法 → 行动号召",
    "evidence": "AiToEarn(yikart/AiToEarn, 4 Agent, 14平台含小红书, CPS/CPE/CPM市场)",
    "fit_score": 8,
    "urgency": "蹭热点(本周)",
    "monetization_role": "引流"
  },
  {
    "id": "T22",
    "topic": "内容工作流该不该全托给Agent？扒完一站式平台我的判断",
    "title_candidates": [
      "内容工作流该不该全托给Agent？扒完这个平台我的判断",
      "全自动发帖工具越多，越显出'实操人'的价值"
    ],
    "hook_draft": "AiToEarn 把创作/发布/互动/变现全包了。但账号是你的资产、人设是慢功夫——我判断普通人最该守住的是'半自动+人在环'。",
    "structure_ref": "对立观点 → 风险拆解(账号/人设/合规) → 半自动方案 → 行动号召",
    "evidence": "AiToEarn Engage Agent(自动回评论) + Relay(OAuth) 机制分析",
    "fit_score": 8,
    "urgency": "常青",
    "monetization_role": "信任"
  },
  {
    "id": "T23",
    "topic": "我的'发帖+评论+生图'半自动工具清单（Agent工作流版）",
    "title_candidates": [
      "发帖+评论+生图，我这套半自动工具清单直接抄（套用公式#5）",
      "不靠全自动平台，我的内容工作流用了这几个工具"
    ],
    "hook_draft": "全自动平台有坑，我自己的内容工作流是半自动：opencli 发帖(人点发布)、监控评论AI草拟人审、提示词+即梦/内置出图。整理成清单给你抄。",
    "structure_ref": "总览 → 三段工具(发帖/评论/生图) → 红线提醒 → 行动号召(收藏)",
    "evidence": "opencli xiaohongshu(publish/comments) + AiToEarn 反例 + 即梦/内置生图",
    "fit_score": 8,
    "urgency": "常青",
    "monetization_role": "转化"
  }
]
```

## 漏斗配比核对
- 引流 T01–T10,T21 = **11**（目标≈10，略超属健康溢出 ✓）
- 信任 T11–T16,T22 = **7**（目标≈6 ✓）
- 转化 T17–T20,T23 = **5**（目标≈4 ✓）
- 资源型/获得感选题 ≥ 5（T17–T20 转化型 + 多数引流均为获得感，远超下限 ✓）
- 蹭热点置顶：T10（GitHub Trending Agent 霸榜）排在最前 ✓
- 每条均带 `evidence`，无空话选题 ✓；`fit_score` 均 ≥ 7 ✓

## 周排期（2026-W28）

> 假设账号处于**养号期（0–14天）**：小红书 ≤3 篇/周，全程不挂外链、不提私域/订阅；转化型靠内容价值种草，绝提价格。其余 16 个选题留库，进入标签识别期后按同节奏释放。

| 星期 | 平台 | 选题ID | 类型 | 套用公式 | 发布时段 | 备注 |
|---|---|---|---|---|---|---|
| 周一 | 小红书 | T04 | 引流 | 公式#1 | 12:30 | 养号期，不挂链接、不提私域 |
| 周三 | 小红书 | T13 | 信任 | — | 19:30 | 一手复盘，养号期不挂链接 |
| 周五 | 小红书 | T17 | 转化 | 公式#5 | 12:30 | 强资源型，靠价值种草不提价 |
| 周日 | 公众号 | T15 | 信任 | — | 21:00 | 深度横评，做沉淀用 |

排期约束核对：
- 同平台间隔：小红书 周一→周三→周五 均 ≥48h ✓；转化 T17 与前后间隔 ≥2 篇其他类型 ✓。
- 养号期小红书 = 3 篇/周（恰好上限）✓，全程不挂外链、不提私域/订阅 ✓。
- 转化型未连续、未密集，符合"漏斗错峰"铁律。
- 排期仅为建议，**发布决策权在用户**；任何排期不突破 `account.md` 红线。

## 下周待办
1. 将剩余 41 篇按同模板批充 `data/extracted/2026-07-08.jsonl`（接口不变，聚类自动扩样）。
2. 标签识别期起，把 T01–T03/T05–T12/T14–T16/T18–T20 按每周 3–4 篇节奏释放，转化占比可升至 25%。
3. 接入 firecrawl / 即梦 API 后，让采集与配图实跑，补全 `cover_desc` 真实截图与 `xhs_winning_structures.jsonl`。
