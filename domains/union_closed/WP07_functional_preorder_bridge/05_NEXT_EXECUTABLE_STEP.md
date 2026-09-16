# WP07 Next Executable Step

Date: 2026-09-16

## Current frontier

D001 source/build audit, D002 semantic obstruction, and D003 local predicate are
closed in the current integration package. The first D004 semantic bridge is
also checked. The missing mathematical theorem is now precise:

```lean
SourceShapedMainNDSStatement α
```

which states NDS nonpositivity for every local source-shaped finite functional
preorder. Once this theorem is proved, `sourceShapedMainNDS_implies_D004`
discharges the exact local average-rarity target.

## Selected route: smallest proof-bearing D004 transport

Do not import the external repository as authority and do not copy unrelated
infrastructure. Use the audited upstream proof only as provenance and extract
the smallest dependency cone needed to establish the local NDS theorem.

The next tranche should proceed in this order:

1. Map the exact upstream dependencies of
   `AvgRare.MainStatement.main_nds_nonpos`, beginning with
   `Reduction.main_nds_nonpos_of_secondary` and the secondary theorem actually
   consumed by that proof.
2. For each required declaration, decide whether the local D003 surface already
   states the same object, whether a small semantic lemma is sufficient, or
   whether a proof component must be ported/reproved.
3. Prefer semantic lemmas for family membership, cardinality, total edge size,
   degree/frequency, and NDS before porting structural machinery.
4. Prove `SourceShapedMainNDSStatement` directly, or replace it only with a
   proposition proved equivalent to it inside the local trusted boundary.
5. Close D004 locally before beginning D005 complement duality.

A fresh proof is also admissible if it is materially smaller than the source
transport. The criterion is proof economy inside the local trusted boundary,
not textual similarity to the external repository.

## D004 acceptance criteria

- the exact D003 predicate remains unchanged unless a checked semantic defect is found;
- a local theorem proves `SourceShapedMainNDSStatement` or directly proves `D004AverageRarityStatement`;
- no `sorry`, `admit`, or new unexplained axiom is introduced;
- source definitions and local definitions are not conflated by name alone;
- NDS normalization and family-cardinality semantics remain explicit;
- the external repository remains provenance, not an imported trust root;
- `UC-P04` and `UC-FRANKL` remain open.

## After D004

Only after local D004 closure, prove D005 complement duality for the exact D003
class. Then compare the resulting restricted complement-abundance theorem
against WP05 structural conditions and the universal `UC-P04` obstruction.
MATHCERT receives a bounded exact handoff only after a new substantive local
claim exists.
