from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BASE_REL = Path("work_packages/GCL_ERDOS3")
DISPATCH_DIR_REL = BASE_REL / "dispatches"

MARKER = "GCL-CONTRIBUTION-RESULT/1"
DISPATCH_MARKER = "GCL-CONTRIBUTION-DISPATCH/1"
DISPATCH_ID_RE = re.compile(r"^GCL-ERDOS3-E3-[A-Z][A-Z0-9]*-IA-[0-9]{3}$")
URL_RE = re.compile(r"(?:https?://|www\.)", re.IGNORECASE)
MD_LINK_RE = re.compile(r"!?\[[^\]\n]*\]\([^\)\n]+\)")
HTML_LINK_RE = re.compile(r"</?(?:a|img)\b(?:\s+[^<>]*?)?\s*/?>", re.IGNORECASE)
HEADING_RE = re.compile(r"^## .+$", re.MULTILINE)

PREAMBLE_KEYS = (
    "dispatch_id",
    "assignment",
    "agent_ref",
    "disposition",
    "context_class",
    "external_sources",
)


class IntakeError(ValueError):
    pass


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def git_blob_sha1(text: str) -> str:
    raw = text.encode("utf-8")
    header = f"blob {len(raw)}\0".encode("ascii")
    return hashlib.sha1(header + raw).hexdigest()


def _object(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise IntakeError(f"{label} must be a JSON object")
    return value


def load_dispatch(root: Path, dispatch_id: str) -> dict[str, Any]:
    if not DISPATCH_ID_RE.fullmatch(dispatch_id):
        raise IntakeError("dispatch_id has invalid or unregistered GCL-ERDOS3 form")
    path = root / DISPATCH_DIR_REL / f"{dispatch_id}.json"
    if not path.is_file():
        raise IntakeError("dispatch_id is not registered on protected repository state")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise IntakeError(f"dispatch record is invalid JSON: {exc}") from exc
    return _object(data, "dispatch record")


def parse_result_comment(body: str, dispatch: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(body, str) or not body.strip():
        raise IntakeError("comment body is empty")

    parsed_body = body.replace("\r\n", "\n")
    if not parsed_body.startswith(MARKER + "\n"):
        raise IntakeError(f"comment must begin exactly with {MARKER}")

    policy = _object(dispatch.get("intake_policy"), "dispatch intake_policy")
    forbidden: list[str] = []
    if policy.get("raw_urls_allowed") is False and URL_RE.search(body):
        forbidden.append("raw URL")
    if policy.get("markdown_links_allowed") is False and MD_LINK_RE.search(body):
        forbidden.append("Markdown link or image")
    if policy.get("html_links_or_images_allowed") is False and HTML_LINK_RE.search(body):
        forbidden.append("HTML link or image")
    if policy.get("attachments_allowed") is False and "github.com/user-attachments" in body.lower():
        forbidden.append("GitHub attachment")
    if forbidden:
        raise IntakeError("forbidden content: " + ", ".join(sorted(set(forbidden))))

    lines = parsed_body.splitlines()
    preamble: dict[str, str] = {}
    cursor = 1
    for key in PREAMBLE_KEYS:
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

    if preamble["dispatch_id"] != dispatch.get("dispatch_id"):
        raise IntakeError("dispatch_id does not match protected dispatch")
    if preamble["assignment"] != dispatch.get("assignment_id"):
        raise IntakeError("assignment does not match protected dispatch")
    if preamble["agent_ref"] != dispatch.get("agent_ref"):
        raise IntakeError("agent_ref does not match protected dispatch")
    if preamble["context_class"] != dispatch.get("context_class"):
        raise IntakeError("context_class does not match protected dispatch")
    if preamble["external_sources"] != dispatch.get("external_sources"):
        raise IntakeError("external_sources does not match protected dispatch")

    allowed = dispatch.get("acceptable_dispositions")
    if not isinstance(allowed, list) or not allowed or not all(isinstance(x, str) for x in allowed):
        raise IntakeError("protected dispatch lacks acceptable_dispositions")
    if preamble["disposition"] not in allowed:
        raise IntakeError("disposition is invalid for this protected dispatch")

    required_sections = dispatch.get("required_result_sections")
    if not isinstance(required_sections, list) or not required_sections or not all(
        isinstance(x, str) and x for x in required_sections
    ):
        raise IntakeError("protected dispatch lacks required_result_sections")
    headings = HEADING_RE.findall(parsed_body)
    expected_headings = [f"## {name}" for name in required_sections]
    if headings != expected_headings:
        raise IntakeError("level-2 sections must match the protected RESULT/1 schema exactly and in order")

    sections: dict[str, str] = {}
    positions = [(parsed_body.index(h), h) for h in expected_headings]
    for index, (start, heading) in enumerate(positions):
        end = positions[index + 1][0] if index + 1 < len(positions) else len(parsed_body)
        content = parsed_body[start + len(heading):end].strip()
        if not content:
            raise IntakeError(f"{heading} is empty")
        sections[heading[3:]] = content

    residual = sections.get("Next residual", "")
    sentence_view = re.sub(r"(?m)^\s*\d+\.\s+", "", residual)
    sentence_marks = len(re.findall(r"[.!?](?:\s|$)", sentence_view))
    max_sentences = policy.get("next_residual_max_sentences")
    if not isinstance(max_sentences, int) or max_sentences < 0:
        raise IntakeError("protected dispatch has invalid next_residual_max_sentences")
    if sentence_marks > max_sentences:
        raise IntakeError(f"Next residual exceeds {max_sentences} sentences")

    return {"preamble": preamble, "sections": sections}


def validate_dispatch_issue(root: Path, issue: dict[str, Any], dispatch: dict[str, Any]) -> None:
    if dispatch.get("schema_version") != "1.0.0":
        raise IntakeError("unsupported dispatch schema")
    if dispatch.get("campaign") != "GCL-ERDOS3":
        raise IntakeError("dispatch campaign mismatch")
    if dispatch.get("return_protocol") != MARKER:
        raise IntakeError("dispatch return protocol mismatch")
    if dispatch.get("state") != "DISPATCHED__AWAITING_RETURN":
        raise IntakeError("dispatch is not awaiting a return")
    if dispatch.get("canonical_mutation_authorized") is not False:
        raise IntakeError("dispatch improperly authorizes canonical mutation")
    if dispatch.get("concurrency_mode") != "independent_blind":
        raise IntakeError("dispatch is not independent_blind")

    number = issue.get("number")
    expected_number = dispatch.get("github_issue_number", dispatch.get("issue_number"))
    if not isinstance(number, int) or number != expected_number:
        raise IntakeError("comment was posted to an issue not bound to this dispatch")

    if issue.get("title") != dispatch.get("github_issue_title"):
        raise IntakeError("dispatch issue title does not match protected binding")

    issue_body = issue.get("body")
    if not isinstance(issue_body, str):
        raise IntakeError("dispatch issue body is unavailable")
    if not issue_body.startswith(DISPATCH_MARKER + "\n"):
        raise IntakeError("dispatch issue is missing the dispatch marker")

    bootstrap_path = dispatch.get("bootstrap_path")
    if not isinstance(bootstrap_path, str) or not bootstrap_path:
        raise IntakeError("dispatch record lacks bootstrap_path")
    protected_path = root / bootstrap_path
    if not protected_path.is_file():
        raise IntakeError("protected bootstrap file is missing")
    protected = protected_path.read_text(encoding="utf-8")
    if git_blob_sha1(protected) != dispatch.get("bootstrap_blob_sha1"):
        raise IntakeError("protected bootstrap blob identity does not match dispatch record")
    if issue_body != protected:
        raise IntakeError("GitHub issue body differs from protected bootstrap bytes")


def validate_event(
    event: dict[str, Any], root: Path
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    issue = _object(event.get("issue"), "issue")
    if "pull_request" in issue:
        raise IntakeError("result comments are accepted only on dispatch issues")
    comment = _object(event.get("comment"), "comment")
    body = comment.get("body")
    if not isinstance(body, str):
        raise IntakeError("comment body is unavailable")

    parsed_body = body.replace("\r\n", "\n")
    lines = parsed_body.splitlines()
    if len(lines) < 2 or not lines[1].startswith("dispatch_id: "):
        raise IntakeError("expected dispatch_id at line 2")
    dispatch_id = lines[1][len("dispatch_id: "):].strip()
    dispatch = load_dispatch(root, dispatch_id)
    parsed = parse_result_comment(body, dispatch)
    validate_dispatch_issue(root, issue, dispatch)

    user = _object(comment.get("user"), "comment user")
    login = user.get("login")
    if not isinstance(login, str) or not login:
        raise IntakeError("authenticated GitHub actor is unavailable")
    comment_id = comment.get("id")
    if not isinstance(comment_id, int):
        raise IntakeError("GitHub comment id is unavailable")

    return parsed, dispatch, {
        "issue": issue,
        "comment": comment,
        "actor": login,
        "comment_id": comment_id,
    }


def emit_intake(event: dict[str, Any], root: Path, output: Path) -> dict[str, Any]:
    parsed, dispatch, observed = validate_event(event, root)
    body = observed["comment"]["body"]
    assert isinstance(body, str)

    dispatch_id = parsed["preamble"]["dispatch_id"]
    comment_id = observed["comment_id"]
    raw_rel = BASE_REL / "intake" / "raw" / dispatch_id / f"github-comment-{comment_id}.md"
    receipt_rel = BASE_REL / "intake" / "receipts" / dispatch_id / f"github-comment-{comment_id}.json"

    receipt = {
        "schema_version": "1.0.0",
        "record_type": "GCL_ERDOS3_EXTERNAL_RESULT_RECEIPT",
        "receipt_id": f"{dispatch_id}:github-comment:{comment_id}",
        "campaign": "GCL-ERDOS3",
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
        "raw_sha256": sha256_text(body),
        "bootstrap_path": dispatch["bootstrap_path"],
        "bootstrap_blob_sha1": dispatch["bootstrap_blob_sha1"],
        "task_commit": dispatch["task_commit"],
        "task_path": dispatch["task_path"],
        "task_blob_sha1": dispatch["task_blob_sha1"],
        "target_node": dispatch.get("target_node"),
        "frontier_action": dispatch.get("frontier_action"),
        "replay_budget_ordinal": dispatch.get("replay_budget_ordinal"),
        "disposition_declared": parsed["preamble"]["disposition"],
        "context_class_declared": parsed["preamble"]["context_class"],
        "external_sources_declared": parsed["preamble"]["external_sources"],
        "schema_result": "valid",
        "freshness": "current_for_dispatch",
        "handling_state": "received_unadjudicated",
        "mathematical_correctness_adjudicated": False,
        "independence_strength_adjudicated": False,
        "canonical_claim_effect": False,
        "certification_effect": False,
        "recorded_by": "github-actions:gcl-erdos3-controlled-epistemic-interface-intake",
    }

    output.mkdir(parents=True, exist_ok=True)
    (output / "RAW.md").write_text(body, encoding="utf-8")
    (output / "RECEIPT.json").write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    meta = {
        "campaign": "GCL-ERDOS3",
        "dispatch_id": dispatch_id,
        "comment_id": comment_id,
        "issue_number": observed["issue"]["number"],
        "raw_repo_path": raw_rel.as_posix(),
        "receipt_repo_path": receipt_rel.as_posix(),
        "branch": f"intake/{dispatch_id.lower()}",
        "pr_title": f"GCL-ERDOS3 intake: {dispatch_id}",
    }
    (output / "META.json").write_text(
        json.dumps(meta, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return meta


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--event", type=Path, required=True)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        event = _object(json.loads(args.event.read_text(encoding="utf-8")), "event")
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
