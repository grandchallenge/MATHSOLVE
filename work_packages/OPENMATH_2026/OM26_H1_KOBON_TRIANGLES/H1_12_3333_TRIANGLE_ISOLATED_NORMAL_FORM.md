# H1-12 q=4 profile 3333 — triangle-plus-isolated equality normal form

**State:** `SOLVE_SOURCE_CONDITIONAL_NORMAL_FORM__FINITE_REPLAYED__NOT_CERTIFIED`

## Scope

Continue from the protected five-normal-form profile-3333 residual.

The sole remaining charge-equality form is

```
D2 graph = K3 + isolated core
d2 = (2,2,2,0)
d1 = (2,2,2,2)
D1 = 8
U = 2
I = 12
D2 = 3
clean lower bound = 9
charge capacity = 9.
```

Let the three D2-connected cores be `A,B,C`, and let the isolated core be `D`.

This tranche does not exclude the form. It derives its exact local geometric normal form, conditional on the named triple-point local fan premise and clean-line charging map.

## 1. Equality fixes the core-line count

The core-incidence inequality gives

```
h <= I-D2 = 9.
```

The clean-line charging bound is already at equality:

```
18-h >= 9 = charge capacity.
```

Therefore any realization must have

```
h = 9.
```

No arrangement line may contain two cores unless that repeated incidence is already accounted for by one of the three D2 edges `AB,BC,CA`.

Consequently:

- the isolated core `D` shares no arrangement line with `A,B,C`;
- the third line through each of `A,B,C` contains no other core;
- the three lines through `D` contain no other core;
- the nine core-containing lines are exactly the three triangle-side lines, the three remaining lines through `A,B,C`, and the three lines through `D`.

Any extra core-pair line would make `h<=8`, hence at least ten clean lines against capacity nine.

## 2. Local equality at a triangle core

Fix `A`. Its two D2 rays point to `B` and `C`.

The protected blocked-target equality requires exactly one of the two D1 rays at `A` to be adjacent to a D2 ray.

For six cyclic rays with

```
2 D1,
2 D2,
2 other,
```

and no two consecutive D1 rays, the protected finite classification has two dihedral mechanisms.

### Mechanism B cannot occur here

In the second mechanism, the unique blocked D1 ray lies cyclically between the two D2 rays.

Let its ordinary endpoint be `P`. The transverse-line lemma then puts `B,P,C` on one arrangement line. As in the protected saturated-hub separator lemma, `P` lies strictly between `B` and `C`: otherwise one of the elementary triangle sides from `P` to `B` or `C` would contain the other core in its interior.

But `BC` is itself a D2 elementary segment. It cannot contain the ordinary arrangement vertex `P` in its relative interior.

Contradiction.

Therefore the between-D2 blocked-ray mechanism is impossible.

### Only adjacent D2 rays remain

The two D2 rays at `A` must therefore be cyclically adjacent.

The sector between them is triangular: the D2 segments `AB` and `AC` are each used by two triangular faces, and this common sector is the face on their shared side.

Its third side lies on the D2 line `BC`.

Thus `ABC` is a counted bounded triangular face.

The same conclusion is obtained at all three connected cores.

## 3. The isolated core is exterior

Because `ABC` is a counted face, no other arrangement line crosses its open interior.

The core `D` is an intersection of three arrangement lines. Hence `D` cannot lie in the open triangle `ABC`.

It also cannot lie on a side or side-support through a triangle core, because equality forbids every additional core-pair line.

Therefore `D` is strictly exterior to the closed triangular face `ABC`, and all three lines through `D` avoid its open interior.

## 4. Two local choices at each triangle vertex

Once the two D2 rays are fixed as adjacent positions, the exact local equality words are

```
D2,D2,O,D1,O,D1
D2,D2,D1,O,D1,O
```

up to cyclic reversal of the local labeling.

Equivalently, at each of `A,B,C` exactly one of its two incident central-triangle edges is selected.

If `A` selects edge `AB`, then the local D1 rays are:

- the outward continuation of the line `AB` opposite the D2 segment `AB`;
- the ray on the third line through `A` that bounds the outer triangle across edge `AB`.

The reflected local pattern selects `AC` instead.

Thus each triangle vertex chooses one of its two incident triangle edges.

## 5. Eight assignments, two symmetry types

There are

```
2^3 = 8
```

edge-choice assignments on the three vertices.

Modulo permutation of `A,B,C`, they have exactly two types.

### Type C — cyclic

Each central edge is selected exactly once.

There are two oriented labeled assignments, exchanged by reflection:

```
A->AB, B->BC, C->CA
```

and its reverse.

The edge-selection multiplicities are

```
(1,1,1).
```

### Type P — doubled edge plus tail

One central edge is selected by both its endpoints, one is selected once, and one is not selected.

There are six labeled assignments.

The edge-selection multiplicities are

```
(2,1,0).
```

No third symmetry type exists.

## Result

Conditional on the named source-scoped local fan and clean-line charging premises, the final charge-equality arithmetic normal form is reduced to two explicit geometric orientation types:

1. **Type C:** cyclic selection `(1,1,1)`;
2. **Type P:** doubled-edge selection `(2,1,0)`.

Both contain:

- a central counted D2 triangle `ABC`;
- an exterior isolated triple core `D`;
- exactly nine core-containing lines and no additional core-pair line.

The companion replay `ci/validate_openmath_h1_12_3333_triangle_isolated.py` reconstructs the local equality words and the two edge-choice symmetry classes.

## Next step

Analyze Type P first because its doubly selected edge forces both non-base sides of one outer triangle to be D1. Then analyze Type C, where every outer triangle receives exactly one selected endpoint.

The four positive-slack profile-3333 forms remain separate. The q>=5 residual remains separate.

## Claim boundary

The elementary-segment contradiction eliminating the between-D2 mechanism, the central-face conclusion, the exterior-core consequence, and the two-type quotient are independently reconstructed.

The reduction remains source-conditional because the local equality words and charge saturation invoke the named local fan premise and clean-line charging map. This artifact does not prove `T<=94`, does not certify optimality of the 93 construction, and has no MATHCERT effect.
