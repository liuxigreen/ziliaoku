#!/bin/bash
cd /d/WorkBuddyProjects/ziliaoku
export XHS_PROFILE=kzbaq3xs
PY=/c/Users/liuxi/.workbuddy/binaries/python/versions/3.13.12/python.exe
P="D:/WorkBuddyProjects/ziliaoku/output/posts/2026-07-28/claude_skills_practice"
"$PY" scripts/publish_xhs_draft.py \
  "$P/claude_skills_xhs.md" \
  "$P/xhs_cover_claude_skills_3x4.png" \
  "ClaudeCode,AI编程,效率工具,程序员,打工人摸鱼" \
  "$P/xhs_card1_claude_skills_3x4.png,$P/xhs_card2_claude_skills_3x4.png,$P/xhs_card3_claude_skills_3x4.png,$P/xhs_illus01_claude_skills_3x4.jpg"
