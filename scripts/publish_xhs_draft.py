#!/usr/bin/env python3
"""
把小红书图文笔记存进草稿箱（图文模式，支持封面+内文卡片图）。
用法：python publish_xhs_draft.py <md_path> <cover_path> <topics> [card_paths]
"""
import os, sys, subprocess, pathlib

OPENCLI_JS = "C:/Program Files/nodejs/node_global/node_modules/@jackwener/opencli/dist/src/main.js"
NODE = "C:/Users/liuxi/.workbuddy/binaries/node/versions/22.22.2/node.exe"
PROFILE = "kzbaq3xs"


def parse_md(md_path):
    text = pathlib.Path(md_path).read_text(encoding="utf-8")
    lines = text.splitlines()
    title = ""
    body_lines = []
    tags = []
    in_body = False
    for line in lines:
        if line.startswith("# ") and not title:
            title = line.lstrip("# ").strip()
            in_body = True
            continue
        if in_body:
            if line.strip() == "---" or line.strip().startswith("【配图说明】"):
                break
            # collect topic tags from hashtag lines
            if line.strip().startswith("#") and not line.strip().startswith("# "):
                # hashtags line
                tags = [t.strip() for t in line.strip().replace("#", "").split() if t.strip()]
                continue
            body_lines.append(line)
    body = "\n".join(body_lines).strip()
    return title, body, tags


def main():
    if len(sys.argv) < 4:
        print("Usage: python publish_xhs_draft.py <md_path> <cover_path> <topics> [card_paths]")
        print("  topics: comma-separated, no #")
        print("  card_paths: comma-separated image files, optional")
        sys.exit(1)
    md_path = sys.argv[1]
    cover_path = sys.argv[2]
    topics = sys.argv[3]
    card_paths = sys.argv[4] if len(sys.argv) > 4 else ""

    title, body, auto_tags = parse_md(md_path)
    if topics.lower() == "none":
        topics = None
    elif not topics:
        topics = ",".join(auto_tags) if auto_tags else None

    images = cover_path
    if card_paths:
        images = ",".join([cover_path] + [p for p in card_paths.split(",") if p.strip()])

    cmd = [
        NODE, OPENCLI_JS, "--profile", PROFILE, "xiaohongshu", "publish", body,
        "--title", title,
        "--images", images,
        "--draft"
    ]
    if topics:
        cmd += ["--topics", topics]
    env = os.environ.copy()
    env["OPENCLI_BROWSER_COMMAND_TIMEOUT"] = "300"
    print("[CMD]", " ".join([f'"{c}"' if " " in c else c for c in cmd[:7]]), "...")
    p = subprocess.run(cmd, env=env, shell=False, capture_output=True, text=True)
    print("STDOUT:", p.stdout[-2000:] if p.stdout else "(empty)")
    print("STDERR:", p.stderr[-1000:] if p.stderr else "(empty)")
    print("EXIT:", p.returncode)
    return p.returncode


if __name__ == "__main__":
    sys.exit(main())
