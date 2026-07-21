#!/usr/bin/env python3
"""生成「AI让我写代码更快却变笨了」双版配图（纯 PIL，中文不乱码）。
小红书：封面 3:4 + 3 张自救动作卡片 3:4（叠「打工人北北」）
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
AMBER   = (217, 119, 6)        # 反差警示色
AMBER_S = (254, 243, 199)


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
    d.ellipse([792, 56, 1008, 272], fill=SOFT)
    d.ellipse([860, 124, 952, 216], fill=GREEN)
    # 顶部两个标签（反差/陷阱）
    d.rounded_rectangle([120, 150, 330, 222], radius=24, fill=AMBER_S)
    d.text((150, 172), "认知反差", font=F(36, True), fill=AMBER)
    d.rounded_rectangle([350, 150, 560, 222], radius=24, fill=GREEN)
    d.text((378, 172), "效率陷阱", font=F(36, True), fill=WHITE)
    # 主卡片
    d.rounded_rectangle([70, 300, W-70, 1140], radius=40, fill=WHITE, outline=GREEN, width=5)
    # 主标题
    d.text((120, 350), "用AI写代码", font=F(78, True), fill=INK)
    d.text((120, 442), "我反而变笨了", font=F(78, True), fill=GREEN_D)
    # 副标题
    d.text((122, 558), "3周实测 · 3个自救动作", font=F(44, True), fill=INK)
    # 三个自救动作 pill
    pills = [("① 关键模块自己先写", "夺回所有权"),
             ("② 每天30分钟零AI", "手感不能丢"),
             ("③ 逼AI讲为什么", "防顺着你说")]
    y = 660
    for name, desc in pills:
        d.rounded_rectangle([120, y, W-120, y+80], radius=20, fill=SOFT)
        d.text((150, y+14), name, font=F(36, True), fill=GREEN_D)
        d.text((150, y+52), desc, font=F(30, False), fill=GREY)
        y += 96
    # 底部品牌胶囊
    d.rounded_rectangle([330, 1000, 750, 1130], radius=65, fill=GREEN)
    d.text((430, 1038), "打工人北北", font=F(52, True), fill=WHITE)
    img.save(os.path.join(OUT, "xhs_cover_ai_slower_3x4.png"))
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
    d.ellipse([700, -60, 900, 140], fill=(255, 255, 255))
    d.ellipse([760, 0, 860, 100], fill=GREEN_D)
    for i, ln in enumerate(wrap("AI让我写代码更快，却更笨了", F(42, True), W-300, d)):
        d.text((50, 80 + i*58), ln, font=F(42, True), fill=WHITE)
    d.rounded_rectangle([650, 280, 840, 348], radius=34, fill=WHITE)
    d.text((698, 298), "小木", font=F(36, True), fill=GREEN_D)
    img.save(os.path.join(OUT, "gzh_header_ai_slower.png"))
    print("gzh header done")


if __name__ == "__main__":
    cover()
    card(1, "关键模块自己先写", "不再丢需求等实现\n先出初稿再让AI改\n把所有权拿回来", "xhs_card1_ai_slower_3x4.png")
    card(2, "每天30分钟零AI", "手写一个小功能\n不允许开任何助手\n手感不能丢", "xhs_card2_ai_slower_3x4.png")
    card(3, "逼AI讲为什么", "给方案必问理由\n不复读答案\n防它顺着你说", "xhs_card3_ai_slower_3x4.png")
    gzh_header()
    print("ALL DONE")
