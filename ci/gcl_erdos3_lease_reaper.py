from __future__ import annotations

import argparse
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BASE = Path("work_packages/GCL_ERDOS3")
RESULT_MARKER = "GCL-CONTRIBUTION-RESULT/1"
ACTIVATION_MARKER = "GCL-LEASE-ACTIVATION/1"


class LeaseError(ValueError):
    pass


def utc(value: Any) -> datetime:
    if not isinstance(value, str) or not value.endswith("Z"):
        raise LeaseError(f"invalid UTC timestamp: {value!r}")
    return datetime.fromisoformat(value[:-1] + "+00:00").astimezone(timezone.utc)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def parse_activation(body: Any) -> dict[str, str] | None:
    if not isinstance(body, str) or not body.startswith(ACTIVATION_MARKER + "\n"):
        return None
    lines = body.splitlines()
    keys = ("dispatch_id", "assignment", "lease_epoch", "lease_duration_minutes", "agent_max_execution_minutes")
    if len(lines) != 1 + len(keys):
        raise LeaseError("activation marker has unexpected shape")
    out: dict[str, str] = {}
    for i, key in enumerate(keys, start=1):
        prefix = key + ": "
        if not lines[i].startswith(prefix):
            raise LeaseError(f"activation marker expected field {key}")
        value = lines[i][len(prefix):].strip()
        if not value:
            raise LeaseError(f"activation marker field {key} is empty")
        out[key] = value
    return out


def find_activation(comments: list[dict[str, Any]], dispatch: dict[str, Any]) -> dict[str, Any] | None:
    matches: list[dict[str, Any]] = []
    for row in comments:
        parsed = parse_activation(row.get("body"))
        if parsed is None:
            continue
        if (
            parsed.get("dispatch_id") == dispatch.get("dispatch_id")
            and parsed.get("assignment") == dispatch.get("assignment_id")
            and parsed.get("lease_epoch") == str(dispatch.get("lease_epoch"))
        ):
            matches.append({"comment": row, "parsed": parsed})
    if not matches:
        return None
    if len(matches) != 1:
        raise LeaseError("expected exactly one matching activation marker")
    match = matches[0]
    parsed = match["parsed"]
    if parsed.get("lease_duration_minutes") != "25":
        raise LeaseError("activation marker lease duration drift")
    if parsed.get("agent_max_execution_minutes") != "24":
        raise LeaseError("activation marker agent cap drift")
    comment = match["comment"]
    if not isinstance(comment.get("id"), int):
        raise LeaseError("activation marker comment id unavailable")
    start = utc(comment.get("created_at"))
    return {
        "comment_id": comment["id"],
        "start": start,
        "expiry": start + timedelta(minutes=25),
    }


def result_matches_dispatch(body: Any, dispatch: dict[str, Any]) -> bool:
    if not isinstance(body, str) or not body.startswith(RESULT_MARKER + "\n"):
        return False
    lines = body.splitlines()
    wanted = {
        "dispatch_id": str(dispatch.get("dispatch_id")),
        "assignment": str(dispatch.get("assignment_id")),
        "agent_ref": str(dispatch.get("agent_ref")),
        "lease_epoch": str(dispatch.get("lease_epoch")),
    }
    found: dict[str, str] = {}
    for line in lines[1:12]:
        if ": " not in line:
            if line == "":
                break
            continue
        key, value = line.split(": ", 1)
        if key in wanted:
            found[key] = value.strip()
    return found == wanted


def valid_result_before_expiry(
    comments: list[dict[str, Any]], dispatch: dict[str, Any], start: datetime, expiry: datetime
) -> bool:
    for row in comments:
        if not result_matches_dispatch(row.get("body"), dispatch):
            continue
        created = utc(row.get("created_at"))
        if start <= created <= expiry:
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
    if dispatch.get("lease_clock_source") != "GITHUB_ACTIVATION_COMMENT":
        return {"changed": False, "reason": "ACTIVE_DISPATCH_NOT_MARKER_CLOCK"}
    if dispatch.get("state") != "DISPATCHED__AWAITING_RETURN":
        return {"changed": False, "reason": "ACTIVE_DISPATCH_NOT_AWAITING_RETURN"}

    activation = find_activation(comments, dispatch)
    if activation is None:
        return {
            "changed": False,
            "reason": "LEASE_NOT_ACTIVATED",
            "dispatch_id": dispatch_id,
            "issue_number": dispatch.get("issue_number"),
            "lease_epoch": dispatch.get("lease_epoch"),
        }

    start = activation["start"]
    expiry = activation["expiry"]
    if now <= expiry:
        return {
            "changed": False,
            "reason": "LEASE_STILL_ACTIVE",
            "dispatch_id": dispatch_id,
            "issue_number": dispatch.get("issue_number"),
            "lease_epoch": dispatch.get("lease_epoch"),
            "activation_comment_id": activation["comment_id"],
            "lease_started_at": start.isoformat().replace("+00:00", "Z"),
            "lease_expires_at": expiry.isoformat().replace("+00:00", "Z"),
        }
    if valid_result_before_expiry(comments, dispatch, start, expiry):
        return {
            "changed": False,
            "reason": "TIMELY_RESULT_PRESENT_DO_NOT_EXPIRE",
            "dispatch_id": dispatch_id,
            "issue_number": dispatch.get("issue_number"),
            "lease_epoch": dispatch.get("lease_epoch"),
            "activation_comment_id": activation["comment_id"],
        }

    epoch = dispatch.get("lease_epoch")
    attempt = dispatch.get("lease_attempt_ordinal")
    if not isinstance(epoch, int) or not isinstance(attempt, int):
        raise LeaseError("active dispatch lacks numeric lease epoch/attempt")

    start_z = start.isoformat().replace("+00:00", "Z")
    expiry_z = expiry.isoformat().replace("+00:00", "Z")
    dispatch["state"] = "LEASE_EXPIRED__NO_RETURN"
    dispatch["dispatch_status"] = "LEASE_EXPIRED__NO_RETURN"
    dispatch["lease_activation_comment_id"] = activation["comment_id"]
    dispatch["lease_started_at_observed"] = start_z
    dispatch["lease_expires_at_observed"] = expiry_z
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
        "lease_activation_comment_id": activation["comment_id"],
        "lease_started_at_observed": start_z,
        "lease_expires_at_observed": expiry_z,
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
        "lease_activation_comment_id": activation["comment_id"],
        "lease_started_at_observed": start_z,
        "lease_expires_at_observed": expiry_z,
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
        "lease_activation_comment_id": activation["comment_id"],
        "lease_started_at_observed": start_z,
        "lease_expires_at_observed": expiry_z,
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
        "activation_comment_id": activation["comment_id"],
        "lease_started_at": start_z,
        "lease_expires_at": expiry_z,
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
