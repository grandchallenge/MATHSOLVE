#!/usr/bin/env python3
"""Fail-closed WP28B2 exact original source/axiom/parent identity guard."""
from pathlib import Path
import json,hashlib,re,subprocess,sys

if len(sys.argv)!=4:
    raise SystemExit('USAGE: WP28B2_SOURCE_GUARD.py LOCK SOURCE_DIR STAGED_DIR')
lock,src,stage=map(Path,sys.argv[1:])
m=json.loads(lock.read_text())
assert m['schema']=='PNP-ABOVE-WP28B2-SOURCE-LOCK/1'
assert m['original_upstream']=='vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970'
assert m['source_protected_parent']=='d41eb5f2af9856080fa10a7a093d1ea5d0672e08'
mods={'WP28B2NodeReader.lean':'WP28B2_NodeReader.lean',
      'WP28B2Evaluator.lean':'WP28B2_Evaluator.lean',
      'WP28B2Raw.lean':'WP28B2_RawVerifier.lean',
      'WP28B2Value.lean':'WP28B2_NativeValues.lean'}
assert set(m['modules'])==set(mods)
stage.mkdir(parents=True,exist_ok=True)
seen=set()
for module,fname in mods.items():
    rec=m['modules'][module]
    assert rec['path']==f'research/PNP-ABOVE/{fname}'
    p=src/fname
    assert p.is_file() and not p.is_symlink()
    raw=p.read_bytes()
    assert not re.search(rb'(?m)^\s*(?:axiom|sorry)\b|\bnative_decide\b',raw)
    assert hashlib.sha256(raw).hexdigest()==rec['sha256']
    assert subprocess.check_output(['git','hash-object','--',str(p)],
                                   text=True).strip()==rec['git_blob']
    theorems=[n.decode() for n in re.findall(rb'^theorem\s+([A-Za-z_][A-Za-z0-9_]*)',raw,re.M)]
    assert theorems==rec['theorems'] and not (seen & set(theorems))
    seen.update(theorems)
    (stage/module).write_bytes(raw)
assert len(seen)==m['theorem_count']==22
print(f"WP28B2_SOURCE_LOCK_PASS modules={len(mods)} theorems={len(seen)}")
