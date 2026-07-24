# NS-CI-R014-A2 — Parabolic superlevel persistence reduction

## Status

- Campaign: `NS-CI-001`
- Selected target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#24`
- Result type: strict conditional reduction
- Result state: `LEMMA_PROVED / PDE PERSISTENCE INTERFACE OPEN`
- Claim boundary: this does not prove A2

## 1. Purpose

The A2 hypothesis

```math
\Lambda\in L^2(0,T)
```

permits unbounded measurable profiles with very short high-frequency excursions. The missing PDE question is therefore temporal: can the Navier–Stokes dissipation wavenumber cross arbitrarily high dyadic levels without spending a parabolic amount of time near those levels?

This note isolates an exact sufficient interface. If high dissipation-wavenumber excursions have uniform parabolic persistence, then A2 follows by a layer-cake argument.

## 2. Abstract setting

Let

```math
\Lambda:(0,T)\to[0,\infty]
```

be measurable. For each integer `k`, define the dyadic superlevel set

```math
M_k:=\{t\in(0,T):\Lambda(t)\ge 2^k\},
\qquad
m_k:=|M_k|.
```

### Parabolic superlevel persistence hypothesis

There exist `c_p>0` and an integer `k_0` such that, for every `k>=k_0`,

```math
m_{k+1}>0
\quad\Longrightarrow\quad
m_k\ge c_p2^{-2k}.
```

The scale `2^{-2k}` is the parabolic time scale corresponding to frequency `2^k`. The hypothesis is scale-compatible: under Navier–Stokes rescaling, frequency is multiplied by `lambda` and time by `lambda^{-2}`.

## 3. Dyadic layer-cake lemma

### Lemma A2-P1

Assume the parabolic superlevel persistence hypothesis. If

```math
\int_0^T\Lambda(t)^2dt<\infty,
```

then `Lambda` is essentially bounded on `(0,T)`.

More quantitatively, writing

```math
L_2^2:=\int_0^T\Lambda(t)^2dt,
```

one may take the crude bound

```math
\operatorname*{ess\,sup}_{(0,T)}\Lambda
\le
2^{k_0+2+4L_2^2/(3c_p)}.
```

### Proof

The layer-cake formula gives

```math
\int_0^T\Lambda(t)^2dt
=
2\int_0^\infty r\,|\{t:\Lambda(t)>r\}|\,dr.
```

For any integer `k`, and every

```math
r\in[2^{k-1},2^k),
```

one has

```math
M_k\subseteq\{t:\Lambda(t)>r\}.
```

Therefore

```math
\begin{aligned}
\int_{2^{k-1}}^{2^k}
2r\,|\{\Lambda>r\}|\,dr
&\ge
m_k\int_{2^{k-1}}^{2^k}2r\,dr\\
&=
\left(2^{2k}-2^{2k-2}\right)m_k\\
&=
\frac34\,2^{2k}m_k.
\end{aligned}
```

Suppose the essential supremum of `Lambda` is infinite. Then `m_{k+1}>0` for every sufficiently large `k`. The persistence hypothesis yields

```math
2^{2k}m_k\ge c_p.
```

Each disjoint dyadic `r`-interval then contributes at least `3c_p/4` to the layer-cake integral. Summing over infinitely many `k` forces

```math
\int_0^T\Lambda(t)^2dt=\infty,
```

contradicting the hypothesis. Hence `Lambda` is essentially bounded.

For the quantitative estimate, if the essential supremum exceeds `2^{K+1}`, then `m_{k+1}>0` for every `k_0<=k<=K`, and hence

```math
L_2^2
\ge
\frac{3c_p}{4}(K-k_0+1).
```

Solving for `K` and enlarging by two dyadic levels gives the displayed bound. `square`

## 4. Excursion formulation

The following stronger but more directly mechanistic interface implies the superlevel hypothesis.

### Parabolic excursion property

There exist `c_e>0` and `k_0` such that whenever

```math
\Lambda(t_*)\ge2^{k+1},
\qquad k\ge k_0,
```

in the essential sense, there is a measurable interval or time set `J_k` with

```math
|J_k|\ge c_e2^{-2k}
```

on which

```math
\Lambda(t)\ge2^k
```

for almost every `t in J_k`.

Then `m_k>=c_e2^{-2k}` whenever level `2^{k+1}` is reached, so Lemma A2-P1 applies.

No disjointness of the excursion intervals is required. The proof sums over disjoint frequency layers in the layer-cake variable, not over time intervals.

## 5. Navier–Stokes corollary

### Corollary A2-P2

Let `u` be a Leray–Hopf solution in the whole-space setting of `NS-CI-001`, and let `Lambda` be the Cheskidov–Shvydkoy dissipation wavenumber. Assume:

1. `Lambda in L^2(0,T)`;
2. `Lambda` satisfies the parabolic superlevel persistence hypothesis.

Then

```math
\int_0^T\|u(t)\|_{L^6(\mathbb R^3)}^4dt<\infty.
```

### Proof

Lemma A2-P1 gives

```math
\Lambda\in L^\infty(0,T).
```

The audited source interface gives, with the Leray energy bound absorbed into the constant,

```math
f(t)
=
\|\omega_{\le Q(t)}(t)\|_{B^0_{\infty,\infty}}
\le
C\left(1+\Lambda(t)^{5/2}\right).
```

Hence `f in L^1(0,T)`. The imported low-mode regularity theorem yields regularity on `(0,T]`; the WP02 LPS and continuation ledger then gives the finite critical integral. `square`

## 6. What remains open

The abstract lemma is exact. The unresolved Navier–Stokes interface is:

> Derive parabolic superlevel persistence, or a weaker layer-cake condition with the same consequence, from the frequency-localized evolution equation and the dissipation-wavenumber threshold.

At a threshold time with `Lambda=lambda_Q>1`, minimality gives schematically

```math
\|u_Q\|_\infty\gtrsim\nu\Lambda.
```

Bernstein then gives a minimum shell `L^2` amplitude and instantaneous dissipation cost. This is not yet a persistence estimate. One must control how rapidly the threshold shell can appear or disappear under the nonlinear evolution.

Admissible PDE routes include:

- temporal modulus estimates for the threshold shell;
- a lower bound on threshold-crossing duration;
- an energy cost for rapid crossings;
- a bound on the number of high-level upcrossings;
- a Carleson packing estimate for active time-frequency boxes.

Any route must preserve the physical time scale, account for low-mode forcing, and avoid assuming the regularity it seeks to prove.

## 7. Adversarial boundary

The persistence hypothesis must not be presented as automatic. In particular:

- measurability or continuity alone does not provide a uniform `2^{-2k}` dwell time;
- a level-dependent constant tending to zero can destroy the layer-cake divergence;
- evidence from a finite numerical trajectory cannot establish continuum persistence;
- an interval on which a Galerkin dissipation wavenumber persists is not a resolution-uniform continuum statement;
- assuming a parabolic modulus derived from uniform `H^1` or stronger regularity is circular.

## 8. Research disposition

A2-P1 is the first proved narrower lemma under the selected A2 target. It converts the excursion lane into a precise PDE obligation:

```text
unbounded Lambda
  -> parabolic superlevel persistence
  -> divergence of integral Lambda^2
```

Thus, under `Lambda in L^2`, any hypothetical failure of A2 must involve increasingly high dissipation-wavenumber excursions whose superlevel occupancy is strictly sub-parabolic.

This conclusion narrows the mechanism search but does not resolve A2.