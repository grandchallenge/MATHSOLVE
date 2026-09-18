# NS-CI-R014-A2-L5-31 — finite coherent transverse shear family

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected mathematical predecessor:
  `a198d526d94e9f817b66a15128a9d20e228f25c7`
- Result:
  `FINITE_COHERENT_SHEAR_FAMILY_COLLAPSES_TO_ONE_PROFILE__R_SQUARED_DELTA_CHARGE_PERSISTS`
- A2 theorem: open
- L5: active
- C2-MIX-MULTICHANNEL: coherent same-direction finite family resolved in calibration
- MATHCERT adjudication: absent
- Evidence class: exact smooth unforced periodic 2.5D NSE calibration theorem;
  not the selected whole-space A2 class

L5-30 proves the secondary-charge mechanism for one cosine shear.

A finite coherent family of same-direction transverse shear modes does not
require a separate charge ledger. It is exactly one horizontal shear profile.

Fix a real nonconstant trigonometric polynomial

```math
G(Y)
=
\sum_{1\le |m|\le M}
\widehat G_m e^{imY},
\qquad
\widehat G_{-m}
=
\overline{\widehat G_m}.
```

Let the horizontal shear amplitude be

```math
B=\delta A,
\qquad
0<\delta\le1,
```

and define

```math
R=\frac{A}{\nu N},
\qquad
\rho=\frac{B}{\nu N}=R\delta.
```

The exact horizontal velocity is

```math
U(t,Y)
=
B
\left(
e^{\nu N^2t\partial_Y^2}G
\right)(Y).
```

A vertical carrier of amplitude `A` obeys passive advection-diffusion under
this shear. The full 2.5D field is an exact smooth unforced NSE solution.

The same two-regime argument as L5-30 survives for every fixed nonconstant
profile `G`:

- for bounded effective Reynolds `\rho`, any fixed nonzero Fourier
  coefficient of `G` produces a neighboring carrier coefficient of order
  `\rho` over a fixed parabolic-time interval;
- for large `\rho`, critical rescaling freezes the heat-evolving profile to
  `G(Y)` up to `O(h^2)`, where `h=\rho^{-1/3}`;
- exact phase removal then gives the critical amplitude limit
  `\exp[-s^3|G'(Y)|^2/3]`;
- because `G` is nonconstant, the scaled second Fourier moment is positive,
  so a fixed positive amount of carrier mass reaches
  `|n|\asymp\rho^{1/3}`;
- the corresponding selector charge is again bounded below by `c_G/\nu`.

Therefore

```math
\boxed{
R^2\delta\to\infty
\quad\Longrightarrow\quad
\int_{I_R}\Lambda(t)^2\,dt
\ge
\frac{c_G}{\nu}
}
```

for a suitable interval `I_R`.

Thus any **fixed finite coherent same-direction shear family** can be collapsed
to one generalized transport channel. There is no need to sum overlapping
channel charges.

The unresolved whole-space issue is no longer finite coherent shear
superposition. It is extracting such a coherent transverse profile from a
generic active packet.

## 1. Exact heat shear

Set

```math
Y=Nx_2.
```

Define

```math
U(t,Y)
=
B
\sum_{1\le |m|\le M}
\widehat G_m
e^{-m^2\nu N^2t}
e^{imY}.
```

Let

```math
v=(U,0).
```

Because `U` is independent of `x_1`,

```math
(v\cdot\nabla)v=0.
```

Also

```math
\partial_tU
=
\nu\partial_{x_2}^2U.
```

Thus `v` is an exact horizontal NSE heat shear.

## 2. Exact vertical carrier

Let

```math
z(0,x)
=
A\cos(Nx_1)
```

and solve

```math
\partial_tz
+
U(t,Y)\partial_{x_1}z
=
\nu\Delta z.
```

Then

```math
u=(U,0,z)
```

is an exact smooth unforced periodic 2.5D NSE solution.

No finite-dimensional invariance of the vertical carrier is assumed.

## 3. Effective shear normalization

Set

```math
z=A\theta.
```

Use shear-turnover time

```math
\tau=BNt.
```

Then

```math
\boxed{
\partial_\tau\theta
+
G_\rho(\tau,Y)\partial_X\theta
=
\rho^{-1}\Delta\theta,
}
```

where

```math
G_\rho(\tau,\cdot)
=
e^{(\tau/\rho)\partial_Y^2}G.
```

The carrier starts from

```math
\theta(0,X,Y)=\cos X.
```

## 4. Bounded-\(\rho\) coefficient generation

Use parabolic time

```math
\sigma=\nu N^2t.
```

For the complex carrier write

```math
z
=
A\operatorname{Re}
[
e^{iX}\psi_\rho(\sigma,Y)
].
```

Then

```math
\partial_\sigma\psi_\rho
+
i\rho
G_\sigma(Y)\psi_\rho
=
(\partial_Y^2-1)\psi_\rho,
```

with

```math
G_\sigma=e^{\sigma\partial_Y^2}G,
\qquad
\psi_\rho(0)=1.
```

Choose one fixed `m_0\ne0` such that

```math
\widehat G_{m_0}\ne0.
```

At `\rho=0`,

```math
\psi_0=e^{-\sigma}.
```

The first Duhamel iterate at Fourier index `m_0` is

```math
\boxed{
a_{m_0,\mathrm{lin}}^\rho(\sigma)
=
-i\rho
\widehat G_{m_0}
\sigma
e^{-(1+m_0^2)\sigma}.
}
```

The identity is exact at first order because the heat decay of the profile
mode, the carrier zero mode, and the target semigroup combine to the same
factor `e^{-(1+m_0^2)\sigma}`.

For every fixed `M_\rho<\infty`, Duhamel contraction gives

```math
|a_{m_0}^\rho-a_{m_0,\mathrm{lin}}^\rho|
\le
C_G\rho^2\sigma^2
```

on a fixed short interval.

Choose

```math
\sigma_*
=
c_{G}/M_\rho
```

small enough. Then uniformly for

```math
0<\rho\le M_\rho
```

and

```math
\sigma_*/2
\le
\sigma
\le
\sigma_*,
```

one has

```math
\boxed{
|a_{m_0}^\rho|
\ge
c_{G,M_\rho}\rho.
}
```

## 5. Bounded-\(\rho\) threshold and charge

The corresponding physical frequency is

```math
N(1,m_0,0),
```

a fixed multiple of `N`.

Finite LP overlap therefore gives a physical block with

```math
\|u_p\|_\infty
\ge
c_{G,M_\rho}A\rho.
```

Hence

```math
\lambda_p^{-1}\|u_p\|_\infty
\ge
c_{G,M_\rho}\nu R\rho.
```

Whenever

```math
R\rho
=
R^2\delta
\to\infty,
```

this block violates the fixed campaign threshold.

The interval has physical length comparable to

```math
(\nu N^2)^{-1},
```

so

```math
\boxed{
\int_{I_{\rm bd}}
\Lambda(t)^2\,dt
\ge
\frac{c_{G,M_\rho}}{\nu}.
}
```

## 6. Large-\(\rho\) critical scaling

Set

```math
h=\rho^{-1/3},
\qquad
s=h\tau.
```

For the complex `X\)-frequency-one carrier,

```math
\Phi_h(s,Y)
=
\psi_\rho(\tau,Y),
```

the exact critical equation is

```math
\boxed{
\partial_s\Phi_h
+
ih^{-1}
G_h(s,Y)\Phi_h
=
h^2(\partial_Y^2-1)\Phi_h,
}
```

where

```math
G_h(s,\cdot)
=
e^{h^2s\partial_Y^2}G.
```

Because `G` has fixed finite Fourier support,

```math
G_h(s)
=
G+O(h^2)
```

in every fixed Sobolev norm on bounded `s\)-intervals.

## 7. Exact time-dependent phase removal

Define

```math
F_h(s,Y)
=
\int_0^s
G_h(\sigma,Y)\,d\sigma.
```

Then

```math
F_h(s,Y)
=
sG(Y)+O(h^2)
```

in every fixed Sobolev norm.

Set

```math
\Phi_h
=
e^{-ih^{-1}F_h}A_h.
```

Because

```math
\partial_sF_h=G_h,
```

the fast potential cancels exactly.

A direct calculation gives

```math
\boxed{
\begin{aligned}
\partial_sA_h
={}&
h^2\partial_Y^2A_h
-
2ih(F_h)_Y\partial_YA_h
-
ih(F_h)_{YY}A_h
\\
&-
|(F_h)_Y|^2A_h
-
h^2A_h.
\end{aligned}
}
```

## 8. Critical profile limit

Since

```math
(F_h)_Y
=
sG'(Y)+O(h^2),
```

the limiting amplitude obeys

```math
\partial_sA_0
=
-s^2|G'(Y)|^2A_0,
\qquad
A_0(0)=1.
```

Thus

```math
\boxed{
A_0(s,Y)
=
\exp\left(
-\frac{s^3}{3}|G'(Y)|^2
\right).
}
```

Fixed-window Sobolev energy estimates give, for every fixed `k`,

```math
\sup_{0\le s\le S}
\|A_h-A_0\|_{H^k}
\le
C_{G,k,S}h.
```

The proof is the same critical energy mechanism as L5-26, with the
`O(h^2)` profile-freezing error absorbed into the operator remainder.

## 9. Nondegenerate scaled Fourier moments

Write

```math
\Phi_h
=
\sum_n
a_n^{(h)}e^{inY}.
```

The exact first derivative identity is

```math
h\partial_Y\Phi_h
=
e^{-ih^{-1}F_h}
[
h\partial_YA_h
-i(F_h)_YA_h
].
```

Therefore

```math
\boxed{
h^2
\sum_n
n^2|a_n^{(h)}|^2
\longrightarrow
s^2
\|G'A_0\|_2^2.
}
```

Since `G` is nonconstant and `A_0>0`,

```math
\|G'A_0\|_2>0
```

for every `s>0`.

Similarly,

```math
\boxed{
h^4
\sum_n
n^4|a_n^{(h)}|^2
\longrightarrow
s^4
\|(G')^2A_0\|_2^2.
}
```

On any compact positive `s\)-interval, zeroth mass is uniformly positive,
scaled second moment uniformly positive, and scaled fourth moment uniformly
finite.

## 10. Critical band mass and charge

The same normalized Paley--Zygmund/Markov argument as L5-26 gives constants

```math
0<c_-<c_+<\infty,
\qquad
m_G>0
```

such that

```math
\sum_{c_-\le|hn|\le c_+}
|a_n^{(h)}(s)|^2
\ge
m_G
```

throughout one fixed positive critical interval.

The band has `O(h^{-1})` modes, so some coefficient satisfies

```math
|a_n^{(h)}|
\ge
c_Gh^{1/2}.
```

The physical block frequency is

```math
\lambda_p
\asymp
Nh^{-1}
=
N\rho^{1/3}.
```

Its amplitude is at least

```math
c_GAh^{1/2}.
```

Hence

```math
\lambda_p^{-1}\|u_p\|_\infty
\ge
c_G\nu
\frac{R}{\sqrt\rho}.
```

Because

```math
\rho=R\delta\le R,
```

this exceeds the fixed threshold for large `R`.

The physical critical time element is

```math
dt
=
\frac{\rho^{-2/3}}{\nu N^2}\,ds.
```

Thus

```math
\boxed{
\int_{I_{\rm crit}}
\Lambda(t)^2\,dt
\ge
\frac{c_G}{\nu}.
}
```

## 11. Combined general-profile theorem

Fix one nonconstant real trigonometric polynomial `G`.

Let

```math
R_j\to\infty,
\qquad
0<\delta_j\le1,
\qquad
\rho_j=R_j\delta_j.
```

If

```math
R_j^2\delta_j
=
R_j\rho_j
\to\infty,
```

then there is an interval `I_j` such that

```math
\boxed{
\int_{I_j}
\Lambda_j(t)^2\,dt
\ge
\frac{c_G}{\nu}
}
```

for all sufficiently large `j`.

The constant depends on the fixed profile but not on `R_j`.

## 12. Finite coherent families collapse to one channel

Any finite family of same-direction transverse Fourier shears with fixed
normalized frequencies and fixed relative coefficients is exactly one
trigonometric polynomial `G`.

Their heat evolution is already included in

```math
e^{\nu N^2t\partial_Y^2}G.
```

Therefore such a family should not be assigned separate overlapping charge
ledgers.

If the combined profile is nonconstant, its critical phase gradient
`G'` supplies the single nondegenerate mixing observable.

This removes finite coherent same-direction channel count as an obstruction.

## 13. What remains unresolved

The theorem requires:

- a common transverse coordinate;
- a common horizontal transport direction;
- fixed finite normalized profile complexity;
- temporal coherence through exact shear heat evolution.

A generic whole-space active packet need not admit such a representation.

In particular, instantaneous polarization decomposition does not imply that
the components retain a common coherent shear profile over the critical
interval.

## 14. Next live obligation: C2-MIX-COHERENCE

The smallest safe successor is:

> Can selected whole-space active-band dynamics produce, or be decomposed into,
> a coherent transverse transport profile over the critical time scale without
> assuming that coherence a priori?

The first audit should quantify profile drift.

A useful positive theorem would permit

```math
G_h(s,Y)
=
G_0(Y)
+
\mathcal E_h(s,Y)
```

with a critical norm small enough that the generalized phase-removal theorem
survives.

A negative theorem should exhibit the first whole-space interaction that
changes transport direction/profile at order one on the critical interval.

## 15. Hard rejection tests

Reject any successor that:

- sums selector charges from overlapping coherent shear components;
- treats a one-time Fourier decomposition as temporal coherence;
- assumes fixed profile complexity without stating it;
- promotes the periodic 2.5D calibration to the selected whole-space class;
- infers exact shear structure from shell energies;
- calls the unresolved `R^2\delta=O(1)` regime charge-free.

## 16. Claim boundary

The protected claim sought from this tranche is exactly

```text
FINITE_COHERENT_SHEAR_FAMILY_COLLAPSES_TO_ONE_PROFILE
__R_SQUARED_DELTA_CHARGE_PERSISTS.
```

It proves, for exact smooth unforced periodic 2.5D NSE:

- any fixed finite coherent same-direction shear family is one heat-evolving
  transverse profile;
- bounded effective Reynolds generates a fixed neighboring carrier mode;
- large effective Reynolds has critical limit
  `exp[-s^3|G'|^2/3]`;
- every nonconstant fixed profile has nondegenerate critical Fourier variance;
- `R^2\delta\to\infty` forces selector charge `c_G/\nu`;
- no separate overlapping charge sum is needed.

It does not derive coherent transverse profiles from selected whole-space
solutions.

It does not prove A2.

It does not reopen L3 or L4.

No MATHCERT, novelty, priority, or publication claim is asserted.
