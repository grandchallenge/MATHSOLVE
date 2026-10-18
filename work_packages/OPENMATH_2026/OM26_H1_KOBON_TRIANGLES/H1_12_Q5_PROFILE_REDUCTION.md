# H1-12 q=5 multiplicity and core-graph reduction

**State:** `SOLVE_SOURCE_CONDITIONAL_FINITE_REDUCTION__REPLAYED__NOT_CERTIFIED`

## Scope

Continue from the protected H1-12 result that any normalized `n=18,T=95` witness must have at least five finite multiple points.

This tranche treats the exact case

```
q = 5.
```

Write the five multiplicities as `r_1,...,r_5 >= 3`, and retain

```
delta = 18*16 - 3*95 = 3,
I = sum r_i,
S = sum r_i(r_i-2).
```

The defect identity is

```
3 = S + U - D1 - D2.
```

## 1. Coarse multiplicity reduction

The protected universal local fan bound gives

```
d1(v) <= 2r_v-3,
```

hence

```
D1 <= 2I-3q = 2I-15.
```

With five core points, an elementary D2 segment can join at most one segment for each unordered core pair:

```
D2 <= C(5,2) = 10.
```

Since `U>=0`,

```
S <= 3 + D1 + D2
  <= 3 + (2I-15) + 10
  = 2I-2.
```

Therefore

```
sum_i r_i(r_i-4) = S-2I <= -2.
```

For `r>=3` the values begin

```
r=3 -> -3
r=4 ->  0
r=5 ->  5
r=6 -> 12
```

and increase thereafter.

The only nondecreasing five-tuples satisfying the inequality are

```
33333
33334
33335
33344
33345
33444
34444.
```

So every q=5 score-95 candidate is already confined to seven low-multiplicity profiles.

## 2. Sector-consistent local replay

The companion replay then applies the stronger local information protected in the q=4 closure.

For each candidate multiplicity assignment and each simple graph on five labeled core points:

1. the graph degree at a core is its local `d2(v)`;
2. enumerate the `2r` cyclic triangular/nontriangular sector bits;
3. derive shared rays exactly from
   ```
   shared(i) <=> sector(i-1) and sector(i);
   ```
4. label exactly `d2(v)` shared rays as D2 and the rest as D1;
5. enforce the named local fan premise that no block of `r-1` consecutive rays is entirely D1;
6. record the resulting local pairs
   ```
   (d1(v), blocked(v)),
   ```
   where a blocked D1 ray is adjacent to at least one D2 ray.

The replay combines the five local option sets by dynamic programming over total `D1` and total blocked count `B`.

For each state it then computes

```
U = 3 - S + D1 + D2
```

and requires

```
U >= 0.
```

The baseline core-incidence bound gives

```
h <= I-D2,
clean >= 18-(I-D2).
```

Blocked D1 targets cannot receive clean-line charges, so the necessary charge condition is

```
18-(I-D2) <= 2U + D1 - B.
```

No geometric claim beyond the explicitly named local fan/charging premises is inserted into this replay.

## 3. Exact surviving profiles

The seven coarse profiles reduce to exactly three.

### 33333

Survives only with

```
3 <= D2 <= 10.
```

The replay retains 671 labeled core-graph states at this level.

### 33334

Survives only with

```
5 <= D2 <= 9.
```

Across the five possible placements of the quadruple core, the replay retains 1270 labeled multiplicity-placement/core-graph states.

### 33344

Survives only with

```
6 <= D2 <= 7.
```

Across the ten placements of the two quadruple cores, the replay retains 140 labeled multiplicity-placement/core-graph states.

## 4. Profiles excluded at q=5

The following four coarse profiles have no sector-consistent core graph satisfying the defect and clean-line charge conditions:

```
33335
33345
33444
34444.
```

This exclusion is a finite consequence of the protected premises, not an unconditional hill-global theorem.

## Result

Conditional on the named source-scoped fan and clean-line charging premises, a normalized `n=18,T=95` witness with exactly five finite multiple points must have one of

```
33333
33334
33344.
```

Therefore the live H1-12 residual is

1. q=5 with one of those three profiles; or
2. q>=6.

The companion replay `ci/validate_openmath_h1_12_q5_profiles.py` reconstructs the seven-profile arithmetic gate, all 1024 labeled five-core graphs, the sector-consistent local option tables, and the exact surviving profile/D2 ranges.

## Next step

Begin with the densest q=5 profile `33344`, where `D2` is forced to six or seven. Quotient its labeled graph states by permutations preserving multiplicity roles and apply saturation/extreme-core geometry before treating `33334` and `33333`.

Keep q>=6 separate.

## Claim boundary

The coarse profile inequality, graph enumeration, sector-to-shared-ray construction, and finite dynamic-programming replay are independently reconstructed.

The result remains source-conditional because the no-long-run local fan premise and clean-line charging map retain their protected source scope. It does not prove `T<=94`, does not certify optimality of the 93 construction, and has no MATHCERT effect.
