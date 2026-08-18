#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]
RECORD=ROOT/"work_packages/OPENAI_TEN_PROOFS_WP00/result_family_handoff_successors/OTP-A-SPHERE-PACKING.json"
SCHEMA=ROOT/"schemas/openai_ten_proofs_a_sphere_packing_handoff.schema.json"
TARGETS=[
 "PackingBounds.FullMain.exact_limit",
 "PackingBounds.FullMain.exact_binary_exponent",
 "PackingBounds.PackingBridge.sphere_packing_sharp_asymptotic_upper",
 "PackingBounds.sharpFullCohnElkiesManuscriptConclusions",
]
CLASSES=[
 "direct_source_theorem_projection_modulo_proved_full_radial_equivalence",
 "derived_base_two_logarithmic_consequence",
 "source_faithful_displayed_consequence_with_proved_scale_normalization",
 "source_faithful_derived_composite_certificate",
]
AXIOMS=["propext","Classical.choice","Quot.sound"]

def load(p): return json.loads(p.read_text(encoding="utf-8"))

def validation_errors(record=None,schema=None):
    r=load(RECORD) if record is None else record
    s=load(SCHEMA) if schema is None else schema
    e=[]
    if s.get("additionalProperties") is not False: e.append("schema must remain top-level closed")
    e += [f"schema: {x.message}" for x in Draft202012Validator(s).iter_errors(r)]
    if (r.get("handoff_id"),r.get("result_family"),r.get("tracker_issue")) != ("MC-OTP-HANDOFF-A-SPHERE-PACKING","OTP-A-SPHERE-PACKING",112): e.append("identity drift")
    if r.get("protected_solve_base")!="7d1f9edf16558ba4c4396126e24fd2c9ae4826f7": e.append("Solve base drift")
    a=r.get("authority",{})
    for k,v in {
      "forge_formal_source_successor_merge":"48e8bf8e0fd157688ae83a8110d63b1e500ee688",
      "forge_composite_semantic_merge":"706d0291370bf3f14aa37be0823e33d06f7343b0",
      "forge_bridge_semantic_merge":"5a0cb9a7b7eef210dd0fce5c527d09b6eef3bc12",
      "forge_bridge_reviewed_head":"e1208d042da9f1a85da84c74a3f0804737e25f92",
      "forge_bridge_review_id":4948688730,
      "forge_semantic_reviewer":"jimsteeg",
    }.items():
        if a.get(k)!=v: e.append(f"authority drift: {k}")
    if a.get("composite_semantic_record") != {"repository":"grandchallenge/MATHFORGE","commit_sha":"706d0291370bf3f14aa37be0823e33d06f7343b0","path":"sources/OPENAI-TEN-PROOFS-001/semantic/OTP-A-SPHERE-PACKING-COMPOSITE/audit_record.json","digest_algorithm":"git_blob_sha1","digest":"b2e309ad96e750651fc7149a6bad54c6bf99015b"}: e.append("composite record drift")
    if a.get("bridge_semantic_record") != {"repository":"grandchallenge/MATHFORGE","commit_sha":"5a0cb9a7b7eef210dd0fce5c527d09b6eef3bc12","path":"sources/OPENAI-TEN-PROOFS-001/semantic/OTP-A-SPHERE-PACKING-BRIDGE/audit_record.json","digest_algorithm":"git_blob_sha1","digest":"7858b156fc4490ecc6e3572dcf449d84dcc99f93"}: e.append("bridge record drift")
    pdf=a.get("source_pdf",{})
    if (pdf.get("revision"),pdf.get("sha256"),pdf.get("byte_length"),pdf.get("successor_record_blob")) != ("2026-08-06","ebc561ab5c53dbd240e17a8fdb6fffeb648591eca85dbfc7466f563638f8c566",2487031,"02d1748abed36717afba46451330be165c076737"): e.append("source PDF drift")
    subj=a.get("official_subject",{})
    for k,v in {"commit":"94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6","tree":"174289e4d4958cb0509874e6e53400e098213de7","formal_successor_record_blob":"6993ce9fac2c65ffae7f2a0c7d728aab828ed532","config_blob":"46b2e7b49da43fb17a7efa88652f8ee1adc01cbe","challenge_blob":"2477846e1883534837340c636fd928b091509783","solution_blob":"e6117934a80142a8249356fdafa797eba030e920"}.items():
        if subj.get(k)!=v: e.append(f"formal subject drift: {k}")
    rp=a.get("replay",{})
    if (rp.get("run_id"),rp.get("job_id"),rp.get("result")) != (31945652355,95161117046,"comparator_lean_kernel_nanoda_accept"): e.append("replay drift")
    if rp.get("permitted_axioms")!=AXIOMS: e.append("axiom drift")
    g=r.get("semantic_gate",{})
    if g.get("state")!="clear" or g.get("disposition")!="SPHERE_PACKING_CURRENT_ROOT__SEMANTIC_AND_NONVACUITY_CLEAR__SOLVE_HANDOFF_NOT_AUTHORIZED": e.append("semantic gate drift")
    if g.get("activated_by_protected_merge")!="5a0cb9a7b7eef210dd0fce5c527d09b6eef3bc12": e.append("activation drift")
    if g.get("forge_record_solve_handoff_authorized") is not False: e.append("Forge authority inflation")
    sc=r.get("target_scope",{})
    if sc.get("lean_theorems")!=TARGETS: e.append("target drift")
    if sc.get("classifications")!=CLASSES: e.append("classification drift")
    qt="\n".join(sc.get("mandatory_qualifications",[]))
    for t in ("not a single verbatim manuscript theorem","30-decimal","rescaling invariance","little-o witness","whole-chapter"):
        if t not in qt: e.append(f"qualification lost: {t}")
    nv=r.get("nonvacuity",{})
    if nv.get("state")!="clear_for_current_root_four_target_surface": e.append("nonvacuity drift")
    nvt="\n".join(nv.get("evidence",[]))
    for t in ("admissible_nonempty","fullQuotientSet_eq_radial","singleton","upper_packing_density_le_one","positive-dimensional"):
        if t not in nvt: e.append(f"nonvacuity evidence lost: {t}")
    adj=r.get("requested_adjudication",{})
    if adj != {"mode":"independent_result_family_review","route_id":"MC-ROUTE-OTP-A-SPHERE-PACKING","current_route_state":"not_registered","cert_output":None,"may_adjudicate_on_branch":False}: e.append("adjudication boundary drift")
    rc=r.get("route_controls",{})
    if rc.get("result_family_only") is not True: e.append("family isolation lost")
    for k in ("historical_six_packet_registry_mutable","may_create_aggregate_handoff","may_imply_mathcert_acceptance","may_imply_adjudication","may_claim_mathematical_proof","may_promote_claim","whole_chapter_equivalence","decimal_precision_source_authored"):
        if rc.get(k) is not False: e.append(f"authority inflation: {k}")
    b=r.get("claim_boundary","")
    for t in ("exact four configured targets","30-decimal","scale-normalization","historical six-packet registry","MATHCERT route"):
        if t not in b: e.append(f"claim boundary lost: {t}")
    return e

def main():
    e=validation_errors()
    if e: print("\n".join(e),file=sys.stderr); return 1
    print("validated OTP-A Sphere Packing successor handoff candidate"); return 0

if __name__=="__main__": raise SystemExit(main())
