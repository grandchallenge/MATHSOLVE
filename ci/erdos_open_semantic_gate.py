#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BASE_REL = Path("contributions/ERDOS-OPEN-001/RECON_TRANCHE_001")
POLICY_REL = BASE_REL / "SEMANTIC_GATE_POLICY.json"

BLOCKER_MARKER = "GCL-SEMANTIC-BLOCKER/1"
SOURCE_FORMAL_CONFLICT = "SOURCE_FORMAL_CONFLICT"
ALLOWED_BLOCKER_DISPOSITIONS = {
    "COUNTEREXAMPLE",
    "SOURCE_INTERFACE_FOUND",
    "EXACT_BLOCKER",
}
BLOCKER_ID_RE = re.compile(r"^[A-Z0-9][A-Z0-9._:-]{2,127}$")
ERDOS_DISPATCH_RE = re.compile(r"^ERDOS-(593|595|241|470|1052|99|101|138)-(R1|S1|A1)-IA-001$")


def _readj(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _problem_for_dispatch(dispatch_id: str) -> str:
    match = ERDOS_DISPATCH_RE.fullmatch(dispatch_id)
    if match is None:
        raise ValueError("semantic blocker dispatch is not a registered ERDOS-OPEN lane")
    return match.group(1)


def _normalize_blocker(blocker: dict[str, Any], problem: str) -> dict[str, str]:
    blocker_id = blocker.get("blocker_id")
    kind = blocker.get("kind")
    requires_dispatch_id = blocker.get("requires_dispatch_id")
    reason = blocker.get("reason", "")

    if not isinstance(blocker_id, str) or not BLOCKER_ID_RE.fullmatch(blocker_id):
        raise ValueError("semantic blocker_id is malformed")
    if kind != SOURCE_FORMAL_CONFLICT:
        raise ValueError("semantic blocker kind is not supported")
    expected_source = f"ERDOS-{problem}-S1-IA-001"
    if requires_dispatch_id != expected_source:
        raise ValueError(
            f"semantic blocker must require the matching source lane {expected_source}"
        )
    if reason is not None and not isinstance(reason, str):
        raise ValueError("semantic blocker reason must be text")

    out = {
        "blocker_id": blocker_id,
        "kind": kind,
        "requires_dispatch_id": requires_dispatch_id,
    }
    if reason:
        out["reason"] = reason
    return out


def merge_blockers(*groups: list[dict[str, Any]]) -> list[dict[str, str]]:
    merged: dict[str, dict[str, str]] = {}
    for group in groups:
        for blocker in group:
            blocker_id = blocker.get("blocker_id")
            if not isinstance(blocker_id, str):
                raise ValueError("semantic blocker lacks blocker_id")
            normalized = dict(blocker)
            if blocker_id in merged:
                existing = merged[blocker_id]
                core = ("kind", "requires_dispatch_id")
                if any(existing.get(key) != normalized.get(key) for key in core):
                    raise ValueError(f"semantic blocker definition drift: {blocker_id}")
                if not existing.get("reason") and normalized.get("reason"):
                    existing["reason"] = normalized["reason"]
                continue
            merged[blocker_id] = normalized
    return [merged[key] for key in sorted(merged)]


def parse_declared_blockers(
    body: str,
    dispatch_id: str,
    disposition: str,
) -> list[dict[str, str]]:
    normalized_body = body.replace("\r\n", "\n")
    if BLOCKER_MARKER not in normalized_body:
        return []

    match = ERDOS_DISPATCH_RE.fullmatch(dispatch_id)
    if match is None or match.group(2) not in {"R1", "A1"}:
        raise ValueError("semantic blocker declarations are allowed only on ERDOS R1/A1 returns")
    if disposition not in ALLOWED_BLOCKER_DISPOSITIONS:
        raise ValueError(
            "semantic blocker declaration requires COUNTEREXAMPLE, SOURCE_INTERFACE_FOUND, or EXACT_BLOCKER"
        )

    problem = match.group(1)
    lines = normalized_body.splitlines()
    blockers: list[dict[str, str]] = []
    for index, line in enumerate(lines):
        if line != BLOCKER_MARKER:
            continue
        if index + 3 >= len(lines):
            raise ValueError("semantic blocker declaration is truncated")
        expected = ("blocker_id", "kind", "requires_dispatch_id")
        values: dict[str, str] = {}
        for offset, key in enumerate(expected, start=1):
            prefix = key + ": "
            row = lines[index + offset]
            if not row.startswith(prefix):
                raise ValueError(f"semantic blocker expected field {key}")
            value = row[len(prefix):].strip()
            if not value:
                raise ValueError(f"semantic blocker field {key} is empty")
            values[key] = value
        blockers.append(_normalize_blocker(values, problem))

    ids = [blocker["blocker_id"] for blocker in blockers]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate semantic blocker_id in RESULT/1")
    return blockers


def _load_policy(root: Path = ROOT) -> dict[str, Any]:
    path = root / POLICY_REL
    if not path.is_file():
        return {
            "schema_version": "1.0.0",
            "record_type": "GCL_ERDOS_SEMANTIC_GATE_POLICY",
            "rules": [],
        }
    data = _readj(path)
    if data.get("schema_version") != "1.0.0":
        raise ValueError("semantic gate policy schema drift")
    if data.get("record_type") != "GCL_ERDOS_SEMANTIC_GATE_POLICY":
        raise ValueError("semantic gate policy record type drift")
    rules = data.get("rules")
    if not isinstance(rules, list):
        raise ValueError("semantic gate policy rules must be a list")
    return data


def policy_blockers(
    dispatch_id: str,
    disposition: str,
    root: Path = ROOT,
) -> list[dict[str, str]]:
    problem = _problem_for_dispatch(dispatch_id)
    out: list[dict[str, str]] = []
    for rule in _load_policy(root).get("rules", []):
        if not isinstance(rule, dict) or rule.get("dispatch_id") != dispatch_id:
            continue
        triggers = rule.get("trigger_dispositions")
        blockers = rule.get("blockers")
        if not isinstance(triggers, list) or not all(isinstance(x, str) for x in triggers):
            raise ValueError(f"{dispatch_id}: semantic policy trigger list malformed")
        if not isinstance(blockers, list) or not all(isinstance(x, dict) for x in blockers):
            raise ValueError(f"{dispatch_id}: semantic policy blocker list malformed")
        if disposition in triggers:
            out.extend(_normalize_blocker(blocker, problem) for blocker in blockers)
    return merge_blockers(out)


def effective_blockers(
    receipt: dict[str, Any],
    root: Path = ROOT,
) -> list[dict[str, str]]:
    dispatch_id = receipt.get("dispatch_id")
    disposition = receipt.get("disposition_declared")
    if not isinstance(dispatch_id, str) or not isinstance(disposition, str):
        raise ValueError("receipt lacks dispatch/disposition for semantic gate evaluation")
    problem = _problem_for_dispatch(dispatch_id)

    declared_raw = receipt.get("semantic_blockers", [])
    if declared_raw is None:
        declared_raw = []
    if not isinstance(declared_raw, list):
        raise ValueError(f"{dispatch_id}: receipt semantic_blockers must be a list")
    declared = [
        _normalize_blocker(blocker, problem)
        for blocker in declared_raw
        if isinstance(blocker, dict)
    ]
    if len(declared) != len(declared_raw):
        raise ValueError(f"{dispatch_id}: malformed semantic blocker entry")

    return merge_blockers(declared, policy_blockers(dispatch_id, disposition, root))


def required_source_dispatches(blockers: list[dict[str, Any]]) -> list[str]:
    required = {
        blocker.get("requires_dispatch_id")
        for blocker in blockers
        if isinstance(blocker, dict)
    }
    if None in required or not all(isinstance(item, str) for item in required):
        raise ValueError("semantic blocker lacks source-audit dispatch")
    return sorted(required)
