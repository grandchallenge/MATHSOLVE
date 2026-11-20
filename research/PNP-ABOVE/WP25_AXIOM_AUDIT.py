#!/usr/bin/env python3
"""Check all original kernel WP25 source axioms; no synthetic confidence."""
from pathlib import Path
import json,re,subprocess,sys
if len(sys.argv)!=3:
    raise SystemExit("USAGE: WP25_AXIOM_AUDIT.py REPLAY_DIR PINNED_UPSTREAM")
work,original=map(Path,sys.argv[1:])
m=json.loads((work/'WP25_SOURCE_LOCK.json').read_text())
names=m['modules']['WP25SourceEvaluator.lean']['theorems']
assert len(set(names))==len(names)==m['theorem_count']==11
source=work/'WP25_AxiomAudit.lean'
source.write_text('import PNPAbove.WP25SourceEvaluator\n'+
  ''.join(f'#print axioms PNPAbove.WP25.{n}\n' for n in names))
out=work/'WP25_AxiomAudit.log'
with out.open('w') as f:
  p=subprocess.run(['lake','env','lean','-R',str(work),str(source)],
                   cwd=original,stdout=f,stderr=subprocess.STDOUT)
if p.returncode:
  raise SystemExit(f'WP25_AXIOM_AUDIT_COMPILATION_FAILED exit={p.returncode}')
log=out.read_text()
allowed={'propext','Classical.choice','Quot.sound'}
for n in names:
  mark=f"'PNPAbove.WP25.{n}'"
  match=re.findall(re.escape(mark)+r' depends on axioms: \[([^\]]*)\]',log)
  if not match and mark+' does not depend on any axioms' in log:
    continue
  if len(match)!=1:
    raise SystemExit('WP25_AXIOM_REPORT_MISSING '+n)
  axioms={x.strip() for x in match[0].split(',') if x.strip()}
  if not axioms<=allowed:
    raise SystemExit('WP25_FORBIDDEN_AXIOMS '+n+' '+repr(axioms-allowed))
print(f"WP25_STANDARD_AXIOMS_ONLY_PASS modules=1 theorems={len(names)}")
