# NS-CI-WP04 — Restricted theorem target formulation

## Status

- Campaign: `NS-CI-001`
- Programme tracker: `grandchallenge/MATH-PROGRAMME#61`
- MATHSOLVE tracker: `grandchallenge/MATHSOLVE#22`
- MATHFORGE input: PR `grandchallenge/MATHFORGE#19`, commit `514e44e`
- State: `SHORTLIST_FORMULATED_PROVISIONAL_LEAD_A2`
- Selection limit: at most one target
- Referee selection: not yet made

## Shortlist received

MATHFORGE has terminated the generic geometric-depletion, concentration/sparsity, and symmetry candidates and supplied three exact replacements:

1. `NS-CI-R014-A2` — critical dissipation-wavenumber integrability;
2. `NS-CI-R014-D1` — scale-uniform shell-flux compensation;
3. `NS-CI-R014-E1` — compact-support-to-Schwartz extension bridge.

No novelty is asserted for any candidate.

## Common setting

Fix `nu>0`. Let `u0` be a smooth divergence-free rapidly decreasing vector field on `R3`, and let `u` be a Leray–Hopf solution of the unforced three-dimensional incompressible Navier–Stokes equations. Write

```math
I_T(u)=\int_0^T\|u(t)\|_{L^6(\mathbb R^3)}^4\,dt.
```

Every candidate must preserve this domain, data class, solution class, and quantifier profile unless its restriction is stated explicitly.

---

## Candidate A2 — Critical dissipation-wavenumber criterion

### Proposed theorem statement

Let `Lambda(t)` be the Cheskidov–Shvydkoy dissipation wavenumber associated with `u`, using their fixed Littlewood–Paley decomposition and threshold convention. Prove or disprove:

```math
\Lambda\in L^2(0,T)
\quad\Longrightarrow\quad
I_T(u)<\infty.
```

Equivalently, the scale-invariant quantity

```math
\int_0^T\Lambda(t)^2\,dt
```

would be a sufficient restricted criterion for the critical Ladyzhenskaya–Prodi–Serrin integral.

### Restriction and non-circularity

The hypothesis is a frequency-threshold observable, not the target norm, a uniform `H1` norm, or a stated LPS/Besov regularity assumption. It is stronger than the universal a priori `Lambda in L1_t` information and weaker, on a finite interval, than the established sufficient condition `Lambda in L5/2_t`.

No equivalence between `Lambda in L2_t` and `I_T<infinity` is assumed. Establishing the implication is the open proof obligation.

### Scaling

Under Navier–Stokes scaling,

```math
u_lambda(x,t)=lambda u(lambda x,lambda^2 t),
qquad
Lambda_lambda(t)=lambda Lambda(lambda^2 t).
```

Hence

```math
\int Lambda_lambda(t)^pdt
=
\lambda^{p-2}\int Lambda(s)^pds,
```

so `p=2` is critical. The conclusion `I_T` is also invariant.

### Proof-obligation DAG

```text
A2-D1  Normalize the precise definition and measurability of Lambda
  -> A2-D2  Prove the scaling law with the fixed dyadic convention
  -> A2-L3  Split u=u_{<=Q(t)}+u_{>Q(t)}, Q=log_2 Lambda
  -> A2-L4  Derive a frequency-localized estimate for ||u||_6^4
  -> A2-L5  Obtain an L1_t majorant from Lambda^2 plus Leray energy data
  -> A2-C6  Conclude I_T<infinity
  -> CR-004/CR-007  Apply the WP02 LPS and continuation interfaces
```

`A2-L5` is the decisive missing estimate. The elementary low-frequency bounds only yield products such as

```math
\|u_{\le Q}\|_6^4
\lesssim
\Lambda^2\|u\|_2^2\|\nabla u\|_2^2,
```

and `Lambda^2 in L1_t` together with `||grad u||_2^2 in L1_t` does not by itself make their product integrable. A valid proof therefore needs equation-specific decorrelation, a sharper frequency split, or a new weighted dissipation estimate. Treating the product of two `L1` functions as `L1` would trigger WP01.

### WP01 clearance and attack surface

Cleared syntactically:

- no reversed finite-time inclusion;
- no hidden compact-support restriction;
- no fixed-resolution numerical inference;
- no imported formal premise presented as proof.

Active adversarial risks:

- covert conversion of `Lambda in L2` into an already-known LPS/Besov criterion;
- hidden `L-infinity_t H1_x` control;
- multiplication of two merely `L1_t` quantities;
- nonuniform constants in the time-dependent frequency split.

### Falsification protocol

A counterexample to the implication would require a Leray–Hopf solution with `Lambda in L2_t` but divergent `I_T`; no such continuum solution is presently available. Before continuum falsification, test the candidate estimate algebraically against admissible scalar time profiles and frequency packets to expose any invalid closure step. Numerical trajectories may reject a proposed intermediate inequality but cannot establish or refute the continuum theorem.

### Formalization boundary

MATHCERT can formalize exponent scaling, interval rescaling, implication structure, and scalar counterfixtures. The definition and analytic properties of the dissipation wavenumber and the decisive frequency estimate remain imported PDE interfaces.

---

## Candidate D1 — Uniform shell-flux compensation

### Current theorem shape

Let `u^N=P_{<=N}u` and

```math
\Pi_N(t)
=
\left\langle P_{\le N}((u\cdot\nabla)u),-\Delta u^N\right\rangle.
```

The desired compensated interface is: there exist `theta<1` and `a in L1(0,T)`, independent of `N`, such that

```math
\Pi_N(t)
\le
\theta\nu\|\Delta u^N\|_2^2
+a(t)\|\nabla u^N\|_2^2
```

for almost every `t` and every cutoff `N`.

### Admission defect

The displayed inequality cannot itself serve as the added hypothesis: it already packages the exact Grönwall closure. A theorem-grade candidate must state an independently checkable shell-transfer, commutator, sign, cancellation, or locality condition `H_D(u)` and prove

```text
H_D(u) -> uniform compensated interface.
```

Until `H_D` is explicit, D1 is a mechanism interface rather than an admissible theorem statement.

### Proof-obligation DAG

```text
D1-D1  Define an independent shell-transfer observable H_D
  -> D1-L2  Prove H_D is scaling-compatible and not equivalent to H1/LPS control
  -> D1-L3  Derive a commutator or flux decomposition of Pi_N
  -> D1-L4  Obtain theta<1 and a in L1 uniformly in N
  -> D1-C5  Uniform Gronwall bound for ||grad u^N||_2
  -> D1-L6  Compactness and passage N->infinity
  -> CR-005/CR-007  WP02 continuation route
```

### Hard rejection tests

Reject D1 if:

- `a(t)` is defined using `||u(t)||_6^4` or another equivalent continuation coefficient;
- `H_D` is the compensated inequality under another name;
- constants grow with `N`;
- the passage to the continuum uses only bounded finite-dimensional trajectories;
- pressure or commutator cancellation is asserted without the exact projection identities.

### Formalization boundary

The implication from the compensated differential inequality to the uniform Grönwall bound is formalizable. The commutator decomposition and continuum limit remain analytic interfaces.

---

## Candidate E1 — Uniform compact-support extension bridge

### Proposed bridge theorem

Let `u0` be a fixed Schwartz divergence-free datum. Let `u0,n in C_c^infinity(R3)` be divergence-free with

```math
u_{0,n}\to u_0
```

strongly in `L2` and in an explicitly selected local-strong-theory topology. Suppose each datum generates a global strong solution `u_n` and, for every finite `T`,

```math
\sup_n\int_0^T\|u_n(t)\|_6^4dt<\infty.
```

Then a subsequence converges to a Leray–Hopf solution `u` with datum `u0`, lower semicontinuity gives `I_T(u)<infinity`, the operational LPS theorem makes `u` strong on `(0,T]`, and weak–strong uniqueness identifies every Leray–Hopf solution from `u0` with `u`. Thus every such solution has finite `I_T`.

### Nature of the result

E1 is a bridge theorem, not a regularity mechanism. Its conclusion is useful only when the compact-support estimates are uniform along approximation of the fixed Schwartz datum. Pointwise finiteness for each approximant is insufficient.

### Proof-obligation DAG

```text
E1-D1  Construct divergence-free compactly supported approximants
  -> E1-L2  Uniform energy bounds from strong convergence of initial data
  -> E1-L3  Local compactness and passage through the nonlinear term
  -> E1-L4  Recover initial trace and Leray energy inequality
  -> E1-L5  Weak lower semicontinuity in L4_tL6_x
  -> CR-004  LPS regularity of one limit solution
  -> CR-006  Weak-strong uniqueness identifies every Leray-Hopf solution
```

### Main risks

- the chosen approximation topology may be too weak for the required strong solution interface;
- global strong existence of each approximant is itself conditional;
- a uniform critical bound may encode the original theorem;
- whole-space compactness must be sufficient to pass the nonlinear term and initial trace;
- universal identification requires the exact WP02 weak–strong theorem, not uniqueness in an unrelated class.

### Formalization boundary

The quantifier and implication skeleton is highly formalizable. Whole-space compactness, lower semicontinuity, and weak–strong uniqueness remain imported analytic interfaces with provenance.

---

## Preliminary Council scorecard

Scores are 0–5. Higher is better except execution cost, where 0 is lowest cost and 5 is highest cost.

| Dimension | A2 | D1 | E1 |
|---|---:|---:|---:|
| leverage | 5 | 4 | 3 |
| non-circularity | 4 | 1 | 4 |
| prior-art distance | 3 | 3 | 2 |
| scale compatibility | 5 | 4 | 3 |
| proof tractability | 2 | 2 | 4 |
| formalizability | 4 | 3 | 4 |
| falsifiability | 4 | 4 | 3 |
| full-problem relevance | 5 | 4 | 4 |
| information value if false | 5 | 4 | 3 |
| execution cost | 3 | 4 | 2 |

### Rationale

- **A2** has the highest leverage and cleanest critical scaling. Its central obstruction is explicit rather than hidden: convert `Lambda^2` control into an integrable critical coefficient without multiplying unrelated `L1` quantities.
- **D1** targets the exact cutoff pathology exposed by WP01, but it is not yet theorem-grade because the independent hypothesis `H_D` is missing.
- **E1** is the most tractable and cleanest bridge, but the uniform compact-support bound carries nearly all substantive regularity content and the result is likely close to standard compactness plus weak–strong uniqueness.

## Provisional recommendation

`NS-CI-R014-A2` is the **provisional leading candidate** for `NS-CI-R014` because it is scaling-critical, source-anchored, independently stated, and exposes a precise missing estimate. This is not Referee selection.

Before promotion:

1. MATHCERT must verify the scaling and statement boundary.
2. Prospector must confirm that no exact `Lambda in L2_t` criterion already exists.
3. Adversary must test whether A2 collapses to a known Besov/LPS condition or a WP01 failure.
4. Verifier must either produce a plausible route through `A2-L5` or record an exact no-go obstruction.
5. Referee must compare A2 against the tractable E1 bridge and the incomplete D1 interface.

## Current decision

No target is selected. A2 leads provisionally; D1 remains under formulation debt; E1 remains a bridge-theorem fallback.