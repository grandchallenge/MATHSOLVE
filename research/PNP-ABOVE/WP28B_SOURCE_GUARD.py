#!/usr/bin/env python3
"""Fail closed on exact original WP28B1 source bytes and all 17 declarations."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
if len(sys.argv)!=4:
    raise SystemExit('USAGE: WP28B_SOURCE_GUARD.py LOCK SOURCE_DIR STAGING_DIR')
lock,src,staged=map(Path,sys.argv[1:])
m=json.loads(lock.read_text())
assert m['schema']=='PNP-ABOVE-WP28B1-SOURCE-LOCK/1'
assert m['original_upstream']=='vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970'
assert m['source_protected_parent']=='3ef8c09ecb21392ecf86e23665bc1fdd0733ae73'
assert set(m['modules'])=={'WP28BIndex.lean'}
rec=m['modules']['WP28BIndex.lean']
assert rec['path']=='research/PNP-ABOVE/WP28B_Index.lean'
p=src/'WP28B_Index.lean'
assert p.is_file() and not p.is_symlink()
raw=p.read_bytes()
assert not re.search(rb'(?m)^\s*(?:sorry|axiom)\b|\bnative_decide\b',raw)
assert hashlib.sha256(raw).hexdigest()==rec['sha256']
assert subprocess.check_output(['git','hash-object','--',str(p)],
                               text=True).strip()==rec['git_blob']
theorems=[x.decode() for x in re.findall(rb'^theorem\s+([A-Za-z0-9_]+)',raw,re.M)]
assert theorems==rec['theorems'] and len(set(theorems))==len(theorems)==m['theorem_count']==17
staged.mkdir(parents=True,exist_ok=True)
(staged/'WP28BIndex.lean').write_bytes(raw)
print('WP28B_SOURCE_LOCK_PASS modules=1 theorems=17')
