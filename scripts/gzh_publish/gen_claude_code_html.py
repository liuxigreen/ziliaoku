# -*- coding: utf-8 -*-
"""claude_code_32tips 公众号深度稿 → 摸鱼绿排版 HTML 生成器（复用 gzh_style）。
输出: gzh_publish/claude_code_gzh_排版_摸鱼绿(moyu-green).html
再跑 make_preview.py 包成 _预览.html 即可获得"复制到公众号"链接。
正文 2 张 ian 小黑插图用 base64 内联（本地预览可见；贴公众号时按标记重传图片）。
"""
import os, sys, base64
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gzh_style import (leaf, leaf_br, q, rich, para, small, hack, build_hacks,
                       chapter, build_cover, build_toc, build_intro, build_preamble,
                       build_opinions, build_outro, build_sign,
                       bullets, FONT)

ILLU = 'D:/WorkBuddyProjects/ziliaoku/output/posts/2026-07-11/illustrations/claude_code_32tips'

def img_block(fname, cap):
    p = os.path.join(ILLU, fname)
    with open(p, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode()
    return (f'<figure style="margin:26px 0;text-align:center;">'
            f'<img src="data:image/png;base64,{b64}" '
            f'style="width:100%;max-width:620px;border-radius:10px;'
            f'box-shadow:0 4px 16px rgba(0,0,0,.08);" />'
            f'<figcaption style="font-size:13px;color:#9ca3af;'
            f'margin-top:8px;letter-spacing:.5px;">{cap}</figcaption></figure>')

COVER = {
    'tag': 'AI 编程 · 工具译介',
    't1': '32 招我只留这几条',
    't2': 'Claude Code 真正能落地的',
    'sub': '译介 Nate Herk「32 Tricks」· 结合半年实操',
    'src': 'YouTube | Nate Herk',
    'tag_a': 'Claude Code', 'tag_b': '实操',
}
PARTS = [
    ('01', '地基', '两招吃透已赢过大多数', 'BASE'),
    ('02', '上下文', 'AI 变傻八成是喂涝了', 'CONTEXT'),
    ('03', '协作姿势', '让返工少一半的三招', 'COLLAB'),
    ('04', '规模化', '把重复劳动变成资产', 'SCALE'),
]
INTRO_LEAD = '最贵的不是更聪明的模型，是养成的习惯'

PREAMBLE = [
    '用 Claude Code 大半年，中间一度觉得自己用得挺溜。直到刷到那期「32 个技巧，16 分钟带你从小白到量产工作流」，才意识到自己一直在裸奔——最该开的开关、最该养成的习惯，一个都没碰。',
    '那期视频作者是 Nate Herk，把技巧分成了新手、进阶、高手三档。我扒了完整字幕，又结合自己这半年的踩坑，把 32 招重新归了类，留下真正能当天用、且不容易踩坑的部分。',
]

BASE_INTRO = '这两招成本极低、回报极高，但绝大多数人（包括半年前的我）都没用上。'
BASE = [
    '**1. 进任何项目，先打 /init** —— 它会扫一遍你的代码库，自动生成一份 CLAUDE.md（项目速查卡），把架构、规范、关键文件都记下来。以后每次新会话，它不用你重新解释背景，直接带着上下文上手。空仓库也能让它帮你建第一版。',
    '**2. 永远先 Plan Mode（Shift+Tab 切换）** —— 规划模式下它能读、能调研、能列方案，但一个字都不会改。等方案磨清楚再切回自动执行。进阶玩法：把它当 junior 开发，给问题不给命令（「怎么处理增长追踪？」比「写个 X 函数」出来的东西好）。',
]
BASE_NOTE = '我实测过，90% 的返工都是「一上来就写」导致的。多花两分钟说清要干啥，比改五遍快。'

CTX_INTRO = '上下文腐烂（context rot）是很多人没意识到、却天天在发生的坑。AI 不是突然变笨，是你喂太多无关信息把它淹了。'
CTX = [
    '**3. 保持上下文小** —— 别把整个代码库倒进一个对话，只给当前任务需要的，把大问题拆成小的、聚焦的步骤。',
    '**4. 用 /context 找 token 黑洞** —— 跑一下它把「谁在吃 token」拆成百分比（系统提示、文件、MCP），会话臃肿时就能定位问题。',
    '**5. 60% 就 compact，换任务就 clear** —— 上下文到 60% 敲 /compact 压缩历史（还能指定保留项）；完全不同任务用 /clear 清空，CLAUDE.md 还在，不是真从零来。',
]

COLLAB_INTRO = '第 6、7 两招其实说的是同一件事的两边——对齐和验证。这和我之前写的官方内部用法是同一回事：验证是 ROI 最高的一招。'
COLLAB = [
    ('6', '让它主动提问，别闷头干',
     '直接下指令：「直到你有 95% 确信你懂我要什么，再动手。」它会用提问工具反复对齐，省掉来回改三四个回合。',
     '把沟通成本前置，比写完才发现方向错便宜太多。'),
    ('7', '把「自检」写进待办清单',
     '它每列一个 to-do，你紧跟一条验证：截图看排版、开 DevTools 看报错、不到 95% 确信不许进下一条。质量检查直接烤进执行计划。',
     '不是「写完丢给你反馈」，而是「写完自查、确认没问题再交」。'),
    ('8', '用子代理并行，主线程不卡死',
     '复杂问题让主会话派子代理：各自独立上下文、可跑不同模型，同时调研/写测试/试方案，汇报回来汇总。简单活儿子代理用 Haiku、主线程用 Opus，又快又省。',
     '把「一个人写」变成「一个小团队」。'),
]

SCALE_INTRO = '这两招最反直觉但最值钱——把一次性的活，变成可复用的资产。'
SCALE = [
    ('9', '把重复的事存成自定义技能',
     '在 .claude/skills 建可复用提示词文件（techdebt.md 教它扫技术债、codereview.md 教它审代码），下次自然语言调一句就行。',
     '一件事做过一次就固化成技能，相当于给 AI 攒了肌肉记忆。'),
    ('10', '给它建一本「错题本」',
     '只要 AI 做错一次，就把这条教训写进 CLAUDE.md 并提交，它下次不再犯。这其实就是 /init 生成的那份文件，被你持续喂养后的样子。',
     'CLAUDE.md 不是一次性说明书，是越用越厚的错题本。'),
]

OPINION = [
    '32 招看着过瘾，但我得泼盆冷水：**新手别全学。**',
    '/init 和 Plan Mode 这两招先吃透，你已经能甩开大多数「只会对话式让 AI 写代码」的人。剩下的——/context、compact、子代理、自定义技能——等你在真实项目里真卡住了，再回来翻对应的那一招，印象会深得多。',
    '我见过太多人收藏一堆「AI 编程神技」然后继续裸奔。技巧不是收藏量，是你在哪个卡点用上了哪一招。',
]

OUTRO = [
    '你用 Claude Code / Cursor 踩过哪些坑？评论区聊聊，我挑高频的下次拆开讲。',
    '我平时会在小红书同步这类「能跑的 AI 实操」，从选题到落地都讲，感兴趣可以去逛逛。这篇是公众号深读版，想要更短更碎的，去小红书看。',
]

SIGN_NAME = '小木'
SIGN_DESC = '用 AI 把内容工作流跑起来。译介英文一手好文，讲人话的落地理解，不画饼。'

def main():
    blocks = []
    blocks.append(build_cover(COVER))
    blocks.append(build_toc(PARTS))
    blocks.append(build_intro(INTRO_LEAD))
    blocks.append(build_preamble(PREAMBLE))

    blocks.append(chapter('01', '地基：两招吃透，已赢过大多数', 'BASE'))
    blocks.append(para(BASE_INTRO))
    blocks.append(bullets(BASE))
    blocks.append(para('<span style="color:#059669;font-weight:600;">'+BASE_NOTE+'</span>'))

    blocks.append(chapter('02', '上下文：AI 变傻，八成是喂涝了', 'CONTEXT'))
    blocks.append(para(CTX_INTRO))
    blocks.append(bullets(CTX))

    blocks.append(chapter('03', '协作姿势：让返工少一半的三招', 'COLLAB'))
    blocks.append(para(COLLAB_INTRO))
    blocks.append(build_hacks('三招一起用，返工肉眼变少', COLLAB))
    blocks.append(img_block('ian_02.png', '插图：小黑同时推开三个并行子代理窗口'))

    blocks.append(chapter('04', '规模化：把重复劳动变成「资产」', 'SCALE'))
    blocks.append(para(SCALE_INTRO))
    blocks.append(build_hacks('两招养出「越用越顺」的 AI', SCALE))
    blocks.append(img_block('ian_01.png', '插图：小黑翻开写满规则的 CLAUDE.md 错题本'))

    blocks.append(chapter('05', '我的不同意见：别贪多', 'NOTES'))
    blocks.append(build_opinions('新手先吃透这两招就够了', OPINION))

    blocks.append(build_outro(OUTRO))
    blocks.append(build_sign(SIGN_NAME, SIGN_DESC))

    html = ('<section style="max-width:677px;margin:0 auto;background:#ffffff;'
            + FONT +
            'color:#374151;line-height:1.75;letter-spacing:0.5px;overflow-x:hidden;">\n\n'
            + '\n\n'.join(blocks) +
            '\n</section>\n')
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       'claude_code_gzh_排版_摸鱼绿(moyu-green).html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print('WROTE', out, len(html), 'bytes')

if __name__ == '__main__':
    main()
