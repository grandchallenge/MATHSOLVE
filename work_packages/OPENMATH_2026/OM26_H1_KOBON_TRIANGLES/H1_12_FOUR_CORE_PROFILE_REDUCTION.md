# H1-12 four-core profile reduction

**State:** `SOLVE_SOURCE_CONDITIONAL_REDUCTION__FINITE_ARITHMETIC_REPLAYED__NOT_CERTIFIED`

## Scope

Assume an admissible `n=18` hill arrangement has `T=95` counted bounded triangular faces. Apply the protected H1-12 projective reduction so that all line pairs meet finitely while the selected counted faces are preserved.

This note studies the residual case with exactly four finite multiple points.

As in the protected q=3 tranche, the defect identity, clean-line charging inequality, and local fan bounds are treated with their existing source scope. The arithmetic deductions below are independently reconstructed and replayed in GCL.

Write the four multiplicities as `r_1,...,r_4 >= 3`, and put

```
delta = 18*16 - 3*95 = 3
I = sum r_i
S = sum r_i(r_i-2).
```

Let `U,D1,D2,h` have the meanings fixed in the preceding H1-12 artifacts.

## 1. Five multiplicity profiles only

For four finite multiple points, every elementary segment counted by `D2` joins a distinct unordered pair of core points. Therefore

```
D2 <= C(4,2) = 6.
```

The universal local fan bound gives

```
d1(v) <= 2r_v-3,
```

hence

```
D1 <= 2I-12.
```

The defect identity is

```
3 = S + U - D1 - D2.
```

Since `U>=0`,

```
S <= 3 + D1 + D2
  <= 3 + (2I-12) + 6
  = 2I-3.
```

Therefore

```
sum_i r_i(r_i-4) = S-2I <= -3.
```

For integer `r>=3`,

```
r(r-4):
r=3 -> -3
r=4 ->  0
r=5 ->  5
r=6 -> 12
```

and the value then increases strictly. The only nondecreasing four-tuples satisfying the inequality are

```
(3,3,3,3)
(3,3,3,4)
(3,3,3,5)
(3,3,4,4)
(3,4,4,4).
```

Thus every four-core 95 candidate is low-multiplicity: there is at least one triple point, no multiplicity exceeds five, and a fivefold point can occur only in the profile `(3,3,3,5)`.

## 2. Core-sharing density

The companion exact replay adds the already named local refinements:

- at a triple point, `d1<=2` unless `d2=3`, in which case `d1<=3`;
- if `d2<=1` and `r>=4`, then `d1<=2r-4`;
- universally, `d1<=2r-3`;
- exactly `2r-1` shared radial rays are impossible, because one nontriangular sector removes both of its boundary rays while all-triangular sectors give all `2r` shared rays;
- `h<=I-D2`;
- `18-h<=2U+D1`.

It enumerates all 64 simple core graphs on four labeled core points and every local `d1` count allowed by these necessary conditions.

The resulting necessary lower bounds on `D2` are

| multiplicities | necessary core sharing |
|---|---:|
| `(3,3,3,3)` | `D2 >= 1` |
| `(3,3,3,4)` | `D2 >= 3` |
| `(3,3,3,5)` | `D2 = 6` |
| `(3,3,4,4)` | `D2 >= 5` |
| `(3,4,4,4)` | `D2 = 6` |

Hence the two highest-multiplicity four-core profiles require the complete core graph `K4`, while `(3,3,4,4)` requires at least five of its six possible core-pair segments to be double-used triangular sides.

The replay is implemented by `ci/validate_openmath_h1_12_four_core.py` and its unit tests. It checks only finite arithmetic/combinatorial consequences of the explicitly named premises; it does not promote the source-scoped global charging/fan extraction to an independently certified theorem.

## Result

Conditional on the named source-scoped premises, a hypothetical normalized `n=18,T=95` witness lies in one of two residual classes:

1. at least five finite multiple points; or
2. exactly four finite multiple points with one of the five profiles above and the corresponding minimum `D2` density.

This is a strict reduction of the protected `q>=4` residual.

## Next mathematical step

The highest-value four-core cases are now the dense-core profiles. In particular:

- analyze the complete-core cases `(3,3,3,5)` and `(3,4,4,4)` geometrically;
- analyze `(3,3,4,4)` first at `D2=5` and `D2=6`;
- keep the lower-density all-triple and `(3,3,3,4)` cases separate rather than mixing them into one search.

A construction search, if resumed, should target these exact singular strata.

## Claim boundary

This artifact does not prove `T<=94`. It does not certify optimality of the 93 construction. The five-profile theorem is an independently reconstructed arithmetic consequence of the stated defect/fan premises; the stronger `D2` density table additionally uses the stated clean-line and local fan refinements. Those geometric premises retain their existing source scope until separately proved or certified inside GCL.
