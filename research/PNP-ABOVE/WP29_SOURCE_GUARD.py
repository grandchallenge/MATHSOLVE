#!/usr/bin/env python3
"""Exact source/Git-blob proof lock. Every source byte must match."""
from pathlib import Path
import hashlib,json,re,subprocess,sys

if len(sys.argv)!=4:
    raise SystemExit("USAGE: WP29_SOURCE_GUARD.py LOCK SOURCE_DIR STAGED_DIR")
lock,source,staged=map(Path,sys.argv[1:])
m=json.loads(lock.read_text())
assert m['schema']=='PNP-ABOVE-WP29-SOURCE-LOCK/1'
assert m['original_upstream']=='vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970'
assert m['source_protected_parent']=='9bdf8c4893f8eebfe551b092e1322db7a334541a'
assert set(m['modules'])=={'WP29CNF.lean'}
rec=m['modules']['WP29CNF.lean']
assert rec['path']=='research/PNP-ABOVE/WP29_Explicit3CNF.lean'
p=source/'WP29_Explicit3CNF.lean'
assert p.is_file() and not p.is_symlink()
data=p.read_bytes()
assert not re.search(rb'\b(sorry|admit|axiom|native_decide)\b',data)
assert hashlib.sha256(data).hexdigest()==rec['sha256']
assert subprocess.check_output(['git','hash-object','--',str(p)],text=True).strip()==rec['git_blob']
names=[x.decode() for x in re.findall(rb'^theorem\s+([A-Za-z_][A-Za-z0-9_]*)',data,re.M)]
assert names==rec['theorems'] and len(set(names))==len(names)==m['theorem_count']==31
staged.mkdir(parents=True,exist_ok=True)
(staged/'WP29CNF.lean').write_bytes(data)
print('WP29_SOURCE_LOCK_PASS modules=1 theorems=31')
