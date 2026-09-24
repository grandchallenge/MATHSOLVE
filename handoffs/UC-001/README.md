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

## UC-P04 successor state

The previously open exact-representation subroute is now formally refuted in
WP08.

New theorem surface:

```text
MathSolve/UnionClosed/FunctionalPreorderP04.lean
```

Key result:

```lean
p04_no_universal_exact_functionalPreorder_representation
```

Every exact D003 complement is closed under both union and literal
intersection. The explicit family

```text
{ ∅, {a,b}, {b,c}, {a,b,c} }
```

is union-closed but not intersection-closed, so it cannot have the exact D003
representation.

## Exact logical boundary

The live universal duality is instead:

```text
union-closed family on U
  <-> intersection-closed carrier-relative complement on U
```

with the carried-family hypothesis needed for exact involution.

If the original family contains `∅`, its complement is a finite closure
system. Functional-preorder ideal families are a special subclass of such
closure systems.

Therefore the next substantive UC-P04 problem is:

> extend the rare-element argument from functional-preorder closure systems to
> broader finite closure systems, while preserving ground-element incidence
> data strongly enough to interact with the WP05 lattice counterexample spine.

Abstract lattice structure alone is not sufficient: the concrete family
incidence map is part of the Frankl frequency statement.

## Claim firewall

```text
UC-WP07-P006 = QUALIFIED_PROTECTED
WP08_EXACT_REPRESENTATION_ROUTE = REFUTED
UC-P04 = OPEN
UC-FRANKL = OPEN_PROBLEM
MATHEMATICAL_TARGET_PROVED = false
PROMOTION_ELIGIBLE = false
```

## Stop boundaries

Stop for a failed exact-head replay, a material theorem-statement change, a
reserved certification/governance action, or a genuine mathematical boundary.
Do not stop merely because the universal closure-system extension remains open.
