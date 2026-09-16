# NS-CI-R014-A2-L5-8 — Dimensionally normalized packet/intermittency D=1 bridge

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected source head at tranche start: `64527fcfb07467070c0c3ffd4278e2ddfb663a69`
- Predecessor: `NS_CI_R014_A2_L5_B3_SIGNED_PRESSURE_FIXTURE.md`
- Result: `PACKET_D1_DIMENSIONALLY_NORMALIZED_CONDITIONAL_BRIDGE_PROVED__D1_NOT_IMPLIED_BY_STATIC_A2_BUDGETS`
- A2 theorem: open
- L5: active
- MATHCERT adjudication: absent

The predecessor eliminates exact or sign-definite cancellation coming only from
high-pass/Leray algebra. The remaining B3 frontier must use genuinely dynamic
information. This tranche isolates a dimensionally and scale-covariant packet
condition which would be sufficient, proves the conditional bridge, and shows
that the present A2 scalar budgets do not imply that condition by themselves.

The packet condition is not imported as an assumption of A2. It is the exact
additional theorem that a successful packet route would have to supply.

## 1. A2 interface and intrinsic energy wavenumber

Use the existing whole-space dyadic normalization and write

```math
\Lambda(t)=\lambda_{Q(t)},
\qquad
f(t)=\sup_{q\le Q(t)}\lambda_q\|u_q(t)\|_\infty,
\qquad
U_0=\|u_0\|_2.
```

If `U_0=0`, the Leray solution is trivial. Hence the nontrivial case may assume
`U_0>0`.

The selected A2 hypothesis and Leray inequality give

```math
\int_0^T \Lambda(t)^2\,dt<\infty,
```

and, up to the fixed Littlewood--Paley equivalence constant,

```math
2\nu\int_0^T\sum_q\lambda_q^2\|u_q(t)\|_2^2\,dt
\lesssim U_0^2.
```

Define the intrinsic energy wavenumber

```math
\boxed{\lambda_E:=\left(\frac{\nu}{U_0}\right)^2.}
```

It has physical dimension `length^{-1}`. Under Navier--Stokes scaling

```math
u_\rho(x,t)=\rho u(\rho x,\rho^2t),
```

viscosity is unchanged, while

```math
\Lambda\mapsto\rho\Lambda,
\qquad
f\mapsto\rho^2f,
\qquad
U_0\mapsto\rho^{-1/2}U_0,
\qquad
\lambda_E\mapsto\rho\lambda_E.
```

The time-integrated dissipation density

```math
\mathcal D
:=
\int_0^T\sum_q\lambda_q^2\|u_q\|_2^2dt
```

scales as `rho^{-1}`.

The established low-mode regularity route closes once `f in L1_t`; A2 may not
assume that conclusion.

## 2. Dimensionally normalized active-range packet condition

For `D in [0,3]`, let

```math
S_D(t):=
\sum_{q\le Q(t)}
\lambda_q^{D-1}\|u_q(t)\|_\infty^2.
```

Define `PI_D^*` by

```math
\boxed{
\int_0^T S_D(t)\,dt
\le
C_D\lambda_E^D\mathcal D
=
C_D\nu^{2D}U_0^{-2D}\mathcal D.
}
```

This normalization passes both required audits.

### Navier--Stokes scaling

The left side scales as `rho^{D-1}`. The right side does also, because
`lambda_E^D` scales as `rho^D` and `mathcal D` scales as `rho^{-1}`.

### Physical dimensions

With `[u]=L/T`, `[nu]=L^2/T`, and `[U_0]=L^(5/2)/T`, one has
`[lambda_E]=L^{-1}`. Therefore

```math
[\lambda_E^D\mathcal D]
=
L^{-D}\frac{L^3}{T}
=
\frac{L^{3-D}}{T}
=
\left[\int S_Ddt\right].
```

The earlier raw-dissipation normalization and the intermediate
`U_0^{-2D}`-only normalization are both rejected: the former fails scaling,
and the latter is scale-covariant but fails physical dimensional consistency.

At `D=1`,

```math
\boxed{
\int_0^T
\sum_{q\le Q(t)}\|u_q(t)\|_\infty^2\,dt
\le
C_1\left(\frac{\nu}{U_0}\right)^2\mathcal D.
}
```

By the Leray inequality,

```math
\boxed{
\int_0^T
\sum_{q\le Q(t)}\|u_q(t)\|_\infty^2\,dt
\lesssim
\frac{C_1\nu}{2}.
}
```

The weighting is the `r=infinity` analogue of the active-range
Bernstein-saturation pattern used by Cheskidov and Peng, *An optimal upper
bound on the determining wavenumber for 3D Navier-Stokes Equations*, NoDEA 33
(2026), Art. 92, DOI `10.1007/s00030-026-01232-0`. Their fixed-domain setting
uses the domain wavenumber to supply the missing inverse-length scale. Their
domain, determining wavenumber, and theorem are not substituted for the
present whole-space A2 problem. The intrinsic `lambda_E` above is introduced
here solely to state a whole-space dimensionally consistent conditional bridge.

## 3. Conditional bridge for all D >= 1

For every `q<=Q`, `lambda_q<=Lambda`. Therefore

```math
\lambda_q^2\|u_q\|_\infty^2
=
\lambda_q^{3-D}
\left(\lambda_q^{D-1}\|u_q\|_\infty^2\right)
\le
\Lambda^{3-D}
\left(\lambda_q^{D-1}\|u_q\|_\infty^2\right).
```

Taking the supremum and bounding it by the sum gives

```math
\boxed{f(t)^2\le\Lambda(t)^{3-D}S_D(t).}
```

Hence

```math
\int_0^T f(t)dt
\le
\left(\int_0^T\Lambda^{3-D}dt\right)^{1/2}
\left(\int_0^T S_Ddt\right)^{1/2}.
```

If `D>=1`, then `3-D<=2`. On a finite interval, `Lambda in L2_t` gives
`Lambda^(3-D) in L1_t`. Under `PI_D^*`,

```math
\int_0^T f(t)dt
\le
C_D^{1/2}\lambda_E^{D/2}\mathcal D^{1/2}
\left(\int_0^T\Lambda^{3-D}dt\right)^{1/2}<\infty.
```

Using Leray gives the equivalent bounded form

```math
\int_0^T f(t)dt
\lesssim
C_D^{1/2}(2\nu)^{-1/2}
\nu^D U_0^{1-D}
\left(\int_0^T\Lambda^{3-D}dt\right)^{1/2}.
```

Thus

```math
\boxed{D\ge1\ \text{and}\ PI_D^*\quad\Longrightarrow\quad f\in L^1(0,T).}
```

The already established low-mode criterion then yields regularity. This is a
conditional theorem only; `PI_D^*` is not part of A2.

## 4. Borderline D=1 factorization

At `D=1`,

```math
f(t)^2
\le
\Lambda(t)^2
\sum_{q\le Q(t)}\|u_q(t)\|_\infty^2.
```

Therefore

```math
\int_0^T f(t)dt
\le
\|\Lambda\|_{L^2_t}
\left(
\int_0^T\sum_{q\le Q(t)}\|u_q(t)\|_\infty^2dt
\right)^{1/2}.
```

Under `PI_1^*` and Leray,

```math
\boxed{
\int_0^T f(t)dt
\lesssim
\left(\frac{C_1\nu}{2}\right)^{1/2}
\|\Lambda\|_{L^2_t}.
}
```

This is dimensionless, as `integral f dt` must be, and finite from exactly the
selected A2 budget plus the new packet theorem. No product of unrelated `L1_t`
functions appears; the estimate is a single Cauchy--Schwarz pairing.

The exponent `D=1` is the endpoint for this mechanism. If `D<1`, then
`3-D>2`, and `Lambda in L2_t` alone does not give
`Lambda^(3-D) in L1_t`.

## 5. Static A2 budgets do not imply PI_1^*

The following threshold-compatible scalar fixture separates the current A2
budgets from the missing packet theorem. It is not asserted to be a
Navier--Stokes trajectory.

Normalize `nu=1` and `U_0=1`, so `lambda_E=1`. On disjoint time intervals
`I_n`, choose

```math
\Lambda_n=\lambda_{Q_n}=2^{4n},
\qquad
|I_n|=2^{-9n},
\qquad
E_{Q_n}=1,
\qquad
A_{Q_n}=\Lambda_n^2,
```

and let all shells above `Q_n` vanish. Choose the active shell to saturate the
standard three-dimensional Bernstein scale,

```math
\|u_{Q_n}\|_\infty^2\asymp\Lambda_n^3E_{Q_n}=\Lambda_n^3.
```

For large `n`, this active shell violates the strict-high threshold at `Q_n`
while every shell above it satisfies that threshold trivially, so the selector
logic is respected.

The selected scalar budgets converge:

```math
\sum_n |I_n|\Lambda_n^2
=
\sum_n2^{-n}<\infty,
```

and

```math
\sum_n |I_n|A_{Q_n}
=
\sum_n2^{-n}<\infty.
```

The pointwise energy is uniformly bounded because `E_{Q_n}=1`. Since
`nu=U_0=lambda_E=1`, the normalized `PI_1^*` right side remains finite. But its
left side diverges:

```math
\sum_n |I_n|\|u_{Q_n}\|_\infty^2
\asymp
\sum_n2^{3n}=\infty.
```

Thus `Lambda in L2_t`, Leray dissipation, the energy cap, and the threshold
logic do not imply `PI_1^*` by static functional analysis.

## 6. Literature consistency

Cheskidov and Shvydkoy, *A unified approach to regularity problems for the 3D
Navier-Stokes and Euler equations: the use of Kolmogorov's dissipation range*,
J. Math. Fluid Mech. 16 (2014), prove the low-mode criterion `f in L1_t` and
show that the stronger `Lambda in L^(5/2)_t` condition is sufficient. They also
obtain regularity under a time-averaged intermittency condition.

Cheskidov and Peng (2026) define intermittency dimension through averaged
Bernstein saturation over an active range. In their periodic setting the domain
wavenumber `lambda_0` supplies an inverse-length normalization. The present
calculation uses only that structural cue; it does not import their domain,
determining wavenumber, or theorem. For the whole-space A2 bridge, the intrinsic
energy wavenumber `lambda_E=(nu/U_0)^2` supplies the dimensionally and
scale-consistent inverse-length factor.

## 7. Disposition and successor

The packet route now has a precise boundary:

```text
A2 + PI_D^* with D >= 1
    -> f in L1_t
    -> established low-mode regularity criterion
    -> regularity;

A2 scalar budgets alone
    -/-> PI_1^*
    (threshold-compatible static separation fixture at nu=U_0=1).
```

Therefore

```text
PACKET_D1_DIMENSIONALLY_NORMALIZED_CONDITIONAL_BRIDGE_PROVED__D1_NOT_IMPLIED_BY_STATIC_A2_BUDGETS.
```

The smallest genuinely dynamic successor is one of:

1. prove `PI_1^*` for Leray--Hopf trajectories satisfying `Lambda in L2_t`;
2. prove any `PI_D^*` with `D>1` under the same hypotheses;
3. prove a weaker dimensionally and scale-covariant weighted packet estimate
   that still makes the displayed Cauchy--Schwarz factorization finite;
4. produce a different equation-specific decorrelation theorem controlling
   `f` or the strict-tail endpoint without recreating closed L4/B4 interfaces.

Further static interpolation cannot establish this bridge; the fixture above
already separates it.

## Claim boundary

A2 remains unproved. `PI_1^*` is not assumed, proved for Navier--Stokes
trajectories, or certified. No universal intermittency lower bound, regularity
theorem for A2, `f in L1_t` conclusion under A2 alone, MATHCERT certification,
novelty, priority, or publication claim is asserted.
