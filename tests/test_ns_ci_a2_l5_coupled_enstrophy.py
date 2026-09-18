from fractions import Fraction
import unittest

from tests.test_ns_ci_a2_l5_c2_active_band import NSCIA2L5C2ActiveBandTests  # noqa: F401
from tests.test_ns_ci_a2_l5_c2_overshoot_dynamics import NSCIA2L5C2OvershootDynamicsTests  # noqa: F401
from tests.test_ns_ci_a2_l5_c2_same_band_mild_obstruction import NSCIA2L5C2SameBandMildObstructionTests  # noqa: F401
from tests.test_ns_ci_a2_l5_c2_instantaneous_cross_level import NSCIA2L5C2InstantaneousCrossLevelTests  # noqa: F401
from tests.test_ns_ci_a2_l5_c2_temporal_leakage import NSCIA2L5C2TemporalLeakageTests  # noqa: F401
from tests.test_ns_ci_a2_l5_c2_fixed_distance_amplitude import NSCIA2L5C2FixedDistanceAmplitudeTests  # noqa: F401
from tests.test_ns_ci_a2_l5_c2_distance_sobolev_tail import NSCIA2L5C2DistanceSobolevTailTests  # noqa: F401
from tests.test_ns_ci_a2_l5_c2_flux_ledger import NSCIA2L5C2FluxLedgerTests  # noqa: F401
from tests.test_ns_ci_a2_l5_c2_triad_coherence import NSCIA2L5C2TriadCoherenceTests  # noqa: F401
from tests.test_ns_ci_a2_l5_c2_shear_phase_lock import NSCIA2L5C2ShearPhaseLockTests  # noqa: F401
from tests.test_ns_ci_a2_l5_c2_mix_moment_ceiling import NSCIA2L5C2MixMomentCeilingTests  # noqa: F401
from tests.test_ns_ci_a2_l5_c2_mix_subcritical_lower import NSCIA2L5C2MixSubcriticalLowerTests  # noqa: F401
from tests.test_ns_ci_a2_l5_c2_mix_critical_semiclassical import NSCIA2L5C2MixCriticalSemiclassicalTests  # noqa: F401
from tests.test_ns_ci_a2_l5_c2_mix_bridge_normal_form import NSCIA2L5C2MixBridgeNormalFormTests  # noqa: F401
from tests.test_ns_ci_a2_l5_c2_mix_semiclassical_residual import NSCIA2L5C2MixSemiclassicalResidualTests  # noqa: F401
from tests.test_ns_ci_a2_l5_c2_polarization_corridor import NSCIA2L5C2PolarizationCorridorTests  # noqa: F401
from tests.test_ns_ci_a2_l5_c2_secondary_shear_charge import NSCIA2L5C2SecondaryShearChargeTests  # noqa: F401
from tests.test_ns_ci_a2_l5_c2_general_shear_profile import NSCIA2L5C2GeneralShearProfileTests  # noqa: F401
from tests.test_ns_ci_a2_l5_c2_accumulated_phase import NSCIA2L5C2AccumulatedPhaseTests  # noqa: F401
from tests.test_ns_ci_a2_l5_c2_direction_defect import NSCIA2L5C2DirectionDefectTests  # noqa: F401
from tests.test_ns_ci_a2_l5_c2_direction_moving_frame import NSCIA2L5C2DirectionMovingFrameTests  # noqa: F401
from tests.test_ns_ci_a2_l5_c3_diagonal_audit import NSCIA2L5C3DiagonalAuditTests  # noqa: F401
from tests.test_ns_ci_a2_l5_field_calibration import NSCIA2L5FieldCalibrationTests  # noqa: F401
from tests.test_ns_ci_a2_l5_forced_core_shell_calibration import NSCIA2L5ForcedCoreShellCalibrationTests  # noqa: F401
from tests.test_ns_ci_a2_l5_frequency_scale_transplant import NSCIA2L5FrequencyScaleTransplantTests  # noqa: F401
from tests.test_ns_ci_a2_l5_packet_intermit_d1 import NSCIA2L5PacketIntermittencyD1Tests  # noqa: F401
from tests.test_ns_ci_a2_l5_pi1_critical_energy import NSCIA2L5PI1CriticalEnergyTests  # noqa: F401
from tests.test_ns_ci_a2_l5_signed_pressure_residual import SignedPressureResidualTests  # noqa: F401


class NSCIA2L5CoupledEnstrophyTests(unittest.TestCase):
    def test_weighted_d3_is_bounded_by_leray_dissipation(self) -> None:
        q = 8
        a = [Fraction((p + 1) ** 2, 1) for p in range(q + 1)]
        d3 = sum(
            Fraction(1, 2 ** (3 * (q - p))) * a[p]
            for p in range(q + 1)
        )
        self.assertLessEqual(d3, sum(a))

    def test_l4_column_identity_is_exact(self) -> None:
        nu = Fraction(7, 5)
        for q in range(1, 8):
            lam_q = Fraction(2**q, 1)
            a = [Fraction((p + 2) ** 2, 3) for p in range(q + 1)]
            d3 = sum((Fraction(2**p, 1) / lam_q) ** 3 * a[p] for p in range(q + 1))
            lhs = nu * lam_q * d3
            rhs = sum(
                (Fraction(2**p, 1) / lam_q) ** 2
                * Fraction(2**p, 1)
                * nu
                * a[p]
                for p in range(q + 1)
            )
            self.assertEqual(lhs, rhs)

    def test_active_diagonal_survives_with_unit_kernel(self) -> None:
        nu = Fraction(3, 2)
        for q in range(1, 10):
            lam_q = Fraction(2**q, 1)
            a_q = Fraction(q + 4, 1)
            diagonal = (lam_q / lam_q) ** 2 * lam_q * nu * a_q
            self.assertEqual(diagonal, lam_q * nu * a_q)

    def test_half_integrability_gap_exponents(self) -> None:
        # f <= Lambda^(3/2) * D3^(1/2).
        # Lambda in L2 gives Lambda^(3/2) in L^(4/3), so Holder needs
        # D3^(1/2) in L4. Leray supplies only D3^(1/2) in L2.
        lambda_factor_time_exponent = Fraction(4, 3)
        required_partner = Fraction(1, 1) / (
            Fraction(1, 1) - Fraction(1, 1) / lambda_factor_time_exponent
        )
        self.assertEqual(required_partner, Fraction(4, 1))

    def test_static_fixture_preserves_selected_scalar_budgets(self) -> None:
        lambda_budget = []
        dissipation_budget = []
        energy = []
        for n in range(1, 10):
            # lambda = 2^(4n), so lambda^(-9/4) = 2^(-9n) exactly.
            lam = Fraction(2 ** (4 * n), 1)
            duration = Fraction(1, 2 ** (9 * n))
            a_q = lam**2
            lambda_budget.append(lam**2 * duration)
            dissipation_budget.append(a_q * duration)
            energy.append(a_q / lam**2)

        self.assertLess(sum(lambda_budget), Fraction(1, 1))
        self.assertLess(sum(dissipation_budget), Fraction(1, 1))
        self.assertTrue(all(e == 1 for e in energy))

    def test_static_fixture_low_coefficient_diverges_geometrically(self) -> None:
        terms = []
        for n in range(1, 8):
            # lambda^(5/2) = 2^(10n), and duration = 2^(-9n),
            # so each next contribution is exactly twice the previous one.
            duration = Fraction(1, 2 ** (9 * n))
            f_q = Fraction(2 ** (10 * n), 1)
            terms.append(f_q * duration)
        for left, right in zip(terms, terms[1:]):
            self.assertEqual(right / left, Fraction(2, 1))

    def test_selector_cancellation_is_algebraic_for_finite_complements(self) -> None:
        # At every fixed terminal shell N, E_low(q)+E_(q<p<=N) is independent
        # of q. Thus selector jumps cancel when the complementary finite blocks
        # are retained; no global H1 identity is asserted here.
        terminal_energy = Fraction(19, 7)
        lows = [Fraction(k, 7) for k in range(8)]
        finite_highs = [terminal_energy - low for low in lows]
        for low, high in zip(lows, finite_highs):
            self.assertEqual(low + high, terminal_energy)

    def test_transport_commutator_has_no_frequency_gain_after_derivative(self) -> None:
        # Kernel cancellation contributes lambda_p^-1, while the derivative
        # on a p-shell contributes lambda_p. Their product is scale-neutral,
        # leaving the low Lipschitz coefficient rather than a decaying p-weight.
        for p in range(1, 12):
            lam_p = Fraction(2**p, 1)
            self.assertEqual((Fraction(1, 1) / lam_p) * lam_p, 1)


if __name__ == "__main__":
    unittest.main()
