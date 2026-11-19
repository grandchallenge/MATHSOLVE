#!/usr/bin/env python3
"""Check all nine original WP18 source bytes against protected-candidate manifest."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
if len(sys.argv) != 4:
    raise SystemExit("USAGE: WP18_SOURCE_GUARD.py MANIFEST SOURCE_DIR OUTPUT_DIR")
manifest=Path(sys.argv[1]);src=Path(sys.argv[2]);out=Path(sys.argv[3])
m=json.loads(manifest.read_text())
assert m["schema"]=="PNP-ABOVE-WP18-SOURCE-LOCK/1"
assert m["protected_source_parent"]=="7c999a2f31f6580e8f8e7459818dd04a9bd9d8e2"
expected={"WP18.lean","WP18Sampler.lean","WP18Query.lean","WP18Final.lean",
          "WP18Runs.lean","WP18Native.lean","WP18Bound.lean",
          "WP18Value.lean","WP18NoGap.lean"}
assert set(m["modules"])==expected
for name,record in m["modules"].items():
    rel=record["path"]
    assert rel.startswith("research/PNP-ABOVE/WP18_")
    path=src/Path(rel).name
    assert path.is_file()
    data=path.read_bytes()
    git_blob=subprocess.check_output(["git","hash-object","--",str(path)],
                                     text=True).strip()
    assert git_blob==record["git_blob"],(name,"GIT_BLOB_DRIFT",git_blob)
    assert hashlib.sha256(data).hexdigest()==record["sha256"],(name,"SHA256_DRIFT")
    (out/name).write_bytes(data)
print("WP18_NEW_SOURCE_LOCK_PASS modules=9")
