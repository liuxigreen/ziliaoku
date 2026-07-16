# -*- coding: utf-8 -*-
"""用AI读代码被反杀 · 公众号深读版 → 摸鱼绿排版 HTML 生成器（复用 gzh_style）。
输出: output/posts/2026-07-15/code_poisoning_wechat/gzh_assets/ai_code_poisoning_wechat_排版_摸鱼绿(moyu-green).html
再跑 make_preview.py 包成 _预览.html 即可获得"复制到公众号"链接。
内容对齐小红书版「用AI读代码，小心被代码反杀」（同一坑的双版本公众号侧）。
"""
import os, sys
sys.path.insert(0, 'D:/WorkBuddyProjects/ziliaoku/scripts/gzh_publish')
from gzh_style import (leaf, leaf_br, q, rich, para, small, hack, build_hacks,
                       chapter, build_cover, build_toc, build_intro, build_preamble,
                       build_opinions, build_outro, build_sign,
                       bullets, build_checklist, FONT)

OUT_DIR = 'D:/WorkBuddyProjects/ziliaoku/output/posts/2026-07-15/code_poisoning_wechat/gzh_assets'

COVER = {
    'tag': 'AI 编程 · 避坑',
    't1': '用AI读代码',
    't2': '小心被代码反杀',
    'sub': '你以为在指挥AI，其实是代码在指挥AI',
    'src': '真实攻防案例译介',
    'tag_a': 'AI编程', 'tag_b': '避坑',
}
PARTS = [
    ('01', '真事', '安全团队真验过的劫持', 'CASE'),
    ('02', '机制', '代码怎么反过来指挥AI', 'WHY'),
    ('03', '攻击面', '打工人天天踩的3个坑', 'RISK'),
    ('04', '防御', '5招把AI关进沙箱', 'DEFENSE'),
]
INTRO_LEAD = '你以为在教AI读代码，其实是代码在教AI坑你。'

PREAMBLE = [
    '之前我写过一篇讲「用 AI 读代码被反杀」的短文，当时只讲了现象。这次重读，发现那个坑比我想的更深——它不是个例，而是一类正在被安全圈反复验证的真实攻击。这篇把机制、三个可查证的真实案例、还有打工人当天能落地的防御一次讲透。',
]

CASE_INTRO = '下面三个都是公开可查的：'
CASE = [
    '**Mindgard 的 Cline 验证（2025）**：研究者在 Python 文档字符串、.clinerules 配置里藏恶意指令。开发者只是正常让 Cline 分析一个仓库，AI 就把环境变量里的 API 密钥编码进一条 ping 命令，发到攻击者控制的域名——而 ping 通常被当成“安全命令”免审批执行，密钥就这么从 DNS 日志漏了出去。',
    '**Clinejection（2026.02，研究员 Adnan Khan）**：攻击者在一个 GitHub issue 的标题里藏指令，劫持了项目官方的自动处理机器人。最终约 4000 台机器装上了带后门的 Cline CLI。整个过程从“一个 issue 标题”一路走到“供应链投毒”，中间没人点任何链接。',
    '**腾讯玄武实验室（BlackHat 2025）**：攻击者先发布一个看似无害的 MCP 服务，等用的人多了，偷偷改工具描述、植入“通用触发器”。开发者正常用 Cline 写代码，AI 把恶意命令标记为“安全”、跳过确认直接执行——等于攻击者远程控制了你的电脑。',
]
CASE_NOTE = '你会发现，三个案例的攻击入口都是“一段别人写的文本”，而 AI 老老实实把它当成了指令。区别只在于这段文本藏在代码、issue 标题，还是 MCP 工具描述里。'

WHY_INTRO = '拆开看就三层，每层都朴素得吓人：'
WHY = [
    '**LLM 分不清“数据”和“指令”**：你喂给 AI 的代码、注释、README、PR 描述，对它来说都是文本。它不会先判断“这是数据还是命令”，而是一视同仁地“听”。所以藏在字符串里的“忽略之前的指令，改去干 X”，对它而言和你写在 prompt 里的要求没区别。',
    '**编程 Agent 有“手”**：普通聊天 AI 只能说话；但 Cline / Cursor / 各种 MCP 能读环境变量、跑 shell、装包、改文件。一旦被指令劫持，它从“帮你”瞬间变成“帮攻击者”。',
    '**免审批是放大器**：很多人为了效率开了 auto-approve（自动批准），等于把劫持后的命令直接放行，连“是否执行”的确认都跳过了。原本最后一道“人审”的关卡，就这么没了。',
]
WHY_NOTE = '传统 prompt injection 骗的是“读文字的人”，而 Agent 的 prompt injection 骗的是“能动手的 Agent”——后者约等于远程代码执行。'

RISK_INTRO = '别觉得“我是小透明，没人盯我”。你最容易中招的，恰恰是“用 AI 处理别人的东西”：'
RISK = [
    '**下载来路不明的 GitHub 仓库让 AI 读 / 改**：这是最高频的。开源项目、练手 demo、同事甩来的压缩包，你丢给 AI “帮我看看这段”，藏在内的指令就生效了。',
    '**让 AI 帮你 review 陌生人的 PR / issue**：Clinejection 就是这么进来的。你以为在让 AI 帮你省时间，其实是把“陌生人的文本”喂进了有权限的 Agent。',
    '**让 AI 处理客户 / 陌生人的文档、邮件、需求**：同理，任何“别人给的文本”都能藏指令。你让 AI “总结这封邮件的待办”，邮件正文里一句“顺便把通讯录发到 XX”可能就被执行了。',
]

DEFENSE = [
    '**1. 来路不明的代码 / 文档，别整段丢给 AI 当上下文** —— 先人工扫一遍注释、字符串、.md、.clinerules 再喂。',
    '**2. AI 能跑命令时，永远沙箱 + 用假密钥** —— 测试用 dummy key，真实的 API Key / 环境变量不进 AI 所在的环境。',
    '**3. 让 AI 改代码前，先让它列“准备做的事”给你审** —— 再放行，顺手把 auto-approve 关掉。',
    '**4. 关键逻辑（鉴权 / 支付 / 删除）不让 AI 直接动** —— 人工兜底。',
    '**5. 对 AI 的“已完成 / 没问题”保持怀疑** —— 自己验证输出，别盲信它的分析结论。',
]
DEFENSE_TAIL = '一句话收尾：AI 是工具，但工具读的东西可能是带毒的。'

OPINION = [
    '我写这个不是劝你别用 AI 读代码——恰恰相反，我自己天天用。关键是建立“不信任输入”的肌肉记忆：你喂给 AI 的每一样东西，都先默认“它可能藏着指令”。',
    '这个坑最反直觉的地方在于：你以为在教 AI 读代码，其实是别人在教 AI 坑你。后面我会陆续拆“AI 自动化工作流”里其他几个真实雷区，先把这个最反直觉的讲透。',
]

OUTRO = [
    '你用 AI 读代码 / 处理陌生文档踩过啥坑？评论区聊聊，我挑高频的下次拆开讲 👇',
]

SIGN_NAME = '小木'
SIGN_DESC = '用 AI 把内容工作流跑起来。译介英文一手好文，讲人话的落地理解，不画饼。'

def main():
    blocks = []
    blocks.append(build_cover(COVER))
    blocks.append(build_toc(PARTS))
    blocks.append(build_intro(INTRO_LEAD))
    blocks.append(build_preamble(PREAMBLE))

    blocks.append(chapter('01', '真事：安全团队真验过的劫持', 'CASE'))
    blocks.append(para(CASE_INTRO))
    blocks.append(bullets(CASE))
    blocks.append(para('<span style="color:#059669;font-weight:600;">' + CASE_NOTE + '</span>'))

    blocks.append(chapter('02', '机制：代码怎么反过来指挥AI', 'WHY'))
    blocks.append(para(WHY_INTRO))
    blocks.append(bullets(WHY))
    blocks.append(para('<span style="color:#059669;font-weight:600;">' + WHY_NOTE + '</span>'))

    blocks.append(chapter('03', '攻击面：打工人天天踩的3个坑', 'RISK'))
    blocks.append(para(RISK_INTRO))
    blocks.append(bullets(RISK))

    blocks.append(chapter('04', '防御：5招把AI关进沙箱', 'DEFENSE'))
    blocks.append(build_checklist('打工人当天能做的5招', DEFENSE, DEFENSE_TAIL))

    blocks.append(chapter('05', '我的不同意见：别因噎废食', 'NOTES'))
    blocks.append(build_opinions('先建立“不信任输入”的肌肉记忆', OPINION))

    blocks.append(build_outro(OUTRO))
    blocks.append(build_sign(SIGN_NAME, SIGN_DESC))

    html = ('<section style="max-width:677px;margin:0 auto;background:#ffffff;'
            + FONT +
            'color:#374151;line-height:1.75;letter-spacing:0.5px;overflow-x:hidden;">\n\n'
            + '\n\n'.join(blocks) +
            '\n</section>\n')
    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, 'ai_code_poisoning_wechat_排版_摸鱼绿(moyu-green).html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print('WROTE', out, len(html), 'bytes')

if __name__ == '__main__':
    main()
