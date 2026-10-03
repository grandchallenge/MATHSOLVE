# H1-12 q=4 profile 3333 — D2=4 C4 exclusion

**State:** `SOLVE_SOURCE_CONDITIONAL_GEOMETRIC_REDUCTION__FINITE_REPLAYED__NOT_CERTIFIED`

## Scope

Continue from the protected eight-normal-form profile-3333 residual.

The only remaining `D2=4` form is the non-saturated four-cycle:

```
core graph = C4
d2(v) = 2 at every core
d1(v) = 2 at every core
D1 = 8
U = 3
I = 12
D2 = 4.
```

The protected blocked-target replay gives

```
B >= 4,
clean >= 10,
capacity <= 2U + D1 - B = 10.
```

Thus any realization must attain equality everywhere:

```
B = 4,
h = I-D2 = 8,
clean = 10,
capacity = 10.
```

In particular, each core has exactly one blocked `D1` target.

## Local equality lemma

Fix a core `V` and let its two `D2` neighbors in the four-cycle be `A` and `B`.

At `V` there are six cyclic radial rays consisting of

```
2 D1 rays,
2 D2 rays,
2 other rays.
```

The named triple-point local fan premise forbids two consecutive `D1` rays.

Impose the equality condition that exactly one of the two `D1` rays is adjacent to a `D2` ray. Exhausting the six-ray cyclic words gives exactly two forms up to rotation and reflection.

### Type A — the two D2 rays are adjacent

The sector between the two `D2` rays is adjacent to each of the two double-used `D2` segments. Therefore it is a triangular face.

Its third side joins the two neighbor cores `A` and `B`. Hence the line `AB` is one of the arrangement lines.

### Type B — the unique blocked D1 ray lies between the D2 rays

Let `VP` be that `D1` segment.

Because `VP` is shared by two triangular faces and its adjacent radial rays terminate at `A` and `B`, the protected transverse-line argument gives that the unique transverse arrangement line through the ordinary endpoint `P` contains both `A` and `B`.

Again `AB` is an arrangement line.

Thus, in every local equality pattern:

```
the two C4 neighbors of V share an arrangement line.
```

## Why this contradicts h=8

The two neighbors `A,B` of `V` are nonadjacent in the `D2` four-cycle.

The core-incidence inequality

```
h <= I-D2
```

comes from counting repeated core incidences on arrangement lines. Equality `h=I-D2=8` means the four `D2` elementary core-core segments account for all such incidence savings. Any additional arrangement line through a pair of cores makes the inequality strict.

The forced line `AB` is additional.

It cannot be the same line as the two `D2` spokes `VA,VB`: that would put the two `D2` rays at `V` on one arrangement line. If they point to the same side, one elementary segment contains the nearer core; if they point to opposite sides, the two rays are antipodal. Neither occurs in the two local equality types.

It also cannot acquire the fourth core as an intermediate point without contradiction. In a C4, the fourth core is the common `D2` neighbor of `A` and `B`. If it lay between them, its two `D2` rays would be antipodal, again absent from the local equality types; if it did not lie between them, one of the purported elementary `D2` segments would contain another core.

Hence `AB` contributes a genuine additional core-incidence saving, so

```
h <= 7.
```

Therefore

```
clean = 18-h >= 11.
```

But the exact charge capacity of the C4 normal form is at most 10.

Contradiction.

## Result

Conditional on the named source-scoped local fan premise and clean-line charging map, the profile-3333 `D2=4` C4 normal form cannot realize `n=18,T=95`.

The profile-3333 residual is reduced from

```
8 normal forms / 48 labeled states
```

to

```
7 normal forms / 45 labeled states,
```

all with `D2<=3`.

The next tight cases are the three `D2=3` equality forms.

## Claim boundary

The local two-type equality classification and the extra core-line incidence argument are independently reconstructed.

The conclusion remains source-conditional because the local classification invokes the protected no-two-consecutive-`D1` premise and the global contradiction uses the protected clean-line charging map.

This artifact does not prove `T<=94`, does not certify optimality of the 93 construction, and has no MATHCERT effect.
