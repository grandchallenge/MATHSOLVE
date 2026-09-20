from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "contributions" / "NS-CI-001" / "C2_MIX_DIRECTION_COMPRESSION_LEDGER_CHARGE"
PILOT = BASE / "PILOT.md"
TEMPLATE = BASE / "templates" / "INDEPENDENT_CONTRIBUTION_RECORD.md"
ICR_SCHEMA = BASE / "schemas" / "icr_metadata.schema.json"
RECEIPT_SCHEMA = BASE / "schemas" / "intake_receipt.schema.json"
HANDOFF = ROOT / "handoffs" / "NS-CI-001" / "C2_MIX_DIRECTION_COMPRESSION_LEDGER_CHARGE_ZERO_CONTEXT.md"
DISPATCH_DIR = BASE / "dispatches"
COHORT_DIR = BASE / "cohorts"

SHA40 = re.compile(r"^[0-9a-f]{40}$")
SHA64 = re.compile(r"^[0-9a-f]{64}$")

EXPECTED_AUTH_MERGE = "cacfe1f749b91a335e1d1734352cecff56bad7c1"
CONCURRENCY_MODES = {"independent_blind", "cooperative_claimed", "adversarial_replay"}
ASSIGNMENTS = {"A", "B", "C", "D", "E"}
COHORT_STATES = {"OPEN", "CLOSED_FOR_BLINDNESS", "SYNTHESIS_ALLOWED"}


def _read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def _enum(schema: dict[str, Any], field: str) -> set[str]:
    props = schema.get("properties")
    if not isinstance(props, dict) or field not in props:
        return set()
    value = props[field]
    if not isinstance(value, dict):
        return set()
    enum = value.get("enum", [])
    return {str(item) for item in enum} if isinstance(enum, list) else set()


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []

    base = root / BASE.relative_to(ROOT)
    pilot_path = root / PILOT.relative_to(ROOT)
    template_path = root / TEMPLATE.relative_to(ROOT)
    handoff_path = root / HANDOFF.relative_to(ROOT)
    icr_schema_path = root / ICR_SCHEMA.relative_to(ROOT)
    receipt_schema_path = root / RECEIPT_SCHEMA.relative_to(ROOT)
    dispatch_dir = root / DISPATCH_DIR.relative_to(ROOT)
    cohort_dir = root / COHORT_DIR.relative_to(ROOT)

    for path in (pilot_path, template_path, handoff_path, icr_schema_path, receipt_schema_path):
        if not path.is_file():
            errors.append(f"missing pilot artifact: {path.relative_to(root)}")
    if errors:
        return errors

    pilot = pilot_path.read_text(encoding="utf-8")
    for needle in (
        "AUTHORIZED_SETUP__DISPATCH_NOT_YET_ISSUED",
        EXPECTED_AUTH_MERGE,
        "independent_blind",
        "CLOSED_FOR_BLINDNESS",
        "Durability is mandatory. Repository access is not.",
        "Semantic duplication",
    ):
        if needle not in pilot:
            errors.append(f"pilot contract missing required clause: {needle}")

    template = template_path.read_text(encoding="utf-8")
    for needle in (
        "Independent Contribution Record",
        "Verification / falsification hooks",
        "This is evidence, not GCL adjudication.",
        "Repository access is not required.",
    ):
        if needle not in template:
            errors.append(f"ICR template missing required clause: {needle}")

    handoff = handoff_path.read_text(encoding="utf-8")
    for needle in (
        "Independent Contribution Record",
        "durable",
        "Repository access is not required",
        "22 minutes",
    ):
        if needle not in handoff:
            errors.append(f"zero-context handoff missing durable-return clause: {needle}")

    try:
        icr_schema = _read_json(icr_schema_path)
        receipt_schema = _read_json(receipt_schema_path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        errors.append(f"schema parse failure: {exc}")
        return errors

    if _enum(icr_schema, "concurrency_mode") != CONCURRENCY_MODES:
        errors.append("ICR schema concurrency modes differ from Council pilot contract")
    if _enum(icr_schema, "assignment_id") != ASSIGNMENTS:
        errors.append("ICR schema assignment set differs from sealed handoff")
    if _enum(icr_schema, "disposition") != {"PROVED", "REFUTED", "REDUCED", "BLOCKED"}:
        errors.append("ICR schema disposition vocabulary is invalid")
    if _enum(receipt_schema, "concurrency_mode") != CONCURRENCY_MODES:
        errors.append("receipt schema concurrency modes differ from Council pilot contract")
    forbidden_receipt_status = {"certified", "protected_incorporated", "council_approved", "human_steward_approved"}
    if _enum(receipt_schema, "handling_state") & forbidden_receipt_status:
        errors.append("receipt schema improperly confers protected or reserved authority")

    seen_dispatch: set[str] = set()
    if dispatch_dir.is_dir():
        for path in sorted(dispatch_dir.glob("*.json")):
            try:
                d = _read_json(path)
            except (OSError, ValueError, json.JSONDecodeError) as exc:
                errors.append(f"{path.relative_to(root)}: invalid dispatch JSON: {exc}")
                continue
            did = str(d.get("dispatch_id", ""))
            if not did:
                errors.append(f"{path.relative_to(root)}: missing dispatch_id")
            elif did in seen_dispatch:
                errors.append(f"duplicate dispatch_id: {did}")
            seen_dispatch.add(did)
            if d.get("schema_version") != "0.1-pilot":
                errors.append(f"{did}: unsupported dispatch schema_version")
            if d.get("assignment_id") not in ASSIGNMENTS:
                errors.append(f"{did}: invalid assignment_id")
            mode = d.get("concurrency_mode")
            if mode not in CONCURRENCY_MODES:
                errors.append(f"{did}: invalid concurrency_mode")
            if float(d.get("wall_clock_limit_minutes", 999)) > 22:
                errors.append(f"{did}: wall-clock limit exceeds 22 minutes")
            if not SHA40.fullmatch(str(d.get("source_handoff_commit_sha", ""))):
                errors.append(f"{did}: source handoff commit must be exact 40-hex SHA")
            if not SHA40.fullmatch(str(d.get("source_handoff_blob_sha", ""))):
                errors.append(f"{did}: source handoff blob must be exact 40-hex SHA")
            if not SHA64.fullmatch(str(d.get("source_handoff_sha256", ""))):
                errors.append(f"{did}: source handoff SHA-256 missing or malformed")
            if mode == "independent_blind" and not d.get("blind_cohort_id"):
                errors.append(f"{did}: independent_blind dispatch lacks blind_cohort_id")
            if d.get("canonical_mutation_authorized") is not False:
                errors.append(f"{did}: contributor canonical mutation must be false")
            if d.get("contributor_write_authority") not in {"none_required", "proposal_only_inbox"}:
                errors.append(f"{did}: invalid contributor_write_authority")

    if cohort_dir.is_dir():
        for path in sorted(cohort_dir.glob("*.json")):
            try:
                c = _read_json(path)
            except (OSError, ValueError, json.JSONDecodeError) as exc:
                errors.append(f"{path.relative_to(root)}: invalid cohort JSON: {exc}")
                continue
            cid = str(c.get("cohort_id", ""))
            if c.get("mode") != "independent_blind":
                errors.append(f"{cid}: pilot cohort must use independent_blind mode")
            if c.get("state") not in COHORT_STATES:
                errors.append(f"{cid}: invalid cohort state")
            members = c.get("dispatch_ids")
            if not isinstance(members, list) or len(members) < 2:
                errors.append(f"{cid}: blind cohort requires at least two dispatches")
            elif any(str(item) not in seen_dispatch for item in members):
                errors.append(f"{cid}: cohort references unknown dispatch")
            if c.get("cross_disclosure_before_closure") is not False:
                errors.append(f"{cid}: blind cohort must begin with cross-disclosure false")

    return errors


def main() -> int:
    try:
        errors = validate()
    except Exception as exc:  # fail closed for validation infrastructure
        print(f"validator failure: {exc}", file=sys.stderr)
        return 2
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("NS-CI independent contribution pilot validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
