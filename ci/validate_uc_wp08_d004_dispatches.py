#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "contributions/UC-001/WP08_D004_INCIDENCE_INTERFACE"
EXPECTED = {
    "UC-WP08-D004-WP01-IA-001": (721, "INDEPENDENT-AGENT-UC401", "UC-WP08-D004-WP01", "independent_blind"),
    "UC-WP08-D004-WP02-IA-001": (722, "INDEPENDENT-AGENT-UC402", "UC-WP08-D004-WP02", "independent_blind"),
    "UC-WP08-D004-WP03-IA-001": (723, "INDEPENDENT-AGENT-UC403", "UC-WP08-D004-WP03", "independent_blind"),
    "UC-WP08-D004-WP04-IA-001": (724, "INDEPENDENT-AGENT-UC404", "UC-WP08-D004-WP04", "independent_blind"),
    "UC-WP08-D004-WP05-IA-001": (725, "INDEPENDENT-AGENT-UC405", "UC-WP08-D004-WP05", "adversarial_replay"),
}
COHORT = "UC-WP08-D004-BLIND-COHORT-001"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fail(msg: str) -> None:
    raise ValueError(msg)


def main() -> int:
    errors: list[str] = []
    for dispatch_id, (issue, agent, assignment, mode) in EXPECTED.items():
        try:
            p = BASE / "dispatches" / f"{dispatch_id}.json"
            if not p.is_file():
                fail(f"{dispatch_id}: missing dispatch")
            d = json.loads(p.read_text())
            expected = {
                "schema_version": "1.0.0",
                "record_type": "GCL_EXTERNAL_DISPATCH",
                "dispatch_id": dispatch_id,
                "campaign": "UC-001",
                "assignment_id": assignment,
                "agent_ref": agent,
                "concurrency_mode": mode,
                "return_protocol": "GCL-CONTRIBUTION-RESULT/1",
                "github_issue_number": issue,
                "github_issue_url": f"https://github.com/grandchallenge/MATHSOLVE/issues/{issue}",
                "canonical_mutation_authorized": False,
                "protected_lease_required": True,
            }
            for key, value in expected.items():
                if d.get(key) != value:
                    fail(f"{dispatch_id}: {key} drift")
            if d.get("dispatch_status") not in {"PENDING_GITHUB_ISSUE_BINDING", "READY_FOR_GITHUB_COMMENT"}:
                fail(f"{dispatch_id}: invalid dispatch_status")
            if mode == "independent_blind":
                if d.get("blind_cohort_id") != COHORT:
                    fail(f"{dispatch_id}: blind cohort mismatch")
            elif d.get("blind_cohort_id") is not None:
                fail(f"{dispatch_id}: adversarial lane may not join blind cohort")
            for path_key, sha_key in (
                ("bootstrap_path", "bootstrap_sha256"),
                ("task_path", "task_sha256"),
            ):
                path = ROOT / d[path_key]
                if not path.is_file():
                    fail(f"{dispatch_id}: missing {path_key}")
                if sha256(path) != d[sha_key]:
                    fail(f"{dispatch_id}: {sha_key} mismatch")
            task_commit=d.get("task_commit")
            if not isinstance(task_commit,str) or not re.fullmatch(r"[0-9a-f]{40}",task_commit):
                fail(f"{dispatch_id}: invalid task_commit")
            if d.get("task_url") != f"https://github.com/grandchallenge/MATHSOLVE/blob/{task_commit}/{d['task_path']}":
                fail(f"{dispatch_id}: immutable task URL mismatch")
            if d.get("source_handoff_commit_sha") != task_commit:
                fail(f"{dispatch_id}: source handoff commit must equal immutable task commit")
            if d.get("source_handoff_sha256") != d.get("task_sha256"):
                fail(f"{dispatch_id}: source handoff/task digest mismatch")
        except Exception as exc:
            errors.append(str(exc))

    registry_path = BASE / "DISPATCH_REGISTRY.json"
    if not registry_path.is_file():
        errors.append("missing dispatch registry")
    else:
        registry = json.loads(registry_path.read_text())
        statuses = [
            json.loads((BASE / "dispatches" / f"{dispatch_id}.json").read_text()).get("dispatch_status")
            for dispatch_id in EXPECTED
        ]
        if all(status == "READY_FOR_GITHUB_COMMENT" for status in statuses):
            if registry.get("state") != "ACTIVE_EXTERNAL_EVIDENCE":
                errors.append("active dispatches require ACTIVE_EXTERNAL_EVIDENCE registry state")
            receipt_path = BASE / "ACTIVATION_RECEIPT.json"
            if not receipt_path.is_file():
                errors.append("active dispatches require activation receipt")
            else:
                receipt = json.loads(receipt_path.read_text())
                if receipt.get("protected_task_packet_merge_commit") != "7ce9e3b93c92510d574dd6ff9d31d6716915f8fc":
                    errors.append("activation receipt Solve packet identity drift")
                if receipt.get("protected_programme_cei_commit") != "c70bf336ec598bb8654cc465306c6cf3a871341e":
                    errors.append("activation receipt Programme CEI identity drift")
                if receipt.get("all_issue_bodies_verified_byte_equal") is not True:
                    errors.append("activation receipt lacks exact issue-byte verification")
                bindings = {
                    item.get("dispatch_id"): item
                    for item in receipt.get("issue_bindings", [])
                    if isinstance(item, dict)
                }
                for dispatch_id, (issue, _, _, _) in EXPECTED.items():
                    d = json.loads((BASE / "dispatches" / f"{dispatch_id}.json").read_text())
                    item = bindings.get(dispatch_id)
                    if item is None:
                        errors.append(f"{dispatch_id}: activation binding missing")
                        continue
                    if item.get("github_issue_number") != issue:
                        errors.append(f"{dispatch_id}: activation issue number drift")
                    if item.get("protected_bootstrap_sha256") != d.get("bootstrap_sha256"):
                        errors.append(f"{dispatch_id}: activation bootstrap digest drift")
                    if item.get("observed_issue_body_sha256") != d.get("bootstrap_sha256"):
                        errors.append(f"{dispatch_id}: observed issue-body digest drift")
                    if item.get("issue_body_byte_equal_to_protected_bootstrap") is not True:
                        errors.append(f"{dispatch_id}: issue-byte equality not established")

    cohort_path=BASE/"cohorts"/f"{COHORT}.json"
    if not cohort_path.is_file():
        errors.append("missing blind cohort record")
    else:
        c=json.loads(cohort_path.read_text())
        members=[f"UC-WP08-D004-WP0{i}-IA-001" for i in range(1,5)]
        if c.get("dispatch_ids") != members:
            errors.append("blind cohort membership drift")
        if c.get("cross_disclosure_before_closure") is not False:
            errors.append("blind cohort cross-disclosure must be false")
        if c.get("synthesis_allowed") is not False:
            errors.append("blind cohort synthesis must remain false before closure")
        if c.get("state") not in {"PREPARED_PENDING_GITHUB_ISSUE_BINDING", "OPEN_AWAITING_RESULTS"}:
            errors.append("blind cohort state drift")

    if errors:
        for e in errors:
            print(e,file=sys.stderr)
        return 1
    print("UC WP08-D004 dispatch identities, immutable tasks, blind cohort, and claim boundaries are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
