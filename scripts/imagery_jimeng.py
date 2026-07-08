#!/usr/bin/env python3
"""
即梦(Jimeng) 文生图集成层 — 配图步骤(⑧)生产级出图骨架。

当前状态：用户尚未提供即梦 API Key，本脚本为"接 Key 即用"的集成层。
接入方式（二选一）：
  1. 环境变量：  export JIMENG_API_KEY="你的key"
  2. ~/.workbuddy/mcp.json 增加 "jimeng" 条目：{"api_key": "你的key"}

设计纪律（来自 ziliaoku-image SKILL.md）：
  - 输出中文生图提示词(Prompt-F) 由 ziliaoku-image 生成，本脚本只负责"把提示词发给即梦出图"。
  - 出图尺寸默认 3:4（小红书竖图），可参数覆盖。
  - 即梦待 Key 期间，配图由内置 ImageGen demo 兜底（见各成稿的 *_cover_prompt.md）。

注意：即梦底层为字节火山引擎视觉大模型，精确 endpoint / 模型名以官方文档为准，
下方 DEFAULT_* 为占位，接入时按官方最新文档核对。
"""
import os
import sys
import json
import urllib.request
import urllib.error
from pathlib import Path

# ── 配置（待 Key + 待官方 endpoint 核对）───────────────
DEFAULT_BASE_URL = "https://visual.volcengineapi.com/api/v1/jimeng/text2img"  # TODO: 以官方文档核对
DEFAULT_MODEL = "jimeng-2.0-pro"  # TODO: 以官方文档核对
DEFAULT_SIZE = "768:1024"  # 3:4 竖图


def load_key() -> str:
    """优先环境变量，其次 mcp.json 的 jimeng 条目"""
    key = os.environ.get("JIMENG_API_KEY", "").strip()
    if key:
        return key
    mcp = Path.home() / ".workbuddy" / "mcp.json"
    if mcp.exists():
        try:
            data = json.loads(mcp.read_text(encoding="utf-8"))
            jimeng = data.get("jimeng", {})
            k = jimeng.get("api_key", "") or jimeng.get("headers", {}).get("Authorization", "")
            if k and k.startswith("Bearer "):
                k = k[len("Bearer "):]
            return k.strip()
        except Exception:
            return ""
    return ""


def text2img(prompt: str, out_path: str, size: str = DEFAULT_SIZE,
             model: str = DEFAULT_MODEL, base_url: str = DEFAULT_BASE_URL,
             api_key: str = "") -> str:
    """
    调用即梦文生图，保存图片到 out_path，返回本地路径。
    未配 Key 时抛 RuntimeError，由调用方回退到 ImageGen demo。
    """
    api_key = api_key or load_key()
    if not api_key:
        raise RuntimeError("即梦 API Key 未配置（设 JIMENG_API_KEY 或 mcp.json jimeng.api_key）")

    payload = json.dumps({
        "model": model,
        "prompt": prompt,
        "size": size,
        # 其他参数按官方文档补充（seed / guidance_scale 等）
    }).encode("utf-8")

    req = urllib.request.Request(base_url, data=payload, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", f"Bearer {api_key}")

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            # 实际返回结构以官方为准；此处占位解析 image_url
            img_url = body.get("data", {}).get("image_url") or body.get("image_url")
            if not img_url:
                raise RuntimeError(f"即梦返回异常: {body}")
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"即梦 HTTP 错误 {e.code}: {e.read().decode('utf-8', 'replace')}")

    # 下载图片到本地
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    req2 = urllib.request.Request(img_url)
    with urllib.request.urlopen(req2, timeout=120) as r, out.open("wb") as f:
        f.write(r.read())
    return str(out)


def main():
    if len(sys.argv) < 3:
        print("用法: python imagery_jimeng.py <prompt文本> <输出图片路径> [size]")
        sys.exit(2)
    prompt = sys.argv[1]
    out_path = sys.argv[2]
    size = sys.argv[3] if len(sys.argv) > 3 else DEFAULT_SIZE
    try:
        saved = text2img(prompt, out_path, size=size)
        print(f"OK -> {saved}")
    except RuntimeError as e:
        print(f"FAIL: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
