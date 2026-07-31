#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
import pathlib
import unittest

from validate_candidate_admission import RECORD_PATH, validation_errors


class CandidateAdmissionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.record = json.loads(RECORD_PATH.read_text(encoding="utf-8"))

    def errors(self, record=None):
        return validation_errors(copy.deepcopy(self.record if record is None else record))

    def test_current_candidate_record_passes(self) -> None:
        self.assertEqual(validation_errors(), [])

    def test_candidate_cannot_become_active(self) -> None:
        record = copy.deepcopy(self.record)
        record["active_portfolio_member"] = True
        self.assertTrue(any("active portfolio" in error for error in self.errors(record)))

    def test_source_cannot_be_marked_verified_without_manifest(self) -> None:
        record = copy.deepcopy(self.record)
        record["source_provenance"]["state"] = "provider_verified"
        self.assertTrue(any("source provenance inflated" in error for error in self.errors(record)))

    def test_candidate_cannot_create_campaign_manifest(self) -> None:
        record = copy.deepcopy(self.record)
        record["solve_candidate"]["may_create_campaign_manifest"] = True
        self.assertTrue(any("may_create_campaign_manifest" in error for error in self.errors(record)))

    def test_candidate_cannot_create_cert_handoff(self) -> None:
        record = copy.deepcopy(self.record)
        record["solve_candidate"]["may_create_cert_handoff"] = True
        self.assertTrue(any("may_create_cert_handoff" in error for error in self.errors(record)))

    def test_candidate_cannot_create_adjudication(self) -> None:
        record = copy.deepcopy(self.record)
        record["solve_candidate"]["may_create_adjudication"] = True
        self.assertTrue(any("may_create_adjudication" in error for error in self.errors(record)))

    def test_pre_route_cert_candidate_cannot_adjudicate(self) -> None:
        record = copy.deepcopy(self.record)
        record["certification_candidate"]["may_adjudicate"] = True
        self.assertTrue(any("may not adjudicate" in error for error in self.errors(record)))

    def test_admission_gate_cannot_close_without_evidence(self) -> None:
        record = copy.deepcopy(self.record)
        record["admission_gates"]["forge_provider_manifest_admitted"] = True
        self.assertTrue(any("admission gate inflated" in error for error in self.errors(record)))

    def test_commercial_claim_cannot_be_authorized(self) -> None:
        record = copy.deepcopy(self.record)
        record["claim_boundary"]["commercial_claim_authorized"] = True
        self.assertTrue(any("commercial_claim_authorized" in error for error in self.errors(record)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
