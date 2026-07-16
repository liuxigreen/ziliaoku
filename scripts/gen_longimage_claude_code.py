#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""渲染 Claude Code 译介长图：宽1080 竖版，CJK 自动换行 + 分节样式。"""
import os
import re
from PIL import Image, ImageDraw, ImageFont

OUT = r"D:\WorkBuddyProjects\ziliaoku\output\posts\2026-07-09\claude_code_32_tricks_longimage.png"
W = 1080
PAD = 64

# ---- 字体 ----
REG_CANDIDATES = [
    r"C:\Windows\Fonts\msyh.ttc",
    r"C:\Windows\Fonts\simhei.ttf",
    r"C:\Windows\Fonts\simsun.ttc",
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
blocks = [
    ("title", "译介｜Nate Herk 的 32 个 Claude Code 技巧，我扒出最该抄的"),
    ("sep", ""),
    ("h", "📌 原视频在讲啥"),
    ("body", "\"32 Tricks to Level Up Claude Code in 16 Mins\" —— 作者从小白到量产 workflow / 网站 / App / AI agent 的 32 个实操技巧，分 beginner / intermediate / advanced 三层，最好的留在最后。"),
    ("sep", ""),
    ("h", "🔰 Beginner 最该先学的"),
    ("body", "① /init：开老项目先扫一遍，生成 CLAUDE.md 当项目 cheat sheet，不用每轮重讲背景。"),
    ("body", "② /statusline：终端底部挂小仪表盘，看剩余上下文和花费，防「上下文腐烂」。"),
    ("body", "③ 保持上下文小：别把整个代码库塞进对话，只给当前任务要的。"),
    ("body", "④ /context：查 token 都耗在哪（系统提示 / 文件 / MCP），对症下药。"),
    ("body", "⑤ /compact 到 60% 就压，可指定保留某些决策；换任务用 /clear 重开。"),
    ("sep", ""),
    ("h", "🚀 Intermediate 提速"),
    ("body", "⑥ 永远先 plan mode：只读不写，先出方案再执行，返工骤减。"),
    ("body", "⑦ 把 AI 当 junior dev：给它问题而非命令，让它自己想做法。"),
    ("body", "⑧ 让它主动提问：plan mode 里令其连续问到 95% 确信，少来回改。"),
    ("body", "⑨ 自检写进 todo：做完一项就截图 / 开 DevTools 自验，质量焊进计划。"),
    ("body", "⑩ 部署 sub-agents 并行：复杂任务甩给隔离子 agent，主线程保持干净。"),
    ("sep", ""),
    ("h", "🧠 我的不同意见"),
    ("note", "sub-agents 并行很酷，但新手先别碰——先把「对齐 + 自检」练成本能。"),
    ("note", "稳的玩法永远是：AI 跑流程，人盯关键节点。半自动比全自动靠谱。"),
    ("note", "方法 > 工具。会拆结构、会喂样本，裸 Claude Code 也能出好活；不会，换啥都复读机。"),
    ("sep", ""),
    ("src", "来源：Nate Herk \"32 Tricks to Level Up Claude Code in 16 Mins\" (YouTube, 2026) · 译介 + 个人理解，非原视频立场"),
]

# ---- 分词 ----
def tokenize(text):
    toks = []
    for m in re.finditer(r"[A-Za-z0-9]+|[\u4e00-\u9fff]|[^\s]|\s+", text):
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
