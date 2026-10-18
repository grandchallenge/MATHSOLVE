#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / ".gcl/worker_queue/ACTIVATION_RECEIPT.json"
SHA1 = re.compile(r"^[0-9a-f]{40}$")


def validate() -> list[str]:
    e: list[str] = []
    r = json.loads(RECEIPT.read_text(encoding="utf-8"))
    if r.get("record_type") != "GCL_WORKER_QUEUE_ACTIVATION_RECEIPT":
        e.append("receipt record type mismatch")
    if r.get("receipt_id") != "GCL-WORKER-QUEUE-ACTIVATION-001":
        e.append("receipt identity mismatch")
    if r.get("state") != "LIVE":
        e.append("recorded activation state mismatch")

    policy = r.get("protected_programme_policy", {})
    if policy.get("commit") != "0fd894c053922ec43b70878e0f02e8370690449a":
        e.append("Programme policy commit drift")
    if policy.get("policy_blob_sha1") != "6752e92d260d6a44f9e048c8400bddc0848d616d":
        e.append("Programme policy blob drift")

    impl = r.get("solve_implementation", {})
    if impl.get("pull_request") != 895 or impl.get("post_merge_controller_repair_pull_request") != 896:
        e.append("implementation PR identity drift")
    if impl.get("merge_commit") != "fcfc825371b415b76734bfcfbfd41ce4e175dcc3":
        e.append("implementation merge drift")
    if impl.get("protected_readback_commit") != "3b903ad23f0466026df60348b1e0fc7589e2202b":
        e.append("protected readback drift")
    blobs = impl.get("blobs", {})
    for key in ("config", "jobs", "worker_entrypoint", "worker_controller", "ghos_routing"):
        if not SHA1.fullmatch(str(blobs.get(key, ""))):
            e.append(f"invalid historical blob identity: {key}")

    pilot = r.get("pilot", {})
    if pilot.get("job_count") != 24:
        e.append("recorded pilot job count drift")
    if pilot.get("issue_range") != {"first": 842, "last": 865, "count": 24}:
        e.append("recorded pilot issue range drift")
    if pilot.get("live_state_counts") != {"available": 24, "reserved": 0, "returned": 0}:
        e.append("recorded activation state counts drift")
    if pilot.get("result_comment_count") != 0:
        e.append("activation receipt unexpectedly records mathematical returns")

    smoke = r.get("smoke_test", {})
    if smoke.get("claim_comment_id") != 5990656883 or smoke.get("release_comment_id") != 5990668757:
        e.append("smoke-test comment identity drift")
    if smoke.get("final_operational_state") != "AVAILABLE":
        e.append("recorded smoke test did not finish AVAILABLE")
    if smoke.get("mathematical_effect") is not False or smoke.get("certification_effect") is not False:
        e.append("smoke-test authority inflation")

    cohorts = r.get("blind_cohorts", [])
    if len(cohorts) != 8 or len({x.get("id") for x in cohorts}) != 8:
        e.append("recorded blind cohort set is invalid")
    for item in cohorts:
        if not SHA1.fullmatch(str(item.get("blob_sha1", ""))):
            e.append(f"invalid historical cohort blob: {item.get('id')}")

    boundary = r.get("blind_cohort_boundary", {})
    if boundary.get("synthesis_allowed") is not False:
        e.append("activation receipt records synthesis open")
    if boundary.get("cross_disclosure_before_closure") is not False:
        e.append("activation receipt records cross-disclosure open")
    if boundary.get("in_place_reclassification_authorized") is not False:
        e.append("activation receipt records in-place reclassification")

    authority = r.get("authority_effect", {})
    for key in (
        "worker_reservation_is_execution_authority",
        "project_or_labels_are_authority",
        "mathematical",
        "certification",
        "publication",
        "protected_bypass",
    ):
        if authority.get(key) is not False:
            e.append(f"authority inflation: {key}")
    return e


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print("FAIL:", error)
        return 1
    print("PASS: GCL worker queue activation receipt is internally consistent historical evidence")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
