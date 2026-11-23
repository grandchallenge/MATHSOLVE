#!/usr/bin/env python3
"""Exact source/Git-blob proof lock. Every source byte must match."""
from pathlib import Path
import hashlib,json,re,subprocess,sys

if len(sys.argv)!=4:
    raise SystemExit("USAGE: WP30_SOURCE_GUARD.py LOCK SOURCE_DIR STAGED_DIR")
lock,source,staged=map(Path,sys.argv[1:])
m=json.loads(lock.read_text())
assert m['schema']=='PNP-ABOVE-WP30-SOURCE-LOCK/1'
assert m['original_upstream']=='vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970'
assert m['source_protected_parent']=='621f2866eda64f4b00d6b01145351610d0a315da'
assert set(m['modules'])=={'WP30Classical.lean'}
rec=m['modules']['WP30Classical.lean']
assert rec['path']=='research/PNP-ABOVE/WP30_CompressedClassical.lean'
p=source/'WP30_CompressedClassical.lean'
assert p.is_file() and not p.is_symlink()
data=p.read_bytes()
assert not re.search(rb'\b(sorry|admit|axiom|native_decide)\b',data)
assert hashlib.sha256(data).hexdigest()==rec['sha256']
assert subprocess.check_output(['git','hash-object','--',str(p)],text=True).strip()==rec['git_blob']
names=[x.decode() for x in re.findall(rb'^theorem\s+([A-Za-z_][A-Za-z0-9_]*)',data,re.M)]
assert names==rec['theorems'] and len(set(names))==len(names)==m['theorem_count']==2
staged.mkdir(parents=True,exist_ok=True)
(staged/'WP30Classical.lean').write_bytes(data)
print('WP30_SOURCE_LOCK_PASS modules=1 theorems=2')
