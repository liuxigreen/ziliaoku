#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 ziliaoku 的公众号 Markdown 稿排成微信可粘贴的样式 HTML。
不依赖外部库（自写极简 markdown 解析 + 微信 CSS + 封面 base64 内嵌）。
用法: python wechat_render.py <md_path> [cover_png_path] [输出 html 路径]
"""
import sys, re, base64, io, os
from PIL import Image

ACCENT = "#e74c3c"  # 主题红，呼应封面

def strip_frontmatter(text):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:].lstrip("\n")
    return text

def compress_cover_b64(path, max_w=1200, quality=82):
    im = Image.open(path).convert("RGB")
    if im.width > max_w:
        h = int(im.height * max_w / im.width)
        im = im.resize((max_w, h))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=quality)
    return base64.b64encode(buf.getvalue()).decode("ascii")

def inline_bold(s):
    # **x** -> <strong>
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)

def render_md(md):
    lines = md.split("\n")
    html = []
    i = 0
    n = len(lines)
    list_stack = []  # 记录当前列表类型 'ul'/'ol'

    def close_lists(upto=0):
        out = []
        while len(list_stack) > upto:
            t = list_stack.pop()
            out.append("</%s>" % t)
        return "".join(out)

    while i < n:
        line = lines[i]
        # 标题
        m = re.match(r"^(#{1,3})\s+(.*)$", line)
        if m:
            html.append(close_lists())
            lvl = len(m.group(1))
            html.append("<h%d>%s</h%d>" % (lvl, inline_bold(m.group(2).strip()), lvl))
            i += 1
            continue
        # 引用
        if line.startswith("> "):
            html.append(close_lists())
            # 收集连续引用
            quote = []
            while i < n and lines[i].startswith("> "):
                quote.append(inline_bold(lines[i][2:].strip()))
                i += 1
            html.append('<blockquote>%s</blockquote>' % "<br>".join(quote))
            continue
        # 无序列表
        if re.match(r"^- ", line):
            if not list_stack or list_stack[-1] != "ul":
                html.append(close_lists())
                html.append("<ul>")
                list_stack.append("ul")
            html.append("<li>%s</li>" % inline_bold(line[2:].strip()))
            i += 1
            continue
        # 有序列表
        if re.match(r"^\d+\.\s+", line):
            if not list_stack or list_stack[-1] != "ol":
                html.append(close_lists())
                html.append("<ol>")
                list_stack.append("ol")
            html.append("<li>%s</li>" % inline_bold(re.sub(r"^\d+\.\s+", "", line).strip()))
            i += 1
            continue
        # 空行
        if line.strip() == "":
            html.append(close_lists())
            i += 1
            continue
        # 普通段落
        html.append(close_lists())
        html.append("<p>%s</p>" % inline_bold(line.strip()))
        i += 1
    html.append(close_lists())
    return "\n".join(html)

CSS = """
<style>
.wx-wrap { max-width: 720px; margin: 0 auto; padding: 8px 4px;
  font-size: 16px; color: #333; line-height: 1.85; letter-spacing: .3px;
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", sans-serif; }
.wx-wrap h1 { font-size: 22px; font-weight: 700; color: #1a1a1a; border-left: 5px solid %s;
  padding-left: 12px; margin: 32px 0 16px; line-height: 1.4; }
.wx-wrap h2 { font-size: 19px; font-weight: 700; color: #1a1a1a; margin: 30px 0 12px;
  padding-bottom: 8px; border-bottom: 1px solid #eee; }
.wx-wrap h3 { font-size: 17px; font-weight: 600; color: %s; margin: 24px 0 10px; }
.wx-wrap p { margin: 15px 0; }
.wx-wrap strong { color: %s; font-weight: 700; }
.wx-wrap ul, .wx-wrap ol { padding-left: 22px; margin: 15px 0; }
.wx-wrap li { margin: 9px 0; }
.wx-wrap blockquote { border-left: 4px solid %s; background: #fdf3f2; color: #666;
  padding: 12px 16px; margin: 18px 0; border-radius: 0 6px 6px 0; }
.wx-wrap .hero { width: 100%%; border-radius: 8px; margin: 0 0 22px; display: block; }
.wx-wrap .note { font-size: 13px; color: #999; text-align: center; margin-top: 34px; }
</style>
""" % (ACCENT, ACCENT, ACCENT, ACCENT)

def main():
    md_path = sys.argv[1]
    cover_path = sys.argv[2] if len(sys.argv) > 2 else None
    out_path = sys.argv[3] if len(sys.argv) > 3 else md_path.rsplit(".", 1)[0] + "_rendered.html"

    with open(md_path, "r", encoding="utf-8") as f:
        raw = f.read()
    body = strip_frontmatter(raw)
    body_html = render_md(body)

    hero = ""
    if cover_path and os.path.exists(cover_path):
        b64 = compress_cover_b64(cover_path)
        hero = '<img class="hero" src="data:image/jpeg;base64,%s">' % b64

    full = (
        "<!DOCTYPE html><html><head><meta charset='utf-8'>"
        + CSS
        + "</head><body><div class='wx-wrap'>"
        + hero + body_html
        + '<p class="note">—— 本文由 ziliaoku 工作流排版生成 ——</p>'
        + "</div></body></html>"
    )
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full)
    print("OK ->", out_path, "size", os.path.getsize(out_path))

if __name__ == "__main__":
    main()
