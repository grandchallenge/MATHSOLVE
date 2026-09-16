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
- `HC-WP01/WP02`: complete/current for the selected target.
- `HC-P03`: active through `HC-R021-A8-CM4-C2`; `HC-P04` and the universal Hodge conjecture remain open.
- source-proved inputs: coherent secant objects, nonzero Fourier-Mukai rank, Hodge persistence of the normalized class, and nonzero Weil projection.
- `L001-L006`: restricted first-order semiregularity interface, familywise Perry reduction, same-ray finite equivariance, ordinary-semiregularity dimension obstruction, exact kernel criterion, and exact contraction rank `20` with eight-dimensional kernel.
- `L007`: objectwise rank `20` is equivalent to vanishing of eight explicit degree-two Yoneda relations.
- `L008-L010`: Example 11.2.7 gives a family rather than a canonical object; the rank-20 locus `D20` is determinantal closed; the admissible gluing choices form a nonempty finite-type stack with a universal relatively perfect family after flattening/base change.
- `L011`: a naive transitive pure-translation copy of the sixfold strategy is dimensionally pruned; `dim Ext^2(E,E)^G >= 8qN-2`.
- `L012`: for every positive integral `q`, the correction-curve step has a constructive `N=6` tranche by taking `d=q m^3`, `m>>0`.
- `L013`: `k_1,...,k_6` are exactly the simultaneous first-order Hodge-preserving directions for `D=g^*Theta` and `H=(g^-1)^*Theta`; `k_7,k_8` are genuinely mixed `H^2(O_X)+H^0(Lambda^2T_X)` directions.
- `L014`: a sufficiently small PEL/full-level cover of the selected period component carries a universal abelian scheme and Markman's invariant normalized class as a global flat rational Hodge section. `P4-G6` is complete.
- `L015`: an explicit split perfect complex `P_beta` has `ch(P_beta)=12 beta'`, `ker(ob_P_beta)=span(k_1,...,k_6)`, and obstruction rank `22`; precisely the two mixed classes survive.
- `L016`: no nonzero split complex of shifted line bundles can satisfy all eight beta-prime kernel relations. A positive perfect-complex route must be genuinely non-formal or use non-line-bundle geometry.
- `L017`: for any finite translation-plus-degree-zero-twist subgroup preserving an Example 11.2.7 coherent second-factor gluing, projection to translations is faithful and `|G|<=N`; hence the second factor cannot be weakly `G`-semiregular when `qN>=4`, including the explicit `N=6` tranche.
- `L018`: weak equivariant semiregularity of the final external-product/Orlov object cannot bypass the second-factor rank-20 condition. For finite identity-component autoequivalence actions on an abelian variety, the relevant weak and ordinary `G`-semiregularity tests have the same degree-two Hochschild target; every second-factor contraction-kernel direction produces an invariant total obstruction. Therefore final weak `G`-semiregularity forces all eight second-factor relations and hence rank `20`.

The protected MATHCERT WP00 disposition remains `qualified_semantic_and_conditional_interface_only`. No new certification request is justified.

## Active first-order frontier

Every currently viable route now passes through the same second-factor condition:

```text
construct E' on the source abelian fourfold
with ch(E') = M beta', M != 0
        |
        +--> kill k1,...,k6                 [ordinary directions]
        |
        +--> kill k7,k8                     [mixed gerby/bivector directions]
        |
        +--> ker(ob_E') = ker(c_beta')
             rank(ob_E') = 20
```

There are two live engineering realizations.

### Coherent Route A

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

The six ordinary directions are not yet object-level deformations: a proof must deform the actual secant constituents, correction curve, line bundle, and gluing maps. The two mixed relations require generalized deformation theory.

### Non-formal perfect-complex lane

Markman Lemma 11.2.8 accepts any `E' in D^b(X)` whose Chern character is a nonzero integer multiple of `beta'`.

`L015` supplies a rank-22 split control; `L016` proves every split line-bundle realization fails. Therefore the live perfect-complex problem is:

```text
construct a genuinely non-formal same-ray E'
with Ext^{<0}(E',E')=0
and ob_E'(k_i)=0 for i=1,...,8.
```

The differential/extension data must provide nullhomotopies for `k_7,k_8` while retaining the six ordinary kernel directions.

## Route G ordering after L018

Route G is no longer an independent first-order escape:

```text
second-factor rank 20 / eight relations          [REQUIRED]
        |
        +--> construct useful finite symmetry of total object
        |
        +--> G3: weak G-semiregularity of final eightfold     [OPEN]
        |       including mixed Ext^1 tensor Ext^1
        |
        +--> G4/G5 Perry familywise transport                 [CONDITIONAL]
        |
        +--> G6 algebraic PEL family + global flat class      [COMPLETE L014]
```

`L017` rules out proving `G3` by first making the coherent second factor weakly equivariantly semiregular in the source-relevant `qN>=4` range. `L018` is stronger: even a genuinely total weakly equivariant solution must already contain the second-factor rank-20 cancellation.

## Authoritative pointers

- `grandchallenge/INTELLECT:CONSTITUTION.md`
- `grandchallenge/INTELLECT:governance/constitutional_authority_schedule.json`
- `grandchallenge/MATHSOLVE:AGENTS.md`
- `grandchallenge/MATHSOLVE:campaign_ledgers/HC-001/proof_obligation_dag.json` — immutable WP00 DAG
- `grandchallenge/MATHSOLVE:campaign_ledgers/HC-001/post_wp00_proof_obligation_dag.json` — active theorem DAG
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
- `grandchallenge/MATHSOLVE:work_packages/HC_R021_P4_WEAK_EQUIV_REQUIRES_D20.md`
- Markman, arXiv:2509.23079, especially Question 11.2.2, Example 11.2.7, Lemma 11.2.8, Proposition 10.2.1
- Markman, arXiv:2502.03415, Sections 8.3 and 9.3
- Perry, arXiv:2604.00511v2, especially Lemma 3.3, Proposition 5.19, Theorem 1.2, and Theorem 6.3

## Smallest safe next tranche

Work only the second-factor rank-20 frontier.

1. Reconstruct Markman's genus-four building block `F'` from the earlier secant paper and compute the Hochschild action on that object as far as the source permits.
2. For the Example 11.2.7 gluing triangle

```text
E' -> A direct_sum i_*L -> Q -> E'[1],
```

compute how the two mixed classes `k_7,k_8` change under the connecting morphism. The target is an explicit criterion on the extension/gluing class for the mixed action to become nullhomotopic.
3. In parallel, formulate the same problem for a finite locally free resolution of the non-formal perfect-complex lane: seek `h_7,h_8` with `ev(k_i)=[d,h_i]` for `i=7,8`, while preserving the six ordinary relations and `Ext^{<0}=0`.
4. Do not spend further effort on split line-bundle decompositions or on equivariance before rank `20`; `L016` and `L018` respectively rule those out as shortcuts.

## Material boundaries

- coefficient ring remains `Q`;
- geometric category remains smooth projective complex varieties;
- target remains the Hodge-generic CM4 locus only;
- Chern-character contraction is not the object-specific Atiyah obstruction map;
- `D20` nonemptiness remains unproved;
- six Hodge-preserving tangent directions are not six sheaf deformations until the actual object is lifted;
- the two mixed directions require generalized deformation theory;
- split line-bundle K-theory cancellation cannot supply the mixed nullhomotopies;
- final weak equivariant semiregularity cannot bypass second-factor rank `20`;
- `G6` closure supplies only an algebraic family and global flat Hodge section, not algebraicity;
- no inverse Lefschetz, Kunneth projector, Hodge-locus, Tate, motivated, or numerical substitute may replace an algebraic cycle;
- no claim from this target is certified until independently adjudicated by MATHCERT.

## Legitimate stop/re-plan boundaries

Stop or re-plan only for a material source correction; evidence that the selected target is known or vacuous; a genuine obstruction to both coherent and non-formal-perfect rank-20 constructions; contradiction of the exact target formulation; a reserved INTELLECT transition; authentication or safety failure; or material theorem closure.

The second-factor rank-20/eight-relation problem is the current mathematical frontier, not a governance stop.
