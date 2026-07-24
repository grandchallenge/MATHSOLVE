# NS-CI-R014-A2 — Critical dissipation-wavenumber attack ledger

## Status

- Campaign: `NS-CI-001`
- Parent: `NS-CI-WP04`
- Tracker: `MATHSOLVE#24`
- Candidate state: `PROVISIONAL_LEAD_UNPROVED`
- Result state: `SOURCE_ROUTE_RECONSTRUCTED_ELEMENTARY_CLOSURES_REJECTED`

## Candidate statement

Let `u` be a Leray–Hopf solution on `R3` and let `Lambda(t)=lambda_{Q(t)}` be the Cheskidov–Shvydkoy dissipation wavenumber. Determine whether

```math
\Lambda\in L^2(0,T)
\quad\Longrightarrow\quad
I_T(u)=\int_0^T\|u(t)\|_6^4dt<\infty.
```

The source-aligned intermediate target is

```math
\Lambda\in L^2(0,T)
\quad\Longrightarrow\quad
f(t)=\|\omega_{\le Q(t)}(t)\|_{B^0_{\infty,\infty}}\in L^1(0,T).
```

The imported low-mode theorem then gives regularity, and WP02 gives the critical integral and continuation consequences.

## Exact source interface

The source defines

```math
\Lambda(t)
=
\min\{\lambda_q:
\lambda_p^{-1}\|u_p(t)\|_\infty<c_0\nu
\text{ for every }p>q\}.
```

On the active set `Lambda>1`, the threshold shell and Bernstein inequality give, schematically with the energy factor retained,

```math
c\nu\Lambda^2
\le
f(t)
\le
C\Lambda^{5/2}\|u(t)\|_2.
```

Since the Leray energy inequality bounds `||u(t)||_2` uniformly, `Lambda in L5/2_t` implies `f in L1_t`. The same source proves `Lambda in L1_t` for every Leray–Hopf solution.

Under scaling,

```math
\Lambda_\lambda(t)=\lambda\Lambda(\lambda^2t),
\qquad
f_\lambda(t)=\lambda^2 f(\lambda^2t),
```

so both `Lambda in L2_t` and `f in L1_t` are critical.

## Exact obstruction A2-O1 — Source envelope

The source bounds do not imply the candidate. The scalar profile

```math
\Lambda(t)=t^{-9/20},\qquad 0<t<1,
```

satisfies

```math
\Lambda^2=t^{-9/10}\in L^1(0,1),
```

while

```math
\Lambda^{5/2}=t^{-9/8}\notin L^1(0,1).
```

Thus any proof of A2 must improve the source upper envelope or use a different equation-specific route. This is a kinematic obstruction to an estimate, not a Navier–Stokes counterexample.

## Exact obstruction A2-O2 — Low-frequency enstrophy

Let

```math
D_{\le Q}(t)=\|\nabla u_{\le Q(t)}(t)\|_2^2.
```

Bernstein and the energy bound give

```math
D_{\le Q}\le \Lambda^2\|u\|_2^2.
```

Also `D_{<=Q}<=D=||grad u||_2^2`. Therefore

```math
D_{\le Q}^2
\le
\Lambda^2\|u\|_2^2D.
```

The hypotheses supply `Lambda^2 in L1_t`, `D in L1_t`, and `||u||_2 in L-infinity_t`; they do not supply integrability of the product `Lambda^2D`. The scalar fixture `t^(-2/3)*t^(-2/3)` rejects this closure.

Consequently the route

```text
Lambda in L2
  -> low-frequency H1 squared integrable in time
  -> L4_t L6_x
```

fails at the multiplication step.

## Exact obstruction A2-O3 — Direct low-mode coefficient bound

For each `q<=Q`,

```math
\lambda_q\|u_q\|_\infty
\lesssim
\lambda_q^{3/2}\|\nabla u_q\|_2.
```

Hence

```math
f(t)
\lesssim
\Lambda(t)^{3/2}D_{\le Q}(t)^{1/2}.
```

Cauchy–Schwarz requires `Lambda^3 in L1_t`, not merely `Lambda^2 in L1_t`; Young's inequality produces the same cubic requirement. This standard interpolation route does not improve the `5/2` source exponent to `2`.

## Level-set ledger

Let

```math
E_k=\{t:2^k\le\Lambda(t)<2^{k+1}\}.
```

The A2 hypothesis is equivalent up to fixed dyadic constants to

```math
\sum_k2^{2k}|E_k|<\infty.
```

The source upper envelope yields

```math
\int f
\lesssim
\|u_0\|_2
\sum_k2^{5k/2}|E_k|.
```

Therefore a source-compatible proof needs an additional half-power gain. Admissible forms include:

- a packing estimate suppressing high-level occupancy;
- a shell-energy cost per excursion;
- a parabolic dwell-time or threshold-crossing estimate;
- a correlation estimate coupling `f` to the energy dissipation measure;
- a cancellation estimate replacing the absolute Bernstein bound.

Merely renaming the missing factor is not progress.

## Active attack lanes

### A2-L2 — Carleson packing of active boxes

Seek a measure estimate for time-frequency boxes

```text
(t,q) with q near Q(t)
```

that gains `2^{-k/2}` relative to the raw `Lambda^2` level-set sum. Every proposed packing estimate must be derived from a localized energy inequality or the equation.

### A2-L3 — Parabolic excursion cost

A threshold shell satisfies

```math
\|u_Q\|_\infty\gtrsim\nu\Lambda.
```

Bernstein implies a minimum shell `L2` amplitude and a corresponding instantaneous shell-dissipation cost. Determine whether the evolution equation forces that cost to persist over a parabolic interval or controls the number of rapid threshold crossings.

The missing point is temporal control: an instantaneous threshold does not by itself give a duration estimate.

### A2-L4 — Weighted energy measure

Search for a valid estimate of one of the forms

```math
\int\Lambda^2D\,dt
\le
F(\|u_0\|_2,\nu,\|\Lambda\|_{L^2}),
```

or

```math
\int f\,dt
\le
F(\|u_0\|_2,\nu,\|\Lambda\|_{L^2}),
```

using the frequency-localized energy equation. Such an estimate cannot follow from Hölder alone and must identify a sign, flux, cancellation, or monotonicity mechanism.

### A2-L5 — High-mode viscous absorption and direct `I_T`

Split

```math
u=u_{\le Q}+u_{>Q}.
```

The high-mode threshold may allow viscous absorption, but the proof must produce an explicit summable bound on `||u_{>Q}||_6^4`. The low-mode contribution must avoid A2-O2. Record all dyadic sums and constants.

### A2-L6 — Abstract packet adversary

Construct dyadic packets satisfying:

- the threshold-shell definition;
- the Leray energy and dissipation exponents at the scalar level;
- `Lambda in L2_t`;
- failure of each proposed intermediate majorant.

These packets test estimates only. They are not claimed solutions.

## Route status

| Route | Status | Exact reason |
|---|---|---|
| source bound `f<=Lambda^(5/2)||u||2` | terminated | exponent `5/2` not controlled by `L2` |
| low-frequency enstrophy plus Sobolev | terminated | requires product of unrelated `L1` coefficients |
| `f<=Lambda^(3/2)D^(1/2)` plus Hölder | terminated | requires `Lambda in L3` |
| level-set packing | active | exact half-power gain identified, no estimate yet |
| excursion/dwell-time control | active | temporal threshold dynamics not yet derived |
| weighted frequency energy | active | needs new sign, correlation, or cancellation |
| direct high/low `I_T` split | active | both high-mode summability and low-mode product must close |

## Falsification and WP03 boundary

WP03 remains closed for theorem evidence. It may be opened later only to falsify a precise proposed intermediate inequality, such as a claimed uniform packing law or shell-persistence estimate. Numerical boundedness of `Lambda`, `f`, or `I_T` cannot validate A2.

## Current determination

A2 survives initial semantic and scaling review but not because an elementary proof route is available. Three natural closures fail exactly. The candidate remains the provisional lead because it exposes a critical, source-defined half-power gap and a finite list of equation-specific mechanisms that could bridge it.

No Referee selection or novelty claim is made.