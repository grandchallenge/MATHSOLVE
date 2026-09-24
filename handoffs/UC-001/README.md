# UC-001 — Handoff

## Target repository and authority

Target work repository: `grandchallenge/MATHSOLVE`.

MATHSOLVE owns bounded theorem development. MATHFORGE owns external-source
provenance. MATHCERT alone owns certification. `UC-P04` and `UC-FRANKL`
remain outside restricted-result promotion by implication.

## Protected WP07 theorem spine

WP07-D002 through D005 have protected Lean surfaces:

- `MathSolve/UnionClosed/FunctionalPreorderBridge.lean`
- `MathSolve/UnionClosed/FunctionalPreorderD004.lean`
- `MathSolve/UnionClosed/FunctionalPreorderD005.lean`
- `MathSolve/UnionClosed/AvgRarePort/`

D004 proves average rarity for the exact D003 functional-preorder class.

D005 proves that the carrier-relative complements are union-closed and
Frankl-abundant without using WP06 `IsIdealFamilyOn`.

The principal theorem is:

```lean
d005_complement_frankl
```

The exact restricted claim has been independently adjudicated by MATHCERT:

- disposition: `QUALIFIED`
- protected merge: `245a2f395c358a8d11941e7085512a2e53751619`
- adjudication record blob: `00c37d4a379811b52e7f44e6d384adc75e2fc850`

## UC-P04 / WP08 state

### D001: exact representation route refuted

Protected theorem surface:

```text
MathSolve/UnionClosed/FunctionalPreorderP04.lean
```

Key endpoint:

```lean
p04_no_universal_exact_functionalPreorder_representation
```

Exact D003 complement families are both union- and intersection-closed. The
explicit union-closed family

```text
{ ∅, {a,b}, {b,c}, {a,b,c} }
```

is not intersection-closed, so universal exact D003 representation is false.

### D002: arbitrary finite poset extension

The functional-preorder restriction is not required for the Frankl-facing
half-frequency conclusion.

New theorem surface:

```text
MathSolve/UnionClosed/PosetIdealP04.lean
```

For any nonempty finite carrier in any partial order, a maximal carrier element
occurs in at most half of all downward order ideals. The proof injects ideals
containing that maximal element into ideals omitting it by erasure.

Principal endpoints:

```lean
posetIdealFamily_exists_rare
posetIdeal_complement_frankl
```

Thus complements of all finite-poset order ideals satisfy Frankl abundance.

This does not assert an average-rarity theorem for arbitrary posets.

## Exact logical boundary

The universal complement duality remains:

```text
union-closed family on U
  <-> intersection-closed carrier-relative complement on U
```

for carried families.

The live gap is now:

```text
finite-poset ideal closure systems
  ?-> arbitrary finite closure systems.
```

The next route is closure operators / finite implication bases. Poset ideals
encode unary order implications; arbitrary closure systems can require
genuinely non-unary premises.

In parallel, any WP05 bridge must preserve both abstract lattice order and the
ground-element incidence map. Abstract lattice structure alone does not carry
the Frankl frequency statistic.

## Claim firewall

```text
UC-WP07-P006 = QUALIFIED_PROTECTED
WP08-D001 = CLOSED_NEGATIVE
WP08-D002 = CLOSED_LOCAL
UC-P04 = OPEN
UC-FRANKL = OPEN_PROBLEM
MATHEMATICAL_TARGET_PROVED = false
PROMOTION_ELIGIBLE = false
```

## Stop boundaries

Stop for a failed exact-head replay, a material theorem-statement change, a
reserved certification/governance action, or a genuine mathematical boundary.
Do not stop merely because the universal closure-system extension remains open.
