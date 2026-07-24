# NS-CI-WP00 — Quantitative L4_t L6_x reconstruction

## Status

- Campaign: `NS-CI-001`
- Parent tracker: `grandchallenge/MATH-PROGRAMME#55`
- Source input: `grandchallenge/MATHFORGE#15`
- Result class: reconstruction of a classical conditional argument
- New theorem claim: none

## 1. Purpose

This document exposes the estimate behind the `(q,p)=(4,6)` Ladyzhenskaya–Prodi–Serrin criterion. It separates three tasks:

1. propagation of an `H1` strong norm under a finite `L4_tL6_x` integral;
2. uniqueness of an energy solution relative to a solution in `L4_tL6_x`;
3. continuation of the maximal strong solution.

The argument consumes the critical integral. It does not produce that integral from the energy inequality.

## 2. Working equation and hypotheses

On `R3`, consider

```math
\partial_t u-\nu\Delta u+(u\cdot\nabla)u+\nabla p=0,
\qquad \nabla\cdot u=0,
\qquad \nu>0.
```

For the differential estimates, begin with a sufficiently smooth decaying solution. Their extension to the standard strong-solution class is by the approximation and density machinery of the chosen local theory. This extension remains an imported analytic interface until its exact theorem statement is committed.

## 3. Critical H1 estimate

Take the `L2` inner product of the equation with `-Delta u`. The pressure term vanishes by incompressibility and decay. Thus

```math
\frac12\frac{d}{dt}\|\nabla u\|_2^2
 +\nu\|\Delta u\|_2^2
 =\int_{\mathbb R^3}(u\cdot\nabla)u\cdot\Delta u\,dx.
```

By Hölder,

```math
\left|\int (u\cdot\nabla)u\cdot\Delta u\right|
\le \|u\|_6\,\|\nabla u\|_3\,\|\Delta u\|_2.
```

The three-dimensional Gagliardo–Nirenberg estimate gives

```math
\|\nabla u\|_3
\le C\|\nabla u\|_2^{1/2}\|D^2u\|_2^{1/2}.
```

On `R3`, Fourier multiplier equivalence permits `||D2 u||2` to be replaced by `||Delta u||2`. Therefore

```math
\left|\int (u\cdot\nabla)u\cdot\Delta u\right|
\le C\|u\|_6\|\nabla u\|_2^{1/2}\|\Delta u\|_2^{3/2}.
```

Young's inequality with conjugate exponents `4/3` and `4` yields

```math
C\|u\|_6\|\nabla u\|_2^{1/2}\|\Delta u\|_2^{3/2}
\le \frac\nu2\|\Delta u\|_2^2
 +C\nu^{-3}\|u\|_6^4\|\nabla u\|_2^2.
```

Hence

```math
\frac{d}{dt}\|\nabla u\|_2^2
 +\nu\|\Delta u\|_2^2
\le C\nu^{-3}\|u\|_6^4\|\nabla u\|_2^2.
```

Gronwall gives, for every time on which the strong solution exists,

```math
\|\nabla u(t)\|_2^2
\le \|\nabla u(0)\|_2^2
\exp\!\left(C\nu^{-3}\int_0^t\|u(s)\|_6^4\,ds\right).
```

It also gives an `L2_t H2_x` bound after integration of the dissipative term.

### Exact bottleneck

The coefficient in Gronwall is precisely

```math
\nu^{-3}\|u(t)\|_6^4.
```

The standard energy inequality controls `||u||6^2` in time through Sobolev, not `||u||6^4`. The missing exponent is therefore present at the exact point where the nonlinear term is absorbed into viscosity.

## 4. Weak–strong uniqueness estimate at the same exponent

Let `u` and `v` be two solutions with the same initial datum, and suppose `u` is the controlled solution. Set `w=v-u`. Formally, the difference equation and incompressibility give

```math
\frac12\frac{d}{dt}\|w\|_2^2+\nu\|\nabla w\|_2^2
=-\int (w\cdot\nabla)u\cdot w\,dx.
```

Integration by parts rewrites the nonlinear term as

```math
\int (w\cdot\nabla)u\cdot w
=-\int (w\cdot\nabla)w\cdot u.
```

Then

```math
\left|\int (w\cdot\nabla)w\cdot u\right|
\le \|u\|_6\|w\|_3\|\nabla w\|_2.
```

Interpolation gives

```math
\|w\|_3\le C\|w\|_2^{1/2}\|\nabla w\|_2^{1/2},
```

so Young's inequality yields

```math
\left|\int (w\cdot\nabla)w\cdot u\right|
\le \frac\nu2\|\nabla w\|_2^2
 +C\nu^{-3}\|u\|_6^4\|w\|_2^2.
```

Consequently,

```math
\frac{d}{dt}\|w\|_2^2
\le C\nu^{-3}\|u\|_6^4\|w\|_2^2.
```

If `u in L4(0,T;L6)`, Gronwall and `w(0)=0` imply `w=0`. In the Leray–Hopf setting, the formal testing and time regularization must be supplied by the source-audited weak–strong uniqueness theorem; this calculation identifies its operative exponent.

## 5. Maximal-time continuation consequence

Let `u` be the maximal `H1` strong solution on `[0,T*)`, where the local existence theorem has a restart criterion controlled by the `H1` norm. Suppose

```math
\int_0^{T_*}\|u(t)\|_6^4\,dt<\infty.
```

The estimate in Section 3 gives

```math
\sup_{0\le t<T_*}\|\nabla u(t)\|_2<\infty.
```

Together with the energy estimate, the `H1` norm remains bounded. The local theory can then be restarted from times approaching `T*` with a lifespan bounded below by that norm, contradicting maximality. Therefore

```math
T_*<\infty
\quad\Longrightarrow\quad
\int_0^{T_*}\|u(t)\|_6^4\,dt=\infty.
```

This is the critical-integral blow-up alternative used by the campaign.

## 6. One-way implication to the official whole-space positive branch

The official Clay whole-space branch quantifies over every smooth divergence-free datum satisfying rapid decay condition (4), not only compactly supported data.

For that full data class, the campaign implication is:

```text
global Leray weak existence
 + universal finite L4_tL6_x integral for every finite T
 + LPS strong-solution theorem
 + weak-strong uniqueness
 + parabolic bootstrapping
 -> global smooth solution with bounded energy.
```

Thus the full-data universal integral statement is sufficient for the official whole-space positive branch.

The compact-support-only challenge is a strict restricted lane. No density argument currently in the campaign upgrades it to the full rapidly decreasing class.

## 7. Reverse implication and terminology decision

The phrase `equivalent to the Clay problem` is not promoted in WP00. To establish the reverse direction one must explicitly show:

1. a solution satisfying Fefferman's global smoothness and bounded-energy requirements lies in the local strong class on every finite interval;
2. its `L4_tL6_x` norm is finite on every finite interval;
3. every Leray–Hopf solution with the same datum agrees with it.

These statements are standard in the intended framework, but the exact bridge is not contained merely in the wording of the official problem. Until the source-normalized bridge is committed, the approved wording is:

> Universal critical integrability for the Fefferman whole-space data class is sufficient for Clay statement (A). Bidirectional equivalence remains conditional on the reverse strong-class and weak–strong correspondence audit.

## 8. What has and has not been discharged

### Discharged operationally

- The exponent `(4,6)` is in the non-endpoint LPS range.
- The nonlinear estimate produces `||u||6^4` exactly.
- Finite critical integral prevents finite maximal `H1` breakdown, conditional on standard local theory.
- The same integral coefficient closes the weak–strong difference estimate.
- Compact support is narrower than the official rapidly decreasing data class.

### Still pending

- exact original theorem-text extraction for Serrin;
- mathematical translation audit of Ladyzhenskaya 1967;
- original Leray theorem-number map;
- a source-normalized reverse implication from Fefferman smoothness to the universal every-Leray–Hopf formulation;
- theorem-prover certification of the scaling substrate.

## 9. Route discipline

Any proposed mechanism must identify how it improves or bypasses

```math
\|u\|_6\|\nabla u\|_2^{1/2}\|\Delta u\|_2^{3/2}
```

without assuming an already regular norm. It must also preserve or explicitly exploit the critical scaling. Mechanism generation remains blocked until the programme claim and debt ledgers incorporate the source-audit correction.
