#!/usr/bin/env python3
"""Exact source/Git-blob proof lock. Every source byte must match."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
if not __debug__: raise SystemExit("WP34_GUARD_OPTIMIZATION_FORBIDDEN")

if len(sys.argv)!=4:
    raise SystemExit("USAGE: WP34_SOURCE_GUARD.py LOCK SOURCE_DIR STAGED_DIR")
lock,source,staged=map(Path,sys.argv[1:])
m=json.loads(lock.read_text())
assert m['schema']=='PNP-ABOVE-WP34-SOURCE-LOCK/1'
assert m['original_upstream']=='vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970'
assert m['source_protected_parent']=='935a2e59d13bfb39487b166e187e38e794b913f9'
assert set(m['modules'])=={'WP34Scope.lean'}
rec=m['modules']['WP34Scope.lean']
assert rec['path']=='research/PNP-ABOVE/WP34_CanonicalScope.lean'
p=source/'WP34_CanonicalScope.lean'
assert p.is_file() and not p.is_symlink()
data=p.read_bytes()
assert not re.search(rb'\b(sorry|admit|axiom|native_decide)\b',data)
assert hashlib.sha256(data).hexdigest()==rec['sha256']
assert subprocess.check_output(['git','hash-object','--',str(p)],text=True).strip()==rec['git_blob']
names=[x.decode() for x in re.findall(rb'^theorem\s+([A-Za-z_][A-Za-z0-9_]*)',data,re.M)]
assert names==rec['theorems'] and len(set(names))==len(names)==m['theorem_count']==29
staged.mkdir(parents=True,exist_ok=True)
(staged/'WP34Scope.lean').write_bytes(data)
print('WP34_SOURCE_LOCK_PASS modules=1 theorems=29')
