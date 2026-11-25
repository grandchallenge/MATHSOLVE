#!/usr/bin/env python3
"""Fresh canonical witness module replay; imports only pinned upstream libraries."""
import hashlib,json,os,re,subprocess,sys
from pathlib import Path
if not __debug__: raise SystemExit("WP38_OPTIMIZATION_FORBIDDEN")
if len(sys.argv)!=4: raise SystemExit("USAGE: WP38_REPLAY.py UPSTREAM GCL_HEAD FRESH_DIR")
u,g,w=(Path(s).resolve() for s in sys.argv[1:])
m=json.loads((g/'research/PNP-ABOVE/WP38_SOURCE_LOCK.json').read_text())
assert m['schema']=='PNP-ABOVE-WP38-SOURCE-LOCK/1'
assert m['original_upstream']=='vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970'
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=u,text=True).strip()==m['original_upstream'].split('@')[1]
subprocess.run(['git','merge-base','--is-ancestor',m['protected_parent'],'HEAD'],cwd=g,check=True)
assert not w.exists()
d=w/'PNPAbove'; d.mkdir(parents=True)
env=os.environ.copy()
assert (u/'lean-toolchain').read_text().strip()=='leanprover/lean4:v4.35.0-rc3'
lean=Path.home()/'.elan/toolchains/leanprover--lean4---v4.35.0-rc3/bin/lean'
assert 'version 4.35.0-rc3' in subprocess.check_output([str(lean),'--version'],text=True)
paths=[u/'.lake/build/lib/lean']+sorted((u/'.lake/packages').glob('*/.lake/build/lib/lean'))
assert all(p.is_dir() for p in paths)
env['LEAN_PATH']=':'.join(map(str,[w]+paths))
env['LEAN_NUM_THREADS']='1'
names=[]
def run(args,log):
    with (w/log).open('w') as f:
        subprocess.run([str(lean),'-R',str(w),*map(str,args)],cwd=u,env=env,stdout=f,stderr=subprocess.STDOUT,check=True)
for mod in m['module_order']:
    rec=m['modules'][mod]; f=g/rec['path']; b=f.read_bytes()
    assert f.is_file() and not f.is_symlink()
    assert hashlib.sha256(b).hexdigest()==rec['sha256']
    assert subprocess.check_output(['git','hash-object',str(f)],cwd=g,text=True).strip()==rec['git_blob']
    assert not re.search(rb'\b(sorry|admit|axiom|native_decide)\b',b)
    assert re.findall(r'^theorem\s+(\w+)',b.decode(),re.M)==rec['theorems']
    names+=rec['theorems']
    staged=d/mod; staged.write_bytes(b)
    run(['-o',staged.with_suffix('.olean'),staged],mod+'.log')
assert len(names)==len(set(names))==m['theorem_count']
assert len(list(d.glob('*.olean')))==len(m['module_order'])==3
a=w/'Axioms.lean'
a.write_text('import PNPAbove.WP38Lex\nimport PNPAbove.WP38Parser\n'+''.join('#print axioms PNPAbove.WP38.'+n+'\n' for n in names))
run([a],'axioms.log')
report=(w/'axioms.log').read_text()
for n in names:
    marker="'PNPAbove.WP38."+n+"'"
    hits=re.findall(re.escape(marker)+r' depends on axioms: \[([^\]]*)\]',report)
    if not hits and marker+' does not depend on any axioms' in report: continue
    assert len(hits)==1 and set(x.strip() for x in hits[0].split(',') if x.strip())<={'propext','Classical.choice','Quot.sound'}
status='WP38A_NATIVE_CANONICAL_SEARCH_CONDITIONAL_ON_SAT_DECISION__LOWER_OPEN'
(w/'status.txt').write_text(status+'\n')
print(status)
