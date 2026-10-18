from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BASE_REL = Path("work_packages/GCL_ERDOS3")
DISPATCH_DIR_REL = BASE_REL / "dispatches"
MARKER = "GCL-CONTRIBUTION-RESULT/1"
DISPATCH_MARKER = "GCL-CONTRIBUTION-DISPATCH/1"
LEASE_ACTIVATION_MARKER = "GCL-LEASE-ACTIVATION/1"
DISPATCH_RE = re.compile(r"^GCL-ERDOS3-E3-[A-Z0-9]+-IA-\d{3}$")

PREAMBLE_KEYS = (
    "dispatch_id",
    "assignment",
    "agent_ref",
    "disposition",
    "context_class",
    "external_sources",
)
LEASE_PREAMBLE_KEYS = PREAMBLE_KEYS + (
    "lease_epoch",
    "agent_elapsed_minutes",
)


class IntakeError(ValueError):
    pass


def _obj(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise IntakeError(f"{label} must be an object")
    return value


def git_blob_sha1_text(text: str) -> str:
    data = text.encode("utf-8")
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def parse_result_comment(body: str, allowed_dispositions: set[str], required_sections: list[str], preamble_keys: tuple[str, ...] = PREAMBLE_KEYS) -> dict[str, Any]:
    if not isinstance(body, str) or not body.startswith(MARKER + "\n"):
        raise IntakeError(f"comment must begin exactly with {MARKER}")

    lines = body.splitlines()
    preamble: dict[str, str] = {}
    cursor = 1
    for key in preamble_keys:
        prefix = key + ": "
        if cursor >= len(lines) or not lines[cursor].startswith(prefix):
            raise IntakeError(f"expected preamble field {key}")
        value = lines[cursor][len(prefix):].strip()
        if not value:
            raise IntakeError(f"preamble field {key} is empty")
        preamble[key] = value
        cursor += 1
    if cursor >= len(lines) or lines[cursor] != "":
        raise IntakeError("preamble must be followed by one blank line")

    if not DISPATCH_RE.fullmatch(preamble["dispatch_id"]):
        raise IntakeError("dispatch_id has invalid form")
    if preamble["disposition"] not in allowed_dispositions:
        raise IntakeError("disposition is not permitted by the protected dispatch")
    if preamble["context_class"] != "ZERO_CONTEXT":
        raise IntakeError("context_class must be ZERO_CONTEXT")

    headings = re.findall(r"^## (.+)$", body, flags=re.MULTILINE)
    positions: list[int] = []
    last = -1
    for section in required_sections:
        matches = [i for i, heading in enumerate(headings) if heading == section]
        if len(matches) != 1:
            raise IntakeError(f"required section must appear exactly once: {section}")
        idx = matches[0]
        if idx <= last:
            raise IntakeError("required sections are out of order")
        last = idx
        heading = "## " + section
        positions.append(body.index(heading))

    for i, section in enumerate(required_sections):
        heading = "## " + section
        start = positions[i] + len(heading)
        end = positions[i + 1] if i + 1 < len(positions) else len(body)
        if not body[start:end].strip():
            raise IntakeError(f"required section is empty: {section}")

    residual_start = body.index("## Next residual") + len("## Next residual")
    sources_start = body.index("## Sources")
    residual = body[residual_start:sources_start].strip()
    sentence_count = len(re.findall(r"[.!?](?:\s|$)", residual))
    if sentence_count > 3:
        raise IntakeError("Next residual exceeds three sentences")

    return {"preamble": preamble, "headings": headings}


def load_dispatch(root: Path, dispatch_id: str) -> dict[str, Any]:
    path = root / DISPATCH_DIR_REL / f"{dispatch_id}.json"
    if not path.is_file():
        raise IntakeError("dispatch_id is not registered on protected main")
    try:
        return _obj(json.loads(path.read_text(encoding="utf-8")), "dispatch")
    except json.JSONDecodeError as exc:
        raise IntakeError(f"dispatch record is invalid JSON: {exc}") from exc


def _parse_utc(value: Any, label: str) -> datetime:
    if not isinstance(value, str) or not value.endswith("Z"):
        raise IntakeError(f"{label} must be an RFC3339 UTC timestamp")
    try:
        dt = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError as exc:
        raise IntakeError(f"{label} is invalid") from exc
    return dt.astimezone(timezone.utc)


def parse_activation_marker(body: Any) -> dict[str, str] | None:
    if not isinstance(body, str) or not body.startswith(LEASE_ACTIVATION_MARKER + "\n"):
        return None
    lines = body.splitlines()
    expected = ("dispatch_id", "assignment", "lease_epoch", "lease_duration_minutes", "agent_max_execution_minutes")
    if len(lines) != 1 + len(expected):
        raise IntakeError("activation marker has unexpected shape")
    out: dict[str, str] = {}
    for i, key in enumerate(expected, start=1):
        prefix = key + ": "
        if not lines[i].startswith(prefix):
            raise IntakeError(f"activation marker expected field {key}")
        value = lines[i][len(prefix):].strip()
        if not value:
            raise IntakeError(f"activation marker field {key} is empty")
        out[key] = value
    return out


def find_activation_marker(issue_comments: list[dict[str, Any]], dispatch: dict[str, Any]) -> dict[str, Any]:
    matches: list[dict[str, Any]] = []
    for row in issue_comments:
        parsed = parse_activation_marker(row.get("body"))
        if parsed is None:
            continue
        if (
            parsed.get("dispatch_id") == dispatch.get("dispatch_id")
            and parsed.get("assignment") == dispatch.get("assignment_id")
            and parsed.get("lease_epoch") == str(dispatch.get("lease_epoch"))
        ):
            matches.append({"comment": row, "parsed": parsed})
    if len(matches) != 1:
        raise IntakeError("expected exactly one matching lease activation marker")
    match = matches[0]
    parsed = match["parsed"]
    if parsed.get("lease_duration_minutes") != "25":
        raise IntakeError("activation marker lease duration drift")
    if parsed.get("agent_max_execution_minutes") != "24":
        raise IntakeError("activation marker agent cap drift")
    marker_comment = match["comment"]
    if not isinstance(marker_comment.get("id"), int):
        raise IntakeError("activation marker comment id unavailable")
    _parse_utc(marker_comment.get("created_at"), "activation_marker.created_at")
    return match


def validate_lease_freshness(
    dispatch: dict[str, Any],
    comment: dict[str, Any],
    parsed: dict[str, Any],
    issue_comments: list[dict[str, Any]],
) -> dict[str, Any] | None:
    policy_id = dispatch.get("lease_policy_id")
    if policy_id is None:
        return None
    if policy_id != "GCL-IA-LEASE-25M-24M-001":
        raise IntakeError("unsupported lease policy")
    if dispatch.get("lease_duration_minutes") != 25:
        raise IntakeError("lease duration drift")
    if dispatch.get("agent_max_execution_minutes") != 24:
        raise IntakeError("agent execution cap drift")
    if dispatch.get("return_grace_minutes") != 1:
        raise IntakeError("return grace drift")
    if dispatch.get("lease_clock_source") != "GITHUB_ACTIVATION_COMMENT":
        raise IntakeError("lease clock source drift")
    if dispatch.get("state") != "DISPATCHED__AWAITING_RETURN":
        raise IntakeError("lease is not active")
    if dispatch.get("dispatch_status") != "READY_FOR_GITHUB_COMMENT":
        raise IntakeError("dispatch is not intake-ready")

    activation = find_activation_marker(issue_comments, dispatch)
    marker_comment = activation["comment"]
    start = _parse_utc(marker_comment.get("created_at"), "activation_marker.created_at")
    expiry = start + timedelta(minutes=25)
    created = _parse_utc(comment.get("created_at"), "comment.created_at")
    if created < start:
        raise IntakeError("result predates lease activation")
    if created > expiry:
        raise IntakeError("lease expired before result comment")

    pre = parsed["preamble"]
    try:
        epoch = int(pre.get("lease_epoch", ""))
        elapsed = int(pre.get("agent_elapsed_minutes", ""))
    except ValueError as exc:
        raise IntakeError("lease_epoch and agent_elapsed_minutes must be integers") from exc
    if epoch != dispatch.get("lease_epoch"):
        raise IntakeError("stale or mismatched lease epoch")
    if elapsed < 0 or elapsed > 24:
        raise IntakeError("agent_elapsed_minutes exceeds 24-minute cap")
    return {
        "activation_comment_id": marker_comment["id"],
        "lease_started_at": start.isoformat().replace("+00:00", "Z"),
        "lease_expires_at": expiry.isoformat().replace("+00:00", "Z"),
    }


def validate_dispatch_integrity(root: Path, dispatch: dict[str, Any], issue: dict[str, Any]) -> None:
    if dispatch.get("schema_version") != "1.0.0":
        raise IntakeError("unsupported dispatch schema")
    if dispatch.get("campaign") != "GCL-ERDOS3":
        raise IntakeError("campaign mismatch")
    if dispatch.get("dispatch_status") != "READY_FOR_GITHUB_COMMENT":
        raise IntakeError("dispatch is not ready for automated intake")
    if dispatch.get("state") != "DISPATCHED__AWAITING_RETURN":
        raise IntakeError("dispatch lifecycle is not awaiting a return")
    if dispatch.get("return_protocol") != MARKER:
        raise IntakeError("dispatch return protocol mismatch")
    if dispatch.get("canonical_mutation_authorized") is not False:
        raise IntakeError("dispatch improperly authorizes canonical mutation")
    if dispatch.get("automated_intake_canonical_effect") is not False:
        raise IntakeError("automated intake canonical-effect guard is absent")
    if dispatch.get("first_valid_result_lock") is not True:
        raise IntakeError("first-valid-result lock is not enabled")
    if dispatch.get("concurrency_mode") != "independent_blind":
        raise IntakeError("unsupported concurrency mode")

    if issue.get("number") != dispatch.get("github_issue_number"):
        raise IntakeError("comment posted to wrong issue")
    if issue.get("title") != dispatch.get("github_issue_title"):
        raise IntakeError("issue title differs from protected dispatch binding")

    issue_body = issue.get("body")
    if not isinstance(issue_body, str) or not issue_body.startswith(DISPATCH_MARKER + "\n"):
        raise IntakeError("issue body lacks dispatch marker")
    bootstrap_path = root / str(dispatch.get("bootstrap_path", ""))
    if not bootstrap_path.is_file():
        raise IntakeError("protected bootstrap is missing")
    protected_bootstrap = bootstrap_path.read_text(encoding="utf-8")
    if git_blob_sha1_text(protected_bootstrap) != dispatch.get("bootstrap_blob_sha1"):
        raise IntakeError("protected bootstrap blob mismatch")
    if issue_body != protected_bootstrap:
        raise IntakeError("issue body differs from protected bootstrap bytes")

    task_path = root / str(dispatch.get("task_path", ""))
    if not task_path.is_file():
        raise IntakeError("protected task file is missing on main")
    if git_blob_sha1_text(task_path.read_text(encoding="utf-8")) != dispatch.get("task_blob_sha1"):
        raise IntakeError("protected task bytes drifted from dispatch task blob")


def validate_event(event: dict[str, Any], root: Path, issue_comments: list[dict[str, Any]] | None = None) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    issue = _obj(event.get("issue"), "issue")
    if "pull_request" in issue:
        raise IntakeError("results are accepted only on dispatch issues")
    comment = _obj(event.get("comment"), "comment")
    body = comment.get("body")
    if not isinstance(body, str):
        raise IntakeError("comment body unavailable")

    # Parse dispatch id first, then apply dispatch-specific schema.
    if not body.startswith(MARKER + "\n"):
        raise IntakeError(f"comment must begin exactly with {MARKER}")
    lines = body.splitlines()
    if len(lines) < 2 or not lines[1].startswith("dispatch_id: "):
        raise IntakeError("dispatch_id is missing from RESULT/1 preamble")
    dispatch_id = lines[1][len("dispatch_id: "):].strip()
    if not DISPATCH_RE.fullmatch(dispatch_id):
        raise IntakeError("dispatch_id has invalid form")

    dispatch = load_dispatch(root, dispatch_id)
    allowed = dispatch.get("allowed_dispositions")
    sections = dispatch.get("required_sections")
    if not isinstance(allowed, list) or not allowed or not all(isinstance(x, str) for x in allowed):
        raise IntakeError("protected dispatch lacks allowed_dispositions")
    if not isinstance(sections, list) or not sections or not all(isinstance(x, str) for x in sections):
        raise IntakeError("protected dispatch lacks required_sections")

    preamble_keys = LEASE_PREAMBLE_KEYS if dispatch.get("lease_policy_id") else PREAMBLE_KEYS
    parsed = parse_result_comment(body, set(allowed), sections, preamble_keys)
    validate_dispatch_integrity(root, dispatch, issue)
    lease = validate_lease_freshness(dispatch, comment, parsed, issue_comments or [])

    pre = parsed["preamble"]
    if pre["dispatch_id"] != dispatch.get("dispatch_id"):
        raise IntakeError("dispatch identity mismatch")
    if pre["assignment"] != dispatch.get("assignment_id"):
        raise IntakeError("assignment mismatch")
    if pre["agent_ref"] != dispatch.get("agent_ref"):
        raise IntakeError("agent_ref mismatch")
    if pre["external_sources"] != dispatch.get("external_sources"):
        raise IntakeError("external_sources policy mismatch")

    actor = _obj(comment.get("user"), "comment user").get("login")
    comment_id = comment.get("id")
    if not isinstance(actor, str) or not actor:
        raise IntakeError("authenticated GitHub actor unavailable")
    if not isinstance(comment_id, int):
        raise IntakeError("GitHub comment id unavailable")

    return parsed, dispatch, {
        "issue": issue,
        "comment": comment,
        "actor": actor,
        "comment_id": comment_id,
        "lease": lease,
    }


def emit_intake(event: dict[str, Any], root: Path, output: Path, issue_comments: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    parsed, dispatch, observed = validate_event(event, root, issue_comments)
    body = observed["comment"]["body"]
    assert isinstance(body, str)

    dispatch_id = parsed["preamble"]["dispatch_id"]
    comment_id = observed["comment_id"]
    raw_rel = BASE_REL / "intake" / dispatch_id / f"github-comment-{comment_id}.md"
    receipt_rel = BASE_REL / "intake" / dispatch_id / f"github-comment-{comment_id}.json"

    receipt = {
        "schema_version": "1.0.0",
        "record_type": "GCL_ERDOS3_EXTERNAL_RESULT_RECEIPT",
        "campaign": "GCL-ERDOS3",
        "dispatch_id": dispatch_id,
        "assignment_id": dispatch["assignment_id"],
        "agent_ref": dispatch["agent_ref"],
        "concurrency_mode": dispatch["concurrency_mode"],
        "github_issue_number": observed["issue"]["number"],
        "github_comment_id": comment_id,
        "authenticated_github_actor": observed["actor"],
        "comment_created_at": observed["comment"].get("created_at"),
        "raw_artifact_path": raw_rel.as_posix(),
        "raw_sha256": sha256_text(body),
        "task_commit": dispatch["task_commit"],
        "task_path": dispatch["task_path"],
        "task_blob_sha1": dispatch["task_blob_sha1"],
        "bootstrap_path": dispatch["bootstrap_path"],
        "bootstrap_blob_sha1": dispatch["bootstrap_blob_sha1"],
        "disposition_declared": parsed["preamble"]["disposition"],
        "context_class_declared": parsed["preamble"]["context_class"],
        "external_sources_declared": parsed["preamble"]["external_sources"],
        "handling_state": "RECEIVED_UNADJUDICATED",
        "mathematical_correctness_adjudicated": False,
        "canonical_claim_effect": False,
        "frontier_effect": False,
        "certification_effect": False,
        "lease_policy_id": dispatch.get("lease_policy_id"),
        "lease_epoch": dispatch.get("lease_epoch"),
        "lease_activation_comment_id": (observed.get("lease") or {}).get("activation_comment_id"),
        "lease_started_at": (observed.get("lease") or {}).get("lease_started_at"),
        "lease_expires_at": (observed.get("lease") or {}).get("lease_expires_at"),
        "agent_elapsed_minutes_declared": parsed["preamble"].get("agent_elapsed_minutes"),
        "recorded_by": "github-actions:gcl-erdos3-controlled-intake",
    }

    output.mkdir(parents=True, exist_ok=True)
    (output / "RAW.md").write_text(body, encoding="utf-8")
    (output / "RECEIPT.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    meta = {
        "dispatch_id": dispatch_id,
        "comment_id": comment_id,
        "issue_number": observed["issue"]["number"],
        "raw_repo_path": raw_rel.as_posix(),
        "receipt_repo_path": receipt_rel.as_posix(),
        "branch": f"intake/{dispatch_id.lower()}",
        "pr_title": f"GCL-ERDOS3 intake: {dispatch_id}",
    }
    (output / "META.json").write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return meta


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--event", type=Path, required=True)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--issue-comments", type=Path)
    args = parser.parse_args()
    try:
        event = _obj(json.loads(args.event.read_text(encoding="utf-8")), "event")
        issue_comments: list[dict[str, Any]] = []
        if args.issue_comments is not None:
            raw_comments = json.loads(args.issue_comments.read_text(encoding="utf-8"))
            if not isinstance(raw_comments, list):
                raise IntakeError("issue comments payload must be a list")
            issue_comments = [_obj(x, "issue comment") for x in raw_comments]
        meta = emit_intake(event, args.repo_root, args.output, issue_comments)
    except (OSError, json.JSONDecodeError, IntakeError) as exc:
        args.output.mkdir(parents=True, exist_ok=True)
        (args.output / "ERRORS.txt").write_text(str(exc) + "\n", encoding="utf-8")
        print(f"INTAKE_INVALID: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(meta, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
