#!/usr/bin/env python3
import json, os, re, sys, urllib.request, urllib.error
from pathlib import Path

BASE = "https://app.autolab.ai"
token = os.environ.get("AUTOLAB_TOKEN")
if not token:
    raise SystemExit("AUTOLAB_TOKEN missing")

tool_root = Path.home() / ".local" / "share" / "uv" / "tools" / "autolab"
print("AUTOLAB_TOOL_ROOT", tool_root)
hits = []
if tool_root.exists():
    for p in tool_root.rglob("*.py"):
        try:
            text = p.read_text(errors="replace")
        except Exception:
            continue
        if ("leaderboard" in text.lower() and "hill" in text.lower()) or ("hills submit" in text.lower()):
            for m in re.finditer(r"(?i)(leaderboard|hills submit|submit.*report|report.*submit)", text):
                line = text.count("\n", 0, m.start()) + 1
                lines = text.splitlines()
                lo, hi = max(0, line-8), min(len(lines), line+12)
                excerpt = "\n".join(f"{i+1}: {lines[i]}" for i in range(lo, hi))
                hits.append((str(p.relative_to(tool_root)), line, excerpt))
                if len(hits) >= 40:
                    break
        if len(hits) >= 40:
            break

print("=== CLI SOURCE HITS ===")
for path, line, excerpt in hits:
    print(f"--- {path}:{line} ---")
    print(excerpt)


print("=== INSTALLED AUTOLAB ROUTE INVENTORY ===")
route_hits = []
if tool_root.exists():
    for p in tool_root.rglob("*.py"):
        try:
            src = p.read_text(errors="replace")
        except Exception:
            continue
        if "/api/v1/" not in src:
            continue
        for lineno, line in enumerate(src.splitlines(), 1):
            if "/api/v1/" in line:
                safe = line.replace(token, "***")
                route_hits.append((str(p.relative_to(tool_root)), lineno, safe.strip()))
for path, line, txt in route_hits:
    print(f"{path}:{line}: {txt}")

def get(path):
    req = urllib.request.Request(BASE + path, headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "User-Agent": "GCL-OPENMATH-read-only-route-probe/1"
    }, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            body = r.read().decode("utf-8", errors="replace")
            return r.status, r.headers.get("content-type"), body
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("content-type"), e.read().decode("utf-8", errors="replace")
    except Exception as e:
        return -1, None, repr(e)

paths = [
    "/api/v1/hills/alejandrozu/kobon-triangles",
    "/api/v1/hills/alejandrozu/kobon-triangles/leaderboard",
    "/api/v1/hills/alejandrozu/kobon-triangles/versions/7d3f1d91dcb8be8d0eef20be763557bd6d876707/leaderboard",
    "/api/v1/hills/alejandrozu/kobon-triangles/submissions",
    "/api/v1/projects/a-hamdi/hamdi-kobon-18-93",
    "/api/v1/projects/a-hamdi/hamdi-kobon-18-93/jobs",
    "/api/v1/projects/ashleychenyj/kobon-triangles-attempt-7",
    "/api/v1/projects/ashleychenyj/kobon-triangles-attempt-7/jobs",
    "/api/v1/projects/jimsteeg/gcl-2026-h1-fixed-e606799ad6c1",
    "/api/v1/projects/jimsteeg/gcl-2026-h1-fixed-e606799ad6c1/jobs",
]
print("=== READ-ONLY API PROBES ===")
for path in paths:
    status, ctype, body = get(path)
    print("PATH", path, "STATUS", status, "CTYPE", ctype)
    # Never print bearer/token-like strings if an error reflects request metadata.
    body = body.replace(token, "***")
    print(body[:12000])
