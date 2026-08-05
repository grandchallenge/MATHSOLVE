from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

import validate_vgse_activation as module


class SuccessorOverlayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.vgse_overlay = module.load_json(module.OVERLAY_PATH)
        cls.euclid_overlay = module.load_json(module.EUCLID_OVERLAY_PATH)

    def vgse_errors(self, mutation=None):
        data = copy.deepcopy(self.vgse_overlay)
        if mutation is not None:
            mutation(data)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "overlay.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            return module.vgse_overlay_errors(overlay_path=path)

    def euclid_errors(self, mutation=None):
        data = copy.deepcopy(self.euclid_overlay)
        if mutation is not None:
            mutation(data)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "euclid-overlay.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            return module.euclid_overlay_errors(overlay_path=path)

    def test_current_successor_overlays_pass(self):
        self.assertEqual(module.merged_current_cert_route_errors(), [])

    def test_vgse_route_cannot_be_claimed_present_before_registration(self):
        errors = self.vgse_errors(lambda data: data["campaign"].__setitem__("route_registry_entry_present", True))
        self.assertTrue(any("registered" in error or "False was expected" in error for error in errors))

    def test_vgse_pending_route_cannot_adjudicate(self):
        errors = self.vgse_errors(lambda data: data["campaign"].__setitem__("may_adjudicate", True))
        self.assertTrue(any("may_adjudicate" in error or "False was expected" in error for error in errors))

    def test_vgse_pending_route_cannot_issue_output(self):
        errors = self.vgse_errors(lambda data: data["campaign"].__setitem__("may_issue_certificate_output", True))
        self.assertTrue(any("may_issue_certificate_output" in error or "False was expected" in error for error in errors))

    def test_vgse_manifest_digest_is_pinned(self):
        errors = self.vgse_errors(lambda data: data["campaign"]["manifest"].__setitem__("digest", "0" * 40))
        self.assertTrue(any("manifest identity drift" in error for error in errors))

    def test_vgse_handoff_digest_is_pinned(self):
        errors = self.vgse_errors(lambda data: data["campaign"]["handoff"].__setitem__("digest", "0" * 40))
        self.assertTrue(any("handoff identity drift" in error for error in errors))

    def test_vgse_base_registry_digest_is_pinned(self):
        errors = self.vgse_errors(lambda data: data["base_registry"].__setitem__("digest", "0" * 40))
        self.assertTrue(any("base_registry" in error and "identity drift" in error for error in errors))

    def test_vgse_cannot_pass_judgment_before_route_adjudication(self):
        errors = module.merged_provider_gate_errors("VGSE-001", "JUDGMENT")
        self.assertTrue(any("not an adjudicated" in error for error in errors))

    def test_vgse_cannot_promote_claims(self):
        errors = module.merged_provider_gate_errors("VGSE-001", "CLAIM_PROMOTION")
        self.assertTrue(any("not promotion eligible" in error for error in errors))

    def test_euclid_ready_handoff_retains_pending_route(self):
        record = self.euclid_overlay["campaign"]
        self.assertEqual(record["handoff_state"], "ready")
        self.assertEqual(record["route_state"], "pending")
        self.assertIsNone(record["cert_output"])
        self.assertIsNone(record["qualification_scope"])
        self.assertFalse(record["mathematical_target_proved"])
        self.assertFalse(record["may_adjudicate"])
        self.assertFalse(record["may_issue_certificate_output"])

    def test_euclid_route_cannot_be_claimed_registered(self):
        errors = self.euclid_errors(lambda data: data["campaign"].__setitem__("route_registry_entry_present", True))
        self.assertTrue(any("registered" in error or "False was expected" in error for error in errors))

    def test_euclid_ready_handoff_cannot_inflate_route_state(self):
        errors = self.euclid_errors(lambda data: data["campaign"].__setitem__("route_state", "ready"))
        self.assertTrue(any("pending" in error or "was expected" in error for error in errors))

    def test_euclid_cannot_issue_cert_output(self):
        errors = self.euclid_errors(lambda data: data["campaign"].__setitem__("may_issue_certificate_output", True))
        self.assertTrue(any("may_issue_certificate_output" in error or "False was expected" in error for error in errors))

    def test_euclid_manifest_digest_is_pinned(self):
        errors = self.euclid_errors(lambda data: data["campaign"]["manifest"].__setitem__("digest", "0" * 40))
        self.assertTrue(any("manifest identity drift" in error for error in errors))

    def test_euclid_handoff_digest_is_pinned(self):
        errors = self.euclid_errors(lambda data: data["campaign"]["handoff"].__setitem__("digest", "0" * 40))
        self.assertTrue(any("handoff identity drift" in error for error in errors))

    def test_euclid_predecessor_overlay_is_pinned(self):
        errors = self.euclid_errors(lambda data: data["predecessor_overlay"].__setitem__("digest", "0" * 40))
        self.assertTrue(any("predecessor_overlay" in error and "identity drift" in error for error in errors))

    def test_euclid_cannot_pass_judgment_before_cert_adjudication(self):
        errors = module.merged_provider_gate_errors("EUCLID-GCD-E2E-001", "JUDGMENT")
        self.assertTrue(any("not an adjudicated" in error for error in errors))

    def test_euclid_cannot_promote_candidate_claims(self):
        errors = module.merged_provider_gate_errors("EUCLID-GCD-E2E-001", "CLAIM_PROMOTION")
        self.assertTrue(any("not promotion eligible" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
