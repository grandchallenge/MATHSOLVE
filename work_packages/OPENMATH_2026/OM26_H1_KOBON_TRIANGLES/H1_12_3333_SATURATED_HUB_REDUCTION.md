# H1-12 q=4 profile 3333 — saturated-hub separator reduction

**State:** `SOLVE_SOURCE_CONDITIONAL_GEOMETRIC_REDUCTION__FINITE_REPLAYED__NOT_CERTIFIED`

## Scope

Continue from the protected 12-normal-form reduction for profile `3333`.

This tranche studies the forms containing a saturated triple core. At such a hub `H`,

```
d2(H)=3,
d1(H)=3.
```

The named local triple-point fan premise forbids two consecutive `D1` rays. Since all six radial rays are shared, the cyclic pattern must alternate

```
D2, D1, D2, D1, D2, D1.
```

Let the three `D2` leaf cores be `A,B,C`.

## Separator lemma

Consider the hub `D1` segment `HP` lying cyclically between the `D2` spokes `HA` and `HB`.

Because `HP` is a `D1` segment, it is incident to triangular faces on both sides. The two faces adjacent to the spokes are

```
HAP
HBP.
```

At the ordinary point `P`, the unique transverse arrangement line must therefore contain both `A` and `B`.

Moreover, `P` lies strictly between `A` and `B` on that line. If `P` lay outside the segment `AB`, then one of the two elementary triangle sides `AP` or `BP` would contain the other core point in its interior, contradicting that it is an elementary arrangement segment.

Hence every pair of leaves has an ordinary arrangement vertex strictly between them:

```
P_AB in segment AB,
P_BC in segment BC,
P_CA in segment CA.
```

Therefore none of the three leaf-pair core segments can be a `D2` elementary segment.

### Consequence 1 — saturated hub forces D2=3

The three hub spokes are `D2`. The separator lemma shows that all three leaf-pair core segments are not `D2`.

Thus a saturated triple hub in profile `3333` forces

```
D2 = 3
```

and the `D2` graph is exactly `K1,3`.

All saturated-hub normal forms with `D2>=4` are impossible.

### Consequence 2 — the six core-pair lines are distinct

The three hub-spoke lines are distinct: two different leaf cores cannot lie on the same spoke ray because the nearer core would cut the farther purported elementary `D2` segment, and the alternating six-ray pattern puts no two `D2` spokes on antipodal rays.

The three leaf cores cannot be collinear. If, say, `B` lay between `A` and `C`, then no ordinary point could lie strictly between `A` and `C` while being joined to both by elementary segments, because the core `B` would intervene. This contradicts the separator lemma for the pair `A,C`.

Hence the three leaf-pair lines are distinct.

No leaf-pair line can coincide with a hub-spoke line, because that would put two `D2` leaf cores on one line through `H`, contradicting the elementary-spoke and alternating-ray observations above.

Therefore all six pair lines among

```
H,A,B,C
```

are distinct arrangement lines.

Each core is triple, so exactly three arrangement lines pass through each core. The six pair lines already supply those three lines at every core. Hence the total number `h` of arrangement lines containing a multiple point is exactly

```
h = 6.
```

Thus any saturated-hub `3333` form has exactly

```
18-h = 12
```

clean lines.

## Replay consequence

The protected 12-normal-form table contains five saturated-hub forms:

- two with `D2=3`;
- two with `D2=4`;
- one with `D2=5`.

By Consequence 1, all three saturated forms with `D2>=4` are excluded immediately.

For the two `D2=3` saturated-star forms, the protected charge capacities are:

```
lower-count form: capacity 9,
higher-count form: capacity 12.
```

Consequence 2 strengthens the clean-line lower bound from 9 to exactly 12.

Therefore the lower-count saturated star is excluded:

```
12 > 9.
```

The higher-count saturated star remains as an equality form:

```
12 = 12.
```

## Updated profile-3333 residual

The 108 labeled states in 12 normal forms reduce to:

```
48 labeled states
8 normal forms.
```

The remaining `D2` histogram is

| D2 | labeled states |
|---:|---:|
| 1 | 6 |
| 2 | 15 |
| 3 | 24 |
| 4 | 3 |
| 5 | 0 |

Thus the only remaining `D2=4` form is the non-saturated four-cycle. No `D2>=5` form remains.

Four normal forms now exactly saturate the strongest current charge bound:

1. D2=3 non-saturated star;
2. D2=3 higher-count saturated star, with exactly 12 clean lines;
3. D2=3 triangle plus isolated core;
4. D2=4 non-saturated four-cycle.

These are the next geometric targets.

## Claim boundary

The separator lemma, distinct-six-line consequence, and finite filtering are independently reconstructed.

The conclusion remains source-conditional because the initial alternating saturated-hub pattern uses the named local no-two-consecutive-`D1` premise, and the exclusion of the lower-count star uses the protected clean-line charging map.

This artifact does not prove `T<=94`, does not certify optimality of the 93 construction, and has no MATHCERT effect.
