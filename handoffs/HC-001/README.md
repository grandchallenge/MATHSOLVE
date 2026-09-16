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
- `HC-R021-L012`: for every positive integral `q`, the correction-curve effectivity step has a constructive `N=6` tranche: choose `d=q m^3` and `m>>0`; the required class is an explicit positive sum of complete-intersection classes.
- `HC-R021-L013`: `k_1,...,k_6` are exactly the simultaneous first-order Hodge-preserving directions for `D=g^*Theta` and `H=(g^-1)^*Theta`; `k_7,k_8` are genuinely mixed `H^2(O_X)+H^0(Lambda^2T_X)` directions.
- `HC-R021-L014`: a sufficiently small PEL/full-level cover of the selected period component carries a universal abelian scheme and Markman's invariant normalized class as a global flat rational Hodge section. `P4-G6` is complete.
- `HC-R021-L015`: an explicit split perfect complex `P_beta` has `ch(P_beta)=12 beta'`, `ker(ob_P_beta)=span(k_1,...,k_6)`, and obstruction rank `22`; precisely the two mixed classes survive.
- `HC-R021-L016`: this failure is structural for split line bundles. If a line bundle kills all six ordinary directions, its Chern class is `A U+B V` and the mixed actions are `(qa+A^2)y_1y_2` and `(qb+B^2)y_3y_4`, both nonzero. No nonzero split complex of shifted line bundles lies in the rank-20 kernel class.
- `HC-R021-L017`: for every finite translation-plus-degree-zero-twist subgroup preserving an Example 11.2.7 coherent second-factor gluing, projection to translations is faithful and `|G|<=N`. Hence `dim Ext^2(E,E)^G>=8qN-2`; weak equivariant semiregularity of that second factor is impossible whenever `qN>=4`, including the explicit `N=6` tranche.

The protected MATHCERT WP00 disposition remains `qualified_semantic_and_conditional_interface_only`. No new certification request is justified.

## Active coherent Route A frontier

The coherent route remains blocked by nonemptiness of `D20`:

```text
explicit N=6 admissible source tranche          [L012]
   |
   +--> D20 closed determinantal                [L009/L010]
          |
          +--> A0d-COMM: kill k1,...,k6         [OPEN]
          |
          +--> A0d-MIXED: kill k7,k8             [OPEN]
                    |
                    +--> D20 nonempty            [OPEN]
                           |
                           +--> rank(ob_E)=20     [A1 conditional]
                                  |
                                  +--> all-orders obstruction-image
                                       stability [A2 conditional]
```

The six commutative directions are not yet object-level deformations. A positive proof must deform the actual secant constituents, correction curve, line bundle, and gluing morphisms compatibly. The two mixed relations cannot be replaced by ordinary Kodaira-Spencer arguments.

The numerical possibility `(q,N)=(1,2)` left by `L011` is not source-supported. Markman's effectivity argument provides some positive multiplier, not `N=2`; the constructive tranche `L012` instead has `N=6`.

## Alternate perfect-complex lane

Markman's downstream Weil-projection calculation accepts an object of `D^b(X)` whose Chern character is a nonzero integer multiple of `beta'`. This permits an alternate engineering lane not tied to the coherent gluing stack.

`L015` gives an exact control:

```text
P_beta split line-bundle complex
ch(P_beta)=12 beta'
ker(ob)=span(k1,...,k6)
rank(ob)=22
```

`L016` shows that changing the split line-bundle presentation cannot repair the two mixed classes. Any positive perfect-complex construction must therefore be genuinely non-formal: its differential or extension data, or higher-rank geometry, must supply nullhomotopies for `k_7,k_8` while retaining the six ordinary relations. A later positive object must also satisfy the negative-Ext hypothesis required by the intended all-orders deformation theorem.

## Route G frontier

The global-family edge is closed, but the factorwise equivariant shortcut is now pruned.

- `P4-G1/G2`: finite-equivariant same-ray representatives are available;
- `P4-G3`: **open** — prove weak `G`-semiregularity for a genuinely eight-dimensional external-product/Orlov representative, including the mixed `Ext^1 tensor Ext^1` contribution;
- `L017`: for the coherent second factor, every finite identity-component autoequivalence stabilizer has `|G|<=N`, and weak `G`-semiregularity is impossible when `qN>=4`. Thus `G3` cannot be proved by first making the second factor weakly equivariantly semiregular in the explicit `N=6` tranche;
- `P4-G4`: derived-equivalence symmetry transport interface available;
- `P4-G5`: Perry application conditional on `G3`;
- `P4-G6`: **complete by L014** — the level PEL family carries the global flat Hodge section and covers every selected target point.

A viable `G3` proof must exploit the total eightfold object and the mixed external-product obstruction theory, not a factorwise semiregularity argument.

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
- `grandchallenge/MATHSOLVE:work_packages/HC_R021_P4_LINE_BUNDLE_CONTROL.md`
- `grandchallenge/MATHSOLVE:work_packages/HC_R021_P4_SPLIT_LINE_BUNDLE_NO_GO.md`
- `grandchallenge/MATHSOLVE:work_packages/HC_R021_P4_AUTOEQUIV_STABILIZER_BOUND.md`
- `grandchallenge/MATHCERT:certificates/hodge/MC-HC-WP00-QUAL-001.json`
- Markman, arXiv:2509.23079, especially Corollary 7.2.5, Sections 9.1-9.2, Proposition 10.2.1, Question 11.2.2, Example 11.2.7, and Lemma 11.2.8.
- Markman, arXiv:2502.03415, Sections 8.3 and 9.3.
- Perry, arXiv:2604.00511v2, especially Theorem 1.2, Definition 2.6, Proposition 5.19, and Theorem 6.3.
- Milne, *Shimura Varieties and Moduli*, for full-level universal abelian families and the PEL interpretation.

## Smallest safe next tranche

The frontier has narrowed to non-formality and the total eightfold obstruction theory.

1. `PERFECT-MIXED`: starting from the same-ray `K_0` identity of `L015`, construct a non-split complex whose differential or extension classes make the characteristic actions of `k_7,k_8` nullhomotopic while preserving `k_1,...,k_6`. Do not search over split line-bundle decompositions; `L016` rules them all out.
2. `A0d-MIXED`: in parallel, compute the two mixed actions on a tractable coherent Example 11.2.7 gluing. One nonzero action refutes that point; simultaneous vanishing completes the mixed half of `D20`.
3. `G3`: analyze the total external-product/Orlov object directly. `L017` rules out a factorwise second-factor semiregularity proof for the source-relevant range; any useful symmetry must control the mixed `Ext^1 tensor Ext^1` contribution at the eightfold level.

## Material dependencies and boundaries

- coefficient ring remains `Q`;
- geometric category remains smooth projective complex varieties;
- target remains the Hodge-generic CM4 locus only;
- Chern-character contraction is not the object-specific Atiyah obstruction map;
- `D20` is closed and its nonemptiness remains unproved;
- six Hodge-preserving tangent directions are not six sheaf deformations until the actual gluing family is lifted;
- the two mixed directions require generalized, not purely commutative, deformation theory;
- split line-bundle K-theory cancellation cannot supply the mixed nullhomotopies;
- finite equivariance is not weak equivariant semiregularity;
- second-factor weak equivariant semiregularity is impossible for the coherent gluing when `qN>=4`, but final-eightfold `G3` remains open;
- `G6` closure supplies only an algebraic family and global flat Hodge section, not algebraicity;
- no inverse Lefschetz, Kunneth projector, Hodge-locus, Tate, motivated, or numerical substitute may replace an algebraic cycle;
- no claim from this target is certified until independently adjudicated by MATHCERT.

## Legitimate stop/re-plan boundaries

Stop or re-plan only for a material source correction; evidence that the selected target is known or vacuous; a genuine obstruction to all coherent, non-formal-perfect, and total-equivariant routes; contradiction of the exact target formulation; a reserved INTELLECT transition; authentication or safety failure; or material theorem closure.

`D20` nonemptiness, non-formal mixed cancellation, and genuinely eight-dimensional `G3` are mathematical frontiers, not governance stops.
