#!/usr/bin/env python3
"""Fail closed on original pinned WP25 source, theorem inventory and protected parent."""
from pathlib import Path
import hashlib,json,re,subprocess,sys

if len(sys.argv)!=4:
    raise SystemExit("USAGE: WP25_SOURCE_GUARD.py LOCK SOURCE_DIR STAGED_DIR")
lock, source, staged=map(Path,sys.argv[1:])
doc=json.loads(lock.read_text())
assert doc['schema']=='PNP-ABOVE-WP25-SOURCE-LOCK/1'
assert doc['original_upstream']=='vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970'
assert doc['source_protected_parent']=='af675f4862d2f2822d6fe669ab043be438dff4ed'
assert set(doc['modules'])=={'WP25SourceEvaluator.lean'}
d=doc['modules']['WP25SourceEvaluator.lean']
assert d['path']=='research/PNP-ABOVE/WP25_SourceEvaluator.lean'
p=source/'WP25_SourceEvaluator.lean'
assert p.is_file() and not p.is_symlink()
raw=p.read_bytes()
assert not re.search(rb'(?m)^\s*(?:sorry|axiom)\b|\bnative_decide\b',raw)
assert hashlib.sha256(raw).hexdigest()==d['sha256']
assert subprocess.check_output(['git','hash-object','--',str(p)],
                               text=True).strip()==d['git_blob']
names=[x.decode() for x in re.findall(rb'^theorem\s+([A-Za-z_][A-Za-z0-9_]*)',raw,re.M)]
assert names==d['theorems'] and len(set(names))==len(names)==doc['theorem_count']==11
staged.mkdir(parents=True,exist_ok=True)
(staged/'WP25SourceEvaluator.lean').write_bytes(raw)
print('WP25_SOURCE_LOCK_PASS modules=1 theorems=11')
