# H1-12 q=5 — K3 plus two isolated cores equality normal form

**State:** `SOLVE_SOURCE_CONDITIONAL_NORMAL_FORM__FINITE_REPLAYED__NOT_CERTIFIED`

## Scope

Continue from the protected q=5 `33333` reduction.

The sole q=5 score-95 residual has five triple cores and

```
D2 graph = K3 + two isolated vertices
D2 = 3
D1 = 10
U = 1
blocked D1 = 6
clean lower bound = charge capacity = 6.
```

Let the D2 triangle cores be `A,B,C`. Let the two isolated triple cores be `D,E`.

This tranche derives the exact equality geometry. It does **not** exclude the case.

## 1. Equality fixes the core-line count

The core-incidence inequality gives

```
h <= I-D2 = 15-3 = 12.
```

Hence at least six arrangement lines are clean.

The protected charge capacity is exactly six. Therefore any realization must attain equality:

```
h = 12
clean = 6.
```

There can be no additional arrangement line containing two cores beyond the three D2 side lines

```
AB, BC, CA.
```

Otherwise `h<=11`, giving at least seven clean lines against capacity six.

Consequently:

- `D` shares no arrangement line with `A,B,C,E`;
- `E` shares no arrangement line with `A,B,C,D`;
- the three lines through `D` are distinct from the three lines through `E`;
- none of those six lines contains `A,B,` or `C`;
- at each of `A,B,C`, the third incident line is unique to that core.

## 2. The D2 triangle is a counted central face

At each triangle core, the two D2 rays are shared by two triangular faces.

The third line through the vertex cannot enter the open sector between the two D2 edges: that sector is bounded by the two elementary D2 segments and is the common sector adjacent to both shared rays.

Hence the D2 rays are cyclically adjacent and the common sector is triangular.

Thus

```
ABC
```

is a counted bounded triangular face.

## 3. Unique local sector word at A, B, C

Fix `A` and place its two D2 rays in adjacent cyclic positions.

The protected local data are

```
d2(A)=2
d1(A)=2
blocked(A)=2.
```

Sector-consistent enumeration gives exactly one six-ray word, up to rotation/reflection preserving the two adjacent D2 rays:

```
D2, D2, D1, 0, 0, D1.
```

Therefore both D1 rays lie on the third arrangement line through `A`, in opposite directions.

The same holds at `B` and `C`.

Write these third lines as

```
L_A, L_B, L_C.
```

## 4. The three third lines form an outer triangle

Because D2 side `AB` is shared by two triangular faces, one face is central triangle `ABC` and the other lies on the opposite side of line `AB`.

At `A` and `B`, that outer face uses the D1 rays on `L_A` and `L_B`. Its third vertex is therefore

```
X_AB = L_A ∩ L_B.
```

The point `X_AB` is ordinary; otherwise q=5 would contain an additional finite multiple point.

Similarly define

```
X_BC = L_B ∩ L_C
X_CA = L_C ∩ L_A.
```

The outer faces are

```
ABX_AB
BCX_BC
CAX_CA.
```

Since both rays on each `L_A` are D1, the two ordinary vertices `X_AB,X_CA` lie on opposite sides of `A). Hence

```
A in interior segment X_AB X_CA.
```

Cyclically,

```
B in interior segment X_AB X_BC
C in interior segment X_BC X_CA.
```

Thus `L_A,L_B,L_C` form an outer triangle, and `A,B,C` lie in the relative interiors of its three sides.

The q=5 equality core therefore contains an exact six-line nested-triangle skeleton.

## 5. Local form at each isolated core

At isolated core `D`,

```
d2(D)=0
d1(D)=2
blocked(D)=0.
```

Sector-consistent enumeration has one type up to rotation:

> the two D1 rays are antipodal.

Thus both D1 segments at `D` lie on the same arrangement line through `D), one in each direction.

Call that line `M_D`.

The same holds at `E`, with line `M_E`.

The other two lines through each isolated core support no D1 segment.

## 6. Exact clean-line charge partition

The six blocked D1 targets are precisely the two D1 segments at each of `A,B,C`.

The only unblocked D1 segments are the four segments on

```
M_D and M_E.
```

Since total charge capacity equals the six clean lines, equality forces every capacity slot to be used.

Therefore:

1. each of the four isolated-core D1 segments receives one clean-line charge;
2. their four transverse clean lines are pairwise distinct;
3. the unique U segment receives two charges, one at each ordinary endpoint;
4. those two clean lines are distinct from each other and from the four D1-charging lines.

Hence the six clean arrangement lines are partitioned exactly as

```
4 isolated-core D1 transverse lines
+
2 U-endpoint transverse lines.
```

No charge slot can collide or remain unused.

## Result

Conditional on the named source-scoped local fan and clean-line charging premises, the sole q=5 residual is reduced to the following exact geometry:

- a central counted D2 triangle `ABC`;
- an outer triangle formed by `L_A,L_B,L_C`, with `A,B,C` in the relative interiors of its sides;
- two isolated triple cores `D,E`, each with one line carrying two opposite D1 segments;
- no additional core-pair line;
- exactly six clean lines, with the exact charge partition `4+2` above;
- one U segment whose two endpoint charges consume the final two clean lines.

The companion replay `ci/validate_openmath_h1_12_q5_equality.py` checks the unique local sector types and the equality arithmetic.

## Next step

Treat this as an exact incidence-feasibility problem, not a generic coordinate search.

A valid next tranche must either:

1. derive an incidence/ordering contradiction from the nested-triangle skeleton and the `4+2` clean-line charge bijection; or
2. encode exactly this stratum in an independent exact feasibility search and replay any survivor with the existing exact scorer.

Keep q>=6 separate.

## Claim boundary

The nested-triangle skeleton, antipodal isolated-core D1 form, and exact clean-line charge partition are independently reconstructed.

The reduction remains source-conditional because the local sector state space inherits the named fan premise and the equality capacity uses the protected clean-line charging map. This artifact does not prove `T<=94`, does not certify optimality of the 93 construction, and has no MATHCERT effect.
