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

EXPECTED_REPOSITORY_MODES = {
    "grandchallenge/MATHSOLVE": "reservation_controlled",
    "grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS": "direct_editorial",
    "grandchallenge/COMPUTATIONAL-DIFFICULTY-ATLAS": "direct_editorial",
    "grandchallenge/MATH-PROGRAMME": "direct_editorial",
}
DIRECT_LABEL = "gcl-pickup:direct-editorial"


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
    if data.get("project", {}).get("cross_repository_discovery_authority") is not True:
        errors.append("cross-repository Project discovery contract missing")

    if data.get("repository_pickup_modes") != EXPECTED_REPOSITORY_MODES:
        errors.append("repository pickup-mode map drift")

    modes = data.get("pickup_modes", {})
    reservation = modes.get("reservation_controlled", {})
    direct = modes.get("direct_editorial", {})
    if reservation.get("claim_command") != "/claim" or reservation.get("release_command") != "/release":
        errors.append("reservation command contract drift")
    if reservation.get("controller_response_protocol") != "GCL-WORKER-RESERVATION/1":
        errors.append("reservation protocol drift")
    if reservation.get("return_protocol") != "GCL-CONTRIBUTION-RESULT/1":
        errors.append("reservation return protocol drift")
    if reservation.get("execute_before_reservation_confirmation") is not False:
        errors.append("reservation mode permits execution before confirmation")
    if reservation.get("forbidden_label") != DIRECT_LABEL:
        errors.append("reservation/direct pickup boundary label drift")

    if direct.get("required_label") != DIRECT_LABEL:
        errors.append("direct pickup label drift")
    if direct.get("claim_command") is not None or direct.get("reservation_controller") is not None:
        errors.append("direct editorial mode incorrectly uses reservation controller")
    if direct.get("instructions_source") != "bound issue" or direct.get("return_target") != "same bound issue":
        errors.append("direct editorial issue-bound execution/return drift")

    if data.get("commands") != {"claim": "/claim", "release": "/release"}:
        errors.append("legacy command compatibility drift")
    if data.get("commands_apply_to") != "reservation_controlled":
        errors.append("legacy commands are not scoped to reservation-controlled mode")
    if data.get("controller_response_protocol") != "GCL-WORKER-RESERVATION/1":
        errors.append("legacy reservation protocol drift")
    if data.get("return_protocol") != "GCL-CONTRIBUTION-RESULT/1":
        errors.append("legacy return protocol drift")
    if data.get("legacy_top_level_protocol_fields_apply_to") != "reservation_controlled":
        errors.append("legacy top-level protocol scope missing")

    fallbacks = {x.get("repository"): x for x in data.get("fallbacks", [])}
    if set(fallbacks) != set(EXPECTED_REPOSITORY_MODES):
        errors.append("fallback repository set drift")
    for repo, mode in EXPECTED_REPOSITORY_MODES.items():
        row = fallbacks.get(repo, {})
        if row.get("pickup_mode") != mode:
            errors.append(f"fallback pickup mode drift: {repo}")
        url = str(row.get("issue_query_url") or "")
        if repo not in url or "gcl-state" not in url:
            errors.append(f"fallback query malformed: {repo}")
        if mode == "direct_editorial" and "gcl-pickup" not in url:
            errors.append(f"direct fallback query lacks pickup label: {repo}")

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
        "gcl-pickup:direct-editorial",
        "do not post",
        "/claim",
        "GCL-WORKER-RESERVATION/1",
        "GCL-CONTRIBUTION-RESULT/1",
        ".well-known/gcl-worker-queue.json",
        "grandchallenge/COMPUTATIONAL-DIFFICULTY-ATLAS",
        "grandchallenge/MATH-PROGRAMME",
        "authenticated GitHub identity",
        "stop and report a queue-integrity blocker",
        "do not default an unknown job to `/claim`",
    ):
        if needle not in workers:
            errors.append(f"WORKERS.md missing {needle!r}")

    if "If the issue does **not** carry `gcl-pickup:direct-editorial`, use the" in workers:
        errors.append("WORKERS.md defaults unknown/non-direct jobs to MATHSOLVE reservation mode")

    handoff = HANDOFF.read_text(encoding="utf-8")
    for needle in (
        "Reservation-controlled mode",
        "Direct-editorial mode",
        "gcl-pickup:direct-editorial",
        "Do not post",
        "/claim",
        "grandchallenge/COMPUTATIONAL-DIFFICULTY-ATLAS",
    ):
        if needle not in handoff:
            errors.append(f"full worker protocol missing {needle!r}")

    agents = AGENTS.read_text(encoding="utf-8")
    for needle in ("WORKERS.md", "external or zero-context agent", "immutable launch artifact"):
        if needle not in agents:
            errors.append(f"AGENTS.md missing worker bootstrap anchor: {needle}")

    readme = README.read_text(encoding="utf-8")
    if "WORKERS.md" not in readme or "GCL Worker Queue" not in readme:
        errors.append("README.md does not expose external worker bootstrap")

    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    if config.get("worker_discovery_primary") != "github_project":
        errors.append("queue primary discovery surface drift")
    if config.get("project_url") != data["project"]["url"]:
        errors.append("queue config / bootstrap Project mismatch")
    if config.get("repository_pickup_modes") != EXPECTED_REPOSITORY_MODES:
        errors.append("queue config pickup-mode map drift")
    if config.get("labels", {}).get("pickup_direct_editorial") != DIRECT_LABEL:
        errors.append("queue config direct pickup label drift")

    project = json.loads(PROJECT.read_text(encoding="utf-8"))
    if project.get("project", {}).get("number") != data["project"]["number"]:
        errors.append("Project binding / bootstrap number mismatch")
    supported = {
        repo: row.get("pickup_mode")
        for repo, row in project.get("supported_repositories", {}).items()
    }
    if supported != EXPECTED_REPOSITORY_MODES:
        errors.append("Project binding repository pickup-mode map drift")
    for repo, mode in EXPECTED_REPOSITORY_MODES.items():
        row = project.get("supported_repositories", {}).get(repo, {})
        if mode == "direct_editorial" and row.get("required_pickup_label") != DIRECT_LABEL:
            errors.append(f"Project binding direct label missing: {repo}")

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
    print("PASS: zero-context worker bootstrap is cross-repository, mode-aware, and authority-neutral")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
