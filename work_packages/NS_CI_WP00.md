# MS-NS-CI-WP00 — Critical-integrability theorem spine

## Identity

- Parent programme tracker: `grandchallenge/MATH-PROGRAMME#55`
- MATHSOLVE issue: `#18`
- Campaign: `NS-CI-001`
- Owning pillar: MATHSOLVE
- State: initialized; imported theorem chain not yet audited

## Result-status box

| Field | Value |
|---|---|
| Result status | `OPEN / WORK PACKAGE INITIALIZED` |
| Strongest supported local result | Energy plus Sobolev yields `u∈L²_tL⁶_x`; the target `L⁴_tL⁶_x` norm is scaling-critical |
| Not claimed | Universal critical integrability, global regularity, a new regularity criterion, or a novel reduction |
| First executable step | Reconstruct the `(4,6)` conditional regularity proof and continuation bridge with exact hypotheses |

## Problem

For smooth compactly supported divergence-free initial data on `ℝ³`, determine whether every Leray–Hopf solution satisfies

```math
I_T(u):=∫₀ᵀ ‖u(t)‖_{L⁶(ℝ³)}⁴dt<∞
```

for every finite `T>0`.

## Tactical posture

MATHSOLVE must not treat the classical conditional criterion as though the criterion were already known to hold. The immediate task is to expose the proof mechanism consuming `I_T(u)`, identify the precise estimate that remains unavailable, and select restricted targets only after source reconciliation.

## Theorem spine

```text
MS-NS-CI-D000  Fixed equation, domain, data, and solution classes
MS-NS-CI-L001  Leray-Hopf energy inequality                 [import]
MS-NS-CI-L002  Sobolev H1 -> L6                            [local]
MS-NS-CI-C003  u in L2_t L6_x                              [derived]
MS-NS-CI-O004  energy space does not imply L4_t L6_x       [obstruction]
MS-NS-CI-L005  mixed-norm scaling                          [local]
MS-NS-CI-C006  I_T is critical                             [derived]
MS-NS-CI-L007  LPS regularity at (q,p)=(4,6)               [import]
MS-NS-CI-L008  weak-strong uniqueness                      [import]
MS-NS-CI-L009  local strong existence / maximal-time gate  [import]
MS-NS-CI-B010  critical-integral continuation bridge       [to prove]
MS-NS-CI-T011  universal critical-integrability target     [open]
MS-NS-CI-R012  first restricted theorem target             [unselected]
```

## WP00 tasks

### S0 — theorem normalization

Consume the reviewed MATHFORGE source ledger. For each imported theorem, record:

- exact domain and forcing convention;
- data and solution class;
- mixed-norm order and endpoint convention;
- regularity or uniqueness conclusion;
- approximation/density assumptions;
- theorem location and notation translation.

### S1 — quantitative `(4,6)` proof reconstruction

Reconstruct the conditional estimate at enough resolution to answer:

1. Which equation is tested: the equation for `u`, a derivative, the Stokes operator, or a difference of solutions?
2. Which nonlinear trilinear term is bounded?
3. Which Hölder and Sobolev exponents produce `‖u‖₆⁴`?
4. Which strong norm obeys the resulting differential inequality?
5. What Grönwall coefficient is integrated?
6. Which pressure and boundary terms vanish or require estimates?
7. How is the weak solution upgraded or identified with a strong solution?

The output must be an executable proof plan, not the phrase “by the Serrin criterion.”

### S2 — continuation correspondence

Write the implication chain with every hypothesis:

```text
universal I_T finiteness
  -> conditional regularity on each finite interval
  -> weak-strong agreement
  -> no finite maximal strong-solution time
  -> global smoothness in the selected R3 formulation.
```

Audit the reverse direction before retaining the word `equivalent`.

### S3 — negative route ledger

Terminate or restrict any route relying only on:

- the energy-space membership;
- finite-time `L^p` inclusion in the wrong direction;
- a uniform `H¹` bound not already proved;
- a Galerkin cutoff with constants depending badly on cutoff;
- an estimate that becomes weaker at smaller scales;
- a hypothesis that already implies regularity by a known theorem.

Each terminated route must include the smallest exact failure and the nearest viable restricted problem.

### S4 — restricted-target matrix

Score candidates from 0–4 on:

- leverage toward `MS-NS-CI-T011`;
- source novelty risk;
- non-circularity;
- scaling compatibility;
- analytic tractability;
- experimental falsifiability;
- formalization/certification route;
- dependence on unavailable infrastructure.

No target advances unless Axiomatist, Cartographer, Verifier, Adversary, Formalist, and Referee obligations are recorded.

## Candidate mechanism classes to audit, not endorse

1. Smallness in a critical space.
2. Frequency-envelope or shell-localized criteria.
3. Geometric depletion of vortex stretching.
4. One-component or directional criteria.
5. Quantitative continuation bounds from near-critical norms.
6. Conditional transfer from local energy concentration controls.
7. Symmetry classes stable under perturbation.

Each class must be checked against prior art before any novelty claim.

## Proof debt

| Debt | Type | Blocking | Discharge condition |
|---|---|---:|---|
| Exact LPS theorem at `(4,6)` | external source | yes | source-normalized theorem statement |
| Weak–strong uniqueness | imported bridge | yes | matching theorem and hypotheses |
| Local maximal-time theory | external source | yes | matching theorem and strong norm |
| Clay correspondence | semantic bridge | yes | written implication map |
| Critical nonlinear estimate | analytic reconstruction | yes | line-by-line derivation |
| Restricted target | route selection | no | reviewed scorecard |

## MATHCERT handoff

The first certification target is mixed-norm scaling, not PDE regularity. Imported PDE theorems must remain provenance-bearing assumptions in any formal implication theorem.

## First executable step

Produce `work_packages/NS_CI_WP00_LPS_RECONSTRUCTION.md` with:

- exact imported theorem statement;
- derivation of the nonlinear estimate generating `‖u‖₆⁴`;
- differential inequality and Grönwall step;
- weak-to-strong upgrade route;
- assumptions and domain ledger;
- explicit statement of what this proof does not provide.

## Completion gate

WP00 is ready for programme review only when:

- every imported theorem is source-matched;
- the critical estimate is reconstructed rather than cited by name;
- the continuation bridge has no implicit arrow;
- the proof-debt register is current;
- no result claim exceeds the parent MATH-PROGRAMME ledger.