#!/usr/bin/env python3
"""Full original Lean kernel audit for 19 WP27 public theorem declarations."""
from pathlib import Path
import json,subprocess,re,sys
if len(sys.argv)!=3:
  raise SystemExit("USAGE: WP27_AXIOM_AUDIT.py EXACT_REPLAY_DIR ORIGINAL_UPSTREAM")
work,upstream=map(Path,sys.argv[1:])
m=json.loads((work/'WP27_SOURCE_LOCK.json').read_text())
claims=[n for rec in m['modules'].values() for n in rec['theorems']]
assert len(claims)==len(set(claims))==m['theorem_count']==19
source=work/'WP27_AxiomAudit.lean'
source.write_text('import PNPAbove.WP27RobustVerifier\n'+
  ''.join(f'#print axioms PNPAbove.WP27.{n}\n' for n in claims))
log=work/'WP27_AxiomAudit.log'
with log.open('w') as stream:
  p=subprocess.run(['lake','env','lean','-R',str(work),str(source)],
                   cwd=upstream,stdout=stream,stderr=subprocess.STDOUT)
if p.returncode:
  raise SystemExit(f'WP27_ORIGINAL_LEAN_KERNEL_AUDIT_FAILED exit={p.returncode}')
text=log.read_text()
allowed={'propext','Classical.choice','Quot.sound'}
for n in claims:
  marker=f"'PNPAbove.WP27.{n}'"
  found=re.findall(re.escape(marker)+r' depends on axioms: \[([^\]]*)\]',text)
  if not found and marker+' does not depend on any axioms' in text:
    continue
  if len(found)!=1:
    raise SystemExit('WP27_MISSING_AXIOM_REPORT '+n)
  new={v.strip() for v in found[0].split(',') if v.strip()}-allowed
  if new:
    raise SystemExit('WP27_NONSTANDARD_AXIOMS '+n+' '+repr(new))
print(f'WP27_STANDARD_AXIOMS_ONLY_PASS modules=3 theorems={len(claims)}')
