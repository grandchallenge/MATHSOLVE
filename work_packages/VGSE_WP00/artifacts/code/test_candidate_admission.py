#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]
RECORD = ROOT / "candidate_admission.json"


class CandidateAdmissionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.record = json.loads(RECORD.read_text(encoding="utf-8"))

    def test_exact_programme_candidate_identity(self) -> None:
        self.assertEqual(self.record["campaign_id"], "VGSE-001")
        self.assertEqual(self.record["lifecycle_state"], "candidate")
        self.assertFalse(self.record["active_portfolio_member"])
        authority = self.record["programme_authority"]
        self.assertEqual(
            authority["merge_commit"],
            "b78b73e73a62cdb3d54f08ba1af104ceac9c90b8",
        )
        self.assertEqual(
            authority["candidate_registry"]["digest"],
            "9b1a307fde8bfe814210088d544ec8b03f2b413e",
        )
        self.assertEqual(
            authority["runtime_contract"]["digest"],
            "d1503fba284aee29fb517a554ee3440da691fd16",
        )
        self.assertFalse(authority["candidate_work_can_self_admit"])

    def test_source_remains_unverified_candidate(self) -> None:
        source = self.record["source_provenance"]
        self.assertEqual(source["state"], "unverified_candidate")
        self.assertEqual(source["forge_issue"], 32)
        self.assertIsNone(source["provider_manifest"])
        self.assertEqual(
            source["candidate_source"]["candidate_sha256"],
            "e513789426ae6247438920bfc80cfba6bd9c32dc6799a4f7873d806a865f95de",
        )

    def test_candidate_authority_fails_closed(self) -> None:
        solve = self.record["solve_candidate"]
        self.assertEqual(solve["issue"], 84)
        self.assertEqual(solve["pull_request"], 85)
        self.assertEqual(solve["state"], "draft_candidate_implementation")
        self.assertTrue(solve["may_merge_candidate_work_package"])
        for field in (
            "may_create_campaign_manifest",
            "may_create_cert_handoff",
            "may_create_adjudication",
            "may_create_promotion_record",
        ):
            self.assertFalse(solve[field])
        cert = self.record["certification_candidate"]
        self.assertEqual(cert["state"], "pre_route_candidate")
        self.assertIsNone(cert["route_registry_entry"])
        self.assertFalse(cert["may_adjudicate"])

    def test_no_admission_gate_or_downstream_claim_is_inflated(self) -> None:
        self.assertTrue(all(value is False for value in self.record["admission_gates"].values()))
        boundary = self.record["claim_boundary"]
        self.assertTrue(boundary["candidate_registered_not_admitted"])
        for field, value in boundary.items():
            if field != "candidate_registered_not_admitted":
                self.assertFalse(value, field)


if __name__ == "__main__":
    unittest.main(verbosity=2)
