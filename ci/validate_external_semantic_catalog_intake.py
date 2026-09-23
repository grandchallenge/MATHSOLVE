#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "governance" / "external_semantic_catalog_intake.json"
SCHEMA = ROOT / "schemas" / "external_semantic_catalog_intake.schema.json"
EXPECTED_PROGRAMME_COMMIT = "4b78daac0b85298957b52e34687423e5442b5e51"
EXPECTED_PROGRAMME_BLOB = "8544fcd383e68a1ca0acd060e56bb0e7d0fe16a0"
EXPECTED_CHAIDEZ_COMMIT = "861479cb599df01f6e9cafc8647fdefe56249d29"
EXPECTED_CHAIDEZ_BLOB = "29e12c793d116c6c3af121c04486c5daa6c09e1e"


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def validation_errors(instance: dict[str, Any] | None = None) -> list[str]:
    policy = instance if instance is not None else load(POLICY)
    errors = [error.message for error in Draft202012Validator(load(SCHEMA), format_checker=FormatChecker()).iter_errors(policy)]
    authority = policy.get("programme_authority", {})
    if authority.get("commit") != EXPECTED_PROGRAMME_COMMIT or authority.get("git_blob_sha1") != EXPECTED_PROGRAMME_BLOB:
        errors.append("Programme semantic catalog authority identity drift")
    chaidez = policy.get("chaidez_authority", {})
    if (chaidez.get("commit"), chaidez.get("git_blob_sha1")) != (EXPECTED_CHAIDEZ_COMMIT, EXPECTED_CHAIDEZ_BLOB):
        errors.append("Programme Chaidez authority identity drift")
    dossier_gate = policy.get("chaidez_dossier_gate", {})
    if dossier_gate.get("catalog_entries_require_dossier") is not False or dossier_gate.get("trigger") != "REVIEWED_PROMOTION_TO_MATHSOLVE":
        errors.append("Chaidez dossier boundary drift")
    forbidden = policy.get("forbidden_authority", {})
    if any(value is not False for value in forbidden.values()):
        errors.append("catalog authority inflation")
    return errors


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("validated reviewed-proposal intake, campaign-concordance gate, Claim Ledger isolation, and separate MATHCERT handoff boundary")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
