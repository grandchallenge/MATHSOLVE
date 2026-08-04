#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
import unittest

from validate_candidate_admission import (
    HANDOFF_PATH,
    MANIFEST_PATH,
    OVERLAY_PATH,
    RECORD_PATH,
    validation_errors,
)


class CandidateAdmissionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.record = json.loads(RECORD_PATH.read_text(encoding="utf-8"))
        cls.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        cls.handoff = json.loads(HANDOFF_PATH.read_text(encoding="utf-8"))
        cls.overlay = json.loads(OVERLAY_PATH.read_text(encoding="utf-8"))

    def errors(self, *, record=None, manifest=None, handoff=None, overlay=None):
        return validation_errors(
            copy.deepcopy(self.record if record is None else record),
            manifest=copy.deepcopy(self.manifest if manifest is None else manifest),
            handoff=copy.deepcopy(self.handoff if handoff is None else handoff),
            overlay=copy.deepcopy(self.overlay if overlay is None else overlay),
            verify_local_blobs=False,
        )

    def test_current_activation_record_passes(self) -> None:
        self.assertEqual(validation_errors(), [])

    def test_candidate_cannot_become_active_before_cross_repository_activation(self) -> None:
        record = copy.deepcopy(self.record)
        record["active_portfolio_member"] = True
        self.assertTrue(any("active Programme portfolio" in error for error in self.errors(record=record)))

    def test_programme_decision_digest_is_pinned(self) -> None:
        record = copy.deepcopy(self.record)
        record["programme_authority"]["decision"]["digest"] = "0" * 40
        self.assertTrue(any("Programme decision identity drift" in error for error in self.errors(record=record)))

    def test_provider_state_cannot_roll_back(self) -> None:
        record = copy.deepcopy(self.record)
        record["source_provenance"]["state"] = "unverified_candidate"
        self.assertTrue(any("source state rolled back" in error for error in self.errors(record=record)))

    def test_provider_manifest_identity_is_pinned(self) -> None:
        record = copy.deepcopy(self.record)
        record["source_provenance"]["provider_manifest"]["digest"] = "0" * 40
        self.assertTrue(any("provider manifest identity drift" in error for error in self.errors(record=record)))

    def test_manifest_identity_is_pinned(self) -> None:
        record = copy.deepcopy(self.record)
        record["activation_artifacts"]["campaign_manifest"]["digest"] = "0" * 40
        self.assertTrue(any("campaign manifest identity drift" in error for error in self.errors(record=record)))

    def test_handoff_identity_is_pinned(self) -> None:
        record = copy.deepcopy(self.record)
        record["activation_artifacts"]["cert_handoff"]["digest"] = "0" * 40
        self.assertTrue(any("Cert handoff identity drift" in error for error in self.errors(record=record)))

    def test_overlay_identity_is_pinned(self) -> None:
        record = copy.deepcopy(self.record)
        record["activation_artifacts"]["current_route_overlay"]["digest"] = "0" * 40
        self.assertTrue(any("current-route overlay identity drift" in error for error in self.errors(record=record)))

    def test_route_cannot_be_claimed_registered(self) -> None:
        record = copy.deepcopy(self.record)
        record["activation_artifacts"]["current_route_overlay"]["route_registry_entry_present"] = True
        self.assertTrue(any("claimed before protected registration" in error for error in self.errors(record=record)))

    def test_handoff_cannot_become_ready_before_route_registration(self) -> None:
        handoff = copy.deepcopy(self.handoff)
        handoff["status"] = "ready"
        self.assertTrue(any("blocked and pending" in error for error in self.errors(handoff=handoff)))

    def test_overlay_cannot_adjudicate(self) -> None:
        overlay = copy.deepcopy(self.overlay)
        overlay["campaign"]["may_adjudicate"] = True
        self.assertTrue(any("may_adjudicate" in error for error in self.errors(overlay=overlay)))

    def test_overlay_cannot_issue_certificate_output(self) -> None:
        overlay = copy.deepcopy(self.overlay)
        overlay["campaign"]["may_issue_certificate_output"] = True
        self.assertTrue(any("may_issue_certificate_output" in error for error in self.errors(overlay=overlay)))

    def test_manifest_cannot_become_promotion_eligible(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["promotion"]["eligible"] = True
        manifest["promotion"]["blockers"] = []
        self.assertTrue(any("promotion eligible" in error for error in self.errors(manifest=manifest)))

    def test_programme_active_registry_gate_cannot_close_early(self) -> None:
        record = copy.deepcopy(self.record)
        record["admission_gates"]["programme_active_registry_updated"] = True
        self.assertTrue(any("programme_active_registry_updated" in error for error in self.errors(record=record)))

    def test_cert_route_gate_cannot_close_early(self) -> None:
        record = copy.deepcopy(self.record)
        record["admission_gates"]["cert_route_registered"] = True
        self.assertTrue(any("cert_route_registered" in error for error in self.errors(record=record)))

    def test_commercial_claim_cannot_be_authorized(self) -> None:
        record = copy.deepcopy(self.record)
        record["claim_boundary"]["commercial_claim_authorized"] = True
        self.assertTrue(any("commercial_claim_authorized" in error for error in self.errors(record=record)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
