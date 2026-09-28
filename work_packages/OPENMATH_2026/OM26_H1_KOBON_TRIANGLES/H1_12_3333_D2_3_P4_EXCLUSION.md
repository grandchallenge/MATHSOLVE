# H1-12 q=4 profile 3333 — D2=3 P4 exclusion

**State:** `SOLVE_SOURCE_CONDITIONAL_GEOMETRIC_REDUCTION__FINITE_REPLAYED__NOT_CERTIFIED`

## Scope

Continue from the protected four-form positive-slack profile-3333 residual.

This tranche studies the D2=3 path form

```
A -- B -- C -- D
```

with

```
d2 = (1,2,2,1)
d1 = (2,2,2,2)
D1 = 8
U = 2
I = 12
D2 = 3.
```

The protected normal-form budget gives

```
clean >= 9,
nominal blocked lower bound = 2,
nominal charge capacity <= 10.
```

The two internal cores `B,C` have local counts `(d1,d2)=(2,2)`.

## Local dichotomy at an internal core

At a triple core with

```
d1=2,
d2=2,
```

the named local fan premise forbids consecutive D1 rays.

Let `b(v)` be the actual number of D1 rays adjacent to at least one D2 ray. The finite six-ray enumeration gives

```
b(v) in {1,2}.
```

If `b(v)=1`, the protected two-type local classification applies:

1. the two D2 rays are adjacent, so the sector between them is a triangular face; or
2. the unique blocked D1 ray lies between the two D2 rays.

In either mechanism, the two D2-neighbor cores of `v` lie on a common arrangement line.

For an internal vertex of the path, those two neighbors are not joined by a D2 edge. Therefore this is an **additional core-pair incidence** beyond the three D2 path edges.

If `b(v)=2`, no extra core line is needed for the argument; the additional blocked target itself reduces charge capacity by one.

## Core-incidence accounting

The baseline incidence bound is

```
h <= I-D2 = 9,
```

so `clean >= 9`.

Every additional core-pair incidence not already represented by a D2 edge makes the bound stricter by at least one.

The two internal vertices force different non-D2 neighbor pairs:

- `B` forces `AC` when `b(B)=1`;
- `C` forces `BD` when `b(C)=1`.

If both are forced, they contribute at least two additional incidence savings.

They cannot collapse to a single all-four-core line in the `b(B)=b(C)=1` case: that would make the two D2 rays at each internal core antipodal on one arrangement line, while the one-blocked local classification contains only angular separations one or two in the six-ray cycle, never an antipodal pair.

## Three cases

Let

```
B_total
```

denote the total blocked-D1 count. Endpoint blocking can only strengthen the contradictions below, so it is enough to count the two internal cores.

### Case 1: b(B)=1 and b(C)=1

Then

```
B_total >= 2,
charge capacity <= 2U + D1 - B_total
                <= 4 + 8 - 2
                = 10.
```

Both internal cores force an additional non-D2 core-pair incidence, so

```
h <= 12 - 3 - 2 = 7,
clean >= 11.
```

Thus

```
11 > 10.
```

Contradiction.

### Case 2: one internal core has b=1 and the other has b=2

Then

```
B_total >= 3,
charge capacity <= 4 + 8 - 3 = 9.
```

The one-blocked internal core forces at least one additional non-D2 core-pair incidence:

```
h <= 12 - 3 - 1 = 8,
clean >= 10.
```

Thus

```
10 > 9.
```

Contradiction.

### Case 3: b(B)=2 and b(C)=2

Then

```
B_total >= 4,
charge capacity <= 4 + 8 - 4 = 8.
```

Even the baseline clean-line bound gives

```
clean >= 9.
```

Thus

```
9 > 8.
```

Contradiction.

## Result

Conditional on the named source-scoped triple-point local fan premise and clean-line charging map, the profile-3333 D2=3 P4 form cannot realize `n=18,T=95`.

The q=4 residual is reduced to three forms:

1. D2=1 single edge — 6 labeled states;
2. D2=2 P3 plus isolated core — 12 labeled states;
3. D2=2 two disjoint edges — 3 labeled states.

Total:

```
21 labeled states.
```

The companion replay `ci/validate_openmath_h1_12_3333_p4.py` checks the internal-core local dichotomy, the one-blocked neighbor-line mechanisms, and all three budget cases.

## Claim boundary

The P4 case split and extra core-incidence accounting are independently reconstructed.

The conclusion remains source-conditional because the local six-ray restriction and global clean-line charging map retain their protected source scope. This artifact does not prove `T<=94`, does not certify optimality of the 93 construction, and has no MATHCERT effect.
