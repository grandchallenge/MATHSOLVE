#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / ".gcl/worker_queue"
RECEIPT = BASE / "ACTIVATION_RECEIPT.json"


def readj(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def validate() -> list[str]:
    e: list[str] = []
    r = readj(RECEIPT)

    if r.get("record_type") != "GCL_WORKER_QUEUE_ACTIVATION_RECEIPT":
        e.append("receipt record type mismatch")
    if r.get("receipt_id") != "GCL-WORKER-QUEUE-ACTIVATION-001":
        e.append("receipt identity mismatch")
    if r.get("state") != "LIVE":
        e.append("queue activation is not LIVE")

    policy = r.get("protected_programme_policy", {})
    if policy.get("commit") != "0fd894c053922ec43b70878e0f02e8370690449a":
        e.append("Programme policy commit drift")
    if policy.get("policy_blob_sha1") != "6752e92d260d6a44f9e048c8400bddc0848d616d":
        e.append("Programme policy blob drift")

    impl = r.get("solve_implementation", {})
    if impl.get("pull_request") != 895:
        e.append("implementation PR drift")
    if impl.get("merge_commit") != "fcfc825371b415b76734bfcfbfd41ce4e175dcc3":
        e.append("implementation merge drift")
    if impl.get("post_merge_controller_repair_pull_request") != 896:
        e.append("controller repair PR drift")
    if impl.get("protected_readback_commit") != "3b903ad23f0466026df60348b1e0fc7589e2202b":
        e.append("protected readback drift")

    expected_files = {
        "config": ROOT / ".gcl/worker_queue/CONFIG.json",
        "jobs": ROOT / ".gcl/worker_queue/JOBS.json",
        "worker_entrypoint": ROOT / "handoffs/GCL-WORKER-QUEUE.md",
        "worker_controller": ROOT / ".github/workflows/gcl-worker-queue.yml",
        "ghos_routing": ROOT / ".ghos-routing/workflows.json",
    }
    blobs = impl.get("blobs", {})
    for key, path in expected_files.items():
        if not path.is_file():
            e.append(f"missing protected file: {path.as_posix()}")
        elif blob_sha1(path) != blobs.get(key):
            e.append(f"protected blob drift: {key}")

    pilot = r.get("pilot", {})
    if pilot.get("job_count") != 24:
        e.append("pilot job count drift")
    if pilot.get("issue_range") != {"first": 842, "last": 865, "count": 24}:
        e.append("pilot issue range drift")
    if pilot.get("live_state_counts") != {"available": 24, "reserved": 0, "returned": 0}:
        e.append("recorded live state counts drift")
    if pilot.get("result_comment_count") != 0:
        e.append("activation receipt unexpectedly records mathematical returns")

    jobs = readj(ROOT / ".gcl/worker_queue/JOBS.json").get("jobs", [])
    if len(jobs) != 24:
        e.append("protected queue registry no longer has 24 jobs")
    if {j.get("issue_number") for j in jobs} != set(range(842, 866)):
        e.append("protected queue issue set drift")
    for j in jobs:
        did = str(j.get("dispatch_id", ""))
        if j.get("self_claimable") is not True:
            e.append(f"{did}: self-claim disabled")
        if j.get("collaboration_mode") != "STAGED_DISCLOSURE":
            e.append(f"{did}: collaboration mode drift")
        if j.get("visibility_phase") != "BLIND_COLLECTION":
            e.append(f"{did}: visibility phase drift")
        if j.get("sibling_use_policy") != "FORBIDDEN":
            e.append(f"{did}: sibling-use boundary opened")

    smoke = r.get("smoke_test", {})
    if smoke.get("claim_comment_id") != 5990656883 or smoke.get("release_comment_id") != 5990668757:
        e.append("smoke-test comment identity drift")
    if smoke.get("final_operational_state") != "AVAILABLE":
        e.append("smoke test did not finish AVAILABLE")
    if smoke.get("mathematical_effect") is not False or smoke.get("certification_effect") is not False:
        e.append("smoke test authority inflation")

    cohorts = r.get("blind_cohorts", [])
    if len(cohorts) != 8:
        e.append("expected eight blind cohorts")
    for item in cohorts:
        cid = item.get("id")
        path = ROOT / "contributions/ERDOS-OPEN-001/RECON_TRANCHE_001/cohorts" / f"{cid}.json"
        if not path.is_file():
            e.append(f"{cid}: missing cohort file")
            continue
        if blob_sha1(path) != item.get("blob_sha1"):
            e.append(f"{cid}: cohort blob drift")
        co = readj(path)
        if co.get("state") != "OPEN_AWAITING_RESULTS":
            e.append(f"{cid}: cohort state changed")
        if co.get("synthesis_allowed") is not False:
            e.append(f"{cid}: synthesis opened")
        if co.get("cross_disclosure_before_closure") is not False:
            e.append(f"{cid}: cross-disclosure opened")

    authority = r.get("authority_effect", {})
    for key in ("worker_reservation_is_execution_authority", "project_or_labels_are_authority", "mathematical", "certification", "publication", "protected_bypass"):
        if authority.get(key) is not False:
            e.append(f"authority inflation: {key}")

    return e


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print("FAIL:", error)
        return 1
    print("PASS: GCL worker queue activation receipt matches protected repository state and blind-cohort boundary")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
