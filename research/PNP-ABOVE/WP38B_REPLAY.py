#!/usr/bin/env python3
"""Fresh WP38B module check against verified WP35 and WP38A replay dependencies."""
import hashlib,json,os,re,shutil,subprocess,sys
from pathlib import Path
if not __debug__: raise SystemExit("WP38B_OPTIMIZATION_FORBIDDEN")
if len(sys.argv)!=6: raise SystemExit("USAGE: WP38B_REPLAY.py UPSTREAM GCL_HEAD WP35_REPLAY_DIR WP38A_REPLAY_DIR NEW_DIR")
u,g,w,a,d=(Path(s).resolve() for s in sys.argv[1:])
src=g/'research/PNP-ABOVE'
m=json.loads((src/'WP38B_SOURCE_LOCK.json').read_text())
sha=lambda b: hashlib.sha256(b).hexdigest()
assert m['schema']=='PNP-ABOVE-WP38B-SOURCE-LOCK/1'
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=u,text=True).strip()=='5926bdff5db621f44682a101007ef2fe3ae8d970'
subprocess.run(['git','merge-base','--is-ancestor',m['source_protected_parent'],'HEAD'],cwd=g,check=True)
assert not d.exists()
assert (w/'status.txt').read_text().strip()=='WP35_DENSE_SUPPORT_AND_SHORT_WITNESS_CLOSED__NATIVE_CLASSICAL_TRANSFER_CLOSED__LOWER_BOUND_OPEN'
assert (a/'status.txt').read_text().strip()=='WP38A_NATIVE_CANONICAL_SEARCH_CONDITIONAL_ON_SAT_DECISION__LOWER_OPEN'
# Exact protected source hashes for every staged dependency, including the
# early modules predating JSON manifests. This does not authenticate old binary
# objects independently: use the original full replay scripts for reconstruction.
protected={}
for f in src.glob('*.lean'):
    protected.setdefault(sha(f.read_bytes()),[]).append(str(f.relative_to(g)))
assert len(list((w/'PNPAbove').glob('*.lean')))==95
assert len(list((a/'PNPAbove').glob('*.lean')))==3
target=d/'PNPAbove'; target.mkdir(parents=True)
receipts=[]
for prior in (w,a):
    for f in sorted((prior/'PNPAbove').glob('*.lean')):
        b=f.read_bytes(); h=sha(b)
        assert h in protected, f'PREDECESSOR_SOURCE_NOT_PROTECTED {f.name}'
        obj=f.with_suffix('.olean')
        assert obj.is_file() and not obj.is_symlink()
        assert not (target/f.name).exists()
        shutil.copy2(f,target/f.name); shutil.copy2(obj,target/obj.name)
        receipts.append({'module':f.name,'source_sha256':h,'olean_sha256':sha(obj.read_bytes()),'protected_paths':protected[h]})
(d/'predecessor_receipts.json').write_text(json.dumps(receipts,indent=2,sort_keys=True)+'\n')
rec=m['modules']['WP38Bridge.lean']; f=g/rec['path']; b=f.read_bytes()
assert sha(b)==rec['sha256']
assert subprocess.check_output(['git','hash-object',str(f)],cwd=g,text=True).strip()==rec['git_blob']
assert not re.search(rb'\b(sorry|admit|axiom|native_decide)\b',b)
names=re.findall(r'^theorem\s+(\w+)',b.decode(),re.M)
assert names==rec['theorems'] and len(set(names))==m['theorem_count']==15
staged=target/'WP38Bridge.lean'; staged.write_bytes(b)
env=os.environ.copy()
assert (u/'lean-toolchain').read_text().strip()=='leanprover/lean4:v4.35.0-rc3'
lean=Path.home()/'.elan/toolchains/leanprover--lean4---v4.35.0-rc3/bin/lean'
assert 'version 4.35.0-rc3' in subprocess.check_output([str(lean),'--version'],text=True)
paths=[u/'.lake/build/lib/lean']+sorted((u/'.lake/packages').glob('*/.lake/build/lib/lean'))
assert all(p.is_dir() for p in paths)
env['LEAN_PATH']=':'.join(map(str,[d]+paths))
env['LEAN_NUM_THREADS']='1'
def run(args,log):
    with (d/log).open('w') as out:
        subprocess.run([str(lean),'-R',str(d),*map(str,args)],cwd=u,env=env,stdout=out,stderr=subprocess.STDOUT,check=True)
run(['-o',staged.with_suffix('.olean'),staged],'WP38Bridge.log')
audit=d/'Axioms.lean'
audit.write_text('import PNPAbove.WP38Bridge\n'+''.join('#print axioms PNPAbove.WP38.'+n+'\n' for n in names))
run([audit],'axioms.log')
report=(d/'axioms.log').read_text()
for n in names:
    marker="'PNPAbove.WP38."+n+"'"
    hits=re.findall(re.escape(marker)+r' depends on axioms: \[([^\]]*)\]',report)
    if not hits and marker+' does not depend on any axioms' in report: continue
    assert len(hits)==1 and set(x.strip() for x in hits[0].split(',') if x.strip())<={'propext','Classical.choice','Quot.sound'}
status='WP38B_VALID_PROMISE_IFF_WITNESS_IFF_CANONICAL__UNRESTRICTED_LOWER_OPEN'
(d/'status.txt').write_text(status+'\n')
print(status)
