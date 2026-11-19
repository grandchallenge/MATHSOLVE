#!/usr/bin/env python3
"""Fail closed on source bytes and original source identity for WP21."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

if len(sys.argv) != 4:
    raise SystemExit("USAGE: WP21_SOURCE_GUARD.py MANIFEST SOURCE_DIR OUT_DIR")
manifest, src, out = map(Path, sys.argv[1:])
m = json.loads(manifest.read_text())
assert m["schema"] == "PNP-ABOVE-WP21-SOURCE-LOCK/1"
assert m["original_upstream"] == "vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970"
assert m["source_protected_parent"] == "ab30e727a6bf6762432d4b95546908f8c4d3711a"
ordered = ["Masked", "Prog", "Safety", "Total", "Length", "Verifier",
           "Checks", "Runtime", "Time", "Bounded"]
assert set(m["modules"]) == {f"WP21{x}.lean" for x in ordered}
out.mkdir(parents=True, exist_ok=True)
seen = set()
total = 0
for short in ordered:
    module = f"WP21{short}.lean"
    rec = m["modules"][module]
    assert rec["path"] == f"research/PNP-ABOVE/WP21_{short}.lean"
    path = src / f"WP21_{short}.lean"
    data = path.read_bytes()
    assert not re.search(rb"(?m)^\s*(?:sorry|axiom)\b|\bnative_decide\b", data), module
    assert hashlib.sha256(data).hexdigest() == rec["sha256"], module
    assert subprocess.check_output(["git", "hash-object", "--", str(path)], text=True).strip() == rec["git_blob"], module
    names = [x.decode() for x in re.findall(rb"^theorem\s+([A-Za-z][A-Za-z0-9_]*)", data, re.M)]
    assert names == rec["theorems"], module
    assert not seen.intersection(names), ("DUPLICATE_THEOREM", module)
    seen.update(names)
    total += len(names)
    (out / module).write_bytes(data)
assert total == m["theorem_count"] and total >= 20, total
print(f"WP21_SOURCE_LOCK_PASS modules={len(ordered)} theorems={total}")
