# -*- coding: utf-8 -*-
"""awesome-llm-apps 公众号深度稿 → 摸鱼绿排版 HTML 生成器（复用 gzh_style）。
输出: gzh_ecc/awesome_gzh_排版_摸鱼绿(moyu-green).html
再跑 make_preview.py 包成 _预览.html 即可获得"复制到公众号"链接。
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gzh_style import (leaf, leaf_br, q, rich, para, small, hack, build_hacks,
                       chapter, build_cover, build_toc, build_intro, build_preamble,
                       build_opinions, build_checklist, build_outro, build_sign,
                       bullets, FONT)

COVER = {
    'tag': 'AI 实操 · 工具译介',
    't1': '别再从头造轮子',
    't2': '100+ 能直接跑的 AI 应用模板',
    'sub': 'GitHub 11.7万星 awesome-llm-apps · 译介+落地',
    'src': 'GitHub | awesome-llm-apps',
    'tag_a': 'AI 应用', 'tag_b': '开源词典',
}
PARTS = [
    ('01', '它是什么', '一个开源轮子词典', 'WHAT'),
    ('03', '覆盖远不止Agent', '六类应用怎么选', 'SCOPE'),
    ('04', '我的落地', '三个真跑通的模板', 'HOW'),
]
INTRO_LEAD = '最贵的不是更聪明的模型，是现成的轮子'

PREAMBLE = [
    '你是不是也有过这种时刻：想给工作流加个 AI 小工具，结果一半时间花在配环境、查文档、调 API 上，真正写业务逻辑反而没几下。',
    '我前几天在 GitHub 上把 awesome-llm-apps 翻完了——11.7 万星，不是那种「标题吓人、点进去只有个 README」的水库，而是真的把 100+ 个「能直接跑」的 AI 应用模板，收成了一个开源词典。',
    '今天这篇不是帮你「云收藏」，而是说清楚：它到底是什么、为什么我敢说它不画饼、以及我自己的三个真实用法和踩过的坑。',
]

WHAT = [
    '一句话：它把「别人已经踩平过的 AI 应用脚手架」收集起来，你 clone 下来、装好依赖、跑起来，就有真东西，而不是一段伪代码。',
    '它和那些「AI 教程合集」最大的区别是颗粒度。一个典型的模板不是一篇博客，而是一个能跑的小项目：',
]
WHAT_BULLETS = [
    '一个 app.py（或 main.py）主程序；',
    '一个干净的 requirements.txt；',
    '一个 .env.example 告诉你该填哪些 key；',
    '一篇 README 讲清楚「这条能干什么、怎么改」。',
]

WHY = [
    '市面上讲 AI 应用的内容太多了，但我愿意信这个，是因为它有几条硬标准：',
]
WHY_BULLETS = [
    '**手写而非简单搬运**：每个模板都是作者原创、端到端测过才放出来，不是从别处扒一段拼起来的。',
    '**三条命令能跑**：没有坏掉的依赖、没有「剩下的你自己搞」，基本是 git clone → pip install → python app.py。',
    '**覆盖现代技术栈**：AI Agents、常驻 Agent、多智能体、MCP、语音、RAG、Agent Skills、微调。',
    '**厂商无关**：换 Claude / Gemini / GPT / Qwen，改个配置就行，不被绑死在某一家。',
    '**Apache-2.0 协议**：能 fork、能商用，没有墙、没有 telemetry 偷偷上报。',
]

SCOPE_INTRO = '很多人一听「AI 应用」就自动联想到「写自动化脚本的 Agent」。其实这个合集里，Agent 只是其中一类。我按用途给它分了个类，你看看哪类戳中你：'
SCOPE_BULLETS = [
    '**RAG 类**：给公司文档、个人笔记接个问答机器人。适合「资料太多、每次找东西都翻半天」的人。',
    '**语音类**：实时口播、电话 Intake、会议转写。适合做客服、销售、内容二次创作的人。',
    '**MCP 类**：让模型调起各种外部工具（查数据库、发消息、跑脚本）。适合想把一堆 SaaS 串起来的人。',
    '**数据分析类**：丢一个 Excel / CSV 进去，出分析和图表。适合每周做报表的打工人。',
    '**入门类**：Prompt 工程、Generative AI 从零学。适合刚进场、不想一上来就被框架劝退的人。',
    '**微调类**：用自己的数据训个小模型。适合有专有数据、想做差异化的人。',
]

HACKS = [
    ('1', 'always-on agent（常驻监控 Agent）',
     '原版是监控 Hacker News 新帖。我把它改成监控公众号 / 小红书热榜，抓取源换两行、调度逻辑改改，半天跑通——比从零写省一周。',
     '监控源换成自己的阵地，调度一改就上岗，不用重造。'),
    ('2', 'AI 数据分析 Agent',
     '客户要个「丢 Excel 出分析」的小工具。我直接拿模板，把前端改成上传按钮、分析 prompt 换成客户业务口径，当天交付。',
     '业务口径一换，通用模板变专属工具。'),
    ('3', 'RAG over 个人笔记',
     '把我自己的选题库做成可问答的知识库——问它「上个月我记过哪些 MCP 灵感」，它直接翻出来。等于给记忆装了个检索层。',
     '选题库从「存着」变「能问」，灵感不再沉底。'),
]

PICK = [
    ('1', '想痛点，别想技术',
     '你这周最痛的一个重复任务是什么？先想痛点，再想技术。',
     '从痛点出发，才不会挑最火却用不上的。'),
    ('2', '对分类表',
     '它在合集里属于哪一类？对照上面那张分类表定位。',
     '先定位再动手，省得在 100+ 里瞎翻。'),
    ('3', '挑那个，不挑最火的',
     '挑那个，不挑热门。热门很多人抄，但和你实际痛点未必贴。',
     '一个跑通，比收藏一整个仓库有用。'),
]

PITS = [
    '**贪多**：一开始把整个库 clone，环境互相打架、Python 版本乱套。现在纪律：一次只拉 1 个，跑通再说。',
    '**一上来改架构**：原版没跑通就大改，出问题分不清谁的锅。先 python app.py 跑一遍确认环境 OK，再动业务。',
    '**忽视 key 管理**：早期把 API key 写死在代码里，换机器、传仓库差点泄露。现在一律 .env + .env.example，密钥不进版本库。',
]

WASTE = [
    '收藏 ≠ 会用。我自己的做法：每周挑 1 个模板，跑通之后写一句话——「它能省我什么」，存进我的选题库。半年下来，这就是一个只属于我的「可复用轮子清单」。',
]

OUTRO = [
    '如果你也常卡在「想做但懒得从零搭」，建议把这份词典存好。下次灵光一现，先来翻翻有没有现成轮子，比从头造要快十倍。',
    '我平时会在小红书同步这类「能跑的 AI 实操」，从选题到落地都讲，感兴趣可以去逛逛。这篇是公众号的深读版，想要更短更碎的，去小红书看。',
]

SIGN_NAME = '小木'
SIGN_DESC = '用 AI 把内容工作流跑起来。译介英文一手好文，讲人话的落地理解，不画饼。'

def main():
    blocks = []
    blocks.append(build_cover(COVER))
    blocks.append(build_toc(PARTS))
    blocks.append(build_intro(INTRO_LEAD))
    blocks.append(build_preamble(PREAMBLE))

    blocks.append(chapter('01', '它是什么：开源轮子词典', 'WHAT'))
    blocks.append(build_preamble(WHAT))
    blocks.append(bullets(WHAT_BULLETS))

    blocks.append(chapter('02', '为什么我说它不画饼', 'WHY'))
    blocks.append(build_preamble(WHY))
    blocks.append(bullets(WHY_BULLETS))

    blocks.append(chapter('03', '覆盖远不止 Agent', 'SCOPE'))
    blocks.append(para(SCOPE_INTRO))
    blocks.append(bullets(SCOPE_BULLETS))

    blocks.append(chapter('04', '我的落地：三个真跑通的模板', 'HOW'))
    blocks.append(build_hacks('三个我私藏、真跑通的模板', HACKS))
    blocks.append(build_hacks('新手怎么挑第一个（决策思路）', PICK))

    blocks.append(chapter('05', '避坑 + 怎么用不浪费', 'NOTES'))
    blocks.append(build_checklist('避坑：我踩过的 3 个坑', PITS, '这三条，我每条都交过学费。'))
    blocks.append(build_opinions('怎么用才不浪费', WASTE))

    blocks.append(build_outro(OUTRO))
    blocks.append(build_sign(SIGN_NAME, SIGN_DESC))

    html = ('<section style="max-width:677px;margin:0 auto;background:#ffffff;'
            + FONT +
            'color:#374151;line-height:1.75;letter-spacing:0.5px;overflow-x:hidden;">\n\n'
            + '\n\n'.join(blocks) +
            '\n</section>\n')
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       'awesome_gzh_排版_摸鱼绿(moyu-green).html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print('WROTE', out, len(html), 'bytes')

if __name__ == '__main__':
    main()
