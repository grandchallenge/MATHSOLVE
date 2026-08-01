from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_openai_ten_proofs_result_family_handoffs",
    ROOT / "ci" / "validate_openai_ten_proofs_result_family_handoffs.py",
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class OpenAITenProofsResultFamilyHandoffTests(unittest.TestCase):
    def setUp(self) -> None:
        self.registry = json.loads(MODULE.REGISTRY_PATH.read_text(encoding="utf-8"))
        self.packets = {
            path.stem: json.loads(path.read_text(encoding="utf-8"))
            for path in sorted(MODULE.PACKET_DIR.glob("*.json"))
        }
        self.blobs = {
            path.stem: MODULE.git_blob_sha1(path)
            for path in sorted(MODULE.PACKET_DIR.glob("*.json"))
        }

    def errors(self, *, registry=None, packets=None, blobs=None):
        return MODULE.validation_errors(
            registry=copy.deepcopy(self.registry if registry is None else registry),
            packets=copy.deepcopy(self.packets if packets is None else packets),
            packet_blobs=copy.deepcopy(self.blobs if blobs is None else blobs),
        )

    def test_current_registry_and_packets_pass(self) -> None:
        self.assertEqual(self.errors(), [])

    def test_missing_packet_is_rejected(self) -> None:
        packets = copy.deepcopy(self.packets)
        packets.pop("OTP-F-EHRHART")
        self.assertTrue(self.errors(packets=packets))

    def test_unregistered_packet_is_rejected(self) -> None:
        packets = copy.deepcopy(self.packets)
        packets["OTP-X-AGGREGATE"] = copy.deepcopy(packets["OTP-F-EHRHART"])
        self.assertTrue(self.errors(packets=packets))

    def test_semantic_record_digest_drift_is_rejected(self) -> None:
        packets = copy.deepcopy(self.packets)
        packets["OTP-J1-COMPACTNESS"]["authority"]["semantic_record"]["digest"] = "0" * 40
        self.assertTrue(self.errors(packets=packets))

    def test_packet_blob_drift_is_rejected(self) -> None:
        registry = copy.deepcopy(self.registry)
        registry["packets"][0]["digest"] = "0" * 40
        self.assertTrue(self.errors(registry=registry))

    def test_review_identity_drift_is_rejected(self) -> None:
        packets = copy.deepcopy(self.packets)
        packets["OTP-F-EHRHART"]["authority"]["forge_semantic_review"]["review_id"] = 1
        self.assertTrue(self.errors(packets=packets))

    def test_reviewed_head_drift_is_rejected(self) -> None:
        packets = copy.deepcopy(self.packets)
        packets["OTP-J2-TWO-DEGENERATE"]["authority"]["forge_semantic_reviewed_head"] = "0" * 40
        self.assertTrue(self.errors(packets=packets))

    def test_duplicate_handoff_identity_is_rejected(self) -> None:
        packets = copy.deepcopy(self.packets)
        packets["OTP-J1-COMPACTNESS"]["handoff_id"] = packets["OTP-F-EHRHART"]["handoff_id"]
        self.assertTrue(self.errors(packets=packets))

    def test_registered_cert_route_is_rejected(self) -> None:
        packets = copy.deepcopy(self.packets)
        packets["OTP-F-EHRHART"]["requested_adjudication"]["current_route_state"] = "ready"
        self.assertTrue(self.errors(packets=packets))

    def test_cert_output_is_rejected(self) -> None:
        packets = copy.deepcopy(self.packets)
        packets["OTP-J1-COMPACTNESS"]["requested_adjudication"]["cert_output"] = {
            "state": "qualified"
        }
        self.assertTrue(self.errors(packets=packets))

    def test_branch_adjudication_is_rejected(self) -> None:
        packets = copy.deepcopy(self.packets)
        packets["OTP-J2-TWO-DEGENERATE"]["requested_adjudication"]["may_adjudicate_on_branch"] = True
        self.assertTrue(self.errors(packets=packets))

    def test_proof_promotion_is_rejected(self) -> None:
        packets = copy.deepcopy(self.packets)
        packets["OTP-F-EHRHART"]["route_controls"]["may_claim_mathematical_proof"] = True
        self.assertTrue(self.errors(packets=packets))

    def test_aggregate_handoff_injection_is_rejected(self) -> None:
        registry = copy.deepcopy(self.registry)
        registry["route_controls"]["aggregate_handoff"] = {
            "handoff_id": "MC-OTP-HANDOFF-ALL"
        }
        self.assertTrue(self.errors(registry=registry))

    def test_semantic_count_inflation_is_rejected(self) -> None:
        registry = copy.deepcopy(self.registry)
        registry["semantic_gate"]["clear_count"] = 12
        self.assertTrue(self.errors(registry=registry))

    def test_blocked_repair_lane_removal_is_rejected(self) -> None:
        registry = copy.deepcopy(self.registry)
        registry["blocked_repair_lanes"] = ["OTP-C-PERMANENT"]
        self.assertTrue(self.errors(registry=registry))

    def test_all_lean_debt_cannot_reopen_family_gates(self) -> None:
        registry = copy.deepcopy(self.registry)
        registry["aggregate_integration"]["reopens_family_replay"] = True
        self.assertTrue(self.errors(registry=registry))

    def test_cert_state_inflation_is_rejected(self) -> None:
        registry = copy.deepcopy(self.registry)
        registry["cert_state"]["accepted_handoff_count"] = 3
        self.assertTrue(self.errors(registry=registry))


if __name__ == "__main__":
    unittest.main()
