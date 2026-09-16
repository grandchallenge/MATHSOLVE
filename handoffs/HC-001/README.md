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
- `HC-R021-L001`: restricted first-order semiregularity kills Hodge-preserving ambient obstructions when injective on the ambient-obstruction image.
- `HC-R021-L002`: Perry's 2026 theorem gives all-orders algebraicity transport along an explicitly bound smooth proper family once weak finite-group equivariant semiregularity is supplied.
- `HC-R021-L003`: finite translation-orbit sums supply same-ray finite equivariance, but equivariance is not semiregularity.
- `HC-R021-L004`: ordinary semiregularity of the Example 11.2.7 second-factor gluing is impossible whenever `qN^2 >= 4` by an exact Ext-dimension bound.
- `HC-R021-L005`: Markman's restricted condition is equivalent to equality of the ambient-obstruction kernel and the Chern-character contraction kernel.
- `HC-R021-L006`: for the CM4 class `beta'`, the exact HKR contraction rank is `20` and its kernel has dimension `8`.
- `HC-R021-L007`: objectwise, the restricted semiregularity condition is equivalent to vanishing of eight explicit degree-two Yoneda relations `k_1,...,k_8`; any one nonzero relation refutes that object.
- `HC-R021-L008`: Example 11.2.7 does not select one canonical `E'`; it specifies an admissible gluing family through choices of curve, translates, line bundle, and fiber identifications. The common Chern character does not determine the object-specific obstruction map.

The protected MATHCERT WP00 disposition remains `qualified_semantic_and_conditional_interface_only`. No new certification request is justified by the current Solve-level reductions.

## Active Route A frontier

`HC-R021-P4-A0` is now the first open node.

The published source fixes the ray

```text
beta' = g^*Theta - (q/6)(g^-1)^*(Theta^3)
```

but constructs `E'` through existential/generic choices. Before a single numerical `rank(ob_E')` can be computed, do one of the following:

1. **Representative path:** bind a concrete admissible datum

```text
D_star = (d,N,C', {T_j}, L, {phi_p})
```

sufficient to reconstruct the exact gluing sequence

```text
0 -> E'_star -> (direct_sum_j T_j) direct_sum i_*L -> direct_sum_p k_p -> 0;
```

then evaluate the eight `L007` Yoneda classes on that exact object.

2. **Uniform path:** prove that all eight `L007` relations vanish on a stated nonempty open subset of the admissible Example 11.2.7 gluing-parameter space.

Once A0 is discharged, `P4-A1` asks whether `rank(ob_E)=20`; compatibility already forces `20 <= rank(ob_E) <= 28`. A positive A1 still leaves `P4-A2`, the all-orders obstruction-image-stability theorem.

## Parallel Route G frontier

The equivariant route remains available:

- `P4-G3`: prove weak `G`-semiregularity of a useful same-ray total object, including the mixed `Ext^1 tensor Ext^1` contribution;
- `P4-G6`: bind the abstract `C_CM4` target quantifier to explicit algebraic family/level-moduli carriers and a global Gauss-Manin section;
- then apply Perry familywise.

Perry's worked Markman application concerns the earlier abelian-sixfold construction; it does not close the present CM4 genus-four semiregularity problem.

## Authoritative pointers

- `grandchallenge/INTELLECT:CONSTITUTION.md`
- `grandchallenge/INTELLECT:governance/constitutional_authority_schedule.json`
- `grandchallenge/MATHSOLVE:AGENTS.md`
- `grandchallenge/MATHSOLVE:campaign_ledgers/HC-001/proof_obligation_dag.json` — immutable WP00 DAG;
- `grandchallenge/MATHSOLVE:campaign_ledgers/HC-001/post_wp00_proof_obligation_dag.json` — active post-WP00 theorem DAG;
- `grandchallenge/MATHSOLVE:work_packages/HC_R021_CM4_EIGHTFOLD_CODIM2.md`
- `grandchallenge/MATHSOLVE:work_packages/HC_R021_P4_PERRY_EQUIVARIANT_REDUCTION.md`
- `grandchallenge/MATHSOLVE:work_packages/HC_R021_P4_SEMIREGULARITY_DIAGNOSTICS.md`
- `grandchallenge/MATHSOLVE:work_packages/HC_R021_P4_CONTRACTION_RANK.md`
- `grandchallenge/MATHSOLVE:work_packages/HC_R021_P4_ATIYAH_RANK_REDUCTION.md`
- `grandchallenge/MATHSOLVE:work_packages/HC_R021_P4_ATIYAH_DATUM_BOUNDARY.md`
- `grandchallenge/MATHCERT:certificates/hodge/MC-HC-WP00-QUAL-001.json`
- Markman, arXiv:2509.23079, Question 11.2.2, Example 11.2.7, Lemma 11.2.8.
- Markman, arXiv:2502.03415, Lemma 8.3.4, Remark 8.3.5, Proposition 8.3.9.
- Perry, arXiv:2604.00511v2, Theorems 1.2 and 6.3.

## Smallest safe next tranche

Pursue `P4-A0` before attempting further representative-specific Ext calculations.

1. Search the cited genus-four real-multiplication examples for a sufficiently explicit Jacobian/source datum that can bind `X`, `Theta`, and `g`.
2. Determine whether Markman's curve-class existence step can be made constructive for one such datum; if yes, bind `d,N,C'` and the remaining generic gluing choices algebraically.
3. If representative construction remains non-explicit, formulate the admissible gluing parameter space and test whether the eight `L007` Yoneda classes define algebraic sections whose common vanishing can be proved on a nonempty open or closed locus.
4. Do not infer Yoneda vanishing from the common Chern character.

## Material dependencies and boundaries

- coefficient ring remains `Q`;
- geometric category remains smooth projective complex varieties;
- the target remains the Hodge-generic CM4 locus only;
- Chern-character contraction is not the object-specific Atiyah obstruction map;
- Example 11.2.7's existential gluing choices must not be treated as a content-addressed representative;
- first-order restricted semiregularity is not an all-orders deformation theorem;
- finite equivariance is not weak equivariant semiregularity;
- Perry's familywise theorem is not a global period-domain theorem without explicit family coverage;
- no inverse Lefschetz, Kunneth projector, Hodge-locus, Tate, motivated, or numerical substitute may replace an algebraic cycle;
- no claim from this target is certified until independently adjudicated by MATHCERT.

## Legitimate stop/re-plan boundaries

Stop or re-plan only for a material source correction; evidence that the selected target is known or vacuous; a genuine obstruction to both Route A and Route G; contradiction of the exact target formulation; a reserved INTELLECT transition; authentication or safety failure; or material theorem closure.

The current A0 datum gap is an evidentiary frontier to work, not a governance stop.
