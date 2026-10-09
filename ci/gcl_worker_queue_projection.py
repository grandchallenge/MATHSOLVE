from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import sys

# Production workflows execute this file directly (`python ci/...py`).
# In that mode Python places `ci/` rather than the repository root on
# `sys.path`, so the package-qualified import below would otherwise fail.
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from ci.gcl_worker_queue_contract import active_reservation

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / ".gcl/worker_queue/PROJECT.json"
JOBS = ROOT / ".gcl/worker_queue/JOBS.json"
CONFIG = ROOT / ".gcl/worker_queue/CONFIG.json"
RESULT_MARKER = "GCL-CONTRIBUTION-RESULT/1"
INTAKE_CAPTURED_PREFIX = "INTAKE CAPTURED"
INTAKE_REJECTED_PREFIX = "INTAKE REJECTED —"


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


def project_metadata_updates(job: dict[str, Any], project: dict[str, Any]) -> list[dict[str, Any]]:
    """Project immutable queue metadata from protected registry/dispatch sources."""
    cfg = load_json(CONFIG)
    rules = cfg.get("project_metadata_projection") or {}
    dispatch_path = ROOT / str(job.get("dispatch_path") or "")
    if not dispatch_path.is_file():
        raise ValueError(f"{job.get('dispatch_id')}: dispatch missing for Project metadata projection")
    dispatch = load_json(dispatch_path)

    campaign = str(dispatch.get("campaign") or "").strip()
    if not campaign:
        raise ValueError(f"{job.get('dispatch_id')}: dispatch campaign missing")
    campaign = (rules.get("campaign_aliases") or {}).get(campaign, campaign)

    def mapped(group: str, value: Any) -> str:
        table = rules.get(group) or {}
        key = str(value or "")
        if key not in table:
            raise ValueError(
                f"{job.get('dispatch_id')}: no Project {group} mapping for {key!r}"
            )
        return str(table[key])

    role = mapped("role", job.get("role"))
    collaboration = mapped("collaboration", job.get("collaboration_mode"))
    phase = mapped("phase", job.get("visibility_phase"))
    cohort = str(job.get("cohort_id") or "").strip()
    if not cohort:
        raise ValueError(f"{job.get('dispatch_id')}: cohort_id missing")

    updates = [
        {"field_id": field_id(project, "campaign"), "value": campaign},
        {"field_id": field_id(project, "role"), "value": role},
        {"field_id": field_id(project, "collaboration"), "value": collaboration},
        {"field_id": field_id(project, "phase"), "value": phase},
        {"field_id": field_id(project, "cohort"), "value": cohort},
    ]
    if job.get("timebox_minutes") is not None:
        updates.append({
            "field_id": field_id(project, "timebox"),
            "value": int(job["timebox_minutes"]),
        })
    return updates


def latest_result_intake_state(
    comments: list[dict[str, Any]],
    controller_actors: set[str],
) -> str | None:
    state: str | None = None
    for comment in comments:
        body = comment.get("body")
        actor = str((comment.get("user") or {}).get("login") or "")
        if isinstance(body, str) and body.startswith(RESULT_MARKER + "\n"):
            state = "PENDING"
            continue
        if state is None or actor not in controller_actors or not isinstance(body, str):
            continue
        if body.startswith(INTAKE_CAPTURED_PREFIX):
            state = "CAPTURED"
        elif body.startswith(INTAKE_REJECTED_PREFIX):
            state = "REJECTED"
    return state


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

    updates: list[dict[str, Any]] = project_metadata_updates(job, project)
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
        elif outcome == "REJECTED_RESULT_COMMENT_PRESENT":
            updates.append({"field_id": state_id, "value": "BLOCKED"})
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
        controller_actors = set(cfg.get("controller_comment_actors", []))
        result_state = latest_result_intake_state(comments, controller_actors)
        if result_state == "CAPTURED":
            updates.append({"field_id": state_id, "value": "RETURNED"})
            clears.append(expires_id)
            return {
                "queue_managed": True,
                "dispatch_id": dispatch_id,
                "issue_number": job["issue_number"],
                "reservation_state": "RETURNED",
                "issue_field_values": updates,
                "clear_field_ids": clears,
            }
        if result_state == "REJECTED":
            updates.append({"field_id": state_id, "value": "AVAILABLE"})
            clears.extend([worker_id, expires_id])
            return {
                "queue_managed": True,
                "dispatch_id": dispatch_id,
                "issue_number": job["issue_number"],
                "reservation_state": "RESULT_REJECTED",
                "issue_field_values": updates,
                "clear_field_ids": clears,
            }
        if result_state == "PENDING":
            updates.append({"field_id": state_id, "value": "BLOCKED"})
            clears.append(expires_id)
            return {
                "queue_managed": True,
                "dispatch_id": dispatch_id,
                "issue_number": job["issue_number"],
                "reservation_state": "RESULT_PENDING",
                "issue_field_values": updates,
                "clear_field_ids": clears,
            }
        at = now or datetime.now(timezone.utc)
        active = active_reservation(
            comments,
            str(dispatch_id),
            at.astimezone(timezone.utc),
            controller_actors,
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
