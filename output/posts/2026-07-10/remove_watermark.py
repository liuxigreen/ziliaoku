from PIL import Image
import sys

src = "D:\\WorkBuddyProjects\\ziliaoku\\output\\posts\\2026-07-10\\小红书竖版封面_3_4_比例_极简高对比_黑红剪影_风格_只_2026-07-10T08-45-11.png"
dst = "D:\\WorkBuddyProjects\\ziliaoku\\output\\posts\\2026-07-10\\cover_claude_code_3x4_clean.png"

img = Image.open(src).convert("RGB")
w, h = img.size

# 取样左下角干净背景的平均色
sample_box = (0, int(h * 0.92), int(w * 0.15), h)
region = img.crop(sample_box)
px = list(region.getdata())
bg_color = tuple(int(sum(c[i] for c in px) / len(px)) for i in range(3))

# 覆盖右下角水印区域(约底部 12%、右侧 45%)
fill_box = (int(w * 0.55), int(h * 0.88), w, h)
img.paste(bg_color, fill_box)

img.save(dst, "PNG")
print(f"Saved: {dst}")
