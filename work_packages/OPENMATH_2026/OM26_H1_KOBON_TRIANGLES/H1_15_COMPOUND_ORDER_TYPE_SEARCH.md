# H1-15 — compound order-type construction search for score 94

**Tracker:** #955
**Protected predecessor:** `MATHSOLVE/main@5c11f38912d96b63e42340d3207a2467be8b9441`
**Seed:** `RH_BADER_PROJECTIVE_NOPARALLEL_093`
**External proposal generator:** `alejandrozu/kobon-proof@22d1165f6c455fe45e461baef4410f6d5c78a014`
**State:** COMPLETE__NO_94_FOUND__BOUNDED_NEGATIVE_ONLY

## Purpose

H1-13 and H1-14 showed that the protected 93 arrangement is not improved by the previously tested local-wall, two-line, topology/concurrency, or exact nearest-event-cell neighborhoods.

H1-15 therefore changes the discrete move family rather than increasing the continuous parameter count inside those exhausted neighborhoods.

The central observation is that every one-step projective mutation available at the protected 93 seed initially loses affine triangles. A search that insists on monotone score, or that prunes once the score falls more than a few points, can therefore miss a multi-move recovery path.

## Search family

The search uses the pinned external projective oriented-matroid machinery only as a proposal generator.

For each of the 18 arrangement lines in turn, that line is chosen as an **anchor**. A macro may then perform a sequence of projective triangular-cell mutations satisfying:

- any number of mutations whose defining triple contains the anchor line, up to the declared depth;
- at most one off-anchor bridge mutation;
- no repeated determinant flip within one macro;
- no affine-score drop cutoff.

The beam width is 256 and maximum macro depth is 10. Ranking uses exact affine triangle score first, a small projective-face term, and deterministic seeded noise only to diversify tied recovery paths.

This is deliberately complementary to H1-13 tranche 3, whose beam had width 16, depth 12, and pruned states below `93-4`.

## Exact promotion rule

A combinatorial state is not a candidate.

Only an endpoint with combinatorial affine score at least 94 is eligible for the pinned external exact straight-line reconstruction. Any successful reconstruction must then be converted back to the GCL hill convention and independently replayed by the protected direct-interior oracle and AutoLab before candidate-ladder promotion.

No such endpoint occurred in this tranche, so no realization or promotion call was warranted.

## Bounded execution

The completed deterministic macro pass used:

```text
anchors                 18 / 18
beam width              256
maximum depth            10
off-anchor bridge budget 1
seed                     2026100701
score-drop cutoff        none
```

The exact durable receipt records:

```text
nodes visited            38,718
mutation transitions     631,968
initial affine score     93
best combinatorial score 93
best realized score      93
endpoints >=94           0
realization attempts     0
```

Thus this broader compound order-type neighborhood did not produce a 94 proposal.

## Interpretation

This closes one specific concern left by H1-13/H1-14: the failure of the earlier searches was not merely caused by their refusal to traverse a deeper score valley inside a single anchor-line macro with one bridge mutation.

It does **not** exhaust all order types, all compound mutations, all bridge counts, or all nonsimple arrangements. A successful 94 construction may require a qualitatively different global rearrangement, more than one off-anchor bridge, or a seed not connected to the protected 93 arrangement through this bounded macro family.

The campaign-best observed construction therefore remains 93.

## Reproduction

The source lock is recorded in `H1_15_COMPOUND_ORDER_TYPE_SOURCE.json`.

The proposal search is:

```text
search_94_compound_order_type.py
```

The durable result is:

```text
H1_15_COMPOUND_ORDER_TYPE_RECEIPT.json
```

The GitHub workflow reacquires the pinned external source, recreates the exact pairwise-nonparallel 93 seed in the external convention, runs the bounded macro search, and triggers independent promotion replay only if a score-94-or-better exact reconstruction appears.

## Claim boundary

This is bounded negative construction-route evidence only. It is not an upper bound, an infeasibility theorem for 94, proof that 93 is optimal, a novelty or priority claim, competition acceptance, or MATHCERT certification.
