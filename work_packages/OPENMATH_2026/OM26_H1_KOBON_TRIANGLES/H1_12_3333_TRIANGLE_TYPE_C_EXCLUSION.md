# H1-12 q=4 profile 3333 — triangle-isolated Type C exclusion

**State:** `SOLVE_SOURCE_CONDITIONAL_GEOMETRIC_REDUCTION__FINITE_REPLAYED__NOT_CERTIFIED`

## Scope

Continue from the protected triangle-isolated normal form and Type P exclusion.

The sole remaining charge-equality orientation is Type C:

```
central D2 triangle ABC,
exterior isolated triple core D,
exactly nine core-containing lines,
edge-selection multiplicities (1,1,1).
```

Thus each central edge is selected at exactly one endpoint.

This note excludes Type C by a local incidence obstruction.

## 1. Selected-vertex geometry

Fix a triangle vertex `V` selecting edge `VW`, and let `U` be the third triangle vertex.

Let `L_V,L_W,L_U` denote the third core-lines through the three central cores.

From the protected triangle-isolated normal form:

- the blocked D1 segment at `V` lies on `L_V` toward the outer vertex
  ```
  P_VW = L_V ∩ L_W;
  ```
- the unblocked D1 segment at `V` lies on the outward continuation of side line `VW`;
- the local equality geometry contains no extra core-pair line.

Because the blocked D1 segment is shared, the triangular face on its non-outer side has its third vertex at

```
Q_V = L_W ∩ VU.
```

The point `Q_V` lies on the outward ray of side line `VU`.

It is not one of the four existing multiple points:

- it is not `V` or `U`, because that would put `L_W` through an additional central core;
- it is not `W`, because `W` is not on side line `VU`;
- it is not the isolated core `D`, because equality forbids any line through `D` and a central core.

Hence before the next line is considered, `Q_V` is an ordinary intersection of exactly the two arrangement lines

```
L_W
and
VU.
```

## 2. The chargeable outward D1 forces a third line through Q_V

Let `VX` be the unblocked D1 elementary segment on the outward continuation of `VW`.

One of the two triangular sectors adjacent to `VX` is bounded at `V` by the outward `VU` ray. Its first vertex on that ray is exactly `Q_V`, from the preceding shared-face geometry.

Therefore the triangular face in that sector has third side

```
XQ_V.
```

Let its supporting arrangement line be `M_V`.

Thus

```
Q_V ∈ M_V.
```

The line `M_V` is distinct from both pre-existing lines through `Q_V`.

### M_V is not VU

The point `X` lies on side line `VW` and is not `V`. Since the distinct side lines `VU` and `VW` meet only at `V`, `X` is not on `VU`.

So `M_V != VU`.

### M_V is not L_W

The line `L_W` meets side line `VW` at the core `W`. The point `X` lies on the opposite outward ray from `V), so `X != W`.

Hence `X` is not on `L_W`, and

```
M_V != L_W.
```

Therefore the three distinct arrangement lines

```
L_W,
VU,
M_V
```

are concurrent at `Q_V`.

So `Q_V` is a new finite multiple point.

## 3. Contradiction with q=4

This tranche assumes exactly four finite multiple points:

```
A,B,C,D.
```

The selected-vertex geometry forces the additional multiple point `Q_V`.

Contradiction.

The argument applies at every selected central vertex. One vertex already suffices.

## Result

Type C is impossible.

Together with the protected Type P exclusion, the entire K3-plus-isolated charge-equality arithmetic form is excluded.

The profile-3333 q=4 residual is reduced to the four positive-slack normal forms only:

1. D2=1 single edge;
2. D2=2 P3 plus isolated core;
3. D2=2 two disjoint edges;
4. D2=3 P4.

These contain

```
33 labeled states
```

in total.

The companion replay `ci/validate_openmath_h1_12_3333_triangle_type_c.py` checks the selected-vertex incidence roles for both cyclic Type C assignments and verifies that each selected vertex introduces a third distinct line through its `Q_V` descriptor.

## Claim boundary

The forced-new-multiple-point argument is independently reconstructed from the protected local face geometry.

The predecessor reduction remains source-conditional because reaching the Type C normal form used the named local fan premise and clean-line charging equality. This artifact does not prove `T<=94`, does not certify optimality of the 93 construction, and has no MATHCERT effect.
