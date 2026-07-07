#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply ziliaoku-gate (4-state verdict) to all raw files and emit:
  - data/gate/{date}.jsonl   (per-item verdict, per skill contract)
  - print nutrition stats
Rules encode the manual screening of 2026-07-07 batch. This is a REUSABLE
screening pass: future batches can re-run after editing the override maps.
"""
import os, re, glob, json, datetime
from collections import Counter

RAW = "data/raw/2026-07-07"
GATE_DIR = "data/gate"
os.makedirs(GATE_DIR, exist_ok=True)

# ----- manual overrides from 2026-07-07 screening -----
# X handles that are finance/trading (off our 6 AI tracks) -> discard
FINANCE_HANDLES = {"外汇交易员", "川沐", "华尔街观察", "Summer 在交易", "Summer_trading"}
# Reddit posts to discard: soft-ad / off-topic / low-effort question
REDDIT_DISCARD = {
    "31_reddit_AiAutomations.md":  "软广伪装干货：正文结尾导向 kadirx.io 外链，score 仅 25，价值承诺最终导向站外引流",
    "35_reddit_deadbydaylight.md": "离题：游戏公司 BHVR 用生成式 AI 的行业新闻，不在 AI工具/创作/自媒体/副业 六赛道",
    "42_reddit_SoraAi.md":         "产品/展望文：Cannon Studio 支持 Sora 2，score 51 偏低，无一手实测结构",
    "49_reddit_ContentCreators.md":"低质提问帖：'你依赖什么AI工具' 无正文结构，score 40",
}
# Reddit borderline -> hack_only (news/question, value in comments)
REDDIT_HACK = {
    "40_reddit_generativeAI.md":   "低质提问帖，但评论区可能有优质 AI video 推荐，from_comments 可单收",
}
# X borderline tech-news -> hack_only
X_HACK = {
    "21_sopilot_x.md": "博通/苹果芯片合作，科技产业新闻有时效性，蹭法=产业动向解读",
    "17_sopilot_x.md": "駿HaYaO 同款芯片新闻，hack_only",
}
# YouTube failed/artifact -> discard
YT_DISCARD = {
    "06_yt_techwithtim_claudecode_transcript.md": "字幕抓取失败（opencli transcript 返回空），无正文",
    "05_yt_search_results.md":                     "采集发现产物（搜索结果列表），非单篇内容，不入库",
}

def verdict_for(name, d):
    plat = d.get("platform", "")
    # YouTube discards
    if name in YT_DISCARD:
        return "discard", YT_DISCARD[name], None, False
    # Reddit
    if plat == "Reddit":
        if name in REDDIT_DISCARD:
            return "discard", REDDIT_DISCARD[name], None, False
        if name in REDDIT_HACK:
            return "hack_only", REDDIT_HACK[name], "评论区一手经验", True
        # default Reddit rich post -> collect (拿不准判collect)
        rc = d.get("reusable_core_hint")
        return "collect", "Reddit 一手经验帖，爆因可迁移（技能/工作流/收入结构），符合 collect 四条", rc, False
    # X/SoPilot
    if plat == "X/Twitter":
        author = d.get("author", "")
        if any(h in author for h in FINANCE_HANDLES):
            return "discard", f"离题：{author} 为炒股/财经号，不在 AI 六赛道", None, False
        if name in X_HACK:
            return "hack_only", X_HACK[name], "产业动向解读角度", False
        return "collect", "AI 向热帖（模型/工具/编码 Agent 解读），爆因可迁移", None, False
    # exa / fc / 公众号 / 网页
    if plat in ("公众号", "网页", "网页/公众号") or name.startswith(("01_","02_","03_","08_")):
        return "collect", "真实文章/教程，可拆解行文结构", None, False
    return "collect", "默认收录（拿不准判collect）", None, False

rows = []
for f in sorted(glob.glob(os.path.join(RAW, "*.md"))):
    name = os.path.basename(f)
    if name == "_summary.json":
        continue
    txt = open(f, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    d = {}
    if m:
        for line in m.group(1).splitlines():
            mm = re.match(r'^(\w+):\s*"?([^"]*)"?\s*$', line)
            if mm:
                d[mm.group(1)] = mm.group(2)
    v, reason, rc, fc = verdict_for(name, d)
    rows.append({
        "file": f"{RAW}/{name}",
        "verdict": v,
        "reason": reason,
        "reusable_core": rc or "",
        "from_comments": fc,
    })

# write jsonl
out = os.path.join(GATE_DIR, "2026-07-07.jsonl")
with open(out, "w", encoding="utf-8") as fh:
    for r in rows:
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")

# stats
c = Counter(r["verdict"] for r in rows)
print(f"GATE JSONL -> {out}  ({len(rows)} items)")
print("VERDICTS:", dict(c))
print(f"collect率 = {c['collect']/len(rows)*100:.0f}%  | discard率 = {c['discard']/len(rows)*100:.0f}%")
# per platform collect rate
plat = {}
for f in glob.glob(os.path.join(RAW, "*.md")):
    name = os.path.basename(f)
    if name == "_summary.json": continue
    txt = open(f, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    p = "?"
    if m:
        for line in m.group(1).splitlines():
            mm = re.match(r'^platform:\s*"?([^"]*)"?', line)
            if mm: p = mm.group(1)
    plat.setdefault(p, {"c":0,"t":0})
    plat[p]["t"] += 1
vmap = {r["file"].split("/")[-1]: r["verdict"] for r in rows}
for f in glob.glob(os.path.join(RAW, "*.md")):
    name = os.path.basename(f)
    if name == "_summary.json": continue
    txt = open(f, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    p = "?"
    if m:
        for line in m.group(1).splitlines():
            mm = re.match(r'^platform:\s*"?([^"]*)"?', line)
            if mm: p = mm.group(1)
    if vmap.get(name) == "collect":
        plat[p]["c"] += 1
print("\nPER-PLATFORM collect/total:")
for p, s in sorted(plat.items(), key=lambda x:-x[1]["t"]):
    print(f"  {p:<12} {s['c']}/{s['t']}  ({s['c']/s['t']*100:.0f}%)")
