#!/usr/bin/env python3
"""All WP31 original Lean kernel axioms, exact theorem inventory."""
from pathlib import Path
import json,re,subprocess,sys

if len(sys.argv)!=3:
    raise SystemExit("USAGE: WP31_AXIOM_AUDIT.py REPLAY_DIR PINNED_UPSTREAM")
work,upstream=map(Path,sys.argv[1:])
manifest=json.loads((work/'WP31_SOURCE_LOCK.json').read_text())
names=manifest['modules']['WP31Counting.lean']['theorems']
assert len(names)==len(set(names))==manifest['theorem_count']==10
audit=work/'WP31_AxiomAudit.lean'
audit.write_text('import PNPAbove.WP31Counting\n'+
 ''.join(f'#print axioms PNPAbove.WP31.{n}\n' for n in names))
log=work/'WP31_AxiomAudit.log'
with log.open('w') as output:
    p=subprocess.run(['lake','env','lean','-R',str(work),str(audit)],
       cwd=upstream,stdout=output,stderr=subprocess.STDOUT)
if p.returncode:
    raise SystemExit('WP31_AXIOM_AUDIT_COMPILATION_FAILED '+str(p.returncode))
text=log.read_text()
allowed={'propext','Classical.choice','Quot.sound'}
for name in names:
    marker=f"'PNPAbove.WP31.{name}'"
    matches=re.findall(re.escape(marker)+r' depends on axioms: \[([^\]]*)\]',text)
    if not matches and marker+' does not depend on any axioms' in text:
        continue
    if len(matches)!=1:
        raise SystemExit('WP31_AXIOM_REPORT_MISSING '+name)
    actual={x.strip() for x in matches[0].split(',') if x.strip()}
    if not actual<=allowed:
        raise SystemExit('WP31_NONSTANDARD_AXIOMS '+name+' '+repr(actual-allowed))
print(f"WP31_STANDARD_AXIOMS_ONLY_PASS modules=1 theorems={len(names)}")
