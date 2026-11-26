#!/usr/bin/env python3
"""Fresh, source-locked algebraic core and axiom audit on approved native Linux."""
import hashlib,json,os,re,subprocess,sys
from pathlib import Path
from PNP_REPLAY_PREFLIGHT import direct_runner_guard,preflight,bounded_run
direct_runner_guard()
if not __debug__:
    raise SystemExit("WP43_OPTIMIZATION_FORBIDDEN")
if len(sys.argv)!=5:
    raise SystemExit("USAGE: WP43_REPLAY.py UPSTREAM GCL_CHECKOUT EXACT_HEAD OUTPUT")
u,g=map(lambda s:Path(s).resolve(),sys.argv[1:3])
head=sys.argv[3]; d=Path(sys.argv[4]).resolve()
def git(cwd,*args):
    return subprocess.check_output(["git",*args],cwd=cwd,text=True,timeout=15).strip()
sha=lambda b:hashlib.sha256(b).hexdigest()
assert re.fullmatch(r"[0-9a-f]{40}",head) and git(g,"rev-parse","HEAD")==head
assert not git(g,"status","--porcelain","--untracked-files=no")
src=g/"research/PNP-ABOVE"
lock=json.loads((src/"WP43_SOURCE_LOCK.json").read_text())
assert git(u,"rev-parse","HEAD")==lock["upstream"]
assert not git(u,"status","--porcelain","--untracked-files=no")
f=src/lock["file"]; data=f.read_bytes()
assert not f.is_symlink() and sha(data)==lock["sha256"]
assert git(g,"hash-object",str(f))==lock["git_blob"]
assert not re.search(rb"\b(sorry|admit|axiom|native_decide)\b",data)
names=re.findall(r"^theorem\s+(\w+)",data.decode(),re.M)
assert names==lock["theorems"] and len(set(names))==6
lean,placement=preflight(u,d)
d.mkdir(); (d/"placement.json").write_text(json.dumps(placement,sort_keys=True,indent=2)+"\n")
p=d/"PNPAbove";p.mkdir()
f=p/"WP43ReflectionCore.lean";f.write_bytes(data)
env=os.environ.copy()
env["LEAN_PATH"]=":".join(map(str,[d,u/".lake/build/lib/lean"]+sorted((u/".lake/packages").glob("*/.lake/build/lib/lean"))))
env["LEAN_NUM_THREADS"]="1"
def run(args,name):
    bounded_run([lean,"-R",d,*args],cwd=u,env=env,log=d/name,receipt=d/"execution.jsonl",seconds=120)
run(["-o",f.with_suffix(".olean"),f],"core.log")
audit=d/"Audit.lean"
audit.write_text("import PNPAbove.WP43ReflectionCore\n"+"".join("#print axioms PNPAbove.WP43."+n+"\n" for n in names))
run([audit],"axioms.log")
r=(d/"axioms.log").read_text()
for n in names:
    marker="'PNPAbove.WP43."+n+"'"
    hits=re.findall(re.escape(marker)+r" depends on axioms: \[([^\]]*)\]",r)
    if not hits and marker+" does not depend on any axioms" in r:continue
    assert len(hits)==1 and set(x.strip() for x in hits[0].split(",") if x.strip())<={"propext","Classical.choice","Quot.sound"}
result={"status":"WP43_CORE_PASS","head":head,"source_sha256":sha(data),"axioms_sha256":sha((d/"axioms.log").read_bytes()),"theorems":names}
(d/"status.json").write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
print(json.dumps(result))
