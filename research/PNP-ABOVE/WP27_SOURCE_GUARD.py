#!/usr/bin/env python3
"""Fail closed if original source SHA-256, Git blobs or theorem inventory drift."""
from pathlib import Path
import subprocess,hashlib,re,json,sys

if len(sys.argv)!=4:
    raise SystemExit("USAGE: WP27_SOURCE_GUARD.py LOCK SOURCE_ROOT STAGING_ROOT")
lock,root,stage=map(Path,sys.argv[1:])
m=json.loads(lock.read_text())
assert m['schema']=='PNP-ABOVE-WP27-SOURCE-LOCK/1'
assert m['original_upstream']=='vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970'
assert len(m['source_protected_parent'])==40
files={'RawNormalizer':'WP27_RawNormalizer.lean',
       'TotalCost':'WP27_TotalCost.lean',
       'RobustVerifier':'WP27_RobustVerifier.lean'}
assert set(m['modules'])=={f'WP27{stem}.lean' for stem in files}
stage.mkdir(parents=True,exist_ok=True)
total=0; seen=set()
for stem,filename in files.items():
    module=f'WP27{stem}.lean'
    record=m['modules'][module]
    assert record['path']==f'research/PNP-ABOVE/{filename}'
    source=root/filename
    assert source.is_file() and not source.is_symlink()
    raw=source.read_bytes()
    assert not re.search(rb'(?m)^\s*(?:sorry|axiom)\b|\bnative_decide\b',raw)
    assert hashlib.sha256(raw).hexdigest()==record['sha256']
    assert subprocess.check_output(['git','hash-object','--',str(source)],
        text=True).strip()==record['git_blob']
    names=[x.decode() for x in re.findall(rb'^theorem\s+([A-Za-z_][A-Za-z0-9_]*)',raw,re.M)]
    assert names==record['theorems']
    assert len(names)=={'RawNormalizer':5,'TotalCost':2,'RobustVerifier':12}[stem]
    assert not seen.intersection(names)
    total+=len(names);seen.update(names)
    (stage/module).write_bytes(raw)
assert total==m['theorem_count']==19
print('WP27_SOURCE_LOCK_PASS modules=3 theorems=19')
