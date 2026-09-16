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
- `HC-R021-L002`: Perry's theorem gives familywise all-orders algebraicity transport once weak finite-group equivariant semiregularity is supplied.
- `HC-R021-L003`: same-ray finite equivariance is available by translation orbit sums; equivariance is not semiregularity.
- `HC-R021-L004`: ordinary semiregularity is impossible for the Example 11.2.7 gluing whenever `qN^2 >= 4` by an exact Ext-dimension bound.
- `HC-R021-L005`: Markman's restricted condition is equivalent to equality of the ambient-obstruction kernel and Chern-character contraction kernel.
- `HC-R021-L006`: for `beta'`, the exact HKR contraction rank is `20` and its kernel has dimension `8`.
- `HC-R021-L007`: objectwise, rank `20` is equivalent to vanishing of eight explicit degree-two Yoneda relations; any one nonzero relation refutes that object.
- `HC-R021-L008`: Example 11.2.7 defines an admissible gluing family, not one canonical object; the common Chern character does not determine the object-specific obstruction map.
- `HC-R021-L009`: on an algebraic gluing family the minimal-rank condition is the closed determinantal locus `D20={rank(ob)<=20}`; compatibility forces rank at least `20`, so `D20` is exactly the rank-20 locus and the common zero locus of the eight `L007` relations.
- `HC-R021-L010`: after fixing one source-admissible discrete datum, the curve, translations, line bundle, and constituent-wise gluing choices form a nonempty finite-type algebraic stack carrying a universal relatively perfect family after flattening.

The protected MATHCERT WP00 disposition remains `qualified_semantic_and_conditional_interface_only`. No new certification request is justified.

## Active Route A frontier

The source ambiguity and parameter-space construction are now resolved. The first open direct-route node is

```text
HC-R021-P4-A0d: prove D20 != empty.
```

Equivalently, construct one admissible simple Example 11.2.7 gluing for which all eight `L007` Yoneda relations vanish.

The direct route is now

```text
S_adm nonempty                         [L010]
  -> D20 closed determinantal          [L009]
  -> prove D20 nonempty                [A0d OPEN]
  -> choose E in D20; rank(ob_E)=20    [A1 conditional]
  -> all-orders obstruction-image
     stability                         [A2 conditional]
```

The desired minimal-rank locus is closed, not generically open. A specialization argument is valid only if the special point remains inside the admissible/simple family and the eight relations can be checked there.

High-value routes to `A0d` are:

1. construct a symmetric or otherwise tractable admissible gluing point and evaluate the eight relations;
2. specialize within `S_adm` to a calculable point while preserving simplicity/admissibility;
3. prove the eight relative Yoneda sections vanish identically on a parameter component;
4. find a finite symmetry forcing the eight relations, linking Route A with Route G.

## Parallel Route G frontier

The equivariant route remains independent:

- `P4-G3`: prove weak `G`-semiregularity of a useful same-ray total object, including the mixed `Ext^1 tensor Ext^1` contribution;
- `P4-G6`: bind the abstract `C_CM4` target quantifier to explicit algebraic family/level-moduli carriers and a global Gauss-Manin section;
- then apply Perry familywise.

Perry's worked Markman application concerns the earlier abelian-sixfold construction; it does not close the present CM4 genus-four problem.

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
- `grandchallenge/MATHSOLVE:work_packages/HC_R021_P4_ATIYAH_DETERMINANTAL_LOCUS.md`
- `grandchallenge/MATHSOLVE:work_packages/HC_R021_P4_GLUE_PARAMETER_STACK.md`
- `grandchallenge/MATHCERT:certificates/hodge/MC-HC-WP00-QUAL-001.json`
- Markman, arXiv:2509.23079, Question 11.2.2, Example 11.2.7, Lemma 11.2.8.
- Markman, arXiv:2502.03415, Lemma 8.3.4, Remark 8.3.5, Proposition 8.3.9.
- Perry, arXiv:2604.00511v2, Theorems 1.2 and 6.3.

## Smallest safe next tranche

Attack `P4-A0d` directly. First test whether any general Hochschild/Atiyah theorem strengthens the known inclusion `ker(ob_E) subset ker(c_ch(E))` for the present gluing family. If no such theorem applies, construct a symmetry-controlled or specialized admissible point of `S_adm` and compute the eight `L007` Yoneda relations there. Do not infer their vanishing from the Chern character.

## Material dependencies and boundaries

- coefficient ring remains `Q`;
- geometric category remains smooth projective complex varieties;
- the target remains the Hodge-generic CM4 locus only;
- Chern-character contraction is not the object-specific Atiyah obstruction map;
- rank `20` is a closed determinantal condition whose nonemptiness must be proved;
- the universal gluing is constituent-wise over labeled incidence schemes, not an identification of the full direct-sum fiber with a line;
- first-order restricted semiregularity is not an all-orders deformation theorem;
- finite equivariance is not weak equivariant semiregularity;
- Perry's familywise theorem is not a global period-domain theorem without explicit family coverage;
- no inverse Lefschetz, Kunneth projector, Hodge-locus, Tate, motivated, or numerical substitute may replace an algebraic cycle;
- no claim from this target is certified until independently adjudicated by MATHCERT.

## Legitimate stop/re-plan boundaries

Stop or re-plan only for a material source correction; evidence that the selected target is known or vacuous; a genuine obstruction to both Route A and Route G; contradiction of the exact target formulation; a reserved INTELLECT transition; authentication or safety failure; or material theorem closure.

`D20` nonemptiness is the current mathematical frontier, not a governance stop.
