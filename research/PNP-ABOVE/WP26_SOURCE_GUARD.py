#!/usr/bin/env python3
"""Source-lock exact original WP26 modules and theorem declarations."""
from pathlib import Path
import json,re,hashlib,subprocess,sys
if len(sys.argv)!=4:
  raise SystemExit("USAGE: WP26_SOURCE_GUARD.py MANIFEST SOURCE_ROOT STAGING_ROOT")
doc,src,out=map(Path,sys.argv[1:])
m=json.loads(doc.read_text())
assert m['schema']=='PNP-ABOVE-WP26-SOURCE-LOCK/1'
assert m['original_upstream']=='vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970'
assert m['source_protected_parent']=='df62dc3de0a585ff490f4e56abf5d1c76cb6f12e'
names={'NativeVerifier':'WP26_NativeVerifier.lean',
       'UniformCompiler':'WP26_UniformCompiler.lean'}
assert set(m['modules'])=={f'WP26{s}.lean' for s in names}
out.mkdir(parents=True,exist_ok=True)
seen=set();total=0
for stem,filename in names.items():
  module=f'WP26{stem}.lean'
  rec=m['modules'][module]
  assert rec['path']==f'research/PNP-ABOVE/{filename}'
  f=src/filename
  assert f.is_file() and not f.is_symlink()
  raw=f.read_bytes()
  assert not re.search(rb'(?m)^\s*(?:sorry|axiom)\b|\bnative_decide\b',raw)
  assert hashlib.sha256(raw).hexdigest()==rec['sha256']
  assert subprocess.check_output(['git','hash-object','--',str(f)],text=True).strip()==rec['git_blob']
  theorem_names=[x.decode() for x in re.findall(rb'^theorem\s+([A-Za-z_][A-Za-z0-9_]*)',raw,re.M)]
  assert rec['theorems']==theorem_names
  assert not set(theorem_names)&seen
  seen.update(theorem_names);total+=len(theorem_names)
  (out/module).write_bytes(raw)
assert total==m['theorem_count']==32
print(f'WP26_SOURCE_LOCK_PASS modules=2 theorems={total}')
