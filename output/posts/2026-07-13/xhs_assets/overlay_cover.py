from PIL import Image, ImageDraw, ImageFont
import os

base_dir = r"D:\WorkBuddyProjects\ziliaoku\output\posts\2026-07-13\xhs_assets"
src = os.path.join(base_dir, "Create_a_finished_3_4_vertical_2026-07-13T13-51-51.png")
out = os.path.join(base_dir, "xhs_cover_ai_team.png")

img = Image.open(src)
W, H = img.size
draw = ImageDraw.Draw(img)

# 标题分两行：主标题 + 副标题，放在上半部分红黑色块区域
main_title = "AI干活总掉链子？"
sub_title = "不是AI太笨，是你派活方式错了"

font_main = ImageFont.truetype(r"C:\Windows\Fonts\msyhbd.ttc", int(W * 0.115))
font_sub = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", int(W * 0.055))

# 主标题位置：x 居中，y 在红黑色块下 1/3 处
bbox = draw.textbbox((0, 0), main_title, font=font_main)
main_w = bbox[2] - bbox[0]
main_h = bbox[3] - bbox[1]
x_main = (W - main_w) // 2
y_main = int(H * 0.18)

# 副标题
bbox2 = draw.textbbox((0, 0), sub_title, font=font_sub)
sub_w = bbox2[2] - bbox2[0]
sub_h = bbox2[3] - bbox2[1]
x_sub = (W - sub_w) // 2
y_sub = y_main + main_h + int(H * 0.03)

# 加粗阴影描边，提高缩略图可读性
for dx in [-3, -2, -1, 0, 1, 2, 3]:
    for dy in [-3, -2, -1, 0, 1, 2, 3]:
        draw.text((x_main + dx, y_main + dy), main_title, font=font_main, fill="#1a1a1a")
        draw.text((x_sub + dx, y_sub + dy), sub_title, font=font_sub, fill="#1a1a1a")

draw.text((x_main, y_main), main_title, font=font_main, fill="#ffffff")
draw.text((x_sub, y_sub), sub_title, font=font_sub, fill="#fff5f0")

img.save(out, "PNG")
print(f"saved: {out}")
