#!/usr/bin/env python3
"""Audit all 30 WP24 kernel theorem declarations in exact original Lean."""
from pathlib import Path
import json
import re
import subprocess
import sys

if len(sys.argv) != 3:
    raise SystemExit("USAGE: WP24_AXIOM_AUDIT.py REPLAY_DIR PINNED_UPSTREAM")
work, upstream = map(Path, sys.argv[1:])
m = json.loads((work / "WP24_SOURCE_LOCK.json").read_text())
names = [n for rec in m["modules"].values() for n in rec["theorems"]]
assert len(names) == len(set(names)) == m["theorem_count"] == 30
audit = work / "WP24_AxiomAudit.lean"
audit.write_text("import PNPAbove.WP24Examples\n" +
                 "".join(f"#print axioms PNPAbove.WP24.{n}\n" for n in names))
log = work / "WP24_AxiomAudit.log"
with log.open("w") as out:
    proc = subprocess.run(["lake", "env", "lean", "-R", str(work), str(audit)],
                          cwd=upstream, stdout=out, stderr=subprocess.STDOUT)
if proc.returncode:
    raise SystemExit(f"WP24_AXIOM_AUDIT_COMPILATION_FAILED exit={proc.returncode}")
output = log.read_text()
allowed = {"propext", "Classical.choice", "Quot.sound"}
for name in names:
    key = f"'PNPAbove.WP24.{name}'"
    matches = re.findall(re.escape(key)+r" depends on axioms: \[([^\]]*)\]", output, re.S)
    if not matches and key+" does not depend on any axioms" in output:
        continue
    if len(matches) != 1:
        raise SystemExit("WP24_MISSING_AXIOM_REPORT " + name)
    actual = {x.strip() for x in matches[0].split(",") if x.strip()}
    if not actual <= allowed:
        raise SystemExit("WP24_NONSTANDARD_AXIOMS " + name + repr(sorted(actual-allowed)))
print(f"WP24_STANDARD_AXIOMS_ONLY_PASS modules={len(m['modules'])} theorems={len(names)}")
