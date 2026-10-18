# H1-12 q=4 profile 3333 — triangle-isolated Type P exclusion

**State:** `SOLVE_SOURCE_CONDITIONAL_GEOMETRIC_REDUCTION__FINITE_REPLAYED__NOT_CERTIFIED`

## Scope

Continue from the protected triangle-plus-isolated equality normal form.

Let `A,B,C` be the three cores of the central counted D2 triangle, with third core-lines `L_A,L_B,L_C`. Let `D` be the exterior isolated triple core.

At each triangle vertex `V`, the protected local equality form selects one of its two incident central edges.

Type P has edge-selection multiplicities

```
(2,1,0).
```

Thus one central edge is selected by both endpoints, one edge once, and one edge not at all.

This note excludes Type P conditional on the protected clean-line charging equality.

## 1. Outer vertices

For distinct triangle vertices `X,Y`, write

```
P_XY = L_X ∩ L_Y.
```

Because the D2 edge `XY` is shared by the central triangle and one outer triangular face, `P_XY` is the ordinary third vertex of that outer face.

The protected equality normal form says that if vertex `V` selects edge `VW`, with `U` the third triangle vertex, then:

- the blocked D1 ray at `V` lies on `L_V` toward `P_VW`;
- the unblocked, chargeable D1 ray at `V` is the outward continuation of the side line `VW`.

## 2. The clean transverse line of a selected outward D1 segment

Fix `V` selecting `VW`, and let `U` be the third triangle vertex.

The blocked D1 segment on `L_V) toward `P_VW` is shared by two triangular faces.

One is the outer triangle across edge `VW`.

The other lies on the opposite side of that D1 segment. At `V`, its other side follows the outward ray of the unselected side line `VU`. At `P_VW`, its other side follows the line `L_W` away from `W`.

Therefore the first vertex on the outward `VU` ray is

```
Q_V = L_W ∩ VU.
```

Now consider the unblocked D1 segment on the outward continuation of `VW`.

Its two adjacent triangular sectors use:

- the ray of `L_V` toward the other outer vertex `P_VU`;
- the outward `VU` ray toward `Q_V`.

Hence the unique transverse arrangement line through the ordinary endpoint of this chargeable D1 segment is

```
M_V = line(P_VU, Q_V)
    = line(L_V ∩ L_U, L_W ∩ VU).
```

By charge equality, `M_V` must be clean.

This formula is independently reconstructed from the protected local face geometry.

## 3. Type P forces two M-lines to coincide

Without loss of labels, suppose edge `AB` is selected by both `A` and `B`.

The third vertex `C` must select either `CA` or `CB`.

### If C selects CA

For `B`, the selected neighbor is `A` and the third vertex is `C`, so

```
M_B = line(P_BC, L_A ∩ BC).
```

For `C`, the selected neighbor is also `A` and the third vertex is `B`, so

```
M_C = line(P_CB, L_A ∩ CB).
```

These are the same two points. Therefore

```
M_B = M_C.
```

### If C selects CB

Similarly,

```
M_A = line(P_AC, L_B ∩ AC)
```

and

```
M_C = line(P_CA, L_B ∩ CA),
```

so

```
M_A = M_C.
```

Thus every Type P assignment makes two distinct chargeable outward D1 segments share the same unique clean transverse line.

The companion finite replay checks this for all six labeled Type P assignments.

## 4. Equality cannot absorb the duplicate

The protected equality form has

```
D1 = 8,
U = 2,
blocked D1 = 3.
```

Thus exactly five D1 segments remain chargeable.

The clean-line charging proof gives:

- each chargeable D1 segment can receive at most one clean-line charge, through its unique ordinary endpoint and unique transverse line;
- each U segment can receive at most two charges;
- each clean line emits one charge.

The nominal equality capacity is therefore

```
5 + 2*2 = 9,
```

matching the nine clean lines.

But Type P identifies the unique clean transverse lines of two different chargeable D1 segments. One clean line can emit only one charge, so those two D1 capacity slots cannot both be filled.

Hence the actual total charge capacity is at most

```
4 + 2*2 = 8.
```

There are nine clean lines.

Contradiction.

## Result

Conditional on the named source-scoped clean-line charging equality and predecessor local fan reduction, Type P is impossible.

The final charge-equality residual is reduced to **Type C only**:

```
edge-selection multiplicities = (1,1,1).
```

Equivalently, the three triangle vertices select the central edges cyclically, with one selection per edge.

The companion replay `ci/validate_openmath_h1_12_3333_triangle_type_p.py` verifies that every one of the six Type P assignments has a duplicated `M_V` descriptor, while the two cyclic assignments do not.

## Claim boundary

The formula for `M_V` and the duplicate-line argument are independently reconstructed from the protected central-face geometry.

The contradiction remains source-conditional because it invokes the protected clean-line charging rule and exact equality saturation. This artifact does not prove `T<=94`, does not certify optimality of the 93 construction, and has no MATHCERT effect.
