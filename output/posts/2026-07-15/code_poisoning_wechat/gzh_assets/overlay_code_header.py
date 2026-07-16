# -*- coding: utf-8 -*-
"""把宽幅无字视觉裁成 2.35:1 (900x383) 公众号头图，并 PIL 叠中文标题。
纪律：图内不放字（AI 生图易乱码），标题用 PIL 叠。
"""
from PIL import Image, ImageDraw, ImageFont
import os, sys

src = r"D:/WorkBuddyProjects/ziliaoku/output/posts/2026-07-15/code_poisoning_wechat/gzh_assets/Editorial_magazine_style_illus_2026-07-15T15-01-18.png"
out = r"D:/WorkBuddyProjects/ziliaoku/output/posts/2026-07-15/code_poisoning_wechat/gzh_assets/gzh_header_code_poisoning.png"

img = Image.open(src).convert("RGB")
W, H = img.size
out_w, out_h = 900, 383
src_ratio = W / H
target_ratio = out_w / out_h
if src_ratio > target_ratio:
    new_w = int(H * target_ratio)
    crop_box = ((W - new_w) // 2, 0, (W - new_w) // 2 + new_w, H)
else:
    new_h = int(W / target_ratio)
    crop_box = (0, (H - new_h) // 2, W, (H - new_h) // 2 + new_h)
cropped = img.crop(crop_box).resize((out_w, out_h), Image.LANCZOS)

# 左侧加半透明暗板，保证白字可读
from PIL import Image as _I
panel = _I.new("RGBA", (out_w, out_h), (0, 0, 0, 0))
pd = ImageDraw.Draw(panel)
pd.rectangle([0, 0, int(out_w * 0.52), out_h], fill=(8, 30, 22, 165))
cropped = _I.alpha_composite(cropped.convert("RGBA"), panel).convert("RGB")

def find_font():
    for c in [r"C:/Windows/Fonts/msyhbd.ttc", r"C:/Windows/Fonts/msyh.ttc",
              r"C:/Windows/Fonts/simhei.ttf", r"C:/Windows/Fonts/simsun.ttc"]:
        if os.path.exists(c):
            return c
    return None
font_path = find_font()
if not font_path:
    print("No CJK font"); sys.exit(1)

draw = ImageDraw.Draw(cropped)
main_lines = ["用AI读代码", "小心被代码反杀"]
sub_line = "你以为在指挥AI，其实是代码在指挥AI"

max_line_w = int(out_w * 0.46)
for size in [int(out_w * 0.072), int(out_w * 0.066), int(out_w * 0.060), int(out_w * 0.054)]:
    f = ImageFont.truetype(font_path, size)
    if all(draw.textlength(l, font=f) <= max_line_w for l in main_lines):
        break
font_main = f
font_sub = ImageFont.truetype(font_path, int(font_main.size * 0.40))

def draw_text(text, font, x, y, fill, shadow):
    for dx, dy, color in [(2, 2, shadow), (0, 0, fill)]:
        draw.text((x + dx, y + dy), text, font=font, fill=color)
    return draw.textbbox((x, y), text, font=font)

x = int(out_w * 0.055)
y = int(out_h * 0.16)
for line in main_lines:
    bbox = draw_text(line, font_main, x, y, "#FFFFFF", "#00000070")
    y = bbox[3] + int(out_h * 0.015)
y += int(out_h * 0.02)
draw_text(sub_line, font_sub, x, y, "#A7F3D0", "#00000060")

brand = "小木"
font_brand = ImageFont.truetype(font_path, int(out_w * 0.030))
by = out_h - int(out_h * 0.15)
for dx, dy, color in [(1, 1, "#00000060"), (0, 0, "#FFFFFF")]:
    draw.text((x + dx, by + dy), brand, font=font_brand, fill=color)

cropped.save(out, "PNG")
print("saved:", out)
