#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOTSTRAP = ROOT / ".well-known/gcl-worker-queue.json"
WORKERS = ROOT / "WORKERS.md"
AGENTS = ROOT / "AGENTS.md"
README = ROOT / "README.md"
HANDOFF = ROOT / "handoffs/GCL-WORKER-QUEUE.md"
CONFIG = ROOT / ".gcl/worker_queue/CONFIG.json"
PROJECT = ROOT / ".gcl/worker_queue/PROJECT.json"


def validate() -> list[str]:
    errors: list[str] = []
    data = json.loads(BOOTSTRAP.read_text(encoding="utf-8"))

    if data.get("protocol") != "GCL-WORKER-QUEUE/1":
        errors.append("worker bootstrap protocol mismatch")
    if data.get("repository") != "grandchallenge/MATHSOLVE":
        errors.append("worker bootstrap repository mismatch")
    if data.get("instructions_url") != "https://github.com/grandchallenge/MATHSOLVE/blob/main/WORKERS.md":
        errors.append("worker instructions URL drift")
    if data.get("project", {}).get("number") != 2:
        errors.append("worker Project number drift")
    if data.get("project", {}).get("url") != "https://github.com/orgs/grandchallenge/projects/2":
        errors.append("worker Project URL drift")
    if data.get("commands") != {"claim": "/claim", "release": "/release"}:
        errors.append("worker command contract drift")
    if data.get("controller_response_protocol") != "GCL-WORKER-RESERVATION/1":
        errors.append("reservation protocol drift")
    if data.get("return_protocol") != "GCL-CONTRIBUTION-RESULT/1":
        errors.append("return protocol drift")

    authority = data.get("authority", {})
    for key in (
        "project_is_execution_authority",
        "issue_fields_are_execution_authority",
        "reservation_is_execution_authority",
        "mathematical_effect",
        "certification_effect",
    ):
        if authority.get(key) is not False:
            errors.append(f"worker bootstrap authority inflation: {key}")

    workers = WORKERS.read_text(encoding="utf-8")
    for needle in (
        "https://github.com/orgs/grandchallenge/projects/2",
        "/claim",
        "/release",
        "GCL-WORKER-RESERVATION/1",
        "GCL-CONTRIBUTION-RESULT/1",
        ".well-known/gcl-worker-queue.json",
        "sibling_use_policy",
        "The protected dispatch and protected execution lease remain authoritative",
    ):
        if needle not in workers:
            errors.append(f"WORKERS.md missing {needle!r}")

    agents = AGENTS.read_text(encoding="utf-8")
    if "WORKERS.md" not in agents or "do not already hold a bounded assignment" not in agents:
        errors.append("AGENTS.md does not expose zero-context worker bootstrap")

    readme = README.read_text(encoding="utf-8")
    if "WORKERS.md" not in readme or "GCL Worker Queue" not in readme:
        errors.append("README.md does not expose external worker bootstrap")

    if not HANDOFF.is_file():
        errors.append("full worker protocol missing")

    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    if config.get("worker_discovery_primary") != "github_project":
        errors.append("queue primary discovery surface drift")
    if config.get("project_url") != data["project"]["url"]:
        errors.append("queue config / bootstrap Project mismatch")

    project = json.loads(PROJECT.read_text(encoding="utf-8"))
    if project.get("project", {}).get("number") != data["project"]["number"]:
        errors.append("Project binding / bootstrap number mismatch")
    bootstrap = project.get("bootstrap", {})
    if bootstrap.get("instructions_path") != "WORKERS.md":
        errors.append("Project binding lacks WORKERS.md bootstrap")
    if bootstrap.get("machine_path") != ".well-known/gcl-worker-queue.json":
        errors.append("Project binding lacks machine bootstrap")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print("FAIL:", error)
        return 1
    print("PASS: zero-context external-worker bootstrap is durable and authority-neutral")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
