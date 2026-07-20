#!/usr/bin/env python3
"""生成 WorkBuddy 专题 双版配图（纯 PIL，零成本、中文不乱码）。
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
    d.ellipse([770, 70, 1010, 310], fill=SOFT)
    d.ellipse([840, 140, 950, 250], fill=GREEN)
    d.rounded_rectangle([120, 150, 360, 230], radius=24, fill=SOFT)
    d.text((150, 172), "限免2周", font=F(38, True), fill=GREEN_D)
    # 主卡片
    d.rounded_rectangle([70, 300, W-70, 1120], radius=40, fill=WHITE, outline=GREEN, width=5)
    # 主标题
    d.text((120, 360), "WorkBuddy", font=F(74, True), fill=GREEN_D)
    # 副标题
    for i, ln in enumerate(wrap("把重复活\n甩给 AI 打工", F(50, True), W-260, d)):
        d.text((122, 480 + i*66), ln, font=F(50, True), fill=INK)
    # 标签行
    d.rounded_rectangle([120, 700, 430, 772], radius=30, fill=SOFT)
    d.text((150, 722), "hy3免费", font=F(36, True), fill=GREEN_D)
    d.rounded_rectangle([460, 700, 770, 772], radius=30, fill=SOFT)
    d.text((490, 722), "邀请送分", font=F(36, True), fill=GREEN_D)
    # 底部品牌胶囊
    d.rounded_rectangle([330, 940, 750, 1070], radius=65, fill=GREEN)
    d.text((430, 978), "打工人北北", font=F(52, True), fill=WHITE)
    img.save(os.path.join(OUT, "xhs_cover_workbuddy_3x4.png"))
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
    for i, ln in enumerate(wrap(title, F(56, True), W-220, d)):
        d.text((140, 320 + i*74), ln, font=F(56, True), fill=INK)
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
    for i, ln in enumerate(wrap("WorkBuddy hy3限免2周：能自己干活的AI工作台", F(44, True), W-300, d)):
        d.text((50, 70 + i*62), ln, font=F(44, True), fill=WHITE)
    # 品牌胶囊
    d.rounded_rectangle([640, 270, 840, 340], radius=35, fill=WHITE)
    d.text((688, 288), "小木", font=F(36, True), fill=GREEN_D)
    img.save(os.path.join(OUT, "gzh_header_workbuddy.png"))
    print("gzh header done")


if __name__ == "__main__":
    cover()
    card(1, "重复活吃掉半天", "找选题/写稿/出图/排版\n单价低频次高，人累产出少", "xhs_card1_workbuddy_3x4.png")
    card(2, "不是聊天机器人", "给目标→自己拆步骤\n调工具查资料出成品", "xhs_card2_workbuddy_3x4.png")
    card(3, "白嫖攻略", "先注册占坑+邀请送积分\n重活优先丢给hy3", "xhs_card3_workbuddy_3x4.png")
    gzh_header()
    print("ALL DONE")
