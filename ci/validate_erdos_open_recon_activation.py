#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"contributions"/"ERDOS-OPEN-001"/"RECON_TRANCHE_001"
PROBLEMS=["593","595","241","470","1052","99","101","138"]
LANES=["R1","S1","A1"]
PROGRAMME="8f57c7e35393e29b1bdc180b550d30fbbc86682f"
PACK_SET="a9ab08f463740ca86fcc0efc082ce9ba5de72c04"
SHA40=re.compile(r"^[0-9a-f]{40}$"); SHA64=re.compile(r"^[0-9a-f]{64}$")
def readj(p): return json.loads(p.read_text(encoding="utf-8"))
def sha256(t): return hashlib.sha256(t.encode("utf-8")).hexdigest()
def validate():
    e=[]; c=readj(BASE/"ACTIVATION_CANDIDATE_RECEIPT.json")
    if c.get("protected_programme_predecessor")!=PROGRAMME: e.append("Programme authorization drift")
    if c.get("protected_solve_pack_set")!=PACK_SET: e.append("pack-set drift")
    if c.get("issue_byte_lock_complete") is not True: e.append("issue-byte-lock incomplete")
    if c.get("synthesis_allowed") is not False: e.append("synthesis opened on activation")
    bindings=c.get("issue_bindings",[])
    if len(bindings)!=24: e.append("expected 24 issue bindings")
    seen=set()
    for b in bindings:
        did=b.get("dispatch_id"); seen.add(did)
        dp=BASE/"dispatches"/f"{did}.json"
        if not dp.is_file(): e.append(f"{did}: missing dispatch"); continue
        d=readj(dp)
        for k in ("bootstrap_blob_sha1","task_blob_sha1","source_handoff_blob_sha"):
            if not SHA40.fullmatch(str(d.get(k,""))): e.append(f"{did}: malformed {k}")
        for k in ("bootstrap_sha256","task_sha256","source_handoff_sha256"):
            if not SHA64.fullmatch(str(d.get(k,""))): e.append(f"{did}: malformed {k}")
        if d.get("protected_programme_predecessor")!=PROGRAMME: e.append(f"{did}: Programme drift")
        if d.get("source_handoff_commit_sha")!=PACK_SET: e.append(f"{did}: source handoff drift")
        if d.get("dispatch_status")!="READY_FOR_GITHUB_COMMENT": e.append(f"{did}: dispatch not ready")
        if d.get("lease_state")!="ACTIVE": e.append(f"{did}: lease not active")
        if d.get("canonical_mutation_authorized") is not False or d.get("certification_authorized") is not False: e.append(f"{did}: authority inflation")
        bp=ROOT/d["bootstrap_path"]; lp=ROOT/d["task_path"]
        if not bp.is_file() or not lp.is_file(): e.append(f"{did}: missing bootstrap/launch"); continue
        if sha256(bp.read_text(encoding="utf-8"))!=d.get("bootstrap_sha256"): e.append(f"{did}: bootstrap digest mismatch")
        if sha256(lp.read_text(encoding="utf-8"))!=d.get("task_sha256"): e.append(f"{did}: launch digest mismatch")
        if d.get("external_sources_policy") != ("PRIMARY_SOURCES_REQUIRED" if "-S1-" in did else "PROTECTED_PACKET_ONLY"): e.append(f"{did}: source policy mismatch")
    expected={f"ERDOS-{p}-{l}-IA-001" for p in PROBLEMS for l in LANES}
    if seen!=expected: e.append("dispatch identity set drift")
    for p in PROBLEMS:
        cp=BASE/"cohorts"/f"ERDOS-{p}-BLIND-COHORT-001.json"
        if not cp.is_file(): e.append(f"{p}: missing cohort"); continue
        co=readj(cp)
        if co.get("state")!="OPEN_AWAITING_RESULTS" or co.get("synthesis_allowed") is not False or co.get("cross_disclosure_before_closure") is not False: e.append(f"{p}: blind cohort boundary drift")
        if set(co.get("dispatch_ids",[]))!={f"ERDOS-{p}-{l}-IA-001" for l in LANES}: e.append(f"{p}: cohort member drift")
    return e
def main():
    e=validate()
    if e: raise SystemExit("\n".join(e))
    print("ERDOS-OPEN activation candidate valid: 24 dispatches / 8 blind cohorts / synthesis closed")
if __name__=="__main__": main()
