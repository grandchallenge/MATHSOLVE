# UC-001 — Handoff

## Target repository and authority

Target work repository: `grandchallenge/MATHSOLVE`.

MATHSOLVE owns bounded theorem development. MATHFORGE owns external-source
provenance. MATHCERT alone owns certification. `UC-P04` and `UC-FRANKL`
remain outside restricted-result promotion by implication.

## Protected predecessor spine

WP07-D005 proves the restricted functional-preorder complement theorem and is
independently MATHCERT-qualified.

WP08 then advances the `UC-P04` structural programme:

- D001: exact D003 representation is not universal;
- D002: arbitrary finite-poset ideal complements satisfy the Frankl-facing
  half-frequency conclusion;
- D003: arbitrary finite closure systems admit an exact closure-operator /
  finite-implication representation, and the first genuinely non-unary
  obstruction is formalized.

## WP08-D003 theorem surface

```text
MathSolve/UnionClosed/ClosureImplicationP04.lean
```

Principal general endpoints:

```lean
closureOf_idempotent
closureOf_mem_of_closureSystem
mem_iff_closureOf_eq
closureSystem_mem_iff_models_canonicalBasis
unaryModelFamilyOn_unionClosed
unaryImplicationRepresentable_unionClosed
```

Principal bounded non-unary endpoints:

```lean
binaryImplicationClosure_characterization
binaryImplicationClosure_isClosureSystem
binaryImplicationClosure_not_unionClosed
binaryImplicationClosure_not_unaryRepresentable
binaryImplicationClosure_forcedConclusion_erasure_fails
binaryImplicationClosure_exists_rare
binaryImplicationClosure_complement_frankl
```

## Exact structural lesson

The live hierarchy is now:

```text
functional-preorder ideals
        subset
finite-poset ideals / unary order implications
        subset
finite closure systems / arbitrary finite implications.
```

The second inclusion is strict. The checked binary rule

```text
{a,b} -> c
```

produces a closure system that is not union-closed, hence cannot be represented
by unary implications.

It also shows why the D002 erasure mechanism does not generalize verbatim:
erasing the forced conclusion `c` from the full closed set leaves the
nonclosed premise `{a,b}`.

This bounded obstruction does not refute the desired rare-element conclusion;
the same example still has a rare element and a Frankl-abundant complement.

## Governed replay

WP08 now has a dedicated exact-head Lean replay:

```text
.github/workflows/uc-wp08-closure-system.yml
```

The D001-D003 modules are also imported by `MathSolve.lean`. Enabling this
replay exposed and repaired latent D001/D002 compile defects before D003
integration.

## Next governed mathematical tranche: WP08-D004

Build an incidence-preserving interface between the closure-system/implication
surface and the protected WP05 minimum-counterexample lattice spine.

The bridge object must retain:

1. finite lattice / closure order;
2. explicit ground carrier;
3. the incidence relation `x in S`; and
4. exact frequency counts derived from that incidence relation.

Do not replace a concrete family by an abstractly isomorphic lattice and infer
frequency statements without an explicit incidence transport theorem.

The first D004 question is: which protected WP05 minimum-counterexample
conditions constrain the canonical implication basis, especially non-unary
premises?

## Claim firewall

```text
WP08-D001 = CLOSED_NEGATIVE
WP08-D002 = CLOSED_LOCAL
WP08-D003 = CLOSED_LOCAL
WP08-D004 = OPEN_NEXT

UC-P04 = OPEN
UC-FRANKL = OPEN_PROBLEM
MATHEMATICAL_TARGET_PROVED = false
PROMOTION_ELIGIBLE = false
```

## Stop boundaries

Stop for a failed exact-head replay that cannot be repaired within scope, a
material theorem-statement change, a reserved certification/governance action,
or a genuine mathematical/evidentiary boundary. Do not stop merely because the
universal closure-system rare-element theorem remains open.
