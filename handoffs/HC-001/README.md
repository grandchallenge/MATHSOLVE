# HC-001 — Handoff

## Target repository and authority

Target work repository: `grandchallenge/MATHSOLVE`.

MATHSOLVE owns bounded theorem development and research artifacts. MATHCERT is the sole mathematical certification authority. Human Steward authority remains reserved only for transitions named by the live INTELLECT Constitution and authority schedule.

## Purpose

Advance the rational Hodge campaign from the qualified WP00 interface into an executable restricted theorem programme without reopening the completed semantic baseline or implying the universal conjecture.

## Primary deliverable

Prove, refute, or sharply localize `HC-R021-A8-CM4-C2` in `work_packages/HC_R021_CM4_EIGHTFOLD_CODIM2.md`.

## Current substantive state

- `HC-WP00`: complete in Solve and qualified by MATHCERT as semantic/conditional interface only; its content-addressed proof DAG remains unchanged.
- `HC-WP01`: complete for current target selection.
- `HC-WP02`: current for target selection.
- `HC-P03`: active through `HC-R021-A8-CM4-C2`.
- `HC-P04`: open; universal Hodge remains unproved.
- source-proved inputs: coherent secant objects, nonzero Fourier-Mukai rank, Hodge persistence of the normalized class, and nonzero Weil projection.
- `HC-R021-L001` through `L006`: restricted first-order semiregularity interface, familywise Perry reduction, same-ray finite equivariance, ordinary-semiregularity dimension obstruction, exact kernel criterion, and exact contraction rank `20` with eight-dimensional kernel.
- `HC-R021-L007`: objectwise rank `20` is equivalent to vanishing of eight explicit degree-two Yoneda relations; any one nonzero relation refutes that object.
- `HC-R021-L008`: Example 11.2.7 specifies an admissible gluing family, not one canonical object; the common Chern character does not determine the object-specific obstruction map.
- `HC-R021-L009`: the desired minimal-rank locus `D20={rank(ob)<=20}` is determinantal closed and is exactly the common zero locus of the eight `L007` relations.
- `HC-R021-L010`: the Example 11.2.7 choices form a nonempty finite-type algebraic gluing stack with a universal relatively perfect family after flattening/base change.
- `HC-R021-L011`: a naive transitive pure-translation copy of the sixfold strategy is dimensionally pruned; `dim Ext^2(E,E)^G >= 8qN-2`, so dimension forcing reaches rank `20` only for `qN<=2` and full invariant-`Ext^2` semiregularity is impossible for `qN>=4`.
- `HC-R021-L012`: the correction-curve effectivity step admits a constructive bounded tranche: for every positive integral `q`, choose `N=6`, `d=q m^3`, and `m>>0`; then the required curve class is an explicit positive sum of complete-intersection classes.
- `HC-R021-L013`: the six `H^1(T_X)` generators `k_1,...,k_6` are exactly the simultaneous first-order Hodge-preserving directions for the two ample classes `D=g^*Theta` and `H=(g^-1)^*Theta`; the remaining `k_7,k_8` are genuinely mixed `H^2(O_X)+H^0(Lambda^2T_X)` directions.
- `HC-R021-L014`: the selected connected Weil-type period component has a sufficiently small algebraic PEL/full-level cover carrying a universal abelian scheme; Markman's exact `Spin(V)_{eta,B}` invariance makes `kappa(E_0)` descend to a global flat rational section that is Hodge on every fiber. `P4-G6` is therefore complete.

The protected MATHCERT WP00 disposition remains `qualified_semantic_and_conditional_interface_only`. No new certification request is justified.

## Active Route A frontier

The direct route remains blocked only by nonemptiness of `D20`, now split into its actual geometric pieces:

```text
explicit N=6 admissible source tranche          [L012]
   |
   +--> D20 closed determinantal                [L009/L010]
          |
          +--> A0d-COMM: kill k1,...,k6         [OPEN]
          |      by a relative commutative
          |      construction over the
          |      simultaneous D,H Hodge locus
          |
          +--> A0d-MIXED: kill k7,k8             [OPEN]
                 by object-level generalized
                 deformation theory
                    |
                    +--> D20 nonempty            [OPEN]
                           |
                           +--> rank(ob_E)=20     [A1 conditional]
                                  |
                                  +--> all-orders obstruction-image
                                       stability [A2 conditional]
```

The six commutative directions are not yet object-level deformations. A positive proof must deform the secant constituents, correction curve, line bundle, and gluing morphisms compatibly over those directions. The two mixed relations cannot be replaced by ordinary Kodaira-Spencer arguments.

The numerical possibility `(q,N)=(1,2)` left by `L011` is not source-supported: Markman's published effectivity step provides only some positive multiplier `N`, not `N=2`. The constructive source tranche `L012` instead has `N=6`, so `qN=6q>=6` and the naive transitive-translation dimension argument is unavailable there.

## Route G frontier

The global family edge is no longer open.

- `P4-G1/G2`: finite-equivariant same-ray representatives are available;
- `P4-G3`: **open** — prove weak `G`-semiregularity for a useful non-naive representative, including the mixed `Ext^1 tensor Ext^1` contribution;
- `P4-G4`: derived-equivalence symmetry transport interface available;
- `P4-G5`: Perry application conditional on `G3`;
- `P4-G6`: **complete by L014** — an algebraic PEL level cover carries the global flat Hodge section and covers every selected target point.

Thus `G3` is now the sole substantive Route-G obstruction before Perry's all-orders theorem can be invoked.

## Authoritative pointers

- `grandchallenge/INTELLECT:CONSTITUTION.md`
- `grandchallenge/INTELLECT:governance/constitutional_authority_schedule.json`
- `grandchallenge/MATHSOLVE:AGENTS.md`
- `grandchallenge/MATHSOLVE:campaign_ledgers/HC-001/proof_obligation_dag.json` — immutable WP00 DAG;
- `grandchallenge/MATHSOLVE:campaign_ledgers/HC-001/post_wp00_proof_obligation_dag.json` — active post-WP00 theorem DAG;
- `grandchallenge/MATHSOLVE:work_packages/HC_R021_CM4_EIGHTFOLD_CODIM2.md`
- `grandchallenge/MATHSOLVE:work_packages/HC_R021_P4_CONTRACTION_RANK.md`
- `grandchallenge/MATHSOLVE:work_packages/HC_R021_P4_ATIYAH_RANK_REDUCTION.md`
- `grandchallenge/MATHSOLVE:work_packages/HC_R021_P4_ATIYAH_DATUM_BOUNDARY.md`
- `grandchallenge/MATHSOLVE:work_packages/HC_R021_P4_ATIYAH_DETERMINANTAL_LOCUS.md`
- `grandchallenge/MATHSOLVE:work_packages/HC_R021_P4_GLUE_PARAMETER_STACK.md`
- `grandchallenge/MATHSOLVE:work_packages/HC_R021_P4_EQUIVARIANT_DIMENSION_OBSTRUCTION.md`
- `grandchallenge/MATHSOLVE:work_packages/HC_R021_P4_N6_EFFECTIVE_SOURCE.md`
- `grandchallenge/MATHSOLVE:work_packages/HC_R021_P4_SIX_COMMUTATIVE_DIRECTIONS.md`
- `grandchallenge/MATHSOLVE:work_packages/HC_R021_P4_PEL_FAMILY_COVERAGE.md`
- `grandchallenge/MATHCERT:certificates/hodge/MC-HC-WP00-QUAL-001.json`
- Markman, arXiv:2509.23079, especially Corollary 7.2.5, Sections 9.1-9.2, Proposition 10.2.1, Question 11.2.2, Example 11.2.7, and Lemma 11.2.8.
- Markman, arXiv:2502.03415, Section 8.3 and Section 9.3.
- Perry, arXiv:2604.00511v2, Theorems 1.2 and 6.3.
- Milne, *Shimura Varieties and Moduli*, for full-level universal abelian families and the PEL interpretation.

## Smallest safe next tranche

Pursue the two now-independent hard edges rather than more infrastructure.

1. `A0d-COMM`: determine whether the `N=6` gluing construction can be made relative over the simultaneous `D,H` Hodge/PEL deformation directions. A valid proof must lift the actual constituents and gluing triangle, not only their Chern characters.
2. `A0d-MIXED`: compute the actions of `k_7,k_8` on a tractable admissible object; one nonzero action refutes that object, while simultaneous vanishing completes the mixed part of `D20`.
3. In parallel, `G3`: seek a non-naive finite autoequivalence symmetry whose invariant obstruction category controls the mixed `Ext^1 tensor Ext^1` term. Do not return to the pruned pure-transitive translation argument except for an independently constructed admissible exceptional point.

## Material dependencies and boundaries

- coefficient ring remains `Q`;
- geometric category remains smooth projective complex varieties;
- target remains the Hodge-generic CM4 locus only;
- Chern-character contraction is not the object-specific Atiyah obstruction map;
- `D20` is closed and its nonemptiness remains unproved;
- six Hodge-preserving tangent directions are not six sheaf deformations until the actual gluing family is lifted;
- the two mixed directions require generalized, not purely commutative, deformation theory;
- finite equivariance is not weak equivariant semiregularity;
- `G6` closure supplies only an algebraic family and global flat Hodge section, not algebraicity;
- no inverse Lefschetz, Kunneth projector, Hodge-locus, Tate, motivated, or numerical substitute may replace an algebraic cycle;
- no claim from this target is certified until independently adjudicated by MATHCERT.

## Legitimate stop/re-plan boundaries

Stop or re-plan only for a material source correction; evidence that the selected target is known or vacuous; a genuine obstruction to both Route A and Route G; contradiction of the exact target formulation; a reserved INTELLECT transition; authentication or safety failure; or material theorem closure.

`D20` nonemptiness and `G3` weak equivariant semiregularity are mathematical frontiers, not governance stops.
