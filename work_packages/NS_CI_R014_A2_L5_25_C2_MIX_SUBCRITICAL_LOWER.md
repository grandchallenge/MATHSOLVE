# NS-CI-R014-A2-L5-25 — subcritical cubic-root threshold propagation

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected base: `5ca8a2364be241bccbc36f99731f53b069c4da8c`
- Protected predecessor: `NS-CI-R014-A2-L5-24`
- Result:
  `SHEAR_CHAIN_SUBCRITICAL_CUBIC_ROOT_THRESHOLD_PROPAGATION_PROVED__CRITICAL_WINDOW_REMAINS_OPEN`
- A2 theorem: open
- L5: active
- C2-MIX: lower reach proved on every subcritical cubic-root window
- MATHCERT adjudication: absent
- Evidence class: exact theorem for the smooth unforced periodic 2.5D shear
  calibration protected in L5-23/L5-24; not the selected whole-space A2 class

L5-24 proves an all-time upper threshold reach arbitrarily close to
`R^{1/3}`. The complementary lower question can also be resolved below the
critical exponent without any pointwise Bessel asymptotic.

Let

```math
T_R=R^\beta,
\qquad
0<\beta<1/3.
```

For every turnover time

```math
T_R\le\tau\le2T_R,
```

the exact finite-viscosity shear-chain solution has a fixed positive amount of
`L^2` Fourier mass in the moving chain band

```math
\tau/2\le |n|\le2\tau
```

for all sufficiently large `R`.

The proof has two elementary parts:

1. the inviscid chain has fixed positive mass in that band, obtained only from
   its exact second and fourth Fourier moments;
2. the finite-viscosity solution differs from the inviscid solution in
   `L^2` by at most
   `C epsilon (1+tau)^3`, which is `o(1)` uniformly on every
   `tau<=2R^\beta` with `\beta<1/3`.

The band contains only `O(\tau)` modes, so at least one coefficient satisfies

```math
|a_n^\varepsilon(\tau)|
\ge
c\tau^{-1/2}.
```

After restoring physical scaling, a nearby LP block has threshold ratio

```math
\lambda_p^{-1}\|u_p\|_\infty
\ge
c\nu R\tau^{-3/2}.
```

This diverges uniformly on `[T_R,2T_R]` for every `\beta<1/3`. Hence

```math
\boxed{
\Lambda(t)
\ge
c N R^\beta
}
```

throughout that normalized turnover interval, for all sufficiently large
`R`.

Therefore threshold-sized spectral propagation genuinely reaches every power
`R^\beta` below the cubic-root scale. Combined with L5-24, the calibration
threshold reach is pinned to `R^{1/3+o(1)}` in the power-law sense.

The associated selector charge is only

```math
\int\Lambda^2dt
\ge
\frac c\nu R^{3\beta-1},
```

which still tends to zero for every fixed `\beta<1/3`.

Thus the exact critical window `\tau\asymp R^{1/3}` is the first unresolved
scale at which this calibration could produce order-one A2 charge.

## 1. Exact finite-viscosity and inviscid equations

Retain the L5-23/L5-24 scalar equation

```math
\partial_\tau\phi_\varepsilon
+
i e^{-\varepsilon\tau}\cos Y\,\phi_\varepsilon
=
\varepsilon(\partial_Y^2-1)\phi_\varepsilon,
\qquad
\phi_\varepsilon(0,Y)=1.
```

The inviscid comparison is

```math
\partial_\tau\phi_0
+
i\cos Y\,\phi_0
=
0,
\qquad
\phi_0(0,Y)=1.
```

It is explicit:

```math
\phi_0(\tau,Y)
=
e^{-i\tau\cos Y}
=
\sum_{n\in\mathbb Z}
(-i)^nJ_n(\tau)e^{inY}.
```

No pointwise lower bound for a particular Bessel coefficient will be used.

## 2. Polynomial finite-time derivative bounds

For fixed integer `s>=0`, the differentiated energy inequality used in
L5-24 also gives the simpler finite-time estimate

```math
\frac d{d\tau}
\|\partial_Y^s\phi_\varepsilon\|_2
\le
C_s
\sum_{r=0}^{s-1}
\|\partial_Y^r\phi_\varepsilon\|_2,
```

after discarding the nonpositive viscous terms.

Since

```math
\|\phi_\varepsilon(\tau)\|_2\le1,
```

induction gives

```math
\boxed{
\|\partial_Y^s\phi_\varepsilon(\tau)\|_2
\le
C_s(1+\tau)^s
}
```

uniformly in `\varepsilon\in(0,1]`.

In particular,

```math
\|\partial_Y^2\phi_\varepsilon(\tau)\|_2
\le
C(1+\tau)^2.
```

## 3. Growing-window viscous-to-inviscid L2 comparison

Set

```math
z_\varepsilon
=
\phi_\varepsilon-\phi_0.
```

Rewrite the finite-viscosity equation with the inviscid transport operator:

```math
\partial_\tau z_\varepsilon
+
i\cos Y\,z_\varepsilon
=
\varepsilon(\partial_Y^2-1)\phi_\varepsilon
+
i(1-e^{-\varepsilon\tau})
\cos Y\,\phi_\varepsilon.
```

The left multiplication operator is skew-adjoint.

Using

```math
1-e^{-\varepsilon\tau}
\le
\varepsilon\tau,
```

the derivative bound above, and
`\|\phi_\varepsilon\|_2<=1`, one obtains

```math
\frac d{d\tau}
\|z_\varepsilon\|_2
\le
C\varepsilon(1+\tau)^2.
```

Since `z_\varepsilon(0)=0`,

```math
\boxed{
\|\phi_\varepsilon(\tau)-\phi_0(\tau)\|_2
\le
C\varepsilon(1+\tau)^3.
}
```

Now let

```math
T_R
=
R^\beta
=
\varepsilon^{-\beta},
\qquad
\beta<1/3.
```

Uniformly for

```math
0\le\tau\le2T_R,
```

the error is

```math
O(
\varepsilon^{1-3\beta}
),
```

and therefore tends to zero.

This is the growing-window remainder that was missing after L5-24.

## 4. Exact inviscid second Fourier moment

Normalize the torus measure so that

```math
\|\phi_0\|_2=1.
```

Because

```math
\partial_Y\phi_0
=
i\tau\sin Y\,\phi_0,
```

one has

```math
\sum_n
n^2
|J_n(\tau)|^2
=
\|\partial_Y\phi_0\|_2^2
=
\frac{\tau^2}{2}.
```

Thus the exact second moment of the inviscid chain distribution is
`\tau^2/2`.

## 5. Exact inviscid fourth Fourier moment

A second derivative gives

```math
\partial_Y^2\phi_0
=
\big(
i\tau\cos Y
-
\tau^2\sin^2Y
\big)
\phi_0.
```

The two displayed terms are respectively imaginary and real, so their cross
term vanishes in the squared modulus.

Using

```math
\langle\cos^2Y\rangle=\frac12,
\qquad
\langle\sin^4Y\rangle=\frac38,
```

one obtains

```math
\boxed{
\sum_n
n^4
|J_n(\tau)|^2
=
\frac{\tau^2}{2}
+
\frac{3\tau^4}{8}.
}
```

For `\tau>=1`,

```math
\sum_n n^4|J_n(\tau)|^2
\le
\frac78\tau^4.
```

## 6. Constant inviscid mass in a ballistic chain band

Regard

```math
p_n(\tau)=|J_n(\tau)|^2
```

as a probability distribution.

Apply Paley--Zygmund to the nonnegative random variable `n^2` with
parameter `1/2`.

Using the exact moments above,

```math
\mathbb P(
|n|\ge\tau/2
)
\ge
\frac1{14}
```

for `\tau>=1`.

Markov applied to the fourth moment gives

```math
\mathbb P(
|n|>2\tau
)
\le
\frac7{128}.
```

Therefore

```math
\boxed{
\sum_{\tau/2\le|n|\le2\tau}
|J_n(\tau)|^2
\ge
m_0,
\qquad
m_0
=
\frac{15}{896}.
}
```

This lower bound is uniform for every `\tau>=1`.

No stationary-phase or Airy asymptotic is needed.

## 7. Transfer the band mass to finite viscosity

Let `P_\tau` denote the Fourier projection onto

```math
B_\tau
=
\{
n:
\tau/2\le|n|\le2\tau
\}.
```

Since orthogonal projection is contractive,

```math
\|P_\tau\phi_\varepsilon\|_2
\ge
\|P_\tau\phi_0\|_2
-
\|\phi_\varepsilon-\phi_0\|_2.
```

For `\tau\in[T_R,2T_R]`, the inviscid term is at least
`\sqrt{m_0}`, while the comparison error tends uniformly to zero for
`\beta<1/3`.

Hence, for all sufficiently large `R`,

```math
\boxed{
\sum_{n\in B_\tau}
|a_n^\varepsilon(\tau)|^2
\ge
\frac{m_0}{4}
}
```

for every

```math
T_R\le\tau\le2T_R.
```

## 8. One coefficient is polynomially large

For `\tau>=1`, the band `B_\tau` contains at most `6\tau` integer
indices.

Therefore the preceding mass bound implies that for every
`\tau\in[T_R,2T_R]` there exists an index `n(\tau)\in B_\tau` such that

```math
\boxed{
|a_{n(\tau)}^\varepsilon(\tau)|^2
\ge
\frac{m_0}{24\tau}.
}
```

Equivalently,

```math
|a_{n(\tau)}^\varepsilon(\tau)|
\ge
c_*\tau^{-1/2}
```

for one absolute `c_*>0`.

The chosen index may vary with time. No modal residence is assumed.

## 9. Convert one Fourier coefficient to an LP threshold violation

The corresponding physical vertical Fourier frequency is

```math
N(1,n(\tau),0),
```

whose magnitude is comparable to

```math
N\tau
```

throughout the band.

The real physical vertical velocity has Fourier coefficient equal, up to the
fixed real-part factor, to

```math
A a_{n(\tau)}^\varepsilon.
```

A fixed smooth LP partition has finite overlap. Hence at that frequency at
least one overlapping dyadic multiplier has magnitude bounded below by a
partition constant.

For that block,

```math
\|u_p(t)\|_\infty
\ge
c A\tau^{-1/2}.
```

Since

```math
\lambda_p
\asymp
N\tau,
\qquad
A=R\nu N,
```

one obtains

```math
\boxed{
\lambda_p^{-1}
\|u_p(t)\|_\infty
\ge
c\nu
R\tau^{-3/2}.
}
```

On

```math
T_R\le\tau\le2T_R,
\qquad
T_R=R^\beta,
```

this is bounded below by

```math
c\nu
R^{1-3\beta/2}.
```

For every fixed `\beta<1/3`, the exponent is positive. Thus the block violates
the campaign strict-high threshold for all sufficiently large `R`.

## 10. Selector lower bound throughout the moving interval

At every turnover time

```math
T_R\le\tau\le2T_R,
```

there is therefore a threshold-violating shell with frequency comparable to
`N\tau`.

By the definition of the dissipation index,

```math
\boxed{
\Lambda(t)
\ge
cN\tau
\ge
cN T_R.
}
```

No selector continuity and no fixed violating shell are used.

Thus

```math
\boxed{
\Lambda(t)
\ge
cN R^\beta
}
```

throughout the corresponding physical interval for every fixed
`\beta<1/3`.

## 11. Lower selector charge

Use

```math
dt
=
\frac{d\tau}{R\nu N^2}.
```

Then

```math
\int_{T_R/(AN)}^{2T_R/(AN)}
\Lambda(t)^2\,dt
\ge
\frac c{R\nu}
\int_{T_R}^{2T_R}
\tau^2\,d\tau.
```

Hence

```math
\boxed{
\int_{T_R/(AN)}^{2T_R/(AN)}
\Lambda(t)^2\,dt
\ge
\frac c\nu
R^{3\beta-1}.
}
```

For every fixed `\beta<1/3` this still tends to zero.

Therefore actual threshold propagation below the cubic-root scale does not by
itself repair A2.

## 12. Power-law pinning of the threshold front

L5-24 proves that for every `\delta>0`,

```math
\Lambda(t)
\le
C_\delta
N R^{1/3+\delta}
```

throughout the calibration.

The present tranche proves that for every `\eta>0`, taking

```math
\beta=1/3-\eta
```

gives, on the corresponding moving interval,

```math
\Lambda(t)
\ge
c_\eta
N R^{1/3-\eta}.
```

Thus the exact shear calibration has threshold reach pinned in the power-law
sense to

```math
\boxed{
R^{1/3+o(1)}.
}
```

This statement concerns exponents only. It does not provide the exact critical
profile or constant.

## 13. The critical cubic-root window remains open

At the exact scale

```math
\tau
\asymp
R^{1/3},
```

the elementary comparison error

```math
\varepsilon\tau^3
```

is order one.

Therefore the present perturbative argument stops exactly where the selector
charge can first become order one:

```math
\frac{\tau^3}{R}
\asymp1.
```

This identifies a sharp methodological boundary rather than a bookkeeping
gap.

Resolving the critical window requires a nonperturbative finite-viscosity
description.

## 14. Next live obligation: C2-MIX-CRITICAL

The smallest safe successor is:

> At `\tau=cR^{1/3}` with fixed positive `c`, does the finite-viscosity shear
> chain retain a positive amount of Fourier mass at `|n|\asymp R^{1/3}`, or
> does viscous/enhanced dissipation reduce that mass below the campaign
> threshold?

The perturbative `L^2` comparison used here cannot answer this because its
error is order one at the critical scale.

Valid next tools include:

- a rescaled critical-limit equation for
  `n=R^{1/3}\xi`, `\tau=R^{1/3}s`;
- Feynman--Kac/Brownian phase analysis retaining the order-one diffusion;
- a critical hypocoercive estimate with matching lower information;
- a discrete WKB or semiclassical analysis of the exact nearest-neighbour
  chain.

## 15. Hard rejection tests

Reject any successor that:

- extrapolates the present `o(1)` comparison to `\beta=1/3`;
- treats `R^{1/3+o(1)}` exponent pinning as an exact critical profile;
- infers order-one A2 charge from a subcritical lower bound;
- uses one instant of threshold violation instead of the proved moving
  interval;
- assumes the same violating shell persists;
- imports inviscid Bessel amplitudes at critical time without an order-one
  finite-viscosity analysis;
- treats this periodic 2.5D calibration as the selected whole-space result.

## 16. Claim boundary

The protected claim sought from this tranche is exactly

```text
SHEAR_CHAIN_SUBCRITICAL_CUBIC_ROOT_THRESHOLD_PROPAGATION_PROVED
__CRITICAL_WINDOW_REMAINS_OPEN.
```

It proves, in the exact L5-23 shear calibration:

- finite-viscosity/inviscid `L^2` comparison
  `\|\phi_\varepsilon-\phi_0\|_2<=C\varepsilon(1+\tau)^3`;
- fixed positive inviscid Fourier mass in
  `\tau/2<=|n|<=2\tau`;
- fixed positive finite-viscosity mass in that band uniformly on every
  `\tau\in[R^\beta,2R^\beta]` with `\beta<1/3`;
- one coefficient of size at least `c\tau^{-1/2}`;
- a threshold-violating LP block at frequency comparable to `N\tau`;
- selector lower reach `\Lambda>=cNR^\beta`;
- lower selector charge `c\nu^{-1}R^{3\beta-1}`;
- power-law threshold-front pinning to `R^{1/3+o(1)}`.

It does not prove A2.

It does not resolve the exact critical `R^{1/3}` window.

It does not prove order-one selector charge.

It does not prove the selected whole-space result.

No MATHCERT, novelty, priority, or publication claim is asserted.
