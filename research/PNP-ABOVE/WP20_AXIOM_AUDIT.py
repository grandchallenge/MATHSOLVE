#!/usr/bin/env python3
"""Audit all new WP20 public theorem declarations against original pinned Lean."""
from pathlib import Path
import json
import re
import subprocess
import sys
if len(sys.argv)!=3:
    raise SystemExit("USAGE: WP20_AXIOM_AUDIT.py REPLAY_DIR UPSTREAM_DIR")
work,upstream=map(Path,sys.argv[1:])
src=work/"PNPAbove"
m=json.loads((work/"WP20_SOURCE_LOCK.json").read_text())
names=[]
for mod,rec in m["modules"].items():
    discovered=[v.decode() for v in re.findall(
        rb"^theorem\s+([A-Za-z][A-Za-z0-9_]*)",(src/mod).read_bytes(),re.M)]
    if discovered!=rec["theorems"]:
        raise SystemExit("WP20_AX_SRC_DRIFT "+mod)
    names.extend(discovered)
if len(names)!=m["theorem_count"] or len(names)!=len(set(names)) or len(names)<100:
    raise SystemExit(f"WP20_AXIOM_NAME_CARD_FAIL {len(names)}")
audit=work/"WP20_AxiomAudit.lean"
audit.write_text(
    "import PNPAbove.WP20Bounded\nimport PNPAbove.WP20ClassicalExact\n"+
    "".join(f"#print axioms PNPAbove.WP20.{name}\n" for name in names))
log=work/"WP20_AxiomAudit.log"
with log.open("w") as out:
    p=subprocess.run(["lake","env","lean","-R",str(work),str(audit)],
       cwd=upstream,stdout=out,stderr=subprocess.STDOUT,check=False)
if p.returncode:
    raise SystemExit(f"WP20_AXIOM_LEAN_FAILURE exit={p.returncode}")
output=log.read_text()
allowed={"propext","Classical.choice","Quot.sound"}
for n in names:
    target=f"'PNPAbove.WP20.{n}'"
    hits=re.findall(re.escape(target)+r" depends on axioms: \[([^\]]*)\]",output,re.S)
    if not hits and target+" does not depend on any axioms" in output:continue
    if len(hits)!=1:raise SystemExit(f"WP20_MISSING_AXIOM_REPORT {n} hits={len(hits)}")
    actual={x.strip() for x in hits[0].split(",") if x.strip()}
    if not actual<=allowed:
        raise SystemExit("WP20_NONSTANDARD_AXIOMS "+n+" "+repr(sorted(actual-allowed)))
print(f"WP20_STANDARD_AXIOMS_ONLY_PASS modules={len(m['modules'])} theorems={len(names)}")
