from PIL import Image, ImageDraw, ImageFont

SRC = r"D:\WorkBuddyProjects\ziliaoku\output\posts\2026-07-10\punk-assets\punk-cover\awesome-llm-apps\Business_magazine_front_page_e_2026-07-10T14-44-49.png"
OUT = r"D:\WorkBuddyProjects\ziliaoku\output\posts\2026-07-10\punk-assets\punk-cover\awesome-llm-apps\cover.png"
FONT = r"C:\Windows\Fonts\simhei.ttf"  # 黑体，干净无衬线

W, H = 1410, 600
im = Image.open(SRC).convert("RGB").resize((W, H))

# 左侧渐隐底，保证文字区干净（右侧视觉渐显）
panel = Image.new("RGBA", (W, H), (0, 0, 0, 0))
pd = ImageDraw.Draw(panel)
for x in range(700):
    a = int(238 * (1 - x / 700))
    pd.line([(x, 0), (x, H)], fill=(247, 245, 240, a))
im = Image.alpha_composite(im.convert("RGBA"), panel).convert("RGB")

d = ImageDraw.Draw(im)
f_tag = ImageFont.truetype(FONT, 34)
f_title = ImageFont.truetype(FONT, 122)
f_sub = ImageFont.truetype(FONT, 46)

INK = (26, 26, 26)
BLUE = (37, 99, 235)
EMER = (16, 185, 129)
GRAY = (90, 90, 90)

# 顶部小标签
d.text((72, 120), "GitHub 117k★ 开源精选", font=f_tag, fill=EMER)

# 主标题：100+ 用蓝，余下用墨
t1, t2 = "100+", " AI 应用模板"
w1 = d.textlength(t1, font=f_title)
d.text((70, 196), t1, font=f_title, fill=BLUE)
d.text((70 + w1, 196), t2, font=f_title, fill=INK)

# 强调短线
d.rectangle([72, 352, 72 + 360, 358], fill=BLUE)

# 副标题
d.text((72, 374), "从 RAG 到语音到 Agent", font=f_sub, fill=INK)
d.text((72, 436), "抄作业就用它", font=f_sub, fill=GRAY)

im.save(OUT)
print("saved", OUT, im.size)
