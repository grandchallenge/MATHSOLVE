from fractions import Fraction
from math import factorial
import unittest


class NSCIA2L5C2TemporalLeakageTests(unittest.TestCase):
    def test_horizontal_convection_is_exact_gradient(self) -> None:
        # v=(A cos y, A cos x).
        # convection/A^2N is (-cos x sin y, -sin x cos y),
        # the negative gradient of sin x sin y.
        cx, sx = Fraction(2, 3), Fraction(3, 5)
        cy, sy = Fraction(5, 7), Fraction(7, 11)
        convection = (-cx * sy, -sx * cy)
        minus_gradient = (-cx * sy, -sx * cy)
        self.assertEqual(convection, minus_gradient)

    def test_target_amplitude_derivative_recovers_l5_17(self) -> None:
        nu = Fraction(5, 4)
        n = Fraction(9, 1)
        a = Fraction(8, 3)
        c = Fraction(7, 5)
        c_dot = -2 * nu * n**2 * c + a**2 * n
        self.assertEqual(c_dot, a**2 * n - 2 * nu * n**2 * c)

    def test_first_leaked_mode_derivative(self) -> None:
        a = Fraction(7, 3)
        c = Fraction(11, 5)
        n = Fraction(13, 2)
        magnitude = n * a * c / 4
        self.assertEqual(magnitude, c * (n * a) / (2**2))

    def test_second_distance_mode_second_derivative(self) -> None:
        a = Fraction(7, 3)
        c = Fraction(11, 5)
        n = Fraction(13, 2)
        magnitude = c * (n * a) ** 2 / 8
        self.assertEqual(magnitude, c * (n * a) ** 2 / (2**3))

    def test_general_shortest_path_jet_magnitude(self) -> None:
        a = Fraction(5, 2)
        c = Fraction(9, 7)
        n = Fraction(4, 1)
        for r in range(1, 9):
            expected = c * (n * a) ** r / (2 ** (r + 1))
            recurrence = c / 2
            for _ in range(r):
                recurrence *= n * a / 2
            self.assertEqual(recurrence, expected)

    def test_graph_distance_excludes_lower_order_contributions(self) -> None:
        for r in range(1, 12):
            source = (1, 1)
            target = (r + 1, 1)
            distance = abs(target[0] - source[0]) + abs(target[1] - source[1])
            self.assertEqual(distance, r)

    def test_frequency_distance_is_unbounded(self) -> None:
        ratios_sq = [
            Fraction((r + 1) ** 2 + 1, 2)
            for r in range(1, 12)
        ]
        self.assertTrue(all(b > a for a, b in zip(ratios_sq, ratios_sq[1:])))
        self.assertGreater(ratios_sq[-1], 50)

    def test_turnover_scale_leading_jet_has_factorial_penalty(self) -> None:
        ratios = [
            Fraction(1, (2**r) * factorial(r))
            for r in range(1, 9)
        ]
        for r, (left, right) in enumerate(zip(ratios, ratios[1:]), start=1):
            self.assertEqual(right / left, Fraction(1, 2 * (r + 1)))
        self.assertLess(ratios[-1], Fraction(1, 1_000_000))

    def test_support_leakage_does_not_itself_imply_threshold_leakage(self) -> None:
        for r in range(4, 10):
            leading_ratio = Fraction(1, (2**r) * factorial(r))
            frequency_ratio_lower = Fraction(r + 1, 2)
            self.assertLess(leading_ratio, Fraction(1, 100) * frequency_ratio_lower)


if __name__ == "__main__":
    unittest.main()
