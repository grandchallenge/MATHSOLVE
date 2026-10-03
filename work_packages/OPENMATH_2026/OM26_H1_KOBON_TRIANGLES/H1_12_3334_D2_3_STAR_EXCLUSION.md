# H1-12 q=4 profile 3334 — D2=3 star exclusion

**State:** `SOLVE_SOURCE_CONDITIONAL_GEOMETRIC_REDUCTION__FINITE_REPLAYED__NOT_CERTIFIED`

## Scope

Continue from the protected 3334 normal form for a normalized `n=18,T=95` arrangement with exactly four finite multiple points and multiplicities

```
(3,3,3,4).
```

The protected finite quotient shows that every `D2=3` state is a three-spoke star with

```
D1 = 11,
U = 0,
```

and a unique saturated degree-3 hub. Up to permutation of the three triple cores, there are two role-types:

1. a saturated triple hub;
2. a saturated quadruple hub.

This note excludes both role-types conditional on the already named local no-long-run fan premise and clean-line charging map.

The endpoint/transverse-line argument below is independently reconstructed.

## Lemma 1 — transverse line of a shared D1 segment

Let `HP` be a `D1` elementary segment from a multiple point `H` to an ordinary point `P`, and suppose `HP` is incident to triangular faces on both sides.

Exactly two arrangement lines pass through the ordinary point `P`:

- the hub line containing `HP`;
- one transverse line `m_P`.

Each of the two triangular faces incident to `HP` must use `m_P` as its side through `P`. Therefore `m_P` also contains the opposite endpoint on each of the two radial rays adjacent to `HP` in the cyclic order at `H`.

Consequently, if either adjacent radial ray is a `D2` spoke ending at a finite multiple point, then `m_P` contains a finite multiple point and is not clean.

Under the protected charging map, a `D1` segment can receive a clean-line charge only through its unique ordinary endpoint and its transverse line. Hence any such `D1` segment adjacent to a `D2` spoke is unavailable as a clean-line charge target.

## Case A — saturated quadruple hub

At a quadruple hub,

```
r = 4,
d2 = 3,
d1 = 5.
```

Saturation means all eight radial elementary segments are shared by two triangular faces.

The named local fan premise forbids a block of `r-1=3` consecutive `D1` rays. With five `D1` rays and three `D2` rays on an eight-cycle, this implies every `D1` ray is adjacent to at least one `D2` ray: otherwise that ray would be the middle of three consecutive `D1` rays.

By Lemma 1, all five hub `D1` segments are unavailable as clean-line charge targets.

For profile 3334,

```
I = 13.
```

The three star spokes give

```
h <= I-D2 = 10,
```

so there are at least

```
18-h >= 8
```

clean lines.

But `U=0`, and only the `11-5=6` non-hub `D1` segments remain available for clean-line charges. The protected charging map requires one target per clean line, so

```
8 <= 6,
```

a contradiction.

Therefore the quadruple-hub `D2=3` role-type is impossible under the named premises.

## Case B — saturated triple hub

At a triple hub,

```
r = 3,
d2 = 3,
d1 = 3.
```

The local fan premise forbids two consecutive `D1` rays. With three `D1` rays and three `D2` rays on a six-cycle, the cyclic pattern must alternate:

```
D2, D1, D2, D1, D2, D1.
```

Thus every hub `D1` ray lies between two `D2` spokes.

Let the three leaf cores be `A,B,C`. By Lemma 1, the transverse line at each hub `D1` endpoint contains the two leaf cores on its adjacent spokes. Hence the arrangement contains lines through all three leaf pairs:

```
AB, BC, CA.
```

These leaf-pair lines are distinct from the three hub-spoke lines because the alternating pattern places no two `D2` spokes on antipodal rays of one hub line.

Count distinct arrangement lines containing at least one core. The total core-line incidence count is `I=13`.

- The three distinct hub-spoke lines each identify two core incidences, reducing the distinct-line count by at least three.
- The three leaf-pair constraints reduce it by at least two more: if the leaves are noncollinear they use three pair lines, giving reduction three; if the leaves are collinear the one common line contains all three leaves, giving reduction two.

Therefore

```
h <= 13 - 3 - 2 = 8.
```

So at least ten arrangement lines are clean.

All three hub `D1` segments are unavailable as clean-line charge targets by Lemma 1. Since `U=0` and `D1=11`, at most eight `D1` targets remain.

The charging map would require

```
10 <= 8,
```

a contradiction.

Therefore the triple-hub `D2=3` role-type is also impossible under the named premises.

## Result

Conditional on the named source-scoped local fan and clean-line charging premises, profile 3334 has no `D2=3` realization at `n=18,T=95`.

The 3334 residual is therefore reduced to the six protected role-types with

```
D2 in {4,5}.
```

The companion replay `ci/validate_openmath_h1_12_3334_d2_3.py` verifies the finite cyclic-pattern and capacity deductions used above.

## Claim boundary

The transverse-line lemma and the strengthened triple-hub core-line count are independently reconstructed.

The conclusion remains source-conditional because it uses the protected local no-long-run fan premise and clean-line charging map. It does not prove `T<=94`, does not certify optimality of the 93 construction, and has no MATHCERT effect.
