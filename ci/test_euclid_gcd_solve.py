from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "ci" / "validate_euclid_gcd_solve.py"
SPEC = importlib.util.spec_from_file_location("validate_euclid_gcd_solve", VALIDATOR_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

CANDIDATE = json.loads((ROOT / "certificates" / "EUCLID-GCD-E2E-001.json").read_text(encoding="utf-8"))
SCHEMA = json.loads((ROOT / "schemas" / "euclid_gcd_candidate.schema.json").read_text(encoding="utf-8"))


class EuclidGcdSolveTests(unittest.TestCase):
    def assert_rejected(self, mutation) -> None:
        value = copy.deepcopy(CANDIDATE)
        mutation(value)
        self.assertTrue(MODULE.validate_candidate(value, SCHEMA))

    def test_canonical_candidate_is_valid(self) -> None:
        self.assertEqual(MODULE.validate_candidate(CANDIDATE, SCHEMA), [])

    def test_changed_quotient_rejected(self) -> None:
        self.assert_rejected(lambda x: x["euclidean_trace"][0].__setitem__("quotient", 3))

    def test_changed_remainder_rejected(self) -> None:
        self.assert_rejected(lambda x: x["euclidean_trace"][0].__setitem__("remainder", 41))

    def test_non_decreasing_remainder_rejected(self) -> None:
        self.assert_rejected(lambda x: x["euclidean_trace"][0].__setitem__("remainder", 105))

    def test_truncated_trace_rejected(self) -> None:
        self.assert_rejected(lambda x: x.__setitem__("euclidean_trace", x["euclidean_trace"][:-1]))

    def test_wrong_terminal_divisor_rejected(self) -> None:
        self.assert_rejected(lambda x: x["result"].__setitem__("d", 7))

    def test_changed_bezout_coefficient_rejected(self) -> None:
        self.assert_rejected(lambda x: x["bezout_witness"].__setitem__("x", -1))

    def test_input_substitution_rejected(self) -> None:
        self.assert_rejected(lambda x: x["inputs"].__setitem__("a", 253))

    def test_zero_zero_rejected(self) -> None:
        def mutate(x):
            x["inputs"] = {"a": 0, "b": 0}
            x["euclidean_trace"] = []
        self.assert_rejected(mutate)

    def test_forge_commit_drift_rejected(self) -> None:
        self.assert_rejected(lambda x: x["forge_input"].__setitem__("commit_sha", "0" * 40))

    def test_forge_blob_drift_rejected(self) -> None:
        self.assert_rejected(lambda x: x["forge_input"]["package"].__setitem__("digest", "0" * 40))

    def test_authority_inflation_rejected(self) -> None:
        self.assert_rejected(lambda x: x.__setitem__("authority_state", "certified"))

    def test_historical_claim_inflation_rejected(self) -> None:
        self.assert_rejected(lambda x: x["claim_boundary"].__setitem__("historical_verbatim_equivalence_claimed", True))


if __name__ == "__main__":
    unittest.main()
