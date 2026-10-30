#!/usr/bin/env python3
"""Fail-closed Mathematics ACTIVE worker claim capacity from real Solve leases.

This observes the existing /claim reservation protocol; it does not create a
new pickup route or infer worker activity from AVAILABLE Project backlog.
The controller workflow serializes all Solve claim/release/reap operations.
Only trusted controller-authored reservation histories count as evidence.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys

try:
    from ci.gcl_worker_queue_contract import active_reservation, reservation_events, parse_time
except ModuleNotFoundError:
    from gcl_worker_queue_contract import active_reservation, reservation_events, parse_time

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / ".gcl/worker_queue/CONFIG.json"
REGISTRY = ROOT / ".gcl/worker_queue/JOBS.json"
REPO = "grandchallenge/MATHSOLVE"
MAX_JOBS = 300


class CapacityError(ValueError):
    pass


def registry_ids() -> dict[int, str]:
    jobs = json.loads(REGISTRY.read_text(encoding="utf-8"))["jobs"]
    if not isinstance(jobs, list) or not jobs or len(jobs) > MAX_JOBS:
        raise CapacityError("protected Solve job roster incomplete or excessive")
    by_number: dict[int, str] = {}
    for job in jobs:
        number, did = job.get("issue_number"), job.get("dispatch_id")
        if (not isinstance(number, int) or number < 1 or number in by_number
                or not isinstance(did, str) or not did or job.get("self_claimable") is not True):
            raise CapacityError("protected Solve job identity drift")
        by_number[number] = did
    return by_number


def decode_gh_pages(stdout: str) -> list[dict]:
    """GitHub CLI --paginate emits concatenated JSON arrays, not one JSON list."""
    decoder = json.JSONDecoder()
    start = 0
    comments: list[dict] = []
    identifiers: set[int] = set()
    while start < len(stdout):
        while start < len(stdout) and stdout[start].isspace():
            start += 1
        if start == len(stdout):
            break
        page, end = decoder.raw_decode(stdout, start)
        if not isinstance(page, list):
            raise CapacityError("unreadable complete issue-comment pages")
        for comment in page:
            if not isinstance(comment, dict):
                raise CapacityError("malformed issue comment")
            ident = comment.get("id")
            if not isinstance(ident, int) or ident in identifiers:
                raise CapacityError("missing or duplicated comment identity")
            identifiers.add(ident)
            comments.append(comment)
        start = end
    if not stdout.strip():
        raise CapacityError("empty GitHub response is not an authenticated comment page")
    return comments


def collect_snapshot() -> dict:
    ids = registry_ids()
    rows = []
    for number, dispatch in sorted(ids.items()):
        proc = subprocess.run(
            ["gh", "api", "--paginate",
             f"repos/{REPO}/issues/{number}/comments?per_page=100"],
            text=True, capture_output=True, timeout=90, check=False,
        )
        if proc.returncode:
            raise CapacityError(
                f"GitHub comment-history read failed at #{number}: {proc.stderr[:250]}")
        rows.append({
            "issue_number": number, "dispatch_id": dispatch,
            "comments": decode_gh_pages(proc.stdout),
        })
    return {
        "record_type": "GCL_ACTIVE_SOLVE_RESERVATIONS_SNAPSHOT/1",
        "repository": REPO, "complete": True,
        "snapshot_at": datetime.now(timezone.utc).isoformat(),
        "total_jobs": len(ids), "rows": rows,
    }


def unresolved_claims(comments: list[dict], at: datetime, bots: set[str]) -> list[int]:
    """Find recent authenticated /claim commands without a bound controller response."""
    from datetime import timedelta
    import re
    acknowledgments = {}
    commands = {}
    for row in comments:
        body = row.get("body")
        if not isinstance(body, str):
            continue
        actor = (row.get("user") or {}).get("login")
        if (actor in bots and (row.get("user") or {}).get("type") == "Bot"
                and "\nGCL-QUEUE-RESPONSE-ORIGIN/1\n" in body):
            matches = re.findall(r"(?m)^source_comment_id: ([1-9][0-9]*)$", body)
            if len(matches) == 1:
                timestamp = row.get("created_at")
                if not isinstance(timestamp, str):
                    raise CapacityError("acknowledgment timestamp missing")
                acknowledged_at = parse_time(timestamp)
                acknowledgments.setdefault(int(matches[0]), []).append(acknowledged_at)
        if body.strip() != "/claim":
            continue
        ident = row.get("id")
        timestamp = row.get("created_at")
        if type(ident) is not int or not isinstance(timestamp, str):
            raise CapacityError("claim source identity incomplete")
        created = parse_time(timestamp)
        if created > at:
            raise CapacityError("future claim timestamp")
        if at - created <= timedelta(hours=2):
            commands[ident] = created
    for ident, times in acknowledgments.items():
        if ident in commands and len(times) > 1:
            raise CapacityError("duplicate controller acknowledgment for claim")
    return sorted(ident for ident, created in commands.items()
                  if not any(created <= when <= at for when in acknowledgments.get(ident, [])))


def count_live(snapshot: dict, at: datetime) -> dict:
    expected = registry_ids()
    if (snapshot.get("record_type") != "GCL_ACTIVE_SOLVE_RESERVATIONS_SNAPSHOT/1"
            or snapshot.get("repository") != REPO or snapshot.get("complete") is not True
            or snapshot.get("total_jobs") != len(expected)):
        raise CapacityError("active Mathematics snapshot identity/completeness missing")
    rows = snapshot.get("rows")
    if not isinstance(rows, list) or len(rows) != len(expected):
        raise CapacityError("partial Mathematics job-comment inventory")
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    bots = set(config.get("controller_comment_actors") or [])
    if not bots:
        raise CapacityError("trusted reservation controller identities unavailable")
    seen = set()
    all_comment_ids = set()
    active_ids = []
    for row in rows:
        n, did = row.get("issue_number"), row.get("dispatch_id")
        if n in seen or expected.get(n) != did:
            raise CapacityError("duplicate or alien Solve dispatch in active snapshot")
        seen.add(n)
        comments = row.get("comments")
        if not isinstance(comments, list):
            raise CapacityError("missing complete reservation comment history")
        # Validate the identity of injected/replayed snapshot rows as rigorously
        # as the live paginated collector. Duplicate IDs make custody ambiguous.
        comment_ids = [c.get("id") for c in comments if isinstance(c, dict)]
        if (len(comment_ids) != len(comments)
                or any(type(ident) is not int for ident in comment_ids)
                or len(set(comment_ids)) != len(comment_ids)):
            raise CapacityError(f"#{n}: incomplete or duplicate comment identities")
        if all_comment_ids.intersection(comment_ids):
            raise CapacityError("comment identity reused across Solve issue histories")
        all_comment_ids.update(comment_ids)
        if unresolved_claims(comments, at, bots):
            raise CapacityError(f"#{n}: unresolved claim comment; hold new admission")
        events = reservation_events(comments, did, bots)
        if events:
            recent = events[-1]
            if recent.get("state") == "RESERVED":
                worker, expires = recent.get("worker"), recent.get("expires_at")
                if not worker or not expires:
                    raise CapacityError(f"#{n} has malformed active reservation")
                parse_time(expires)
        if active_reservation(comments, did, at, bots) is not None:
            active_ids.append(n)
    if seen != set(expected):
        raise CapacityError("one or more protected Solve dispatches missing")
    return {"class": "Mathematics", "active_count": len(active_ids),
            "active_issue_numbers": sorted(active_ids), "complete": True,
            "source": "controller-authored active Solve reservations"}


def decision(snapshot: dict, candidate: dict) -> dict:
    if candidate.get("outcome") != "RESERVED":
        return candidate
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    limits = config.get("active_class_capacity") or {}
    # Editorial direct issue pickup is explicitly NOT governed by this
    # Mathematics reservation controller. Never share or borrow its slots.
    if set(limits) != {"Mathematics", "Editorial"}:
        raise CapacityError("both independent active-class budgets required")
    if any(type(x) is not int or x < 1 for x in limits.values()):
        raise CapacityError("invalid protected class active-capacity limit")
    at = datetime.now(timezone.utc)
    stamp = snapshot.get("snapshot_at")
    if not isinstance(stamp, str):
        raise CapacityError("capacity snapshot timestamp missing")
    try:
        captured = parse_time(stamp)
    except (ValueError, TypeError) as exc:
        raise CapacityError("invalid capacity snapshot timestamp") from exc
    age_seconds = (at - captured).total_seconds()
    if age_seconds < 0 or age_seconds > 300:
        raise CapacityError("capacity snapshot outside five-minute freshness window")
    status = count_live(snapshot, at)
    if status["active_count"] < limits["Mathematics"]:
        return {**candidate,
                "capacity_evidence": {"Mathematics": status,
                     "limit": limits["Mathematics"], "other_class_untouched": True}}
    return {**candidate, "outcome": "REJECTED_MATHEMATICS_ACTIVE_CAPACITY",
            "labels_add": [], "labels_remove": [],
            "response": (
                "CLAIM REJECTED — active Mathematics reservation capacity reached "
                f"({status['active_count']}/{limits['Mathematics']}). "
                "Existing reservations and Editorial work remain unchanged."
            ), "capacity_evidence": {"Mathematics": status,
                     "limit": limits["Mathematics"], "other_class_untouched": True}}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--snapshot-out", type=Path)
    p.add_argument("--snapshot", type=Path)
    p.add_argument("--candidate", type=Path)
    p.add_argument("--output", type=Path)
    args = p.parse_args()
    if args.snapshot_out:
        if args.snapshot or args.candidate or args.output:
            p.error("snapshot collection must be a separate mode")
        obj = collect_snapshot()
        args.snapshot_out.parent.mkdir(parents=True, exist_ok=True)
        args.snapshot_out.write_text(json.dumps(obj) + "\n", encoding="utf-8")
        print("MATHEMATICS_ACTIVE_INVENTORY",obj["total_jobs"])
        return 0
    if not args.candidate or not args.output:
        p.error("--candidate and --output required in decision mode")
    candidate = json.loads(args.candidate.read_text(encoding="utf-8"))
    if candidate.get("outcome") == "RESERVED":
        if not args.snapshot or not args.snapshot.exists():
            raise CapacityError("Mathematics claim missing complete active reservation snapshot")
        snapshot = json.loads(args.snapshot.read_text(encoding="utf-8"))
    else:
        snapshot = {}
    output = decision(snapshot, candidate)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    tmp = args.output.with_suffix(".tmp")
    tmp.write_text(json.dumps(output,indent=2,sort_keys=True) + "\n",encoding="utf-8")
    tmp.replace(args.output)
    print("ACTIVE_CAPACITY_DECISION",output["outcome"])
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, subprocess.SubprocessError, json.JSONDecodeError) as exc:
        print("ACTIVE_CAPACITY_BLOCKED",str(exc),file=sys.stderr)
        raise SystemExit(2)
