from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from ci.gcl_worker_queue_contract import active_reservation

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / ".gcl/worker_queue/PROJECT.json"
JOBS = ROOT / ".gcl/worker_queue/JOBS.json"
CONFIG = ROOT / ".gcl/worker_queue/CONFIG.json"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def job_by_dispatch(dispatch_id: str) -> dict[str, Any] | None:
    for job in load_json(JOBS).get("jobs", []):
        if job.get("dispatch_id") == dispatch_id:
            return job
    return None


def job_by_issue(issue_number: int) -> dict[str, Any] | None:
    for job in load_json(JOBS).get("jobs", []):
        if job.get("issue_number") == issue_number:
            return job
    return None


def field_id(project: dict[str, Any], name: str) -> int:
    return int(project["issue_fields"][name]["rest_id"])


def projection(
    mode: str,
    dispatch_id: str | None = None,
    result: dict[str, Any] | None = None,
    issue_number: int | None = None,
    comments: list[dict[str, Any]] | None = None,
    now: datetime | None = None,
) -> dict[str, Any]:
    project = load_json(PROJECT)
    if result is not None:
        dispatch_id = str(result.get("dispatch_id") or dispatch_id or "")
    job = job_by_dispatch(dispatch_id) if dispatch_id else None
    if mode == "reconcile":
        if issue_number is None:
            raise ValueError("reconcile requires issue_number")
        job = job_by_issue(issue_number)
        if job is not None:
            dispatch_id = str(job["dispatch_id"])
    if job is None:
        return {
            "queue_managed": False,
            "dispatch_id": dispatch_id,
            "issue_field_values": [],
            "clear_field_ids": [],
        }

    updates: list[dict[str, Any]] = []
    clears: list[int] = []
    state_id = field_id(project, "state")
    worker_id = field_id(project, "worker")
    expires_id = field_id(project, "reservation_expires")

    if mode == "command":
        if result is None:
            raise ValueError("command mode requires result")
        outcome = result.get("outcome")
        if outcome == "RESERVED":
            updates.extend([
                {"field_id": state_id, "value": "RESERVED"},
                {"field_id": worker_id, "value": str(result["worker"])},
                {"field_id": expires_id, "value": str(result["expires_at"])},
            ])
        elif outcome == "RELEASED":
            updates.append({"field_id": state_id, "value": "AVAILABLE"})
            clears.extend([worker_id, expires_id])
        elif outcome == "REJECTED_RESULT_ALREADY_PROTECTED":
            updates.append({"field_id": state_id, "value": "RETURNED"})
            clears.append(expires_id)
    elif mode == "intake":
        updates.append({"field_id": state_id, "value": "RETURNED"})
        clears.append(expires_id)
    elif mode == "expire":
        updates.append({"field_id": state_id, "value": "AVAILABLE"})
        clears.extend([worker_id, expires_id])
    elif mode == "reconcile":
        if comments is None:
            raise ValueError("reconcile requires comments")
        cfg = load_json(CONFIG)
        at = now or datetime.now(timezone.utc)
        active = active_reservation(
            comments,
            str(dispatch_id),
            at.astimezone(timezone.utc),
            set(cfg.get("controller_comment_actors", [])),
        )
        if active is None:
            updates.append({"field_id": state_id, "value": "AVAILABLE"})
            clears.extend([worker_id, expires_id])
            reservation_state = "EXPIRED"
        else:
            updates.extend([
                {"field_id": state_id, "value": "RESERVED"},
                {"field_id": worker_id, "value": str(active["worker"])},
                {"field_id": expires_id, "value": str(active["expires_at"])},
            ])
            reservation_state = "ACTIVE"
        return {
            "queue_managed": True,
            "dispatch_id": dispatch_id,
            "issue_number": job["issue_number"],
            "reservation_state": reservation_state,
            "issue_field_values": updates,
            "clear_field_ids": clears,
        }
    else:
        raise ValueError(f"unsupported mode: {mode}")

    return {
        "queue_managed": True,
        "dispatch_id": dispatch_id,
        "issue_number": job["issue_number"],
        "issue_field_values": updates,
        "clear_field_ids": clears,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["command", "intake", "expire", "reconcile"], required=True)
    parser.add_argument("--dispatch-id")
    parser.add_argument("--result", type=Path)
    parser.add_argument("--issue-number", type=int)
    parser.add_argument("--comments", type=Path)
    parser.add_argument("--now")
    args = parser.parse_args()

    result = load_json(args.result) if args.result else None
    comments = load_json(args.comments) if args.comments else None
    at = None
    if args.now:
        at = datetime.fromisoformat(args.now.replace("Z", "+00:00")).astimezone(timezone.utc)
    data = projection(
        args.mode,
        dispatch_id=args.dispatch_id,
        result=result,
        issue_number=args.issue_number,
        comments=comments,
        now=at,
    )
    print(json.dumps(data, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
