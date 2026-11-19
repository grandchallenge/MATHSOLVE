#!/usr/bin/env python3
"""Fail closed on nonstandard axioms in the nine exact-source WP18 modules."""
from pathlib import Path
import re
import subprocess
import sys
if len(sys.argv) != 3:
    raise SystemExit("USAGE: WP18_AXIOM_AUDIT.py REPLAY_DIR UPSTREAM_DIR")
work, upstream = (Path(x).resolve() for x in sys.argv[1:])
mods = ("WP18", "WP18Sampler", "WP18Query", "WP18Final", "WP18Runs",
        "WP18Native", "WP18Bound", "WP18Value", "WP18NoGap")
names = []
for mod in mods:
    src = (work / "PNPAbove" / (mod + ".lean")).read_text()
    names.extend((mod, name) for name in re.findall(
        r"^theorem\s+([A-Za-z][A-Za-z0-9_]*)", src, re.M))
if len(names) != 36 or len(set(n for _, n in names)) != 36:
    raise SystemExit("BAD_WP18_THEOREM_INVENTORY " + repr(names))
audit = work / "WP18_AxiomAudit.lean"
audit.write_text(
    "import PNPAbove.WP18Value\nimport PNPAbove.WP18NoGap\n" +
    "".join(f"#print axioms PNPAbove.WP18.{name}\n" for _, name in names))
with (work / "WP18_AxiomAudit.log").open("w") as out:
    proc = subprocess.run(["lake", "env", "lean", "-R", str(work), str(audit)],
                          cwd=upstream, stdout=out, stderr=subprocess.STDOUT)
if proc.returncode:
    raise SystemExit("WP18_AXIOM_LEAN_FAILURE " + str(proc.returncode))
output = (work / "WP18_AxiomAudit.log").read_text()
allowed = {"propext", "Classical.choice", "Quot.sound"}
for mod, name in names:
    target = f"'PNPAbove.WP18.{name}'"
    hits = re.findall(re.escape(target) + r" depends on axioms: \[([^\]]*)\]",
                      output, re.S)
    if not hits and target + " does not depend on any axioms" in output:
        continue
    if len(hits) != 1:
        raise SystemExit("MISSING_OR_MULTIPLE_AXIOM_REPORT " + name)
    axioms = {x.strip() for x in hits[0].split(",") if x.strip()}
    if not axioms <= allowed:
        raise SystemExit("WP18_NONSTANDARD_AXIOMS " + name +
                         " " + repr(sorted(axioms-allowed)))
print(f"WP18_STANDARD_AXIOMS_ONLY_PASS modules={len(mods)} theorems={len(names)}")
