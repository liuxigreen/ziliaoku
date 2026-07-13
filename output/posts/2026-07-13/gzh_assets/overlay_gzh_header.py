from PIL import Image, ImageDraw, ImageFont
import os, sys

src = r"D:/WorkBuddyProjects/ziliaoku/output/posts/2026-07-13/gzh_assets/Wide_horizontal_editorial_maga_2026-07-13T14-18-46.png"
out = r"D:/WorkBuddyProjects/ziliaoku/output/posts/2026-07-13/gzh_assets/gzh_header_ai_team.png"

img = Image.open(src)
W, H = img.size
# target 2.35:1, e.g. 900x383
out_w, out_h = 900, 383
# crop from center to target aspect ratio
src_ratio = W / H
target_ratio = out_w / out_h
if src_ratio > target_ratio:
    # too wide, crop width
    new_w = int(H * target_ratio)
    left = (W - new_w) // 2
    top = 0
    crop_box = (left, top, left + new_w, H)
else:
    # too tall, crop height
    new_h = int(W / target_ratio)
    left = 0
    top = (H - new_h) // 2
    crop_box = (left, top, W, top + new_h)

cropped = img.crop(crop_box).resize((out_w, out_h), Image.LANCZOS)

# Font paths: try Windows common fonts
def find_font():
    candidates = [
        r"C:/Windows/Fonts/msyhbd.ttc",
        r"C:/Windows/Fonts/msyh.ttc",
        r"C:/Windows/Fonts/simhei.ttf",
        r"C:/Windows/Fonts/simsun.ttc",
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return None

font_path = find_font()
if not font_path:
    print("No CJK font found")
    sys.exit(1)

# Draw surface must exist before we measure text lengths
draw = ImageDraw.Draw(cropped)

# Overlay: main title on green left side, split into two short lines
main_lines = ["4个AI组队", "吊打一个AI单打"]
sub_lines = ["多智能体分工，", "才是真实生产力"]

# The green left block is roughly 1/3 of the image width. Keep text within it.
green_right = int(out_w * 0.28)  # left green area ends at ~28% width

# Try smaller font until each line fits within green block
max_line_w = green_right - int(out_w * 0.08)
for size in [int(out_w * 0.055), int(out_w * 0.050), int(out_w * 0.045), int(out_w * 0.040)]:
    font_main = ImageFont.truetype(font_path, size)
    if all(draw.textlength(line, font=font_main) <= max_line_w for line in main_lines):
        break

font_sub = ImageFont.truetype(font_path, int(font_main.size * 0.62))

# Draw a text line with shadow
def draw_text_line(draw, text, font, x, y, fill, shadow):
    for dx, dy, color in [(2, 2, shadow), (0, 0, fill)]:
        draw.text((x + dx, y + dy), text, font=font, fill=color)
    return draw.textbbox((x, y), text, font=font)

x = int(out_w * 0.055)
y = int(out_h * 0.18)
for line in main_lines:
    bbox = draw_text_line(draw, line, font_main, x, y, "#FFFFFF", "#00000060")
    y = bbox[3] + int(out_h * 0.02)

y += int(out_h * 0.02)
for line in sub_lines:
    bbox = draw_text_line(draw, line, font_sub, x, y, "#F0FDF4", "#00000055")
    y = bbox[3] + int(out_h * 0.015)

# Brand at bottom left, small and inside green area
brand_text = "打工人北北"
font_brand = ImageFont.truetype(font_path, int(out_w * 0.028))
by = out_h - int(out_h * 0.16)
bx = x
for dx, dy, color in [(1, 1, "#00000060"), (0, 0, "#FFFFFF")]:
    draw.text((bx + dx, by + dy), brand_text, font=font_brand, fill=color)

cropped.save(out, "PNG")
print(f"saved: {out}")
