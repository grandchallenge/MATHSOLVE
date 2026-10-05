#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / ".gcl/worker_queue/CONFIG.json"
REGISTRY = ROOT / ".gcl/worker_queue/JOBS.json"
WORKFLOW = ROOT / ".github/workflows/gcl-worker-queue.yml"
ROUTING = ROOT / ".ghos-routing/workflows.json"
ENTRYPOINT = ROOT / "handoffs/GCL-WORKER-QUEUE.md"
INTAKE = ROOT / "ci/ns_ci_github_contribution_intake.py"
INTAKE_WORKFLOW = ROOT / ".github/workflows/ns-ci-independent-contribution-intake.yml"
PROGRAMME_COMMIT = "0fd894c053922ec43b70878e0f02e8370690449a"
TASK_COMMIT = "13f8364d0dd052bf0cd9f6a9f66dc135d770529f"
PROBLEMS = ["593", "595", "241", "470", "1052", "99", "101", "138"]
LANES = ["R1", "S1", "A1"]


def readj(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def validate() -> list[str]:
    errors: list[str] = []
    config = readj(CONFIG)
    registry = readj(REGISTRY)

    if config.get("policy_id") != "GCL-WORKER-QUEUE-001":
        errors.append("queue policy id mismatch")
    if config.get("programme_policy_commit") != PROGRAMME_COMMIT:
        errors.append("Programme policy commit drift")
    for key in ("reservation_is_execution_authority", "project_or_labels_are_authority", "mathematical_effect", "certification_effect"):
        if config.get(key) is not False:
            errors.append(f"authority boundary widened: {key}")

    jobs = registry.get("jobs", [])
    if len(jobs) != 24:
        errors.append("expected exactly 24 ERDOS pilot jobs")
    expected = {f"ERDOS-{p}-{lane}-IA-001" for p in PROBLEMS for lane in LANES}
    if {j.get("dispatch_id") for j in jobs} != expected:
        errors.append("queue dispatch identity set drift")
    if {j.get("issue_number") for j in jobs} != set(range(842, 866)):
        errors.append("queue issue binding set drift")

    for job in jobs:
        did = str(job.get("dispatch_id"))
        if job.get("self_claimable") is not True:
            errors.append(f"{did}: not self-claimable")
        if job.get("reservation_ttl_minutes") != 65:
            errors.append(f"{did}: reservation TTL drift")
        if job.get("collaboration_mode") != "STAGED_DISCLOSURE":
            errors.append(f"{did}: collaboration mode drift")
        if job.get("visibility_phase") != "BLIND_COLLECTION" or job.get("sibling_use_policy") != "FORBIDDEN":
            errors.append(f"{did}: blind pickup boundary drift")
        if job.get("task_commit") != TASK_COMMIT:
            errors.append(f"{did}: immutable task commit drift")

        dp = ROOT / str(job.get("dispatch_path", ""))
        if not dp.is_file():
            errors.append(f"{did}: protected dispatch missing")
            continue
        d = readj(dp)
        if d.get("dispatch_id") != did:
            errors.append(f"{did}: dispatch identity mismatch")
        if d.get("github_issue_number") != job.get("issue_number"):
            errors.append(f"{did}: issue binding mismatch")
        if d.get("dispatch_status") != "READY_FOR_GITHUB_COMMENT":
            errors.append(f"{did}: protected dispatch not ready")
        if d.get("lease_state") != "ACTIVE":
            errors.append(f"{did}: protected lease not active")
        if d.get("canonical_mutation_authorized") is not False or d.get("certification_authorized") is not False:
            errors.append(f"{did}: authority inflation")
        if d.get("concurrency_mode") != "independent_blind":
            errors.append(f"{did}: historical blind dispatch reclassified")
        if d.get("blind_cohort_id") != job.get("cohort_id"):
            errors.append(f"{did}: cohort identity mismatch")
        task = ROOT / str(d.get("task_path", ""))
        if not task.is_file():
            errors.append(f"{did}: immutable task missing")
        elif hashlib.sha256(task.read_text(encoding="utf-8").encode("utf-8")).hexdigest() != d.get("task_sha256"):
            errors.append(f"{did}: immutable task digest mismatch")

    for p in PROBLEMS:
        co = readj(ROOT / f"contributions/ERDOS-OPEN-001/RECON_TRANCHE_001/cohorts/ERDOS-{p}-BLIND-COHORT-001.json")
        if co.get("state") != "OPEN_AWAITING_RESULTS":
            errors.append(f"ERDOS-{p}: blind cohort state changed")
        if co.get("synthesis_allowed") is not False or co.get("cross_disclosure_before_closure") is not False:
            errors.append(f"ERDOS-{p}: disclosure/synthesis opened in place")

    workflow = WORKFLOW.read_text(encoding="utf-8")
    for needle in (
        "issue_comment:",
        "schedule:",
        "contents: read",
        "issues: write",
        "gcl-worker-reservation-${{ github.event.issue.number }}",
        "cancel-in-progress: false",
        "ref: main",
        "ci/gcl_worker_queue.py",
        "Reconcile expired reservations",
    ):
        if needle not in workflow:
            errors.append(f"worker workflow missing {needle!r}")

    routes = readj(ROUTING)
    route = [x for x in routes.get("workflows", []) if x.get("path") == ".github/workflows/gcl-worker-queue.yml"]
    if len(route) != 1:
        errors.append("worker queue workflow missing from GH-OS routing")
    else:
        r = route[0]
        if r.get("topology") != "PERSISTENT_CONTROLLER_REQUIRED" or r.get("controller_id") != "GITHUB_ACTIONS":
            errors.append("worker queue persistent-controller routing mismatch")
        features = set(r.get("observed_features", []))
        for required in {"OPAQUE_EXECUTION", "SCHEDULED", "SECRET_CREDENTIAL", "WRITE_CAPABLE"}:
            if required not in features:
                errors.append(f"worker queue routing missing {required}")

    intake = INTAKE.read_text(encoding="utf-8")
    for needle in ("queue-managed result has no active worker reservation", "authenticated result author does not match active worker reservation"):
        if needle not in intake:
            errors.append(f"intake missing reservation-owner control: {needle}")
    intake_workflow = INTAKE_WORKFLOW.read_text(encoding="utf-8")
    if '--comments "$RUNNER_TEMP/issue-comments.json"' not in intake_workflow:
        errors.append("intake workflow does not supply issue comment history")

    entry = ENTRYPOINT.read_text(encoding="utf-8")
    for needle in ("/claim", "/release", "No bootstrap prompt must be copied", "sibling use is `FORBIDDEN`"):
        if needle not in entry:
            errors.append(f"worker entrypoint missing {needle!r}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for e in errors:
            print("FAIL:", e)
        return 1
    print("PASS: GCL worker queue policy, ERDOS pilot bindings, controller routing, and blind-collaboration boundary agree")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
