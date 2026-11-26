#!/usr/bin/env python3
"""Fresh WP41 check against source-matched retained WP40 replay outputs."""
import hashlib,json,os,re,shutil,subprocess,sys
from pathlib import Path
from PNP_REPLAY_PREFLIGHT import direct_runner_guard, preflight, bounded_run

if not __debug__: raise SystemExit("WP41_OPTIMIZATION_FORBIDDEN")
if len(sys.argv)!=5: raise SystemExit("USAGE: WP41_REPLAY.py UPSTREAM GCL_HEAD WP40_REPLAY_DIR FRESH_DIR")
u,g,b,d=(Path(s).resolve() for s in sys.argv[1:])
direct_runner_guard()
src=g/'research/PNP-ABOVE'
m=json.loads((src/'WP41_SOURCE_LOCK.json').read_text())
sha=lambda data: hashlib.sha256(data).hexdigest()
assert m['schema']=='PNP-ABOVE-WP41-SOURCE-LOCK/1'
assert m['original_upstream']=='vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970'
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=u,text=True).strip()==m['original_upstream'].split('@')[1]
subprocess.run(['git','merge-base','--is-ancestor',m['protected_parent'],'HEAD'],cwd=g,check=True)
assert not d.exists()
assert (b/'status.txt').read_text().strip()=='WP40_SEMANTIC_CAPACITY_BARRIER_PROVED__UNRESTRICTED_LOWER_OPEN'
lean,placement=preflight(u,d)
protected={}
for f in src.glob('*.lean'):
    protected.setdefault(sha(f.read_bytes()),[]).append(str(f.relative_to(g)))
target=d/'PNPAbove'; target.mkdir(parents=True)
(d/'placement.json').write_text(json.dumps(placement,indent=2,sort_keys=True)+'\n')
receipts=[]
for prior,count in ((b,101),):
    files=sorted((prior/'PNPAbove').glob('*.lean'))
    assert len(files)==count
    for f in files:
        h=sha(f.read_bytes()); obj=f.with_suffix('.olean')
        assert h in protected and obj.is_file() and not obj.is_symlink(),f
        assert not (target/f.name).exists(),f
        shutil.copy2(f,target/f.name); shutil.copy2(obj,target/obj.name)
        receipts.append({'module':f.name,'source_sha256':h,'olean_sha256':sha(obj.read_bytes()),'protected_paths':protected[h]})
(d/'predecessor_receipts.json').write_text(json.dumps(receipts,indent=2,sort_keys=True)+'\n')
env=os.environ.copy()
assert (u/'lean-toolchain').read_text().strip()=='leanprover/lean4:v4.35.0-rc3'
paths=[u/'.lake/build/lib/lean']+sorted((u/'.lake/packages').glob('*/.lake/build/lib/lean'))
assert all(p.is_dir() for p in paths)
env['LEAN_PATH']=':'.join(map(str,[d]+paths)); env['LEAN_NUM_THREADS']='1'
def run(args,log):
    bounded_run([str(lean),'-R',str(d),*map(str,args)],cwd=u,env=env,log=d/log,receipt=d/'execution.jsonl')
names=[]
for mod in m['module_order']:
    rec=m['modules'][mod]; f=g/rec['path']; data=f.read_bytes()
    assert f.is_file() and not f.is_symlink()
    assert sha(data)==rec['sha256']
    assert subprocess.check_output(['git','hash-object',str(f)],cwd=g,text=True).strip()==rec['git_blob']
    assert not re.search(rb'\b(sorry|admit|axiom|native_decide)\b',data)
    assert re.findall(r'^theorem\s+(\w+)',data.decode(),re.M)==rec['theorems']
    names+=rec['theorems']
    staged=target/mod; staged.write_bytes(data)
    run(['-o',staged.with_suffix('.olean'),staged],mod+'.log')
assert len(names)==len(set(names))==m['theorem_count']
audit=d/'Axioms.lean'
audit.write_text(''.join('import PNPAbove.'+Path(mod).stem+'\n' for mod in m['module_order'])+''.join('#print axioms PNPAbove.WP41.'+n+'\n' for n in names))
run([audit],'axioms.log')
report=(d/'axioms.log').read_text()
for n in names:
    marker="'PNPAbove.WP41."+n+"'"
    hits=re.findall(re.escape(marker)+r' depends on axioms: \[([^\]]*)\]',report)
    if not hits and marker+' does not depend on any axioms' in report: continue
    assert len(hits)==1 and set(x.strip() for x in hits[0].split(',') if x.strip())<={'propext','Classical.choice','Quot.sound'}
status='WP41_WEIGHTED_CAPACITY_TRANSPORT_AND_FINITE_BUDGET_SEARCH_PROVED__UNRESTRICTED_LOWER_OPEN'
(d/'status.txt').write_text(status+'\n')
print(status)
