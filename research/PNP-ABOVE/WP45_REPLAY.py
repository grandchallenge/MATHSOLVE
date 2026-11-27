#!/usr/bin/env python3
"""Fresh isolated replay of the generic native budget-selector theorem."""
import hashlib,json,os,re,subprocess,sys
from pathlib import Path
from PNP_REPLAY_PREFLIGHT import direct_runner_guard,preflight,bounded_run

if not __debug__: raise SystemExit("WP45_OPTIMIZATION_FORBIDDEN")
if len(sys.argv)!=4: raise SystemExit("USAGE: WP45_REPLAY.py UPSTREAM GCL_HEAD FRESH_DIR")
u,g,d=(Path(s).resolve() for s in sys.argv[1:])
direct_runner_guard()
src=g/'research/PNP-ABOVE'
m=json.loads((src/'WP45_SOURCE_LOCK.json').read_text())
sha=lambda b:hashlib.sha256(b).hexdigest()
assert m['schema']=='PNP-ABOVE-WP45-SOURCE-LOCK/1'
assert m['original_upstream']=='vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970'
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=u,text=True).strip()==m['original_upstream'].split('@')[1]
subprocess.run(['git','merge-base','--is-ancestor',m['protected_parent'],'HEAD'],cwd=g,check=True)
lean,placement=preflight(u,d)
target=d/'PNPAbove'; target.mkdir(parents=True)
(d/'placement.json').write_text(json.dumps(placement,indent=2,sort_keys=True)+'\n')
env=os.environ.copy()
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
audit.write_text(''.join('import PNPAbove.'+Path(mod).stem+'\n' for mod in m['module_order'])+''.join('#print axioms PNPAbove.WP45.'+n+'\n' for n in names))
run([audit],'axioms.log')
report=(d/'axioms.log').read_text()
for n in names:
    marker="'PNPAbove.WP45."+n+"'"
    hits=re.findall(re.escape(marker)+r' depends on axioms: \[([^\]]*)\]',report)
    if not hits and marker+' does not depend on any axioms' in report: continue
    assert len(hits)==1 and set(x.strip() for x in hits[0].split(',') if x.strip())<={'propext','Classical.choice','Quot.sound'}
(d/'status.txt').write_text('WP45_GENERIC_WEIGHTED_BOUND_IFF_NATIVE_WITNESS_SOLVER__UNRESTRICTED_LOWER_OPEN\n')
print((d/'status.txt').read_text().strip())
