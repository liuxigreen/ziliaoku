# -*- coding: utf-8 -*-
"""Claude Skills 实战双版配图：小红书封面+3卡片(3:4) / 公众号头图(900x383)。"""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))

FB = "C:/Windows/Fonts/msyhbd.ttc"   # 粗体
FR = "C:/Windows/Fonts/msyh.ttc"     # 常规

def font(size, bold=True):
    return ImageFont.truetype(FB if bold else FR, size)

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
    d.rectangle([0, 0, W, 470], fill=GREEN)
    d.rectangle([0, 440, W, 470], fill=AMBER)
    capsule(d, 60, 56, "打工人北北", GREEN_D, (255, 255, 255), font(34))
    d.text((60, 140), "Claude Skills 爆了", font=font(86), fill=(255, 255, 255))
    d.text((60, 250), "我早写了", font=font(64, False), fill=(255, 245, 225))
    d.text((60, 345), "把双平台发布流程焊死进 Skill", font=font(40, False), fill=(235, 245, 238))
    items = [
        ("单聊会失忆", "流程只在对话里，没在文件里"),
        ("我的 Skill 干了啥", "9步流程+资产清单+已知坑写死"),
        ("隔一夜还记得", "流程在文件里，不在我脑子里"),
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
    d.rounded_rectangle([60, y + 10, W - 60, y + 110], radius=24, fill=AMBER_S)
    d.text((84, y + 34), "你给 AI 写过 Skill 吗？", font=font(38, True), fill=AMBER)
    out = os.path.join(BASE, "xhs_cover_claude_skills_3x4.png")
    img.save(out, quality=90)
    print("cover ->", out)

# ---------------- 小红书文字卡片 3:4 ----------------
def make_card(idx, title, lines, accent):
    W, H = 1080, 1440
    img = Image.new("RGB", (W, H), CARD_BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 200], fill=accent)
    capsule(d, 60, 70, "打工人北北", (255, 255, 255), accent if False else (255, 255, 255), font(32))
    for j, ln in enumerate(wrap(d, title, font(60, True), 920)):
        d.text((60, 250 + j * 76), ln, font=font(60, True), fill=INK)
    sep = 250 + len(wrap(d, title, font(60, True), 920)) * 76 + 30
    d.line([60, sep, W - 60, sep], fill=LINE, width=3)
    yy = sep + 60
    for i, ln in enumerate(lines):
        d.ellipse([70, yy + 14, 92, yy + 36], fill=accent)
        for j, sub in enumerate(wrap(d, ln, font(44, False), 880)):
            d.text((120, yy + j * 56), sub, font=font(44, False), fill=(70, 80, 76))
        yy += len(wrap(d, ln, font(44, False), 880)) * 56 + 36
    out = os.path.join(BASE, f"xhs_card{idx}_claude_skills_3x4.png")
    img.save(out, quality=90)
    print("card ->", out)

# ---------------- 公众号头图 900x383 ----------------
def make_header():
    W, H = 900, 383
    img = Image.new("RGB", (W, H), GREEN)
    d = ImageDraw.Draw(img)
    d.ellipse([W - 260, -120, W + 80, 260], fill=GREEN_D)
    d.ellipse([W - 160, 180, W + 120, 460], fill=(30, 130, 80))
    capsule(d, 56, 50, "小木", (255, 255, 255), GREEN_D, font(30))
    d.text((56, 110), "Claude Skills 大火", font=font(52, True), fill=(255, 255, 255))
    d.text((56, 185), "我早把发布流程焊进 Skill", font=font(38, False), fill=(232, 245, 238))
    d.text((56, 255), "把会忘的流程，变成不会忘的文件", font=font(28, False), fill=(210, 235, 220))
    out = os.path.join(BASE, "gzh_header_claude_skills.png")
    img.save(out, quality=90)
    print("header ->", out)

if __name__ == "__main__":
    make_cover()
    make_card(1, "单聊会失忆", ["你让 AI 发一次双平台文，它干得挺好", "第二天再说「再发一篇」", "它又把流程问一遍：封面多大、插画啥格式"], GREEN)
    make_card(2, "我的 Skill 干了啥", ["把 9 步流程 + 资产清单 + 已知坑", "写成一个 skill 文件", "加载就走，不跳步不漏资产"], AMBER)
    make_card(3, "隔一夜还记得", ["流程写在文件里，不在我脑子里", "连出两篇隔一夜照样清楚", "这就是焊进 Skill 的用处"], GREEN_D)
    make_header()
