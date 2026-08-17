#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "work_packages/OPENAI_TEN_PROOFS_WP00/result_family_handoff_successors/OTP-H-GAPCVP.json"
SCHEMA = ROOT / "schemas/openai_ten_proofs_h_gapcvp_handoff.schema.json"
TARGETS = [
    "GapCVP.Comparator.gapCVP400IsNPHard",
    "GapCVP.Comparator.binaryNearestCodewordIsNPHard",
    "GapCVP.Comparator.binarySyndromeDecodingIsNPHard",
    "GapCVP.Comparator.finitePNormGapCVPIsNPHard",
]
PROMISES = [
    "GapCVP.Comparator.gapCVP400Promise",
    "GapCVP.Comparator.binaryNearestCodewordPromise",
    "GapCVP.Comparator.binarySyndromeDecodingPromise",
    "GapCVP.Comparator.finitePGapCVPPromise",
]
CLASSES = [
    "source_faithful_restricted_consequence_integer_target",
    "source_faithful_up_to_generator_orientation",
    "source_faithful_restricted_consequence_consistent_syndrome",
    "source_faithful_fixed_rational_p_consequence",
]
FACTORS = ["n^(1/400)", "n^(1/200)", "n^(1/200)", "n^(1/(200p))"]
AXIOMS = ["propext", "Classical.choice", "Quot.sound"]


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validation_errors(record=None, schema=None):
    r = load(RECORD) if record is None else record
    s = load(SCHEMA) if schema is None else schema
    e=[]
    if s.get("additionalProperties") is not False: e.append("schema must remain top-level closed")
    e += [f"schema: {x.message}" for x in Draft202012Validator(s).iter_errors(r)]
    if (r.get("handoff_id"),r.get("result_family"),r.get("tracker_issue")) != ("MC-OTP-HANDOFF-H-GAPCVP","OTP-H-GAPCVP",113): e.append("identity drift")
    if r.get("protected_solve_base") != "7d1f9edf16558ba4c4396126e24fd2c9ae4826f7": e.append("Solve base drift")
    a=r.get("authority",{})
    for k,v in {
      "forge_formal_source_successor_merge":"48e8bf8e0fd157688ae83a8110d63b1e500ee688",
      "forge_semantic_merge":"b9dda1a5b958fd1be37a26324a025013a39584c1",
      "forge_semantic_reviewed_head":"d4de1716857998667f513f63d6ddf362eb88c054",
      "forge_semantic_review_id":4948807629,
      "forge_semantic_reviewer":"jimsteeg",
    }.items():
        if a.get(k)!=v: e.append(f"authority drift: {k}")
    if a.get("semantic_record") != {"repository":"grandchallenge/MATHFORGE","commit_sha":"b9dda1a5b958fd1be37a26324a025013a39584c1","path":"sources/OPENAI-TEN-PROOFS-001/semantic/OTP-H-GAPCVP/audit_record.json","digest_algorithm":"git_blob_sha1","digest":"673f541fbb552d307cc226c51d2f0fd2916b328d"}: e.append("semantic record drift")
    pdf=a.get("source_pdf",{})
    if (pdf.get("revision"),pdf.get("sha256"),pdf.get("byte_length"),pdf.get("successor_record_blob")) != ("2026-08-06","ebc561ab5c53dbd240e17a8fdb6fffeb648591eca85dbfc7466f563638f8c566",2487031,"02d1748abed36717afba46451330be165c076737"): e.append("source PDF drift")
    subj=a.get("official_subject",{})
    for k,v in {"commit":"94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6","tree":"174289e4d4958cb0509874e6e53400e098213de7","formal_successor_record_blob":"6993ce9fac2c65ffae7f2a0c7d728aab828ed532","config_blob":"fdba0e774acc6c2bd6fd450ee155975c0eda1833","challenge_blob":"770e202350a5c94d3f6516428ff01092cb8f8cb4","solution_blob":"47f3a395e4d9ec3e2892664860f26ed63421b0c9"}.items():
        if subj.get(k)!=v: e.append(f"formal subject drift: {k}")
    rp=a.get("replay",{})
    if (rp.get("run_id"),rp.get("job_id"),rp.get("result")) != (31945652355,95161117067,"comparator_lean_kernel_nanoda_accept"): e.append("replay drift")
    if rp.get("permitted_axioms")!=AXIOMS: e.append("axiom drift")
    g=r.get("semantic_gate",{})
    if g.get("state")!="clear" or g.get("disposition")!="PROMISE_INTERFACES_CLOSED__SEMANTIC_AND_NONVACUITY_CLEAR_CURRENT_ROOT": e.append("semantic gate drift")
    if g.get("activated_by_protected_merge")!="b9dda1a5b958fd1be37a26324a025013a39584c1": e.append("activation drift")
    if g.get("forge_record_solve_handoff_authorized") is not False: e.append("Forge authority inflation")
    sc=r.get("target_scope",{})
    if sc.get("lean_theorems")!=TARGETS: e.append("target drift")
    if sc.get("promise_interfaces")!=PROMISES: e.append("promise interface drift")
    if sc.get("classifications")!=CLASSES: e.append("classification drift")
    if sc.get("gap_factors")!=FACTORS: e.append("gap-factor drift")
    qt="\n".join(sc.get("mandatory_qualifications",[]))
    for t in ("exponent denominators","integer targets","consistent systems","transpose convention","outside the promise","do not independently certify"):
        if t not in qt: e.append(f"qualification lost: {t}")
    nv=r.get("nonvacuity",{})
    if nv != {"state":"clear_all_four_promise_interfaces","yes_witness_count":4,"no_witness_count":4,"all_yes_sides_inhabited":True,"all_no_sides_inhabited":True}: e.append("nonvacuity drift")
    adj=r.get("requested_adjudication",{})
    if adj != {"mode":"independent_result_family_review","route_id":"MC-ROUTE-OTP-H-GAPCVP","current_route_state":"not_registered","cert_output":None,"may_adjudicate_on_branch":False}: e.append("adjudication boundary drift")
    rc=r.get("route_controls",{})
    if rc.get("result_family_only") is not True: e.append("family isolation lost")
    for k in ("historical_six_packet_registry_mutable","may_create_aggregate_handoff","may_imply_mathcert_acceptance","may_imply_adjudication","may_claim_mathematical_proof","may_promote_claim","whole_source_interface_identity"):
        if rc.get(k) is not False: e.append(f"authority inflation: {k}")
    b=r.get("claim_boundary","")
    for t in ("exact four configured hardness targets","integer-target Euclidean restriction","consistent-syndrome restriction","dimension-dependent gap exponents","historical six-packet registry","MATHCERT route"):
        if t not in b: e.append(f"claim boundary lost: {t}")
    return e


def main():
    e=validation_errors()
    if e:
        print("\n".join(e),file=sys.stderr); return 1
    print("validated OTP-H GapCVP successor handoff candidate"); return 0


if __name__=="__main__": raise SystemExit(main())
