# -*- coding: utf-8 -*-
"""生成小红书封面（叠中文）+ 3 张文字卡片（纯 PIL，3:4）。"""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = r"c:\Users\liuxi\WorkBuddy\2026-07-07-17-49-26\generated-images\Flat_modern_vector_illustratio_2026-07-15T16-04-10.png"
OUT = r"D:\WorkBuddyProjects\ziliaoku\output\posts\2026-07-16\rss_ai_daily_brief"

# 字体（Windows 自带）
FONT_DIR = r"C:\Windows\Fonts"
def font(name, sz):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), sz)

F_TITLE = font("msyhbd.ttc", 60)   # 微软雅黑粗体
F_SUB   = font("msyh.ttc", 34)
F_BODY  = font("msyh.ttc", 40)
F_TAG   = font("msyhbd.ttc", 30)
F_NAME  = font("msyhbd.ttc", 30)

MINT = (16, 185, 129)      # 摸鱼绿主色
MINT_D = (6, 95, 70)
DARK = (33, 37, 41)
WHITE = (255, 255, 255)
CARD_BG = (240, 253, 248)   # 极浅绿

def wrap(text, fnt, max_w, draw):
    lines = []
    for para in text.split("\n"):
        line = ""
        for ch in para:
            t = (line + ch)
            if draw.textlength(t, font=fnt) > max_w and line:
                lines.append(line); line = ch
            else:
                line = t
        lines.append(line)
    return lines

# ---------- 1) 封面：底图 resize 到 1080x1440，叠标题+署名 ----------
base = Image.open(BASE).convert("RGB")
base = base.resize((1080, 1440))
cv = ImageDraw.Draw(base)
# 顶部半透明深条保证标题可读
cv.rectangle([0, 0, 1080, 470], fill=(20, 30, 28, 180) if base.mode == "RGBA" else (18, 28, 26))
# 重画为 RGB 后叠
base = base.convert("RGB")
cv = ImageDraw.Draw(base)
cv.rectangle([0, 0, 1080, 470], fill=(18, 28, 26))
title_lines = ["算法喂你的", "都是二手货？", "我搭了个一手信息源"]
y = 70
for ln in title_lines:
    cv.text((60, y), ln, font=F_TITLE, fill=WHITE)
    y += 78
cv.text((60, y + 6), "RSS + AI 摘要 · 跑一周真实复盘", font=F_SUB, fill=(180, 245, 220))
# 底部署名胶囊
cv.rounded_rectangle([60, 1310, 360, 1380], radius=35, fill=MINT)
cv.text((88, 1322), "打工人北北", font=F_NAME, fill=WHITE)
cover_path = os.path.join(OUT, "xhs_cover_rss_brief_3x4.png")
base.save(cover_path, "PNG")
print("cover ->", cover_path)

# ---------- 2) 3 张文字卡片 1080x1440 ----------
cards = [
    ("为什么做", [
        "你每天刷的 AI 资讯，",
        "90% 是别人嚼过的二手货。",
        "",
        "一手信息早就在英文博客、",
        "论文、推特里——只是你",
        "没空翻。",
    ], "信息差 = 先知道"),
    ("怎么搭", [
        "① 把想看的源做成 RSS",
        "② 每天让 AI 自动摘要成",
        "   5 条中文速览",
        "③ 推到我的笔记里",
        "",
        "打开就是筛选过的重点。",
    ], "10 分钟搭完"),
    ("跑一周的 3 个坑", [
        "坑1：AI 摘要会漏关键",
        "   细节，重要的得看原文",
        "坑2：源没选好 = 垃圾进",
        "   垃圾出，别喂营销号",
        "坑3：别指望全自动，",
        "   每周清一次源",
    ], "值得 replicate"),
]

for i, (head, body_lines, tag) in enumerate(cards, 1):
    img = Image.new("RGB", (1080, 1440), CARD_BG)
    d = ImageDraw.Draw(img)
    # 顶部色块
    d.rectangle([0, 0, 1080, 200], fill=MINT)
    d.text((60, 60), head, font=F_TITLE, fill=WHITE)
    # 序号圆
    d.ellipse([900, 50, 1020, 170], fill=MINT_D)
    d.text((938, 82), str(i), font=F_TITLE, fill=WHITE)
    # 正文
    y = 280
    for ln in body_lines:
        d.text((70, y), ln, font=F_BODY, fill=DARK)
        y += 78
    # 底部标签
    d.rounded_rectangle([70, 1300, 70 + 320, 1372], radius=36, fill=WHITE)
    d.text((100, 1312), tag, font=F_TAG, fill=MINT_D)
    d.text((420, 1312), "打工人北北", font=F_NAME, fill=MINT)
    p = os.path.join(OUT, f"xhs_card{i}_rss_brief_3x4.png")
    img.save(p, "PNG")
    print("card ->", p)

print("DONE")
