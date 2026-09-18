from fractions import Fraction
import unittest


C = tuple[Fraction, Fraction]


def cadd(a: C, b: C) -> C:
    return (a[0] + b[0], a[1] + b[1])


def cmul(a: C, b: C) -> C:
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cscale(a: C, s: Fraction) -> C:
    return (s * a[0], s * a[1])


def imul(a: C, n: int) -> C:
    # (i n) * (a_re + i a_im)
    return (-n * a[1], n * a[0])


def add_mode(dst: dict[tuple[int, int], C], k: tuple[int, int], value: C) -> None:
    dst[k] = cadd(dst.get(k, (Fraction(0), Fraction(0))), value)
    if dst[k] == (0, 0):
        del dst[k]


def convolution(
    left: dict[tuple[int, int], C],
    right: dict[tuple[int, int], C],
) -> dict[tuple[int, int], C]:
    out: dict[tuple[int, int], C] = {}
    for k, a in left.items():
        for ell, b in right.items():
            q = (k[0] + ell[0], k[1] + ell[1])
            add_mode(out, q, cmul(a, b))
    return out


def central_flux_fixture(sign: int = 1) -> tuple[
    dict[tuple[int, int], C],
    dict[tuple[int, int], C],
    dict[tuple[int, int], C],
    dict[tuple[int, int], C],
]:
    # On T^2_(x,z), use
    # psi = cos(x-z) + sin(2x+2z) + cos(3x+z)
    # and u=(partial_z psi, 0, -partial_x psi).
    half = Fraction(1, 2)
    psi: dict[tuple[int, int], C] = {}

    for k in [(1, -1), (3, 1)]:
        add_mode(psi, k, (half, Fraction(0)))
        add_mode(psi, (-k[0], -k[1]), (half, Fraction(0)))

    add_mode(psi, (2, 2), (Fraction(0), -half))
    add_mode(psi, (-2, -2), (Fraction(0), half))

    u1: dict[tuple[int, int], C] = {}
    u3: dict[tuple[int, int], C] = {}
    for (kx, kz), coeff in psi.items():
        add_mode(u1, (kx, kz), cscale(imul(coeff, kz), Fraction(sign)))
        add_mode(u3, (kx, kz), cscale(imul(coeff, -kx), Fraction(sign)))

    t11 = convolution(u1, u1)
    t33 = convolution(u3, u3)
    t13 = convolution(u1, u3)

    pressure: dict[tuple[int, int], C] = {}
    for q in set(t11) | set(t33) | set(t13):
        if q == (0, 0):
            continue
        qx, qz = q
        norm_sq = qx * qx + qz * qz
        numerator = cadd(
            cscale(t11.get(q, (0, 0)), Fraction(qx * qx)),
            cadd(
                cscale(t13.get(q, (0, 0)), Fraction(2 * qx * qz)),
                cscale(t33.get(q, (0, 0)), Fraction(qz * qz)),
            ),
        )
        pressure[q] = cscale(numerator, Fraction(-1, norm_sq))

    enthalpy: dict[tuple[int, int], C] = {}
    for q in set(t11) | set(t33):
        add_mode(
            enthalpy,
            q,
            cscale(
                cadd(t11.get(q, (0, 0)), t33.get(q, (0, 0))),
                Fraction(1, 2),
            ),
        )
    for q, coeff in pressure.items():
        add_mode(enthalpy, q, coeff)

    flux3 = convolution(enthalpy, u3)
    return u1, u3, pressure, flux3


class NSCIA2L5C3DiagonalAuditTests(unittest.TestCase):
    def test_fixed_shift_cannot_remove_half_derivative(self) -> None:
        # Representative critical source exponents: p=4, m=6.
        # The low-frequency kernel contributes 2^(-(k-j)/m), while
        # the Leray source estimate loses 2^(j/2).
        m = Fraction(6, 1)
        fixed_shift = 8
        exponents = [
            Fraction(j, 2) - Fraction(fixed_shift, 1) / m
            for j in range(20, 28)
        ]
        self.assertTrue(all(right > left for left, right in zip(exponents, exponents[1:])))
        self.assertTrue(all(exponent > 0 for exponent in exponents))

    def test_linear_shift_threshold_is_strictly_supercritical(self) -> None:
        # At k-j=(m/2)j the half-derivative is only flattened, not made
        # summable against arbitrary ell^1 shell dissipation.
        m = Fraction(6, 1)
        for j in range(1, 12):
            shift = (m / 2) * j
            exponent = Fraction(j, 2) - shift / m
            self.assertEqual(exponent, 0)

        # D_j=j^-p is ell^1 for p=4, but D_j^(1/p)=1/j is harmonic.
        p = 4
        contributions = [Fraction(1, j) for j in range(2, 18)]
        for j, term in enumerate(contributions, start=2):
            self.assertEqual(term**p, Fraction(1, j**p))

        # A shift with slope strictly larger than m/2 creates geometric decay.
        for j in range(1, 12):
            shift = 4 * j
            exponent = Fraction(j, 2) - Fraction(shift, 1) / m
            self.assertEqual(exponent, -Fraction(j, 6))

    def test_strict_high_threshold_does_not_supply_source_ell1(self) -> None:
        # Static/scaling fixture only, not an NSE trajectory.
        # Use even shell indices so lambda^(1/2) is exact rational.
        c = Fraction(1, 2)
        c0 = Fraction(1, 1)
        nu = Fraction(1, 1)
        source_terms = []
        dissipation_terms = []
        energy_levels = []
        durations = []

        for n in range(2, 10):
            j = 2 * n
            lam = Fraction(2**j, 1)
            duration = lam ** -2
            amplitude_inf = c * nu * lam

            # The shell is strictly high relative to Q=0.
            self.assertLess(amplitude_inf / lam, c0 * nu)

            # A fixed annular packet scaled as amplitude*phi(lambda x).
            energy_l2_sq = amplitude_inf**2 * lam ** -3
            energy_levels.append(energy_l2_sq)
            durations.append(duration)
            dissipation_terms.append(nu * lam**2 * energy_l2_sq * duration)

            # For p=4,m=6: ||u_j||_6 ~ amplitude*lambda^-1/2.
            spatial_l6 = amplitude_inf * lam ** -Fraction(1, 2)
            source_terms.append(spatial_l6 * duration ** Fraction(1, 4))

        self.assertLess(sum(durations), Fraction(1, 1))
        self.assertLess(sum(dissipation_terms), Fraction(1, 1))
        self.assertTrue(all(e <= energy_levels[0] for e in energy_levels))
        self.assertTrue(all(term == c * nu for term in source_terms))

    def test_unsigned_active_diagonal_is_exact_l4_column_scaling(self) -> None:
        # Bernstein squared: ||u_Q||_inf^2 <= C lambda_Q^3 ||u_Q||_2^2.
        # With D_Q=nu lambda_Q^2 ||u_Q||_2^2 this is
        # C nu^-1 lambda_Q D_Q: exactly the protected L4 active diagonal.
        nu = Fraction(7, 5)
        for q in range(1, 10):
            lam = Fraction(2**q, 1)
            l2_sq = Fraction(q + 3, 11)
            d_q = nu * lam**2 * l2_sq
            bernstein_sq = lam**3 * l2_sq
            l4_diagonal = (Fraction(1, 1) / nu) * lam * d_q
            self.assertEqual(bernstein_sq, l4_diagonal)

    def test_central_flux_fixture_is_divergence_free_and_finite_band(self) -> None:
        u1, u3, _, _ = central_flux_fixture()
        for q in set(u1) | set(u3):
            qx, qz = q
            div = cadd(imul(u1.get(q, (0, 0)), qx), imul(u3.get(q, (0, 0)), qz))
            self.assertEqual(div, (0, 0))

        norm_sq = [kx * kx + kz * kz for kx, kz in u1]
        self.assertLess(max(norm_sq), 16 * min(norm_sq))

    def test_localized_total_energy_flux_has_no_universal_sign(self) -> None:
        # p solves -Delta p = partial_i partial_j(u_i u_j), with zero mean.
        # For the positive test phi(z)=1+(1/4)sin(4z), phi'(z)=cos(4z).
        _, _, pressure_pos, flux_pos = central_flux_fixture(sign=1)
        _, _, pressure_neg, flux_neg = central_flux_fixture(sign=-1)

        self.assertEqual(pressure_pos, pressure_neg)
        self.assertEqual(flux_pos[(0, 4)], (Fraction(-3, 20), 0))
        self.assertEqual(flux_pos[(0, -4)], (Fraction(-3, 20), 0))

        # Torus mean of F_3 cos(4z) is half the +4 coefficient plus
        # half the -4 coefficient.
        pairing_pos = cscale(
            cadd(flux_pos[(0, 4)], flux_pos[(0, -4)]),
            Fraction(1, 2),
        )
        pairing_neg = cscale(
            cadd(flux_neg[(0, 4)], flux_neg[(0, -4)]),
            Fraction(1, 2),
        )
        self.assertEqual(pairing_pos, (Fraction(-3, 20), 0))
        self.assertEqual(pairing_neg, (Fraction(3, 20), 0))

        # The test itself is strictly positive.
        self.assertGreater(Fraction(1, 1) - Fraction(1, 4), 0)


if __name__ == "__main__":
    unittest.main()
