#!/usr/bin/env python3
"""生成 本地优先 AI 编码工具 双版配图（纯 PIL，零成本、中文不乱码）。
小红书：封面 3:4 + 3 张文字卡片 3:4（叠「打工人北北」）
公众号：头图 2.35:1（叠「小木」）
"""
import os
from PIL import Image, ImageDraw, ImageFont

FONT_DIR = "C:/Windows/Fonts"
def F(size, bold=True):
    return ImageFont.truetype(os.path.join(FONT_DIR, "msyhbd.ttc" if bold else "msyh.ttc"), size)

OUT = os.path.dirname(os.path.abspath(__file__))

GREEN   = (38, 156, 94)
GREEN_D = (22, 102, 62)
INK     = (33, 40, 35)
PAPER   = (244, 248, 243)
GREY    = (110, 122, 112)
WHITE   = (255, 255, 255)
SOFT    = (214, 236, 220)


def wrap(text, fnt, max_w, draw):
    lines = []
    for para in text.split("\n"):
        line = ""
        for ch in para:
            if draw.textlength(line + ch, font=fnt) <= max_w:
                line += ch
            else:
                lines.append(line); line = ch
        lines.append(line)
    return lines


def vgrad(w, h, c1, c2):
    img = Image.new("RGB", (w, h))
    px = img.load()
    for y in range(h):
        r = int(c1[0] + (c2[0]-c1[0])*y/h)
        g = int(c1[1] + (c2[1]-c1[1])*y/h)
        b = int(c1[2] + (c2[2]-c1[2])*y/h)
        for x in range(w):
            px[x, y] = (r, g, b)
    return img


def cover():
    W, H = 1080, 1440
    img = vgrad(W, H, PAPER, (220, 238, 226))
    d = ImageDraw.Draw(img)
    # 装饰几何
    d.ellipse([790, 60, 1010, 280], fill=SOFT)
    d.ellipse([858, 128, 952, 222], fill=GREEN)
    # 顶部两个标签
    d.rounded_rectangle([120, 150, 320, 222], radius=24, fill=SOFT)
    d.text((148, 172), "代码安全", font=F(36, True), fill=GREEN_D)
    d.rounded_rectangle([340, 150, 560, 222], radius=24, fill=GREEN)
    d.text((368, 172), "保命用法", font=F(36, True), fill=WHITE)
    # 主卡片
    d.rounded_rectangle([70, 300, W-70, 1140], radius=40, fill=WHITE, outline=GREEN, width=5)
    # 主标题
    d.text((120, 350), "别把代码", font=F(78, True), fill=INK)
    d.text((120, 442), "喂云端AI", font=F(78, True), fill=GREEN_D)
    # 副标题（单行）
    d.text((122, 558), "本地优先，打工人保命用法", font=F(44, True), fill=INK)
    # 三个工具 pill
    pills = [("code-review-graph", "本地代码地图"),
             ("wigolo", "本地搜索免 key"),
             ("claude-code-router", "密钥留本机")]
    y = 660
    for name, desc in pills:
        d.rounded_rectangle([120, y, W-120, y+80], radius=20, fill=SOFT)
        d.text((150, y+14), name, font=F(36, True), fill=GREEN_D)
        d.text((150, y+52), desc, font=F(30, False), fill=GREY)
        y += 96
    # 底部品牌胶囊
    d.rounded_rectangle([330, 1000, 750, 1130], radius=65, fill=GREEN)
    d.text((430, 1038), "打工人北北", font=F(52, True), fill=WHITE)
    img.save(os.path.join(OUT, "xhs_cover_local_first_3x4.png"))
    print("cover done")


def card(idx, title, body, fname):
    W, H = 1080, 1440
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([60, 80, W-60, H-80], radius=44, fill=WHITE, outline=GREEN, width=5)
    # 序号圆
    d.ellipse([100, 130, 240, 270], fill=GREEN)
    d.text((140, 165), str(idx), font=F(80, True), fill=WHITE)
    # 标题
    for i, ln in enumerate(wrap(title, F(54, True), W-220, d)):
        d.text((140, 320 + i*72), ln, font=F(54, True), fill=INK)
    # 正文
    for i, ln in enumerate(wrap(body, F(42, False), W-220, d)):
        d.text((140, 640 + i*64), ln, font=F(42, False), fill=GREY)
    img.save(os.path.join(OUT, fname))
    print(fname, "done")


def gzh_header():
    W, H = 900, 383
    img = vgrad(W, H, GREEN_D, GREEN)
    d = ImageDraw.Draw(img)
    # 装饰
    d.ellipse([700, -60, 900, 140], fill=(255, 255, 255))
    d.ellipse([760, 0, 860, 100], fill=GREEN_D)
    # 标题（两行）
    for i, ln in enumerate(wrap("本地优先的 AI 编码工具：把代码留在自己机器", F(42, True), W-300, d)):
        d.text((50, 80 + i*58), ln, font=F(42, True), fill=WHITE)
    # 品牌胶囊
    d.rounded_rectangle([650, 280, 840, 348], radius=34, fill=WHITE)
    d.text((698, 298), "小木", font=F(36, True), fill=GREEN_D)
    img.save(os.path.join(OUT, "gzh_header_local_first.png"))
    print("gzh header done")


if __name__ == "__main__":
    cover()
    card(1, "code-review-graph", "本地给代码建地图\nAI 只读该读的\n不把整库传出去", "xhs_card1_local_first_3x4.png")
    card(2, "wigolo", "本地搜索/抓取/爬\n免 API key\n$0/次不连云端", "xhs_card2_local_first_3x4.png")
    card(3, "claude-code-router", "本地控制面\n统一调度多模型\n密钥留你本机", "xhs_card3_local_first_3x4.png")
    gzh_header()
    print("ALL DONE")
