from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "ci" / "validate_openai_ten_proofs_result_family_handoffs.py"
SPEC = importlib.util.spec_from_file_location("handoff_validator", VALIDATOR_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def load_packets():
    return {path.stem: json.loads(path.read_text(encoding="utf-8")) for path in sorted(MODULE.PACKET_DIR.glob("*.json"))}


class PermanentCircuitHandoffMutationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.registry = json.loads(MODULE.REGISTRY_PATH.read_text(encoding="utf-8"))
        self.packets = load_packets()

    def packet_errors(self, mutate):
        packets = copy.deepcopy(self.packets)
        mutate(packets["OTP-C-PERMANENT-CIRCUIT"])
        return MODULE.validation_errors(registry=copy.deepcopy(self.registry), packets=packets)

    def registry_errors(self, mutate):
        registry = copy.deepcopy(self.registry)
        mutate(registry)
        return MODULE.validation_errors(registry=registry, packets=copy.deepcopy(self.packets))

    def test_current_surface_passes(self):
        self.assertEqual(MODULE.validation_errors(), [])

    def test_formula_target_insertion_rejected(self):
        self.assertTrue(self.packet_errors(lambda p: p["target_scope"]["source_projection"].__setitem__("formula_target_count", 1)))

    def test_threshold_drift_rejected(self):
        self.assertTrue(self.packet_errors(lambda p: p["target_scope"]["source_projection"].__setitem__("dimension_threshold", 65535)))

    def test_denominator_drift_rejected(self):
        self.assertTrue(self.packet_errors(lambda p: p["target_scope"]["source_projection"].__setitem__("finite_bound_denominator", 143)))

    def test_division_model_drift_rejected(self):
        self.assertTrue(self.packet_errors(lambda p: p["target_scope"]["source_projection"].__setitem__("division_allowed", True)))

    def test_fanout_convention_drift_rejected(self):
        self.assertTrue(self.packet_errors(lambda p: p["target_scope"]["source_projection"].__setitem__("fanout_reuse_allowed", False)))

    def test_size_measure_drift_rejected(self):
        self.assertTrue(self.packet_errors(lambda p: p["target_scope"]["source_projection"].__setitem__("input_gates_counted", True)))

    def test_target_omission_rejected(self):
        self.assertTrue(self.packet_errors(lambda p: p["target_scope"]["lean_theorems"].pop()))

    def test_target_inflation_rejected(self):
        self.assertTrue(self.packet_errors(lambda p: p["target_scope"]["lean_theorems"].append("PermanentRollout.unapproved_target")))

    def test_nonvacuity_substitution_rejected(self):
        self.assertTrue(self.packet_errors(lambda p: p["target_scope"]["nonvacuity_witnesses"].__setitem__(0, "PermanentRollout.fake_witness")))

    def test_forge_authority_substitution_rejected(self):
        self.assertTrue(self.packet_errors(lambda p: p["authority"].__setitem__("forge_semantic_merge", "0" * 40)))

    def test_replay_receipt_substitution_rejected(self):
        self.assertTrue(self.packet_errors(lambda p: p["replay_gate"].__setitem__("exact_job", 1)))

    def test_formula_route_authority_rejected(self):
        self.assertTrue(self.packet_errors(lambda p: p["route_controls"].__setitem__("may_route_formula_theorems", True)))

    def test_cert_acceptance_inference_rejected(self):
        self.assertTrue(self.packet_errors(lambda p: p["route_controls"].__setitem__("may_imply_mathcert_acceptance", True)))

    def test_adjudication_authority_rejected(self):
        self.assertTrue(self.packet_errors(lambda p: p["requested_adjudication"].__setitem__("may_adjudicate_on_branch", True)))

    def test_cert_output_insertion_rejected(self):
        self.assertTrue(self.packet_errors(lambda p: p["requested_adjudication"].__setitem__("cert_output", "forbidden")))

    def test_proof_promotion_rejected(self):
        self.assertTrue(self.packet_errors(lambda p: p["route_controls"].__setitem__("may_claim_mathematical_proof", True)))

    def test_historical_variable_packet_mutation_authority_rejected(self):
        self.assertTrue(self.packet_errors(lambda p: p["route_controls"].__setitem__("historical_variable_leaf_packet_mutable", True)))

    def test_full_formula_packet_mutation_authority_rejected(self):
        self.assertTrue(self.packet_errors(lambda p: p["route_controls"].__setitem__("full_formula_packet_mutable", True)))

    def test_registry_cert_count_inflation_rejected(self):
        self.assertTrue(self.registry_errors(lambda r: r["cert_state"].__setitem__("registered_route_count", 1)))

    def test_registry_aggregate_authority_rejected(self):
        self.assertTrue(self.registry_errors(lambda r: r["route_controls"].__setitem__("aggregate_route_prohibited", False)))

    def test_registry_surface_collapse_rejected(self):
        self.assertTrue(self.registry_errors(lambda r: r["route_controls"].__setitem__("circuit_successor_packet_separate", False)))

    def test_historical_pdf_cannot_be_marked_encoded(self):
        self.assertTrue(self.registry_errors(lambda r: r.__setitem__("permanent_unencoded_successors", [])))


if __name__ == "__main__":
    unittest.main()
