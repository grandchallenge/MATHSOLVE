#!/usr/bin/env python3
"""All WP33 original Lean kernel axioms, exact theorem inventory."""
from pathlib import Path
import json,re,subprocess,sys

if len(sys.argv)!=3:
    raise SystemExit("USAGE: WP33_AXIOM_AUDIT.py REPLAY_DIR PINNED_UPSTREAM")
work,upstream=map(Path,sys.argv[1:])
manifest=json.loads((work/'WP33_SOURCE_LOCK.json').read_text())
names=manifest['modules']['WP33Budget.lean']['theorems']
assert len(names)==len(set(names))==manifest['theorem_count']==7
audit=work/'WP33_AxiomAudit.lean'
audit.write_text('import PNPAbove.WP33Budget\n'+
 ''.join(f'#print axioms PNPAbove.WP33.{n}\n' for n in names))
log=work/'WP33_AxiomAudit.log'
with log.open('w') as output:
    p=subprocess.run(['lake','env','lean','-R',str(work),str(audit)],
       cwd=upstream,stdout=output,stderr=subprocess.STDOUT)
if p.returncode:
    raise SystemExit('WP33_AXIOM_AUDIT_COMPILATION_FAILED '+str(p.returncode))
text=log.read_text()
allowed={'propext','Classical.choice','Quot.sound'}
for name in names:
    marker=f"'PNPAbove.WP33.{name}'"
    matches=re.findall(re.escape(marker)+r' depends on axioms: \[([^\]]*)\]',text)
    if not matches and marker+' does not depend on any axioms' in text:
        continue
    if len(matches)!=1:
        raise SystemExit('WP33_AXIOM_REPORT_MISSING '+name)
    actual={x.strip() for x in matches[0].split(',') if x.strip()}
    if not actual<=allowed:
        raise SystemExit('WP33_NONSTANDARD_AXIOMS '+name+' '+repr(actual-allowed))
print(f"WP33_STANDARD_AXIOMS_ONLY_PASS modules=1 theorems={len(names)}")
