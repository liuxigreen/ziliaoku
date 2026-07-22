#!/usr/bin/env python3
"""生成「我用Claude Code踩的3个坑」双版配图（纯 PIL，中文不乱码）。
小红书：封面 3:4 + 3 张坑位卡片 3:4（叠「打工人北北」）
公众号：头图 2.35:1（叠「小木」，必填）
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
AMBER   = (217, 119, 6)
AMBER_S = (254, 243, 199)
RED     = (214, 52, 64)        # 坑/警示
RED_S   = (255, 235, 236)


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
    img = vgrad(W, H, PAPER, (226, 240, 230))
    d = ImageDraw.Draw(img)
    d.ellipse([800, 60, 1004, 264], fill=SOFT)
    d.ellipse([864, 124, 952, 212], fill=RED)
    # 顶部两个标签（实测/翻车）
    d.rounded_rectangle([120, 150, 330, 222], radius=24, fill=AMBER_S)
    d.text((150, 172), "半年实测", font=F(36, True), fill=AMBER)
    d.rounded_rectangle([350, 150, 560, 222], radius=24, fill=RED_S)
    d.text((378, 172), "3次翻车", font=F(36, True), fill=RED)
    # 主卡片
    d.rounded_rectangle([70, 300, W-70, 1140], radius=40, fill=WHITE, outline=RED, width=5)
    # 主标题
    d.text((120, 350), "我用Claude Code", font=F(70, True), fill=INK)
    d.text((120, 440), "踩的3个坑", font=F(78, True), fill=RED)
    # 副标题
    d.text((122, 556), "北北替你踩，能避就避", font=F(42, True), fill=INK)
    # 三个坑 pill
    pills = [("① 当黑盒甩需求", "返工比写还累"),
             ("② 不写开发文档", "CC 立刻失忆"),
             ("③ 全自动一把梭", "报错雪崩")]
    y = 668
    for name, desc in pills:
        d.rounded_rectangle([120, y, W-120, y+80], radius=20, fill=RED_S)
        d.text((150, y+14), name, font=F(36, True), fill=RED)
        d.text((150, y+52), desc, font=F(30, False), fill=GREY)
        y += 96
    # 底部品牌胶囊
    d.rounded_rectangle([330, 1000, 750, 1130], radius=65, fill=GREEN)
    d.text((430, 1038), "打工人北北", font=F(52, True), fill=WHITE)
    img.save(os.path.join(OUT, "xhs_cover_claude_code_pitfalls_3x4.png"))
    print("cover done")


def card(idx, title, body, fname):
    W, H = 1080, 1440
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([60, 80, W-60, H-80], radius=44, fill=WHITE, outline=RED, width=5)
    # 序号圆
    d.ellipse([100, 130, 240, 270], fill=RED)
    d.text((138, 165), str(idx), font=F(80, True), fill=WHITE)
    # 标题
    for i, ln in enumerate(wrap(title, F(52, True), W-220, d)):
        d.text((140, 320 + i*70), ln, font=F(52, True), fill=INK)
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
    for i, ln in enumerate(wrap("我用Claude Code踩的3个坑", F(40, True), W-300, d)):
        d.text((50, 80 + i*56), ln, font=F(40, True), fill=WHITE)
    d.rounded_rectangle([650, 280, 840, 348], radius=34, fill=WHITE)
    d.text((698, 298), "小木", font=F(34, True), fill=GREEN_D)
    img.save(os.path.join(OUT, "gzh_header_claude_code_pitfalls.png"))
    print("gzh header done")


if __name__ == "__main__":
    cover()
    card(1, "坑① · 当黑盒甩需求", "先给方向+约束\n让它先列计划再跑", "xhs_card1_claude_code_pitfalls_3x4.png")
    card(2, "坑② · 不写开发文档", "留 dev docs 记决策\nCC 才不跑偏", "xhs_card2_claude_code_pitfalls_3x4.png")
    card(3, "坑③ · 全自动一把梭", "拆小步+加检查点\n拒绝报错雪崩", "xhs_card3_claude_code_pitfalls_3x4.png")
    gzh_header()
    print("ALL DONE")
