#!/usr/bin/env python3
"""No-network GCL PNP-ABOVE documentary snapshot identity/coverage check.

Not a mathematical theorem check or certification.
"""
import json,re,subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[2]
m=json.loads(Path(__file__).with_name("COVERAGE_SNAPSHOT.json").read_text())
assert m["schema"]=="GCL-PNP-ABOVE-DOCUMENTARY-SNAPSHOT/1"
source=m["source_commit"]
assert re.fullmatch(r"[0-9a-f]{40}",source)
def git(*a):return subprocess.check_output(["git","-C",str(root),*a],text=True).strip()
assert git("cat-file","-t",source)=="commit"
tree={}
for line in git("ls-tree","-r",source,"--","research/PNP-ABOVE/").splitlines():
 meta,path=line.split("\t",1)
 _,kind,blob=meta.split()
 assert kind=="blob";tree[path]=blob
assert [r["wp"] for r in m["work_packages"]]==[f"WP{i:02d}" for i in range(18)]
seen=set()
for w in m["work_packages"]:
 listed=set()
 for a in w["artifacts"]:
  p=a["path"];b=a["git_blob_sha1"]
  assert p.startswith("research/PNP-ABOVE/"+w["wp"]+"_")
  assert p in tree and tree[p]==b,(p,b,tree.get(p))
  assert git("hash-object",p)==b,("working tree changed",p)
  assert p not in seen and p not in listed,p
  listed.add(p);seen.add(p)
 assert w["primary_path"] in listed and w["receipt_path"] in listed
 assert w["claim_status"]=="BOUNDED_RESEARCH_NOT_CERTIFICATION"
assert seen==set(tree),("coverage missing",sorted(set(tree)-seen))
assert m["artifact_count"]==len(seen)==72 and m["wp_count"]==18
assert "MATHCERT mathematical certification" in m["not_claimed"]
print(f"PNP_ABOVE_COVERAGE_SNAPSHOT_PASS wp_count=18 source_artifacts={len(seen)} source_commit={source}")
