#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parents[1]
REGISTRY=".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json"
BOARD="handoffs/OPENMATH-2026/CEX_JOB_BOARD.md"
ENTRYPOINT="handoffs/OPENMATH-2026/CEX_AGENT_ENTRYPOINT.md"
BASE_URL="https://github.com/grandchallenge/MATHSOLVE"
ENTRYPOINT_URL=BASE_URL+"/blob/main/"+ENTRYPOINT
REGISTRY_URL="https://raw.githubusercontent.com/grandchallenge/MATHSOLVE/main/"+REGISTRY
H1={"assignment":"OM26-H1-H1-12","dispatch":"OM26-H1-H1-12-IA-001","agent":"INDEPENDENT-AGENT-001","issue":498}
INTRO="3c835aaf6173176b64efca5f03ffdc27b20af965"
EXPECTED={
  "OM26-H2-WP01": {
    "hill": "OM26-H2",
    "dispatch": "OM26-H2-WP01-IA-001",
    "agent": "INDEPENDENT-AGENT-002",
    "issue": 505
  },
  "OM26-H3-WP01": {
    "hill": "OM26-H3",
    "dispatch": "OM26-H3-WP01-IA-001",
    "agent": "INDEPENDENT-AGENT-003",
    "issue": 506
  },
  "OM26-H4-WP01": {
    "hill": "OM26-H4",
    "dispatch": "OM26-H4-WP01-IA-001",
    "agent": "INDEPENDENT-AGENT-004",
    "issue": 507
  },
  "OM26-H5-WP01": {
    "hill": "OM26-H5",
    "dispatch": "OM26-H5-WP01-IA-001",
    "agent": "INDEPENDENT-AGENT-005",
    "issue": 508
  },
  "OM26-H6-WP01": {
    "hill": "OM26-H6",
    "dispatch": "OM26-H6-WP01-IA-001",
    "agent": "INDEPENDENT-AGENT-006",
    "issue": 509
  },
  "OM26-H7-WP01": {
    "hill": "OM26-H7",
    "dispatch": "OM26-H7-WP01-IA-001",
    "agent": "INDEPENDENT-AGENT-007",
    "issue": 510
  }
}

def load(rel): return json.loads((ROOT/rel).read_text(encoding="utf-8"))
def absolute_https(v):
    if not isinstance(v,str): return False
    p=urlparse(v); return p.scheme=="https" and bool(p.netloc) and bool(p.path)
def git_blob_sha1(path):
    data=(ROOT/path).read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode()+data).hexdigest()

def validate():
    errors=[]
    registry=load(REGISTRY)
    if registry.get("record_type")!="GCL_CEX_ASSIGNMENT_REGISTRY": errors.append("registry record_type mismatch")
    disc=registry.get("discovery",{})
    if disc.get("entrypoint_url")!=ENTRYPOINT_URL or not absolute_https(disc.get("entrypoint_url")): errors.append("entrypoint discovery mismatch")
    if disc.get("machine_registry_url")!=REGISTRY_URL or not absolute_https(disc.get("machine_registry_url")): errors.append("machine registry discovery mismatch")
    if registry.get("lease_policy",{}).get("external_self_claim_allowed") is not False: errors.append("external self-claim enabled")

    math=[x for x in registry.get("assignments",[]) if x.get("class")=="MATHEMATICAL_RESEARCH"]
    h1=[x for x in math if x.get("assignment_id")==H1["assignment"]]
    if len(h1)!=1: errors.append("H1 lease missing")
    else:
        lease=h1[0].get("lease",{})
        if h1[0].get("state")!="LEASED" or lease.get("state")!="LEASED": errors.append("H1 not leased")
        if lease.get("dispatch_id")!=H1["dispatch"] or lease.get("agent_ref")!=H1["agent"] or lease.get("dispatch_issue_number")!=H1["issue"]: errors.append("H1 lease identity mismatch")

    seen_agents=set(); seen_issues=set(); seen_dispatches=set()
    for aid,exp in EXPECTED.items():
        items=[x for x in math if x.get("assignment_id")==aid]
        if len(items)!=1:
            errors.append(f"{aid}: expected exactly one assignment"); continue
        item=items[0]; lease=item.get("lease",{})
        if item.get("hill")!=exp["hill"] or item.get("slot_binding")!=exp["hill"]: errors.append(f"{aid}: hill binding mismatch")
        if item.get("state")!="LEASED" or lease.get("state")!="LEASED": errors.append(f"{aid}: not LEASED")
        if lease.get("dispatch_id")!=exp["dispatch"] or lease.get("agent_ref")!=exp["agent"] or lease.get("dispatch_issue_number")!=exp["issue"]: errors.append(f"{aid}: lease identity mismatch")
        if lease.get("protected_lease_commit")!=INTRO: errors.append(f"{aid}: introducing commit mismatch")
        url=BASE_URL+f"/issues/{exp['issue']}"
        if lease.get("dispatch_url")!=url or lease.get("return_url")!=url: errors.append(f"{aid}: return URL mismatch")
        if exp["agent"] in seen_agents: errors.append(f"{aid}: duplicate agent_ref")
        if exp["issue"] in seen_issues: errors.append(f"{aid}: duplicate issue")
        if exp["dispatch"] in seen_dispatches: errors.append(f"{aid}: duplicate dispatch")
        seen_agents.add(exp["agent"]); seen_issues.add(exp["issue"]); seen_dispatches.add(exp["dispatch"])
        expected_wp=f"handoffs/OPENMATH-2026/jobs/{exp['dispatch']}.md"
        if item.get("work_package")!=expected_wp or item.get("work_package_url")!=BASE_URL+"/blob/main/"+expected_wp: errors.append(f"{aid}: work-package locator mismatch")
        dpath=item.get("dispatch_record"); opath=item.get("operation_contract")
        if not dpath or not (ROOT/dpath).is_file(): errors.append(f"{aid}: dispatch record missing"); continue
        if not opath or not (ROOT/opath).is_file(): errors.append(f"{aid}: operation contract missing"); continue
        dispatch=load(dpath); operation=load(opath)
        if dispatch.get("dispatch_id")!=exp["dispatch"] or dispatch.get("agent_ref")!=exp["agent"] or dispatch.get("assignment_id")!=aid: errors.append(f"{aid}: dispatch record identity mismatch")
        if dispatch.get("github_issue_number")!=exp["issue"] or dispatch.get("github_issue_url")!=url: errors.append(f"{aid}: dispatch issue mismatch")
        if dispatch.get("bootstrap_path")!=expected_wp: errors.append(f"{aid}: bootstrap path mismatch")
        if dispatch.get("bootstrap_blob_sha1")!=git_blob_sha1(expected_wp): errors.append(f"{aid}: bootstrap blob mismatch")
        if operation.get("dispatch_id")!=exp["dispatch"] or operation.get("agent_ref")!=exp["agent"] or operation.get("assignment_id")!=aid: errors.append(f"{aid}: operation identity mismatch")
        if not isinstance(operation.get("acceptable_dispositions"),list) or not operation["acceptable_dispositions"]: errors.append(f"{aid}: no acceptable dispositions")

    policy=registry.get("mathematics_release_policy",{})
    if policy.get("h2_h7_available_math_jobs")!=0 or policy.get("h2_h7_leased_math_jobs")!=6: errors.append("H2-H7 lease counters mismatch")
    if registry.get("wp01_leases",{}).get("lease_introducing_commit")!=INTRO: errors.append("aggregate lease introducing commit mismatch")

    board=(ROOT/BOARD).read_text(encoding="utf-8")
    for exp in EXPECTED.values():
        for marker in (exp["dispatch"],exp["agent"],f"#{exp['issue']}"):
            if marker not in board: errors.append(f"board missing {marker}")
    entry=(ROOT/ENTRYPOINT).read_text(encoding="utf-8")
    for marker in (ENTRYPOINT_URL,REGISTRY_URL,"DISPATCH_ID:","AGENT_REF:","work_package_url"):
        if marker not in entry: errors.append(f"entrypoint missing {marker}")
    return errors

def main():
    errors=validate()
    if errors:
        for e in errors: print("FAIL:",e)
        return 1
    print("PASS: OPENMATH CEX has six distinct H2-H7 WP01 leases plus the preserved H1 lease")
    return 0

if __name__=="__main__": raise SystemExit(main())
