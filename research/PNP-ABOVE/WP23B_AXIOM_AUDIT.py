#!/usr/bin/env python3
"""Audit all new WP23B public declarations through original pinned Lean kernel."""
from pathlib import Path
import json
import re
import subprocess
import sys
if len(sys.argv) != 3:
    raise SystemExit("USAGE: WP23B_AXIOM_AUDIT.py REPLAY_DIR UPSTREAM_DIR")
work, upstream = map(Path, sys.argv[1:])
m = json.loads((work / "WP23B_SOURCE_LOCK.json").read_text())
names = [n for rec in m["modules"].values() for n in rec["theorems"]]
assert len(names) == len(set(names)) == m["theorem_count"]
audit = work / "WP23B_AxiomAudit.lean"
audit.write_text("import PNPAbove.WP23BConcrete\n"
                 + "".join(f"#print axioms PNPAbove.WP23B.{n}\n" for n in names))
log = work / "WP23B_AxiomAudit.log"
with log.open("w") as out:
    proc = subprocess.run(["lake", "env", "lean", "-R", str(work), str(audit)],
                          cwd=upstream, stdout=out, stderr=subprocess.STDOUT)
if proc.returncode:
    raise SystemExit(f"WP23B_AX_LEAN_FAILURE exit={proc.returncode}")
output = log.read_text()
allowed = {"propext", "Classical.choice", "Quot.sound"}
for n in names:
    key = f"'PNPAbove.WP23B.{n}'"
    hits = re.findall(re.escape(key)+r" depends on axioms: \[([^\]]*)\]", output, re.S)
    if not hits and key+" does not depend on any axioms" in output:
        continue
    if len(hits) != 1:
        raise SystemExit("WP23B_MISSING_AXIOM_REPORT "+n)
    actual = {x.strip() for x in hits[0].split(",") if x.strip()}
    if not actual <= allowed:
        raise SystemExit("WP23B_NONSTANDARD_AXIOMS "+n+" "+repr(sorted(actual-allowed)))
print(f"WP23B_STANDARD_AXIOMS_ONLY_PASS modules={len(m['modules'])} theorems={len(names)}")
