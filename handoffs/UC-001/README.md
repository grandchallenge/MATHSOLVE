# UC-001 — Handoff

## Target repository and authority

Target work repository: `grandchallenge/MATHSOLVE`.

INTELLECT work-package phase: `not applicable`.

MATHSOLVE owns bounded theorem development. MATHFORGE owns external source and
provider provenance. MATHCERT alone owns certification. `UC-FRANKL` and
`UC-P04` remain outside any restricted-result promotion by implication.

## Purpose

Advance the functional-preorder order-ideal branch through an exact local
semantic bridge while keeping preorder-downward closure distinct from WP06's
subset-downward `IsIdealFamilyOn` predicate.

## Primary deliverable

A checked local WP07 theorem surface containing the finite semantic obstruction,
the exact functional-preorder family predicate, and a proof-bearing bridge from
the source-shaped NDS theorem interface to local average rarity.

## Material acceptance criteria

- D001 binds and independently builds the selected `avg-rare` revision.
- D002 is a checked three-element-chain obstruction with no proof placeholders.
- D003 represents exactly the finite functional-preorder order-ideal family.
- D004 is frozen in local UC vocabulary and has at least one substantive checked semantic bridge.
- No result is promoted beyond its restricted class.

## Current substantive state

`UC-FRANKL` is open and `UC-P04` is open. WP04 remains qualified only for its
existing bounded claims. WP06 has a checked restricted local ideal-family
surface; those declarations are not silently added to `MC-ROUTE-UC-001`.

WP07 uses historical source pin
`49c3f1d96ca8518d16e203fd0429ac1216838a4f`. The selected current source is
`kashiwabarakenji/avg-rare@21451877e9996a295bbc1ec25856d07fa302d48c`.
The two intervening commits are comment-only. D002/D003 and the first D004
bridge are implemented on the active WP07 branch and require exact CI replay
before protected integration.

## Authoritative pointers

- `grandchallenge/INTELLECT:CONSTITUTION.md`
- `grandchallenge/INTELLECT:governance/constitutional_authority_schedule.json`
- `grandchallenge/INTELLECT:governance/handoffs/README.md`
- `grandchallenge/MATHSOLVE:AGENTS.md`
- `grandchallenge/MATHSOLVE:domains/union_closed/WP07_functional_preorder_bridge/`
- `grandchallenge/MATHSOLVE:MathSolve/UnionClosed/FunctionalPreorderBridge.lean`
- `grandchallenge/MATHSOLVE:campaign_ledgers/UC-001/proof_obligation_dag.json`
- `grandchallenge/MATHCERT:governance/certification_routes.json`
- `grandchallenge/MATHFORGE:sources/UC-001/AVG_RARE_WP07_SOURCE_PROVENANCE.md`

## Smallest safe next tranche

Finish exact-head CI and source-build replay. Then transport or locally reprove
`main_nds_nonpos` against the checked D003 semantics. After local D004 closes,
prove the corresponding complement result as D005 and only then compare the
restricted class against WP05 / `UC-P04`.

## Material dependencies and boundaries

The external repository remains provenance until its theorem is transported
into the local trusted boundary. The selected source uses Lean 4.23.0 and
mathlib v4.23.0; MATHSOLVE uses its own current toolchain, so semantic transport
must not rely on definitional identity across projects. MATHCERT adjudication
must remain independent of MATHSOLVE construction.

## Reserved authority / stop conditions

Stop for a material source/theorem change, an exact semantic incompatibility,
a checked failure of the D003 representation, a material UC target change, a
MATHCERT certification boundary, or another reserved constitutional boundary.
Do not stop merely because the source is external, the proof requires several
transport lemmas, or Frankl's conjecture remains open.

## Notes intentionally omitted

This handoff intentionally omits generic constitutional doctrine, the generic
handoff contract, WP01-WP07 history, and procedural evidence preserved in the
work-package and CI records.
