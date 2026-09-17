# NS-CI-R014-A2-L5-10 — Field calibration and frequency--scale successor handoff

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected predecessor at tranche start: `7d72d4f8aec2019a8eefb4db4fe151e4f14b1211`
- Predecessor disposition: `PI1_CRITICAL_H12_ROUTE_REDUCED_TO_SUPERLINEAR_RICCATI__GLOBAL_CRITICAL_TRANSFER_HAS_NO_SIGN`
- A2 theorem: open
- L5: active
- MATHCERT adjudication: absent
- Purpose of this package: preserve the post-L5-9 research frontier in a form an independent agent can execute without reconstructing the campaign from conversation history.

This package is a governed continuation plan plus one proved reduction. It is not a proof of A2, not a literature novelty claim, and not a certification artifact.

## 1. Exact target and current mathematical frontier

The selected theorem remains the unforced whole-space criterion

```math
Lambda in L^2(0,T)
    ->
I_T(u)=integral_0^T ||u(t)||_6^4 dt < infinity
```

for a three-dimensional Leray--Hopf Navier--Stokes solution in the target data class and with the fixed Cheskidov--Shvydkoy dissipation-wavenumber convention.

The established low-mode regularity interface uses

```math
f(t)=sup_{q<=Q(t)} lambda_q ||u_q(t)||_infinity,
qquad Lambda(t)=lambda_{Q(t)},
```

and it is enough to prove `f in L^1_t`.

L5-8 introduced

```math
S_1(t)=sum_{q<=Q(t)} ||u_q(t)||_infinity^2
```

and proved the pointwise bridge

```math
f(t)^2 <= C Lambda(t)^2 S_1(t).
```

A global dimensionally normalized `PI_1^*` estimate would imply the target, but L5-8 separated that global estimate from the static A2/Leray budgets. L5-9 then showed that the straight global critical `H^(1/2)` energy route reduces to a superlinear Riccati comparison and that the complete critical nonlinear transfer has no universal sign.

The live frontier is therefore not another global interpolation. It is active-set-specific depletion, anti-concentration, or frequency/physical-scale coherence.

## 2. New proved reduction: only the high-Lambda packet tail is needed

A full global `PI_1^*` estimate is stronger than A2 needs.

For every fixed finite `R>=1`, split time into

```math
E_low(R)={t: Lambda(t)<=R},
qquad
E_high(R)={t: Lambda(t)>R}.
```

The source envelope already gives, schematically with the conserved energy factor retained,

```math
f(t) <= C U_0 Lambda(t)^(5/2).
```

On `E_low(R)`,

```math
Lambda^(5/2) <= R^(1/2) Lambda^2,
```

hence

```math
integral_{E_low(R)} f(t) dt
<= C U_0 R^(1/2) integral_0^T Lambda(t)^2 dt
< infinity.
```

Thus bounded-dissipation-wavenumber times are automatically harmless under A2.

On `E_high(R)`, the L5-8 pointwise bridge gives

```math
f^2 <= C Lambda^2 S_1.
```

Therefore Cauchy--Schwarz yields

```math
integral_{E_high(R)} f(t) dt
<= C
   (integral_{E_high(R)} Lambda(t)^2 dt)^(1/2)
   (integral_{E_high(R)} S_1(t) dt)^(1/2).
```

Consequently the following strictly weaker successor is sufficient:

```text
HIGH-LAMBDA PACKET TAIL TARGET

There exists a finite R such that

integral_{ {Lambda>R} } S_1(t) dt < infinity.
```

No universal quantitative `PI_1^*` constant is required. No estimate on the full time interval is required beyond what A2 already supplies on `{Lambda<=R}`.

This reduction should be treated as the default successor target unless a still weaker equivalent closure is found.

## 3. Recent field development A: September 2026 forced blow-up construction

### Primary source

OpenAI, *Finite Time Blowup for Navier--Stokes*, released 8 September 2026.

- announcement: `https://openai.com/index/navier-stokes-solution/`
- paper: `https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf`

Theorem 1.1 constructs, for every positive viscosity, a smooth solution on `[0,1)` with zero initial velocity and a smooth compactly supported external force, uniformly bounded kinetic energy, and unbounded velocity as `t -> 1`.

### Governance/claim boundary

This is a **forced** solution. The selected A2 theorem is presently an **unforced** Leray--Hopf criterion. Therefore:

```text
THE OPENAI CONSTRUCTION CANNOT DIRECTLY FALSIFY A2.
```

It is a calibration object for singularity mechanics, frequency thresholds, packet concentration, and sharpness heuristics. A direct counterexample claim would require an unforced solution in the exact A2 class, or a separately proved force-insensitive extension of A2. Neither is available here.

### Published similarity scales worth calibrating

Writing `tau=1-t`, the paper gives the leading inner-core scales

```math
ell_r ~ tau^(1/2),
ell_z ~ tau^(1/2-h),
0<h<1/100,
```

with characteristic angular/axial velocity

```math
|u_theta|, |u_z| ~ tau^(-1/2-h),
```

and radial velocity `O(tau^(-1/2))`.

Thus the core radial wavenumber scale is

```math
lambda_core ~ ell_r^(-1) ~ tau^(-1/2),
```

and the angular Reynolds ratio at that scale behaves as

```math
|u_theta|/(nu lambda_core) ~ tau^(-h) -> infinity.
```

If an exact Littlewood--Paley lower bound shows that a core-scale shell carries a fixed fraction of this angular velocity, then the strict-high inequality

```math
||u_p||_infinity < c_0 nu lambda_p
```

cannot hold on that shell for late times. Such a result would force the dissipation wavenumber to stay at or above the core scale:

```math
Lambda(t) >= c lambda_core(t) ~ c tau^(-1/2).
```

That would imply the logarithmic lower divergence

```math
integral Lambda(t)^2 dt
>= c integral tau^(-1) d tau
= infinity.
```

This is currently a **calibration conjecture**, not a proved property of the construction. The missing step is an exact dyadic lower bound compatible with the campaign's fixed Littlewood--Paley convention and with all correction/pulse terms in the constructed velocity.

### Calibration work package C1

An independent agent should test, in order:

1. Identify the exact leading velocity formula and correction hierarchy in the released paper.
2. Fix the same Littlewood--Paley decomposition used by A2, or prove robustness under equivalent smooth dyadic partitions.
3. Establish a lower bound for at least one shell `p(t)` with `lambda_p ~ tau^(-1/2)`:

   ```math
   ||u_p(t)||_infinity >= c tau^(-1/2-h)
   ```

   on a sequence or terminal interval with uniform `c>0`.
4. Control cancellation from the oscillatory correction terms at that shell. Do not infer a shell lower bound from the pointwise velocity scale without this step.
5. Deduce whether the strict-high threshold fails at `p(t)` and hence whether `Q(t)>=p(t)-O(1)`.
6. Compute the resulting lower/upper asymptotics for `Lambda`, `f`, `S_1`, `W_{<=Q}`, and `Z_{>Q}`.

**Success condition C1:** a theorem-grade asymptotic bound for one or more campaign observables on the explicit forced singular solution.

**Failure condition C1:** the correction hierarchy prevents a uniform shell lower bound, or the campaign's threshold observable is not stable enough under the construction. Record the exact failure; do not replace it with similarity-scale intuition.

Even a successful C1 result is calibration evidence only unless the forced/unforced boundary is separately crossed by theorem.

## 4. Recent field development B: Cheskidov--Peng intermittency/determining-wavenumber framework

### Primary source

Alexey Cheskidov and Qirui Peng, *An optimal upper bound on the determining wavenumber for 3D Navier-Stokes Equations*, Nonlinear Differential Equations and Applications 33, 92 (2026), published 2 June 2026.

- DOI: `10.1007/s00030-026-01232-0`
- source: `https://link.springer.com/article/10.1007/s00030-026-01232-0`

Their intermittency dimension is defined through averaged saturation of Bernstein-type estimates over active shells. In the `r=infinity` specialization, its weighted active-shell quantity is structurally aligned with the campaign's

```math
S_D(t)=sum_{q<=Q(t)} lambda_q^(D-1)||u_q(t)||_infinity^2.
```

This is why L5-8's `D=1` endpoint is not an arbitrary packet quantity.

### Important boundary

Their theorem concerns averaged determining wavenumbers and intermittency in a periodic/forced turbulence framework. It does **not** prove

```text
Lambda in L2_t -> PI_1^*
```

for the selected whole-space unforced A2 problem.

Use the paper to import definitions, exact Bernstein-saturation weights, and proof mechanisms only after checking domain/forcing/averaging hypotheses. Do not import its conclusions as A2 evidence.

### Intermittency work package C2

The preferred target is no longer a global dimension statement. It is the high-Lambda tail estimate

```math
integral_{Lambda>R} S_1(t) dt < infinity.
```

Test whether high-`Lambda` times force enough effective Bernstein non-saturation to make this tail finite. Concretely:

1. Rewrite the Cheskidov--Peng active-range intermittency definition at `r=infinity` and `D=1` in campaign notation.
2. Remove periodic-domain dimensional constants and identify the correct whole-space, scale-covariant substitute, retaining `lambda_E=(nu/U_0)^2` when needed.
3. Localize the definition to the high-`Lambda` time set rather than averaging over all times.
4. Determine whether the NSE energy/flux identities imply a lower bound on effective intermittency dimension, or directly a bound on the time integral of `S_1`, when `Lambda` is large.
5. Falsify every proposed implication against the existing static packet fixtures before investing in PDE closure.

**Success condition C2:** a PDE-derived high-`Lambda` packet tail theorem, or a weaker estimate that makes `integral f` finite.

**Failure condition C2:** the argument only restates a Bernstein-saturation assumption, recreates global `PI_1^*`, or needs a product of unrelated `L1_t` quantities.

## 5. Recent field development C: frequency--scale matching

### Primary source

Maotuo Guo, Wendong Wang, and Shiyang Xiong, *A Critical Chemin--Lerner Regularity Criterion via One Velocity Component for the Three-Dimensional Navier--Stokes Equations*, arXiv:2609.03877v1, submitted 3 September 2026.

- source: `https://arxiv.org/abs/2609.03877`
- arXiv identifier: `2609.03877`

The principal mechanism is frequency--scale matching inside a local energy inequality. Dyadic blocks are retained until paired with a physical backward scale. The authors obtain summability from three different mechanisms:

- low frequencies: gain from physical slab thickness;
- high frequencies: transfer of the projection to localized flux plus inverse Bernstein gain;
- separated pressure sources: harmonic decay.

These contributions produce a two-sided `ell^1` kernel linking frequency index to physical observation scale.

### Why this is new relative to closed L5 routes

The campaign's standard direct-L6 commutator route failed because kernel cancellation `lambda_p^-1` and the derivative on a high shell `lambda_p` canceled, leaving a scale-neutral low deformation coefficient. That failure occurred after choosing a global/fixed frequency decomposition and estimating absolute values.

Frequency--scale matching introduces an **independent physical scale** before summing. A gain depending on the difference between frequency index and physical-cylinder index is therefore not ruled out by the existing scale-neutral commutator termination.

This is a genuinely distinct route provided the agent does not collapse the two indices prematurely.

### Main analytic work package C3

The preferred successor after calibration is a localized active-scale estimate.

Let a candidate singular time be `T`, choose a backward physical scale `r_k ~ 2^{-k}`, and retain dyadic shell `q` separately. The goal is to derive a kernel `K(q-k)` with

```math
sum_n K(n) < infinity
```

and an inequality that controls high-`Lambda` packet mass or the low-mode coefficient on the corresponding backward cylinder.

The agent should attempt the following decomposition before absolute summation:

1. Local kinetic-energy inequality on a backward parabolic cylinder with radius comparable to `lambda_k^-1`.
2. Dyadic decomposition of transport and pressure while retaining `(q,k)` as separate indices.
3. `q << k`: extract geometric gain from the physical cutoff/slab thickness.
4. `q >> k`: move the projection/derivative onto the localized factor where possible and seek inverse-Bernstein or cancellation gain.
5. Pressure: separate local, near, and far sources; test harmonic decay for far spatial annuli before dyadic summation.
6. Sum only after establishing a two-sided kernel in `q-k`.
7. Bind `k` to the active scale only at the final stage, for example `k=Q(t)` or over level sets `Q(t)~k`.

The minimum useful output is not a full regularity theorem. It is any bound of the form

```math
integral_{Lambda>R} S_1(t) dt
<= finite expression controlled by A2/Leray data,
```

or

```math
integral_{Lambda>R} f(t) dt < infinity,
```

without assuming the conclusion.

**Hard rejection tests C3:**

- if `q` is set equal to `k` before the local-energy gains are derived, reject the route as collapsed;
- if the high-frequency estimate returns only the already-closed `G_Q`, `S_Q`, or `Lambda^2 X^(3/2)` coefficient, record the exact reduction and stop that variant;
- if a selector derivative `d 1_{Q=q}` is introduced, the argument has re-entered B4 and must satisfy its reopening conditions;
- if the pressure term is estimated globally by a scale-neutral Calderon--Zygmund bound before spatial separation, the field-development mechanism has not actually been used;
- if constants depend on a terminal frequency cutoff, reject the estimate.

**Success condition C3:** a summable frequency/physical-scale kernel yielding a new quantitative gain on the high-`Lambda` active set.

## 6. Terminal-local formulation is sufficient and should be preferred

A2 is a continuation criterion. A successor need not prove a global packet inequality with a polished universal constant if a putative singular time `T` can be excluded by a backward-local estimate.

A useful target is therefore:

```text
For every putative singular time T, there exist R<infinity and delta>0 such that

integral_{(T-delta,T) intersect {Lambda>R}} S_1(t) dt < infinity.
```

Combined with the low-`Lambda` source envelope and the A2 assumption, this gives `f in L1(T-delta,T)`, which is the part needed for continuation.

This terminal-tail formulation should be tested before attempting a global-in-time `PI_1^*` theorem. It is weaker and better matched to local-energy/frequency--scale methods.

## 7. Prioritized independent-agent execution order

### Priority 0 — Rebind exact state

Before mutation, fetch protected `MATHSOLVE/main`, read this file and `handoffs/NS-CI-001/README.md`, and verify that the protected NS predecessor containing L5-9 remains in ancestry. If unrelated main drift occurred, rebind; do not treat unrelated movement as a mathematical invalidation.

### Priority 1 — Prove and protect the high-Lambda tail reduction

The reduction in Section 2 should be encoded with a focused algebraic regression test and reflected in the handoff. It is elementary but strategically important because it changes the target from global `PI_1^*` to high-`Lambda` tail finiteness.

### Priority 2 — Execute forced-blow-up calibration C1

This is the most bounded and falsifiable new-field task. Do not claim it falsifies A2. The first theorem-grade target is the dyadic shell lower bound at `lambda ~ tau^-1/2`.

If that lower bound succeeds, compute the exact dissipation-wavenumber asymptotics and packet observables of the construction.

### Priority 3 — Launch frequency--scale matching C3

Use the Guo--Wang--Xiong mechanism as a template, not as an imported theorem. Derive a two-index `(q,k)` local-energy/pressure estimate and seek a summable kernel before setting `k=Q`.

### Priority 4 — Relate successful C3 estimates to C2 intermittency language

If the two-index estimate implies active-shell Bernstein non-saturation, express it in the Cheskidov--Peng `D` language. Do not lead with an assumed intermittency dimension.

## 8. What not to repeat

The following lanes are already characterized or closed as bounded families:

- source envelope alone (`5/2` exponent gap);
- multiplying unrelated `L1_t` quantities;
- static packet interpolation;
- excursion bookkeeping without a PDE residence/coherence theorem;
- L4 positive weighted-column / active diagonal;
- moving low enstrophy without an actual selector-variation theorem;
- moving-tail H1 energy;
- fixed-tail bad-set splitting;
- threshold-residence Duhamel without new residence input;
- standard direct-L6 absolute commutator estimates;
- pure signed high-pass/Leray projection-pressure algebra;
- straight global critical `H^(1/2)` energy closure;
- universal sign of the complete critical nonlinear transfer.

A new argument may touch one of these objects, but it must introduce a protected reopening mechanism rather than relabeling the same obstruction.

## 9. Evidence standard for the next tranche

Every claimed advance must distinguish among:

1. exact algebraic theorem;
2. PDE theorem for the selected unforced A2 class;
3. theorem for a different domain/forcing class used only as structural guidance;
4. calibration on the explicit forced singular construction;
5. static or Fourier fixture used only to falsify a proposed estimate;
6. heuristic scaling observation.

Do not promote categories 3--6 into category 2.

For a protected mathematical mutation:

- bind to exact branch head;
- add focused executable tests for algebraic/exponent claims where feasible;
- run independent Adversary and Referee reviews on the final immutable head;
- require hosted CI to execute the new test shard;
- reject stale evidence after any mutation or base drift;
- merge only under the live ruleset with expected-head protection;
- require fresh exact-merge replay;
- update `MATHSOLVE#59` and the programme navigation tracker only after the protected replay closes.

## 10. Decision tree

```text
START
  |
  |-- prove high-Lambda tail reduction (Section 2)
  |
  |-- C1: explicit forced blow-up calibration
  |      |
  |      |-- dyadic core-shell lower bound succeeds
  |      |       -> compute Lambda/f/S1/W/Z asymptotics
  |      |       -> use result to calibrate sharpness only
  |      |
  |      `-- shell lower bound fails
  |              -> record exact cancellation/correction obstruction
  |
  |-- C3: frequency--scale matching
  |      |
  |      |-- summable q-k kernel obtained
  |      |       -> bind physical scale to active Q/level sets
  |      |       -> target high-Lambda S1 tail or f tail
  |      |
  |      `-- collapses to G_Q/S_Q/Riccati/B4
  |              -> terminate that variant exactly
  |
  `-- C2: express any successful depletion in intermittency language
         -> test whether D>=1 is consequence or only interpretation
```

## 11. Claim boundary

A2 remains unproved. The September 2026 blow-up construction is forced and does not directly settle A2. `PI_1^*` remains unproved for selected unforced Navier--Stokes trajectories. The high-`Lambda` packet-tail condition is proved here only as a **sufficient successor target**, not as a consequence of A2. Frequency--scale matching and intermittency are research mechanisms to test, not imported results for this campaign. No MATHCERT certification, novelty, priority, or publication claim is asserted.
