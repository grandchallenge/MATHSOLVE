#!/usr/bin/env python3
"""Fail closed on nonstandard WP12 theorem axioms using exact compiled Lean modules."""
from pathlib import Path
import re
import subprocess
import sys

if len(sys.argv) != 3:
    raise SystemExit("usage: WP12_AXIOM_AUDIT.py WORK_DIR UPSTREAM_DIR")
work = Path(sys.argv[1]).resolve()
upstream = Path(sys.argv[2]).resolve()
source = (work / "PNPAbove/WP12.lean").read_text()
names = re.findall(r"^theorem\s+([A-Za-z][A-Za-z0-9_]*)", source, re.M)
if len(names) != 15 or len(set(names)) != 18:
    raise SystemExit(f"UNEXPECTED_THEOREM_INVENTORY: {len(names)} {names}")
audit = work / "AxiomAudit.lean"
audit.write_text("import PNPAbove.WP12\n" + "".join(
    f"#print axioms PNPAbove.WP12.{name}\n" for name in names
))
with (work / "AxiomAudit.log").open("w") as log:
    p = subprocess.run(["lake", "env", "lean", "-R", str(work), str(audit)],
                       cwd=upstream, stdout=log, stderr=subprocess.STDOUT,
                       check=False)
if p.returncode:
    raise SystemExit(f"LEAN_AXIOM_AUDIT_FAIL: exit={p.returncode}")
output = (work / "AxiomAudit.log").read_text()
allowed = {"propext", "Classical.choice", "Quot.sound"}
for name in names:
    prefix = re.escape(f"'PNPAbove.WP12.{name}'")
    hits = re.findall(prefix + r" depends on axioms: \[([^\]]*)\]", output, re.S)
    if len(hits) == 0 and f"'PNPAbove.WP12.{name}' does not depend on any axioms" in output:
        continue
    if len(hits) != 1:
        raise SystemExit("AXIOM_REPORT_MISSING_OR_DUPLICATE " + name)
    found = {a.strip() for a in hits[0].split(",") if a.strip()}
    if not found <= allowed:
        raise SystemExit(f"UNEXPECTED_AXIOMS {name}: {sorted(found - allowed)}")
print(f"WP12_STANDARD_AXIOMS_ONLY_PASS count={len(names)}")
