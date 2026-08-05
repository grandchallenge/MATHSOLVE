from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validator = load_module("validate_euclid_diophantine_solve", ROOT / "ci" / "validate_euclid_diophantine_solve.py")
producer = load_module("euclid_diophantine", ROOT / "solve" / "euclid_diophantine.py")


class EuclidDiophantineSolveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.candidate = validator.load_json(validator.CERTIFICATE_PATH)
        cls.schema = validator.load_json(validator.SCHEMA_PATH)

    def errors(self, mutation=None):
        data = copy.deepcopy(self.candidate)
        if mutation is not None:
            mutation(data)
        return validator.validate_candidate(data, self.schema)

    def test_baseline_passes(self):
        self.assertEqual(self.errors(), [])

    def test_deterministic_replay_matches_byte_for_byte(self):
        rendered = json.dumps(producer.build_candidate(), indent=2, sort_keys=True) + "\n"
        self.assertEqual(rendered, validator.CERTIFICATE_PATH.read_text(encoding="utf-8"))

    def test_sign_normalization_reuses_protected_witness(self):
        case = producer.solve_case(-252, 105, 84, case_id="SIGN")
        self.assertEqual(case["constructive_solution"]["x"], 8)
        self.assertEqual(case["constructive_solution"]["y"], 20)
        self.assertEqual((-252) * 8 + 105 * 20, 84)

    def test_zero_target_has_constructive_zero_witness(self):
        case = producer.solve_case(252, 105, 0, case_id="ZERO")
        self.assertEqual(case["evidence_type"], "constructive_solution")
        self.assertEqual((case["constructive_solution"]["x"], case["constructive_solution"]["y"]), (0, 0))

    def test_outside_protected_coefficient_family_is_rejected(self):
        with self.assertRaises(ValueError):
            producer.solve_case(6, 9, 3, case_id="OUTSIDE")

    def test_forge_commit_mutation_rejects(self):
        self.assertTrue(self.errors(lambda d: d["forge_input"].__setitem__("commit_sha", "0" * 40)))

    def test_forge_package_mutation_rejects(self):
        self.assertTrue(self.errors(lambda d: d["forge_input"]["package"].__setitem__("digest", "0" * 40)))

    def test_forge_manifest_mutation_rejects(self):
        self.assertTrue(self.errors(lambda d: d["forge_input"]["provider_manifest"].__setitem__("digest", "0" * 40)))

    def test_stage1_certification_output_mutation_rejects(self):
        self.assertTrue(self.errors(lambda d: d["protected_stage1"]["certification_output"].__setitem__("digest", "0" * 40)))

    def test_positive_input_substitution_rejects(self):
        self.assertTrue(self.errors(lambda d: d["cases"][0]["inputs"].__setitem__("c", 85)))

    def test_positive_scale_mutation_rejects(self):
        self.assertTrue(self.errors(lambda d: d["cases"][0]["constructive_solution"].__setitem__("scale_factor", 5)))

    def test_positive_witness_mutation_rejects(self):
        self.assertTrue(self.errors(lambda d: d["cases"][0]["constructive_solution"].__setitem__("x", -7)))

    def test_positive_obstruction_injection_rejects(self):
        self.assertTrue(self.errors(lambda d: d["cases"][0].__setitem__("divisibility_obstruction", {"absolute_target":84,"quotient":4,"remainder":1,"equation_value":85,"strict_nonzero_remainder":True})))

    def test_negative_zero_remainder_rejects(self):
        self.assertTrue(self.errors(lambda d: d["cases"][1]["divisibility_obstruction"].__setitem__("remainder", 0)))

    def test_negative_out_of_range_remainder_rejects(self):
        self.assertTrue(self.errors(lambda d: d["cases"][1]["divisibility_obstruction"].__setitem__("remainder", 21)))

    def test_negative_quotient_mutation_rejects(self):
        self.assertTrue(self.errors(lambda d: d["cases"][1]["divisibility_obstruction"].__setitem__("quotient", 1)))

    def test_timeout_as_unsat_rejects(self):
        self.assertTrue(self.errors(lambda d: d["solver"].__setitem__("timeout_or_failed_search_used_as_unsat", True)))

    def test_recomputed_gcd_rejects(self):
        self.assertTrue(self.errors(lambda d: d["solver"].__setitem__("recomputes_gcd", True)))

    def test_authority_inflation_rejects(self):
        self.assertTrue(self.errors(lambda d: d["claim_boundary"].__setitem__("theorem_certified", True)))

    def test_arbitrary_completeness_claim_rejects(self):
        self.assertTrue(self.errors(lambda d: d["claim_boundary"].__setitem__("arbitrary_diophantine_completeness_claimed", True)))

    def test_historical_verbatim_claim_rejects(self):
        self.assertTrue(self.errors(lambda d: d["claim_boundary"].__setitem__("historical_verbatim_equivalence_claimed", True)))


if __name__ == "__main__":
    unittest.main()
