#!/usr/bin/env python3
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]
ADOPTION = ROOT / ".gcl/agent-continuity.json"
AGENTS = ROOT / "AGENTS.md"
SCHEMA = ROOT / "schemas/agent_continuity_adoption.schema.json"

SCHEMA_AUTHORITY_COMMIT = "7e6b61ddf77e2d73309657d089a98cae84cc735f"
SCHEMA_BLOB_SHA = "b019881a54763a949613c8116260b729742867bd"
LOCAL_VALIDATOR = "scripts/validate_agent_continuity_adoption.py"

EXPECTED_COMMON = {
    "schema_id": "GCL-AGENT-CONTINUITY-ADOPTION-001",
    "schema_version": "1.0.0",
    "adoption_id": "MATHSOLVE-GCL-AGENT-CONTINUITY-001",
    "policy_id": "GCL-AGENT-CONTINUITY-001",
    "version": "1.0.0",
    "authority_repository": "grandchallenge/INTELLECT",
    "authority_path": "governance/agent_execution/GCL-AGENT-CONTINUITY-001.md",
    "repository": "grandchallenge/MATHSOLVE",
    "binding_surface": "AGENTS.md",
    "specialization": None,
    "local_validator": LOCAL_VALIDATOR,
}
ALLOWED_TOP_LEVEL = set(EXPECTED_COMMON) | {
    "required",
    "authority_preservation",
    "specialization_data",
}
EXPECTED_SCHEMA_BINDING = {
    "authority_commit": SCHEMA_AUTHORITY_COMMIT,
    "schema_blob_sha": SCHEMA_BLOB_SHA,
    "local_snapshot": "schemas/agent_continuity_adoption.schema.json",
    "local_snapshot_authoritative": False,
    "mutable_remote_fetch_allowed": False,
}
REQUIRED_CONTROLS = (
    "exact_head_preflight",
    "narrow_durable_tranches",
    "checkpoint_before_branch_expansion",
    "post_mutation_readback",
    "timeout_recovery_from_repository",
    "alternate_agent_rebind",
    "named_terminal_boundary",
)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha(path: Path) -> str:
    payload = path.read_bytes()
    header = f"blob {len(payload)}\0".encode("utf-8")
    return hashlib.sha1(header + payload).hexdigest()


def adoption_errors(record: dict[str, Any], agents_text: str) -> list[str]:
    errors: list[str] = []

    missing = ALLOWED_TOP_LEVEL - set(record)
    extra = set(record) - ALLOWED_TOP_LEVEL
    for key in sorted(missing):
        errors.append(f"missing common adoption field: {key}")
    for key in sorted(extra):
        errors.append(f"unexpected top-level adoption field: {key}")

    for key, value in EXPECTED_COMMON.items():
        if record.get(key) != value:
            errors.append(f"{key}: expected {value!r}, found {record.get(key)!r}")

    if record.get("required") is not True:
        errors.append("continuity policy is not required")

    authority = record.get("authority_preservation", {})
    if not isinstance(authority, dict):
        errors.append("authority_preservation must be an object")
        authority = {}
    if authority.get("authority_changed") is not False:
        errors.append("authority_preservation.authority_changed must be false")
    if authority.get("certification_authority_changed") is not False:
        errors.append("authority_preservation.certification_authority_changed must be false")
    if any(not isinstance(value, bool) for value in authority.values()):
        errors.append("authority_preservation values must be boolean")

    specialization = record.get("specialization_data", {})
    if not isinstance(specialization, dict):
        errors.append("specialization_data must be an object")
        specialization = {}

    binding = specialization.get("schema_binding", {})
    if not isinstance(binding, dict):
        errors.append("specialization_data.schema_binding must be an object")
        binding = {}
    for key, value in EXPECTED_SCHEMA_BINDING.items():
        if binding.get(key) != value:
            errors.append(
                f"specialization_data.schema_binding.{key}: "
                f"expected {value!r}, found {binding.get(key)!r}"
            )

    controls = specialization.get("controls", {})
    if not isinstance(controls, dict):
        errors.append("specialization_data.controls must be an object")
        controls = {}
    for key in REQUIRED_CONTROLS:
        if controls.get(key) is not True:
            errors.append(f"required control disabled: {key}")

    if set(specialization) - {"schema_binding", "controls"}:
        errors.append("unexpected MATHSOLVE specialization_data field")

    if "GCL-AGENT-CONTINUITY-001@1.0.0" not in agents_text:
        errors.append("AGENTS.md does not bind continuity policy")

    return errors


def schema_binding_errors() -> list[str]:
    errors: list[str] = []
    if not SCHEMA.is_file():
        return ["missing pinned common adoption schema snapshot"]

    observed_blob = git_blob_sha(SCHEMA)
    if observed_blob != SCHEMA_BLOB_SHA:
        errors.append(
            f"pinned schema blob mismatch: expected {SCHEMA_BLOB_SHA}, found {observed_blob}"
        )
        return errors

    try:
        schema = load_json(SCHEMA)
    except Exception as exc:
        return [f"invalid pinned schema JSON: {exc}"]

    expected_schema_markers = {
        "$id": "https://grandchallenge.ai/schemas/GCL-AGENT-CONTINUITY-ADOPTION-001.schema.json",
        "type": "object",
        "additionalProperties": False,
    }
    for key, value in expected_schema_markers.items():
        if schema.get(key) != value:
            errors.append(f"pinned schema marker {key}: expected {value!r}, found {schema.get(key)!r}")
    properties = schema.get("properties", {})
    if properties.get("schema_id", {}).get("const") != "GCL-AGENT-CONTINUITY-ADOPTION-001":
        errors.append("pinned schema has unexpected schema_id contract")
    if properties.get("policy_id", {}).get("const") != "GCL-AGENT-CONTINUITY-001":
        errors.append("pinned schema has unexpected policy_id contract")
    return errors


def adversarial_errors(record: dict[str, Any], agents_text: str) -> list[str]:
    errors: list[str] = []

    def rejected(label: str, mutate: Callable[[dict[str, Any]], None]) -> None:
        candidate = copy.deepcopy(record)
        mutate(candidate)
        if not adoption_errors(candidate, agents_text):
            errors.append(f"adversarial mutation was not rejected: {label}")

    rejected("policy_id drift", lambda r: r.update(policy_id="OTHER"))
    rejected("policy version drift", lambda r: r.update(version="9.9.9"))
    rejected("authority path drift", lambda r: r.update(authority_path="elsewhere.md"))
    rejected("required=false", lambda r: r.update(required=False))
    rejected(
        "authority expansion",
        lambda r: r["authority_preservation"].update(authority_changed=True),
    )
    rejected(
        "certification authority expansion",
        lambda r: r["authority_preservation"].update(certification_authority_changed=True),
    )
    rejected("missing local validator", lambda r: r.pop("local_validator"))
    rejected("missing specialization_data", lambda r: r.pop("specialization_data"))
    rejected(
        "schema blob drift",
        lambda r: r["specialization_data"]["schema_binding"].update(schema_blob_sha="0" * 40),
    )
    rejected(
        "mutable remote fetch",
        lambda r: r["specialization_data"]["schema_binding"].update(mutable_remote_fetch_allowed=True),
    )
    rejected(
        "disabled exact-head preflight",
        lambda r: r["specialization_data"]["controls"].update(exact_head_preflight=False),
    )
    return errors


def main() -> int:
    errors: list[str] = []
    for path in (ADOPTION, AGENTS, SCHEMA):
        if not path.exists():
            errors.append(f"missing required file: {path.relative_to(ROOT)}")

    record: dict[str, Any] = {}
    agents_text = ""
    if ADOPTION.exists():
        try:
            loaded = load_json(ADOPTION)
            if not isinstance(loaded, dict):
                errors.append("adoption record must be an object")
            else:
                record = loaded
        except Exception as exc:
            errors.append(f"invalid adoption JSON: {exc}")
    if AGENTS.exists():
        agents_text = AGENTS.read_text(encoding="utf-8")

    if record:
        errors.extend(adoption_errors(record, agents_text))
    errors.extend(schema_binding_errors())

    if record and not errors:
        errors.extend(adversarial_errors(record, agents_text))

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(
        "MATHSOLVE continuity adoption: PASS "
        f"(INTELLECT schema {SCHEMA_AUTHORITY_COMMIT}:{SCHEMA_BLOB_SHA})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
