# -*- coding: utf-8 -*-
"""PIL 叠中文标题到 ponyo 无字底图（规避 AI 生图中文乱码 + 数字幻觉）。
使用相对坐标，适配 ImageGen 实际返回的任何分辨率。
小红书 3:4 + 公众号 2.35:1。"""
from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = "C:/Windows/Fonts/simhei.ttf"  # 黑体

def font(sz):
    return ImageFont.truetype(FONT, int(sz))

def shadow_text(draw, xy, text, fnt, fill, shadow=(0, 0, 0)):
    x, y = xy
    draw.text((x + 2, y + 2), text, font=fnt, fill=shadow + (170,))
    draw.text((x, y), text, font=fnt, fill=fill)

# ---------- 小红书 3:4 ----------
xhs = Image.open(os.path.join(HERE, "base_xhs.png")).convert("RGBA")
W, H = xhs.size
ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(ov)
# 底部渐隐底
band = int(H * 0.42)
for i in range(band):
    a = int(210 * (i / band))
    d.rectangle([0, H - i, W, H - i], fill=(8, 10, 26, a))
# 顶部标签
tw, th = int(W * 0.20), int(H * 0.038)
d.rectangle([int(W*0.06), int(H*0.05), int(W*0.06)+tw, int(H*0.05)+th], fill=(231, 76, 60, 235))
d.text((int(W*0.06)+int(W*0.012), int(H*0.05)+int(th*0.18)), "AI 编程干货", font=font(int(th*0.64)), fill=(255, 255, 255, 255))
# 大号「32」
big = int(H * 0.24)
shadow_text(d, (int(W*0.06), int(H*0.46)), "32", fnt=font(big), fill=(241, 196, 15, 255))
d.text((int(W*0.06), int(H*0.46)+big), "招", font=font(int(H*0.075)), fill=(255, 255, 255, 255))
# 主标题两行
ts = int(H * 0.052)
shadow_text(d, (int(W*0.062), int(H*0.70)), "Claude Code 技巧", fnt=font(ts), fill=(255, 255, 255, 255))
shadow_text(d, (int(W*0.062), int(H*0.70)+int(ts*1.18)), "我留这 5 个", fnt=font(ts), fill=(255, 255, 255, 255))
xhs = Image.alpha_composite(xhs, ov).convert("RGB")
xhs.save(os.path.join(HERE, "cover_xhs.png"))
print("saved cover_xhs.png", xhs.size)

# ---------- 公众号 2.35:1 ----------
we = Image.open(os.path.join(HERE, "base_wechat.png")).convert("RGBA")
W, H = we.size
ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(ov)
# 左三分之一渐隐底
band = int(W * 0.42)
for i in range(band):
    a = int(215 * (1 - i / band))
    d.rectangle([i, 0, i, H], fill=(6, 8, 22, max(0, a)))
# 顶部标签
tw, th = int(W*0.13), int(H*0.16)
d.rectangle([int(W*0.035), int(H*0.075), int(W*0.035)+tw, int(H*0.075)+th], fill=(231, 76, 60, 235))
d.text((int(W*0.035)+int(W*0.012), int(H*0.075)+int(th*0.2)), "AI 编程", font=font(int(th*0.62)), fill=(255, 255, 255, 255))
# 大号「32」
big = int(H * 0.62)
shadow_text(d, (int(W*0.035), int(H*0.30)), "32", fnt=font(big), fill=(241, 196, 15, 255))
d.text((int(W*0.035), int(H*0.30)+int(big*1.02)), "招", font=font(int(H*0.20)), fill=(255, 255, 255, 255))
# 主标题
ts = int(H * 0.30)
shadow_text(d, (int(W*0.30), int(H*0.34)), "Claude Code 32 招", fnt=font(ts), fill=(255, 255, 255, 255))
shadow_text(d, (int(W*0.30), int(H*0.34)+int(ts*1.08)), "我替你筛出能落地的", fnt=font(int(H*0.27)), fill=(255, 255, 255, 255))
we = Image.alpha_composite(we, ov).convert("RGB")
we.save(os.path.join(HERE, "cover_wechat.png"))
print("saved cover_wechat.png", we.size)
