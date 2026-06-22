# WP07 Next Executable Step

Date: 2026-06-22

## Selected Route

Proceed with the functional-preorder branch through an audit-first bridge path.
Do not present the branch as a direct consumer of the WP06
`localIdealFamily_complement_frankl` theorem.

## Step 1: External Build Audit

Create a MATHSOLVE external-audit note for:

```text
repository: https://github.com/kashiwabarakenji/avg-rare
observed branch: main
observed commit: 49c3f1d96ca8518d16e203fd0429ac1216838a4f
observed date: 2026-06-22
```

The audit should record:

- `lean-toolchain`;
- `lakefile.lean` dependencies;
- `lake update` and `lake build` result;
- theorem names for the source main theorem and secondary theorem;
- whether any `sorry`, `admit`, or new axioms appear in the trusted path.

## Step 2: First Local Formal Target

After the external audit, add a tiny local obstruction theorem showing that
functional-preorder order ideals are not automatically `IsIdealFamilyOn`.

The intended finite example is the three-element functional chain:

```text
f(a) = b, f(b) = c, f(c) = c
order ideals: empty, {a}, {a,b}, {a,b,c}
proper ideal: {a,b}
bad subset: {b}
```

The theorem should establish that the induced family of order ideals fails the
proper-member subset-downward condition required by `IsIdealFamilyOn`.

## Step 3: Bridge Predicate Design

Only after Step 2, define a local predicate for finite functional-preorder
order-ideal families over `Family alpha`. It should be separate from
`IsIdealFamilyOn` and should expose the exact data needed for a later average
rarity theorem.

## Acceptance Criteria

- MATHSOLVE validation passes.
- The WP07 ledger remains presentation/source assessment only.
- No MATHCERT theorem is claimed for WP07 until a local Lean file compiles with
  no `sorry`, `admit`, or new axioms.
- The external repository remains provenance until independently audited and,
  if needed, ported.

