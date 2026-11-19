#!/usr/bin/env python3
"""Audit every public WP19 theorem against exact pinned Lean kernel declarations."""
from pathlib import Path
import re
import subprocess
import sys
if len(sys.argv)!=3:
    raise SystemExit("USAGE: WP19_AXIOM_AUDIT.py REPLAY_DIR UPSTREAM_DIR")
work,upstream=map(Path,sys.argv[1:])
modules=("WP19Support","WP19Law","WP19Choice","WP19Scalar",
         "WP19Envelope","WP19Global","WP19Strategies","WP19Native")
names=[]
for mod in modules:
    s=(work/"PNPAbove"/(mod+".lean")).read_text()
    names.extend((mod,n) for n in re.findall(
        r"^theorem\s+([A-Za-z][A-Za-z0-9_]*)",s,re.M))
assert len(names)==36 and len({name for _,name in names})==36,names
audit=work/"WP19_AxiomAudit.lean"
audit.write_text("import PNPAbove.WP19Native\n"+
                 "".join(f"#print axioms PNPAbove.WP19.{n}\n" for _,n in names))
with (work/"WP19_AxiomAudit.log").open("w") as out:
    p=subprocess.run(["lake","env","lean","-R",str(work),str(audit)],
                     cwd=upstream,stdout=out,stderr=subprocess.STDOUT,check=False)
if p.returncode:
    raise SystemExit(f"WP19_AXIOM_LEAN_FAILURE exit={p.returncode}")
output=(work/"WP19_AxiomAudit.log").read_text()
allowed={"propext","Classical.choice","Quot.sound"}
for mod,n in names:
    target=f"'PNPAbove.WP19.{n}'"
    hits=re.findall(re.escape(target)+r" depends on axioms: \[([^\]]*)\]",
                    output,re.S)
    if not hits and target+" does not depend on any axioms" in output:
        continue
    if len(hits)!=1:
        raise SystemExit(f"WP19_MISSING_AXIOM_REPORT {n} hits={len(hits)}")
    actual={x.strip() for x in hits[0].split(",") if x.strip()}
    if not actual<=allowed:
        raise SystemExit("WP19_NONSTANDARD_AXIOMS "+n+" "+repr(sorted(actual-allowed)))
print(f"WP19_STANDARD_AXIOMS_ONLY_PASS modules={len(modules)} theorems={len(names)}")
