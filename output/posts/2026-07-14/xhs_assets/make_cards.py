from PIL import Image, ImageDraw, ImageFont
import os, sys

def make_card(title, items, accent, bg, out_path, size=(900, 1200)):
    w, h = size
    img = Image.new("RGB", size, bg)
    draw = ImageDraw.Draw(img)

    def font(size):
        for p in ["C:/Windows/Fonts/msyhbd.ttc", "C:/Windows/Fonts/msyh.ttc"]:
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
        return ImageFont.load_default()

    # Title bar
    bar_h = int(h * 0.16)
    draw.rounded_rectangle([0, 0, w, bar_h], radius=0, fill=accent)

    # Title
    title_font = font(int(w * 0.07))
    # wrap if too long
    tw = draw.textlength(title, font=title_font)
    if tw > w * 0.9:
        title_font = font(int(w * 0.06))
    tw = draw.textlength(title, font=title_font)
    tx = (w - tw) / 2
    ty = (bar_h - title_font.size) / 2 + int(h * 0.01)
    draw.text((tx, ty), title, font=title_font, fill="white")

    # Items
    item_font = font(int(w * 0.05))
    sub_font = font(int(w * 0.04))
    y = bar_h + int(h * 0.08)
    x = int(w * 0.08)
    max_w = w - 2 * x

    for icon, text in items:
        # icon circle
        r = int(w * 0.045)
        cy = y + r
        cx = x + r
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=accent)
        # draw number centered in circle
        num_font = font(int(w * 0.06))
        nw = draw.textlength(icon, font=num_font)
        nh = num_font.size
        draw.text((cx - nw / 2, cy - nh / 1.7), icon, font=num_font, fill="white")

        # text
        tx = x + int(w * 0.12)
        # wrap text if too long
        words = text
        line = ""
        lines = []
        for ch in words:
            if draw.textlength(line + ch, font=sub_font) > max_w - int(w * 0.12):
                lines.append(line)
                line = ch
            else:
                line += ch
        if line:
            lines.append(line)
        for i, ln in enumerate(lines):
            draw.text((tx, y + i * sub_font.size * 1.3), ln, font=sub_font, fill="#1F2937")
        y += max(int(w * 0.16), len(lines) * sub_font.size * 1.3 + int(w * 0.05))

    # footer brand
    brand_font = font(int(w * 0.03))
    brand = "打工人北北"
    bw = draw.textlength(brand, font=brand_font)
    draw.text(((w - bw) / 2, h - int(h * 0.06)), brand, font=brand_font, fill="#6B7280")

    img.save(out_path, quality=95)
    print(f"saved {out_path}")

out_dir = os.path.dirname(__file__)
make_card(
    "AI读代码翻车的3个信号",
    [("1", "不分析真实代码，改听黑客的"),
     ("2", "明明没分析完，却谎称已完成"),
     ("3", "从被污染的状态重新开始推理")],
    "#C0202E", "#FEF2F2",
    os.path.join(out_dir, "card1_signals.png")
)
make_card(
    "打工人绕坑3招",
    [("1", "不信任代码别直接丢给AI"),
     ("2", "让AI读敏感代码前先扫注释和字符串"),
     ("3", "关键逻辑别全信AI，自己留一手验证")],
    "#059669", "#F0FDF4",
    os.path.join(out_dir, "card2_tips.png")
)
