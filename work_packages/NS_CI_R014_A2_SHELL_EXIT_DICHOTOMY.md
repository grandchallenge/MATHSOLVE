# NS-CI-R014-A2-L3c — Buffered shell-exit dichotomy

## Status

- Campaign: `NS-CI-001`
- Parent: `MATHSOLVE#24`
- Tracker: `MATHSOLVE#30`
- Result: `PROVED_BUFFERED_EXIT_CHARGE_PACKING_INSUFFICIENT`
- A2 status: unproved

This package proves a rigorous first-exit inequality for a dyadic shell after the principal low–high transport has been removed. A buffered shell that loses half its amplitude in less than one parabolic time must charge a scale-invariant local dissipation quantity. The resulting packing law is valid but too weak: its physical cost is proportional to `lambda_q^{-1}`, which is summable over dyadic levels. Thus energy-charged exits alone cannot close the A2 layer-cake gap.

## Projected transport equation

Fix a dyadic shell `q` and set

```math
A_q(t)=\|u_q(t)\|_\infty,
\qquad
\theta_q=c_0\nu\lambda_q,
\qquad
a_q=u_{\le q-2}.
```

The projected equation may be written

```math
\partial_tu_q+a_q\cdot\nabla u_q-\nu\Delta u_q=R_q.
```

The interaction audit in `NS_CI_R014_A2_FORCING_DEFECT.md` gives the schematic bound

```math
\|R_q(t)\|_\infty
\lesssim
G_q(t)M_q(t)+H_q(t),
```

where

```math
G_q=\|\nabla u_{\le q-2}\|_\infty,
\qquad
M_q=\max_{|p-q|\le C}\|u_p\|_\infty,
```

and the absolute high–high remainder satisfies

```math
\frac1{\nu\lambda_q}\int_IH_q(t)dt
\lesssim
\mathcal E_q(I),
```

with

```math
\mathcal E_q(I)
=
\frac{\lambda_q}{\nu}
\int_I\|\nabla u(t)\|_2^2dt.
```

For each fixed `q`, the projected equation supplies an absolutely continuous spatially smooth representative. The argument below may equivalently be performed on standard smooth approximations, with constants independent of the approximation.

## Last-passage normalization

Suppose a shell drops from at least `2 theta_q` to `theta_q`. Define `t_*` to be the first exit time below `theta_q`, and replace the initial time by the last time `s<t_*` at which

```math
A_q(s)=2\theta_q.
```

Then

```math
\theta_q\le A_q(t)\le2\theta_q
\qquad
(s\le t\le t_*).
```

This normalization removes prior upward excursions. It does not assert a uniform threshold buffer for the dissipation wavenumber; the lemma is conditional on a buffered event.

Define the finite-neighbour ratio

```math
K_q(I)
=
\sup_{t\in I}
\frac{M_q(t)}{\theta_q},
\qquad I=[s,t_*].
```

## Proposition — First-exit charge

There are absolute constants `c_*`, `C_*`, and, for each finite `K`, a number `epsilon_K>0` with the following property.

Assume

```math
A_q(s)=2\theta_q,
\qquad
A_q(t_*)=\theta_q,
\qquad
\theta_q\le A_q(t)\le2\theta_q
```

on `I=[s,t_*]`, and

```math
t_*-s\le c_*(\nu\lambda_q^2)^{-1},
\qquad
K_q(I)\le K.
```

Then

```math
\mathcal E_q(I)\ge\epsilon_K.
```

More precisely,

```math
1
\lesssim
K\,\mathcal E_q(I)^{1/2}
+
\mathcal E_q(I).
```

### Proof

Choose `x_s` so that

```math
|u_q(s,x_s)|\ge(2-o(1))\theta_q.
```

Let `X(t)` be the characteristic of the smooth low-mode drift:

```math
\dot X(t)=a_q(t,X(t)),
\qquad
X(s)=x_s.
```

Along the characteristic,

```math
\frac d{dt}u_q(t,X(t))
=
\nu\Delta u_q(t,X(t))+R_q(t,X(t)).
```

Because `|u_q(t_*,X(t_*))|\le A_q(t_*)=theta_q`, the amplitude loss gives, after sending the initial `o(1)` to zero,

```math
\theta_q
\le
\nu\int_I\|\Delta u_q\|_\infty dt
+
\int_I\|R_q\|_\infty dt.
```

The shell remains band-limited and `A_q<=2 theta_q` on `I`, hence

```math
\nu\int_I\|\Delta u_q\|_\infty dt
\lesssim
\nu\lambda_q^2|I|\theta_q.
```

Choose `c_*` so that this term is at most `theta_q/4`. The remainder bound yields

```math
1
\lesssim
K\int_IG_qdt
+
\frac1{\nu\lambda_q}\int_IH_qdt.
```

The energy estimate from the interaction audit gives

```math
\int_IG_qdt
\lesssim
\mathcal E_q(I)^{1/2},
```

where the fixed factor `c_*^{1/2}` is absorbed into the constant. The high–high estimate gives

```math
\frac1{\nu\lambda_q}\int_IH_qdt
\lesssim
\mathcal E_q(I).
```

Combining them proves

```math
1\lesssim K\mathcal E_q(I)^{1/2}+\mathcal E_q(I).
```

For fixed `K`, the right side tends to zero with `mathcal E_q(I)`, so an explicit positive `epsilon_K` follows.

## Corollary — Energy-charge packing

Let `{I_j}` be pairwise disjoint buffered rapid-exit intervals, with shell indices `q_j`, a uniform neighbour ratio `K`, and lengths at most `c_*(nu lambda_{q_j}^2)^{-1}`. Then

```math
\sum_j\lambda_{q_j}^{-1}
\lesssim_K
\nu^{-2}\|u_0\|_2^2.
```

### Proof

The proposition gives

```math
\frac{\lambda_{q_j}}{\nu}
\int_{I_j}\|\nabla u\|_2^2dt
\ge\epsilon_K,
```

or equivalently

```math
\nu\int_{I_j}\|\nabla u\|_2^2dt
\ge
\epsilon_K\nu^2\lambda_{q_j}^{-1}.
```

Sum over disjoint intervals and use the Leray energy inequality.

For an overlapping family, the proposition controls every pairwise disjoint subfamily. Turning that fact into control of the complete family requires an additional scale-aware covering or tree-packing theorem. No weighted Vitali estimate for the full family is asserted here.

## Exact insufficiency of the packing exponent

The packing weight is

```math
\lambda_q^{-1}=2^{-q}.
```

Since

```math
\sum_{q\ge q_0}2^{-q}<\infty,
```

the energy budget can fund one charged rapid exit at every arbitrarily high dyadic level. The corollary therefore does not imply that the dissipation wavenumber is bounded, does not imply parabolic superlevel occupancy, and does not supply the missing half-power in the source envelope.

## Scalar box counterfixture

The insufficiency is exact at the level of the proved scalar constraints.

Let `lambda_q=2^q`. Choose pairwise disjoint parabolic boxes

```math
I_q,
\qquad
|I_q|=c(\nu\lambda_q^2)^{-1},
```

and subintervals `J_q subset I_q` of lengths

```math
|J_q|
=
\frac1{\nu\lambda_q^2q^2}.
```

Set an abstract wavenumber profile

```math
\Lambda(t)=\lambda_q
\quad\text{on }J_q,
```

and assign to each full box the dissipation charge

```math
\mu(I_q)=\epsilon\nu^2\lambda_q^{-1}.
```

Then

```math
\int\Lambda(t)^2dt
=
\nu^{-1}\sum_q\frac1{q^2}<\infty,
```

and

```math
\sum_q\mu(I_q)
=
\epsilon\nu^2\sum_q2^{-q}<\infty.
```

All dyadic levels are nevertheless attained. Moreover, the source upper-envelope cost may diverge:

```math
\sum_q\lambda_q^{5/2}|J_q|
=
\nu^{-1}\sum_q\frac{2^{q/2}}{q^2}
=
\infty.
```

Thus `Lambda in L2`, the energy-charge packing law, and attainment of only short sub-parabolic excursions are mutually compatible in the abstract. This is a counterfixture to an estimate-closing argument, not a Navier–Stokes solution.

## Route disposition

| Route | Disposition | Exact reason |
|---|---|---|
| buffered first-exit inequality | proved | transport removal and fixed-shell regularity suffice |
| local dissipation charge | proved under bounded neighbour ratio | exit forces `mathcal E_q>=epsilon_K` |
| disjoint packing | proved | global energy controls `sum lambda_q^-1` for disjoint exit intervals |
| full overlapping-family packing | open | requires a scale-aware covering or tree theorem |
| use the packing law to bound attained levels | terminated | dyadic weight `lambda_q^-1` is summable |
| use the packing law to close `f in L1` | terminated | scalar box fixture preserves `Lambda in L2` but permits divergent `lambda^(5/2)` cost |
| remove the neighbour-ratio hypothesis by energy | open | energy does not control the threshold cluster uniformly |
| signed flux or cross-scale charge | open | must be stronger than absolute local dissipation packing |

## Strongest surviving dynamic interface

Any continuation of the shell-exit route must produce more than a dimensionless local energy charge. It must identify one of:

1. a signed flux charge with non-summable cross-level cost;
2. an orthogonality or tree-packing law coupling exits at distinct levels;
3. a mechanism forcing actual time occupancy rather than merely charging an enclosing box;
4. a threshold-cluster estimate that removes `K_q(I)` without importing the low-mode regularity criterion.

## WP03 boundary

No numerical lane is authorized by this result. A future WP03 task would require a precise proposed signed-flux or cross-level packing inequality with continuum-uniform constants. Measuring rapid exits or local dissipation alone cannot validate A2.

## Claim boundary

This package proves a buffered first-exit dichotomy and its disjoint energy-charge packing consequence. It also proves that this consequence is insufficient for A2. It does not prove same-threshold persistence, a non-summable packing law, a weighted covering theorem for overlapping exit boxes, the low-mode criterion, or the selected A2 implication.
