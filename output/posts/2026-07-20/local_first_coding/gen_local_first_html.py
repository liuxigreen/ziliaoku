# -*- coding: utf-8 -*-
"""本地优先 AI 编码工具 · 公众号深读版 → 摸鱼绿排版 HTML（复用 gzh_style）。
输出: gzh_assets/local_first_wechat_排版_摸鱼绿(moyu-green).html
再跑 make_preview.py 包成 _预览.html。
"""
import os, re, sys
sys.path.insert(0, 'D:/WorkBuddyProjects/ziliaoku/scripts/gzh_publish')
from gzh_style import (leaf, para, chapter, build_cover, build_toc, build_intro,
                       build_preamble, build_opinions, build_outro, build_sign,
                       bullets, FONT)

SRC = 'D:/WorkBuddyProjects/ziliaoku/output/posts/2026-07-20/local_first_coding/local_first_wechat.md'
OUT_DIR = 'D:/WorkBuddyProjects/ziliaoku/output/posts/2026-07-20/local_first_coding/gzh_assets'

COVER = {
    'tag': 'AI 编程 · 避坑实测',
    't1': '代码别交给',
    't2': '云端 AI',
    'sub': '今天 GitHub 三连上榜的本地优先工具，打工人保命用法',
    'src': '打工人可复制',
    'tag_a': '本地优先', 'tag_b': '密钥守本机',
}
INTRO_LEAD = 'AI 编程助手很香，但敏感代码和密钥，别随手交出去。今天三个本地优先工具同时上榜，给你一张能照做的保命清单。'

SIGN_NAME = '小木'
SIGN_DESC = '用 AI 把内容工作流跑起来。译介一手好工具，讲人话的落地理解，不画饼。'


def inline(t):
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)


def build_ai_instr(title, lines):
    inner = ''.join(
        f'<p style="margin:0 0 7px;font-size:13px;line-height:1.75;color:#374151;">{leaf(l)}</p>'
        for l in lines)
    return (f'  <section style="margin:24px 20px 8px;padding:16px 18px;'
            f'background:#F0FDF4;border:1px solid #BBF7D0;border-radius:10px;">'
            f'<p style="margin:0 0 10px;font-size:13px;font-weight:800;color:#059669;letter-spacing:0.5px;">{leaf(title)}</p>'
            f'{inner}</section>')


def main():
    text = open(SRC, encoding='utf-8').read()
    lines = text.split('\n')
    blocks = []
    parts = []
    buf = []
    ch = 0
    i = 0

    def flush():
        nonlocal buf
        txt = '\n'.join(l for l in buf if l.strip())
        if txt.strip():
            blocks.append(para(inline(txt)))
        buf = []

    while i < len(lines):
        line = lines[i]
        if line.startswith('# '):
            i += 1; continue
        if line.strip() == '' or line.strip() == '---':
            flush(); i += 1; continue
        if line.startswith('## '):
            flush()
            ch += 1
            title = line[3:].strip()
            code = f'P{ch:02d}'
            parts.append((f'{ch:02d}', title, '', code))
            blocks.append(chapter(f'{ch:02d}', title, code))
            i += 1; continue
        if line.startswith('- '):
            flush()
            items = []
            while i < len(lines) and lines[i].startswith('- '):
                items.append(inline(lines[i][2:].strip()))
                i += 1
            if items:
                blocks.append(bullets(items))
            continue
        if line.startswith('> '):
            flush()
            q = line[2:].strip()
            if '我是小木' in q:
                blocks.append(build_sign(SIGN_NAME, SIGN_DESC))
            else:
                blocks.append(para('<blockquote style="border-left:3px solid #BBF7D0;padding-left:12px;color:#6B7280;">' + inline(q) + '</blockquote>'))
            i += 1; continue
        if line.startswith('🤖'):
            flush()
            title = line.replace('🤖', '').strip()
            instr = []
            i += 1
            while i < len(lines) and lines[i].strip().startswith('·'):
                instr.append(lines[i].strip()[1:].strip())
                i += 1
            blocks.append(build_ai_instr(title, instr))
            continue
        buf.append(line)
        i += 1
    flush()

    html = ('<section style="max-width:677px;margin:0 auto;background:#ffffff;'
            + FONT + 'color:#374151;line-height:1.75;letter-spacing:0.5px;overflow-x:hidden;">\n\n'
            + '\n\n'.join([build_cover(COVER), build_toc(parts), build_intro(INTRO_LEAD)] + blocks)
            + '\n</section>\n')
    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, 'local_first_wechat_排版_摸鱼绿(moyu-green).html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print('WROTE', out, len(html), 'bytes')


if __name__ == '__main__':
    main()
