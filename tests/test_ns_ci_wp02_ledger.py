import unittest
from fractions import Fraction
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
LEDGER_PATH = ROOT / "work_packages" / "ns_ci_wp02_theorem_ledger.yaml"


class NSCIWP02LedgerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with LEDGER_PATH.open("r", encoding="utf-8") as handle:
            cls.payload = yaml.safe_load(handle)
        cls.entries = {entry["theorem_id"]: entry for entry in cls.payload["entries"]}

    def test_entry_ids_are_complete_and_unique(self) -> None:
        ids = [entry["theorem_id"] for entry in self.payload["entries"]]
        self.assertEqual(ids, [f"CR-{index:03d}" for index in range(12)])
        self.assertEqual(len(ids), len(set(ids)))

    def test_required_source_ids_are_explicit(self) -> None:
        required = set(self.payload["sources"]["required_source_ids"])
        expected = {
            "NS-CI-SRC-CLAY-FEFFERMAN",
            "NS-CI-SRC-LERAY-1934",
            "NS-CI-SRC-OZANSKI-POOLEY",
            "NS-CI-SRC-PRODI-1959",
            "NS-CI-SRC-SERRIN-1962",
            "NS-CI-SRC-LADYZHENSKAYA-1967",
            "NS-CI-SRC-OPERATIONAL-LPS-2024",
        }
        self.assertEqual(required, expected)

    def test_critical_pair_arithmetic(self) -> None:
        self.assertEqual(Fraction(2, 4) + Fraction(3, 6), 1)

    def test_cr005_holder_and_young_exponents(self) -> None:
        self.assertEqual(Fraction(1, 6) + Fraction(1, 3) + Fraction(1, 2), 1)
        self.assertEqual(Fraction(3, 2) * Fraction(4, 3), 2)
        self.assertEqual(Fraction(1, 2) * 4, 2)
        cr005 = self.entries["CR-005"]
        conclusion = cr005["conclusion"]
        self.assertIn("nu^(-3)", conclusion)
        self.assertIn("norm_L6(u)^4", conclusion)
        self.assertIn("Not an unconditional Leray-Hopf estimate", cr005["prohibited_overstatement"])

    def test_cr006_uses_integrated_weak_strong_route(self) -> None:
        cr006 = self.entries["CR-006"]
        self.assertIn("weak energy inequality for v", cr006["hypotheses"])
        self.assertIn("strong energy equality for u", cr006["hypotheses"])
        self.assertIn("integrated inequality", cr006["conclusion"])
        self.assertIn("distributional or justified strong form", cr006["differential_form"])
        prohibited = " ".join(cr006["prohibited_overstatement"]).lower()
        self.assertIn("formal smooth-pair equality", prohibited)
        self.assertIn("unconditional weak-solution identity", prohibited)

    def test_one_way_bridge_and_reverse_debt_are_separate(self) -> None:
        cr009 = self.entries["CR-009"]
        cr010 = self.entries["CR-010"]
        self.assertEqual(cr009["role"], "one_way_bridge")
        self.assertEqual(cr009["status"], "CHECKED_ONE_WAY_BRIDGE")
        self.assertEqual(cr010["role"], "pending_bridge")
        self.assertEqual(cr010["status"], "PENDING")
        self.assertIn("Do not call this bidirectional equivalence", cr009["prohibited_overstatement"])
        self.assertIn("exact source location", " ".join(cr009["unresolved_debt"]).lower())

    def test_compact_support_lane_is_restricted(self) -> None:
        cr011 = self.entries["CR-011"]
        self.assertEqual(cr011["status"], "CHECKED_RESTRICTION")
        self.assertIn("Do not promote to the full whole-space positive branch", cr011["prohibited_overstatement"])


if __name__ == "__main__":
    unittest.main()
