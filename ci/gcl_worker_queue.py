from __future__ import annotations

import argparse
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

try:
    from ci.gcl_worker_queue_contract import active_reservation
except ModuleNotFoundError:
    from gcl_worker_queue_contract import active_reservation

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / ".gcl/worker_queue/CONFIG.json"
REGISTRY = ROOT / ".gcl/worker_queue/JOBS.json"
RESULT_MARKER = "GCL-CONTRIBUTION-RESULT/1"
RESERVATION_MARKER = "GCL-WORKER-RESERVATION/1"


class QueueError(ValueError):
    pass


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def job_for_issue(registry: dict[str, Any], issue_number: int) -> dict[str, Any]:
    matches = [j for j in registry.get("jobs", []) if j.get("issue_number") == issue_number]
    if len(matches) != 1:
        raise QueueError("issue is not bound to exactly one queue job")
    return matches[0]


def validate_dispatch(job: dict[str, Any], issue: dict[str, Any]) -> dict[str, Any]:
    path = ROOT / str(job.get("dispatch_path", ""))
    if not path.is_file():
        raise QueueError("protected dispatch is missing")
    dispatch = load_json(path)
    if dispatch.get("dispatch_id") != job.get("dispatch_id"):
        raise QueueError("queue/dispatch identity mismatch")
    if dispatch.get("github_issue_number") != issue.get("number"):
        raise QueueError("queue issue differs from protected dispatch")
    if dispatch.get("github_issue_title") != issue.get("title"):
        raise QueueError("issue title differs from protected dispatch")
    if dispatch.get("dispatch_status") != "READY_FOR_GITHUB_COMMENT":
        raise QueueError("protected dispatch is not ready")
    if dispatch.get("protected_lease_required") is not True or dispatch.get("lease_state") != "ACTIVE":
        raise QueueError("protected execution lease is not active")
    if dispatch.get("canonical_mutation_authorized") is not False:
        raise QueueError("protected dispatch improperly authorizes canonical mutation")
    if dispatch.get("certification_authorized") is not False:
        raise QueueError("protected dispatch improperly authorizes certification")
    task_path = ROOT / str(dispatch.get("task_path", ""))
    if not task_path.is_file():
        raise QueueError("immutable launch artifact is missing")
    return dispatch


def protected_result_exists(dispatch_id: str) -> bool:
    pattern = f"contributions/**/raw/{dispatch_id}/github-comment-*.md"
    return any(ROOT.glob(pattern))


def any_result_comment(comments: list[dict[str, Any]]) -> bool:
    return any(
        isinstance(c.get("body"), str) and c["body"].startswith(RESULT_MARKER + "\n")
        for c in comments
    )


def build_marker(
    dispatch_id: str,
    state: str,
    worker: str,
    actor: str,
    claimed_at: str | None = None,
    expires_at: str | None = None,
    reason: str | None = None,
) -> str:
    lines = [
        RESERVATION_MARKER,
        f"dispatch_id: {dispatch_id}",
        f"state: {state}",
        f"worker: {worker}",
        f"controller_actor: {actor}",
    ]
    if claimed_at:
        lines.append(f"claimed_at: {claimed_at}")
    if expires_at:
        lines.append(f"expires_at: {expires_at}")
    if reason:
        lines.append(f"reason: {reason}")
    lines.extend([
        "reservation_is_execution_authority: NO",
        "mathematical_effect: NO",
        "certification_effect: NO",
    ])
    return "\n".join(lines)


def process(event: dict[str, Any], comments: list[dict[str, Any]], when: datetime) -> dict[str, Any]:
    config = load_json(CONFIG)
    registry = load_json(REGISTRY)
    issue = event.get("issue") or {}
    comment = event.get("comment") or {}
    if issue.get("pull_request"):
        raise QueueError("pull requests are not queue jobs")
    number = issue.get("number")
    if not isinstance(number, int):
        raise QueueError("issue number unavailable")
    body = str(comment.get("body") or "").strip()
    if body not in {"/claim", "/release"}:
        raise QueueError("unsupported queue command")
    actor = str((comment.get("user") or {}).get("login") or "")
    if not actor:
        raise QueueError("authenticated GitHub actor unavailable")

    job = job_for_issue(registry, number)
    if job.get("self_claimable") is not True:
        raise QueueError("job is not self-claimable")
    dispatch = validate_dispatch(job, issue)
    dispatch_id = str(job["dispatch_id"])
    controller_actors = set(config.get("controller_comment_actors", []))
    active = active_reservation(comments, dispatch_id, when, controller_actors)

    common = {
        "dispatch_id": dispatch_id,
        "issue_number": number,
        "actor": actor,
        "collaboration_mode": job["collaboration_mode"],
        "visibility_phase": job["visibility_phase"],
        "sibling_use_policy": job["sibling_use_policy"],
        "role": job["role"],
    }

    if body == "/claim":
        if protected_result_exists(dispatch_id):
            return {**common, "outcome": "REJECTED_RESULT_ALREADY_PROTECTED", "labels_add": ["returned"], "labels_remove": ["available", "reserved"],
                    "response": "CLAIM REJECTED — a protected result already exists for this dispatch."}
        if any_result_comment(comments):
            return {**common, "outcome": "REJECTED_RESULT_COMMENT_PRESENT", "labels_add": [], "labels_remove": [],
                    "response": "CLAIM REJECTED — a RESULT/1 comment is already present on this issue and must be reconciled before reassignment."}
        if active is not None:
            return {**common, "outcome": "REJECTED_ALREADY_RESERVED", "labels_add": ["reserved"], "labels_remove": ["available"],
                    "response": f"CLAIM REJECTED — already reserved by @{active['worker']} until {active['expires_at']}."}
        ttl = int(job.get("reservation_ttl_minutes", 60))
        claimed = iso(when)
        expires = iso(when + timedelta(minutes=ttl))
        task_commit = str(job["task_commit"])
        task_path = str(dispatch["task_path"])
        task_url = f"https://github.com/grandchallenge/MATHSOLVE/blob/{task_commit}/{task_path}"
        marker = build_marker(dispatch_id, "RESERVED", actor, "github-actions[bot]", claimed, expires)
        response = "\n".join([
            marker,
            "",
            "CLAIM ACCEPTED",
            f"role: {job['role']}",
            f"collaboration_mode: {job['collaboration_mode']}",
            f"visibility_phase: {job['visibility_phase']}",
            f"sibling_use_policy: {job['sibling_use_policy']}",
            f"cohort_id: {job['cohort_id']}",
            f"immutable_task: {task_url}",
            f"return_issue: https://github.com/grandchallenge/MATHSOLVE/issues/{number}",
            "",
            "The protected dispatch and execution lease remain authoritative. This reservation creates no mathematical or certification effect.",
        ])
        return {**common, "outcome": "RESERVED", "worker": actor, "claimed_at": claimed, "expires_at": expires,
                "task_url": task_url, "labels_add": ["reserved"], "labels_remove": ["available", "returned"], "response": response}

    if active is None:
        return {**common, "outcome": "REJECTED_NO_ACTIVE_RESERVATION", "labels_add": ["available"], "labels_remove": ["reserved"],
                "response": "RELEASE REJECTED — no active reservation exists."}
    if actor != active.get("worker") and actor not in set(config.get("operators", [])):
        return {**common, "outcome": "REJECTED_NOT_OWNER", "labels_add": [], "labels_remove": [],
                "response": f"RELEASE REJECTED — active reservation belongs to @{active['worker']}."}
    marker = build_marker(dispatch_id, "RELEASED", str(active["worker"]), "github-actions[bot]", reason=f"released_by:{actor}")
    response = marker + "\n\nRELEASE ACCEPTED — the job is operationally available again if its protected dispatch remains executable."
    return {**common, "outcome": "RELEASED", "worker": active["worker"], "labels_add": ["available"], "labels_remove": ["reserved"], "response": response}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--event", type=Path, required=True)
    parser.add_argument("--comments", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--now")
    args = parser.parse_args()
    try:
        event = load_json(args.event)
        comments = load_json(args.comments)
        if not isinstance(comments, list):
            raise QueueError("comments payload must be a JSON list")
        when = datetime.fromisoformat(args.now.replace("Z", "+00:00")) if args.now else now_utc()
        result = process(event, comments, when.astimezone(timezone.utc))
    except (OSError, json.JSONDecodeError, QueueError, KeyError, ValueError) as exc:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps({"outcome": "ERROR", "response": f"QUEUE COMMAND REJECTED — {exc}"}) + "\n", encoding="utf-8")
        print(f"QUEUE_INVALID: {exc}")
        return 2
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
