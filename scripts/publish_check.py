# -*- coding: utf-8 -*-
"""
发布前合规自检（publish_check 模式）
扫绝对化/收益数字/硬引流/AI味，输出 data/gate/{date}_publish_check.jsonl
"""
import re, json
from pathlib import Path

ROOT = Path(r"D:\WorkBuddyProjects\ziliaoku")
POST = ROOT / "output/posts/2026-07-09/ecc_github_repo_publish_ready.md"
OUT = ROOT / "data/gate/2026-07-09_publish_check.jsonl"
DATE = "2026-07-09"

# 红线词
ABSOLUTE = ["最", "第一", "唯一", "全网", "必", "一定", "100%", "绝对", "史上", "顶级", "极致"]
# 收益数字：具体金额 / 月入X / 赚X元 / X天见效（引用他人案例且标注可豁免，此处简单扫）
MONEY = [r"月入\s*\d", r"赚\s*\d+\s*元", r"\d+\s*天见效", r"日入", r"年薪", r"\$\d+", r"\d+\s*元/?月?", r"\d+\s*万/?年?"]
HARD_PROMO = ["私信我", "加我微信", "主页有链接", "关注我", "加微信", "扫码", "回复666", "领取"]
AI_CLICHE = ["在当今时代", "随着AI发展", "赋能", "抓手", "闭环", "颗粒度", "底层逻辑"]
AI_OPENERS = ["在当今时代", "随着人工智能", "随着AI"]

def extract_front(body_text):
    # 从 md 抽 final_title / cta / tags / body
    fm = {}
    if body_text.startswith("---"):
        parts = body_text.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].splitlines():
                m = re.match(r'^(\w+):\s*"?([^"]*)"?\s*$', line.strip())
                if m:
                    fm[m.group(1)] = m.group(2)
            body = parts[2].strip()
        else:
            body = body_text
    else:
        body = body_text
    return fm, body

def check(title, body, cta, tags):
    issues = []
    blob = f"{title}\n{body}\n{cta}"
    # 1 绝对化
    for w in ABSOLUTE:
        if w in blob:
            # 标题里"最戳我"等主观不算硬绝对化，但"最"仍标（让用户判断）
            issues.append({"type": "绝对化", "hit": w, "suggest": "去绝对化，改『我试过的/目前见过/相对』"})
    # 2 收益数字（豁免 GitHub star 数：数字后紧跟 星/★ 属热度证据，非收益）
    blob_safe = re.sub(r'\d+\s*万?\s*[★星]', 'STAR', blob)
    for pat in MONEY:
        m = re.search(pat, blob_safe)
        if m:
            issues.append({"type": "收益数字", "hit": m.group(0), "suggest": "删；或标引用他人案例且非承诺"})
    # 3 硬引流
    for w in HARD_PROMO:
        if w in blob:
            issues.append({"type": "硬引流", "hit": w, "suggest": "改提问式 cta，不直给联系方式"})
    # 4 AI味
    for w in AI_CLICHE:
        if w in blob:
            issues.append({"type": "AI味", "hit": w, "suggest": "换大白话"})
    for w in AI_OPENERS:
        if body.strip().startswith(w):
            issues.append({"type": "AI味", "hit": w, "suggest": "砍套话，直接进钩子"})
    # 单句过长 >25字（跳过话题标签行）
    for sent in re.split(r'[。！？\n]', body):
        sent = sent.strip()
        if sent.startswith("#"):
            continue
        if len(sent) > 25:
            issues.append({"type": "AI味", "hit": f"长句({len(sent)}字)", "suggest": "拆成短句，≤25字"})
    # 禁用词连用
    if sum(1 for w in ["赋能","抓手","闭环","颗粒度","底层逻辑"] if w in blob) >= 2:
        issues.append({"type": "AI味", "hit": "禁用词连用≥2", "suggest": "重写，去黑话"})
    return issues

def main():
    text = POST.read_text(encoding="utf-8")
    fm, body = extract_front(text)
    title = fm.get("final_title", "")
    cta = fm.get("cta", "")
    tags = fm.get("tags", "")
    issues = check(title, body, cta, tags)
    passed = len(issues) == 0
    verdict = "修改后过" if issues else "通过"
    rec = {
        "file": "output/posts/2026-07-09/ecc_github_repo_publish_ready.md",
        "final_title": title,
        "pass": passed,
        "issues": issues,
        "verdict": verdict,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"=== publish_check ===")
    print(f"title: {title}")
    print(f"pass: {passed}")
    print(f"issues: {len(issues)}")
    for i in issues:
        print(f"  [{i['type']}] hit={i['hit']} -> {i['suggest']}")
    print(f"verdict: {verdict}")
    print(f"产出: {OUT.name}")

if __name__ == "__main__":
    main()
