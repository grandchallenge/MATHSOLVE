#!/usr/bin/env python3
"""Fail-closed source-side preflight for a prospective Solve specialist pilot.

This checks *existing* evidence, never manufactures a positive replay or
specialist receipt. A positive preflight is NOT specialist admission.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

HEX40 = re.compile(r"[0-9a-f]{40}\Z")
HEX64 = re.compile(r"[0-9a-f]{64}\Z")
KINDS = (
    "GCL_SOLVE_CAPTURE_RECEIPT_V1",
    "GCL_SOLVE_REPLAY_RECEIPT_V1",
    "GCL_SOLVE_ADJUDICATION_RECEIPT_V1",
)
EFFECTS = (
    "mathematical_claim_effect",
    "certification_effect",
    "publication_effect",
    "source_semantic_effect",
    "security_authority_effect",
)


class EvidenceError(ValueError):
    pass


def require(test: bool, message: str) -> None:
    if not test:
        raise EvidenceError(message)


def git_bytes(root: Path, revision: str, path: str) -> bytes:
    require(bool(HEX40.fullmatch(revision)), "revision must be an exact commit SHA")
    require(path.startswith("contributions/") and ".." not in Path(path).parts, "unsafe contribution path")
    result = subprocess.run(
        ["git", "-C", str(root), "show", f"{revision}:{path}"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    require(result.returncode == 0, f"protected artifact unavailable: {path}")
    return result.stdout


def blob_sha(payload: bytes) -> str:
    return hashlib.sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def parse(payload: bytes, name: str) -> dict:
    try:
        value = json.loads(payload)
    except (ValueError, UnicodeError) as exc:
        raise EvidenceError(f"{name} is not valid JSON") from exc
    require(isinstance(value, dict), f"{name} must be a JSON object")
    return value


def preflight(root: Path, revision: str, binding: dict, *, source_revision: str | None = None) -> dict:
    """Verify locked artifacts and identities, not truth of replay_pass."""
    require(binding.get("schema_version") == "1.0.0", "binding schema mismatch")
    dispatch = binding.get("dispatch_id")
    result_ref = binding.get("result_ref")
    digest = binding.get("result_sha256")
    require(isinstance(dispatch, str) and dispatch and isinstance(result_ref, str) and result_ref, "missing identities")
    require(isinstance(digest, str) and HEX64.fullmatch(digest) is not None, "bad result digest")
    effects = binding.get("claim_effects")
    require(isinstance(effects, dict) and set(effects) == set(EFFECTS), "incomplete claim-effect mask")
    require(all(effects[k] is False for k in EFFECTS), "claim authority must be false")

    objects: dict[str, dict] = {}
    locks: dict[str, str] = {}
    for key, kind in zip(("capture", "replay", "adjudication"), KINDS):
        pointer = binding.get(key)
        require(isinstance(pointer, dict) and set(pointer) == {"path", "blob_sha"}, f"{key} pointer malformed")
        path, sha = pointer["path"], pointer["blob_sha"]
        require(isinstance(path, str) and isinstance(sha, str) and HEX40.fullmatch(sha) is not None,
                f"{key} blob lock malformed")
        require(f"/{dispatch}/" in path, f"{key} path is not dispatch-scoped")
        data = git_bytes(root, revision, path)
        require(blob_sha(data) == sha, f"{key} protected blob mismatch")
        record = parse(data, key)
        require(record.get("record_type") == kind, f"{key} record type mismatch")
        require(record.get("dispatch_id") == dispatch and record.get("result_ref") == result_ref,
                f"{key} identity mismatch")
        objects[key] = record
        locks[key] = sha

    capture, replay, adjud = (objects[k] for k in ("capture", "replay", "adjudication"))
    require(capture.get("result_sha256") == digest, "capture digest mismatch")
    require(replay.get("input_result_sha256") == digest, "replay input digest mismatch")
    require(replay.get("capture_blob_sha") == locks["capture"], "replay capture lock mismatch")
    require(replay.get("replay_pass") is True, "replay failure or absent replay")
    require(adjud.get("replay_blob_sha") == locks["replay"], "adjudication replay lock mismatch")
    require(adjud.get("adjudication_disposition") == "REPLAYED_AND_ADJUDICATED",
            "adjudication disposition mismatch")
    require(isinstance(adjud.get("adjudication_id"), str) and bool(adjud["adjudication_id"]),
            "missing adjudication identity")
    require(adjud.get("claim_effects") == effects, "adjudication claim effects mismatch")
    require(isinstance(capture.get("authenticated_intake_provenance"), dict)
            and bool(capture["authenticated_intake_provenance"]), "missing authenticated intake provenance")
    require(isinstance(replay.get("reproducibility_artifact"), str)
            and bool(replay["reproducibility_artifact"]), "missing reproducibility artifact")

    raw_path = capture.get("captured_result_path")
    require(isinstance(raw_path, str) and f"/{dispatch}/" in raw_path, "captured source path missing")
    original = git_bytes(root, revision, raw_path)
    require(hashlib.sha256(original).hexdigest() == digest, "captured result bytes differ from digest")
    return {
        "state": "SOURCE_LINK_PREFLIGHT_PASS_ONLY",
        "dispatch_id": dispatch, "result_ref": result_ref,
        "result_sha256": digest, "source_revision": source_revision or revision,
        "mathematical_certification": False, "specialist_positive_receipt": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--revision", required=True, help="exact protected commit SHA")
    parser.add_argument("--binding", required=True, type=Path)
    args = parser.parse_args()
    try:
        binding = parse(args.binding.read_bytes(), "binding")
        result = preflight(args.root, args.revision, binding)
        print(json.dumps(result, sort_keys=True))
    except EvidenceError as exc:
        parser.exit(1, f"REJECTED: {exc}\n")


if __name__ == "__main__":
    main()
