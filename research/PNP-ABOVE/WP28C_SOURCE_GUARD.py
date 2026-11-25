#!/usr/bin/env python3
"""Exact source identity, original compiler and theorem-manifest audit."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
if len(sys.argv)!=4:
    raise SystemExit("USAGE: WP28C_SOURCE_GUARD.py LOCK SOURCE_DIR STAGED_DIR")
lock,source,staged=map(Path,sys.argv[1:])
m=json.loads(lock.read_text())
assert m['schema']=='PNP-ABOVE-WP28C-SOURCE-LOCK/1'
assert m['source_protected_parent']=='b0e9acce5cffa8aeff5e7a6fd9e7f20970ea9602'
assert m['original_upstream']=='vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970'
mapping={
 'WP28CPower.lean':'WP28C_PowerIndex.lean',
 'WP28CVerifier.lean':'WP28C_SourceVerifier.lean',
 'WP28CCompression.lean':'WP28C_Compression.lean',
}
assert set(m['modules'])==set(mapping)
staged.mkdir(parents=True,exist_ok=True)
names_all=[]
for mod,name in mapping.items():
    rec=m['modules'][mod]
    assert rec['path']=='research/PNP-ABOVE/'+name
    p=source/name
    assert p.is_file() and not p.is_symlink()
    d=p.read_bytes()
    assert not re.search(rb'\b(sorry|admit|axiom|native_decide)\b',d)
    assert hashlib.sha256(d).hexdigest()==rec['sha256']
    assert subprocess.check_output(['git','hash-object','--',str(p)],text=True).strip()==rec['git_blob']
    names=[x.decode() for x in re.findall(rb'^theorem\s+([A-Za-z_][A-Za-z0-9_]*)',d,re.M)]
    assert names==rec['theorems']
    names_all.extend(names)
    (staged/mod).write_bytes(d)
assert len(names_all)==len(set(names_all))==m['theorem_count']==16
print('WP28C_SOURCE_LOCK_PASS modules=3 theorems=16')
