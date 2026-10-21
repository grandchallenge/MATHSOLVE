#!/usr/bin/env python3
"""Central serial admission to 8 active direct-Editorial worker runs; no /claim."""
from __future__ import annotations
from datetime import datetime,timezone,timedelta
import json,re,subprocess,sys,os
from pathlib import Path
from gcl_queue_class_contract import classify,QueueIntegrityError
REPO="grandchallenge/MATHSOLVE"; HUB=1096
PREFIX="GCL-EDITORIAL-DECISION/1\n"
MAX_ACTIVE=8; TTL=timedelta(hours=4)
REPOS={"grandchallenge/MATH-PROGRAMME","grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS",
       "grandchallenge/COMPUTATIONAL-DIFFICULTY-ATLAS"}
BOT="github-actions[bot]"
RE=re.compile(r'^EDITORIAL-(START|END)/1\nrepository: (grandchallenge/[A-Za-z0-9-]+)\nissue: ([1-9][0-9]{0,5})\nrun_id: ([0-9a-f]{32})(?:\nsource_head: ([0-9a-f]{40}))?\s*$')
class Denied(ValueError):pass
def parse(body):
    m=RE.fullmatch(body)
    if not m:raise Denied("INVALID_START_END_GRAMMAR")
    op,repo,num,run,head=m.groups()
    if repo not in REPOS or (op=="START")!=bool(head):raise Denied("ROUTE_OR_HEAD_INVALID")
    return {"op":op,"repo":repo,"issue":int(num),"run":run,"head":head}
def ledger(comments,now):
    if not isinstance(comments,list):raise Denied("HISTORY_INCOMPLETE")
    decisions={};live={};all_grants={};requests={}
    ids=set()
    for c in comments:
        ident=c.get("id")
        if type(ident)is not int or ident in ids:raise Denied("HISTORY_IDENTITY_DRIFT")
        ids.add(ident)
        actor=(c.get("user") or {}).get("login")
        if actor!=BOT:
            if c.get("body","").startswith(("EDITORIAL-START/1\n","EDITORIAL-END/1\n")):
                try:requests[ident]=(parse(c["body"]),actor)
                except Denied:pass
            continue
        if not c.get("body","").startswith(PREFIX):continue
        try:d=json.loads(c["body"][len(PREFIX):])
        except (ValueError,TypeError) as e:raise Denied("TRUSTED_DECISION_MALFORMED") from e
        required={"request_id","outcome","op","repo","issue","run","worker","expires_at","reason"}
        if set(d)!=required or type(d["request_id"])is not int or d["op"] not in ("START","END") or d["outcome"] not in ("GRANTED","ENDED","DENIED") or d["repo"] not in REPOS or type(d["issue"])is not int or not re.fullmatch(r"[0-9a-f]{32}",str(d["run"])):raise Denied("TRUSTED_DECISION_INVALID")
        if d["request_id"] in decisions:raise Denied("DUPLICATED_CONTROLLER_DECISION")
        req=requests.get(d["request_id"])
        if not req or req[1]!=d["worker"] or any((
             req[0]["op"]!=d["op"],req[0]["repo"]!=d["repo"],req[0]["issue"]!=d["issue"],req[0]["run"]!=d["run"])):
            raise Denied("DECISION_NOT_BOUND_TO_AUTHENTIC_REQUEST")
        decisions[d["request_id"]]=d
        key=(d["repo"],d["issue"],d["run"])
        if d["outcome"]=="GRANTED":
            if d["op"]!="START" or key in all_grants or not d["worker"]:raise Denied("GRANT_INTEGRITY")
            try:exp=datetime.fromisoformat(d["expires_at"])
            except (ValueError,TypeError) as e:raise Denied("EXPIRY_INTEGRITY") from e
            if exp.tzinfo is None:raise Denied("EXPIRY_TZ_MISSING")
            all_grants[key]=d
            live[key]=d
        elif d["outcome"]=="ENDED":
            if d["op"]!="END" or key not in all_grants or d["worker"]!=all_grants[key]["worker"]:raise Denied("END_INTEGRITY")
            live.pop(key,None)
    live={k:v for k,v in live.items() if datetime.fromisoformat(v["expires_at"])>now}
    if len(live)>MAX_ACTIVE:raise Denied("CAPACITY_INVARIANT_VIOLATION")
    return decisions,live
def choose(event,history,now,target=None):
    if event["issue"]["number"]!=HUB or "pull_request" in event["issue"]:raise Denied("NOT_HUB_ISSUE")
    comment=event["comment"]
    if (comment.get("user") or {}).get("type")=="Bot":raise Denied("BOT_COMMAND_FORBIDDEN")
    worker=(comment.get("user") or {}).get("login")
    if not worker or type(comment.get("id"))is not int:raise Denied("ACTOR_IDENTITY_MISSING")
    if not any(x["id"]==comment["id"] and x["body"]==comment["body"] and (x.get("user") or {}).get("login")==worker for x in history):
        raise Denied("COMMENT_NOT_IN_FRESH_HISTORY")
    decisions,live=ledger(history,now)
    if comment["id"] in decisions:return None
    cmd=parse(comment["body"]);key=(cmd["repo"],cmd["issue"],cmd["run"])
    outcome="DENIED";reason="UNKNOWN";expires=None
    if cmd["op"]=="END":
        prev=live.get(key)
        if prev and prev["worker"]==worker: outcome,reason,expires="ENDED","RELEASED",prev["expires_at"]
        else:reason="NO_MATCHING_ACTIVE_GRANT"
    else:
        if not isinstance(target,dict):raise Denied("LIVE_TARGET_LOOKUP_MISSING")
        labels={x["name"] for x in target.get("labels",[])}
        if (target.get("number")!=cmd["issue"] or target.get("state")!="open"
            or target.get("pull_request") or not {"gcl-job","gcl-state:available","gcl-pickup:direct-editorial"}<=labels):
            reason="TARGET_NOT_OPEN_AVAILABLE_DIRECT"
        else:
            try:klass,mode=classify(cmd["repo"],target["title"],labels)
            except (QueueIntegrityError,KeyError):klass,mode=None,None
            if (klass,mode)!=("Editorial","direct_editorial"):reason="NOT_EDITORIAL"
            elif key in live or any(k[:2]==key[:2] for k in live):reason="DUPLICATE_ACTIVE_ISSUE"
            elif len(live)>=MAX_ACTIVE:reason="CAPACITY_FULL"
            else:
                outcome,reason="GRANTED","CAPACITY_ADMITTED"
                expires=(now+TTL).isoformat()
    return {"request_id":comment["id"],"outcome":outcome,"op":cmd["op"],
        "repo":cmd["repo"],"issue":cmd["issue"],"run":cmd["run"],
        "worker":worker,"expires_at":expires,"reason":reason}
def gh(path,**kwargs):
    p=subprocess.run(["gh","api",path],capture_output=True,text=True,timeout=60,check=False)
    if p.returncode:raise Denied("GITHUB_READ_ERROR")
    return json.loads(p.stdout)
def main():
    event=json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text())
    if os.environ.get("GITHUB_REPOSITORY")!=REPO or os.environ.get("GITHUB_EVENT_NAME")!="issue_comment":raise Denied("HOST_EVENT_NOT_BOUND")
    if event["issue"]["number"]!=HUB:return
    h=subprocess.run(["gh","api","--paginate","--slurp",
           f"repos/{REPO}/issues/{HUB}/comments?per_page=100"],
           capture_output=True,text=True,timeout=90,check=False)
    if h.returncode:raise Denied("COMPLETE_HUB_COMMENT_READ_UNAVAILABLE")
    pages=json.loads(h.stdout)
    if not isinstance(pages,list) or not pages or any(not isinstance(p,list) for p in pages):
        raise Denied("COMPLETE_HUB_PAGINATION_MISSING")
    history=[c for p in pages for c in p]
    if len(history)>10000:raise Denied("HUB_HISTORY_EXCEEDS_GUARDED_BOUND")
    now=datetime.now(timezone.utc)
    cmd=parse(event["comment"]["body"])
    target=gh(f"repos/{cmd['repo']}/issues/{cmd['issue']}") if cmd["op"]=="START" else None
    if cmd["op"]=="START":
        gh(f"repos/{cmd['repo']}/commits/{cmd['head']}")
    choice=choose(event,history,now,target)
    if choice is None:print("IDEMPOTENT_NOOP");return
    output=Path(os.environ["RUNNER_TEMP"])/"editorial-decision.txt"
    output.write_text(PREFIX+json.dumps(choice,sort_keys=True,separators=(",",":")))
    print("EDITORIAL_DECISION",choice["outcome"],choice["repo"],choice["issue"])
if __name__=="__main__":
    try:main()
    except (Denied,ValueError,KeyError,OSError) as exc:
        print("EDITORIAL_CAPACITY_FAIL_CLOSED",str(exc),file=sys.stderr);sys.exit(2)
