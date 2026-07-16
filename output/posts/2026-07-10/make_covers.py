#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""给生成的封面去角标水印 + 叠中文标题。复用 managed venv (Pillow)。"""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = r"D:\WorkBuddyProjects\ziliaoku\output\posts\2026-07-10"
FONT = r"C:\Windows\Fonts\msyh.ttc"  # 微软雅黑

def font(size, idx=0):
    return ImageFont.truetype(FONT, size, index=idx)

def cover_xhs(src, dst):
    im = Image.open(src).convert("RGB")
    im = im.resize((1080, 1440))
    W, H = im.size
    d = ImageDraw.Draw(im, "RGBA")
    # 底部暗化面板（同时压住角标水印）
    panel = Image.new("RGBA", (W, 520), (8, 12, 28, 178))
    im.putalpha(255)
    base = im.convert("RGBA")
    base.alpha_composite(panel, (0, H - 520))
    im = base.convert("RGB")
    d = ImageDraw.Draw(im, "RGBA")
    # 标题
    title = "100+ 能跑的 AI 应用"
    sub = "GitHub 11.7万星 · 开源模板词典"
    d.text((60, H - 460), title, font=font(72), fill=(255, 255, 255, 255))
    d.text((62, H - 360), sub, font=font(34), fill=(150, 210, 255, 255))
    d.text((62, H - 300), "#AI应用 #效率工具 #Agent", font=font(30), fill=(200, 210, 230, 230))
    im.save(dst, "PNG")
    print("xhs cover ->", dst)

def cover_wechat(src, dst):
    im = Image.open(src).convert("RGB")
    # 1536x1024 -> 1280x720 (16:9) 居中裁切
    im = im.resize((1280, 853))
    left = (1280 - 1280) // 2
    top = (853 - 720) // 2
    im = im.crop((left, top, left + 1280, top + 720))
    W, H = im.size
    base = im.convert("RGBA")
    panel = Image.new("RGBA", (W, 360), (8, 12, 28, 170))
    base.alpha_composite(panel, (0, 0))  # 顶部暗化放标题
    im = base.convert("RGB")
    d = ImageDraw.Draw(im, "RGBA")
    title = "别再从头造轮子"
    sub = "GitHub 11.7万星 · 100+ 能直接跑的 AI 应用模板"
    d.text((60, 70), title, font=font(64), fill=(255, 255, 255, 255))
    d.text((62, 170), sub, font=font(30), fill=(150, 210, 255, 255))
    im.save(dst, "PNG")
    print("wechat cover ->", dst)

if __name__ == "__main__":
    cover_xhs(
        os.path.join(BASE, "Minimalist_tech_illustration___2026-07-10T11-33-26.png"),
        os.path.join(BASE, "cover_awesome_xhs_3x4.png"),
    )
    cover_wechat(
        os.path.join(BASE, "Wide_minimalist_tech_banner__d_2026-07-10T11-33-26.png"),
        os.path.join(BASE, "cover_awesome_wechat_16x9.png"),
    )
