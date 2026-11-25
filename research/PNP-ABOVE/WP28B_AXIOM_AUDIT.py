#!/usr/bin/env python3
"""Kernel axiom scope for 17 original-source WP28B1 theorem declarations."""
from pathlib import Path
import json,re,subprocess,sys
if len(sys.argv)!=3:
    raise SystemExit('USAGE: WP28B_AXIOM_AUDIT.py REPLAY_DIR ORIGINAL_UPSTREAM')
work,source=map(Path,sys.argv[1:])
m=json.loads((work/'WP28B_SOURCE_LOCK.json').read_text())
names=m['modules']['WP28BIndex.lean']['theorems']
assert len(names)==len(set(names))==m['theorem_count']==17
script=work/'WP28B_AxiomAudit.lean'
script.write_text('import PNPAbove.WP28BIndex\n'+
    ''.join('#print axioms PNPAbove.WP28B.'+n+'\n' for n in names))
output=work/'WP28B_AxiomAudit.log'
with output.open('w') as fh:
    proc=subprocess.run(['lake','env','lean','-R',str(work),str(script)],
                        cwd=source,stdout=fh,stderr=subprocess.STDOUT)
if proc.returncode:
    raise SystemExit('WP28B_AXIOM_AUDIT_FAILED '+str(proc.returncode))
log=output.read_text()
allowed={'propext','Classical.choice','Quot.sound'}
for n in names:
    key="'PNPAbove.WP28B."+n+"'"
    axioms=re.findall(re.escape(key)+r' depends on axioms: \[([^\]]*)\]',log)
    if not axioms and key+' does not depend on any axioms' in log:
        continue
    if len(axioms)!=1:
        raise SystemExit('WP28B_MISSING_KERNEL_REPORT '+n)
    got={x.strip() for x in axioms[0].split(',') if x.strip()}
    if got-allowed:
        raise SystemExit('WP28B_NONSTANDARD_AXIOMS '+n+' '+str(got-allowed))
print('WP28B_STANDARD_AXIOMS_ONLY_PASS modules=1 theorems=17')
