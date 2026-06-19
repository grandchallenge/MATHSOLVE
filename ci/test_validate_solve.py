#!/usr/bin/env python3
"""Regression test for unresolved graph references."""
from pathlib import Path

from validate_solve import validate_ledger


def main() -> int:
    ledger = {
        "claims": [
            {
                "claim_id": "TEST-C001",
                "claim_text": "test",
                "claim_class": "HEURISTIC",
                "support_type": "HEURISTIC_ARGUMENT",
                "status": "DRAFT",
                "source_or_artifact": ["https://example.com"],
                "promotion_condition": "review",
                "knowledge_graph_refs": ["MISSING-NODE"],
            }
        ]
    }
    errors = validate_ledger(ledger, Path("test.yaml"), {"KNOWN-NODE"}, {})
    assert any("unresolved knowledge_graph_ref" in error for error in errors)
    print("MATHSOLVE validator rejection tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
