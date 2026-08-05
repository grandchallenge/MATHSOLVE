from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

import validate_vgse_activation as module


class DiophantineSuccessorOverlayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.overlay = module.load_json(module.DIO_OVERLAY_PATH)

    def errors(self, mutation=None):
        data = copy.deepcopy(self.overlay)
        if mutation is not None:
            mutation(data)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "diophantine-overlay.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            return module.diophantine_overlay_errors(overlay_path=path)

    def test_current_successor_chain_passes(self):
        self.assertEqual(module.merged_current_cert_route_errors(), [])

    def test_ready_handoff_retains_pending_route(self):
        record = self.overlay["campaign"]
        self.assertEqual(record["handoff_state"], "ready")
        self.assertEqual(record["route_state"], "pending")
        self.assertFalse(record["route_registry_entry_present"])
        self.assertIsNone(record["cert_output"])
        self.assertIsNone(record["qualification_scope"])
        self.assertFalse(record["mathematical_target_proved"])
        self.assertFalse(record["may_adjudicate"])
        self.assertFalse(record["may_issue_certificate_output"])

    def test_route_cannot_be_claimed_registered(self):
        errors = self.errors(lambda d: d["campaign"].__setitem__("route_registry_entry_present", True))
        self.assertTrue(any("registered" in error or "False was expected" in error for error in errors))

    def test_ready_handoff_cannot_inflate_route_state(self):
        errors = self.errors(lambda d: d["campaign"].__setitem__("route_state", "ready"))
        self.assertTrue(any("pending" in error or "was expected" in error for error in errors))

    def test_manifest_digest_is_pinned(self):
        errors = self.errors(lambda d: d["campaign"]["manifest"].__setitem__("digest", "0" * 40))
        self.assertTrue(any("manifest identity drift" in error for error in errors))

    def test_handoff_digest_is_pinned(self):
        errors = self.errors(lambda d: d["campaign"]["handoff"].__setitem__("digest", "0" * 40))
        self.assertTrue(any("handoff identity drift" in error for error in errors))

    def test_predecessor_overlay_is_pinned(self):
        errors = self.errors(lambda d: d["predecessor_overlay"].__setitem__("digest", "0" * 40))
        self.assertTrue(any("predecessor_overlay" in error and "identity drift" in error for error in errors))

    def test_cannot_pass_judgment_before_cert_adjudication(self):
        errors = module.merged_provider_gate_errors(module.DIO_ID, "JUDGMENT")
        self.assertTrue(any("not an adjudicated" in error for error in errors))

    def test_cannot_promote_candidate_claims(self):
        errors = module.merged_provider_gate_errors(module.DIO_ID, "CLAIM_PROMOTION")
        self.assertTrue(any("not promotion eligible" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
