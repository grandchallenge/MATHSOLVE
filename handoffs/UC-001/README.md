# UC-001 — Handoff

## Target repository and authority

Target work repository: `grandchallenge/MATHSOLVE`.

MATHSOLVE owns bounded theorem development. MATHFORGE owns external-source
provenance. MATHCERT alone owns certification. `UC-P04` and `UC-FRANKL`
remain outside restricted-result promotion by implication.

## Current protected theorem spine

WP07-D002 through D005 now have local Lean surfaces:

- `MathSolve/UnionClosed/FunctionalPreorderBridge.lean`
- `MathSolve/UnionClosed/FunctionalPreorderD004.lean`
- `MathSolve/UnionClosed/FunctionalPreorderD005.lean`
- `MathSolve/UnionClosed/AvgRarePort/`

D004 proves average rarity for the exact D003 functional-preorder class.

D005 proves, without using WP06 `IsIdealFamilyOn`, that these order-ideal
families are intersection-closed and hence that their carrier-relative
complements are union-closed. Finite double counting plus D004 supplies a rare
ground element; exact complement-frequency arithmetic turns that element into
an abundant supported element.

The principal D005 theorem is:

```lean
d005_complement_frankl
```

with the restricted representation wrapper:

```lean
IsComplementOfFunctionalPreorderIdealFamily
complementOfFunctionalPreorderIdealFamily_frankl
```

## Exact logical boundary

The checked direction is:

```text
functional-preorder ideal-family representation
  -> complement is union-closed
  -> complement is nontrivial
  -> complement is Frankl-abundant.
```

The reverse/universal representation direction is not proved.

No theorem presently establishes that an arbitrary finite union-closed family is
the complement of an exact D003 family. This is the live `UC-P04`-side
boundary.

## Next governed action

After protected MATHSOLVE integration, provide MATHCERT a bounded exact handoff
for independent adjudication of D005. Certification must not broaden the
hypothesis or imply `UC-P04` or `UC-FRANKL`.

In parallel, compare the explicit D005 representation predicate with the WP05
structural ledger to determine whether it sharpens, subsumes, or remains
orthogonal to the current universal obstruction.

## Claim firewall

```text
WP07-D005 = CLOSED_LOCAL
UC-P04 = OPEN
UC-FRANKL = OPEN_PROBLEM
MATHEMATICAL_TARGET_PROVED = false
PROMOTION_ELIGIBLE = false
```

## Stop boundaries

Stop for a material change to the exact D003/D004/D005 theorem statements, a
failed exact-head replay, a MATHCERT certification decision, a material target
change, or another reserved constitutional boundary. Do not stop merely because
the universal representation problem remains open.
