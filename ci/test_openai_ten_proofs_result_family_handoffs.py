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
        self.packets = {path.stem: json.loads(path.read_text(encoding="utf-8")) for path in sorted(MODULE.PACKET_DIR.glob("*.json"))}
        self.blobs = {path.stem: MODULE.git_blob_sha1(path) for path in sorted(MODULE.PACKET_DIR.glob("*.json"))}

    def errors(self, *, registry=None, packets=None, blobs=None):
        return MODULE.validation_errors(
            registry=copy.deepcopy(self.registry if registry is None else registry),
            packets=copy.deepcopy(self.packets if packets is None else packets),
            packet_blobs=copy.deepcopy(self.blobs if blobs is None else blobs),
        )

    def mutate_projection(self, key, path, value):
        packets = copy.deepcopy(self.packets)
        target = packets[key]["target_scope"]["source_projection"]
        for part in path[:-1]:
            target = target[part]
        target[path[-1]] = value
        return packets

    def test_current_registry_and_packets_pass(self):
        self.assertEqual(self.errors(), [])

    def test_missing_packet_is_rejected(self):
        packets = copy.deepcopy(self.packets); packets.pop("OTP-C-PERMANENT-FULL-FORMULA")
        self.assertTrue(self.errors(packets=packets))

    def test_unknown_packet_is_rejected(self):
        packets = copy.deepcopy(self.packets); packets["OTP-X-AGGREGATE"] = copy.deepcopy(packets["OTP-F-EHRHART"])
        self.assertTrue(self.errors(packets=packets))

    def test_historical_permanent_blob_is_immutable(self):
        blobs = copy.deepcopy(self.blobs); blobs["OTP-C-PERMANENT"] = "0" * 40
        self.assertTrue(self.errors(blobs=blobs))

    def test_full_formula_blob_is_bound(self):
        blobs = copy.deepcopy(self.blobs); blobs["OTP-C-PERMANENT-FULL-FORMULA"] = "0" * 40
        self.assertTrue(self.errors(blobs=blobs))

    def test_registry_packet_digest_drift_is_rejected(self):
        registry = copy.deepcopy(self.registry); registry["packets"][4]["digest"] = "0" * 40
        self.assertTrue(self.errors(registry=registry))

    def test_duplicate_handoff_identity_is_rejected(self):
        packets = copy.deepcopy(self.packets)
        packets["OTP-C-PERMANENT-FULL-FORMULA"]["handoff_id"] = packets["OTP-C-PERMANENT"]["handoff_id"]
        self.assertTrue(self.errors(packets=packets))

    def test_full_formula_target_substitution_is_rejected(self):
        packets = copy.deepcopy(self.packets)
        packets["OTP-C-PERMANENT-FULL-FORMULA"]["target_scope"]["lean_theorems"][0] = "PermanentFormulaLowerBound.permanent_divisionFree_formula_logarithmic_lower_bound"
        self.assertTrue(self.errors(packets=packets))

    def test_circuit_target_insertion_is_rejected(self):
        packets = copy.deepcopy(self.packets)
        packets["OTP-C-PERMANENT-FULL-FORMULA"]["target_scope"]["lean_theorems"].append("PermanentRollout.permanent_circuit_loglog_lower_bound")
        self.assertTrue(self.errors(packets=packets))

    def test_dimension_threshold_drift_is_rejected(self):
        self.assertTrue(self.errors(packets=self.mutate_projection("OTP-C-PERMANENT-FULL-FORMULA", ["dimension_threshold"], 31)))

    def test_log_base_drift_is_rejected(self):
        self.assertTrue(self.errors(packets=self.mutate_projection("OTP-C-PERMANENT-FULL-FORMULA", ["log_base"], 10)))

    def test_division_free_variable_constant_drift_is_rejected(self):
        self.assertTrue(self.errors(packets=self.mutate_projection("OTP-C-PERMANENT-FULL-FORMULA", ["division_free", "variable_leaf_constant"], 129)))

    def test_division_free_leaf_constant_drift_is_rejected(self):
        self.assertTrue(self.errors(packets=self.mutate_projection("OTP-C-PERMANENT-FULL-FORMULA", ["division_free", "leaf_count_constant"], 129)))

    def test_division_free_vertex_constant_drift_is_rejected(self):
        self.assertTrue(self.errors(packets=self.mutate_projection("OTP-C-PERMANENT-FULL-FORMULA", ["division_free", "vertex_count_constant"], 129)))

    def test_division_free_gate_constant_drift_is_rejected(self):
        self.assertTrue(self.errors(packets=self.mutate_projection("OTP-C-PERMANENT-FULL-FORMULA", ["division_free", "internal_gate_constant"], 255)))

    def test_rational_variable_constant_drift_is_rejected(self):
        self.assertTrue(self.errors(packets=self.mutate_projection("OTP-C-PERMANENT-FULL-FORMULA", ["rational", "variable_leaf_constant"], 193)))

    def test_rational_leaf_constant_drift_is_rejected(self):
        self.assertTrue(self.errors(packets=self.mutate_projection("OTP-C-PERMANENT-FULL-FORMULA", ["rational", "leaf_count_constant"], 193)))

    def test_rational_vertex_constant_drift_is_rejected(self):
        self.assertTrue(self.errors(packets=self.mutate_projection("OTP-C-PERMANENT-FULL-FORMULA", ["rational", "vertex_count_constant"], 193)))

    def test_rational_gate_constant_drift_is_rejected(self):
        self.assertTrue(self.errors(packets=self.mutate_projection("OTP-C-PERMANENT-FULL-FORMULA", ["rational", "internal_gate_constant"], 383)))

    def test_historical_pdf_equivalence_inflation_is_rejected(self):
        self.assertTrue(self.errors(packets=self.mutate_projection("OTP-C-PERMANENT-FULL-FORMULA", ["historical_pdf_byte_equivalence"], True)))

    def test_human_steward_authority_drift_is_rejected(self):
        packets = copy.deepcopy(self.packets)
        packets["OTP-C-PERMANENT-FULL-FORMULA"]["authority"]["human_steward_control_plan_comment"] = 1
        self.assertTrue(self.errors(packets=packets))

    def test_semantic_record_drift_is_rejected(self):
        packets = copy.deepcopy(self.packets)
        packets["OTP-C-PERMANENT-FULL-FORMULA"]["authority"]["semantic_record"]["digest"] = "0" * 40
        self.assertTrue(self.errors(packets=packets))

    def test_nonvacuity_witness_drift_is_rejected(self):
        packets = copy.deepcopy(self.packets)
        packets["OTP-C-PERMANENT-FULL-FORMULA"]["authority"]["nonvacuity_witness"]["digest"] = "0" * 40
        self.assertTrue(self.errors(packets=packets))

    def test_registered_route_is_rejected(self):
        packets = copy.deepcopy(self.packets)
        packets["OTP-C-PERMANENT-FULL-FORMULA"]["requested_adjudication"]["current_route_state"] = "ready"
        self.assertTrue(self.errors(packets=packets))

    def test_cert_output_is_rejected(self):
        packets = copy.deepcopy(self.packets)
        packets["OTP-C-PERMANENT-FULL-FORMULA"]["requested_adjudication"]["cert_output"] = {"state": "qualified"}
        self.assertTrue(self.errors(packets=packets))

    def test_branch_adjudication_is_rejected(self):
        packets = copy.deepcopy(self.packets)
        packets["OTP-C-PERMANENT-FULL-FORMULA"]["requested_adjudication"]["may_adjudicate_on_branch"] = True
        self.assertTrue(self.errors(packets=packets))

    def test_proof_promotion_is_rejected(self):
        packets = copy.deepcopy(self.packets)
        packets["OTP-C-PERMANENT-FULL-FORMULA"]["route_controls"]["may_claim_mathematical_proof"] = True
        self.assertTrue(self.errors(packets=packets))

    def test_circuit_authority_is_rejected(self):
        packets = copy.deepcopy(self.packets)
        packets["OTP-C-PERMANENT-FULL-FORMULA"]["route_controls"]["may_route_circuit_theorem"] = True
        self.assertTrue(self.errors(packets=packets))

    def test_historical_packet_mutation_authority_is_rejected(self):
        packets = copy.deepcopy(self.packets)
        packets["OTP-C-PERMANENT-FULL-FORMULA"]["route_controls"]["historical_variable_leaf_packet_mutable"] = True
        self.assertTrue(self.errors(packets=packets))

    def test_semantic_family_count_inflation_is_rejected(self):
        registry = copy.deepcopy(self.registry); registry["semantic_gate"]["clear_count"] = 5
        self.assertTrue(self.errors(registry=registry))

    def test_packet_count_drift_is_rejected(self):
        registry = copy.deepcopy(self.registry); registry["semantic_gate"]["packet_count"] = 4
        self.assertTrue(self.errors(registry=registry))

    def test_gapcvp_blocker_removal_is_rejected(self):
        registry = copy.deepcopy(self.registry); registry["blocked_repair_lanes"] = []
        self.assertTrue(self.errors(registry=registry))

    def test_circuit_successor_removal_is_rejected(self):
        registry = copy.deepcopy(self.registry); registry["permanent_unencoded_successors"].pop(0)
        self.assertTrue(self.errors(registry=registry))

    def test_aggregate_handoff_injection_is_rejected(self):
        registry = copy.deepcopy(self.registry); registry["route_controls"]["aggregate_handoff"] = {"handoff_id": "MC-OTP-HANDOFF-ALL"}
        self.assertTrue(self.errors(registry=registry))

    def test_all_lean_debt_cannot_reopen_gates(self):
        registry = copy.deepcopy(self.registry); registry["aggregate_integration"]["reopens_family_replay"] = True
        self.assertTrue(self.errors(registry=registry))

    def test_cert_state_inflation_is_rejected(self):
        registry = copy.deepcopy(self.registry); registry["cert_state"]["accepted_handoff_count"] = 1
        self.assertTrue(self.errors(registry=registry))

    def test_successor_separation_removal_is_rejected(self):
        registry = copy.deepcopy(self.registry); registry["route_controls"]["full_formula_successor_packet_separate"] = False
        self.assertTrue(self.errors(registry=registry))


if __name__ == "__main__":
    unittest.main()
