from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BASE_REL = Path("contributions/NS-CI-001/C2_MIX_DIRECTION_COMPRESSION_LEDGER_CHARGE")
DISPATCH_DIR_REL = BASE_REL / "dispatches"

MARKER = "GCL-CONTRIBUTION-RESULT/1"
DISPATCH_MARKER = "GCL-CONTRIBUTION-DISPATCH/1"
DISPATCH_ID_RE = re.compile(r"^NSCI-C2-[A-E]-(?:BLIND|COOP|ADV)-[0-9]{3}$")
URL_RE = re.compile(r"(?:https?://|www\.)", re.IGNORECASE)
MD_LINK_RE = re.compile(r"!?\[[^\]\n]*\]\([^\)\n]+\)")
HTML_LINK_RE = re.compile(r"<\s*(?:a|img)\b", re.IGNORECASE)
HEADING_RE = re.compile(r"^## .+$", re.MULTILINE)

SECTIONS = [
    "## Strongest exact statement",
    "## Derivation",
    "## Assumptions beyond bootstrap",
    "## Verification / falsification hooks",
    "## Claim boundary",
    "## Next residual",
]
DISPOSITIONS = {"PROVED", "REFUTED", "REDUCED", "BLOCKED"}
ASSIGNMENTS = {"A", "B", "C", "D", "E"}


class IntakeError(ValueError):
    pass


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _object(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise IntakeError(f"{label} must be a JSON object")
    return value


def parse_result_comment(body: str) -> dict[str, Any]:
    if not isinstance(body, str) or not body.strip():
        raise IntakeError("comment body is empty")
    if not body.startswith(MARKER + "\n"):
        raise IntakeError(f"comment must begin exactly with {MARKER}")

    forbidden: list[str] = []
    if URL_RE.search(body):
        forbidden.append("raw URL")
    if MD_LINK_RE.search(body):
        forbidden.append("Markdown link or image")
    if HTML_LINK_RE.search(body):
        forbidden.append("HTML link or image")
    if "github.com/user-attachments" in body.lower():
        forbidden.append("GitHub attachment")
    if forbidden:
        raise IntakeError("forbidden content: " + ", ".join(sorted(set(forbidden))))

    lines = body.splitlines()
    if len(lines) < 8:
        raise IntakeError("comment is too short")

    expected_keys = [
        "dispatch_id",
        "assignment",
        "disposition",
        "context_class",
        "external_sources",
        "timebox_observed",
    ]
    preamble: dict[str, str] = {}
    cursor = 1
    for key in expected_keys:
        if cursor >= len(lines):
            raise IntakeError(f"missing preamble field {key}")
        prefix = key + ": "
        line = lines[cursor]
        if not line.startswith(prefix):
            raise IntakeError(f"expected preamble field {key} at line {cursor + 1}")
        value = line[len(prefix):].strip()
        if not value:
            raise IntakeError(f"preamble field {key} is empty")
        preamble[key] = value
        cursor += 1
    if cursor >= len(lines) or lines[cursor] != "":
        raise IntakeError("preamble must be followed by one blank line")

    if not DISPATCH_ID_RE.fullmatch(preamble["dispatch_id"]):
        raise IntakeError("dispatch_id has invalid form")
    if preamble["assignment"] not in ASSIGNMENTS:
        raise IntakeError("assignment is invalid")
    if preamble["disposition"] not in DISPOSITIONS:
        raise IntakeError("disposition is invalid")
    if preamble["context_class"] != "ZERO_CONTEXT":
        raise IntakeError("context_class must be ZERO_CONTEXT for this pilot")
    if preamble["external_sources"] != "NONE":
        raise IntakeError("external_sources must be NONE for this pilot")
    if preamble["timebox_observed"] not in {"YES", "NO"}:
        raise IntakeError("timebox_observed must be YES or NO")

    headings = HEADING_RE.findall(body)
    if headings != SECTIONS:
        raise IntakeError("level-2 sections must match the RESULT/1 schema exactly and in order")

    sections: dict[str, str] = {}
    positions = [(body.index(h), h) for h in SECTIONS]
    for index, (start, heading) in enumerate(positions):
        content_start = start + len(heading)
        content_end = positions[index + 1][0] if index + 1 < len(positions) else len(body)
        content = body[content_start:content_end].strip()
        if not content:
            raise IntakeError(f"{heading} is empty")
        sections[heading[3:]] = content

    next_residual = sections["Next residual"]
    sentence_marks = len(re.findall(r"[.!?](?:\s|$)", next_residual))
    if sentence_marks > 3:
        raise IntakeError("Next residual exceeds three sentences")

    return {"preamble": preamble, "sections": sections}


def load_dispatch(root: Path, dispatch_id: str) -> dict[str, Any]:
    path = root / DISPATCH_DIR_REL / f"{dispatch_id}.json"
    if not path.is_file():
        raise IntakeError("dispatch_id is not registered on protected repository state")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise IntakeError(f"dispatch record is invalid JSON: {exc}") from exc
    return _object(data, "dispatch record")


def validate_dispatch_issue(root: Path, issue: dict[str, Any], dispatch: dict[str, Any]) -> None:
    if dispatch.get("schema_version") != "0.2-pilot":
        raise IntakeError("dispatch is not enabled for GitHub intake v1")
    if dispatch.get("return_protocol") != MARKER:
        raise IntakeError("dispatch return protocol is not RESULT/1")
    if dispatch.get("dispatch_status") != "READY_FOR_GITHUB_COMMENT":
        raise IntakeError("dispatch is not ready for GitHub comment intake")
    if dispatch.get("canonical_mutation_authorized") is not False:
        raise IntakeError("dispatch improperly authorizes canonical mutation")

    number = issue.get("number")
    if not isinstance(number, int) or number != dispatch.get("github_issue_number"):
        raise IntakeError("comment was posted to an issue not bound to this dispatch")

    title = issue.get("title")
    if title != dispatch.get("github_issue_title"):
        raise IntakeError("dispatch issue title does not match protected binding")

    body = issue.get("body")
    if not isinstance(body, str):
        raise IntakeError("dispatch issue body is unavailable")
    if not body.startswith(DISPATCH_MARKER + "\n"):
        raise IntakeError("dispatch issue is missing the dispatch marker")

    bootstrap_path = dispatch.get("bootstrap_path")
    if not isinstance(bootstrap_path, str) or not bootstrap_path:
        raise IntakeError("dispatch record lacks bootstrap_path")
    path = root / bootstrap_path
    if not path.is_file():
        raise IntakeError("protected bootstrap file is missing")
    protected = path.read_text(encoding="utf-8")
    if sha256_text(protected) != dispatch.get("bootstrap_sha256"):
        raise IntakeError("protected bootstrap digest does not match dispatch record")
    if body != protected:
        raise IntakeError("GitHub issue body differs from the protected bootstrap bytes")


def validate_event(event: dict[str, Any], root: Path) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    issue = _object(event.get("issue"), "issue")
    if "pull_request" in issue:
        raise IntakeError("result comments are accepted only on dispatch issues")
    comment = _object(event.get("comment"), "comment")
    body = comment.get("body")
    if not isinstance(body, str):
        raise IntakeError("comment body is unavailable")

    parsed = parse_result_comment(body)
    dispatch_id = parsed["preamble"]["dispatch_id"]
    dispatch = load_dispatch(root, dispatch_id)
    validate_dispatch_issue(root, issue, dispatch)

    if parsed["preamble"]["assignment"] != dispatch.get("assignment_id"):
        raise IntakeError("assignment does not match protected dispatch")
    if dispatch.get("concurrency_mode") not in {"independent_blind", "cooperative_claimed", "adversarial_replay"}:
        raise IntakeError("protected dispatch has invalid concurrency mode")

    user = _object(comment.get("user"), "comment user")
    login = user.get("login")
    if not isinstance(login, str) or not login:
        raise IntakeError("authenticated GitHub actor is unavailable")

    comment_id = comment.get("id")
    if not isinstance(comment_id, int):
        raise IntakeError("GitHub comment id is unavailable")

    return parsed, dispatch, {"issue": issue, "comment": comment, "actor": login, "comment_id": comment_id}


def emit_intake(event: dict[str, Any], root: Path, output: Path) -> dict[str, Any]:
    parsed, dispatch, observed = validate_event(event, root)
    body = observed["comment"]["body"]
    assert isinstance(body, str)

    dispatch_id = parsed["preamble"]["dispatch_id"]
    comment_id = observed["comment_id"]
    raw_rel = BASE_REL / "raw" / dispatch_id / f"github-comment-{comment_id}.md"
    receipt_rel = BASE_REL / "receipts" / dispatch_id / f"github-comment-{comment_id}.json"

    receipt = {
        "schema_version": "0.2-pilot",
        "receipt_id": f"{dispatch_id}:github-comment:{comment_id}",
        "dispatch_id": dispatch_id,
        "assignment_id": dispatch["assignment_id"],
        "concurrency_mode": dispatch["concurrency_mode"],
        "blind_cohort_id": dispatch.get("blind_cohort_id"),
        "result_protocol": MARKER,
        "github_issue_number": observed["issue"]["number"],
        "github_comment_id": comment_id,
        "authenticated_github_actor": observed["actor"],
        "comment_created_at": observed["comment"].get("created_at"),
        "raw_artifact_path": raw_rel.as_posix(),
        "raw_sha256": sha256_text(body),
        "bootstrap_path": dispatch["bootstrap_path"],
        "bootstrap_sha256": dispatch["bootstrap_sha256"],
        "source_handoff_commit_sha": dispatch["source_handoff_commit_sha"],
        "source_handoff_blob_sha": dispatch["source_handoff_blob_sha"],
        "source_handoff_sha256": dispatch["source_handoff_sha256"],
        "disposition_declared": parsed["preamble"]["disposition"],
        "context_class_declared": parsed["preamble"]["context_class"],
        "external_sources_declared": parsed["preamble"]["external_sources"],
        "timebox_observed_declared": parsed["preamble"]["timebox_observed"],
        "schema_result": "valid",
        "freshness": "current_for_dispatch",
        "security_state": "narrative_only_no_links_no_attachments",
        "handling_state": "received_unadjudicated",
        "mathematical_correctness_adjudicated": False,
        "independence_strength_adjudicated": False,
        "canonical_claim_effect": False,
        "recorded_by": "github-actions:ns-ci-independent-contribution-intake",
    }

    output.mkdir(parents=True, exist_ok=True)
    raw_out = output / "RAW.md"
    receipt_out = output / "RECEIPT.json"
    meta_out = output / "META.json"
    raw_out.write_text(body, encoding="utf-8")
    receipt_out.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    meta = {
        "dispatch_id": dispatch_id,
        "comment_id": comment_id,
        "issue_number": observed["issue"]["number"],
        "raw_repo_path": raw_rel.as_posix(),
        "receipt_repo_path": receipt_rel.as_posix(),
        "branch": f"intake/{dispatch_id.lower()}",
        "pr_title": f"NS-CI intake: {dispatch_id}",
    }
    meta_out.write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return meta


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--event", type=Path, required=True)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        event = json.loads(args.event.read_text(encoding="utf-8"))
        event = _object(event, "event")
        meta = emit_intake(event, args.repo_root, args.output)
    except (OSError, json.JSONDecodeError, IntakeError) as exc:
        args.output.mkdir(parents=True, exist_ok=True)
        (args.output / "ERRORS.txt").write_text(str(exc) + "\n", encoding="utf-8")
        print(f"INTAKE_INVALID: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(meta, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
