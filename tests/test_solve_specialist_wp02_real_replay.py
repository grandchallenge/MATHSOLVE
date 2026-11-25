"""Real protected-evaluator replay and hostile mismatch tests for #1040."""
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "solve_specialist_wp02_real_replay",
    ROOT / "ci/solve_specialist_wp02_real_replay.py",
)
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class RealWP02ReplayTests(unittest.TestCase):
    def test_real_pinned_replay_preserves_narrow_claim_boundary(self):
        result = module.verify()
        self.assertTrue(result["replay_pass"])
        self.assertEqual(result["witnesses"], module.EXPECTED)
        self.assertFalse(result["exact_search_design_admitted"])
        self.assertFalse(result["specialist_positive_receipt"])
        self.assertFalse(result["mathematical_certification"])

    def test_hostile_expected_span_rejected(self):
        altered = {k: dict(v) for k, v in module.EXPECTED.items()}
        altered["W8021"]["tape_span"] = 121
        with self.assertRaisesRegex(module.ReplayFailure, "W8021: protected evaluator mismatch"):
            module.verify(expected=altered)


if __name__ == "__main__":
    unittest.main()
