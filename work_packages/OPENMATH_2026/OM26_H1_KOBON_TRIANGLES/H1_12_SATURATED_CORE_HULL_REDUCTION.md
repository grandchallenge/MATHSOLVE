# H1-12 saturated-core hull reduction

**State:** `SOLVE_SOURCE_CONDITIONAL_GEOMETRIC_REDUCTION__FINITE_REPLAYED__NOT_CERTIFIED`

## Scope

Continue from the protected four-core reduction for a normalized `n=18, T=95` arrangement.

The protected finite replay leaves five possible multiplicity profiles for exactly four finite multiple points:

```
3333, 3334, 3335, 3344, 3444.
```

This note removes the three densest profiles, conditional on the already named local fan premise.

## Saturated core

At an `r`-fold finite multiple point, call the core **saturated** when every one of its `2r` radial elementary segments is shared by two triangular faces. In the established notation this is

```
d1(v) + d2(v) = 2r.
```

Here `d1` counts shared radial segments whose other endpoint is ordinary, while `d2` counts those whose other endpoint is another finite multiple point.

The local fan premise retained from the protected source-scoped H1-12 evidence says:

> among the `2r` cyclic rays at an `r`-fold point, no block of `r-1` consecutive rays can all be counted by `d1`.

The convex-hull argument below is independently reconstructed; only that local fan premise retains source-conditional status.

## Lemma — a hull core cannot be saturated

Let `v` be a core point lying on the convex hull of the finite core set.

All other core points lie in a closed half-plane bounded by some supporting line through `v`. No two core-directed rays from `v` can be antipodal while `v` is an extreme point: antipodal core points would put `v` between them on their common line.

Because the finite set of `d2` rays contains no antipodal pair, the supporting direction can be perturbed slightly so that **all `d2` rays lie in one open half-plane through `v`**.

The complementary open half-plane contains exactly one ray from each of the `r` arrangement lines through `v`, hence exactly `r` consecutive radial rays in the cyclic order.

None of these `r` rays is a `d2` ray. If `v` were saturated, every remaining radial ray would be a `d1` ray. We would therefore obtain a block of `r` consecutive `d1` rays, in particular a block of `r-1` consecutive `d1` rays.

This contradicts the local fan premise.

Therefore:

```
a convex-hull core cannot be saturated.
```

## Corollary — at most one saturated core when D2 >= 5

With four core points and `D2>=5`, the core set cannot be collinear.

Indeed, on one straight line through four ordered core points there are only three elementary core-to-core intervals, namely the intervals between consecutive points. Hence a collinear four-core set can contribute at most three `D2` segments.

Thus for `D2>=5` the four core points are noncollinear. Their convex hull has at least three vertices, so at most one core point is strictly interior to the hull.

Since every saturated core must be non-hull by the lemma, a four-core state with `D2>=5` can contain **at most one saturated core**.

## Replay consequence

The protected q=4 finite enumerator records the following facts.

### Profile 3335

Every admissible arithmetic state has

```
D2 = 6
```

and all four cores are saturated.

This violates the at-most-one-saturated corollary. Therefore `3335` is excluded.

### Profile 3444

Every admissible arithmetic state has

```
D2 = 6
```

and all four cores are saturated.

Therefore `3444` is excluded.

### Profile 3344

Every admissible arithmetic state has `D2=5` or `D2=6`.

The exact replay shows that every such state has at least two saturated cores:

- for `D2=5`, exactly two cores are saturated in every surviving arithmetic state;
- for `D2=6`, every surviving arithmetic state has at least two saturated cores.

Therefore `3344` is excluded.

## Remaining four-core residual

Conditional on the named local fan premise, the four-core `T=95` residual is reduced from five multiplicity profiles to exactly

```
3333
3334.
```

The finite replay further records:

- `3333`: `1 <= D2 <= 6`, with at most one saturated core;
- `3334`: `3 <= D2 <= 5`, with at most one saturated core.

In particular, complete-core `D2=6` is no longer possible for `3334`.

The companion validator `ci/validate_openmath_h1_12_saturated_core.py` recomputes these consequences directly from the protected q=4 state enumerator.

## Claim boundary

This is a strict Solve-level residual reduction, not a hill-global upper bound and not a MATHCERT disposition.

The convex-hull argument is independently reconstructed. The conclusion remains source-conditional because it invokes the local no-long-run fan premise. The global clean-line/fan extraction used earlier in H1-12 also remains outside independent GCL certification.

No conclusion `T<=94` follows yet: the four-core profiles `3333` and `3334`, together with the `q>=5` residual, remain open.
