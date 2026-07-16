#!/usr/bin/env python3
"""PIL 生成第三篇双出版本的所有视觉素材：小红书封面、公众号头图、文字卡片。"""
import os, sys
from PIL import Image, ImageDraw, ImageFont

base = "D:/WorkBuddyProjects/ziliaoku/output/posts/2026-07-14/ai_engineer_roadmap"
xhs_assets = os.path.join(base, "xhs_assets")
gzh_assets = os.path.join(base, "gzh_assets")

# CJK font fallback
font_candidates = [
    "C:/Windows/Fonts/msyhbd.ttc",
    "C:/Windows/Fonts/msyh.ttc",
    "C:/Windows/Fonts/simhei.ttf",
]
font_path = next((p for p in font_candidates if os.path.exists(p)), None)
if not font_path:
    print("No CJK font found")
    sys.exit(1)

# ---------- 小红书封面 ----------
def fit_text_in_width(draw, text, font_path, max_w, start_size, min_size=20):
    for size in range(start_size, min_size - 1, -2):
        font = ImageFont.truetype(font_path, size)
        if draw.textlength(text, font=font) <= max_w:
            return font
    return ImageFont.truetype(font_path, min_size)

xhs_src = os.path.join(gzh_assets, "Vertical_3_4_editorial_illustr_2026-07-14T07-10-44.png")
xhs = Image.open(xhs_src)
w, h = xhs.size
xhs_draw = ImageDraw.Draw(xhs)

# 主标题分两行，叠在底部绿块左侧；绿块大约占下 40%，全宽
line1 = "6个月用AI"
line2 = "练成工程师？"
sub = "我拆了一遍普通人能抄的部分"

xhs_font_main = fit_text_in_width(xhs_draw, line1, font_path, int(w * 0.80), int(w * 0.12))
xhs_font_line2 = fit_text_in_width(xhs_draw, line2, font_path, int(w * 0.80), int(w * 0.12))
xhs_font_sub = fit_text_in_width(xhs_draw, sub, font_path, int(w * 0.80), int(w * 0.055))

x = int(w * 0.08)
y = int(h * 0.72)

def draw_shadow_text(draw, x, y, text, font, fill, shadow):
    for dx, dy, color in [(2, 2, shadow), (0, 0, fill)]:
        draw.text((x + dx, y + dy), text, font=font, fill=color)
    return draw.textbbox((x, y), text, font=font)

bbox1 = draw_shadow_text(xhs_draw, x, y, line1, xhs_font_main, "#FFFFFF", "#00000055")
bbox2 = draw_shadow_text(xhs_draw, x, bbox1[3] + int(h * 0.015), line2, xhs_font_line2, "#FFFFFF", "#00000055")
bbox3 = draw_shadow_text(xhs_draw, x, bbox2[3] + int(h * 0.04), sub, xhs_font_sub, "#F0FDF4", "#00000045")

# brand top right
brand = "打工人北北"
brand_font = ImageFont.truetype(font_path, int(w * 0.028))
bw = xhs_draw.textlength(brand, font=brand_font)
bx = w - int(w * 0.035) - bw
by = int(h * 0.04)
draw_shadow_text(xhs_draw, bx, by, brand, brand_font, "#FFFFFF", "#00000055")

xhs_out = os.path.join(xhs_assets, "xhs_cover_roadmap.png")
xhs.save(xhs_out)
print("saved", xhs_out)

# ---------- 公众号头图 ----------
gzh_src = os.path.join(gzh_assets, "Wide_horizontal_editorial_maga_2026-07-14T07-10-44.png")
gzh = Image.open(gzh_src)
# crop to 2.35:1 from top-left-ish (900x383 target)
out_w, out_h = 900, 383
raw_w, raw_h = gzh.size
# source crop box: 2.35:1 from the image, avoid right-bottom watermark if possible
# take left 1/3 green area, full height of illustration part
src_ratio = out_w / out_h
src_h = raw_h
src_w = int(src_h * src_ratio)
left = 0
top = 0
if src_w > raw_w:
    src_w = raw_w
    src_h = int(src_w / src_ratio)
    top = 0
right = left + src_w
bottom = top + src_h
cropped = gzh.crop((left, top, right, bottom)).resize((out_w, out_h), Image.LANCZOS)

gzh_draw = ImageDraw.Draw(cropped)
g_line1 = "6个月用AI"
g_line2 = "练成工程师？"
g_sub = "普通人能抄的路线图"

g_font_main = fit_text_in_width(gzh_draw, g_line1, font_path, int(out_w * 0.28), int(out_w * 0.070))
g_font_main2 = fit_text_in_width(gzh_draw, g_line2, font_path, int(out_w * 0.28), int(out_w * 0.070))
g_font_sub = fit_text_in_width(gzh_draw, g_sub, font_path, int(out_w * 0.28), int(out_w * 0.035))

gx = int(out_w * 0.06)
gy = int(out_h * 0.22)
gb1 = draw_shadow_text(gzh_draw, gx, gy, g_line1, g_font_main, "#FFFFFF", "#00000055")
gb2 = draw_shadow_text(gzh_draw, gx, gb1[3] + int(out_h * 0.02), g_line2, g_font_main2, "#FFFFFF", "#00000055")
gb3 = draw_shadow_text(gzh_draw, gx, gb2[3] + int(out_h * 0.04), g_sub, g_font_sub, "#F0FDF4", "#00000045")

# brand bottom right
brand_font_gzh = ImageFont.truetype(font_path, int(out_w * 0.028))
gzh_brand = "小木"
bw_g = gzh_draw.textlength(gzh_brand, font=brand_font_gzh)
bx_g = out_w - int(out_w * 0.035) - bw_g
by_g = out_h - int(out_h * 0.14)
draw_shadow_text(gzh_draw, bx_g, by_g, gzh_brand, brand_font_gzh, "#FFFFFF", "#00000055")

gzh_out = os.path.join(gzh_assets, "gzh_header_roadmap.png")
cropped.save(gzh_out)
print("saved", gzh_out)

# ---------- 小红书文字卡片 ----------
def make_card(title, items, accent, bg, out_path):
    W, H = 900, 1350
    img = Image.new("RGB", (W, H), color=bg)
    draw = ImageDraw.Draw(img)
    title_font = ImageFont.truetype(font_path, int(W * 0.085))
    item_font = ImageFont.truetype(font_path, int(W * 0.055))
    y = int(H * 0.12)
    # title
    draw.text((W // 2, y), title, font=title_font, fill=accent, anchor="mm")
    y = int(H * 0.28)
    for i, text in enumerate(items, 1):
        # number badge
        r = int(W * 0.055)
        cx = int(W * 0.14)
        cy = y + r
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=accent)
        draw.text((cx, cy), str(i), font=item_font, fill="white", anchor="mm")
        # text wrapped roughly to width
        x_text = cx + r + int(W * 0.06)
        max_w = W - x_text - int(W * 0.10)
        # simple line wrapping by character
        line = ""
        line_y = y
        for ch in text:
            test = line + ch
            if draw.textlength(test, font=item_font) > max_w and line:
                draw.text((x_text, line_y + r), line, font=item_font, fill="#1F2937")
                line = ch
                line_y += int(W * 0.09)
            else:
                line = test
        if line:
            draw.text((x_text, line_y + r), line, font=item_font, fill="#1F2937")
        y = max(y + int(H * 0.18), line_y + int(W * 0.10))
    # brand
    bf = ImageFont.truetype(font_path, int(W * 0.035))
    bw = draw.textlength(brand, font=bf)
    draw.text((W - int(W * 0.05) - bw, H - int(H * 0.06)), brand, font=bf, fill="#9CA3AF")
    img.save(out_path)
    print("saved", out_path)

make_card(
    "6个月路线图",
    ["第1月：Python / Git / API 地基",
     "第2月：LLM 指令 / 结构化输出 / 工具调用",
     "第3-4月：RAG / Agent / 不该用时",
     "第5-6月：部署 / 选方向 / 拿项目练",
     "关键：每月交付一个真实项目"],
    "#059669", "#F0FDF4",
    os.path.join(xhs_assets, "card1_roadmap.png")
)
make_card(
    "普通人先啃这2块",
    ["第1月：地基别跳过，慢=快",
     "第2月：重点不是背 API，是会指挥 AI",
     "同时刻进脑子：提示注入意识",
     "别让 AI 读到来路不明的'暗指令'",
     "从身边真项目开始，别收藏吃灰"],
    "#C0202E", "#FEF2F2",
    os.path.join(xhs_assets, "card2_tips.png")
)
