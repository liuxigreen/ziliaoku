# -*- coding: utf-8 -*-
"""RSS + AI 摘要 一手信息源 · 公众号深读版 → 摸鱼绿排版 HTML 生成器（复用 gzh_style）。
输出: output/posts/2026-07-16/rss_ai_daily_brief/gzh_assets/rss_ai_daily_brief_wechat_排版_摸鱼绿(moyu-green).html
再跑 make_preview.py 包成 _预览.html。
"""
import os, sys
sys.path.insert(0, 'D:/WorkBuddyProjects/ziliaoku/scripts/gzh_publish')
from gzh_style import (leaf, leaf_br, q, rich, para, small,
                       chapter, build_cover, build_toc, build_intro, build_preamble,
                       build_opinions, build_outro, build_sign,
                       bullets, build_checklist, FONT)

OUT_DIR = 'D:/WorkBuddyProjects/ziliaoku/output/posts/2026-07-16/rss_ai_daily_brief/gzh_assets'

COVER = {
    'tag': 'AI 工作流 · 译介实测',
    't1': '别被算法投喂了',
    't2': '搭个一手信息源',
    'sub': '用 RSS + AI 摘要，把看什么的选择权从算法手里夺回来',
    'src': '跑一周真实复盘',
    'tag_a': 'RSS', 'tag_b': 'AI摘要',
}
PARTS = [
    ('01', '为什么做', '我的信息痛点', 'WHY'),
    ('02', '怎么搭', '最小可行版', 'HOW'),
    ('03', '真收益', '跑一周的 3 个好处', 'GAINS'),
    ('04', '反直觉坑', '3 个踩坑实录', 'PITFALLS'),
    ('05', '可抄配置', '最低配置 30 分钟跑通', 'SETUP'),
    ('06', '落地判断', '谁适合谁不适合', 'VERDICT'),
]
INTRO_LEAD = '你每天刷的 AI 资讯，90% 是别人嚼过的二手解读。'

PREAMBLE = [
    '我前阵子认真数了一下：刷 30 分钟，真正来自一手信源（英文博客、论文、GitHub Release、创业者推特）的内容不到 10%。剩下 90% 是中文转载、情绪标题、或者别人嚼完再喂给你的“总结”。不是不能看，但看多了会有一个错觉——你以为自己在追前沿，其实只是在追别人的情绪。',
    '老外用 RSS + LLM 做“个人日报”这套 workflow 已经流行一阵了。原理不复杂：把你真正想追的源汇总到一个阅读器，再用 AI 每天自动摘要、翻译、推送。我 replicate 了一遍，跑了一周，发现它确实能省时间，但也确实有几个反直觉的坑。这篇把我怎么搭的、踩了什么坑、值不值得你抄，全部摊开讲。',
]

WHY_INTRO = '我的核心痛点不是“信息少”，而是“信息太多、太碎、太二手”。作为靠 AI 工具做内容工作流的人，我需要同时盯着几类信号：新出的 AI 工具 / 开源项目；海外博主对某个工具的真实实测；学界 / 工业界的新论文、新框架；偶尔还要看几篇高质量的英文长文，判断能不能落地成选题。'
WHY_PAIN = [
    '过去我的方式是：打开社交平台、即刻、Twitter、公众号、邮件列表，每个 App 看一遍。',
    '问题是推荐流会无限喂新东西，我的时间不是花在看“重要信息”上，而是花在“抵抗算法”上。',
    '更麻烦的是，很多信息已经被中文自媒体转了几手，标题党和过度解读混在一起，我得自己回原文核对。',
]
WHY_CLOSE = 'RSS + AI 摘要这个 workflow 吸引我的地方，不是它多高级，而是它把“看什么”的主动权从算法手里夺回来。你自己决定订阅谁，AI 只负责帮你压缩阅读量。'

HOW_INTRO = '我没有一上来搞复杂系统，而是先搭了一个“能跑 7 天不出错”的最小版。核心是三条链路：'
HOW = [
    '**选源：只放你真正会回头看原文的源**。RSS 最大的坑是“源没选好，后面全是垃圾”。我一开始为了“多覆盖”，把几十个营销号、科技媒体也塞了进去，结果 AI 摘要每天给我推一堆“马斯克又发推了”“OpenAI 下周要发新模型”这种没有信息量的东西。后来我砍到只剩三类：海外个人博主 / 独立开发者的博客；开源项目 Release Note / GitHub 讨论区；几个我信得过的技术媒体。源的数量控制在 10 个以内。',
    '**抓全文：让 AI 有东西可摘要**。很多 RSS 源只输出摘要，AI 拿到 100 字摘要再去总结，等于“二手的二手”。我用的方式是把 RSS 项的原文链接丢给 AI，让 AI 读完整网页再出摘要。这步会多花一点时间，但摘要质量差很多。',
    '**推送：每天一次，不要实时刷屏**。我的设置是每天上午 10 点推一次汇总，包含标题 + 一句话摘要、哪些值得点进去看原文（标“必读”）、哪些是“知道就行”的背景信息、自动归类到“工具 / 论文 / 观点 / 新闻”四个标签。推送到我的笔记软件里，一天只处理一次，不会被打断。',
]

GAINS_INTRO = '跑了一周，先说 3 个真收益。'
GAINS = [
    '**省时间**：以前我早上会不由自主刷半小时各个 App。现在我知道 10 点有一份汇总，刷 App 的冲动明显下降。不是说我完全不刷了，但“主动查”和“被动喂”消耗的心力完全不一样。',
    '**不会漏掉重要的一手信息**：有一篇海外博主写的 Claude Code 实测，我如果看中文圈至少要晚 3-5 天才能看到。RSS 里当天就抓到了，第二天我就在自己的选题库里做了标记。这种“信息差”在长期来看是复利。',
    '**逼自己明确“什么值得追”**：订阅源的过程，其实是把自己关注范围显式化的过程。你不能再说“我关注 AI 前沿”，你必须列出：我关注哪几个人的博客？哪几个项目的 Release？哪几个细分领域？这个过程本身就有价值。',
]

PITFALLS_INTRO = '再说 3 个反直觉的坑。'
PITFALLS = [
    '**AI 摘要会“看起来懂，其实漏了关键”**。AI 很会写那种“这段讲了……”的摘要，但有时会漏掉关键限制条件。比如一篇讲“新模型在某基准上提升 20%”的文章，AI 摘要可能根本不提“这个基准是作者自己做的”或者“只测了英文”。如果你只读摘要，会做出错误判断。我的对策：摘要只用来决定“要不要看原文”，凡是涉及结论、数字、能不能落地的，必须点原文。',
    '**源不维护，信息流就会慢性死亡**。有些博客几个月不更新，有些博主从写技术转向做营销，有些源突然停止 RSS 输出。如果你不定期清理，列表会越来越臃肿。我第一周就花了 10 分钟删掉 3 个已经变质的源。所以这套 workflow 不是“搭完就自动跑”，而是每周要维护 5-10 分钟。',
    '**不要指望 AI 替你“选题”**。AI 能帮你发现信息，但“这个选题适不适合我”这件事，AI 判断不了。它不知道我的账号定位、我的读者画像、我能不能 replicate。选题决策仍然要人来做。',
]

SETUP_INTRO = '如果你也想 replicate，别一上来搞复杂系统。下面这个最小配置，30 分钟能跑通：'
SETUP = [
    'RSS 阅读器：Inoreader / Feedly / 或任意支持 RSS 的本地工具',
    '自动化：n8n / Make / 或一个定时 Python 脚本',
    'AI 摘要：任意支持长文本的 LLM API（Claude / GPT / 国产大模型都可以）',
    '输出：推送到你每天都会看的笔记或邮件',
]
SETUP_STEPS = [
    '列出 5-10 个你真正愿意看原文的源',
    '用 RSS 订阅它们',
    '写一个 prompt：让 AI 把每天的新文章归类、写一句话摘要、标出必读项',
    '每天定时跑一次，把结果推送到你的笔记',
    '每周花 10 分钟清理 / 调整源',
]
SETUP_CLOSE = '不要追求“全自动”，先追求“每天少刷 30 分钟手机”。'

VERDICT = [
    '适合的人：工作中需要持续追踪某个领域的前沿信息；已经发现自己被推荐流消耗太多时间；愿意每周花 10 分钟维护信息流。',
    '不适合的人：只想看热点、吃瓜、追情绪——这套 workflow 会让你觉得“信息太少”；期望 AI 100% 准确摘要，自己不想看原文；没有明确的“我要追踪什么”这个问题。',
]
VERDICT_CLOSE = 'RSS + AI 摘要不是万能药，它解决的是一个很具体的问题：把“被动被算法投喂”改成“主动选源 + AI 压缩阅读”。它的价值不是让你知道更多，而是让你在更少的时间里，拿到更接近一手的信息。'

OPINION = [
    '对我这种靠“译介 + 落地”做内容的人来说，这套 workflow 最大的好处是：我能比中文圈早几天看到一手信息，然后决定要不要 replicate、能不能落地、值不值得分享。',
    '如果你也在做内容、做产品、或者做研究，我建议你先花 30 分钟搭一个最小版，跑一周，再决定要不要升级。别买课，别买工具，先让它在你自己的信息流里跑起来。',
]

OUTRO = [
    '如果你也在用 AI 处理信息流，欢迎评论区聊聊你的 setup，我挑好玩的下次拆开讲 👇',
]

# 文末极简 AI 指令（给 AI 的复现 spec，读者也能一眼看懂）
AI_INSTR_TITLE = '想复现？给 AI 的极简指令'
AI_INSTR_LINES = [
    '用 GitHub Actions 搭 RSS+AI 每日简报，无需自有服务器：',
    '· 逻辑：定时抓 14 个英文 RSS 信源 → 关键词相关度评分 → 去重 → 生成 Markdown 日报 → 自动 commit 回仓库',
    '· 三文件：config.py（信源+评分参数）、generate_brief.py（抓取/过滤/评分）、rss-daily-brief.yml（cron 每天北京 8:00）',
    '· 依赖：feedparser ｜ 输出：output/rss_briefs/YYYY-MM-DD_ai_daily_brief.md',
]

SIGN_NAME = '小木'
SIGN_DESC = '用 AI 把内容工作流跑起来。译介英文一手好文，讲人话的落地理解，不画饼。'

def build_ai_instr(title, lines):
    inner = ''.join(
        f'<p style="margin:0 0 7px;font-size:13px;line-height:1.75;color:#374151;">{leaf(l)}</p>'
        for l in lines)
    return (f'  <section style="margin:24px 20px 8px;padding:16px 18px;'
            f'background:#F0FDF4;border:1px solid #BBF7D0;border-radius:10px;">'
            f'<p style="margin:0 0 10px;font-size:13px;font-weight:800;color:#059669;letter-spacing:0.5px;">{leaf(title)}</p>'
            f'{inner}</section>')


def main():
    blocks = []
    blocks.append(build_cover(COVER))
    blocks.append(build_toc(PARTS))
    blocks.append(build_intro(INTRO_LEAD))
    blocks.append(build_preamble(PREAMBLE))

    blocks.append(chapter('01', '为什么做：我的信息痛点', 'WHY'))
    blocks.append(para(WHY_INTRO))
    blocks.append(bullets(WHY_PAIN))
    blocks.append(para('<span style="color:#059669;font-weight:600;">' + WHY_CLOSE + '</span>'))

    blocks.append(chapter('02', '怎么搭：我的最小可行版', 'HOW'))
    blocks.append(para(HOW_INTRO))
    blocks.append(bullets(HOW))

    blocks.append(chapter('03', '真收益：跑了一周的 3 个好处', 'GAINS'))
    blocks.append(para(GAINS_INTRO))
    blocks.append(bullets(GAINS))

    blocks.append(chapter('04', '反直觉坑：跑了一周的 3 个坑', 'PITFALLS'))
    blocks.append(para(PITFALLS_INTRO))
    blocks.append(bullets(PITFALLS))

    blocks.append(chapter('05', '可抄配置：最低配置 30 分钟跑通', 'SETUP'))
    blocks.append(para(SETUP_INTRO))
    blocks.append(build_checklist('5 步最小配置', SETUP_STEPS, SETUP_CLOSE))

    blocks.append(chapter('06', '落地判断：谁适合，谁不适合', 'VERDICT'))
    blocks.append(bullets(VERDICT))
    blocks.append(para(VERDICT_CLOSE))

    blocks.append(build_opinions('最后：先让它跑起来，再决定升级', OPINION))
    blocks.append(build_outro(OUTRO))
    blocks.append(build_sign(SIGN_NAME, SIGN_DESC))
    blocks.append(build_ai_instr(AI_INSTR_TITLE, AI_INSTR_LINES))

    html = ('<section style="max-width:677px;margin:0 auto;background:#ffffff;'
            + FONT +
            'color:#374151;line-height:1.75;letter-spacing:0.5px;overflow-x:hidden;">\n\n'
            + '\n\n'.join(blocks) +
            '\n</section>\n')
    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, 'rss_ai_daily_brief_wechat_排版_摸鱼绿(moyu-green).html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print('WROTE', out, len(html), 'bytes')


if __name__ == '__main__':
    main()
