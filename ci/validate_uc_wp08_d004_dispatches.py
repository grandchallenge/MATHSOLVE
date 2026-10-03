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

    if errors:
        for e in errors:
            print(e,file=sys.stderr)
        return 1
    print("UC WP08-D004 dispatch identities, immutable tasks, blind cohort, and claim boundaries are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
