# NS-CI-R014-A2-L5-9 — PI1 critical-energy dynamic audit

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected source head at tranche start: `24081fcc1b212d33dd865cc5512a837b8101faf1`
- Protected mathematical predecessor: merge `b05c3e6ec996a2191b7084a2438147958a58be1d`
- Predecessor work package: `NS_CI_R014_A2_L5_B3_PACKET_INTERMITTENCY_D1.md`
- Result: `PI1_CRITICAL_H12_ROUTE_REDUCED_TO_SUPERLINEAR_RICCATI__GLOBAL_CRITICAL_TRANSFER_HAS_NO_SIGN`
- A2 theorem: open
- L5: active
- MATHCERT adjudication: absent

The predecessor proves that the dimensionally normalized packet estimate
`PI_1^*` would close the established low-mode criterion, while static A2
budgets do not imply that estimate. This tranche tests the smallest natural
PDE mechanism for manufacturing `PI_1^*`: the critical
`H^{1/2} -> H^{3/2}` energy balance.

The result is a bounded route termination. It does not prove that no dynamic
packet theorem is available. It identifies the exact obstruction met by the
straight critical-energy comparison and removes a possible hidden-sign escape.

## 1. Packet target and critical Sobolev densities

Write, up to the fixed Littlewood--Paley equivalence constants,

```math
X(t):=\sum_q \lambda_q\|u_q(t)\|_2^2
\sim \|u(t)\|_{\dot H^{1/2}}^2,
```

and

```math
Y(t):=\sum_q \lambda_q^3\|u_q(t)\|_2^2
\sim \|u(t)\|_{\dot H^{3/2}}^2.
```

The packet endpoint from L5-8 is

```math
S_1(t)=\sum_{q\le Q(t)}\|u_q(t)\|_\infty^2.
```

Three-dimensional Bernstein gives shellwise

```math
\|u_q\|_\infty^2
\lesssim
\lambda_q^3\|u_q\|_2^2.
```

Therefore

```math
\boxed{
S_1(t)
\lesssim
Y_{\le Q}(t)
\le Y(t).
}
```

Consequently, a critical energy argument that supplied

```math
\int_0^T Y(t)\,dt<\infty
```

would in particular supply the finiteness needed by the `PI_1^*` bridge.
This is why the critical energy level is a genuine dynamic candidate rather
than another static interpolation.

## 2. Exact low-mode coefficient bound at the critical level

Recall

```math
f(t)=\sup_{q\le Q(t)}\lambda_q\|u_q(t)\|_\infty.
```

For every `q<=Q`, Bernstein gives

```math
\lambda_q\|u_q\|_\infty
\lesssim
\lambda_q^{5/2}\|u_q\|_2
=
\lambda_q^2
\left(\lambda_q^{1/2}\|u_q\|_2\right).
```

Since `lambda_q<=Lambda`,

```math
\lambda_q^2
\left(\lambda_q^{1/2}\|u_q\|_2\right)
\le
\Lambda^2 X^{1/2}.
```

Thus

```math
\boxed{f(t)\lesssim\Lambda(t)^2X(t)^{1/2}.}
```

This estimate uses no selector differentiation and no strict-high bound at the
active shell.

## 3. The straight critical-energy comparison is superlinear

The standard dissipation-wavenumber regularity mechanism estimates the low
part of the nonlinear interaction by the low-mode coefficient `f(t)`, while
strict-high interactions are the terms available for viscous absorption.
At the critical energy level, the optimistic selector-free closure therefore
has the schematic form

```math
X'(t)+c\nu Y(t)
\lesssim
f(t)X(t)
```

up to the fixed inhomogeneous base remainder and the usual harmless constants.
The present tranche does **not** assert that every possible critical-energy
rearrangement must have this form. It audits this standard low-mode-controlled
candidate.

Inserting the exact estimate from Section 2 yields

```math
\boxed{
X'(t)
\lesssim
\Lambda(t)^2 X(t)^{3/2}.
}
```

The selected A2 hypothesis gives `Lambda^2 in L1_t`, but the state exponent is
`3/2`, not `1`. Ordinary Gronwall therefore does not close this comparison.

The Leray budgets add

```math
X(t)
\lesssim
\|u(t)\|_2\|\nabla u(t)\|_2,
```

hence

```math
X(t)^2
\lesssim
U_0^2\|\nabla u(t)\|_2^2
```

and so

```math
X\in L^2(0,T).
```

That extra integrability still does not close the superlinear comparison.

## 4. Scalar separation of the Riccati comparison

This subsection is a comparison fixture only. It is not a Navier--Stokes
trajectory.

Let `h=T-t`, choose `p=1/4`, and set

```math
x(t)=h^{-p},
\qquad
a(t)=p h^{p/2-1}.
```

Then

```math
x'(t)=p h^{-p-1}
=a(t)x(t)^{3/2}.
```

The coefficient is integrable because

```math
p/2-1=-7/8>-1,
```

while the state retains the Leray-compatible analogue

```math
x^2\in L^1
```

because

```math
-2p=-1/2>-1.
```

Nevertheless `x(t)` diverges as `t` approaches `T`.

There is also no automatic terminal-interval rescue. The tail integral of the
coefficient has size

```math
\int_{T-h}^T a(t)dt\asymp h^{p/2},
```

while

```math
x(T-h)^{-1/2}=h^{p/2}.
```

The two quantities have exactly the same scaling. Therefore merely choosing a
late starting time so that `integral Lambda^2` is small does not, at the level
of this comparison, force the Riccati denominator to stay positive.

Hence the information

```text
Lambda^2 in L1_t,
X in L2_t,
X' <= C Lambda^2 X^(3/2)
```

is insufficient as an abstract closure mechanism.

## 5. The global critical nonlinear transfer has no universal sign

A second possible escape would be a hidden sign in the
`dot H^{1/2}`-weighted nonlinear transfer. A finite exact Fourier triad rules
out such a universal sign.

Use the wavevectors

```math
k=(1,0,0),
\qquad
\ell=(0,2,0),
\qquad
m=(-1,-2,0),
```

so `k+ell+m=0`, and define complex divergence-free Fourier coefficients

```math
u_k=(0,1,i),
\qquad
u_\ell=(1,0,i),
\qquad
u_m=(2i,-i,-1).
```

Complete these to a real field by `u_{-r}=conj(u_r)`.
Each coefficient is perpendicular to its wavevector.

For the Euler/Navier--Stokes quadratic term, write

```math
N_r
=
-i P_r
\sum_{a+b=r}(b\cdot u_a)u_b,
```

where `P_r` is the Leray projector, and set

```math
T_r=Re(\overline{u_r}\cdot N_r).
```

Direct finite arithmetic gives

```text
T_k =  4,
T_l = -4,
T_m =  0,
```

with the same values at the conjugate negative modes. Thus

```math
\sum_r T_r=0,
```

as required by the ordinary `L^2` energy cancellation. But the critical
weighted pairing is

```math
\sum_r |r|T_r
=2(4\cdot1-4\cdot2)
=-8.
```

Changing only the phase `u_m -> -u_m` preserves divergence freedom and reality
symmetry, reverses the two nonzero transfers, and gives

```math
\sum_r |r|T_r=+8.
```

Therefore

```math
\boxed{
\text{the global }\dot H^{1/2}\text{-weighted nonlinear transfer has no universal sign.}
}
```

This fixture excludes a sign-definite disposal of the complete critical
nonlinear term. It does not exclude a more selective signed cancellation tied
to the dissipation-wavenumber active set.

## 6. Relation to the existing dissipation-wavenumber criterion

The protected campaign already uses the Cheskidov--Shvydkoy low-mode
coefficient

```math
f(t)=\sup_{q\le Q(t)}\lambda_q\|u_q(t)\|_\infty.
```

Their whole-space dissipation-wavenumber criterion closes regularity when
`f in L1_t`; the same work records the weaker unconditional Leray-Hopf
integrability `Lambda in L1_t` and the sufficient pure-wavenumber condition
`Lambda in L^(5/2)_t`.

The later Cheskidov--Peng intermittency framework uses averaged Bernstein
saturation over the active range in a periodic setting. L5-8 used that only as
structural guidance for the dimensionally normalized packet quantity. Neither
paper supplies the missing implication

```text
Lambda in L2_t -> PI_1^*.
```

No literature theorem is imported as A2 evidence here.

## 7. Bounded disposition

The audited route is

```text
S_1 <= C Y
    -> try critical H^(1/2) energy closure
    -> standard low-mode coefficient f X
    -> f <= C Lambda^2 X^(1/2)
    -> X' <= C Lambda^2 X^(3/2)
    -> scalar comparison remains blow-up compatible even with X in L2;

possible hidden global H^(1/2) transfer sign
    -> exact divergence-free triad has both signs.
```

Therefore

```text
PI1_CRITICAL_H12_ROUTE_REDUCED_TO_SUPERLINEAR_RICCATI__GLOBAL_CRITICAL_TRANSFER_HAS_NO_SIGN.
```

This is not an exhaustion theorem for dynamic packet mechanisms. It terminates
the straight global/selector-free critical-energy candidate unless an
additional Navier--Stokes structure changes the comparison itself.

A material reopening requires at least one of:

1. a PDE estimate replacing `f X` by a coefficient linear in `X` whose time
   integral is controlled by the A2/Leray budgets;
2. active-shell or packet depletion that improves
   `f <= C Lambda^2 X^(1/2)` on the relevant high-`Lambda` set;
3. selected-transfer cancellation or coherence unavailable to the complete
   global critical pairing;
4. a different dimensionally and scale-covariant packet estimate that closes
   the L5-8 Cauchy--Schwarz bridge without the superlinear critical state.

Static interpolation, generic shrinking of the terminal interval, or a
universal sign of the complete critical nonlinear term do not supply such a
reopening theorem.

## Claim boundary

A2 remains unproved. `PI_1^*` remains unproved for Navier--Stokes trajectories.
The scalar comparison profile is not a Navier--Stokes solution. The Fourier
triad is a finite algebraic sign fixture, not a blow-up trajectory. No L3/L4
reopening theorem, universal intermittency theorem, MATHCERT certification,
novelty, priority, or publication claim is asserted.
