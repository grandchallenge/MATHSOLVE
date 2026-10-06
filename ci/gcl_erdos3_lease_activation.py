from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BASE = Path("work_packages/GCL_ERDOS3")
ACTIVATION_MARKER = "GCL-LEASE-ACTIVATION/1"
RESULT_MARKER = "GCL-CONTRIBUTION-RESULT/1"


class ActivationError(ValueError):
    pass


def git_blob_sha1_text(text: str) -> str:
    data = text.encode("utf-8")
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_activation(body: Any) -> dict[str, str] | None:
    if not isinstance(body, str) or not body.startswith(ACTIVATION_MARKER + "\n"):
        return None
    lines = body.splitlines()
    keys = ("dispatch_id", "assignment", "lease_epoch", "lease_duration_minutes", "agent_max_execution_minutes")
    if len(lines) != 1 + len(keys):
        raise ActivationError("activation marker has unexpected shape")
    out: dict[str, str] = {}
    for i, key in enumerate(keys, start=1):
        prefix = key + ": "
        if not lines[i].startswith(prefix):
            raise ActivationError(f"activation marker expected field {key}")
        value = lines[i][len(prefix):].strip()
        if not value:
            raise ActivationError(f"activation marker field {key} is empty")
        out[key] = value
    return out


def marker_body(dispatch: dict[str, Any]) -> str:
    return "\n".join([
        ACTIVATION_MARKER,
        f"dispatch_id: {dispatch['dispatch_id']}",
        f"assignment: {dispatch['assignment_id']}",
        f"lease_epoch: {dispatch['lease_epoch']}",
        "lease_duration_minutes: 25",
        "agent_max_execution_minutes: 24",
    ])


def plan_activation(
    root: Path,
    issue: dict[str, Any],
    comments: list[dict[str, Any]],
) -> dict[str, Any]:
    campaign = load_json(root / BASE / "CAMPAIGN.json")
    active = campaign.get("active_dispatches", {})
    if set(active) != {"E3-V03"}:
        return {"activate": False, "reason": "NO_SINGLE_ACTIVE_E3_V03_DISPATCH"}

    row = active["E3-V03"]
    dispatch_id = row.get("dispatch_id")
    if not isinstance(dispatch_id, str):
        raise ActivationError("active E3-V03 lacks dispatch_id")
    dispatch_path = root / BASE / "dispatches" / f"{dispatch_id}.json"
    if not dispatch_path.is_file():
        raise ActivationError("active dispatch record missing")
    dispatch = load_json(dispatch_path)

    if dispatch.get("state") != "DISPATCHED__AWAITING_RETURN":
        raise ActivationError("protected dispatch is not awaiting return")
    if dispatch.get("dispatch_status") != "READY_FOR_GITHUB_COMMENT":
        raise ActivationError("protected dispatch is not intake-ready")
    if dispatch.get("lease_policy_id") != "GCL-IA-LEASE-25M-24M-001":
        raise ActivationError("protected dispatch lease policy drift")
    if dispatch.get("lease_clock_source") != "GITHUB_ACTIVATION_COMMENT":
        raise ActivationError("protected dispatch is not marker-clocked")
    if dispatch.get("lease_duration_minutes") != 25 or dispatch.get("agent_max_execution_minutes") != 24:
        raise ActivationError("protected dispatch lease duration/cap drift")

    issue_number = issue.get("number")
    if issue_number != dispatch.get("github_issue_number"):
        raise ActivationError("canonical issue number drift")
    issue_state = issue.get("state")
    if issue_state == "closed":
        return {
            "activate": False,
            "reason": "CANONICAL_ISSUE_CLOSED",
            "dispatch_id": dispatch_id,
            "issue_number": issue_number,
            "lease_epoch": dispatch.get("lease_epoch"),
        }
    if issue_state != "open":
        raise ActivationError("canonical issue state is invalid")

    bootstrap_path = root / str(dispatch.get("bootstrap_path", ""))
    if not bootstrap_path.is_file():
        raise ActivationError("protected bootstrap missing")
    bootstrap = bootstrap_path.read_text(encoding="utf-8")
    if git_blob_sha1_text(bootstrap) != dispatch.get("bootstrap_blob_sha1"):
        raise ActivationError("protected bootstrap blob mismatch")
    if issue.get("body") != bootstrap:
        raise ActivationError("canonical issue body differs from protected bootstrap")

    expected_title = dispatch.get("github_issue_title")
    staging_title = dispatch.get("github_issue_staging_title")
    if not isinstance(expected_title, str) or not isinstance(staging_title, str):
        raise ActivationError("dispatch lacks active/staging title bindings")

    matching: list[dict[str, Any]] = []
    result_before_activation = False
    for row_comment in comments:
        body = row_comment.get("body")
        parsed = parse_activation(body)
        if parsed is not None and (
            parsed.get("dispatch_id") == dispatch.get("dispatch_id")
            and parsed.get("assignment") == dispatch.get("assignment_id")
            and parsed.get("lease_epoch") == str(dispatch.get("lease_epoch"))
        ):
            matching.append(row_comment)
        if isinstance(body, str) and body.startswith(RESULT_MARKER + "\n"):
            result_before_activation = True

    if len(matching) > 1:
        raise ActivationError("multiple matching activation markers exist")
    if matching:
        if issue.get("title") != expected_title:
            raise ActivationError("activated issue title drift")
        return {
            "activate": False,
            "reason": "ALREADY_ACTIVATED",
            "dispatch_id": dispatch_id,
            "issue_number": issue_number,
            "lease_epoch": dispatch.get("lease_epoch"),
            "activation_comment_id": matching[0].get("id"),
            "activation_created_at": matching[0].get("created_at"),
        }

    if result_before_activation:
        raise ActivationError("RESULT/1 exists before lease activation")
    if issue.get("title") not in {staging_title, expected_title}:
        raise ActivationError("canonical issue title is neither protected staging nor active title")

    return {
        "activate": True,
        "reason": "ACTIVATION_REQUIRED",
        "dispatch_id": dispatch_id,
        "issue_number": issue_number,
        "lease_epoch": dispatch.get("lease_epoch"),
        "current_title": issue.get("title"),
        "expected_title": expected_title,
        "marker_body": marker_body(dispatch),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--repo-root", type=Path, default=ROOT)
    p.add_argument("--issue-json", type=Path, required=True)
    p.add_argument("--comments-json", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    issue = json.loads(args.issue_json.read_text(encoding="utf-8"))
    comments = json.loads(args.comments_json.read_text(encoding="utf-8"))
    if not isinstance(issue, dict) or not isinstance(comments, list):
        raise SystemExit("issue/comments payload shape invalid")
    try:
        result = plan_activation(args.repo_root, issue, comments)
    except (OSError, json.JSONDecodeError, ActivationError) as exc:
        args.output.write_text(json.dumps({"ok": False, "error": str(exc)}, indent=2) + "\n", encoding="utf-8")
        print(f"ACTIVATION_INVALID: {exc}")
        return 2
    result["ok"] = True
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
