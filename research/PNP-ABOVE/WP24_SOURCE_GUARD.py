#!/usr/bin/env python3
"""Fail closed on all WP24 original source bytes, kernel declarations, and commit parent."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

if len(sys.argv) != 4:
    raise SystemExit("USAGE: WP24_SOURCE_GUARD.py MANIFEST SOURCE_DIR OUT_DIR")
manifest, src, out = map(Path, sys.argv[1:])
m = json.loads(manifest.read_text())
assert m["schema"] == "PNP-ABOVE-WP24-SOURCE-LOCK/1"
assert m["original_upstream"] == "vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970"
assert m["source_protected_parent"] == "442cef7f7b5c18afffa132ae5eba01087ba7cdea"
filenames = {"SATGame": "WP24_SATGame.lean", "CNF": "WP24_3CNF.lean",
             "Examples": "WP24_Examples.lean"}
assert set(m["modules"]) == {f"WP24{k}.lean" for k in filenames}
out.mkdir(parents=True, exist_ok=True)
seen = set()
total = 0
for short, filename in filenames.items():
    module = f"WP24{short}.lean"
    rec = m["modules"][module]
    assert rec["path"] == f"research/PNP-ABOVE/{filename}", module
    path = src / filename
    assert path.is_file() and not path.is_symlink(), module
    data = path.read_bytes()
    assert not re.search(rb"(?m)^\s*(?:sorry|axiom)\b|\bnative_decide\b", data), module
    assert hashlib.sha256(data).hexdigest() == rec["sha256"], module
    assert subprocess.check_output(["git", "hash-object", "--", str(path)],
                                   text=True).strip() == rec["git_blob"], module
    names = [name.decode() for name in
             re.findall(rb"^theorem\s+([A-Za-z][A-Za-z0-9_]*)", data, re.M)]
    assert names == rec["theorems"], module
    assert not seen.intersection(names), ("DUPLICATE_THEOREM", module)
    seen.update(names)
    total += len(names)
    (out / module).write_bytes(data)
assert total == m["theorem_count"] and total == 30, total
print(f"WP24_SOURCE_LOCK_PASS modules={len(filenames)} theorems={total}")
