#!/usr/bin/env python3
"""Fail closed if any exact original WP19 Lean source blob differs."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
if len(sys.argv)!=4:
    raise SystemExit("USAGE: WP19_SOURCE_GUARD.py MANIFEST SOURCE_DIR WORK_DIR")
manifest,src,out=map(Path,sys.argv[1:])
m=json.loads(manifest.read_text())
assert m["schema"]=="PNP-ABOVE-WP19-SOURCE-LOCK/1"
assert m["source_protected_parent"]=="21f3e9edb946ae2ab4f4a312663f1e5559214a6b"
assert m["source_admitted_wp18_sha"]=="760d30d74672309ae58f015b0f511c062f431e08"
expected={"WP19Support.lean","WP19Law.lean","WP19Choice.lean",
          "WP19Scalar.lean","WP19Envelope.lean","WP19Global.lean",
          "WP19Strategies.lean","WP19Native.lean"}
assert set(m["modules"])==expected
for mod,record in m["modules"].items():
    rel=record["path"]
    assert rel.startswith("research/PNP-ABOVE/WP19_")
    path=src/Path(rel).name
    assert path.is_file()
    b=path.read_bytes()
    git_blob=subprocess.check_output(["git","hash-object","--",str(path)],
                                     text=True).strip()
    assert git_blob==record["git_blob"],(mod,"GIT_BLOB_DRIFT",git_blob)
    assert hashlib.sha256(b).hexdigest()==record["sha256"],(mod,"SHA256_DRIFT")
    (out/mod).write_bytes(b)
print("WP19_SOURCE_LOCK_PASS modules=8")
