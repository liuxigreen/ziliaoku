#!/usr/bin/env python3
"""
firecrawl_client.py — 用付费 Key 直接调 Firecrawl REST API
读取 ~/.workbuddy/mcp.json 里的 firecrawl-mcp.headers.Authorization 作为 Key，
不在脚本里硬编码密钥。

用法:
  python firecrawl_client.py search "你的查询" [limit]
  python firecrawl_client.py scrape "https://..." [outfile.md]

依赖: 仅标准库 (urllib, json)
"""
import os
import sys
import json
import urllib.request
from pathlib import Path

API_BASE = "https://api.firecrawl.dev/v1"
MCP_JSON = Path.home() / ".workbuddy" / "mcp.json"


def load_key() -> str:
    try:
        cfg = json.loads(MCP_JSON.read_text(encoding="utf-8"))
        hdr = cfg["mcpServers"]["firecrawl-mcp"]["headers"]
        auth = hdr.get("Authorization", "")
        if auth.startswith("Bearer "):
            return auth[len("Bearer "):].strip()
        return auth.strip()
    except Exception as e:
        print(f"[key] 读取 mcp.json 失败: {e}", file=sys.stderr)
        return os.environ.get("FIRECRAWL_API_KEY", "")


def _post(path: str, payload: dict, key: str, timeout: int = 60):
    url = f"{API_BASE}{path}"
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url, data=data, method="POST",
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def search(query: str, limit: int = 5, fresh_days: int = 30):
    payload = {
        "query": query,
        "limit": limit,
        "lang": "en",
        "country": "us",
    }
    if fresh_days:
        payload["tbs"] = f"qdr:m"  # 近一月，保证时效性
    return _post("/search", payload, load_key(), timeout=60)


def scrape(url: str, outfile: str = None, timeout: int = 60):
    payload = {
        "url": url,
        "formats": ["markdown"],
        "onlyMainContent": True,
        "timeout": 30000,
        "waitFor": 0,
    }
    data = _post("/scrape", payload, load_key(), timeout=timeout)
    md = ""
    if data.get("success") and "data" in data:
        md = data["data"].get("markdown", "")
        meta = data["data"].get("metadata", {})
        print(f"[scrape] 状态={data.get('status')} 长度={len(md)} 标题={meta.get('title','')[:60]}")
    else:
        print(f"[scrape] 失败: {json.dumps(data, ensure_ascii=False)[:300]}")
        return None
    if outfile:
        Path(outfile).parent.mkdir(parents=True, exist_ok=True)
        Path(outfile).write_text(md, encoding="utf-8")
        print(f"[scrape] 已存 {outfile}")
    return md


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "search":
        q = sys.argv[2]
        lim = int(sys.argv[3]) if len(sys.argv) > 3 else 5
        res = search(q, lim)
        if res.get("success"):
            for i, r in enumerate(res.get("data", []), 1):
                print(f"{i}. {r.get('title','')[:70]}")
                print(f"   {r.get('url','')}")
                print(f"   摘要: {r.get('description','')[:120]}")
        else:
            print("搜索失败:", json.dumps(res, ensure_ascii=False)[:400])
    elif cmd == "scrape":
        u = sys.argv[2]
        out = sys.argv[3] if len(sys.argv) > 3 else None
        scrape(u, out)
    else:
        print(__doc__)
