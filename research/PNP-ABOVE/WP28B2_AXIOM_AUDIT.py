#!/usr/bin/env python3
"""Audit every WP28B2 original Lean kernel theorem declaration."""
from pathlib import Path
import json,re,subprocess,sys
if len(sys.argv)!=3:
    raise SystemExit('USAGE: WP28B2_AXIOM_AUDIT.py REPLAY_DIR PINNED_UPSTREAM')
work,original=map(Path,sys.argv[1:])
m=json.loads((work/'WP28B2_SOURCE_LOCK.json').read_text())
names=[name for rec in m['modules'].values() for name in rec['theorems']]
assert len(names)==len(set(names))==m['theorem_count']==22
script=work/'WP28B2_AxiomAudit.lean'
script.write_text('import PNPAbove.WP28B2Value\n'+
    ''.join(f'#print axioms PNPAbove.WP28B2.{n}\n' for n in names))
log=work/'WP28B2_AxiomAudit.log'
with log.open('w') as f:
    p=subprocess.run(['lake','env','lean','-R',str(work),str(script)],
                     cwd=original,stdout=f,stderr=subprocess.STDOUT)
if p.returncode:
    raise SystemExit('WP28B2_AXIOM_AUDIT_KERNEL_FAILURE '+str(p.returncode))
text=log.read_text()
allowed={'propext','Classical.choice','Quot.sound'}
for n in names:
    key=f"'PNPAbove.WP28B2.{n}'"
    reports=re.findall(re.escape(key)+r' depends on axioms: \[([^\]]*)\]',text)
    if not reports and key+' does not depend on any axioms' in text:
        continue
    if len(reports)!=1:
        raise SystemExit('WP28B2_MISSING_AXIOM_REPORT '+n)
    got={x.strip() for x in reports[0].split(',') if x.strip()}
    if got-allowed:
        raise SystemExit('WP28B2_NONSTANDARD_AXIOMS '+n+' '+str(got-allowed))
print('WP28B2_STANDARD_AXIOMS_ONLY_PASS modules=4 theorems=22')
