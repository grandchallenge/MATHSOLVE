from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

RESERVATION_MARKER = "GCL-WORKER-RESERVATION/1"
QUEUE_REGISTRY = Path(".gcl/worker_queue/JOBS.json")


def parse_time(value: str) -> datetime:
    text = value.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    dt = datetime.fromisoformat(text)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def queue_job_for_dispatch(root: Path, dispatch_id: str) -> dict[str, Any] | None:
    path = root / QUEUE_REGISTRY
    if not path.is_file():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    for job in data.get("jobs", []):
        if isinstance(job, dict) and job.get("dispatch_id") == dispatch_id:
            return job
    return None


def reservation_events(
    comments: list[dict[str, Any]],
    dispatch_id: str,
    controller_actors: set[str] | None = None,
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for comment in comments:
        body = comment.get("body")
        if not isinstance(body, str) or not body.startswith(RESERVATION_MARKER + "\n"):
            continue
        user = comment.get("user") or {}
        actor = user.get("login")
        if controller_actors is not None and actor not in controller_actors:
            continue
        fields: dict[str, str] = {}
        for line in body.splitlines()[1:]:
            if ": " in line:
                key, value = line.split(": ", 1)
                fields[key.strip()] = value.strip()
        if fields.get("dispatch_id") != dispatch_id:
            continue
        if fields.get("state") not in {"RESERVED", "RELEASED", "RETURNED"}:
            continue
        fields["_created_at"] = str(comment.get("created_at") or "")
        fields["_comment_id"] = str(comment.get("id") or "")
        out.append(fields)
    out.sort(key=lambda x: (x.get("_created_at", ""), x.get("_comment_id", "")))
    return out


def active_reservation(
    comments: list[dict[str, Any]],
    dispatch_id: str,
    at: datetime,
    controller_actors: set[str] | None = None,
) -> dict[str, Any] | None:
    events = reservation_events(comments, dispatch_id, controller_actors)
    if not events:
        return None
    latest = events[-1]
    if latest.get("state") != "RESERVED":
        return None
    expires = latest.get("expires_at")
    worker = latest.get("worker")
    if not expires or not worker:
        return None
    if parse_time(expires) <= at.astimezone(timezone.utc):
        return None
    return latest
