#!/usr/bin/env python3
"""Fresh two-module original-model observation/copy-cost proof replay.
Does not use WP08-WP35 oleans: these generic results import only original Cost.PolyTime."""
import hashlib,json,os,re,subprocess,sys
from pathlib import Path
if not __debug__:
    raise SystemExit("WP36A_OPTIMIZATION_FORBIDDEN")
if len(sys.argv)!=4:
    raise SystemExit("USAGE: WP36A_REPLAY.py PINNED_UPSTREAM GCL_HEAD FRESH_DIR")
u,g,w=(Path(s).resolve() for s in sys.argv[1:])
src=g/'research/PNP-ABOVE'
m=json.loads((src/'WP36A_SOURCE_LOCK.json').read_text())
assert m['schema']=='PNP-ABOVE-WP36A-SOURCE-LOCK/1'
assert m['original_upstream']=='vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970'
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=u,text=True).strip()==m['original_upstream'].split('@')[1]
subprocess.run(['git','merge-base','--is-ancestor',m['source_protected_parent'],'HEAD'],cwd=g,check=True)
assert not w.exists()
d=w/'PNPAbove'; d.mkdir(parents=True)
env=os.environ.copy()
env['LEAN_PATH']=str(w)+':'+subprocess.check_output(['lake','env','printenv','LEAN_PATH'],cwd=u,text=True).strip()
env['LEAN_NUM_THREADS']='1'
names=[]
for mod in ('WP36Eval.lean','WP36Copy.lean'):
    rec=m['modules'][mod]
    f=g/rec['path']
    assert f.is_file() and not f.is_symlink()
    b=f.read_bytes()
    assert hashlib.sha256(b).hexdigest()==rec['sha256']
    assert subprocess.check_output(['git','hash-object',str(f)],cwd=g,text=True).strip()==rec['git_blob']
    assert not re.search(rb'\b(sorry|admit|axiom|native_decide)\b',b)
    assert re.findall(r'^theorem\s+([A-Za-z_][A-Za-z0-9_]*)',b.decode(),re.M)==rec['theorems']
    names+=rec['theorems']
    staged=d/mod; staged.write_bytes(b)
    with (w/(mod+'.log')).open('w') as log:
        subprocess.run(['lake','env','lean','-R',str(w),'-o',str(staged.with_suffix('.olean')),str(staged)],cwd=u,env=env,stdout=log,stderr=subprocess.STDOUT,check=True)
assert len(names)==len(set(names))==m['theorem_count']==22
a=w/'Axioms.lean'
a.write_text('import PNPAbove.WP36Copy\n'+''.join('#print axioms PNPAbove.WP36.'+n+'\n' for n in names))
with (w/'axioms.log').open('w') as log:
    subprocess.run(['lake','env','lean','-R',str(w),str(a)],cwd=u,env=env,stdout=log,stderr=subprocess.STDOUT,check=True)
report=(w/'axioms.log').read_text()
for n in names:
    marker="'PNPAbove.WP36."+n+"'"
    hits=re.findall(re.escape(marker)+r' depends on axioms: \[([^\]]*)\]',report)
    if not hits and marker+' does not depend on any axioms' in report: continue
    assert len(hits)==1 and set(x.strip() for x in hits[0].split(',') if x.strip())<={'propext','Classical.choice','Quot.sound'}
status='WP36A_ALL_PROGRAM_COPY_COST_BOUND_PROVED__NATIVE_MODEL_OVERHEAD_ONLY'
(w/'status.txt').write_text(status+'\n')
print(status)
