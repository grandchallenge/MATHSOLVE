#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / ".gcl/worker_queue/PROJECT.json"
BOOTSTRAP = ROOT / ".well-known/gcl-worker-queue.json"

EXPECTED_REPOSITORY_MODES = {
    "grandchallenge/MATHSOLVE": "reservation_controlled",
    "grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS": "direct_editorial",
    "grandchallenge/COMPUTATIONAL-DIFFICULTY-ATLAS": "direct_editorial",
}
DIRECT_LABEL = "gcl-pickup:direct-editorial"


def validate() -> list[str]:
    e: list[str] = []
    data = json.loads(PROJECT.read_text(encoding="utf-8"))
    bootstrap = json.loads(BOOTSTRAP.read_text(encoding="utf-8"))

    if data.get("record_type") != "GCL_WORKER_QUEUE_PROJECT_BINDING":
        e.append("project binding record type mismatch")
    if data.get("binding_id") != "GCL-WORKER-QUEUE-PROJECT-001":
        e.append("project binding identity mismatch")

    p = data.get("project", {})
    if p.get("number") != 2 or p.get("id") != "PVT_kwDOB9Ao_c4Blwur":
        e.append("GitHub Project identity mismatch")
    if p.get("visibility") != "PUBLIC" or p.get("worker_facing_primary") is not True:
        e.append("worker-facing Project is not public/primary")
    if p.get("authority") is not False:
        e.append("Project improperly treated as authority")

    supported = {
        repo: row.get("pickup_mode")
        for repo, row in data.get("supported_repositories", {}).items()
    }
    if supported != EXPECTED_REPOSITORY_MODES:
        e.append("Project supported-repository pickup modes drift")
    if bootstrap.get("repository_pickup_modes") != EXPECTED_REPOSITORY_MODES:
        e.append("machine bootstrap repository pickup modes drift")
    if supported != bootstrap.get("repository_pickup_modes"):
        e.append("Project/bootstrap repository pickup-mode disagreement")

    for repo, mode in EXPECTED_REPOSITORY_MODES.items():
        row = data.get("supported_repositories", {}).get(repo, {})
        if mode == "direct_editorial" and row.get("required_pickup_label") != DIRECT_LABEL:
            e.append(f"direct-editorial pickup label missing for {repo}")

    fields = data.get("issue_fields", {})
    expected_ids = {
        "state": 47953501,
        "campaign": 47953502,
        "role": 47953503,
        "collaboration": 47953504,
        "phase": 47953505,
        "cohort": 47953514,
        "timebox": 47953515,
        "worker": 47953516,
        "reservation_expires": 47953521,
    }
    for key, expected in expected_ids.items():
        if fields.get(key, {}).get("rest_id") != expected:
            e.append(f"issue field binding drift: {key}")

    status_field = data.get("project_status_field", {})
    if status_field.get("field_id") != "PVTSSF_lADOB9Ao_c4BlwurzhkcRPQ":
        e.append("Project Status field id drift")
    if status_field.get("options") != {
        "Todo": "f75ad846",
        "In Progress": "47fc9ee4",
        "Done": "98236657",
    }:
        e.append("Project Status option binding drift")

    views = data.get("views", {})
    required = {
        "all_jobs": "",
        "available": 'is:open "GCL State":AVAILABLE',
        "independent": 'is:open "GCL Phase":INDEPENDENT',
        "cooperative": 'is:open "GCL Collaboration":COOPERATIVE',
        "returned": '"GCL State":RETURNED',
        "erdos_open": 'is:open "GCL Campaign":"ERDOS-OPEN-RECON"',
    }
    for key, filt in required.items():
        if views.get(key, {}).get("filter") != filt:
            e.append(f"Project view binding drift: {key}")

    authority = data.get("authority_effect", {})
    for key in (
        "project_is_execution_authority",
        "issue_fields_are_execution_authority",
        "mathematical",
        "certification",
    ):
        if authority.get(key) is not False:
            e.append(f"Project authority inflation: {key}")

    worker = (ROOT / ".github/workflows/gcl-worker-queue.yml").read_text(encoding="utf-8")
    intake = (ROOT / ".github/workflows/ns-ci-independent-contribution-intake.yml").read_text(encoding="utf-8")
    if "gcl_worker_queue_projection.py" not in worker:
        e.append("reservation controller does not synchronize issue fields")
    if "gcl_worker_queue_projection.py" not in intake:
        e.append("RESULT/1 intake does not synchronize issue fields")

    return e


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print("FAIL:", error)
        return 1
    print("PASS: Worker Queue Project binding, repository pickup modes, and issue-field synchronization agree")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
