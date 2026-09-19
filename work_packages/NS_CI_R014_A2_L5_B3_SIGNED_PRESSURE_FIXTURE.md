# NS-CI-R014-A2-L5-7 — Signed projection/pressure residual falsification

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Predecessor: `NS_CI_R014_A2_L5_B3_L6_TRANSPORT_AUDIT.md`
- Result: `SIGNED_PROJECTION_PRESSURE_IDENTITY_FALSIFIED__NONZERO_SIGN_INDEFINITE`
- A2 theorem: open
- L5: active

The predecessor left one narrow B3 possibility open: perhaps the signed
high-pass/Leray projection residual produced by direct `L6` testing vanishes
identically, or has a universal favorable sign, before absolute values are
taken.

This tranche falsifies that operator-algebraic possibility exactly.

The falsification is deliberately narrower than a Navier--Stokes theorem. It
uses smooth divergence-free Fourier fields to test only identities that could
follow from incompressibility, spectral separation, self-adjoint high/low
Fourier projection, and Leray projection algebra. The fixture is not asserted
to be a Navier--Stokes solution and does not exclude a new estimate that uses
additional equation-specific dynamics.

## 1. Residual under test

For fixed `q`, write

```math
V=P_{>q}u,\qquad L=P_{\le q-2}u,\qquad
\Phi(V)=|V|^4V.
```

The low--high contribution is

```math
I_q
=
\langle P_{>q}\mathbb P(L\cdot\nabla V),\Phi(V)\rangle .
```

Bare transport cancels:

```math
\langle L\cdot\nabla V,\Phi(V)\rangle
=
\frac16\int L\cdot\nabla |V|^6\,dx
=
0.
```

The open question was whether the remaining signed projection/pressure part
could vanish identically, or have one sign, from the projector algebra itself.

## 2. Exact Fourier fixture

Work on the algebraic test domain

```math
\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3.
```

Set

```math
L(x)=(0,\cos x_1,0)
```

and

```math
V(x)
=
a_1\cos(m_1\cdot x)
+
a_2\sin(m_2\cdot x)
+
a_3\cos(m_3\cdot x),
```

with

```text
m1=(24,3,1),   a1=(0,1,-3),
m2=(25,2,1),   a2=(0,1,-2),
m3=(26,2,1),   a3=(-1,0,26).
```

Each mode is exactly divergence free:

```math
m_j\cdot a_j=0.
```

Let

```math
A=L\cdot\nabla V=\cos x_1\,\partial_2V.
```

Every Fourier mode of `A` is one of `\pm m_j\pm(1,0,0)`. Hence

```math
\min_{\xi\in\operatorname{supp}\widehat A}|\xi|^2=539,
```

so the transport support lies above `sqrt(539)>23` while `L` lives at frequency
one. Any standard compactly supported high-pass whose multiplier is already
one on this transport support acts as the identity on `A`. Thus this fixture
can isolate the Leray pressure correction without contamination from a
high-pass transition region.

Exact rational Fourier convolution gives

```math
\langle A,|V|^4V\rangle_{\mathbb T^3}=0
```

but

```math
\boxed{
\langle \mathbb P A,|V|^4V\rangle_{\mathbb T^3,\mathrm{mean}}
=
-\frac{5169371}{154140}
\neq0 .
}
```

Because the bare term is zero, the nonzero contribution is exactly the Leray
gradient/pressure correction:

```math
\langle (I-\mathbb P)A,|V|^4V\rangle_{\mathrm{mean}}
=
+\frac{5169371}{154140}.
```

No floating-point approximation is used in the committed fixture.

## 3. Sign reversal

Replace only the sine mode by its negative:

```math
a_2\sin(m_2\cdot x)\longmapsto -a_2\sin(m_2\cdot x).
```

All divergence-free and support conditions remain unchanged, while the exact
projected value becomes

```math
\langle \mathbb P A,|V|^4V\rangle_{\mathrm{mean}}
=
+\frac{5169371}{154140}.
```

Therefore the residual is not only nonzero; its sign is not fixed by the
algebraic constraints under test.

## 4. What this fixture proves

The following bounded candidate is falsified:

```text
INCOMPRESSIBILITY + LOW/HIGH SPECTRAL SEPARATION
+ HIGH-PASS / LERAY SELF-ADJOINTNESS
=> EXACT SIGNED PROJECTION/PRESSURE CANCELLATION
```

and so is the weaker universal-sign candidate.

Accordingly,

```text
SIGNED_PROJECTION_PRESSURE_IDENTITY_FALSIFIED__NONZERO_SIGN_INDEFINITE.
```

This is stronger than the predecessor's standard absolute commutator
termination in one precise sense: taking absolute values was not the only
reason the route failed. Even before absolute values, the Leray pressure
correction can survive with either sign.

## 5. Scope boundary

This fixture does **not** prove any of the following:

- that every signed estimate for `I_q` is impossible;
- that Navier--Stokes dynamics cannot force time-averaged cancellation;
- that a whole-space decay argument cannot add information absent from the
  pure Fourier algebra;
- that packet/intermittency depletion is false;
- that A2 is false or proved.

The periodic fixture is used only as an algebraic identity falsifier. Any
future route that survives it must invoke additional PDE/dynamic information,
not only incompressibility and projector identities.

## 6. Successor

The exact signed identity route is now closed. The remaining distinct B3
frontier is an equation-specific quantitative depletion mechanism, for example:

```math
\int_0^T
\left(
\sum_{p>Q(t)}\lambda_p^2 A_p(t)
\right)^{2/3}dt<\infty,
```

or a genuinely dynamic signed estimate for the pressure residual that is
strictly stronger than the algebraic identities falsified here.

A next attempt should therefore test packet/intermittency depletion or a
time-correlated pressure-flux estimate. It must not return to:

- exact projector cancellation;
- a universal sign of the pressure residual;
- the standard absolute commutator estimate;
- moving-tail `H1` energy;
- fixed-`q` bad-set splitting;
- threshold-residence Duhamel;
- the closed L4 weighted column.

## Claim boundary

A2 remains unproved. No regularity theorem, `f in L1_t`, dynamic pressure
depletion, packet theorem, MATHCERT certification, novelty, priority, or theorem
promotion is asserted.
