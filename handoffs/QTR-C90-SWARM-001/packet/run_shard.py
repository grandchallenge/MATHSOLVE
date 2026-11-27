#!/usr/bin/env python3
"""Transient external candidate computation; never manufactures provider custody."""
import argparse, base64, datetime as dt, hashlib, json, os, pathlib as pl
import fcntl, re, shutil, signal, subprocess as sp, sys, tempfile, time, urllib.request, zipfile
P = pl.Path
HERE = P(__file__).resolve().parent
QTR = "cd35fd801dc6573a03f53e46f5b1ba02ea430f47"
BIN = "e9c63b0d329e165cf96a1de37ee324f52ed35a95201dae347c4c6a4a3f35384c"
RECIPIENT = "F150CE96CDE0A23FDBECF8A0A708906431EFBE26"
TOOLS = {
    "qtr_c90_compact_batch.py":"18c5ee050a635876c426400e08109e26c3e32f6f9ae2f913b8a8c4806f1ac6f6",
    "qtr_c90_selector_batches.py":"b020472edeb9f828d7c0a4a49c7e8c01cfca2cc19c32b024f0ddf1040d24361c",
    "qtr_c90_external_execution.py":"3ab3e8a6fddeddc2ec2349e9ee9cb63d8381ed170c0e928d5467ca0b66530ab1",
}
def require(ok, message):
    if not ok: raise ValueError(message)
def digest(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda:f.read(1<<20),b""):h.update(chunk)
    return h.hexdigest()
def fetch(url, p, sha, end):
    with urllib.request.urlopen(url, timeout=max(1,min(60,end-time.time()))) as r, p.open("xb") as f:
        while True:
            require(time.time()<end,"lease time exhausted during download")
            b=r.read(1<<20)
            if not b:break
            f.write(b)
    require(digest(p)==sha,"input digest mismatch: "+p.name)
def now():return dt.datetime.now(dt.timezone.utc)
def api(path):return sp.check_output(["gh","api",path],timeout=60)
def observe(job):
    sys.path.insert(0,str(HERE.parents[2]/"ci"))
    from gcl_worker_queue_contract import active_reservation,parse_time
    actor=json.loads(api("user"))["login"]; issue=job["issue"]
    comments=[]
    for page in range(1,101):
        rows=json.loads(api(f"repos/grandchallenge/MATHSOLVE/issues/{issue}/comments?per_page=100&page={page}"))
        comments.extend(rows)
        if len(rows)<100:break
    else:raise ValueError("comment history exceeds bounded census")
    require(not any(str(c.get("body","")).startswith("GCL-CONTRIBUTION-RESULT/1\n") for c in comments),"existing result requires reconciliation")
    lease=active_reservation(comments,job["dispatch_id"],now(),{"github-actions[bot]"})
    require(lease is not None and lease["worker"]==actor,"no active lease for authenticated worker")
    m=re.fullmatch(r"https://github.com/grandchallenge/MATHSOLVE/blob/([0-9a-f]{40})/(.+)",lease.get("immutable_task",""))
    require(m is not None and m.group(2)==job["task_path"],"lease task mismatch")
    head=sp.check_output(["git","-C",str(HERE.parents[2]),"rev-parse","HEAD"],text=True).strip()
    require(head==m.group(1),"checkout must be exact immutable task revision")
    require(not sp.check_output(["git","-C",str(HERE.parents[2]),"status","--porcelain","--untracked-files=no"]).strip(),"tracked packet checkout modified")
    return lease,actor,int(parse_time(lease["expires_at"]).timestamp())
def available():
    a=int(re.search(r"^MemAvailable:\s+(\d+)",P("/proc/meminfo").read_text(),re.M)[1])*1024
    v2=next((x.split(":",2)[2] for x in P("/proc/self/cgroup").read_text().splitlines() if x.startswith("0::")),None)
    if v2 is not None:
        root=P("/sys/fs/cgroup"); cur=(root/v2.lstrip("/")).resolve()
        require(cur.is_relative_to(root),"invalid cgroup path")
        while True:
            lim=cur/"memory.max"; used=cur/"memory.current"
            if lim.is_file() and used.is_file() and lim.read_text().strip()!="max":
                a=min(a,max(0,int(lim.read_text())-int(used.read_text())))
            if cur==root:break
            cur=cur.parent
    return a
def main():
    ap=argparse.ArgumentParser();ap.add_argument("job",type=P);ap.add_argument("work",type=P);args=ap.parse_args()
    require(sys.platform=="linux" and os.uname().machine=="x86_64","requires existing Linux x86_64 environment")
    require(args.job.resolve().parent==HERE,"job must be an immutable packet file")
    job=json.loads(args.job.read_text());lease,actor,expires=observe(job);end=expires-120
    require(time.time()+900<end,"insufficient remaining lease time")
    require(available()>=11*2**30,"insufficient effective memory")
    w=args.work.resolve();w.mkdir(mode=0o700,exist_ok=False)
    source=w/"tools";source.mkdir(mode=0o700)
    for name,sha in TOOLS.items():
        fetch(f"https://raw.githubusercontent.com/grandchallenge/QUANTUM-TECHNOLOGIES/{QTR}/scripts/{name}",source/name,sha,end)
    sys.path.insert(0,str(source))
    import qtr_c90_compact_batch as compact
    import qtr_c90_selector_batches as batches
    exe=w/"eval-compact";fetch(job["binary_url"],exe,BIN,end);exe.chmod(0o700)
    sel=HERE/job["selector_file"]
    require(digest(sel)==job["selectors_sha256"],"selector digest mismatch")
    arc=w/"graph.zip"
    with arc.open("xb") as out:
        sp.run(["gh","api",f"repos/grandchallenge/QUANTUM-TECHNOLOGIES/actions/artifacts/{job['artifact_id']}/zip"],stdout=out,check=True,timeout=max(1,end-time.time()-900))
    require(digest(arc)==job["archive_sha256"],"graph archive digest mismatch")
    graph=w/("compiled-"+job["algebra"]+".qtrbin")
    with zipfile.ZipFile(arc) as z, graph.open("xb") as out:
        with z.open(graph.name) as f:
            while True:
                require(time.time()<end,"lease time exhausted while staging")
                chunk=f.read(1<<20)
                if not chunk:break
                out.write(chunk)
    require(digest(graph)==job["graph_sha256"]==batches.GRAPHS[job["algebra"]][1],"graph digest mismatch")
    graph.chmod(0o400)
    for file in (arc,graph):
        with file.open("rb") as f:os.posix_fadvise(f.fileno(),0,0,os.POSIX_FADV_DONTNEED)
    observed,actor2,expiry2=observe(job)
    require(observed["_comment_id"]==lease["_comment_id"] and actor==actor2 and expiry2==expires,"reservation changed")
    require(time.time()+600<end,"insufficient time for batch")
    pre=available();require(pre>=compact.CAP+compact.RESERVE,"post-stage memory preflight failed")
    minimum=pre;peak=0;start=int(time.time())
    rows=w/"rows.jsonl";timing=w/"time.txt";err=w/"stderr.txt"
    ident=[(p.stat().st_ino,p.stat().st_size,p.stat().st_mtime_ns) for p in (exe,graph,sel)]
    with rows.open("xb") as out,err.open("xb") as log:
        proc=sp.Popen(["/usr/bin/time","-v","-o",str(timing),str(exe),"--native",str(graph),"--selectors",str(sel)],stdout=out,stderr=log,start_new_session=True,env={"PATH":"/usr/bin:/bin","LC_ALL":"C"})
        try:
            while proc.poll() is None:
                minimum=min(minimum,available())
                try:children=P(f"/proc/{proc.pid}/task/{proc.pid}/children").read_text().split()
                except FileNotFoundError:children=[]
                for pid in children:
                    try:status=P(f"/proc/{pid}/status").read_text()
                    except FileNotFoundError:continue
                    m=re.search(r"^VmRSS:\s+(\d+)",status,re.M)
                    if m:peak=max(peak,int(m[1])*1024)
                require(minimum>=compact.RESERVE and peak<=compact.CAP,"sampled memory guard failed")
                require(time.time()<end,"lease time exhausted")
                time.sleep(.25)
            require(proc.returncode==0,"evaluator failed")
        except BaseException:
            try:os.killpg(proc.pid,signal.SIGTERM)
            except ProcessLookupError:pass
            try:proc.wait(timeout=3)
            except sp.TimeoutExpired:os.killpg(proc.pid,signal.SIGKILL);proc.wait()
            raise
        out.flush();os.fsync(out.fileno())
    peak=max(peak,compact.peak_from_time(timing));minimum=min(minimum,available())
    require(peak<=compact.CAP and minimum>=compact.RESERVE,"terminal memory guard failed")
    require(ident==[(p.stat().st_ino,p.stat().st_size,p.stat().st_mtime_ns) for p in (exe,graph,sel)],"input identity changed")
    compact.verify_rows(job,sel,rows)
    finish=int(time.time());require(finish<end,"lease time exhausted")
    observed,actor2,expiry2=observe(job)
    require(observed["_comment_id"]==lease["_comment_id"] and actor==actor2 and expiry2==expires,"reservation changed before return")
    receipt={"record_type":"QTR_C90_EXTERNAL_AGENT_CANDIDATE/1","job":job,"worker":actor,"reservation_comment_id":lease["_comment_id"],"claimed_at":lease["claimed_at"],"expires_at":lease["expires_at"],"started_epoch":start,"finished_epoch":finish,"peak_rss_bytes":peak,"preflight_available_bytes":pre,"minimum_available_bytes":minimum,"evaluator_sha256":BIN,"quality_exposed":False,"campaign_admission":False,"independent_execution_attested":False,"artifacts":{p.name:{"sha256":digest(p),"bytes":p.stat().st_size,"base64":base64.b64encode(p.read_bytes()).decode()} for p in (rows,timing,err)}}
    payload=json.dumps(receipt,sort_keys=True,separators=(",",":")).encode()
    require(len(payload)<=40000,"return exceeds inline size limit")
    with tempfile.TemporaryDirectory(prefix="qtr-gpg-") as tmp:
        sp.run(["gpg","--homedir",tmp,"--batch","--import",str(HERE/"recipient.asc")],check=True,stdout=sp.DEVNULL)
        encrypted=sp.check_output(["gpg","--homedir",tmp,"--batch","--trust-model","always","--armor","--recipient",RECIPIENT,"--encrypt"],input=payload,timeout=30).decode()
    require(len(encrypted)<48000,"encrypted return exceeds comment size limit")
    result=f"""GCL-CONTRIBUTION-RESULT/1
dispatch_id: {job['dispatch_id']}
agent_ref: {job['agent_ref']}
assignment: {job['assignment']}
disposition: FINITE_CERTIFICATE
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement
Computed {job['count']} assigned candidate rows with exact protected evaluator and inputs; candidate execution evidence only.

## Derivation
{encrypted.strip()}

## Assumptions beyond bootstrap
Worker-local runtime observations; no independent execution attestation.

## Verification / falsification hooks
Rows SHA256: {digest(rows)}
Reservation comment ID: {lease['_comment_id']}
Peak RSS bytes: {peak}; minimum available bytes: {minimum}.

## Claim boundary
No scoring, independent execution attestation, campaign admission or certification.

## Next residual
Coordinator decrypts and independently validates the returned candidate.
"""
    (w/"RESULT.md").write_text(result)
    print("RETURN_READY",w/"RESULT.md")
if __name__=="__main__":main()
