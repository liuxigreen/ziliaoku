# -*- coding: utf-8 -*-
"""把 _排版.html 包成 _预览.html（自带「📋 复制到公众号」按钮的自包含预览页）。
从既有 claude_code_..._预览.html 反推的通用模板：head(工具栏+复制JS) + 正文 + tail。
用法: python make_preview.py <_排版.html路径>
"""
import sys, os

def make_preview(排版_path):
    with open(排版_path, encoding='utf-8') as f:
        content = f.read()
    title = os.path.basename(排版_path).replace('_排版_', ' · ').replace('.html', '')
    head = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · 公众号排版预览</title>
<style>
  body{{margin:0;background:#eef0f2;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;-webkit-text-size-adjust:100%;}}
  .gzh-toolbar{{position:fixed;top:0;left:0;right:0;height:54px;background:#ffffff;box-shadow:0 1px 10px rgba(0,0,0,.08);display:flex;align-items:center;justify-content:space-between;padding:0 16px;z-index:99;}}
  .gzh-hint{{font-size:13px;color:#6b7280;line-height:1.4;}}
  .gzh-hint b{{color:#111827;}}
  .gzh-copy{{background:#059669;color:#fff;border:0;border-radius:9px;padding:10px 20px;font-size:14px;font-weight:700;cursor:pointer;box-shadow:0 3px 10px rgba(5,150,105,.28);white-space:nowrap;transition:transform .08s,background .15s;}}
  .gzh-copy:hover{{background:#047857;}}
  .gzh-copy:active{{transform:translateY(1px);}}
  .gzh-toast{{position:fixed;top:66px;left:50%;transform:translateX(-50%);background:#111827;color:#fff;padding:11px 20px;border-radius:10px;font-size:14px;font-weight:600;opacity:0;pointer-events:none;transition:opacity .25s;z-index:100;box-shadow:0 6px 20px rgba(0,0,0,.25);max-width:88vw;text-align:center;}}
  .gzh-toast.show{{opacity:1;}}
  .gzh-stage{{max-width:700px;margin:78px auto 64px;padding:0 8px;}}
  @media(max-width:520px){{.gzh-hint{{max-width:150px;}}}}
</style>
</head>
<body>
<div class="gzh-toolbar">
  <span class="gzh-hint">👇 下方是排版效果 · 点右侧 <b>复制</b> 直接粘到公众号</span>
  <button class="gzh-copy" id="gzhCopyBtn" onclick="gzhCopy()">📋 复制到公众号</button>
</div>
<div class="gzh-toast" id="gzhToast"></div>
<div class="gzh-stage">
  <div id="gzh-content">
{content}
  </div>
</div>
<script>
  function gzhShowToast(msg){{
    var t=document.getElementById('gzhToast');
    t.textContent=msg;t.classList.add('show');
    clearTimeout(t._timer);
    t._timer=setTimeout(function(){{t.classList.remove('show');}},2800);
  }}
  function gzhCopy(){{
    var el=document.getElementById('gzh-content');
    var range=document.createRange();
    range.selectNodeContents(el);
    var sel=window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);
    var ok=false;
    try{{ok=document.execCommand('copy');}}catch(e){{ok=false;}}
    sel.removeAllRanges();
    var btn=document.getElementById('gzhCopyBtn');
    if(ok){{
      gzhShowToast('✅ 已复制！去公众号编辑器按 Ctrl/⌘+V 粘贴即可');
      var old=btn.textContent;btn.textContent='✅ 已复制';
      setTimeout(function(){{btn.textContent=old;}},2200);
    }}else{{
      gzhShowToast('⚠ 自动复制失败，请手动全选(Ctrl/⌘+A)再复制(Ctrl/⌘+C)');
    }}
  }}
</script>
</body>
</html>'''
    out = 排版_path[:-5] + '_预览.html'
    with open(out, 'w', encoding='utf-8') as f:
        f.write(head)
    print('WROTE', out, os.path.getsize(out), 'bytes')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: python make_preview.py <_排版.html>')
        sys.exit(1)
    make_preview(sys.argv[1])
