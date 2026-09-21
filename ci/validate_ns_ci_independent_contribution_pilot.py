from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "contributions" / "NS-CI-001" / "C2_MIX_DIRECTION_COMPRESSION_LEDGER_CHARGE"
PILOT = BASE / "PILOT.md"
RESULT_SPEC = BASE / "RESULT_COMMENT_V1.md"
RECEIPT_SCHEMA = BASE / "schemas" / "intake_receipt.schema.json"
HANDOFF = ROOT / "handoffs" / "NS-CI-001" / "C2_MIX_DIRECTION_COMPRESSION_LEDGER_CHARGE_ZERO_CONTEXT.md"
DISPATCH_DIR = BASE / "dispatches"
COHORT_DIR = BASE / "cohorts"
WORKFLOW = ROOT / ".github" / "workflows" / "ns-ci-independent-contribution-intake.yml"
INTAKE_SCRIPT = ROOT / "ci" / "ns_ci_github_contribution_intake.py"

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


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


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
    result_spec = root / RESULT_SPEC.relative_to(ROOT)
    receipt_schema_path = root / RECEIPT_SCHEMA.relative_to(ROOT)
    handoff_path = root / HANDOFF.relative_to(ROOT)
    workflow_path = root / WORKFLOW.relative_to(ROOT)
    intake_script = root / INTAKE_SCRIPT.relative_to(ROOT)
    dispatch_dir = root / DISPATCH_DIR.relative_to(ROOT)
    cohort_dir = root / COHORT_DIR.relative_to(ROOT)

    required = (pilot_path, result_spec, receipt_schema_path, handoff_path, workflow_path, intake_script)
    for path in required:
        if not path.is_file():
            errors.append(f"missing pilot artifact: {path.relative_to(root)}")
    if errors:
        return errors

    superseded = (
        base / "templates" / "INDEPENDENT_CONTRIBUTION_RECORD.md",
        base / "schemas" / "icr_metadata.schema.json",
    )
    for path in superseded:
        if path.exists():
            errors.append(f"superseded free-form intake artifact still exists: {path.relative_to(root)}")

    pilot = pilot_path.read_text(encoding="utf-8")
    if EXPECTED_AUTH_MERGE not in pilot:
        errors.append("pilot contract lost Human Steward authorization binding")
    for needle in (
        "generated GitHub dispatch issue",
        "GCL-CONTRIBUTION-RESULT/1",
        "issue_comment_only",
        "no attachments",
    ):
        if needle not in pilot:
            errors.append(f"pilot contract missing GitHub-native clause: {needle}")

    result_text = result_spec.read_text(encoding="utf-8")
    for needle in (
        "GCL-CONTRIBUTION-RESULT/1",
        "## Strongest exact statement",
        "## Verification / falsification hooks",
        "No other level-2 headings are allowed",
        "attachments",
    ):
        if needle not in result_text:
            errors.append(f"RESULT/1 contract missing clause: {needle}")

    handoff = handoff_path.read_text(encoding="utf-8")
    for needle in (
        "GitHub-native contributor return",
        "READ ISSUE -> THINK -> POST ONE RESULT/1 COMMENT -> STOP",
        "No attachments, links, images",
    ):
        if needle not in handoff:
            errors.append(f"zero-context handoff missing GitHub-native return clause: {needle}")

    workflow = workflow_path.read_text(encoding="utf-8")
    for needle in (
        "issue_comment:",
        "contents: write",
        "pull-requests: write",
        "issues: write",
        "ci/ns_ci_github_contribution_intake.py",
        "group: ns-ci-contribution-intake-${{ github.event.issue.number }}",
        "Recover missing intake pull request",
        "INTAKE ALREADY ACCEPTED",
        "RAW EVIDENCE PR CREATED",
    ):
        if needle not in workflow:
            errors.append(f"intake workflow missing control: {needle}")
    for forbidden in (
        "pull_request_target:",
        "workflow_run:",
        "auto-merge",
        "gh pr merge",
        "group: ns-ci-contribution-intake-${{ github.event.comment.id }}",
    ):
        if forbidden in workflow:
            errors.append(f"intake workflow contains forbidden authority surface: {forbidden}")

    try:
        receipt_schema = _read_json(receipt_schema_path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        errors.append(f"receipt schema parse failure: {exc}")
        return errors

    props = receipt_schema.get("properties", {})
    if not isinstance(props, dict):
        errors.append("receipt schema properties missing")
    else:
        if "attachment_sha256" in props or "attachments" in props:
            errors.append("receipt schema still permits attachment metadata")
    if receipt_schema.get("properties", {}).get("schema_version", {}).get("const") != "0.2-pilot":
        errors.append("receipt schema is not GitHub intake v0.2")
    if receipt_schema.get("properties", {}).get("result_protocol", {}).get("const") != "GCL-CONTRIBUTION-RESULT/1":
        errors.append("receipt schema does not bind RESULT/1")

    seen_dispatch: set[str] = set()
    statuses: set[str] = set()
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
                continue
            if did in seen_dispatch:
                errors.append(f"duplicate dispatch_id: {did}")
            seen_dispatch.add(did)

            if d.get("schema_version") != "0.2-pilot":
                errors.append(f"{did}: dispatch schema must be 0.2-pilot")
            if d.get("assignment_id") not in ASSIGNMENTS:
                errors.append(f"{did}: invalid assignment_id")
            if d.get("concurrency_mode") not in CONCURRENCY_MODES:
                errors.append(f"{did}: invalid concurrency_mode")
            if d.get("return_protocol") != "GCL-CONTRIBUTION-RESULT/1":
                errors.append(f"{did}: invalid return_protocol")
            if d.get("contributor_write_authority") != "issue_comment_only":
                errors.append(f"{did}: contributor authority must be issue_comment_only")
            for field in ("canonical_mutation_authorized", "attachments_allowed", "external_urls_allowed", "supplementary_files_allowed"):
                if d.get(field) is not False:
                    errors.append(f"{did}: {field} must be false")
            if d.get("result_comment_count_expected") != 1:
                errors.append(f"{did}: exactly one result comment must be expected")
            if float(d.get("wall_clock_limit_minutes", 999)) > 22:
                errors.append(f"{did}: wall-clock limit exceeds 22 minutes")
            for field in ("source_handoff_commit_sha", "source_handoff_blob_sha"):
                if not SHA40.fullmatch(str(d.get(field, ""))):
                    errors.append(f"{did}: {field} must be exact 40-hex SHA")
            for field in ("source_handoff_sha256", "bootstrap_sha256"):
                if not SHA64.fullmatch(str(d.get(field, ""))):
                    errors.append(f"{did}: {field} missing or malformed")

            bootstrap = d.get("bootstrap_path")
            if not isinstance(bootstrap, str) or not bootstrap:
                errors.append(f"{did}: bootstrap_path missing")
            else:
                bpath = root / bootstrap
                if not bpath.is_file():
                    errors.append(f"{did}: bootstrap file missing")
                else:
                    btext = bpath.read_text(encoding="utf-8")
                    if _sha256(btext) != d.get("bootstrap_sha256"):
                        errors.append(f"{did}: bootstrap digest mismatch")
                    if not btext.startswith("GCL-CONTRIBUTION-DISPATCH/1\n"):
                        errors.append(f"{did}: bootstrap marker missing")
                    if f"Dispatch ID: `{did}`" not in btext:
                        errors.append(f"{did}: bootstrap does not state exact dispatch id")
                    if "Do not create branches, pull requests, files, commits, issues, notes, attachments" not in btext:
                        errors.append(f"{did}: bootstrap work-set is not narrow enough")
                    if "GCL-CONTRIBUTION-RESULT/1" not in btext:
                        errors.append(f"{did}: bootstrap lacks exact return grammar")

            status = str(d.get("dispatch_status", ""))
            statuses.add(status)
            issue_number = d.get("github_issue_number")
            if status == "PENDING_GITHUB_ISSUE_BINDING":
                if issue_number is not None or d.get("github_issue_url") is not None:
                    errors.append(f"{did}: pending dispatch already carries issue binding")
            elif status == "READY_FOR_GITHUB_COMMENT":
                if not isinstance(issue_number, int) or issue_number < 1:
                    errors.append(f"{did}: ready dispatch lacks issue number")
                if not isinstance(d.get("github_issue_url"), str) or not d.get("github_issue_url"):
                    errors.append(f"{did}: ready dispatch lacks issue URL")
            else:
                errors.append(f"{did}: invalid dispatch_status {status}")

    if "PILOT_RECONFIGURING__GITHUB_INTAKE_V1" in pilot:
        if statuses != {"PENDING_GITHUB_ISSUE_BINDING"}:
            errors.append("reconfiguring pilot requires all dispatches pending issue binding")
    elif "PILOT_ACTIVE__GITHUB_INTAKE_V1" in pilot:
        if statuses != {"READY_FOR_GITHUB_COMMENT"}:
            errors.append("active GitHub intake pilot requires all dispatches ready")
    else:
        errors.append("pilot state is neither reconfiguring nor active GitHub intake v1")

    if cohort_dir.is_dir():
        for path in sorted(cohort_dir.glob("*.json")):
            try:
                c = _read_json(path)
            except (OSError, ValueError, json.JSONDecodeError) as exc:
                errors.append(f"{path.relative_to(root)}: invalid cohort JSON: {exc}")
                continue
            cid = str(c.get("cohort_id", ""))
            if c.get("schema_version") != "0.2-pilot":
                errors.append(f"{cid}: cohort schema must be 0.2-pilot")
            if c.get("mode") != "independent_blind":
                errors.append(f"{cid}: pilot cohort must use independent_blind")
            if c.get("state") not in COHORT_STATES:
                errors.append(f"{cid}: invalid cohort state")
            if c.get("return_protocol") != "GCL-CONTRIBUTION-RESULT/1":
                errors.append(f"{cid}: cohort return protocol mismatch")
            if c.get("intake_channel") != "github_issue_comment":
                errors.append(f"{cid}: cohort intake channel mismatch")
            members = c.get("dispatch_ids")
            if not isinstance(members, list) or len(members) < 2:
                errors.append(f"{cid}: blind cohort requires at least two dispatches")
            elif any(str(item) not in seen_dispatch for item in members):
                errors.append(f"{cid}: cohort references unknown dispatch")
            if c.get("cross_disclosure_before_closure") is not False:
                errors.append(f"{cid}: blind cohort cross-disclosure must begin false")
            if c.get("synthesis_allowed") is not False:
                errors.append(f"{cid}: synthesis must remain false while cohort is open")

    return errors


def main() -> int:
    try:
        errors = validate()
    except Exception as exc:
        print(f"validator failure: {exc}", file=sys.stderr)
        return 2
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("NS-CI GitHub-native independent contribution pilot validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
