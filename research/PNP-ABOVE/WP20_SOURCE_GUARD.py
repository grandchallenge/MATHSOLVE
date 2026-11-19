#!/usr/bin/env python3
"""Verify all 17 exact original-source WP20 Lean byte identities; fail closed."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
if len(sys.argv) != 4:
    raise SystemExit("USAGE: WP20_SOURCE_GUARD.py MANIFEST SOURCE_DIR WORK_DIR")
manifest,src,out=map(Path,sys.argv[1:])
m=json.loads(manifest.read_text())
assert m["schema"]=="PNP-ABOVE-WP20-SOURCE-LOCK/1"
assert m["original_upstream"]=="vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970"
assert m["source_protected_parent"]=="0780909e5a31c8fb7ff882a25b1ccad5bf31dd51"
expected={"WP20Cycle","WP20Law","WP20Parity","WP20Quantum","WP20Decomp",
          "WP20Expectation","WP20Aggregation","WP20QuantumGlobal","WP20BellGap",
          "WP20SourceProg","WP20SourceSemantics","WP20CLSem","WP20SourceQueries",
          "WP20BitEquiv","WP20Native","WP20Bounded","WP20ClassicalExact"}
assert set(m["modules"])=={n+".lean" for n in expected}
out.mkdir(parents=True,exist_ok=True)
names=[]
paths=set()
for mod,record in m["modules"].items():
    rel=record["path"]
    assert rel.startswith("research/PNP-ABOVE/WP20_")
    assert rel.endswith(".lean") and "/../" not in rel and "\\" not in rel
    assert rel not in paths,("REPEATED_SOURCE",rel)
    paths.add(rel)
    p=src/Path(rel).name
    assert p.is_file(),("MISSING_FILE",rel)
    b=p.read_bytes()
    assert b"\nsorry" not in b and b"\naxiom" not in b and b"native_decide" not in b
    gh=subprocess.check_output(["git","hash-object","--",str(p)],text=True).strip()
    assert gh==record["git_blob"],(mod,"GIT_BLOB_DRIFT",gh)
    assert hashlib.sha256(b).hexdigest()==record["sha256"],(mod,"SHA256_DRIFT")
    n=[v.decode() for v in re.findall(rb"^theorem\s+([A-Za-z][A-Za-z0-9_]*)",b,re.M)]
    assert record["theorems"]==n,(mod,"THEOREM_MANIFEST_DRIFT")
    names.extend(n)
    (out/mod).write_bytes(b)
assert len(names)==m["theorem_count"] and len(names)==len(set(names))
assert len(names)>=100
print(f"WP20_SOURCE_LOCK_PASS modules={len(expected)} theorems={len(names)}")
