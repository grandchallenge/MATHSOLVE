#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def fail(msg):
    raise SystemExit("GCL BSD-R5-WIT preflight: FAIL: " + msg)

def load(rel):
    p = ROOT / rel
    if not p.exists():
        fail("missing " + rel)
    return json.loads(p.read_text())

def blob(rel):
    data = (ROOT / rel).read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

def main():
    if len(sys.argv) != 3 or sys.argv[1:] != ["BSD-001", "BSD-R5-WIT"]:
        fail("expected BSD-001 BSD-R5-WIT")

    state = load(".gcl/campaigns/BSD-001/CAMPAIGN_STATE.json")
    op = load(".gcl/operations/BSD-R5-WIT/OPERATION.json")
    fr = load(".gcl/admission/BSD-R5-WIT/FREEZE.json")

    if state["current_operation"] != "BSD-R5-WIT" or op["operation"] != "BSD-R5-WIT":
        fail("operation mismatch")
    if state["current_frontier"]["id"] != op["objective"]["frontier"]:
        fail("frontier mismatch")
    if state["candidate_disposition"]["type"] != op["candidate_disposition"] or op["candidate_disposition"] != "BLOCKED":
        fail("disposition mismatch")
    if state["candidate_disposition"]["blocked_on"] != op["blocked_on"]:
        fail("blocked frontier mismatch")
    if not state["protected_inputs"]["math_base"].endswith(op["protected_base"]):
        fail("base mismatch")
    if not state["protected_inputs"]["provider"].endswith(op["provider_anchor"]):
        fail("provider mismatch")
    if not state["authority"]["constitution"].endswith(op["constitutional_anchor"]):
        fail("constitution mismatch")
    if state["execution_standard"]["staffing_directive"] != op["staffing_directive"]:
        fail("staffing directive mismatch")
    if fr["protected_base"] != op["protected_base"]:
        fail("freeze base mismatch")
    if fr["provider_anchor"] != op["provider_anchor"]:
        fail("freeze provider mismatch")

    ledger = (ROOT / op["validation"]["claim_ledger"]).read_text()
    theorem = (ROOT / op["validation"]["theorem"]).read_text()
    frontier = (ROOT / op["validation"]["frontier_record"]).read_text()
    combined = "\n".join((ledger, theorem, frontier))

    for token in op["validation"]["required_tokens"]:
        if token not in combined:
            fail("missing token " + token)
    for token in op["validation"]["forbidden_tokens"]:
        if token in ledger:
            fail("forbidden token " + token)
    for key, value in op["claim_firewall"].items():
        if value is False and f"{key}: false" not in ledger:
            fail("firewall " + key)
        if value is True and f"{key}: true" not in ledger:
            fail("protected truth " + key)

    routing = load(op["validation"]["routing_registry"])
    if op["validation"]["workflow"] not in {x.get("path") for x in routing["workflows"]}:
        fail("workflow not routed")
    if not (ROOT / op["validation"]["workflow"]).exists():
        fail("workflow missing")

    if set(fr["artifacts"]) != set(op["governed_artifacts"]):
        fail("freeze set mismatch")
    for rel in op["governed_artifacts"]:
        if not (ROOT / rel).exists():
            fail("missing " + rel)
        if blob(rel) != fr["artifacts"][rel]:
            fail("freeze mismatch " + rel)

    print(json.dumps({
        "status": "PASS",
        "campaign": "BSD-001",
        "operation": "BSD-R5-WIT",
        "candidate_disposition": "BLOCKED",
        "blocked_on": op["blocked_on"],
        "frozen_artifacts": len(op["governed_artifacts"]),
        "r5_lift": True,
        "r5_prim": False,
        "r5_res": False,
        "bsd_r2_a1": False,
        "mathcert_certified": False,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
