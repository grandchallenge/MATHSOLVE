#!/usr/bin/env python3
"""Fail closed on source bytes and original source identity for WP23B."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

if len(sys.argv) != 4:
    raise SystemExit("USAGE: WP23B_SOURCE_GUARD.py MANIFEST SOURCE_DIR OUT_DIR")
manifest, src, out = map(Path, sys.argv[1:])
m = json.loads(manifest.read_text())
assert m["schema"] == "PNP-ABOVE-WP23B-SOURCE-LOCK/1"
assert m["original_upstream"] == "vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970"
assert m["source_protected_parent"] == "c6a3bb4c389baa093a4acbd644284b343e42d08c"
ordered = ['NativeCost', 'Mask', 'SuccinctBridge', 'Characterization', 'Concrete']
assert set(m["modules"]) == {f"WP23B{x}.lean" for x in ordered}
out.mkdir(parents=True, exist_ok=True)
seen = set()
total = 0
for short in ordered:
    module = f"WP23B{short}.lean"
    rec = m["modules"][module]
    assert rec["path"] == f"research/PNP-ABOVE/WP23B_{short}.lean"
    path = src / f"WP23B_{short}.lean"
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
assert total == m["theorem_count"] and total >= 8, total
print(f"WP23B_SOURCE_LOCK_PASS modules={len(ordered)} theorems={total}")
