# H1-12 q=5 saturation/extreme-core reduction

**State:** `SOLVE_SOURCE_CONDITIONAL_GEOMETRIC_REDUCTION__FINITE_REPLAYED__NOT_CERTIFIED`

## Scope

Continue from the protected q=5 profile reduction. The only surviving multiplicity profiles are

```
33333 with D2 in 3..10
33334 with D2 in 5..9
33344 with D2 in 6..7.
```

This tranche combines those finite states with the protected saturated-core geometry.

## 1. Saturated cores are non-extreme

A core of multiplicity `r` is saturated when every one of its `2r` radial elementary segments is shared:

```
d1(v)+d2(v)=2r.
```

The protected extreme-core lemma proves, conditional on the named local no-long-run fan premise:

```
a saturated core cannot be an extreme point of the finite core set.
```

Hence, for a noncollinear set of five cores, at least three cores are extreme and at most two cores can be saturated.

## 2. Dense D2 forces noncollinearity

Five collinear core points can contribute at most four elementary core-to-core intervals on their common line: the intervals between consecutive points.

Therefore

```
D2 >= 5
```

forces the five-core set to be noncollinear.

This applies to every protected `33334` and `33344` state, and to every `33333` state with `D2>=5`.

The `33333` states at `D2=3,4` do not require this observation; the finite replay already shows they contain at most one saturated core.

## 3. Exact minimum saturation counts

The companion replay reconstructs the protected q=5 state space but retains one additional local bit:

```
saturated(v) <=> d1(v)+d2(v)=2r_v.
```

For every multiplicity placement and D2 graph, it asks whether the defect and clean-line charge inequalities admit a sector-consistent local state with a given total saturation count.

The minimum saturation counts by D2 are:

### Profile 33333

| D2 | minimum saturated cores |
|---:|---:|
| 3 | 0 |
| 4 | 1 |
| 5 | 1 |
| 6 | 2 |
| 7 | 2 |
| 8 | 3 |
| 9 | 4 |
| 10 | 5 |

Thus every state with `D2>=8` has at least three saturated cores. Since `D2>=8` is noncollinear, these states are impossible.

The retained range is

```
33333: 3 <= D2 <= 7.
```

At the labeled graph-placement level, 595 states remain.

### Profile 33334

| D2 | minimum saturated cores |
|---:|---:|
| 5 | 2 |
| 6 | 2 |
| 7 | 3 |
| 8 | 4 |
| 9 | 5 |

All these core sets are noncollinear.

Therefore every state with `D2>=7` is impossible.

The retained range is

```
33334: D2 in {5,6}.
```

Across the five placements of the quadruple core, 300 labeled graph-placement states remain.

### Profile 33344

Every protected state has

```
D2 in {6,7}
```

and at least four saturated cores.

Since the core set is noncollinear, at most two saturated cores are possible.

Therefore

```
33344
```

is excluded completely.

## Result

Conditional on the named source-scoped local fan and clean-line charging premises, the q=5 residual is reduced to exactly

```
33333 with D2 in 3..7
33334 with D2 in {5,6}.
```

The live H1-12 residual is therefore:

1. q=5 in one of those two profiles; or
2. q>=6.

The companion replay `ci/validate_openmath_h1_12_q5_saturation.py` imports the protected q=5 sector option table, recomputes saturation counts, and applies only the at-most-two-saturated condition where noncollinearity is justified.

## Next step

Treat `33334` first. Its five-core graph has five or six D2 edges and at least two saturated cores. Quotient the remaining core graphs by permutation of the four triple cores, preserving the quadruple role, and derive the exact saturated-core location types.

Then treat `33333`.

Keep q>=6 separate.

## Claim boundary

The noncollinearity observation and finite saturation replay are independently reconstructed.

The reduction remains source-conditional because saturated-core non-extremality inherits the named local fan premise, and the predecessor q=5 state space inherits the clean-line charging map. This artifact does not prove `T<=94`, does not certify optimality of the 93 construction, and has no MATHCERT effect.
