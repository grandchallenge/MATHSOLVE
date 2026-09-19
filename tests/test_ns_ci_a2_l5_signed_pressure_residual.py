from collections import defaultdict
from fractions import Fraction as F
import unittest

Z = (F(0), F(0))
ZV = (Z, Z, Z)


def ca(a, b): return (a[0] + b[0], a[1] + b[1])
def cn(a): return (-a[0], -a[1])
def cm(a, b): return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
def cs(q, a): return (q * a[0], q * a[1])
def cis(n, a): return (-F(n) * a[1], F(n) * a[0])
def va(a, b): return tuple(ca(a[j], b[j]) for j in range(3))
def cvs(z, a): return tuple(cm(z, a[j]) for j in range(3))
def vd(a, b):
    out = Z
    for j in range(3): out = ca(out, cm(a[j], b[j]))
    return out

def ka(a, b): return tuple(a[j] + b[j] for j in range(3))
def kn(a): return tuple(-x for x in a)


def add_mode(field, k, amp, kind):
    av = tuple((F(x), F(0)) for x in amp)
    if kind == "cos":
        plus = minus = (F(1, 2), F(0))
    elif kind == "sin":
        plus, minus = (F(0), F(-1, 2)), (F(0), F(1, 2))
    else:
        raise ValueError(kind)
    field[k] = va(field.get(k, ZV), cvs(plus, av))
    nk = kn(k)
    field[nk] = va(field.get(nk, ZV), cvs(minus, av))


def scalar_vec_conv(s, v):
    out = defaultdict(lambda: ZV)
    for k, sv in s.items():
        for ell, vv in v.items(): out[ka(k, ell)] = va(out[ka(k, ell)], cvs(sv, vv))
    return dict(out)


def scalar_conv(a, b):
    out = defaultdict(lambda: Z)
    for k, av in a.items():
        for ell, bv in b.items(): out[ka(k, ell)] = ca(out[ka(k, ell)], cm(av, bv))
    return dict(out)


def vec_dot_field(a, b):
    out = defaultdict(lambda: Z)
    for k, av in a.items():
        for ell, bv in b.items(): out[ka(k, ell)] = ca(out[ka(k, ell)], vd(av, bv))
    return dict(out)


def dy(v):
    return {k: tuple(cis(k[1], z) for z in vv) for k, vv in v.items()}


def leray(v):
    out = {}
    for k, vv in v.items():
        k2 = sum(x * x for x in k)
        kd = Z
        for j in range(3): kd = ca(kd, cs(F(k[j]), vv[j]))
        out[k] = tuple(ca(vv[j], cn(cs(F(k[j], k2), kd))) for j in range(3))
    return out


def mean_inner(a, b):
    out = Z
    for k, av in a.items():
        if kn(k) in b: out = ca(out, vd(av, b[kn(k)]))
    return out


def fixture(sign):
    low_y = {(1, 0, 0): (F(1, 2), F(0)), (-1, 0, 0): (F(1, 2), F(0))}
    v = {}
    add_mode(v, (24, 3, 1), (0, 1, -3), "cos")
    add_mode(v, (25, 2, 1), (0, sign, -2 * sign), "sin")
    add_mode(v, (26, 2, 1), (-1, 0, 26), "cos")
    a = scalar_vec_conv(low_y, dy(v))
    v2 = vec_dot_field(v, v)
    phi = scalar_vec_conv(scalar_conv(v2, v2), v)
    return a, phi


class SignedPressureResidualTests(unittest.TestCase):
    def test_divergence_free_modes_and_gap(self):
        for k, a in [((24, 3, 1), (0, 1, -3)), ((25, 2, 1), (0, 1, -2)), ((26, 2, 1), (-1, 0, 26))]:
            self.assertEqual(sum(k[j] * a[j] for j in range(3)), 0)
        a, _ = fixture(+1)
        self.assertEqual(min(sum(x * x for x in k) for k in a), 539)

    def test_bare_transport_cancels(self):
        a, phi = fixture(+1)
        self.assertEqual(mean_inner(a, phi), Z)

    def test_leray_residual_nonzero_exactly(self):
        a, phi = fixture(+1)
        self.assertEqual(mean_inner(leray(a), phi), (F(-5169371, 154140), F(0)))

    def test_residual_has_no_universal_sign(self):
        ap, pp = fixture(+1)
        am, pm = fixture(-1)
        self.assertEqual(mean_inner(leray(ap), pp), (F(-5169371, 154140), F(0)))
        self.assertEqual(mean_inner(leray(am), pm), (F(5169371, 154140), F(0)))

    def test_nonzero_piece_is_pressure_correction(self):
        a, phi = fixture(+1)
        pa = leray(a)
        pressure = {k: va(a[k], cvs((F(-1), F(0)), pa[k])) for k in a}
        self.assertEqual(mean_inner(a, phi), Z)
        self.assertEqual(mean_inner(pressure, phi), (F(5169371, 154140), F(0)))


if __name__ == "__main__":
    unittest.main()
