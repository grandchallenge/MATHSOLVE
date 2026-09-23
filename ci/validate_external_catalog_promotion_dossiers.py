#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "external_catalog_promotion_dossier.schema.json"
PROMOTIONS = ROOT / "promotions" / "external_catalog"


def validate_document(document: dict) -> list[str]:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    return [error.message for error in Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(document)]


def main() -> int:
    errors: list[str] = []
    for path in sorted(PROMOTIONS.glob("*.json")) if PROMOTIONS.exists() else []:
        try:
            document = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path}: {exc}")
            continue
        errors.extend(f"{path}: {error}" for error in validate_document(document))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("validated all reviewed external-catalog promotion dossiers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
