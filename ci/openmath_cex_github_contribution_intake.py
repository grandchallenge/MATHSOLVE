from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONTRIBUTIONS_ROOT_REL = Path("contributions/OPENMATH-2026")

MARKER = "GCL-CONTRIBUTION-RESULT/1"
DISPATCH_MARKER = "GCL-CONTRIBUTION-DISPATCH/1"
TOKEN_RE = re.compile(r"^[A-Z0-9][A-Z0-9._-]{2,127}$")
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
EXTERNAL_SOURCE_CLASSES = {"PROTECTED_PACKET_ONLY", "ADDITIONAL_PUBLIC_SOURCES"}


class IntakeError(ValueError):
    pass


def unwrap_return(body: str) -> tuple[str, dict[str, str] | None]:
    """Extract RESULT/1 without stripping or rewriting its bytes."""
    if not body.startswith("GCL-RETURN-RELAY/1\n"):
        return body, None
    pattern = (r"\AGCL-RETURN-RELAY/1\nDISPATCH_ID: ([A-Z0-9._-]+)\n"
               r"AGENT_REF: ([A-Z0-9._-]+)\n"
               r"INTENDED_RETURN: (https://github\.com/grandchallenge/MATHSOLVE/issues/[1-9][0-9]*)\n"
               r"\nBEGIN_RESULT\n(.*)\nEND_RESULT\n?\Z")
    match = re.fullmatch(pattern, body, re.DOTALL)
    if not match:
        raise IntakeError("relay envelope must match GCL-RETURN-RELAY/1 exactly")
    dispatch_id, agent_ref, intended_return, inner = match.groups()
    if "\nBEGIN_RESULT\n" in inner or "\nEND_RESULT" in inner:
        raise IntakeError("nested or ambiguous relay delimiters")
    parsed = parse_result_comment(inner)
    if (parsed["preamble"]["dispatch_id"] != dispatch_id or
            parsed["preamble"]["agent_ref"] != agent_ref):
        raise IntakeError("relay identity differs from inner RESULT/1")
    return inner, {"dispatch_id": dispatch_id, "agent_ref": agent_ref,
                   "intended_return": intended_return,
                   "envelope_sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
                   "inner_result_sha256": hashlib.sha256(inner.encode("utf-8")).hexdigest(),
                   "normalization": "NONE; delimiter framing excluded from inner result"}


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
    expected_keys = [
        "dispatch_id",
        "agent_ref",
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

    for key in ("dispatch_id", "agent_ref", "assignment", "disposition"):
        if not TOKEN_RE.fullmatch(preamble[key]):
            raise IntakeError(f"{key} has invalid form")
    if preamble["context_class"] != "ZERO_CONTEXT":
        raise IntakeError("context_class must be ZERO_CONTEXT")
    if preamble["external_sources"] not in EXTERNAL_SOURCE_CLASSES:
        raise IntakeError("external_sources class is invalid")
    if preamble["timebox_observed"] not in {"YES", "NO"}:
        raise IntakeError("timebox_observed must be YES or NO")

    headings = HEADING_RE.findall(body)
    if headings != SECTIONS:
        raise IntakeError("level-2 sections must match RESULT/1 schema exactly and in order")

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
    if len(re.findall(r"[.!?](?:\s|$)", next_residual)) > 3:
        raise IntakeError("Next residual exceeds three sentences")

    return {"preamble": preamble, "sections": sections}


def load_dispatch(root: Path, dispatch_id: str) -> tuple[dict[str, Any], Path]:
    base = root / CONTRIBUTIONS_ROOT_REL
    if not base.is_dir():
        raise IntakeError("OPENMATH contribution root is missing")
    matches = list(base.glob(f"**/dispatches/{dispatch_id}.json"))
    if not matches:
        raise IntakeError("dispatch_id is not registered on protected repository state")
    if len(matches) != 1:
        raise IntakeError("dispatch_id is ambiguous on protected repository state")
    path = matches[0]
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise IntakeError(f"dispatch record is invalid JSON: {exc}") from exc
    return _object(data, "dispatch record"), path


def load_operation(root: Path, dispatch: dict[str, Any]) -> dict[str, Any]:
    rel = dispatch.get("operation_contract")
    if not isinstance(rel, str) or not rel:
        raise IntakeError("dispatch record lacks operation_contract")
    path = root / rel
    if not path.is_file():
        raise IntakeError("protected operation contract is missing")
    try:
        operation = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise IntakeError(f"operation contract is invalid JSON: {exc}") from exc
    return _object(operation, "operation contract")


def _normalize_single_terminal_lf(value: str) -> str:
    """Ignore at most one transport-added terminal LF; preserve all other bytes."""
    return value[:-1] if value.endswith("\n") else value


def validate_dispatch_issue(
    root: Path,
    issue: dict[str, Any],
    dispatch: dict[str, Any],
    operation: dict[str, Any],
) -> None:
    if dispatch.get("schema_version") != "1.0.0":
        raise IntakeError("dispatch schema is not enabled for this intake")
    if dispatch.get("return_protocol") != MARKER:
        raise IntakeError("dispatch return protocol is not RESULT/1")
    if dispatch.get("dispatch_status") != "READY_FOR_GITHUB_COMMENT":
        raise IntakeError("dispatch is not ready for GitHub comment intake")
    if dispatch.get("canonical_mutation_authorized") is not False:
        raise IntakeError("dispatch improperly authorizes canonical mutation")
    if dispatch.get("dispatch_id") != operation.get("dispatch_id"):
        raise IntakeError("dispatch and operation IDs differ")
    if dispatch.get("assignment_id") != operation.get("assignment_id"):
        raise IntakeError("dispatch and operation assignments differ")
    if dispatch.get("agent_ref") != operation.get("agent_ref"):
        raise IntakeError("dispatch and operation agent identities differ")

    number = issue.get("number")
    if not isinstance(number, int) or number != dispatch.get("github_issue_number"):
        raise IntakeError("comment was posted to an issue not bound to this dispatch")
    if issue.get("title") != dispatch.get("github_issue_title"):
        raise IntakeError("dispatch issue title does not match protected binding")

    body = issue.get("body")
    if not isinstance(body, str) or not body.startswith(DISPATCH_MARKER + "\n"):
        raise IntakeError("dispatch issue is missing the dispatch marker")

    bootstrap_path = dispatch.get("bootstrap_path")
    if not isinstance(bootstrap_path, str) or not bootstrap_path:
        raise IntakeError("dispatch record lacks bootstrap_path")
    path = root / bootstrap_path
    if not path.is_file():
        raise IntakeError("protected bootstrap file is missing")
    protected = path.read_text(encoding="utf-8")
    normalized_body = _normalize_single_terminal_lf(body)
    normalized_protected = _normalize_single_terminal_lf(protected)
    if normalized_body != normalized_protected:
        raise IntakeError("GitHub issue body differs from protected bootstrap bytes")


def validate_event(
    event: dict[str, Any], root: Path
) -> tuple[dict[str, Any], dict[str, Any], Path, dict[str, Any], dict[str, Any]]:
    issue = _object(event.get("issue"), "issue")
    if "pull_request" in issue:
        raise IntakeError("result comments are accepted only on dispatch issues")
    comment = _object(event.get("comment"), "comment")
    body = comment.get("body")
    if not isinstance(body, str):
        raise IntakeError("comment body is unavailable")

    inner, relay = unwrap_return(body)
    parsed = parse_result_comment(inner)
    dispatch_id = parsed["preamble"]["dispatch_id"]
    dispatch, dispatch_path = load_dispatch(root, dispatch_id)
    operation = load_operation(root, dispatch)
    validate_dispatch_issue(root, issue, dispatch, operation)

    if relay is not None and relay["intended_return"] != dispatch.get("github_issue_url"):
        raise IntakeError("relay intended return differs from protected dispatch issue")

    if parsed["preamble"]["assignment"] != dispatch.get("assignment_id"):
        raise IntakeError("assignment does not match protected dispatch")
    if parsed["preamble"]["agent_ref"] != dispatch.get("agent_ref"):
        raise IntakeError("agent_ref does not match protected dispatch")
    if dispatch.get("concurrency_mode") != "independent_blind":
        raise IntakeError("protected dispatch concurrency mode mismatch")

    if dispatch.get("protected_lease_required"):
        registry_path = root / ".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        matches = [x for x in registry["assignments"] if x.get("assignment_id") == dispatch["assignment_id"]]
        if len(matches) != 1:
            raise IntakeError("dispatch must have exactly one protected assignment")
        item = matches[0]
        lease = item.get("lease", {})
        if item.get("state") not in {"LEASED_NOT_LAUNCHED", "LAUNCHED", "RETURNED", "CAPTURED", "ADJUDICATING"}:
            # A repeated wake for the same already-captured first comment is idempotent.
            base = dispatch_path.parent.parent
            captured = base / "raw" / dispatch_id / f"github-comment-{comment.get('id')}.md"
            if item.get("state") != "ACCEPTED" or not captured.is_file() or captured.read_text(encoding="utf-8") != inner:
                raise IntakeError("protected lease is closed or superseded")
        elif lease.get("state") != "LEASED" or lease.get("execution_authorized") is not True:
            raise IntakeError("protected lease is not executable")
        if lease.get("dispatch_id") != dispatch_id or lease.get("agent_ref") != dispatch.get("agent_ref"):
            raise IntakeError("protected lease identity mismatch")
        if lease.get("return_url") != dispatch.get("github_issue_url"):
            raise IntakeError("protected lease return issue mismatch")

    dispositions = operation.get("acceptable_dispositions")
    if not isinstance(dispositions, list) or not all(isinstance(x, str) and x for x in dispositions):
        raise IntakeError("operation lacks acceptable_dispositions")
    if parsed["preamble"]["disposition"] not in dispositions:
        raise IntakeError("disposition is not allowed by protected operation")

    user = _object(comment.get("user"), "comment user")
    login = user.get("login")
    if not isinstance(login, str) or not login:
        raise IntakeError("authenticated GitHub actor is unavailable")
    comment_id = comment.get("id")
    if not isinstance(comment_id, int):
        raise IntakeError("GitHub comment id is unavailable")

    observed = {"issue": issue, "comment": comment, "actor": login, "comment_id": comment_id,
                "inner_result": inner, "relay": relay}
    return parsed, dispatch, dispatch_path, operation, observed


def emit_intake(event: dict[str, Any], root: Path, output: Path) -> dict[str, Any]:
    parsed, dispatch, dispatch_path, operation, observed = validate_event(event, root)
    body = observed["inner_result"]
    assert isinstance(body, str)

    try:
        base_rel = dispatch_path.parent.parent.relative_to(root)
    except ValueError as exc:
        raise IntakeError("dispatch record is outside repository root") from exc

    dispatch_id = parsed["preamble"]["dispatch_id"]
    comment_id = observed["comment_id"]
    raw_rel = base_rel / "raw" / dispatch_id / f"github-comment-{comment_id}.md"
    receipt_rel = base_rel / "receipts" / dispatch_id / f"github-comment-{comment_id}.json"

    receipt = {
        "schema_version": "1.0.0",
        "receipt_id": f"{dispatch_id}:github-comment:{comment_id}",
        "dispatch_id": dispatch_id,
        "assignment_id": dispatch["assignment_id"],
        "agent_ref": dispatch["agent_ref"],
        "concurrency_mode": dispatch["concurrency_mode"],
        "result_protocol": MARKER,
        "github_issue_number": observed["issue"]["number"],
        "github_comment_id": comment_id,
        "authenticated_github_actor": observed["actor"],
        "comment_created_at": observed["comment"].get("created_at"),
        "raw_artifact_path": raw_rel.as_posix(),
        "dispatch_record_path": dispatch_path.relative_to(root).as_posix(),
        "bootstrap_path": dispatch["bootstrap_path"],
        "bootstrap_blob_sha1": dispatch["bootstrap_blob_sha1"],
        "source_handoff_commit_sha": dispatch["source_handoff_commit_sha"],
        "operation_contract": dispatch["operation_contract"],
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
        "recorded_by": "github-actions:openmath-cex-independent-contribution-intake",
    }
    if observed["relay"] is not None:
        receipt["return_transport"] = "GCL-RETURN-RELAY/1"
        receipt["relay_provenance"] = observed["relay"]
        receipt["relay_provenance"]["source_comment_url"] = observed["comment"].get("html_url")
        receipt["relay_provenance"]["authenticated_relay_actor"] = observed["actor"]
        receipt["relay_provenance"]["envelope_utf8"] = observed["comment"]["body"]

    output.mkdir(parents=True, exist_ok=True)
    (output / "RAW.md").write_text(body, encoding="utf-8")
    (output / "RECEIPT.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    meta = {
        "dispatch_id": dispatch_id,
        "comment_id": comment_id,
        "issue_number": observed["issue"]["number"],
        "raw_repo_path": raw_rel.as_posix(),
        "receipt_repo_path": receipt_rel.as_posix(),
        "branch": f"intake/openmath-{dispatch_id.lower()}",
        "pr_title": f"OPENMATH CEX intake: {dispatch_id}",
    }
    (output / "META.json").write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return meta


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--event", type=Path, required=True)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        event = json.loads(args.event.read_text(encoding="utf-8"))
        meta = emit_intake(_object(event, "event"), args.repo_root, args.output)
    except (OSError, json.JSONDecodeError, IntakeError) as exc:
        args.output.mkdir(parents=True, exist_ok=True)
        (args.output / "ERRORS.txt").write_text(str(exc) + "\n", encoding="utf-8")
        print(f"INTAKE_INVALID: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(meta, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
