from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BASE = Path("work_packages/GCL_ERDOS3")
MARKER = "GCL-CONTRIBUTION-RESULT/1"


class LeaseError(ValueError):
    pass


def utc(value: str) -> datetime:
    if not isinstance(value, str) or not value.endswith("Z"):
        raise LeaseError(f"invalid UTC timestamp: {value!r}")
    return datetime.fromisoformat(value[:-1] + "+00:00").astimezone(timezone.utc)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def valid_result_before_expiry(comments: list[dict[str, Any]], expiry: datetime) -> bool:
    for row in comments:
        body = row.get("body")
        created = row.get("created_at")
        if isinstance(body, str) and body.startswith(MARKER + "\n") and isinstance(created, str):
            if utc(created) <= expiry:
                return True
    return False


def expire_v03(root: Path, now: datetime, comments: list[dict[str, Any]]) -> dict[str, Any]:
    campaign_path = root / BASE / "CAMPAIGN.json"
    frontier_path = root / BASE / "FRONTIER.json"
    campaign = load_json(campaign_path)
    frontier = load_json(frontier_path)

    active = campaign.get("active_dispatches", {})
    if set(active) != {"E3-V03"}:
        return {"changed": False, "reason": "NO_SINGLE_ACTIVE_E3_V03_LEASE"}

    row = active["E3-V03"]
    dispatch_id = row.get("dispatch_id")
    if not isinstance(dispatch_id, str):
        raise LeaseError("active E3-V03 lacks dispatch_id")
    dispatch_path = root / BASE / "dispatches" / f"{dispatch_id}.json"
    if not dispatch_path.is_file():
        raise LeaseError("active dispatch record missing")
    dispatch = load_json(dispatch_path)

    if dispatch.get("lease_policy_id") != "GCL-IA-LEASE-25M-24M-001":
        return {"changed": False, "reason": "ACTIVE_DISPATCH_NOT_ON_EXPIRING_POLICY"}
    if dispatch.get("state") != "DISPATCHED__AWAITING_RETURN":
        return {"changed": False, "reason": "ACTIVE_DISPATCH_NOT_AWAITING_RETURN"}

    expiry = utc(dispatch["lease_expires_at"])
    if now <= expiry:
        return {
            "changed": False,
            "reason": "LEASE_STILL_ACTIVE",
            "dispatch_id": dispatch_id,
            "issue_number": dispatch.get("issue_number"),
            "lease_epoch": dispatch.get("lease_epoch"),
            "lease_expires_at": dispatch.get("lease_expires_at"),
        }
    if valid_result_before_expiry(comments, expiry):
        return {
            "changed": False,
            "reason": "TIMELY_RESULT_PRESENT_DO_NOT_EXPIRE",
            "dispatch_id": dispatch_id,
            "issue_number": dispatch.get("issue_number"),
            "lease_epoch": dispatch.get("lease_epoch"),
        }

    epoch = dispatch.get("lease_epoch")
    attempt = dispatch.get("lease_attempt_ordinal")
    if not isinstance(epoch, int) or not isinstance(attempt, int):
        raise LeaseError("active dispatch lacks numeric lease epoch/attempt")

    dispatch["state"] = "LEASE_EXPIRED__NO_RETURN"
    dispatch["dispatch_status"] = "LEASE_EXPIRED__NO_RETURN"
    dispatch["silence_observed"] = True
    dispatch["valid_result_count_at_expiry"] = 0
    dispatch["stale_return_fenced"] = True
    dispatch["replay_budget_consumed"] = False
    dispatch["mathematical_replay_completed"] = False
    dispatch["issue_close_reason"] = "LEASE_EXPIRED__NO_RETURN"
    dispatch["expiry_effect"] = {
        "canonical_claim_effect": False,
        "frontier_effect": False,
        "verification_effect": False,
        "replay_budget_effect": "NOT_CONSUMED",
    }
    write_json(dispatch_path, dispatch)

    campaign["status"] = "ACTIVE__E3_V03_LEASE_EXPIRED"
    campaign["dispatch_state"] = "VERIFY_LEASE_EXPIRED__REISSUE_REQUIRED"
    campaign["next_action"] = (
        "Reissue E3-V03 under a fresh dispatch/agent identity and lease epoch, "
        "retaining replay_budget_ordinal=1. Accept no evidence from the expired issue."
    )
    ver = campaign.get("verification_dispatches", {}).get("E3-V03", {})
    ver.update({
        "dispatch_id": dispatch_id,
        "issue_number": dispatch.get("issue_number"),
        "issue_url": dispatch.get("issue_url"),
        "state": "LEASE_EXPIRED__NO_RETURN",
        "lease_epoch": epoch,
        "lease_attempt_ordinal": attempt,
        "lease_started_at": dispatch.get("lease_started_at"),
        "lease_expires_at": dispatch.get("lease_expires_at"),
        "replay_budget_consumed": False,
        "successor_dispatch_id": None,
    })
    campaign.setdefault("verification_dispatches", {})["E3-V03"] = ver
    campaign.setdefault("completed_dispatches", {})[f"E3-V03-LEASE-{epoch:03d}"] = {
        "issue_number": dispatch.get("issue_number"),
        "dispatch_id": dispatch_id,
        "state": "LEASE_EXPIRED__NO_RETURN",
        "lease_epoch": epoch,
        "lease_attempt_ordinal": attempt,
        "valid_result_count": 0,
        "replay_budget_consumed": False,
    }
    campaign["active_dispatches"] = {}
    write_json(campaign_path, campaign)

    nodes = {n.get("id"): n for n in frontier.get("nodes", [])}
    vnode = nodes.get("E3-V-B03")
    if not isinstance(vnode, dict):
        raise LeaseError("E3-V-B03 frontier node missing")
    vnode["status"] = "LEASE_EXPIRED__REISSUE_REQUIRED"
    vnode["replay_budget"] = 1
    vnode["replay_budget_consumed"] = 0
    vnode["lease_policy"] = str(BASE / "LEASE_POLICY.json")
    vnode["expired_dispatch"] = {
        "dispatch_id": dispatch_id,
        "issue_number": dispatch.get("issue_number"),
        "lease_epoch": epoch,
        "lease_attempt_ordinal": attempt,
        "lease_started_at": dispatch.get("lease_started_at"),
        "lease_expires_at": dispatch.get("lease_expires_at"),
        "valid_result_count": 0,
        "replay_budget_consumed": False,
    }
    vnode.pop("dispatch", None)
    candidate = nodes.get("E3-Q4-GLUING-RADIUS")
    if isinstance(candidate, dict):
        candidate["promotion_gate"] = "E3-V03__FRESH_LEASE_REQUIRED"
    frontier["next_tranche"] = {
        "id": "E3-V03-REISSUE",
        "status": "LEASE_REQUIRED",
        "objective": "Reissue the same independent verification under a fresh lease epoch without consuming a second mathematical replay.",
        "lease_policy": str(BASE / "LEASE_POLICY.json"),
        "replay_budget_ordinal": 1,
    }
    write_json(frontier_path, frontier)

    return {
        "changed": True,
        "reason": "LEASE_EXPIRED__NO_RETURN",
        "dispatch_id": dispatch_id,
        "issue_number": dispatch.get("issue_number"),
        "lease_epoch": epoch,
        "lease_attempt_ordinal": attempt,
        "lease_expires_at": dispatch.get("lease_expires_at"),
        "replay_budget_consumed": False,
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--repo-root", type=Path, default=ROOT)
    p.add_argument("--now", required=True)
    p.add_argument("--comments-json", type=Path, required=True)
    p.add_argument("--result-json", type=Path, required=True)
    args = p.parse_args()
    now = utc(args.now)
    comments = json.loads(args.comments_json.read_text(encoding="utf-8"))
    if not isinstance(comments, list):
        raise SystemExit("comments JSON must be a list")
    result = expire_v03(args.repo_root, now, comments)
    args.result_json.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
