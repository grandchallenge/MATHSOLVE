#!/usr/bin/env python3
"""Original Lean kernel axiom inventory of all 32 WP26 claims."""
from pathlib import Path
import json,subprocess,re,sys
if len(sys.argv)!=3:
  raise SystemExit("USAGE: WP26_AXIOM_AUDIT.py EXACT_REPLAY_ROOT PINNED_ORIGINAL")
work,upstream=map(Path,sys.argv[1:])
m=json.loads((work/'WP26_SOURCE_LOCK.json').read_text())
names=[x for rec in m['modules'].values() for x in rec['theorems']]
assert len(names)==len(set(names))==m['theorem_count']==32
src=work/'WP26_AxiomAudit.lean'
src.write_text('import PNPAbove.WP26UniformCompiler\n'+
  ''.join(f'#print axioms PNPAbove.WP26.{name}\n' for name in names))
log=work/'WP26_AxiomAudit.log'
with log.open('w') as stream:
  p=subprocess.run(['lake','env','lean','-R',str(work),str(src)],
                   cwd=upstream,stdout=stream,stderr=subprocess.STDOUT)
if p.returncode:
  raise SystemExit(f'WP26_AXIOM_AUDIT_KERNEL_FAILURE={p.returncode}')
text=log.read_text()
allowed={'propext','Classical.choice','Quot.sound'}
for n in names:
  mark=f"'PNPAbove.WP26.{n}'"
  found=re.findall(re.escape(mark)+r' depends on axioms: \[([^\]]*)\]',text)
  if not found and mark+' does not depend on any axioms' in text:
    continue
  if len(found)!=1:
    raise SystemExit('WP26_AXIOM_REPORT_MISSING '+n)
  extra={v.strip() for v in found[0].split(',') if v.strip()}-allowed
  if extra:
    raise SystemExit('WP26_NONSTANDARD_AXIOMS '+n+':'+repr(extra))
print(f'WP26_STANDARD_AXIOMS_ONLY_PASS modules=2 theorems={len(names)}')
