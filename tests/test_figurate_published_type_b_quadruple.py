"""Reproduce a published triangular-output quadruple from the 2023 primary paper.

This is regression evidence of a known example, not a new mathematical result.
"""
import unittest

from research.figurate_census import verify_tuple


class TypeBPublishedWitnessTests(unittest.TestCase):
    def test_filipin_szalay_2023_quadruple(self):
        values = (14, 31, 135, 3510)
        witness = verify_tuple(values, "B", 3, 1)
        self.assertIsNotNone(witness)
        self.assertEqual(witness, {
            "14,31": 29,
            "14,135": 61,
            "14,3510": 313,
            "31,135": 91,
            "31,3510": 466,
            "135,3510": 973,
        })

    def test_no_type_a_transfer(self):
        values = (14, 31, 135, 3510)
        self.assertIsNone(verify_tuple(values, "A", 3, 1))


if __name__ == "__main__":
    unittest.main()
