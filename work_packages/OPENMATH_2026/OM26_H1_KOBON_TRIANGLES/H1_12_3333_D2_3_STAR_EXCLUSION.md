# H1-12 q=4 profile 3333 — D2=3 non-saturated star exclusion

**State:** `SOLVE_SOURCE_CONDITIONAL_GEOMETRIC_REDUCTION__FINITE_REPLAYED__NOT_CERTIFIED`

## Scope

Continue from the protected seven-normal-form profile-3333 residual.

One of the three remaining charge-equality forms is the non-saturated `D2=3` star:

```
core graph = K1,3
hub:   d2=3, d1=1
leaves: d2=1, d1=2
D1 = 7
U = 1
I = 12
D2 = 3
clean lower bound = 9
charge capacity = 9.
```

Any realization must therefore attain equality in the current charging and core-incidence bounds.

## Equality at the hub

The protected transverse-line blocked-target lemma says that a `D1` segment adjacent to a `D2` ray cannot receive a clean-line charge.

The star normal form has blocked-target lower bound zero. Since its total charge capacity already equals the clean-line lower bound, any actual blocked `D1` target would make the capacity strictly too small.

Hence the unique hub `D1` ray is adjacent to no `D2` ray.

At the hub there are six cyclic radial rays consisting of

```
3 D2,
1 D1,
2 other.
```

If the `D1` ray has no `D2` neighbor, both of its cyclic neighbors are the two other rays. Therefore the remaining three positions form one consecutive run of `D2` rays:

```
other, D1, other, D2, D2, D2
```

up to cyclic symmetry.

The companion replay checks this exhaustively.

## Two forced leaf-pair lines

Let the three consecutive hub spokes terminate at leaves `A,B,C` in cyclic order.

The sectors between the consecutive pairs

```
HA, HB
HB, HC
```

are adjacent to double-used `D2` segments on both boundaries. Therefore both sectors are triangular faces.

Their third sides force arrangement lines

```
AB
BC.
```

These two leaf-pair relations contribute at least two additional core-incidence savings beyond the three star spokes.

If `AB` and `BC` are distinct, each is an additional line through two cores.

If they coincide, the common line contains `A,B,C` and contributes two incidence savings by itself.

Neither can coincide with a hub-spoke line. Such coincidence would put two leaf cores on one line through the hub. If they lie on the same ray, one purported elementary `D2` segment contains the nearer core; if they lie on opposite rays, the spokes are antipodal. The three consecutive `D2` rays are not antipodal.

Thus the total core-incidence saving is at least

```
3 + 2 = 5.
```

Since `I=12`,

```
h <= 12-5 = 7.
```

Therefore at least

```
18-h >= 11
```

lines are clean.

But the exact charge capacity of the normal form is only 9.

Contradiction.

## Result

Conditional on the protected clean-line charging map and the previously established transverse-line blocked-target consequence, the non-saturated `D2=3` star cannot realize `n=18,T=95`.

The profile-3333 residual is reduced from

```
7 normal forms / 45 labeled states
```

to

```
6 normal forms / 41 labeled states.
```

Two charge-equality `D2=3` forms remain:

- the higher-count saturated star;
- the triangle-plus-isolated-core form.

## Claim boundary

The six-ray equality pattern and the two forced leaf-pair incidence savings are independently reconstructed.

The global contradiction uses the protected clean-line charging map and its exact equality consequence. No hill-global `T<=94`, optimality, or MATHCERT claim follows.
