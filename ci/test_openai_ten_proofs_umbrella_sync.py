from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "work_packages" / "OPENAI_TEN_PROOFS_WP00" / "umbrella_sync.json"
SCHEMA = ROOT / "schemas" / "openai_ten_proofs_umbrella_sync.schema.json"


class OpenAITenProofsUmbrellaSyncTests(unittest.TestCase):
    def setUp(self) -> None:
        self.record = json.loads(RECORD.read_text(encoding="utf-8"))
        self.validator = Draft202012Validator(json.loads(SCHEMA.read_text(encoding="utf-8")))

    def errors(self, record):
        return list(self.validator.iter_errors(record))

    def test_current_record_is_valid(self) -> None:
        self.assertEqual(self.errors(self.record), [])

    def test_current_and_historical_roots_cannot_be_conflated(self) -> None:
        record = copy.deepcopy(self.record)
        record["source_subject"]["current_official"]["commit"] = record["source_subject"]["historical_disconnected"]["commit"]
        self.assertTrue(self.errors(record))

    def test_replay_clear_count_is_exact(self) -> None:
        record = copy.deepcopy(self.record)
        record["replay_gate"]["result_family_clear_count"] = 11
        self.assertTrue(self.errors(record))

    def test_all_import_failure_does_not_reopen_replay(self) -> None:
        record = copy.deepcopy(self.record)
        record["aggregate_integration"]["reopens_replay_gate"] = True
        self.assertTrue(self.errors(record))

    def test_semantic_audit_is_allowed_but_handoffs_are_not(self) -> None:
        self.assertTrue(self.record["route_controls"]["may_start_statement_concordance"])
        for field in ("may_emit_result_family_mathcert_handoff", "may_emit_aggregate_mathcert_handoff", "may_claim_statement_equivalence", "may_promote_mathematical_result"):
            with self.subTest(field=field):
                record = copy.deepcopy(self.record)
                record["route_controls"][field] = True
                self.assertTrue(self.errors(record))

    def test_first_tranche_and_blocked_lanes_are_closed(self) -> None:
        for field in ("first_tranche", "blocked_repair_lanes"):
            record = copy.deepcopy(self.record)
            record["semantic_gate"][field] = []
            self.assertTrue(self.errors(record))

    def test_authority_blobs_are_exact(self) -> None:
        record = copy.deepcopy(self.record)
        record["authority"]["theorem_matrix_blob"] = "0" * 40
        self.assertTrue(self.errors(record))

    def test_unexpected_route_field_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["route_controls"]["aggregate_certified"] = True
        self.assertTrue(self.errors(record))


if __name__ == "__main__":
    unittest.main()
