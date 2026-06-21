# Proofs And Computations

## Proof Route

The WP06 proof is a formal Lean proof, not a finite search. The essential route
is:

1. Start with a local ideal family `F` on finite ground `U`.
2. Translate `F` to a ported predicate-style ideal structure.
3. Prove NDS nonpositivity for every ported ideal by induction on the ground
   cardinality.
4. Convert NDS nonpositivity into average rarity for `F`.
5. Pass through complements to obtain a union-closed Frankl-abundant family.

## Mathematical Action

The induction step uses two derived families after choosing a vertex:

- the trace on `ground.erase v`;
- the contraction family of members containing `v`, with `v` erased.

The exact trace-difference formula accounts for the change in NDS between the
original ideal and its trace. The singleton/contraction branch supplies the
remaining inequality needed to keep the induction closed.

## Checked Arithmetic Boundary

The proof does not use floating-point or heuristic computation. Its arithmetic
is finite-cardinality and integer/rational inequality reasoning inside Lean.

The related exact finite replays in MATHCERT remain separate infrastructure:

- union-closed universe audit for `n <= 4`;
- finite-lattice enumeration certificate for sizes `4..7`.

Those replays are regression and certification gates, not the proof of WP06.

## Reproducibility Commands

Run from `MATHCERT`:

```powershell
.\ci\check_lean.ps1
```

Targeted checks:

```powershell
lake env lean MathCert/Domains/UnionClosed/IdealFamilyBridge.lean
lake env lean MathCert/Domains/UnionClosed/IdealFamilyNDSEndgame.lean
lake env lean MathCert/Domains/UnionClosed/IdealFamilyDuality.lean
```

Run from `MATHSOLVE`:

```powershell
python ci/validate_solve.py
```

## Presentation Summary

The proof should be taught as one controlled mechanism:

```text
global average rarity is hard
  -> NDS is the right global invariant
  -> trace/contraction explains one induction step
  -> complement turns rarity into abundance
```

