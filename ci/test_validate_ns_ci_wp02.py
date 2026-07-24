import copy
import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "ci" / "validate_ns_ci_wp02.py"
SPEC = importlib.util.spec_from_file_location("validate_ns_ci_wp02", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class NSCIWP02ValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.payload = MODULE.load_ledger()

    def test_current_ledger_validates(self) -> None:
        MODULE.validate(self.payload)

    def test_holder_exponents_close(self) -> None:
        self.assertEqual(Fraction(1, 6) + Fraction(1, 3) + Fraction(1, 2), 1)

    def test_young_exponents_and_viscosity_power(self) -> None:
        # p=4/3 and p'=4 are conjugate.
        self.assertEqual(Fraction(3, 4) + Fraction(1, 4), 1)
        # (nu^(3/4) * Delta^(3/2))^(4/3) = nu * Delta^2.
        self.assertEqual(Fraction(3, 4) * Fraction(4, 3), 1)
        self.assertEqual(Fraction(3, 2) * Fraction(4, 3), 2)
        # (nu^(-3/4) * U * G^(1/2))^4 = nu^(-3) U^4 G^2.
        self.assertEqual(Fraction(-3, 4) * 4, -3)
        self.assertEqual(Fraction(1, 2) * 4, 2)

    def test_critical_pair_is_time_four_space_six(self) -> None:
        self.assertEqual(Fraction(2, 4) + Fraction(3, 6), 1)
        self.assertNotEqual(Fraction(2, 6) + Fraction(3, 4), 1)

    def test_missing_reverse_bridge_is_rejected(self) -> None:
        payload = copy.deepcopy(self.payload)
        entry = next(item for item in payload["entries"] if item["theorem_id"] == "CR-010")
        entry["status"] = "CHECKED"
        with self.assertRaises(MODULE.ValidationError):
            MODULE.validate(payload)

    def test_equivalence_overclaim_is_rejected(self) -> None:
        payload = copy.deepcopy(self.payload)
        entry = next(item for item in payload["entries"] if item["theorem_id"] == "CR-009")
        entry["prohibited_overstatement"] = []
        with self.assertRaises(MODULE.ValidationError):
            MODULE.validate(payload)

    def test_unknown_source_id_is_rejected(self) -> None:
        payload = copy.deepcopy(self.payload)
        entry = next(item for item in payload["entries"] if item["theorem_id"] == "CR-004")
        entry["source_ids"].append("NS-CI-SRC-INVENTED")
        with self.assertRaises(MODULE.ValidationError):
            MODULE.validate(payload)

    def test_unconditional_weak_h1_overclaim_is_rejected(self) -> None:
        payload = copy.deepcopy(self.payload)
        entry = next(item for item in payload["entries"] if item["theorem_id"] == "CR-005")
        entry["prohibited_overstatement"] = []
        with self.assertRaises(MODULE.ValidationError):
            MODULE.validate(payload)


if __name__ == "__main__":
    unittest.main()
