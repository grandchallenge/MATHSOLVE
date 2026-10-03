#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / ".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json"
BOARD = ROOT / "handoffs/OPENMATH-2026/CEX_JOB_BOARD.md"
INDEX = ROOT / "handoffs/OPENMATH-2026/launch/README.md"
HILLS = [f"OM26-H{i}" for i in range(1, 8)]
PINNED = re.compile(r"^https://github\.com/grandchallenge/MATHSOLVE/blob/([0-9a-f]{40})/(.+)$")


def load(path: Path | str):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def validate() -> list[str]:
    errors: list[str] = []
    registry = load(REGISTRY)
    if registry.get("record_type") != "GCL_CEX_ASSIGNMENT_REGISTRY":
        errors.append("registry record_type mismatch")
    topology = registry.get("current_topology", {})
    if topology.get("hills") != HILLS:
        errors.append("current hill roster mismatch")
    if topology.get("grouped_current_lanes") not in (None, []):
        errors.append("grouped current lanes must be empty")

    assignments = {
        x["assignment_id"]: x
        for x in registry.get("assignments", [])
        if isinstance(x, dict) and x.get("assignment_id")
    }
    policy = registry.get("mathematics_release_policy", {})
    per_hill = policy.get("per_hill", {})
    if set(per_hill) != set(HILLS):
        errors.append("per-hill release policy roster mismatch")

    scripts = registry.get("launch_contract", {}).get("current_scripts", {})
    if list(scripts) != HILLS:
        errors.append("launch-script roster mismatch")

    active_leased = 0
    for hill in HILLS:
        p = per_hill.get(hill, {})
        aid = p.get("assignment")
        item = assignments.get(aid, {})
        if not item:
            errors.append(f"{hill}: current assignment missing")
            continue
        if item.get("hill") != hill:
            errors.append(f"{hill}: assignment hill mismatch")
        if p.get("agent_state") != item.get("state"):
            errors.append(f"{hill}: release policy state differs from assignment")

        script = scripts.get(hill, {})
        if item.get("state") == "LEASED_NOT_LAUNCHED":
            active_leased += 1
            lease = item.get("lease", {})
            if lease.get("state") != "LEASED":
                errors.append(f"{hill}: current lease not LEASED")
            if lease.get("execution_authorized") is not True:
                errors.append(f"{hill}: current lease not execution-authorized")
            if item.get("lifecycle", {}).get("launched") is not False:
                errors.append(f"{hill}: current assignment unexpectedly launched")
            if script.get("executable") is not True:
                errors.append(f"{hill}: current task not executable")
            for key in ("assignment_id", "dispatch_id", "agent_ref"):
                expected = item.get("assignment_id") if key == "assignment_id" else lease.get(key)
                if script.get(key) != expected:
                    errors.append(f"{hill}: current script {key} mismatch")
            rel = script.get("path", "")
            task = ROOT / rel
            if not task.is_file():
                errors.append(f"{hill}: current task file missing")
            else:
                if script.get("task_blob_sha1") != git_blob_sha1(task):
                    errors.append(f"{hill}: current task blob mismatch")
            match = PINNED.fullmatch(str(script.get("task_url", "")))
            if not match:
                errors.append(f"{hill}: task URL is not immutable")
            else:
                commit, url_path = match.groups()
                if commit != script.get("task_commit") or url_path != rel:
                    errors.append(f"{hill}: task URL identity mismatch")
        elif item.get("state") == "ACCEPTED":
            if item.get("lifecycle", {}).get("closed") is not True:
                errors.append(f"{hill}: accepted current assignment is not closed")
        else:
            errors.append(f"{hill}: unsupported current assignment state {item.get('state')}")

        pred = p.get("predecessor")
        if pred:
            prev = assignments.get(pred.get("assignment"), {})
            if prev.get("state") != "ACCEPTED":
                errors.append(f"{hill}: predecessor not ACCEPTED")
            if prev.get("lifecycle", {}).get("closed") is not True:
                errors.append(f"{hill}: predecessor not closed")

    support_scripts = registry.get("launch_contract", {}).get("support_scripts", {})
    for slot, script in support_scripts.items():
        item = assignments.get(script.get("assignment_id"), {})
        if item.get("lane_role") != "SUPPORT" or item.get("support_slot") != slot:
            errors.append(f"{slot}: supporting task role/slot mismatch")
        if item.get("state") == "LEASED_NOT_LAUNCHED":
            active_leased += 1
            lease = item.get("lease", {})
            if lease.get("state") != "LEASED" or lease.get("execution_authorized") is not True:
                errors.append(f"{slot}: supporting lease not authorized")
            for key in ("assignment_id", "dispatch_id", "agent_ref"):
                expected = item.get("assignment_id") if key == "assignment_id" else lease.get(key)
                if script.get(key) != expected:
                    errors.append(f"{slot}: supporting script {key} mismatch")
            path = ROOT / script.get("path", "")
            if not path.is_file() or script.get("task_blob_sha1") != git_blob_sha1(path):
                errors.append(f"{slot}: supporting task blob mismatch")
            match = PINNED.fullmatch(str(script.get("task_url", "")))
            if not match or match.groups() != (script.get("task_commit"), script.get("path")):
                errors.append(f"{slot}: supporting task URL identity mismatch")
            if script.get("intended_return") != lease.get("return_url"):
                errors.append(f"{slot}: supporting return mismatch")
        else:
            errors.append(f"{slot}: unsupported supporting state")

    math_assignments = [
        x for x in assignments.values()
        if x.get("class") == "MATHEMATICAL_RESEARCH"
    ]
    accepted = sum(1 for x in math_assignments if x.get("state") == "ACCEPTED")
    summary = policy.get("summary", {})
    if summary.get("accepted_agents") != accepted:
        errors.append("accepted-agent summary mismatch")
    if summary.get("leased_not_launched_agents") != active_leased:
        errors.append("leased-not-launched summary mismatch")
    if summary.get("returned_unadjudicated_agents") not in (0, None):
        errors.append("returned-unadjudicated summary must be zero after lifecycle candidate")

    board = BOARD.read_text(encoding="utf-8")
    if "READY -> LAUNCHED -> RETURNED -> CAPTURED -> REPLAYED -> ADJUDICATED -> ADVANCED" not in board:
        errors.append("job board missing frozen lifecycle")
    for x in math_assignments:
        marker = f"| `{x['assignment_id']}` |"
        if marker not in board:
            errors.append(f"job board missing {x['assignment_id']}")

    index = INDEX.read_text(encoding="utf-8")
    if "LINK_IN_RELAY_OUT" not in index:
        errors.append("launch index missing LINK_IN_RELAY_OUT")
    for hill, row in {**scripts, **support_scripts}.items():
        if row.get("task_url") and row.get("task_url") not in index:
            errors.append(f"launch index missing {hill} task URL")

    if registry.get("launch_contract", {}).get("mode") != "LINK_IN_RELAY_OUT":
        errors.append("launch mode mismatch")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print("FAIL:", error)
        return 1
    print("PASS: OPENMATH seven-hill registry, lifecycle board, and immutable launch tasks agree")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
