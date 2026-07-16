#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""渲染 ECC 译介长图(1080竖版) + 3:4 封面图。"""
import os, re
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = r"D:\WorkBuddyProjects\ziliaoku\output\posts\2026-07-09"
W = 1080
PAD = 64

REG = [r"C:\Windows\Fonts\msyh.ttc", r"C:\Windows\Fonts\simhei.ttf", r"C:\Windows\Fonts\simsun.ttc"]
BOLD = [r"C:\Windows\Fonts\msyhbd.ttc", r"C:\Windows\Fonts\simhei.ttf", r"C:\Windows\Fonts\msyh.ttc"]

def load(paths, size, index=0):
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size, index=index)
            except Exception:
                continue
    return ImageFont.load_default()

F_TITLE = load(BOLD, 46)
F_H     = load(BOLD, 36)
F_BODY  = load(REG, 30)
F_QUOTE = load(REG, 28)
F_NOTE  = load(REG, 28)
F_SRC   = load(REG, 24)

blocks = [
    ("title", "译介｜GitHub 22万★神库 affaan-m/ECC"),
    ("sep", ""),
    ("h", "📌 它是什么"),
    ("body", "不是配置文件堆，是一整套 harness 优化系统：skills（技能）、memory（记忆）、security（安全）打包好。跨 Claude Code、Codex、Cursor 等 7 个 AI 编程助手通用。OSS 永久 MIT 免费。"),
    ("sep", ""),
    ("h", "🔥 我重点看的 3 块"),
    ("body", "① 省 token：Token Optimization + Memory Persistence 两块，用 hooks 自动存读上下文。长会话不用每次从头重灌。"),
    ("body", "② 安全兜底：AgentShield 做沙箱加净化，Agent 跑命令不裸奔。"),
    ("body", "③ 不硬塞全家桶：261 个 skills 别全装，按需取。"),
    ("sep", ""),
    ("h", "💬 我的落地（按文档，未全套实测）"),
    ("note", "1) 新手别一上来全接。开源 MIT 免费够用；Pro 付费版（托管私有库）我没买，没必要。"),
    ("note", "2) 我先接 memory 一块：hooks 自动存读上下文，思路跟我半自动攒素材库一致——会话不丢前情，token 肉眼可见地省。"),
    ("note", "3) Claude Code 裸跑命令我踩过雷，所以 AgentShield 那块最对我胃口。"),
    ("note", "4) 一句话：工具不在多，把 memory + skills 这两块用顺，比囤 100 个插件强。"),
    ("sep", ""),
    ("src", "来源：github.com/affaan-m/ECC（22万★）· 译介+个人理解，非原库立场；README 读法，未全套实测"),
]

def tokenize(text):
    return [m.group() for m in re.finditer(r"[A-Za-z0-9]+|[\u4e00-\u9fff]|[^\s]|\s+", text)]

def wrap(draw, toks, font, max_w):
    lines, cur, cur_w = [], "", 0.0
    for tk in toks:
        w = draw.textlength(tk, font=font)
        if cur_w + w <= max_w:
            cur += tk; cur_w += w
        else:
            if cur.strip(): lines.append(cur.strip())
            cur, cur_w = tk, w
    if cur.strip(): lines.append(cur.strip())
    return lines

STYLE = {
    "title": (F_TITLE, 66, (20, 20, 20), 0, 18),
    "h":     (F_H, 52, (196, 58, 38), 0, 14),
    "body":  (F_BODY, 46, (45, 45, 45), 0, 12),
    "quote": (F_QUOTE, 42, (95, 95, 95), 26, 12),
    "note":  (F_NOTE, 42, (22, 92, 140), 26, 12),
    "src":   (F_SRC, 34, (150, 150, 150), 0, 8),
}

# ---- 长图 ----
img = Image.new("RGB", (W, 20000), (255, 255, 255))
draw = ImageDraw.Draw(img)
y = PAD
max_w = W - 2 * PAD
for kind, text in blocks:
    if kind == "sep":
        y += 8
        draw.line([(PAD, y), (W - PAD, y)], fill=(225, 225, 225), width=1)
        y += 20
        continue
    font, lh, color, indent, gap = STYLE.get(kind, (F_BODY, 46, (45, 45, 45), 0, 12))
    for line in wrap(draw, tokenize(text), font, max_w - indent):
        draw.text((PAD + indent, y), line, font=font, fill=color)
        y += lh
    y += gap
y += PAD
img = img.crop((0, 0, W, y))
LONG = os.path.join(OUT_DIR, "ecc_longimage.png")
img.save(LONG, "PNG")
print("SAVED LONG:", LONG, img.size)

# ---- 3:4 封面 ----
CW, CH = 1080, 1440
cover = Image.new("RGB", (CW, CH), (28, 28, 32))
cd = ImageDraw.Draw(cover)
# 顶部色块
cd.rectangle([0, 0, CW, 360], fill=(196, 58, 38))
cd.text((PAD, 120), "22万★ Agent 神库", font=load(BOLD, 60), fill=(255, 255, 255))
cd.text((PAD, 210), "我留下的 3 个理由", font=load(REG, 38), fill=(255, 240, 235))
# 中部大字
cd.text((PAD, 480), "affaan-m/ECC", font=load(BOLD, 52), fill=(255, 255, 255))
lines = ["不是配置堆，是整套", "harness 优化系统", "skills · memory · security", "跨 7 个 AI 助手通用"]
yy = 620
for ln in lines:
    cd.text((PAD, yy), ln, font=load(REG, 36), fill=(220, 220, 225))
    yy += 56
# 底部
cd.text((PAD, 1180), "译介自 GitHub · 开源 MIT 免费", font=load(REG, 30), fill=(170, 170, 175))
cd.text((PAD, 1240), "实操博主视角，非原库立场", font=load(REG, 28), fill=(140, 140, 145))
COVER = os.path.join(OUT_DIR, "ecc_cover.png")
cover.save(COVER, "PNG")
print("SAVED COVER:", COVER, cover.size)
