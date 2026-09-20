# UC-001 — Handoff

## Target repository and authority

Target work repository: `grandchallenge/MATHSOLVE`.

INTELLECT work-package phase: `not applicable`.

MATHSOLVE owns bounded theorem development. MATHFORGE owns external source and
provider provenance. MATHCERT alone owns certification. `UC-FRANKL` and
`UC-P04` remain outside any restricted-result promotion by implication.

## Purpose

Advance the functional-preorder order-ideal branch while keeping
preorder-downward closure distinct from WP06's subset-downward
`IsIdealFamilyOn` predicate.

## Current substantive state

`UC-FRANKL` is open and `UC-P04` is open.

WP07 preserves historical source pin
`49c3f1d96ca8518d16e203fd0429ac1216838a4f` and selects
`kashiwabarakenji/avg-rare@21451877e9996a295bbc1ec25856d07fa302d48c`.
The two intervening commits are comment-only. MATHFORGE has admitted the exact
source provenance. Independent MATHSOLVE replay builds all 879 upstream jobs,
finds no active `sorry`/`admit` or explicit source `axiom`, and reports
`AvgRare.MainStatement.main_nds_nonpos` as depending on
`[propext, Classical.choice, Quot.sound]`.

D002 and D003 are checked in
`MathSolve/UnionClosed/FunctionalPreorderBridge.lean`.

D004 is now closed locally. The audited source theorem dependency cone is
compiled inside MATHSOLVE under `MathSolve/UnionClosed/AvgRarePort/`, with
module-path changes and bounded Lean-4.29 compatibility adaptations. The
external repository is not a build-time trust root.
`MathSolve/UnionClosed/FunctionalPreorderD004.lean` explicitly proves
carrier-preserving semantic correspondence and contains:

```lean
sourceShapedMainNDS : SourceShapedMainNDSStatement α
d004_averageRarity : D004AverageRarityStatement α
```

D005 is the next open restricted obligation.

## Authoritative pointers

- `grandchallenge/INTELLECT:CONSTITUTION.md`
- `grandchallenge/INTELLECT:governance/constitutional_authority_schedule.json`
- `grandchallenge/INTELLECT:governance/handoffs/README.md`
- `grandchallenge/MATHSOLVE:AGENTS.md`
- `grandchallenge/MATHSOLVE:domains/union_closed/WP07_functional_preorder_bridge/`
- `grandchallenge/MATHSOLVE:MathSolve/UnionClosed/FunctionalPreorderBridge.lean`
- `grandchallenge/MATHSOLVE:MathSolve/UnionClosed/FunctionalPreorderD004.lean`
- `grandchallenge/MATHSOLVE:MathSolve/UnionClosed/AvgRarePort/`
- `grandchallenge/MATHSOLVE:campaign_ledgers/UC-001/proof_obligation_dag.json`
- `grandchallenge/MATHCERT:governance/certification_routes.json`
- `grandchallenge/MATHFORGE:sources/UC-001/AVG_RARE_WP07_SOURCE_PROVENANCE.md`

## Smallest safe next tranche

Close WP07-D005 for the exact D003 class:

- prove functional-preorder ideal families are intersection-closed;
- define or verify the exact carrier-relative complement family;
- prove its union closure;
- prove complement frequency/cardinality identities;
- transport D004 average rarity to complement average abundance and the
  restricted Frankl half-frequency conclusion.

Do not route this through `IsIdealFamilyOn`; D002 established that such a
reuse is not valid in general.

## Material dependencies and boundaries

The D004 port is governed local source, but its provenance remains the selected
external revision. Any future modification to the vendored mathematical
statements requires a new source/semantic audit.

D005 remains restricted to complements of functional-preorder order-ideal
families. A theorem representing arbitrary union-closed families in this class
is not present. Therefore D005 cannot close `UC-P04` or `UC-FRANKL` by
implication.

MATHCERT adjudication must remain independent of MATHSOLVE construction.

## Reserved authority / stop conditions

Stop for a material source/theorem change, a checked failure of D003/D004
semantic correspondence, a material UC target change, a MATHCERT certification
boundary, or another reserved constitutional boundary. Do not stop merely
because D005 requires fresh complement lemmas or because Frankl's conjecture
remains open.
