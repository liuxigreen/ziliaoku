# -*- coding: utf-8 -*-
"""公众号摸鱼绿(moyu-green)排版样式库 —— 从 gen_claude_code_html.py 抽出的通用函数。
所有中文文字自动 <span leaf=""> 包裹（微信编辑器合规）；**关键词** 绿字高亮；英文引号转中文。
用法: from gzh_style import *  ; 各 build_* 返回 HTML 片段，main 里拼装后写 _排版.html。
"""
import re

FONT = "font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;"

def leaf(t):
    return f'<span leaf="">{t}</span>'

def leaf_br():
    return '<span leaf=""><br></span>'

def q(text):
    res = []
    flip = False
    for ch in text:
        if ch == '"':
            res.append('“' if not flip else '”'); flip = not flip
        elif ch == "'":
            res.append('‘' if not flip else '’'); flip = not flip
        else:
            res.append(ch)
    return ''.join(res)

def rich(text):
    text = q(text)
    parts = re.split(r'(\*\*.+?\*\*)', text)
    out = []
    for s in parts:
        if len(s) >= 4 and s.startswith('**') and s.endswith('**'):
            out.append(f'<strong style="color:#059669;">{leaf(s[2:-2])}</strong>')
        else:
            out.append(leaf(s))
    return ''.join(out)

def para(text, extra=''):
    return (f'<p style="margin:0 0 14px;font-size:14px;line-height:1.9;'
            f'text-align:justify;{extra}">{rich(text)}</p>')

def small(text):
    return (f'<p style="margin:0 0 14px;font-size:12px;line-height:1.7;color:#9CA3AF;'
            f'text-align:center;">{rich(text)}</p>')

def bullets(items, color='#059669'):
    lis = '\n'.join(
        f'  <section style="display:flex;align-items:flex-start;gap:8px;margin-bottom:10px;">'
        f'<span style="color:{color};font-weight:900;font-size:14px;flex-shrink:0;margin-top:2px;">{leaf("•")}</span>'
        f'<p style="margin:0;font-size:14px;line-height:1.8;color:#374151;">{rich(it)}</p></section>'
        for it in items)
    return f'  <section style="padding:0 20px;margin-bottom:8px;">\n{lis}\n  </section>'

def hack(n, t, u, p):
    return f'''  <section style="padding:0 20px;margin-bottom:24px;">
    <section style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
      <span style="background:#059669;color:#fff;font-size:12px;font-weight:800;padding:2px 8px;border-radius:6px;">{leaf(n)}</span>
      <p style="margin:0;font-size:15px;font-weight:900;color:#111827;line-height:1.4;">{leaf(t)}</p>
    </section>
    {para('我的用法：' + u)}
    {para('效果：' + p, extra='color:#6B7280;')}
  </section>'''

def build_hacks(title, hacks):
    body = '\n'.join(hack(*h) for h in hacks)
    return f'''  <section style="margin-top:40px;margin-bottom:32px;padding:0 20px;">
    <p style="margin:0 0 16px;font-size:18px;font-weight:900;color:#111827;letter-spacing:0.3px;">{leaf(title)}</p>
{body}
  </section>'''

def chapter(num, title, en):
    return f'''  <section style="margin-top:40px;margin-bottom:6px;padding:0 20px;">
    <section style="display:flex;align-items:center;gap:16px;margin-bottom:18px;">
      <section style="text-align:center;flex-shrink:0;">
        <p style="margin:0;font-size:28px;font-weight:900;color:#059669;line-height:1;letter-spacing:-2px;">{leaf(num)}</p>
        <p style="margin:0;font-size:8px;font-weight:700;color:#D1D5DB;letter-spacing:2px;">{leaf('PART')}</p>
      </section>
      <span style="width:1px;height:36px;background:#E5E7EB;flex-shrink:0;">{leaf_br()}</span>
      <section>
        <p style="margin:0 0 1px;font-size:17px;font-weight:900;color:#111827;letter-spacing:0.3px;">{leaf(title)}</p>
        <p style="margin:0;font-size:11px;font-weight:600;color:#9CA3AF;letter-spacing:1.5px;">{leaf(en)}</p>
      </section>
    </section>
  </section>'''

def build_cover(c):
    return f'''  <!-- 1. 封面 -->
  <section style="margin:0 0 32px;background:#fff;border:1.5px solid rgba(5,150,105,0.15);border-radius:20px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,0.06);width:100%;">
    <section style="padding:32px 28px 28px;">
      <section style="display:flex;align-items:center;gap:8px;margin-bottom:28px;">
        <span style="width:6px;height:6px;background:#059669;border-radius:50%;">{leaf_br()}</span>
        <span style="font-size:11px;font-weight:700;letter-spacing:3px;color:#059669;">{leaf(c['tag'])}</span>
        <section style="flex:1;height:1px;overflow:hidden;background:linear-gradient(to right,rgba(5,150,105,0.12),transparent);">{leaf_br()}</section>
        <span style="font-size:10px;color:#D1D5DB;font-weight:600;">{leaf('2026.07')}</span>
      </section>
      <section>
        <p style="font-size:15px;color:#D1D5DB;margin:0 0 6px;text-decoration:line-through;letter-spacing:0.5px;">{leaf('从零造轮子？')}</p>
        <p style="font-size:24px;font-weight:900;color:#111827;margin:0;line-height:1.05;letter-spacing:-2px;">{leaf(c['t1'])}</p>
        <p style="font-size:24px;font-weight:900;color:#059669;margin:0 0 16px;line-height:1.05;letter-spacing:-2px;">{leaf(c['t2'])}</p>
        <section style="width:48px;height:3px;background:linear-gradient(to right,#059669,#34D399);border-radius:2px;margin-bottom:12px;">{leaf_br()}</section>
        <p style="font-size:13px;color:#9CA3AF;margin:0;line-height:1.7;letter-spacing:0.5px;">{leaf(c['sub'])}</p>
      </section>
    </section>
    <section style="background:linear-gradient(135deg,#059669,#10B981);padding:12px 28px;display:flex;align-items:center;justify-content:space-between;">
      <p style="font-size:12px;color:rgba(255,255,255,0.9);margin:0;font-weight:600;letter-spacing:0.5px;">{leaf(c['src'])}</p>
      <section style="display:flex;gap:4px;">
        <span style="background:rgba(255,255,255,0.2);padding:1px 6px;border-radius:3px;font-size:8px;color:#fff;font-weight:600;">{leaf(c['tag_a'])}</span>
        <span style="background:rgba(255,255,255,0.2);padding:1px 6px;border-radius:3px;font-size:8px;color:#fff;font-weight:600;">{leaf(c['tag_b'])}</span>
      </section>
    </section>
  </section>'''

def build_toc(parts):
    cards = []
    for i, (num, zh, sub, en) in enumerate(parts):
        if i == 0:
            style = 'background:linear-gradient(135deg,#059669,#10B981);'
            tcol, scol = '#fff', 'rgba(255,255,255,0.7)'
        else:
            style = 'background:#fff;border:1px solid #E5E7EB;box-shadow:0 2px 6px rgba(0,0,0,0.04);'
            tcol, scol = '#111827', '#9CA3AF'
        cards.append(f'''      <section style="display:inline-block;white-space:normal;vertical-align:top;width:120px;{style}border-radius:12px;padding:12px;margin-right:8px;">
        <p style="font-size:9px;font-weight:700;color:{scol};letter-spacing:1px;margin:0 0 5px;">{leaf('PART ' + num)}</p>
        <p style="font-size:13px;font-weight:800;color:{tcol};margin:0 0 3px;">{leaf(zh)}</p>
        <p style="font-size:10px;color:{scol};margin:0;">{leaf(sub)}</p>
      </section>''')
    return f'''  <!-- 2. 目录 -->
  <section style="margin:0 20px 32px;">
    <section style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;">
      <p style="font-size:10px;color:#9CA3AF;margin:0;text-transform:uppercase;letter-spacing:2px;font-weight:600;">{leaf('📑 3 Parts')}</p>
      <p style="font-size:10px;color:#9CA3AF;margin:0;">{leaf('👉 滑动')}</p>
    </section>
    <section style="overflow-x:scroll;-webkit-overflow-scrolling:touch;white-space:nowrap;padding-bottom:8px;">
{''.join(cards)}
    </section>
  </section>'''

def build_intro(lead):
    return f'''  <!-- 3. 开篇引言 -->
  <section style="background:#FFF;border:1px dashed #BBF7D0;border-radius:8px;padding:14px 16px;margin-bottom:24px;text-align:center;">
    <p style="font-size:12px;color:#9CA3AF;margin:0 0 6px;line-height:1.5;">{leaf('开篇一句话')}</p>
    <p style="margin:0;line-height:1.6;">{leaf(lead)}</p>
  </section>'''

def build_preamble(paras):
    return '  <section style="padding:0 20px;margin-bottom:8px;">\n' + '\n'.join(para(p) for p in paras) + '\n  </section>'

def build_opinions(title, paras):
    body = '\n'.join(para(p) for p in paras)
    return f'''  <section style="margin-top:40px;margin-bottom:32px;padding:0 20px;">
    <p style="margin:0 0 16px;font-size:18px;font-weight:900;color:#111827;letter-spacing:0.3px;">{leaf(title)}</p>
{body}
  </section>'''

def build_checklist(title, items, tail):
    lis = '\n'.join(
        f'  <section style="display:flex;align-items:flex-start;gap:8px;margin-bottom:10px;padding:10px 12px;background:#F0FDF4;border:1px solid #DCFCE7;border-radius:8px;">'
        f'<span style="color:#059669;font-weight:900;font-size:14px;flex-shrink:0;">{leaf("✓")}</span>'
        f'<p style="margin:0;font-size:14px;line-height:1.7;color:#374151;">{leaf(it)}</p></section>'
        for it in items)
    tail_p = para(tail)
    return f'''  <section style="margin-top:40px;margin-bottom:32px;padding:0 20px;">
    <p style="margin:0 0 16px;font-size:18px;font-weight:900;color:#111827;letter-spacing:0.3px;">{leaf(title)}</p>
{lis}
{tail_p}
  </section>'''

def build_outro(paras):
    return '  <section style="padding:0 20px;margin-bottom:32px;">\n' + '\n'.join(para(p) for p in paras) + '\n  </section>'

def build_sign(name, desc):
    return f'''  <!-- 签名 -->
  <section style="margin:40px 20px 8px;padding:20px 0 0;border-top:1px solid #E5E7EB;">
    <p style="margin:0 0 6px;font-size:14px;font-weight:800;color:#111827;">{leaf('我是 ' + name)}</p>
    <p style="margin:0;font-size:13px;color:#9CA3AF;line-height:1.7;">{leaf(desc)}</p>
  </section>'''
