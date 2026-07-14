from PIL import Image, ImageDraw, ImageFont
import sys, os

base_dir = os.path.dirname(__file__)
img_path = os.path.join(base_dir, "Vertical_3_4_editorial_illustr_2026-07-14T05-45-07.png")
out_path = os.path.join(base_dir, "xhs_cover_code_poisoning.png")

def find_font():
    for p in ["C:/Windows/Fonts/msyhbd.ttc", "C:/Windows/Fonts/msyh.ttc"]:
        if os.path.exists(p):
            return p
    return None

font_path = find_font()
if not font_path:
    print("No CJK font found")
    sys.exit(1)

img = Image.open(img_path)
w, h = img.size

draw = ImageDraw.Draw(img)

line1 = "用AI读代码"
line2 = "小心被代码反杀"
sub = "不信任的代码，会带偏你的AI"

# Fit inside red block (~65% of image width)
size_line1 = int(w * 0.085)
size_line2 = int(w * 0.085)
size_sub = int(w * 0.040)
font_line1 = ImageFont.truetype(font_path, size_line1)
font_line2 = ImageFont.truetype(font_path, size_line2)
font_sub = ImageFont.truetype(font_path, size_sub)

x = int(w * 0.05)
y = int(h * 0.74)

def draw_text_with_shadow(draw, text, font, x, y, fill, shadow):
    for dx, dy, color in [(2, 2, shadow), (0, 0, fill)]:
        draw.text((x + dx, y + dy), text, font=font, fill=color)
    bbox = draw.textbbox((x, y), text, font=font)
    return bbox

bbox1 = draw_text_with_shadow(draw, line1, font_line1, x, y, "#FFFFFF", "#00000060")
y2 = bbox1[3] + int(h * 0.02)
bbox2 = draw_text_with_shadow(draw, line2, font_line2, x, y2, "#FFFFFF", "#00000060")
y3 = bbox2[3] + int(h * 0.03)
bbox3 = draw_text_with_shadow(draw, sub, font_sub, x, y3, "#FDE8E8", "#00000055")

# Brand at top-right cream area (dark text)
brand = "打工人北北"
font_brand = ImageFont.truetype(font_path, int(w * 0.028))
bw = draw.textlength(brand, font=font_brand)
bx = w - int(w * 0.05) - bw
by = int(h * 0.05)
draw_text_with_shadow(draw, brand, font_brand, bx, by, "#1A1A1A", "#FFFFFF80")

img.save(out_path, quality=95)
print(f"saved {out_path}")
