from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from ci.gcl_worker_queue_contract import active_reservation, queue_job_for_dispatch

ROOT = Path(__file__).resolve().parents[1]

MARKER = "GCL-CONTRIBUTION-RESULT/1"
DISPATCH_MARKER = "GCL-CONTRIBUTION-DISPATCH/1"
URL_RE = re.compile(r"(?:https?://|www\.)", re.IGNORECASE)
MD_LINK_RE = re.compile(r"!?\[[^\]\n]*\]\([^\)\n]+\)")
HTML_LINK_RE = re.compile(r"</?(?:a|img)\b(?:\s+[^<>]*?)?\s*/?>", re.IGNORECASE)
HEADING_RE = re.compile(r"^## .+$", re.MULTILINE)

SECTIONS = [
    "## Strongest exact statement",
    "## Derivation",
    "## Assumptions beyond bootstrap",
    "## Verification / falsification hooks",
    "## Claim boundary",
    "## Next residual",
]


@dataclass(frozen=True)
class IntakeProfile:
    campaign: str
    dispatch_re: re.Pattern[str]
    base_rel: Path
    dispatch_schema_version: str
    receipt_schema_version: str
    preamble_keys: tuple[str, ...]
    dispositions: frozenset[str]
    external_sources: str
    pr_title_prefix: str


NS_PROFILE = IntakeProfile(
    campaign="NS-CI-001",
    dispatch_re=re.compile(r"^NSCI-C2-[A-E]-(?:BLIND|COOP|ADV)-[0-9]{3}$"),
    base_rel=Path("contributions/NS-CI-001/C2_MIX_DIRECTION_COMPRESSION_LEDGER_CHARGE"),
    dispatch_schema_version="0.2-pilot",
    receipt_schema_version="0.2-pilot",
    preamble_keys=(
        "dispatch_id",
        "assignment",
        "disposition",
        "context_class",
        "external_sources",
        "timebox_observed",
    ),
    dispositions=frozenset({"PROVED", "REFUTED", "REDUCED", "BLOCKED"}),
    external_sources="NONE",
    pr_title_prefix="NS-CI intake",
)

UC_PROFILE = IntakeProfile(
    campaign="UC-001",
    dispatch_re=re.compile(r"^UC-WP08-D004-WP0[1-5]-IA-001$"),
    base_rel=Path("contributions/UC-001/WP08_D004_INCIDENCE_INTERFACE"),
    dispatch_schema_version="1.0.0",
    receipt_schema_version="1.0.0",
    preamble_keys=(
        "dispatch_id",
        "agent_ref",
        "assignment",
        "disposition",
        "context_class",
        "external_sources",
        "timebox_observed",
    ),
    dispositions=frozenset({
        "PROVED_REDUCTION",
        "EXACT_CERTIFICATE",
        "FORMAL_LEMMA_PROVED",
        "COUNTEREXAMPLE",
        "NO_MATERIAL_DELTA",
        "EXACT_BLOCKER",
    }),
    external_sources="PROTECTED_PACKET_ONLY",
    pr_title_prefix="UC-001 intake",
)

CMDG_PROFILE = IntakeProfile(
    campaign="CMDG-CM4",
    dispatch_re=re.compile(r"^CMDG-P3M-SEP-WP-[A-D]-IA-001$"),
    base_rel=Path("contributions/CMDG-CM4/P3M_ONE_POINT_SEPARATION_003"),
    dispatch_schema_version="1.0.0",
    receipt_schema_version="1.0.0",
    preamble_keys=(
        "dispatch_id",
        "agent_ref",
        "assignment",
        "disposition",
        "context_class",
        "external_sources",
        "timebox_observed",
    ),
    dispositions=frozenset({
        "PROVED_REDUCTION",
        "EXACT_CERTIFICATE",
        "FORMAL_LEMMA_PROVED",
        "COUNTEREXAMPLE",
        "NO_MATERIAL_DELTA",
        "EXACT_BLOCKER",
    }),
    external_sources="PROTECTED_PACKET_ONLY",
    pr_title_prefix="CMDG-CM4 intake",
)

CMDG_COV_PROFILE = IntakeProfile(
    campaign="CMDG-CM4-COV",
    dispatch_re=re.compile(r"^CMDG-P3M-COV-WP-[A-D]-IA-001$"),
    base_rel=Path("contributions/CMDG-CM4/P3M_WEIGHTED_ONE_POINT_COVERAGE_004"),
    dispatch_schema_version="1.0.0",
    receipt_schema_version="1.0.0",
    preamble_keys=(
        "dispatch_id",
        "agent_ref",
        "assignment",
        "disposition",
        "context_class",
        "external_sources",
        "timebox_observed",
    ),
    dispositions=frozenset({
        "PROVED_REDUCTION",
        "EXACT_CERTIFICATE",
        "FORMAL_LEMMA_PROVED",
        "COUNTEREXAMPLE",
        "NO_MATERIAL_DELTA",
        "EXACT_BLOCKER",
    }),
    external_sources="PROTECTED_PACKET_ONLY",
    pr_title_prefix="CMDG-CM4 coverage intake",
)

CMDG_N3_PROFILE = IntakeProfile(
    campaign="CMDG-CM4-N3",
    dispatch_re=re.compile(r"^CMDG-P3M-N3-WP-[A-D]-IA-001$"),
    base_rel=Path("contributions/CMDG-CM4/P3M_FINITE_COEFFICIENT_ALLTRUE_005"),
    dispatch_schema_version="1.0.0",
    receipt_schema_version="1.0.0",
    preamble_keys=(
        "dispatch_id",
        "agent_ref",
        "assignment",
        "disposition",
        "context_class",
        "external_sources",
        "timebox_observed",
    ),
    dispositions=frozenset({
        "PROVED_REDUCTION",
        "EXACT_CERTIFICATE",
        "FORMAL_LEMMA_PROVED",
        "COUNTEREXAMPLE",
        "NO_MATERIAL_DELTA",
        "EXACT_BLOCKER",
    }),
    external_sources="PROTECTED_PACKET_ONLY",
    pr_title_prefix="CMDG-CM4 N3 intake",
)

ERDOS_RA_PROFILE = IntakeProfile(
    campaign="ERDOS-OPEN-RECON",
    dispatch_re=re.compile(r"^ERDOS-(?:593|595|241|470|1052|99|101|138)-(?:R1|A1)-IA-001$"),
    base_rel=Path("contributions/ERDOS-OPEN-001/RECON_TRANCHE_001"),
    dispatch_schema_version="1.0.0",
    receipt_schema_version="1.0.0",
    preamble_keys=("dispatch_id","agent_ref","assignment","disposition","context_class","external_sources","timebox_observed"),
    dispositions=frozenset({"EXACT_REDUCTION","FINITE_CERTIFICATE","SOURCE_INTERFACE_FOUND","COUNTEREXAMPLE","EXACT_BLOCKER","NO_MATERIAL_DELTA"}),
    external_sources="PROTECTED_PACKET_ONLY",
    pr_title_prefix="ERDOS-OPEN intake",
)

ERDOS_S_PROFILE = IntakeProfile(
    campaign="ERDOS-OPEN-RECON",
    dispatch_re=re.compile(r"^ERDOS-(?:593|595|241|470|1052|99|101|138)-S1-IA-001$"),
    base_rel=Path("contributions/ERDOS-OPEN-001/RECON_TRANCHE_001"),
    dispatch_schema_version="1.0.0",
    receipt_schema_version="1.0.0",
    preamble_keys=ERDOS_RA_PROFILE.preamble_keys,
    dispositions=ERDOS_RA_PROFILE.dispositions,
    external_sources="PRIMARY_SOURCES_REQUIRED",
    pr_title_prefix="ERDOS-OPEN intake",
)

PROFILES = (NS_PROFILE, UC_PROFILE, CMDG_PROFILE, CMDG_COV_PROFILE, CMDG_N3_PROFILE, ERDOS_RA_PROFILE, ERDOS_S_PROFILE)


class IntakeError(ValueError):
    pass


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _object(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise IntakeError(f"{label} must be a JSON object")
    return value


def profile_for_dispatch(dispatch_id: str) -> IntakeProfile:
    for profile in PROFILES:
        if profile.dispatch_re.fullmatch(dispatch_id):
            return profile
    raise IntakeError("dispatch_id has invalid or unregistered form")


def parse_result_comment(body: str) -> dict[str, Any]:
    if not isinstance(body, str) or not body.strip():
        raise IntakeError("comment body is empty")

    # Parse CRLF comments through an LF-normalized view while retaining the
    # original body bytes for raw evidence and receipt hashing.
    parsed_body = body.replace("\r\n", "\n")
    if not parsed_body.startswith(MARKER + "\n"):
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

    lines = parsed_body.splitlines()
    if len(lines) < 8:
        raise IntakeError("comment is too short")
    if not lines[1].startswith("dispatch_id: "):
        raise IntakeError("expected preamble field dispatch_id at line 2")
    dispatch_id = lines[1][len("dispatch_id: "):].strip()
    profile = profile_for_dispatch(dispatch_id)

    preamble: dict[str, str] = {}
    cursor = 1
    for key in profile.preamble_keys:
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

    if preamble["disposition"] not in profile.dispositions:
        raise IntakeError("disposition is invalid for this registered profile")
    if preamble["context_class"] != "ZERO_CONTEXT":
        raise IntakeError("context_class must be ZERO_CONTEXT")
    if preamble["external_sources"] != profile.external_sources:
        raise IntakeError(
            f"external_sources must be {profile.external_sources} for this registered profile"
        )
    if preamble["timebox_observed"] not in {"YES", "NO"}:
        raise IntakeError("timebox_observed must be YES or NO")

    if profile is NS_PROFILE and preamble["assignment"] not in {"A", "B", "C", "D", "E"}:
        raise IntakeError("assignment is invalid for the NS-CI pilot")
    if profile is UC_PROFILE and not re.fullmatch(r"UC-WP08-D004-WP0[1-5]", preamble["assignment"]):
        raise IntakeError("assignment is invalid for the UC-001 D004 profile")
    if profile is CMDG_PROFILE and not re.fullmatch(r"CMDG-P3M-SEP-WP-[A-D]", preamble["assignment"]):
        raise IntakeError("assignment is invalid for the CMDG P3-M separation profile")
    if profile is CMDG_COV_PROFILE and not re.fullmatch(r"CMDG-P3M-COV-WP-[A-D]", preamble["assignment"]):
        raise IntakeError("assignment is invalid for the CMDG P3-M weighted coverage profile")
    if profile is CMDG_N3_PROFILE and not re.fullmatch(r"CMDG-P3M-N3-WP-[A-D]", preamble["assignment"]):
        raise IntakeError("assignment is invalid for the CMDG P3-M N3 profile")
    if profile in {ERDOS_RA_PROFILE, ERDOS_S_PROFILE} and not re.fullmatch(
        r"ERDOS-(?:593|595|241|470|1052|99|101|138)-(?:R1|S1|A1)",
        preamble["assignment"],
    ):
        raise IntakeError("assignment is invalid for the ERDOS-OPEN reconnaissance profile")

    headings = HEADING_RE.findall(parsed_body)
    if headings != SECTIONS:
        raise IntakeError("level-2 sections must match the RESULT/1 schema exactly and in order")

    sections: dict[str, str] = {}
    positions = [(parsed_body.index(h), h) for h in SECTIONS]
    for index, (start, heading) in enumerate(positions):
        content_start = start + len(heading)
        content_end = positions[index + 1][0] if index + 1 < len(positions) else len(parsed_body)
        content = parsed_body[content_start:content_end].strip()
        if not content:
            raise IntakeError(f"{heading} is empty")
        sections[heading[3:]] = content

    next_residual = sections["Next residual"]
    sentence_view = re.sub(r"(?m)^\s*\d+\.\s+", "", next_residual)
    sentence_marks = len(re.findall(r"[.!?](?:\s|$)", sentence_view))
    if sentence_marks > 3:
        raise IntakeError("Next residual exceeds three sentences")

    return {"profile": profile.campaign, "preamble": preamble, "sections": sections}


def load_dispatch(root: Path, dispatch_id: str) -> tuple[IntakeProfile, dict[str, Any]]:
    profile = profile_for_dispatch(dispatch_id)
    path = root / profile.base_rel / "dispatches" / f"{dispatch_id}.json"
    if not path.is_file():
        raise IntakeError("dispatch_id is not registered on protected repository state")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise IntakeError(f"dispatch record is invalid JSON: {exc}") from exc
    return profile, _object(data, "dispatch record")


def validate_dispatch_issue(
    root: Path,
    issue: dict[str, Any],
    profile: IntakeProfile,
    dispatch: dict[str, Any],
) -> None:
    if dispatch.get("schema_version") != profile.dispatch_schema_version:
        raise IntakeError("dispatch schema version is not enabled for this intake profile")
    if dispatch.get("campaign") not in {None, profile.campaign}:
        raise IntakeError("dispatch campaign does not match registered intake profile")
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


def validate_event(
    event: dict[str, Any],
    root: Path,
    comments: list[dict[str, Any]] | None = None,
) -> tuple[dict[str, Any], IntakeProfile, dict[str, Any], dict[str, Any]]:
    issue = _object(event.get("issue"), "issue")
    if "pull_request" in issue:
        raise IntakeError("result comments are accepted only on dispatch issues")
    comment = _object(event.get("comment"), "comment")
    body = comment.get("body")
    if not isinstance(body, str):
        raise IntakeError("comment body is unavailable")

    parsed = parse_result_comment(body)
    dispatch_id = parsed["preamble"]["dispatch_id"]
    profile, dispatch = load_dispatch(root, dispatch_id)
    validate_dispatch_issue(root, issue, profile, dispatch)

    if parsed["preamble"]["assignment"] != dispatch.get("assignment_id"):
        raise IntakeError("assignment does not match protected dispatch")
    if profile in {UC_PROFILE, CMDG_PROFILE, CMDG_COV_PROFILE, CMDG_N3_PROFILE, ERDOS_RA_PROFILE, ERDOS_S_PROFILE} and parsed["preamble"].get("agent_ref") != dispatch.get("agent_ref"):
        raise IntakeError("agent_ref does not match protected dispatch")
    if dispatch.get("concurrency_mode") not in {
        "independent_blind",
        "cooperative_claimed",
        "adversarial_replay",
    }:
        raise IntakeError("protected dispatch has invalid concurrency mode")

    user = _object(comment.get("user"), "comment user")
    login = user.get("login")
    if not isinstance(login, str) or not login:
        raise IntakeError("authenticated GitHub actor is unavailable")

    comment_id = comment.get("id")
    if not isinstance(comment_id, int):
        raise IntakeError("GitHub comment id is unavailable")

    queue_job = queue_job_for_dispatch(root, dispatch_id)
    reservation = None
    if queue_job is not None and queue_job.get("self_claimable") is True:
        if comments is None:
            raise IntakeError("queue-managed dispatch requires issue comment history")
        created_at = comment.get("created_at")
        if not isinstance(created_at, str) or not created_at:
            raise IntakeError("queue-managed result lacks comment_created_at")
        at = datetime.fromisoformat(created_at.replace("Z", "+00:00")).astimezone(timezone.utc)
        reservation = active_reservation(
            comments,
            dispatch_id,
            at,
            {"github-actions[bot]"},
        )
        if reservation is None:
            raise IntakeError("queue-managed result has no active worker reservation")
        if reservation.get("worker") != login:
            raise IntakeError("authenticated result author does not match active worker reservation")

    return parsed, profile, dispatch, {
        "issue": issue,
        "comment": comment,
        "actor": login,
        "comment_id": comment_id,
        "queue_job": queue_job,
        "worker_reservation": reservation,
    }


def emit_intake(
    event: dict[str, Any],
    root: Path,
    output: Path,
    comments: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    parsed, profile, dispatch, observed = validate_event(event, root, comments)
    body = observed["comment"]["body"]
    assert isinstance(body, str)

    dispatch_id = parsed["preamble"]["dispatch_id"]
    comment_id = observed["comment_id"]
    raw_rel = profile.base_rel / "raw" / dispatch_id / f"github-comment-{comment_id}.md"
    receipt_rel = profile.base_rel / "receipts" / dispatch_id / f"github-comment-{comment_id}.json"

    queue_job = observed.get("queue_job") or {}
    reservation = observed.get("worker_reservation") or {}
    epistemic_class = {
        "independent_blind": "INDEPENDENT_BLIND",
        "cooperative_claimed": "COOPERATIVE",
        "adversarial_replay": "ADVERSARIAL_REPLAY",
    }[dispatch["concurrency_mode"]]

    receipt = {
        "schema_version": profile.receipt_schema_version,
        "receipt_id": f"{dispatch_id}:github-comment:{comment_id}",
        "campaign": profile.campaign,
        "dispatch_id": dispatch_id,
        "assignment_id": dispatch["assignment_id"],
        "agent_ref": dispatch.get("agent_ref"),
        "concurrency_mode": dispatch["concurrency_mode"],
        "blind_cohort_id": dispatch.get("blind_cohort_id"),
        "result_protocol": MARKER,
        "github_issue_number": observed["issue"]["number"],
        "github_comment_id": comment_id,
        "authenticated_github_actor": observed["actor"],
        "comment_created_at": observed["comment"].get("created_at"),
        "queue_managed": bool(queue_job),
        "worker_reservation_enforced": bool(queue_job),
        "worker_reservation_owner": reservation.get("worker"),
        "collaboration_mode": queue_job.get("collaboration_mode"),
        "visibility_phase": queue_job.get("visibility_phase"),
        "sibling_use_policy": queue_job.get("sibling_use_policy"),
        "epistemic_class": epistemic_class,
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
        "recorded_by": "github-actions:controlled-epistemic-interface-intake",
    }

    output.mkdir(parents=True, exist_ok=True)
    (output / "RAW.md").write_text(body, encoding="utf-8")
    (output / "RECEIPT.json").write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    meta = {
        "campaign": profile.campaign,
        "dispatch_id": dispatch_id,
        "comment_id": comment_id,
        "issue_number": observed["issue"]["number"],
        "raw_repo_path": raw_rel.as_posix(),
        "receipt_repo_path": receipt_rel.as_posix(),
        "branch": f"intake/{dispatch_id.lower()}",
        "pr_title": f"{profile.pr_title_prefix}: {dispatch_id}",
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
    parser.add_argument("--comments", type=Path)
    args = parser.parse_args()
    try:
        event = json.loads(args.event.read_text(encoding="utf-8"))
        event = _object(event, "event")
        comments = None
        if args.comments is not None:
            comments = json.loads(args.comments.read_text(encoding="utf-8"))
            if not isinstance(comments, list):
                raise IntakeError("comments payload must be a JSON list")
        meta = emit_intake(event, args.repo_root, args.output, comments)
    except (OSError, json.JSONDecodeError, IntakeError) as exc:
        args.output.mkdir(parents=True, exist_ok=True)
        (args.output / "ERRORS.txt").write_text(str(exc) + "\n", encoding="utf-8")
        print(f"INTAKE_INVALID: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(meta, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
