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
 "OM26-H6":"alejandrozu/collatz-modular-descent" if False else "alejandrozu/matrix-multiplication-tensor-3x3",
 "OM26-H7":"ottogin/erdos-3",
}

def load(rel): return json.loads((ROOT/rel).read_text(encoding="utf-8"))
def absolute_https(v):
    if not isinstance(v,str): return False
    p=urlparse(v); return p.scheme=="https" and bool(p.netloc) and bool(p.path)

def validate():
    errors=[]
    registry=load(REGISTRY)
    if registry.get("record_type")!="GCL_CEX_ASSIGNMENT_REGISTRY": errors.append("registry record_type mismatch")
    if registry.get("campaign")!="OPENMATH-2026": errors.append("registry campaign mismatch")
    disc=registry.get("discovery",{})
    for k,v in {"entrypoint_url":ENTRYPOINT_URL,"machine_registry_url":REGISTRY_URL}.items():
        if disc.get(k)!=v or not absolute_https(disc.get(k)): errors.append(f"discovery {k} mismatch")
    launch=registry.get("launch_contract",{})
    if launch.get("required_fields")!=["ENTRYPOINT_URL","DISPATCH_ID","AGENT_REF"]: errors.append("launch fields mismatch")
    if launch.get("entrypoint_url")!=ENTRYPOINT_URL: errors.append("entrypoint mismatch")
    if registry.get("lease_policy",{}).get("external_self_claim_allowed") is not False: errors.append("self-claim enabled")

    source=[x for x in registry.get("assignments",[]) if x.get("class")=="SOURCE_ACQUISITION"]
    if len(source)!=6 or any(x.get("state")!="CLOSED" for x in source): errors.append("source assignments are not closed")
    if {x.get("slot_binding"):x.get("external_hill_id") for x in source}!=EXPECTED_MAPPING: errors.append("source assignment mapping mismatch")

    math=[x for x in registry.get("assignments",[]) if x.get("class")=="MATHEMATICAL_RESEARCH"]
    h1=[x for x in math if x.get("assignment_id")=="OM26-H1-H1-12"]
    if len(h1)!=1: errors.append("inaugural H1 assignment missing")
    else:
        item=h1[0]; lease=item.get("lease",{})
        if item.get("state")!="LEASED" or lease.get("state")!="LEASED": errors.append("H1 lease not active")
        if lease.get("dispatch_id")!=H1_DISPATCH_ID or lease.get("agent_ref")!=H1_AGENT_REF: errors.append("H1 lease identity mismatch")
        if lease.get("dispatch_url")!=H1_ISSUE_URL or lease.get("return_url")!=H1_ISSUE_URL: errors.append("H1 return surface mismatch")

    if registry.get("mathematics_release_policy",{}).get("current_math_jobs")!=0:
        errors.append("H2-H7 math job count changed before decomposition tranche")
    if registry.get("slot_binding_policy",{}).get("mapping")!=EXPECTED_MAPPING:
        errors.append("registry H2-H7 mapping mismatch")

    entry=(ROOT/ENTRYPOINT).read_text(encoding="utf-8")
    for marker in (ENTRYPOINT_URL,REGISTRY_URL,"DISPATCH_ID:","AGENT_REF:","work_package_url"):
        if marker not in entry: errors.append(f"entrypoint missing {marker}")
    board=(ROOT/BOARD).read_text(encoding="utf-8")
    for marker in ("OM26-H1-H1-12-IA-001","IMPORT_PROTECTION_PENDING","No H2-H7 mathematical assignment is executable yet."):
        if marker not in board: errors.append(f"board missing {marker}")
    return errors

def main():
    errors=validate()
    if errors:
        for e in errors: print("FAIL:",e)
        return 1
    print("PASS: OPENMATH CEX board matches protected H1 lease and H2-H7 import phase")
    return 0

if __name__=="__main__": raise SystemExit(main())
