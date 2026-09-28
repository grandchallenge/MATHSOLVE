#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parents[1]
REGISTRY=".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json"
BOARD="handoffs/OPENMATH-2026/CEX_JOB_BOARD.md"
ENTRYPOINT="handoffs/OPENMATH-2026/CEX_AGENT_ENTRYPOINT.md"
BASE_URL="https://github.com/grandchallenge/MATHSOLVE"
ENTRYPOINT_URL=BASE_URL+"/blob/main/"+ENTRYPOINT
REGISTRY_URL="https://raw.githubusercontent.com/grandchallenge/MATHSOLVE/main/"+REGISTRY
H1_DISPATCH_ID="OM26-H1-H1-12-IA-001"
H1_AGENT_REF="INDEPENDENT-AGENT-001"
H1_ISSUE_URL=BASE_URL+"/issues/498"
EXPECTED_MAPPING={
 "OM26-H2":"alejandrozu/busy-beaver-6-certificates",
 "OM26-H3":"alejandrozu/clique-cluster-ramsey-multiplicity",
 "OM26-H4":"alejandrozu/collatz-modular-descent",
 "OM26-H5":"alejandrozu/grothendieck-constant-witnesses",
 "OM26-H6":"alejandrozu/matrix-multiplication-tensor-3x3",
 "OM26-H7":"ottogin/erdos-3",
}
WP01={"OM26-H2-WP01":"OM26-H2","OM26-H3-WP01":"OM26-H3","OM26-H4-WP01":"OM26-H4","OM26-H5-WP01":"OM26-H5","OM26-H6-WP01":"OM26-H6","OM26-H7-WP01":"OM26-H7"}

def load(rel): return json.loads((ROOT/rel).read_text(encoding="utf-8"))
def absolute_https(v):
    if not isinstance(v,str): return False
    p=urlparse(v); return p.scheme=="https" and bool(p.netloc) and bool(p.path)

def validate():
    errors=[]
    registry=load(REGISTRY)
    if registry.get("record_type")!="GCL_CEX_ASSIGNMENT_REGISTRY": errors.append("registry record_type mismatch")
    disc=registry.get("discovery",{})
    if disc.get("entrypoint_url")!=ENTRYPOINT_URL or not absolute_https(disc.get("entrypoint_url")): errors.append("entrypoint discovery mismatch")
    if disc.get("machine_registry_url")!=REGISTRY_URL or not absolute_https(disc.get("machine_registry_url")): errors.append("machine registry discovery mismatch")
    if registry.get("lease_policy",{}).get("external_self_claim_allowed") is not False: errors.append("external self-claim enabled")

    source=[x for x in registry.get("assignments",[]) if x.get("class")=="SOURCE_ACQUISITION"]
    if len(source)!=6 or any(x.get("state")!="CLOSED" for x in source): errors.append("source assignments are not closed")
    if {x.get("slot_binding"):x.get("external_hill_id") for x in source}!=EXPECTED_MAPPING: errors.append("source mapping mismatch")

    math=[x for x in registry.get("assignments",[]) if x.get("class")=="MATHEMATICAL_RESEARCH"]
    h1=[x for x in math if x.get("assignment_id")=="OM26-H1-H1-12"]
    if len(h1)!=1: errors.append("H1 lease missing")
    else:
        lease=h1[0].get("lease",{})
        if h1[0].get("state")!="LEASED" or lease.get("state")!="LEASED": errors.append("H1 not leased")
        if lease.get("dispatch_id")!=H1_DISPATCH_ID or lease.get("agent_ref")!=H1_AGENT_REF: errors.append("H1 lease identity mismatch")
        if lease.get("dispatch_url")!=H1_ISSUE_URL or lease.get("return_url")!=H1_ISSUE_URL: errors.append("H1 return surface mismatch")

    wp=[x for x in math if x.get("assignment_id") in WP01]
    if len(wp)!=6: errors.append("expected six H2-H7 WP01 assignments")
    for item in wp:
        aid=item.get("assignment_id"); slot=WP01.get(aid)
        if item.get("hill")!=slot or item.get("slot_binding")!=slot: errors.append(f"{aid}: hill binding mismatch")
        if item.get("state")!="AVAILABLE_FOR_LEASE": errors.append(f"{aid}: must be AVAILABLE_FOR_LEASE")
        lease=item.get("lease",{})
        if lease.get("state")!="UNCLAIMED" or any(lease.get(k) is not None for k in ("dispatch_id","agent_ref","dispatch_issue_number","protected_lease_commit","dispatch_url","return_url")):
            errors.append(f"{aid}: unleased assignment carries execution identity")
        if item.get("permissions",{}).get("hill_specific_mathematics") is not True: errors.append(f"{aid}: math permission missing")
        for key in ("competition_submission","certification","canonical_claim_mutation"):
            if item.get("permissions",{}).get(key) is not False: errors.append(f"{aid}: prohibited permission enabled {key}")
        path=item.get("work_package")
        if not path or not (ROOT/path).is_file(): errors.append(f"{aid}: work package missing")
        if item.get("work_package_url")!=BASE_URL+"/blob/main/"+str(path): errors.append(f"{aid}: absolute work_package_url mismatch")

    policy=registry.get("mathematics_release_policy",{})
    if policy.get("current_math_jobs")!=6 or policy.get("h2_h7_available_math_jobs")!=6 or policy.get("h2_h7_leased_math_jobs")!=0:
        errors.append("H2-H7 math job counters mismatch")

    entry=(ROOT/ENTRYPOINT).read_text(encoding="utf-8")
    for marker in (ENTRYPOINT_URL,REGISTRY_URL,"DISPATCH_ID:","AGENT_REF:","work_package_url"):
        if marker not in entry: errors.append(f"entrypoint missing {marker}")
    board=(ROOT/BOARD).read_text(encoding="utf-8")
    for aid in WP01:
        if aid not in board: errors.append(f"board missing {aid}")
    if "none is executable yet" not in board: errors.append("board lost non-executable availability boundary")
    return errors

def main():
    errors=validate()
    if errors:
        for e in errors: print("FAIL:",e)
        return 1
    print("PASS: OPENMATH CEX exposes six bounded H2-H7 WP01 assignments as AVAILABLE_FOR_LEASE with zero leases")
    return 0

if __name__=="__main__": raise SystemExit(main())
