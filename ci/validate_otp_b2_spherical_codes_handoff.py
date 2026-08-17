#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]
RECORD=ROOT/"work_packages/OPENAI_TEN_PROOFS_WP00/result_family_handoff_successors/OTP-B2-SPHERICAL-CODES.json"
SCHEMA=ROOT/"schemas/openai_ten_proofs_b2_spherical_codes_handoff.schema.json"
TARGETS=[
 "MetricCodes.Johnson.main_binary_theorem",
 "MetricCodes.Spherical.HigherHierarchy.main_general",
 "MetricCodes.Spherical.HigherHierarchy.strict_hierarchy",
 "MetricCodes.Spherical.HigherHierarchy.NumericalMaximum.eventually_kissingNumber_lt_published",
]
CLASSES=[
 "source_faithful_exact_projection",
 "source_faithful_structured_projection",
 "source_faithful_structured_projection",
 "formal_strengthening_entailing_source_asymptotic_numerical_statement",
]
AXIOMS=["propext","Quot.sound","Classical.choice"]

def load(p): return json.loads(p.read_text(encoding="utf-8"))

def validation_errors(record=None,schema=None):
    r=load(RECORD) if record is None else record
    s=load(SCHEMA) if schema is None else schema
    e=[]
    if s.get("additionalProperties") is not False: e.append("schema must remain top-level closed")
    e += [f"schema: {x.message}" for x in Draft202012Validator(s).iter_errors(r)]
    if (r.get("handoff_id"),r.get("result_family"),r.get("tracker_issue")) != ("MC-OTP-HANDOFF-B2-SPHERICAL-CODES","OTP-B2-SPHERICAL-CODES",115): e.append("identity drift")
    if r.get("protected_solve_base")!="7d1f9edf16558ba4c4396126e24fd2c9ae4826f7": e.append("Solve base drift")
    a=r.get("authority",{})
    for k,v in {
      "forge_formal_source_successor_merge":"48e8bf8e0fd157688ae83a8110d63b1e500ee688",
      "forge_semantic_merge":"0520d8bae3853798f2edca67c526133e46847a54",
      "forge_semantic_reviewed_head":"e2e288e2a23a045aa34ddec0e8495448d87facb5",
      "forge_semantic_review_id":4949549260,
      "forge_semantic_reviewer":"jimsteeg",
    }.items():
        if a.get(k)!=v: e.append(f"authority drift: {k}")
    if a.get("semantic_record") != {"repository":"grandchallenge/MATHFORGE","commit_sha":"0520d8bae3853798f2edca67c526133e46847a54","path":"sources/OPENAI-TEN-PROOFS-001/semantic/OTP-B2-SPHERICAL-CODES/audit_record.json","digest_algorithm":"git_blob_sha1","digest":"394d1211757d3fc2bc61b238e914b37245967635"}: e.append("semantic record drift")
    pdf=a.get("source_pdf",{})
    if (pdf.get("revision"),pdf.get("sha256"),pdf.get("byte_length"),pdf.get("successor_record_blob")) != ("2026-08-06","ebc561ab5c53dbd240e17a8fdb6fffeb648591eca85dbfc7466f563638f8c566",2487031,"02d1748abed36717afba46451330be165c076737"): e.append("source PDF drift")
    subj=a.get("official_subject",{})
    for k,v in {"commit":"94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6","tree":"174289e4d4958cb0509874e6e53400e098213de7","formal_successor_record_blob":"6993ce9fac2c65ffae7f2a0c7d728aab828ed532","config_blob":"b343dca9c0373f80c6304f30f261b81b371661c3","challenge_blob":"5f2bcda432b7091097ae8753cac24c08d0c10f6c","solution_blob":"51628c0db81bd6cb9a79777fa601306c9d64cbc5"}.items():
        if subj.get(k)!=v: e.append(f"formal subject drift: {k}")
    rp=a.get("replay",{})
    if (rp.get("run_id"),rp.get("job_id"),rp.get("result")) != (31945652355,95161117118,"comparator_lean_kernel_nanoda_accept"): e.append("replay drift")
    if rp.get("permitted_axioms")!=AXIOMS: e.append("axiom drift")
    g=r.get("semantic_gate",{})
    if g.get("state")!="clear" or g.get("disposition")!="SUCCESSOR_FOUR_TARGET_SURFACE__SEMANTIC_AND_NONVACUITY_CLEAR_CURRENT_ROOT": e.append("semantic gate drift")
    if g.get("activated_by_protected_merge")!="0520d8bae3853798f2edca67c526133e46847a54": e.append("activation drift")
    if g.get("forge_record_solve_handoff_authorized") is not False: e.append("Forge authority inflation")
    sc=r.get("target_scope",{})
    if sc.get("predecessor_seven_target_surface_authorized") is not False: e.append("predecessor authority transfer")
    if sc.get("lean_theorems")!=TARGETS: e.append("target drift")
    if sc.get("classifications")!=CLASSES: e.append("classification drift")
    qt="\n".join(sc.get("mandatory_qualifications",[]))
    for t in ("predecessor seven-target","not attributed to the manuscript verbatim","0.39661+o(1)","formal strengthening","Hierarchy, interlacing","do not independently certify"):
        if t not in qt: e.append(f"qualification lost: {t}")
    nv=r.get("nonvacuity",{})
    if nv.get("state")!="clear_for_successor_four_target_surface": e.append("nonvacuity drift")
    nvt="\n".join(nv.get("evidence",[]))
    for t in ("delta=1/4","s=1/2","singleton","r=0","localization"):
        if t not in nvt: e.append(f"nonvacuity evidence lost: {t}")
    adj=r.get("requested_adjudication",{})
    if adj != {"mode":"independent_result_family_review","route_id":"MC-ROUTE-OTP-B2-SPHERICAL-CODES","current_route_state":"not_registered","cert_output":None,"may_adjudicate_on_branch":False}: e.append("adjudication boundary drift")
    rc=r.get("route_controls",{})
    if rc.get("result_family_only") is not True: e.append("family isolation lost")
    for k in ("historical_six_packet_registry_mutable","may_create_aggregate_handoff","may_imply_mathcert_acceptance","may_imply_adjudication","may_claim_mathematical_proof","may_promote_claim","predecessor_target_authority_transfer","exact_039661_source_verbatim"):
        if rc.get(k) is not False: e.append(f"authority inflation: {k}")
    b=r.get("claim_boundary","")
    for t in ("exact four successor targets","predecessor seven-target surface","0.39661+o(1)","historical six-packet registry","MATHCERT route"):
        if t not in b: e.append(f"claim boundary lost: {t}")
    return e

def main():
    e=validation_errors()
    if e: print("\n".join(e),file=sys.stderr); return 1
    print("validated OTP-B2 Spherical Codes successor handoff candidate"); return 0

if __name__=="__main__": raise SystemExit(main())
