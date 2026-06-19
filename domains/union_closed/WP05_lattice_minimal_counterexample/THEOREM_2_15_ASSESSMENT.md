# Theorem 2.15 Assessment

Source: Christopher Bouchard, *On the lattice formulation of the union-closed
sets conjecture*, arXiv:2503.00277v1.

## Source Shape

Bouchard's Theorem 2.15 concerns a subposet `L'` of a minimum-cardinality
counterexample `L_tilde`. The subposet is assumed to be a lattice in its own
right and to satisfy one of two alternative criteria:

1. `L'` has cardinality strictly between `3` and `8`;
2. `L'` has cardinality strictly between `2` and `|L_tilde| - 2`, and some
   dual atom `d` of `L_tilde` satisfies `d <= 1_{L'}`.

The conclusion is a boundary-touch statement: some non-endpoint element of
`L'` either covers or is covered by an element of `L_tilde` that is outside
`L'`.

## Certification Split

The theorem should not be promoted as one undifferentiated Lean target. Its two
source branches have different certification requirements.

### Branch (i): small finite lattices

The proof cites Kyuno and Heitzig-Reinhold enumeration data for unlabeled
lattices with `4`, `5`, `6`, and `7` elements, then observes from the diagrams
that every such lattice has at least two doubly irreducible elements.

This is now internally replay-certified as `UC-WP05-C016`. The replay verifier
enumerates all strict partial orders on `{0,...,n-1}` whose labels are a linear
extension, checks the lattice property by pairwise joins and meets,
canonicalizes the resulting reflexive orders under all relabelings, and proves
by exhaustive exact computation that:

```text
for every finite lattice L,
  4 <= Fintype.card L -> Fintype.card L <= 7 ->
    exists x y, x != y /\ SupIrred x /\ InfIrred x /\
      SupIrred y /\ InfIrred y
```

The verifier obtains unlabeled lattice counts `2`, `5`, `15`, and `53` for
sizes `4`, `5`, `6`, and `7`, and finds zero violations. This certifies the
finite enumeration fact at Level 2; it is not itself a Lean-kernel theorem.

The Lean transfer step is now checked as `UC-WP05-L016`: if an embedded finite
lattice subposet of a minimum counterexample contains two distinct internally
doubly irreducible elements, then it must touch the ambient boundary. The proof
uses the no-boundary transfer lemmas for both `SupIrred` and `InfIrred`, then
contradicts the checked uniqueness of ambient doubly irreducible elements.

### Branch (ii): dual-atom cardinality gap

The second branch is a deletion/minimality argument and has now been checked as
`UC-WP05-L015`. Its proof splits on whether `1_{L'}` is join-reducible inside
`L'`.

If `1_{L'}` is join-reducible, the candidate smaller lattice is `L'` itself.
If `1_{L'}` is join-irreducible, the candidate smaller lattice is
`L' \ {1_{L'}}`, using Lemma 1.2-style deletion. The source then compares
upper-cone sizes using the dual atom below `1_{L'}` and the strict cardinality
gap `|L'| < |L_tilde| - 2`.

This branch required infrastructure that was not present in the earlier Lean
layer: arbitrary finite lattice subposets with induced ambient order,
boundary-cover predicates, and transfer lemmas connecting irreducibility and
upper-cone counts between `L'` and `L_tilde`.

## Lean Infrastructure Needed

The current WP05 machinery handles deletion subtypes and upper intervals. It
does not yet provide a reusable representation for an arbitrary finite
sublattice/subposet whose lattice operations may be internal to the subposet.

The formalization added:

1. A finite induced subposet/sub-lattice wrapper. The checked implementation
   uses an order embedding `K ↪o L`, with carrier `Finset.univ.image e`, to
   avoid subtype typeclass diamonds while preserving the induced-order
   meaning.
2. Accessors for the internal bottom and top of `L'`, written in statements as
   `0_{L'}` and `1_{L'}`.
3. An ambient boundary-touch predicate:

   ```text
   exists x in L',
     x != 0_{L'} /\ x != 1_{L'} /\
       exists y notin L', (y ⋖ x \/ x ⋖ y)
   ```

4. A no-boundary transfer lemma: if an internal non-endpoint of `L'` does not
   cover or get covered by outside elements, then relevant internal
   irreducibility information survives in the ambient lattice.
5. Cone-loss lemmas for branch (ii), separating the `1_{L'}` join-reducible
   and join-irreducible cases.

These items are now checked in Lean for branch (ii) as `UC-WP05-L015`.

## Recommended Formalization Route

Do not make full Theorem 2.15 the next Lean target.

The branch (ii) theorem has now been formalized as `UC-WP05-L015`. The proof
argues by contradiction from no boundary touch, transfers internal
join-irreducibles through the order embedding, bounds ambient cone loss by one
or two points depending on whether the internal top is join-irreducible, and
then contradicts minimum cardinality.

Keep branch (i) behind the finite-lattice certificate boundary now recorded as
`UC-WP05-C016`, paired with the checked Lean transfer theorem `UC-WP05-L016`.
The certificate is independent of Bouchard's prose and replays the `4..7`
lattice classification claim locally.

The ideal-family branch remains deferred. If activated, it should enter
through a translation layer to the existing public Lean development rather than
through a duplicate local formalization.

## Promotion Boundary

`UC-WP05-C015` is now hybrid-certified as a package result, not as a single
Lean theorem. Its branch (ii) has been promoted to the checked Lean claim
`UC-WP05-L015`. Its small-lattice branch combines the exact replay claim
`UC-WP05-C016` with the checked Lean transfer theorem `UC-WP05-L016`.

Promotion to a single Lean theorem remains deferred unless the finite
enumeration for sizes `4..7` is internalized in Lean.
