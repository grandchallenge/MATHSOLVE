#!/usr/bin/env python3
"""Audit original Lean kernel dependencies of every pinned WP28C theorem."""
from pathlib import Path
import json,re,subprocess,sys
if len(sys.argv)!=3:
    raise SystemExit("USAGE: WP28C_AXIOM_AUDIT.py REPLAY_DIR PINNED_UPSTREAM")
work,upstream=map(Path,sys.argv[1:])
m=json.loads((work/'WP28C_SOURCE_LOCK.json').read_text())
names=[n for rec in m['modules'].values() for n in rec['theorems']]
assert len(names)==len(set(names))==m['theorem_count']==16
audit=work/'WP28C_AxiomAudit.lean'
audit.write_text('import PNPAbove.WP28CCompression\n'+
  ''.join(f'#print axioms PNPAbove.WP28C.{n}\n' for n in names))
log=work/'WP28C_AxiomAudit.log'
with log.open('w') as output:
    p=subprocess.run(['lake','env','lean','-R',str(work),str(audit)],
       cwd=upstream,stdout=output,stderr=subprocess.STDOUT)
if p.returncode:
    raise SystemExit(f'WP28C_AXIOM_AUDIT_COMPILATION_FAILED rc={p.returncode}')
txt=log.read_text()
allowed={'propext','Classical.choice','Quot.sound'}
for n in names:
    marker=f"'PNPAbove.WP28C.{n}'"
    matches=re.findall(re.escape(marker)+r' depends on axioms: \[([^\]]*)\]',txt)
    if not matches and marker+' does not depend on any axioms' in txt:
        continue
    if len(matches)!=1:
        raise SystemExit('WP28C_MISSING_AXIOM_REPORT '+n)
    actual={x.strip() for x in matches[0].split(',') if x.strip()}
    if not actual<=allowed:
        raise SystemExit('WP28C_NONSTANDARD_AXIOM '+n+' '+repr(actual-allowed))
print(f'WP28C_STANDARD_AXIOMS_ONLY_PASS modules=3 theorems={len(names)}')
