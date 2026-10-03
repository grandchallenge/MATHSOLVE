from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BASE_REL = Path("contributions/YM-001/YM_D003_MRS_R002")
DISPATCH_DIR_REL = BASE_REL / "dispatches"

MARKER = "GCL-CONTRIBUTION-RESULT/1"
DISPATCH_MARKER = "GCL-CONTRIBUTION-DISPATCH/1"
DISPATCH_ID_RE = re.compile(r"^YM-D003-MRS-R002-WP-[ABC]-IA-[0-9]{3}$")
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
ASSIGNMENTS = {"A", "B", "C"}


class IntakeError(ValueError):
    pass


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _obj(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise IntakeError(f"{label} must be an object")
    return value


def parse_result_comment(body: str) -> dict[str, Any]:
    if not isinstance(body, str) or not body.startswith(MARKER + "\n"):
        raise IntakeError(f"comment must begin exactly with {MARKER}")

    forbidden = []
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
    expected = [
        "dispatch_id",
        "assignment",
        "disposition",
        "context_class",
        "external_sources",
        "timebox_observed",
    ]
    preamble: dict[str, str] = {}
    cursor = 1
    for key in expected:
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

    if not DISPATCH_ID_RE.fullmatch(preamble["dispatch_id"]):
        raise IntakeError("dispatch_id has invalid form")
    if preamble["assignment"] not in ASSIGNMENTS:
        raise IntakeError("assignment is invalid")
    if preamble["disposition"] not in DISPOSITIONS:
        raise IntakeError("disposition is invalid")
    if preamble["context_class"] != "ZERO_CONTEXT":
        raise IntakeError("context_class must be ZERO_CONTEXT")
    if preamble["timebox_observed"] not in {"YES", "NO"}:
        raise IntakeError("timebox_observed must be YES or NO")

    headings = HEADING_RE.findall(body)
    if headings != SECTIONS:
        raise IntakeError("level-2 sections must match RESULT/1 schema exactly and in order")

    sections: dict[str, str] = {}
    positions = [(body.index(h), h) for h in SECTIONS]
    for i, (start, heading) in enumerate(positions):
        end = positions[i + 1][0] if i + 1 < len(positions) else len(body)
        content = body[start + len(heading):end].strip()
        if not content:
            raise IntakeError(f"{heading} is empty")
        sections[heading[3:]] = content

    residual = sections["Next residual"]
    if len(re.findall(r"[.!?](?:\s|$)", residual)) > 3:
        raise IntakeError("Next residual exceeds three sentences")

    return {"preamble": preamble, "sections": sections}


def load_dispatch(root: Path, dispatch_id: str) -> dict[str, Any]:
    path = root / DISPATCH_DIR_REL / f"{dispatch_id}.json"
    if not path.is_file():
        raise IntakeError("dispatch_id is not registered on protected main")
    return _obj(json.loads(path.read_text(encoding="utf-8")), "dispatch")


def validate_event(event: dict[str, Any], root: Path) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    issue = _obj(event.get("issue"), "issue")
    if "pull_request" in issue:
        raise IntakeError("results are accepted only on dispatch issues")
    comment = _obj(event.get("comment"), "comment")
    body = comment.get("body")
    if not isinstance(body, str):
        raise IntakeError("comment body unavailable")

    parsed = parse_result_comment(body)
    dispatch = load_dispatch(root, parsed["preamble"]["dispatch_id"])

    if dispatch.get("schema_version") != "1.0.0":
        raise IntakeError("unsupported dispatch schema")
    if dispatch.get("dispatch_status") != "READY_FOR_GITHUB_COMMENT":
        raise IntakeError("dispatch is not ready")
    if dispatch.get("return_protocol") != MARKER:
        raise IntakeError("dispatch return protocol mismatch")
    if dispatch.get("canonical_mutation_authorized") is not False:
        raise IntakeError("dispatch improperly authorizes canonical mutation")

    number = issue.get("number")
    if number != dispatch.get("github_issue_number"):
        raise IntakeError("comment posted to wrong issue")
    if issue.get("title") != dispatch.get("github_issue_title"):
        raise IntakeError("issue title differs from protected dispatch binding")

    issue_body = issue.get("body")
    if not isinstance(issue_body, str) or not issue_body.startswith(DISPATCH_MARKER + "\n"):
        raise IntakeError("issue body lacks dispatch marker")
    bootstrap = root / str(dispatch.get("bootstrap_path", ""))
    if not bootstrap.is_file():
        raise IntakeError("protected bootstrap missing")
    protected = bootstrap.read_text(encoding="utf-8")
    if sha256_text(protected) != dispatch.get("bootstrap_sha256"):
        raise IntakeError("bootstrap digest mismatch")
    if issue_body != protected:
        raise IntakeError("issue body differs from protected bootstrap")

    pre = parsed["preamble"]
    if pre["assignment"] != dispatch.get("assignment"):
        raise IntakeError("assignment mismatch")
    if pre["external_sources"] != dispatch.get("external_sources"):
        raise IntakeError("external_sources policy mismatch")
    if dispatch.get("concurrency_mode") != "independent_blind":
        raise IntakeError("unsupported concurrency mode")

    actor = _obj(comment.get("user"), "comment user").get("login")
    comment_id = comment.get("id")
    if not isinstance(actor, str) or not actor:
        raise IntakeError("authenticated GitHub actor unavailable")
    if not isinstance(comment_id, int):
        raise IntakeError("GitHub comment id unavailable")

    return parsed, dispatch, {"issue": issue, "comment": comment, "actor": actor, "comment_id": comment_id}


def emit_intake(event: dict[str, Any], root: Path, output: Path) -> dict[str, Any]:
    parsed, dispatch, observed = validate_event(event, root)
    body = observed["comment"]["body"]
    dispatch_id = parsed["preamble"]["dispatch_id"]
    comment_id = observed["comment_id"]

    raw_rel = BASE_REL / "raw" / dispatch_id / f"github-comment-{comment_id}.md"
    receipt_rel = BASE_REL / "receipts" / dispatch_id / f"github-comment-{comment_id}.json"
    receipt = {
        "schema_version": "1.0.0",
        "record_type": "YM_MRS_EXTERNAL_RESULT_RECEIPT",
        "dispatch_id": dispatch_id,
        "assignment": dispatch["assignment"],
        "concurrency_mode": dispatch["concurrency_mode"],
        "github_issue_number": observed["issue"]["number"],
        "github_comment_id": comment_id,
        "authenticated_github_actor": observed["actor"],
        "comment_created_at": observed["comment"].get("created_at"),
        "raw_artifact_path": raw_rel.as_posix(),
        "raw_sha256": sha256_text(body),
        "bootstrap_path": dispatch["bootstrap_path"],
        "bootstrap_sha256": dispatch["bootstrap_sha256"],
        "source_handoff_commit_sha": dispatch["source_handoff_commit_sha"],
        "disposition_declared": parsed["preamble"]["disposition"],
        "external_sources_declared": parsed["preamble"]["external_sources"],
        "timebox_observed_declared": parsed["preamble"]["timebox_observed"],
        "handling_state": "RECEIVED_UNADJUDICATED",
        "mathematical_correctness_adjudicated": False,
        "canonical_claim_effect": False,
        "certification_effect": False,
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
        event = _obj(json.loads(args.event.read_text(encoding="utf-8")), "event")
        emit_intake(event, args.repo_root, args.output)
    except (OSError, json.JSONDecodeError, IntakeError) as exc:
        args.output.mkdir(parents=True, exist_ok=True)
        (args.output / "ERRORS.txt").write_text(str(exc) + "\n", encoding="utf-8")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
