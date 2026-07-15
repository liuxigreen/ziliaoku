# -*- coding: utf-8 -*-
"""生成公众号 2.35:1 头图（900x383），从 ImageGen 横图裁剪 + PIL 叠中文。"""
from PIL import Image, ImageDraw, ImageFont

BASE = r"c:\Users\liuxi\WorkBuddy\2026-07-07-17-49-26\generated-images\Wide_flat_vector_illustration__2026-07-15T16-11-50.png"
OUT = r"D:\WorkBuddyProjects\ziliaoku\output\posts\2026-07-16\rss_ai_daily_brief\gzh_header_rss_brief.png"

F_TITLE = ImageFont.truetype(r"C:\Windows\Fonts\msyhbd.ttc", 44)
F_SUB = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", 22)
F_BRAND = ImageFont.truetype(r"C:\Windows\Fonts\msyhbd.ttc", 20)

WHITE = (255, 255, 255)
MINT = (16, 185, 129)
MINT_D = (6, 95, 70)

img = Image.open(BASE).convert("RGB")
w, h = img.size
# 2.35:1 crop from center
target_h = int(w / 2.35)
top = (h - target_h) // 2
img = img.crop((0, top, w, top + target_h))
# resize to 900x383
img = img.resize((900, 383))

# 左侧加半透明深色竖条，保证文字可读
overlay = Image.new("RGBA", (900, 383), (0, 0, 0, 0))
d = ImageDraw.Draw(overlay)
d.rectangle([0, 0, 520, 383], fill=(18, 28, 26, 210))
img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
d = ImageDraw.Draw(img)

# 标题
d.text((40, 95), "别被算法投喂了", font=F_TITLE, fill=WHITE)
d.text((40, 150), "用 RSS + AI 搭个一手信息源", font=F_SUB, fill=(180, 245, 220))
# 品牌胶囊
d.rounded_rectangle([40, 300, 190, 350], radius=25, fill=MINT)
d.text((60, 309), "小木", font=F_BRAND, fill=WHITE)
d.text((220, 309), "跑一周真实复盘", font=F_SUB, fill=(180, 245, 220))

img.save(OUT, "PNG", quality=95)
print("WROTE", OUT)
