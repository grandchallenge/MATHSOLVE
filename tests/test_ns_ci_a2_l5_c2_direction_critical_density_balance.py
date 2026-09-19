import unittest


class NSCIA2L5C2CriticalDensityBalanceTests(unittest.TestCase):
    def test_density_balance_algebra(self):
        alpha = -3.0
        q2 = 2.0
        phase = 5.0
        q4 = 1.5
        lhs = -alpha * q2 + phase - 2.0 * q4
        rhs = max(-alpha, 0.0) * q2 - max(alpha, 0.0) * q2 + phase - 2.0 * q4
        self.assertAlmostEqual(lhs, rhs)

    def test_compression_enters_with_positive_sign(self):
        alpha = -4.0
        q2 = 0.75
        self.assertAlmostEqual(max(-alpha, 0.0) * q2, 3.0)

    def test_expansion_enters_with_negative_sign(self):
        alpha = 4.0
        q2 = 0.75
        self.assertAlmostEqual(-max(alpha, 0.0) * q2, -3.0)

    def test_q4_is_nonnegative_damping(self):
        q4 = 2.5
        self.assertLessEqual(-2.0 * q4, 0.0)

    def test_integrated_ledger_rearrangement(self):
        q2_final = 1.2
        expansion = 0.4
        phase_total = -0.3
        d4 = 0.5
        compression = q2_final + expansion - phase_total + 2.0 * d4
        self.assertAlmostEqual(compression, 2.9)

    def test_scope_is_not_charge(self):
        result = 'critical_density_balance'
        self.assertNotEqual(result, 'selector_charge_proved')
        self.assertNotEqual(result, 'A2_proved')


if __name__ == '__main__':
    unittest.main()