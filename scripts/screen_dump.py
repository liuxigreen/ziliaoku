#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dump frontmatter of all raw .md into a compact table for gate screening.
Helps validate 营养: per-source counts, score distribution, off-topic noise.
"""
import os, re, glob, sys

RAW = "data/raw/2026-07-07"
out = []
for f in sorted(glob.glob(os.path.join(RAW, "*.md"))):
    if os.path.basename(f) == "_summary.json":
        continue
    name = os.path.basename(f)
    txt = open(f, encoding="utf-8").read()
    fm = ""
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    if m:
        fm = m.group(1)
    d = {}
    for line in fm.splitlines():
        mm = re.match(r'^(\w+):\s*"?([^"]*)"?\s*$', line)
        if mm:
            d[mm.group(1)] = mm.group(2)
    body = txt[m.end():] if m else txt
    d["_file"] = name
    d["_words"] = len(body.split())
    out.append(d)

# print compact table
cols = ["_file", "platform", "subreddit", "score", "comments", "published",
        "query_track", "_words", "title"]
print(f"{'FILE':<26} {'PLAT':<9} {'SCORE':>6} {'CMT':>5} {'WORDS':>5} TRACK / TITLE")
print("-" * 120)
for d in out:
    plat = d.get("platform", "?")[:8]
    sub = (d.get("subreddit") or d.get("source_platform") or "?")[:14]
    score = d.get("score", "?")
    cmt = d.get("comments", "?")
    words = d.get("_words", 0)
    track = (d.get("query_track") or "?")[:18]
    title = (d.get("title") or "?")[:40]
    print(f"{d['_file']:<26} {plat:<9} {str(score):>6} {str(cmt):>5} {words:>5} {track} | {title}")

print("-" * 120)
print(f"TOTAL = {len(out)}")
# per-platform counts
from collections import Counter
pc = Counter(d.get("platform", "?") for d in out)
print("BY PLATFORM:", dict(pc))
