#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""渲染 Reddit 译介长图：宽1080 竖版，CJK 自动换行 + 分节样式。"""
import os
import re
from PIL import Image, ImageDraw, ImageFont

OUT = r"D:\WorkBuddyProjects\ziliaoku\output\posts\2026-07-09\reddit_ai_content_longimage.png"
W = 1080
PAD = 64

# ---- 字体 ----
REG_CANDIDATES = [
    r"C:\Windows\Fonts\msyh.ttc",   # Microsoft YaHei
    r"C:\Windows\Fonts\simhei.ttf",  # 黑体
    r"C:\Windows\Fonts\simsun.ttc",  # 宋体
]
BOLD_CANDIDATES = [
    r"C:\Windows\Fonts\msyhbd.ttc",
    r"C:\Windows\Fonts\simhei.ttf",
    r"C:\Windows\Fonts\msyh.ttc",
]

def load(paths, size, index=0):
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size, index=index)
            except Exception:
                continue
    return ImageFont.load_default()

F_TITLE = load(BOLD_CANDIDATES, 46)
F_H     = load(BOLD_CANDIDATES, 36)
F_BODY  = load(REG_CANDIDATES, 30)
F_QUOTE = load(REG_CANDIDATES, 28)
F_NOTE  = load(REG_CANDIDATES, 28)
F_SRC   = load(REG_CANDIDATES, 24)

# ---- 内容块 ----
# kind: title / h / body / quote / note / src / sep
blocks = [
    ("title", "译介｜Reddit热帖：AI写的内容都“一个味”？老运营拆透真相"),
    ("sep", ""),
    ("h", "📌 原帖在聊啥"),
    ("body", "r/SocialMediaManagers 一个热帖：楼主做效果营销，要把跑得好的帖子改成多平台版本，但用 ChatGPT 改写后“只是换了同义词，味儿全都一样”，调起来还巨费时间。他求教：到底啥工具/方法能保住结构、又出自然的变化？"),
    ("sep", ""),
    ("h", "🔥 老运营吵出的 3 个共识"),
    ("body", "① 锅不在工具，在工作流。大多数人只丢一句“给我 5 个变体”，AI 就吐平均答案——这是提示结构的问题，不是模型不行。"),
    ("body", "② 拆结构，每次只变一个维度。把帖子拆成 钩子 / 角度 / 结构，一次只换“钩子”或“受众”或“CTA”，别全一起换；全换又糊成一团。"),
    ("body", "③ 喂你自己的爆款当样本。把表现最好的帖子导出贴给 AI：“严格对齐这个结构、节奏、语气，只变角度”；或写成可复用的 SKILL.md，让输出像你，不是复读机。"),
    ("sep", ""),
    ("h", "💬 高赞评论（译）"),
    ("quote", "devfromPH：Glean / Moveworks 是企业知识库，不是为社媒变体设计的，你会一直在跟工具较劲。空白 prompt = 平均货。真有用的做法——把你最爆的帖当样本贴进去说“对齐结构节奏语气，只变角度”；锁死变量（句长 / 开头 / CTA 风格）；一次只出 1 个变体。"),
    ("quote", "toprakkaya：可复用的 SKILL.md + 你自己的爆款打底。把各平台最牛内容导出 Excel 喂给 AI，ChatGPT / Claude 都支持，也能接开源 SKILL.md 包，输出立刻不雷同。"),
    ("quote", "Sea-Belt-2937：多数工具把“变体”当“换词”，但你真要的是同一主题按每个平台重新想——LinkedIn 角度 ≠ X，IG 钩子 ≠ 推文。这是策略问题不是换词问题。（他自己做了 Coso.ai，但方法本身跟工具有关）"),
    ("quote", "UnoMaconheiro：雷同是因为只求“变体”没求“结构化变体系统”。固定模板 + 每次只变一维（钩子 / 受众 / CTA）。Higgsfield 文生视频能把赢的文案变视频广告，让你真看到哪个版本在跑。"),
    ("sep", ""),
    ("h", "🧠 我的理解"),
    ("note", "1) 落到小红书：他们的“角度”维度，咱们这就是“封面 + 标题公式”，是第一道生死关，比正文措辞重要得多。"),
    ("note", "2) 他们热衷 auto-post 工具，我相反：账号安全握自己手里，半自动 + 人审最稳。AI 写稿、人点发布，永远是第一步。"),
    ("note", "3) 满屏软广提醒一句：方法 > 工具。会拆结构、会喂样本，裸 ChatGPT 也能出好货；不会，换啥 SaaS 都复读机。"),
    ("note", "4) 一个可抄的极简框架：① 导出你 3 篇最爆的帖当样本 → ② 拆成 钩子 / 角度 / 结构 三段 → ③ 每次只换一维出 1 个变体 → ④ 人审定稿。"),
    ("sep", ""),
    ("src", "来源：r/SocialMediaManagers · “best ai tools for social media content creation” · 2026-07（译介 + 个人理解，非原帖立场）"),
]

# ---- 分词（CJK 单字 / 英文词 / 标点 / 空白）----
def tokenize(text):
    toks = []
    for m in re.finditer(r"[A-Za-z0-9]+|[\u4e00-\u9fff]|[^\s]|\\s+", text):
        toks.append(m.group())
    return toks

def wrap(draw, toks, font, max_w):
    lines, cur, cur_w = [], "", 0.0
    for tk in toks:
        w = draw.textlength(tk, font=font)
        if cur_w + w <= max_w:
            cur += tk
            cur_w += w
        else:
            if cur.strip():
                lines.append(cur.strip())
            cur, cur_w = tk, w
    if cur.strip():
        lines.append(cur.strip())
    return lines

# ---- 样式 ----
STYLE = {
    "title": (F_TITLE, 66, (20, 20, 20), 0, 18),
    "h":     (F_H,     52, (196, 58, 38), 0, 14),
    "body":  (F_BODY,  46, (45, 45, 45), 0, 12),
    "quote": (F_QUOTE, 42, (95, 95, 95), 26, 12),
    "note":  (F_NOTE,  42, (22, 92, 140), 26, 12),
    "src":   (F_SRC,   34, (150, 150, 150), 0, 8),
}

def style_for(kind):
    return STYLE.get(kind, (F_BODY, 46, (45, 45, 45), 0, 12))

# ---- 渲染 ----
img = Image.new("RGB", (W, 20000), (255, 255, 255))
draw = ImageDraw.Draw(img)
y = PAD
max_w = W - 2 * PAD

for kind, text in blocks:
    if kind == "sep":
        y += 8
        draw.line([(PAD, y), (W - PAD, y)], fill=(225, 225, 225), width=1)
        y += 20
        continue
    font, lh, color, indent, gap = style_for(kind)
    for line in wrap(draw, tokenize(text), font, max_w - indent):
        draw.text((PAD + indent, y), line, font=font, fill=color)
        y += lh
    y += gap

y += PAD
img = img.crop((0, 0, W, y))
img.save(OUT, "PNG")
print("SAVED:", OUT, "size:", img.size)
