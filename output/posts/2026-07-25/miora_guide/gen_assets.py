# -*- coding: utf-8 -*-
"""Miora 攻略双版配图：小红书封面+3卡片(3:4) / 公众号头图(900x383)。"""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))

# 字体
FB = "C:/Windows/Fonts/msyhbd.ttc"   # 粗体
FR = "C:/Windows/Fonts/msyh.ttc"     # 常规

def font(size, bold=True):
    return ImageFont.truetype(FB if bold else FR, size)

# 主题色（摸鱼绿主 + 设计橙点缀）
GREEN   = (38, 156, 94)
GREEN_D = (26, 110, 66)
GREEN_L = (224, 244, 233)
SOFT    = (247, 249, 247)
INK     = (33, 40, 38)
AMBER   = (217, 119, 6)
AMBER_S = (252, 238, 214)
CARD_BG = (255, 255, 255)
LINE    = (225, 230, 227)

def wrap(draw, text, fnt, max_w):
    """按像素宽度折行（中文逐字）。"""
    lines, cur = [], ""
    for ch in text:
        if draw.textlength(cur + ch, font=fnt) <= max_w:
            cur += ch
        else:
            lines.append(cur); cur = ch
    if cur:
        lines.append(cur)
    return lines

def capsule(draw, x, y, text, fill, tcolor, fnt, pad=14):
    w = draw.textlength(text, font=fnt) + pad * 2
    h = fnt.size + pad
    draw.rounded_rectangle([x, y, x + w, y + h], radius=h // 2, fill=fill)
    draw.text((x + pad, y + (h - fnt.size) // 2 - 2), text, font=fnt, fill=tcolor)
    return w, h

# ---------------- 小红书封面 1080x1440 ----------------
def make_cover():
    W, H = 1080, 1440
    img = Image.new("RGB", (W, H), SOFT)
    d = ImageDraw.Draw(img)
    # 顶部色块
    d.rectangle([0, 0, W, 470], fill=GREEN)
    d.rectangle([0, 440, W, 470], fill=AMBER)
    # 品牌胶囊
    capsule(d, 60, 56, "打工人北北", GREEN_D, (255, 255, 255), font(34))
    # 主标题
    d.text((60, 150), "腾讯 Miora", font=font(96), fill=(255, 255, 255))
    d.text((60, 270), "注册送 1000 积分", font=font(58, False), fill=(255, 245, 225))
    d.text((60, 350), "我先扒了官方信息", font=font(46, False), fill=(235, 245, 238))
    # 中部卡片区
    items = [
        ("不是又一个生图工具", "一句话出 图+视频+3D+UI 整套"),
        ("最戳我的是「记忆」", "丢参考图 逆向拆出你的风格"),
        ("3 个坑要记牢", "积分烧得快·细节要收尾"),
    ]
    y = 540
    for i, (t, s) in enumerate(items):
        d.rounded_rectangle([60, y, W - 60, y + 250], radius=28, fill=CARD_BG, outline=GREEN, width=3)
        d.rounded_rectangle([60, y, 130, y + 250], radius=28, fill=GREEN_L)
        d.text((78, y + 95), str(i + 1), font=font(90, True), fill=GREEN)
        for j, ln in enumerate(wrap(d, t, font(44, True), 760)):
            d.text((160, y + 40 + j * 56), ln, font=font(44, True), fill=INK)
        for j, ln in enumerate(wrap(d, s, font(34, False), 760)):
            d.text((160, y + 140 + j * 44), ln, font=font(34, False), fill=(110, 120, 116))
        y += 270
    # 底部钩子
    d.rounded_rectangle([60, y + 10, W - 60, y + 110], radius=24, fill=AMBER_S)
    d.text((84, y + 34), "我的判断：拿它打初稿，定稿自己卡", font=font(38, True), fill=AMBER)
    out = os.path.join(BASE, "xhs_cover_miora_3x4.png")
    img.save(out, quality=90)
    print("cover ->", out)

# ---------------- 小红书文字卡片 3:4 ----------------
def make_card(idx, title, lines, accent):
    W, H = 1080, 1440
    img = Image.new("RGB", (W, H), CARD_BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 200], fill=accent)
    capsule(d, 60, 70, "打工人北北", (255, 255, 255), accent if False else (255, 255, 255), font(32))
    d.text((60, 60), "", font=font(32))
    # 标题
    for j, ln in enumerate(wrap(d, title, font(60, True), 920)):
        d.text((60, 250 + j * 76), ln, font=font(60, True), fill=INK)
    # 分隔
    d.line([60, 250 + len(wrap(d, title, font(60, True), 920)) * 76 + 30, W - 60, 250 + len(wrap(d, title, font(60, True), 920)) * 76 + 30], fill=LINE, width=3)
    # 内容
    yy = 250 + len(wrap(d, title, font(60, True), 920)) * 76 + 90
    for i, ln in enumerate(lines):
        d.ellipse([70, yy + 14, 92, yy + 36], fill=accent)
        for j, sub in enumerate(wrap(d, ln, font(44, False), 880)):
            d.text((120, yy + j * 56), sub, font=font(44, False), fill=(70, 80, 76))
        yy += len(wrap(d, ln, font(44, False), 880)) * 56 + 36
    out = os.path.join(BASE, f"xhs_card{idx}_miora_3x4.png")
    img.save(out, quality=90)
    print("card ->", out)

# ---------------- 公众号头图 900x383 ----------------
def make_header():
    W, H = 900, 383
    img = Image.new("RGB", (W, H), GREEN)
    d = ImageDraw.Draw(img)
    # 右侧装饰圆
    d.ellipse([W - 260, -120, W + 80, 260], fill=GREEN_D)
    d.ellipse([W - 160, 180, W + 120, 460], fill=(30, 130, 80))
    # 品牌胶囊
    capsule(d, 56, 50, "小木", (255, 255, 255), GREEN_D, font(30))
    # 主标题
    d.text((56, 110), "腾讯 Miora 全量上线", font=font(52, True), fill=(255, 255, 255))
    d.text((56, 185), "这个新工具，值不值得冲？", font=font(38, False), fill=(232, 245, 238))
    d.text((56, 255), "注册送 1000 积分 · 创意设计版 WorkBuddy", font=font(28, False), fill=(210, 235, 220))
    out = os.path.join(BASE, "gzh_header_miora.png")
    img.save(out, quality=90)
    print("header ->", out)

if __name__ == "__main__":
    make_cover()
    make_card(1, "不是又一个生图工具", ["你丢一句需求 / 一张参考图", "它自己拆任务分给多个专家 Agent", "最后在同一画布给你整套视觉"], GREEN)
    make_card(2, "最戳我的是「记忆」", ["官方演示：丢一张参考封面", "它逆向拆出配色·版式·字体气质", "照着出新的，风格能对上"], AMBER)
    make_card(3, "3 个坑要记牢", ["积分不是无限的，复杂需求烧得快", "一次出整套爽，细节还得自己调", "风格偶尔漂，重要项目别全交"], GREEN_D)
    make_header()
