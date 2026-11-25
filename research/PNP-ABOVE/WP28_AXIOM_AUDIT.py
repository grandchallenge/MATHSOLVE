#!/usr/bin/env python3
"""Check all 8 native Lean kernel public theorem axiom reports."""
from pathlib import Path
import json,re,subprocess,sys
if len(sys.argv)!=3: raise SystemExit("USAGE: WP28_AXIOM_AUDIT.py REPLAY_DIR PINNED_UPSTREAM")
work,upstream=map(Path,sys.argv[1:])
data=json.loads((work/'WP28_SOURCE_LOCK.json').read_text())
names=data['modules']['WP28UniformExponentObstruction.lean']['theorems']
assert len(names)==len(set(names))==8
script=work/'WP28_AxiomAudit.lean'
script.write_text('import PNPAbove.WP28UniformExponentObstruction\n'+
  ''.join('#print axioms PNPAbove.WP28.'+n+'\n' for n in names))
output=work/'WP28_AxiomAudit.log'
with output.open('w') as fh:
  proc=subprocess.run(['lake','env','lean','-R',str(work),str(script)],cwd=upstream,stdout=fh,stderr=subprocess.STDOUT)
if proc.returncode:
  raise SystemExit('WP28_AXIOM_AUDIT_LEAN_FAILED '+str(proc.returncode))
text=output.read_text()
allowed={'propext','Classical.choice','Quot.sound'}
for n in names:
  name="'PNPAbove.WP28."+n+"'"
  reports=re.findall(re.escape(name)+r' depends on axioms: \[([^\]]*)\]',text)
  if not reports and name+' does not depend on any axioms' in text:
    continue
  if len(reports)!=1:
    raise SystemExit('WP28_MISSING_AXIOM_REPORT '+n)
  got={x.strip() for x in reports[0].split(',') if x.strip()}
  if got-allowed:
    raise SystemExit('WP28_NONSTANDARD_AXIOM '+n+' '+str(got-allowed))
print('WP28_STANDARD_AXIOMS_ONLY_PASS modules=1 theorems=8')
