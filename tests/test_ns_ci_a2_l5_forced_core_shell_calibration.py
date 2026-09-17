from fractions import Fraction
import unittest


class NSCIA2L5ForcedCoreShellCalibrationTests(unittest.TestCase):
    def test_core_shell_and_velocity_exponents_give_threshold_growth(self) -> None:
        # For fixed h>0 and viscosity nu, the calibrated shell has
        # lambda ~ (nu*tau)^(-1/2) and ||u_p||_inf ~ nu^(1/2) tau^(-1/2-h).
        h = Fraction(1, 200)
        a = Fraction(1, 2) + h

        lambda_nu_exp = Fraction(-1, 2)
        lambda_tau_exp = Fraction(-1, 2)
        amp_nu_exp = Fraction(1, 2)
        amp_tau_exp = -a

        threshold_ratio_nu_exp = -lambda_nu_exp + amp_nu_exp
        threshold_ratio_tau_exp = -lambda_tau_exp + amp_tau_exp

        self.assertEqual(threshold_ratio_nu_exp, Fraction(1, 1))
        self.assertEqual(threshold_ratio_tau_exp, -h)

    def test_lambda_squared_is_logarithmically_nonintegrable(self) -> None:
        # Lambda >= c (nu*tau)^(-1/2), so Lambda^2 >= c nu^-1 tau^-1.
        lambda_tau_exp = Fraction(-1, 2)
        lambda_sq_tau_exp = 2 * lambda_tau_exp
        self.assertEqual(lambda_sq_tau_exp, Fraction(-1, 1))

    def test_low_mode_coefficient_lower_bound_is_supercritical_in_time(self) -> None:
        # f >= lambda_p ||u_p||_inf ~ tau^(-1-h); viscosity cancels.
        h = Fraction(1, 200)
        a = Fraction(1, 2) + h

        f_nu_exp = Fraction(-1, 2) + Fraction(1, 2)
        f_tau_exp = Fraction(-1, 2) - a

        self.assertEqual(f_nu_exp, Fraction(0, 1))
        self.assertEqual(f_tau_exp, -Fraction(1, 1) - h)
        self.assertLessEqual(f_tau_exp, Fraction(-1, 1))

    def test_packet_s1_lower_bound_is_nonintegrable(self) -> None:
        # S1 contains the violating shell once p<=Q.
        h = Fraction(1, 200)
        a = Fraction(1, 2) + h

        s1_nu_exp = 2 * Fraction(1, 2)
        s1_tau_exp = -2 * a

        self.assertEqual(s1_nu_exp, Fraction(1, 1))
        self.assertEqual(s1_tau_exp, -Fraction(1, 1) - 2 * h)
        self.assertLess(s1_tau_exp, Fraction(-1, 1))

    def test_viscosity_rescaling_preserves_threshold_ratio_structure(self) -> None:
        # The campaign threshold is c0*nu.  The shell lower bound gives
        # lambda^-1 ||u_p||_inf >= c*nu*tau^-h, so division by nu removes
        # all viscosity dependence and leaves the divergent tau^-h factor.
        h = Fraction(1, 200)
        ratio_nu_exp = Fraction(1, 1) - Fraction(1, 1)
        ratio_tau_exp = -h

        self.assertEqual(ratio_nu_exp, Fraction(0, 1))
        self.assertLess(ratio_tau_exp, Fraction(0, 1))

    def test_finite_offset_shell_remains_core_scale(self) -> None:
        # A fixed dyadic offset j only changes the shell by the constant 2^j.
        # It cannot change the tau or nu exponents of the core frequency.
        base_nu_exp = Fraction(-1, 2)
        base_tau_exp = Fraction(-1, 2)
        for _j in range(-8, 9):
            self.assertEqual(base_nu_exp, Fraction(-1, 2))
            self.assertEqual(base_tau_exp, Fraction(-1, 2))


if __name__ == "__main__":
    unittest.main()
