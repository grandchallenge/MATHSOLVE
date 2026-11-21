#!/usr/bin/env python3
"""Check immutable WP28A original MIPRE source bytes and theorem inventory."""
import sys,json,hashlib,re,subprocess
from pathlib import Path
if len(sys.argv)!=4:
  raise SystemExit("USAGE: WP28_SOURCE_GUARD.py LOCK SOURCE_DIR STAGED_DIR")
lock,src,staged=map(Path,sys.argv[1:])
obj=json.loads(lock.read_text())
assert obj['schema']=='PNP-ABOVE-WP28A-SOURCE-LOCK/1'
assert obj['original_upstream']=='vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970'
assert obj['source_protected_parent']=='6182a58097b759119767dc78255e0c38d9f21e03'
assert set(obj['modules'])=={'WP28UniformExponentObstruction.lean'}
rec=obj['modules']['WP28UniformExponentObstruction.lean']
assert rec['path']=='research/PNP-ABOVE/WP28_UniformExponentObstruction.lean'
p=src/'WP28_UniformExponentObstruction.lean'
assert p.is_file() and not p.is_symlink()
data=p.read_bytes()
assert not re.search(rb'(?m)^\s*(?:axiom|sorry)\b|\bnative_decide\b',data)
assert hashlib.sha256(data).hexdigest()==rec['sha256']
assert subprocess.check_output(['git','hash-object','--',str(p)],text=True).strip()==rec['git_blob']
names=[x.decode() for x in re.findall(rb'^theorem\s+([A-Za-z0-9_]+)',data,re.M)]
assert names==rec['theorems'] and len(set(names))==len(names)==obj['theorem_count']==8
staged.mkdir(parents=True,exist_ok=True)
(staged/'WP28UniformExponentObstruction.lean').write_bytes(data)
print('WP28_SOURCE_LOCK_PASS modules=1 theorems=8')
