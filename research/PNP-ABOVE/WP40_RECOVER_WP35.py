#!/usr/bin/env python3
"""Recover WP35 from a completed source-matched WP34 replay.

This is a new incremental recovery, not a replacement for the historical
WP35_REPLAY_STEP.sh or a claim that it passed. Never edit the old receipt.
"""
import hashlib,json,os,shutil,subprocess,sys
from pathlib import Path
from PNP_REPLAY_PREFLIGHT import direct_runner_guard, preflight, bounded_run

if not __debug__: raise SystemExit("WP40_RECOVERY_OPTIMIZATION_FORBIDDEN")
if len(sys.argv)!=5: raise SystemExit("USAGE: WP40_RECOVER_WP35.py UPSTREAM HISTORICAL_WP35_CHECKOUT COMPLETED_WP34_DIR FRESH_DIR")
u,g,p,d=(Path(x).resolve() for x in sys.argv[1:])
direct_runner_guard()
src=g/'research/PNP-ABOVE'
sha=lambda b:hashlib.sha256(b).hexdigest()
def git(*args,cwd=g):
    return subprocess.check_output(['git',*args],cwd=cwd)
assert git('rev-parse','HEAD').decode().strip()=='29697b84bcf40d3e487c19aa1c779064560a0dd8'
assert git('rev-parse','HEAD',cwd=u).decode().strip()=='5926bdff5db621f44682a101007ef2fe3ae8d970'
assert (p/'status.txt').read_text().strip()=='WP34_CANONICAL_SCOPE_AND_NATIVE_BUDGET_CLOSED__VALID_PROMISE_POLYTIME_EQUIVALENT_TO_FORMULA_SAT__LOWER_BOUND_OPEN'
assert not d.exists()
lean,placement=preflight(u,d)
locks=(p/'lock.txt').read_text().splitlines()
prior=[x.split('=',1)[1] for x in locks if x.startswith('WP34_CANDIDATE=')]
assert len(prior)==1 and len(prior[0])==40
git('merge-base','--is-ancestor',git('rev-parse','HEAD').decode().strip(),prior[0])
# Every historical Lean source must be byte-identical at the replayed later
# candidate, and every staged predecessor source must be historical.
allowed={}
for f in sorted(src.glob('*.lean')):
    if f.name.startswith('WP35'): continue
    b=f.read_bytes()
    assert b==git('show',prior[0]+':'+str(f.relative_to(g))),f
    allowed.setdefault(sha(b),[]).append(str(f.relative_to(g)))
files=sorted((p/'PNPAbove').glob('*.lean'))
assert len(files)==len(list((p/'PNPAbove').glob('*.olean')))==94
assert (p/'WP34_AxiomAudit.log').stat().st_size>0
target=d/'PNPAbove'; target.mkdir(parents=True)
(d/'placement.json').write_text(json.dumps(placement,indent=2,sort_keys=True)+'\n')
receipts=[]
for f in files:
    b=f.read_bytes(); h=sha(b); obj=f.with_suffix('.olean')
    assert h in allowed and obj.is_file() and not obj.is_symlink(),f
    shutil.copy2(f,target/f.name); shutil.copy2(obj,target/obj.name)
    receipts.append({'module':f.name,'source_sha256':h,'olean_sha256':sha(obj.read_bytes()),'protected_paths':allowed[h]})
(d/'recovery_receipt.json').write_text(json.dumps({'kind':'incremental_source_matched_WP34_to_WP35','wp34_candidate':prior[0],'wp34_receipt_sha256':sha((p/'lock.txt').read_bytes()),'wp34_axiom_log_sha256':sha((p/'WP34_AxiomAudit.log').read_bytes()),'wp35_protected_head':git('rev-parse','HEAD').decode().strip(),'predecessors':receipts},indent=2)+'\n')
shutil.copy2(src/'WP35_SOURCE_LOCK.json',d/'WP35_SOURCE_LOCK.json')
subprocess.run([sys.executable,str(src/'WP35_SOURCE_GUARD.py'),str(d/'WP35_SOURCE_LOCK.json'),str(src),str(target)],check=True)
env=os.environ.copy()
env['LEAN_PATH']=str(d)+':'+subprocess.check_output(['lake','env','printenv','LEAN_PATH'],cwd=u,text=True).strip()
env['LEAN_NUM_THREADS']='1'
f=target/'WP35Dense.lean'
bounded_run([str(lean),'-R',str(d),'-o',str(f.with_suffix('.olean')),str(f)],cwd=u,env=env,log=d/'WP35Dense.log',receipt=d/'execution.jsonl',seconds=180)
subprocess.run([sys.executable,str(src/'WP35_AXIOM_AUDIT.py'),str(d),str(u)],env=env,check=True,timeout=180)
assert len(list(target.glob('*.olean')))==95
(d/'status.txt').write_text('WP35_DENSE_SUPPORT_AND_SHORT_WITNESS_CLOSED__NATIVE_CLASSICAL_TRANSFER_CLOSED__LOWER_BOUND_OPEN\n')
print('WP35_INCREMENTAL_SOURCE_MATCHED_RECOVERY_PASS')
