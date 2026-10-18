#!/usr/bin/env python3
from __future__ import annotations

import sys
import unittest
from pathlib import Path

CI = Path(__file__).resolve().parent
sys.path.insert(0, str(CI))
import validate_openmath_h1_15_compound as v


class H115CompoundSearchTests(unittest.TestCase):
    def test_durable_receipt(self):
        result = v.validate()
        self.assertEqual(result["anchors_completed"], 18)
        self.assertEqual(result["nodes"], 38718)
        self.assertEqual(result["edges"], 631968)
        self.assertEqual(result["combinatorial_best"], 93)
        self.assertFalse(result["found_94_or_better"])


if __name__ == "__main__":
    unittest.main()
