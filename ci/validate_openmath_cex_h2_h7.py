#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
EXPECTED_SLOTS=["OM26-H2","OM26-H3","OM26-H4","OM26-H5","OM26-H6","OM26-H7"]
EXPECTED_MAPPING={
 "OM26-H2":"alejandrozu/busy-beaver-6-certificates",
 "OM26-H3":"alejandrozu/clique-cluster-ramsey-multiplicity",
 "OM26-H4":"alejandrozu/collatz-modular-descent",
 "OM26-H5":"alejandrozu/grothendieck-constant-witnesses",
 "OM26-H6":"alejandrozu/matrix-multiplication-tensor-3x3",
 "OM26-H7":"ottogin/erdos-3",
}
OPERATION="OM26-H2-H7-SOURCE-ACQ"
FORGE_RELEASE="782b80c8c57d4e77356d8c77c50ee1fffdcd92b8"

def load(rel:str):
    return json.loads((ROOT/rel).read_text(encoding="utf-8"))

def validate():
    errors=[]
    campaign=load(".gcl/campaigns/OPENMATH-2026-SOURCE-ACQ/CAMPAIGN_STATE.json")
    operation=load(".gcl/operations/OM26-H2-H7-SOURCE-ACQ/OPERATION.json")
    prep=load("work_packages/OPENMATH_2026/CEX_H2_H7_PREPARATION.json")
    hills=load("work_packages/OPENMATH_2026/HILL_LANES.json")
    registry=load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
    receipt=load("work_packages/OPENMATH_2026/H2_H7_FORGE_IMPORT.json")
    routing=load(".ghos-routing/workflows.json")

    if campaign.get("current_frontier",{}).get("id") not in {"PROTECTED_SOLVE_IMPORT_AND_READBACK_OM26_H2_H7","SOURCE_ACQUISITION_CLOSED__H2_H7_SOLVE_RELEASED"}:
        errors.append("unexpected H2-H7 campaign frontier")
    if operation.get("provider_anchor") != FORGE_RELEASE:
        errors.append("operation provider anchor mismatch")
    if receipt.get("provider",{}).get("protected_commit") != FORGE_RELEASE:
        errors.append("Forge import receipt anchor mismatch")
    if receipt.get("bindings") is None or {x.get("slot"):x.get("exact_hill_id") for x in receipt["bindings"]} != EXPECTED_MAPPING:
        errors.append("Forge import receipt mapping mismatch")

    prep_lanes=prep.get("lanes",[])
    if [x.get("slot") for x in prep_lanes] != EXPECTED_SLOTS:
        errors.append("preparation lane set mismatch")
    for lane in prep_lanes:
        slot=lane.get("slot")
        if lane.get("exact_hill_id") != EXPECTED_MAPPING.get(slot):
            errors.append(f"{slot}: exact hill identity mismatch")
        if not lane.get("forge_source_lock") or not lane.get("semantic_source_map") or not lane.get("status_triage"):
            errors.append(f"{slot}: imported provider semantics incomplete")

    by_slot={x.get("hill_slot"):x for x in hills.get("hills",[])}
    for slot in EXPECTED_SLOTS:
        lane=by_slot.get(slot)
        if not lane:
            errors.append(f"{slot}: missing Solve lane")
            continue
        if lane.get("exact_hill_id") != EXPECTED_MAPPING[slot]:
            errors.append(f"{slot}: Solve lane mapping mismatch")
        lock=lane.get("statement_lock") or {}
        if lock.get("forge_protected_commit") != FORGE_RELEASE:
            errors.append(f"{slot}: Forge commit mismatch")
        for key in ("source_lock_blob","semantic_source_map_blob","status_triage_blob","evaluator_contract_blob","semantic_pack_blob","semantic_readback_blob"):
            if not isinstance(lock.get(key),str) or len(lock[key]) != 40:
                errors.append(f"{slot}: missing {key}")

    mapping=registry.get("slot_binding_policy",{}).get("mapping")
    if mapping != EXPECTED_MAPPING:
        errors.append("registry mapping mismatch")
    source=[x for x in registry.get("assignments",[]) if x.get("class")=="SOURCE_ACQUISITION"]
    if len(source)!=6 or any(x.get("state")!="CLOSED" for x in source):
        errors.append("source-acquisition assignments must be six CLOSED records")
    if registry.get("mathematics_release_policy",{}).get("current_math_jobs") != 0:
        errors.append("H2-H7 math jobs must remain zero during import phase")

    workflow=".github/workflows/openmath-h2-h7-cex-source-acq.yml"
    entries=[x for x in routing.get("workflows",[]) if x.get("path")==workflow]
    if len(entries)!=1 or entries[0].get("controller_id")!="GITHUB_ACTIONS":
        errors.append("H2-H7 workflow routing registration mismatch")

    final = campaign.get("current_frontier",{}).get("id")=="SOURCE_ACQUISITION_CLOSED__H2_H7_SOLVE_RELEASED"
    expected_release=final
    if any(bool(x.get("solve_release")) != expected_release for x in prep_lanes):
        errors.append("preparation solve_release does not match campaign phase")
    if bool(registry.get("mathematics_release_policy",{}).get("h2_h7_solve_release")) != expected_release:
        errors.append("registry solve release does not match campaign phase")

    return errors

def main():
    errors=validate()
    if errors:
        for e in errors: print("FAIL:",e)
        raise SystemExit(1)
    print("PASS: OPENMATH H2-H7 provider import/release state is coherent")

if __name__=="__main__":
    main()
