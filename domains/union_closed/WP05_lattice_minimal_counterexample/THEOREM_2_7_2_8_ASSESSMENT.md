# Theorem 2.7 and Corollary 2.8 Assessment

Source: Christopher Bouchard, *On the lattice formulation of the union-closed
sets conjecture*, arXiv:2503.00277v1.

External source: Ivan Rival, *Lattices with doubly irreducible elements*,
Canadian Mathematical Bulletin 17 (1974), 91-95.

## Source Shape

Bouchard's Theorem 2.7 states that if `j` is join-irreducible in a
minimum-cardinality finite-lattice counterexample `L_tilde`, then

```text
|up(j)| > ell(L_tilde),
```

where `ell(L)` is the length of `L`, defined as one less than the maximum size
of a chain in `L`.

Bouchard's proof uses Rival's Theorem 1:

```text
|L| >= 2 * (ell(L) + 1) - |Irr(L)|
```

for finite-length lattices, where `Irr(L)` is the set of doubly irreducible
elements. Together with the checked theorem `UC-WP05-L007`, which gives
`|Irr(L_tilde)| <= 1`, this yields `|L_tilde| / 2 > ell(L_tilde)`. The
minimum-counterexample condition then gives `|up(j)| > |L_tilde| / 2`, proving
Theorem 2.7.

Corollary 2.8 states that any doubly irreducible element in `L_tilde` lies
strictly below at least one doubly reducible element. The source proof argues
that if every non-top element above a doubly irreducible `x` were
meet-irreducible, then the whole upper cone above `x` would be a chain. Since
`x` is not bottom, this chain extends downward to a larger chain through
bottom, giving `|up(x)| <= ell(L_tilde)`, contradicting Theorem 2.7.

## Certification Boundary

Theorem 2.7 and the non-top form of Corollary 2.8 are now promoted to
unconditional Lean theorems. Rival's Theorem 1 dependency has been formalized
locally as `UC-WP05-L019` in
`MATHCERT/MathCert/Domains/UnionClosed/RivalLength.lean`.

The endpoint convention needs explicit handling. Rival counts bottom as
join-irreducible and top as meet-irreducible by definition. Bouchard's local
convention, and mathlib's `SupIrred`/`InfIrred`, exclude those endpoints in the
minimum counterexample because bottom is meet-reducible (`UC-WP05-L001`) and top
is join-reducible (`UC-WP05-L005`). Therefore the set of doubly irreducible
elements in the minimum counterexample is unaffected by the convention
difference.

## Lean Feasibility

Mathlib provides `IsChain`, `IsMaxChain`, and `Flag` in
`Mathlib.Order.Preorder.Chain`. The local WP05 layer now adds a small
`LatticeLength.lean` interface:

```text
latticeLength L := max { C.card | C is a finite chain in L } - 1
```

It includes:

1. every chain has cardinality at most `latticeLength L + 1`;
2. a witnessed maximal-size chain realizes `latticeLength L + 1`;
3. a conditional theorem:

   ```text
   RivalBound L ->
     IsMinimumCounterexample L ->
       SupIrred j ->
         latticeLength L < upperConeCard j
   ```

The conditional Theorem 2.7 wrapper remains checked as `UC-WP05-L017`. It is
mostly arithmetic plus the checked uniqueness of doubly irreducible elements.
The promoted theorem `UC-WP05-L017A` supplies `RivalBound` via
`minimumCounterexample_rivalBound`.

The conditional non-top form of Corollary 2.8 remains checked as
`UC-WP05-L018`. The promoted theorem `UC-WP05-L018A` supplies `RivalBound`
via `minimumCounterexample_rivalBound`. The proof packages both pieces of
upper-cone infrastructure:

1. if every non-top element in the principal upper cone above `x` is
   inf-irreducible, then that upper cone is a chain;
2. if a nonbottom element has a chain upper cone, adjoining bottom gives
   `upperConeCard x <= latticeLength L`.

The local statement asks for a non-top doubly reducible witness. This matches
the source proof and avoids endpoint-convention trivialization under mathlib,
where top is not `InfIrred`.

## Completed Route

This route has now been completed for Theorem 2.7 and Corollary 2.8:

- `MATHCERT/MathCert/Domains/UnionClosed/LatticeLength.lean` defines finite
  chain cardinalities and `latticeLength`;
- `RivalBound L` records Rival's inequality in subtraction-free form;
- `UC-WP05-L017` proves the conditional Theorem 2.7 wrapper:
  `IsMinimumCounterexample L -> RivalBound L -> SupIrred j ->
  latticeLength L < upperConeCard j`;
- `UC-WP05-L018` proves the conditional non-top Corollary 2.8 wrapper.
- `MATHCERT/MathCert/Domains/UnionClosed/RivalLength.lean` defines
  source-style endpoint-inclusive irreducibility, proves Rival's finite lattice
  inequality as `rival_length_bound_source`, and proves
  `minimumCounterexample_rivalBound`.
- `UC-WP05-L017A` proves the unconditional Theorem 2.7 wrapper:
  `IsMinimumCounterexample L -> SupIrred j ->
  latticeLength L < upperConeCard j`.
- `UC-WP05-L018A` proves the unconditional non-top Corollary 2.8 wrapper.
