# MS-NS-CI-WP00 — Critical-integrability theorem spine

## Identity

- Parent programme tracker: `grandchallenge/MATH-PROGRAMME#55`
- MATHSOLVE issue: `#18`
- Campaign: `NS-CI-001`
- Owning pillar: MATHSOLVE
- State: quantitative reconstruction complete; parent governance gate pending

## Result-status box

| Field | Value |
|---|---|
| Result status | `OPEN TARGET / CLASSICAL CONTINUATION CHAIN RECONSTRUCTED` |
| Strongest supported result | Finite `L4_tL6_x` control closes the H1 continuation and weak–strong uniqueness estimates; universal control for Fefferman's full data class is sufficient for Clay statement (A) |
| Not claimed | Universal critical integrability, global regularity, a new criterion, bidirectional equivalence, or full-data coverage from compact support alone |
| First executable step | Parent Amanuensis and Referee integration; do not generate mechanisms yet |

## Corrected problem

Let `u0` be any smooth divergence-free field on `R3` satisfying Fefferman's rapid-decay condition. Determine whether every Leray–Hopf solution satisfies

```math
I_T(u):=∫₀ᵀ ‖u(t)‖_{L⁶(ℝ³)}⁴dt<∞
```

for every finite `T>0`.

The former compact-support formulation is retained only as the restricted lane `NS-CI-R-COMPACT`.

## Tactical posture

MATHSOLVE must not treat the conditional criterion as though its hypothesis were universal. The quantitative reconstruction identifies the exact nonlinear estimate a future mechanism would have to improve or bypass. It does not authorize mechanism generation before the parent WP00 governance gate.

## Audited theorem spine

```text
MS-NS-CI-D000  Fixed equation, R3, full rapid-decay data, solution classes  [audited]
MS-NS-CI-L001  Leray-Hopf energy and global weak existence                  [operational import]
MS-NS-CI-L002  Sobolev H1 -> L6                                             [checked]
MS-NS-CI-C003  u in L2_t L6_x                                               [checked]
MS-NS-CI-O004  energy space does not imply L4_t L6_x                        [checked obstruction]
MS-NS-CI-L005  mixed-norm scaling                                           [checked]
MS-NS-CI-C006  I_T is critical                                              [checked]
MS-NS-CI-L007  operational LPS theorem at (4,6)                             [audited]
MS-NS-CI-L008  weak-strong uniqueness                                       [operational import]
MS-NS-CI-L009  local H1 strong existence / maximal-time gate                [operational import]
MS-NS-CI-B010  critical-integral continuation bridge                        [reconstructed]
MS-NS-CI-B011  full-data universal I_T implies Clay statement (A)           [checked one-way]
MS-NS-CI-B012  reverse strong-class correspondence                          [pending]
MS-NS-CI-T013  universal critical-integrability target                      [open]
MS-NS-CI-R014  first selected restricted theorem target                     [unselected]
MS-NS-CI-R-COMPACT compact-support restricted lane                          [defined]
```

## S0 — theorem normalization

The MATHFORGE ledger now separates:

- Fefferman's official rapidly decreasing whole-space data;
- compactly supported data as a strict restricted subclass;
- Prodi's original generalized-solution theorem;
- the modern R3 Leray–Hopf operational formulation;
- historical Serrin and Ladyzhenskaya records with their remaining extraction states;
- local strong, global weak, and weak–strong interfaces from a modern reconstruction of Leray.

The operational theorem chain is usable without falsely declaring the historical extraction complete.

## S1 — quantitative `(4,6)` reconstruction

Delivered in `work_packages/NS_CI_WP00_LPS_RECONSTRUCTION.md`.

Testing the strong equation against `-Delta u` gives

```math
\frac12\frac d{dt}\|\nabla u\|_2^2+\nu\|\Delta u\|_2^2
=\int (u\cdot\nabla)u\cdot\Delta u.
```

The nonlinear term satisfies

```math
\left|\int (u\cdot\nabla)u\cdot\Delta u\right|
\le C\|u\|_6\|\nabla u\|_2^{1/2}\|\Delta u\|_2^{3/2}
\le \frac\nu2\|\Delta u\|_2^2
 +C\nu^{-3}\|u\|_6^4\|\nabla u\|_2^2.
```

Thus

```math
\|\nabla u(t)\|_2^2
\le \|\nabla u_0\|_2^2
\exp\!\left(C\nu^{-3}\int_0^t\|u(s)\|_6^4ds\right).
```

The exact missing coefficient is `||u||6^4`.

For the difference `w=v-u`, the same exponent appears:

```math
\frac d{dt}\|w\|_2^2
\le C\nu^{-3}\|u\|_6^4\|w\|_2^2.
```

This closes weak–strong uniqueness under the standard rigorous interface.

## S2 — continuation and Clay correspondence

For the maximal H1 strong solution on `[0,T*)`, finite critical integral bounds the H1 norm and permits restart. Therefore

```math
T_*<∞
\implies
∫₀^{T_*}‖u(t)‖₆⁴dt=∞.
```

For Fefferman's full data class:

```text
global Leray weak existence
 + universal finite I_T
 + operational LPS regularity and uniqueness
 + local H1 continuation and bootstrapping
 -> global smooth solution with bounded energy
 -> Clay statement (A).
```

This is an audited one-way implication. Bidirectional equivalence is not promoted until the reverse strong-class and every-Leray–Hopf bridge is source-normalized.

## S3 — negative route ledger

Terminate or restrict any route relying only on:

- energy-space membership;
- finite-time `L^p` inclusion in the wrong direction;
- an unproved uniform H1 bound;
- a Galerkin cutoff with scale-deteriorating constants;
- a supercritical estimate;
- a hypothesis already equivalent to known regularity;
- silent transfer from compact support to the full rapid-decay class;
- numerical boundedness as continuum proof.

Each terminated route must record the smallest exact failure and nearest viable restricted problem.

## S4 — restricted-target matrix

Status: not opened for scoring.

After parent WP00 promotion, candidates may be scored on:

- leverage toward `MS-NS-CI-T013`;
- prior-art and novelty risk;
- non-circularity;
- scaling compatibility;
- analytic tractability;
- falsifiability;
- formalization/certification route;
- infrastructure and compute cost.

No target advances without the full Council record.

## Candidate mechanism classes to audit later, not endorse now

1. Smallness in a critical space.
2. Frequency-envelope or shell-localized criteria.
3. Geometric depletion of vortex stretching.
4. One-component or directional criteria.
5. Quantitative continuation from near-critical norms.
6. Local-energy concentration controls.
7. Perturbatively stable symmetry classes.

Each class requires prior-art audit before novelty language.

## Proof debt

| Debt | Type | Blocking here | State |
|---|---|---:|---|
| Operational LPS theorem at `(4,6)` | external source | no | audited |
| Weak–strong uniqueness | imported bridge | no | operationally audited and estimate reconstructed |
| Local maximal-time theory | external source | no | operationally audited and restart route reconstructed |
| Full-data Clay forward implication | semantic bridge | no | checked |
| Reverse equivalence | semantic bridge | no | pending; not claimed |
| Historical Serrin/Ladyzhenskaya extraction | provenance | no | pending |
| Restricted target | route selection | yes before WP04 | unopened |
| Parent Amanuensis/Referee gate | governance | yes | pending |

## MATHCERT handoff

The first certification target remains mixed-norm scaling. Imported PDE theorems stay provenance-bearing assumptions in any formal implication theorem.

## Current executable step

Do not produce a mechanism proposal. Support the parent PR by:

- verifying cross-document data-class consistency;
- verifying the one-way implication language;
- responding to any Referee concern about the H1 restart or every-Leray–Hopf quantifier;
- preserving the quantitative reconstruction as the canonical analytic interface.

## Completion gate

This MATHSOLVE WP00 slice is ready for parent review when:

- the parent artifacts use the full Fefferman data class;
- compact support is only a restricted lane;
- the quantitative estimate is linked in the claim ledger;
- the Referee approves the forward implication and non-equivalence boundary;
- CI passes;
- no result claim exceeds the parent ledger.
