# H1-12 q=4 profile 3333 — low-D2 sector-consistency closure

**State:** `SOLVE_SOURCE_CONDITIONAL_GEOMETRIC_REDUCTION__FINITE_REPLAYED__NOT_CERTIFIED`

## Scope

Continue from the protected profile-3333 residual after exclusion of the D2=3 P4 form.

Three q=4 forms remain:

1. D2=1 single edge;
2. D2=2 P3 plus isolated core;
3. D2=2 two disjoint edges.

All have `d1=2` at every triple core.

This tranche adds one local consistency condition that was deliberately absent from the earlier coarse blocked-target enumerator: the D1/D2 labels must actually arise from triangular sectors.

## 1. Shared-ray sector identity

At a finite multiple point, index the six radial rays cyclically and let

```
t_i = 1
```

when the sector between ray `i` and ray `i+1` is a triangular face.

A radial elementary segment on ray `i` is shared by two triangular faces exactly when both adjacent sectors are triangular:

```
shared(i) <=> t_(i-1)=1 and t_i=1.
```

Every D1 or D2 ray is shared. Every other ray is not shared.

Therefore a nonshared ray cannot lie between two shared rays. If rays `i-1` and `i+1` were shared, then the two sectors adjacent to ray `i` would both be triangular, forcing ray `i` itself to be shared.

This observation is independent of the source-scoped fan bound; it follows directly from the definition of a shared elementary segment.

## 2. Triple-point consequence

Retain the named triple-point local fan premise:

> no two D1 rays are cyclically consecutive.

Now exhaust the six sector bits and label the resulting shared rays as D1 or D2.

### Local counts (d1,d2)=(2,1)

There are three shared rays.

After imposing sector consistency and no consecutive D1 rays, every surviving local word has both D1 rays adjacent to the unique D2 ray.

Hence

```
blocked >= 2.
```

The earlier coarse lower bound zero was not false; it was only a bound on words before requiring them to arise from actual triangular sectors. Sector consistency sharpens it to two.

### Local counts (d1,d2)=(2,2)

There are four shared rays.

Again, every sector-consistent local word satisfying the no-consecutive-D1 premise has both D1 rays adjacent to at least one D2 ray.

Hence

```
blocked >= 2.
```

### Local counts (d1,d2)=(2,0)

The isolated-core case remains compatible with

```
blocked = 0.
```

The companion replay enumerates sector bits first, derives the shared-ray set, then assigns D1/D2 labels. It does not assume these strengthened blocked counts.

## 3. D2=1 single-edge form

The protected normal form has

```
degrees = (1,1,0,0)
D1 = 8
U = 0
D2 = 1.
```

The two degree-1 cores each contribute at least two blocked D1 targets:

```
B >= 4.
```

Therefore the clean-line charge capacity is at most

```
2U + D1 - B
<= 0 + 8 - 4
= 4.
```

The baseline clean-line lower bound is

```
18-(I-D2) = 18-(12-1) = 7.
```

Thus

```
7 > 4.
```

Contradiction.

## 4. D2=2 P3 plus isolated core

The degree sequence is

```
(2,1,1,0).
```

The degree-2 core contributes at least two blocked D1 targets, and each degree-1 endpoint contributes at least two more:

```
B >= 2+2+2 = 6.
```

With

```
D1=8,
U=1,
D2=2,
```

the charge capacity is at most

```
2+8-6 = 4.
```

The clean-line lower bound is

```
18-(12-2)=8.
```

Thus

```
8 > 4.
```

Contradiction.

## 5. D2=2 two-disjoint-edges form

All four cores have degree one:

```
degrees = (1,1,1,1).
```

Each contributes at least two blocked D1 targets:

```
B >= 8.
```

With

```
D1=8,
U=1,
```

the charge capacity is at most

```
2+8-8 = 2.
```

The clean-line lower bound remains eight.

Thus

```
8 > 2.
```

Contradiction.

## Cross-check on the protected P4 form

The same local refinement gives blocked count two at all four P4 cores, hence

```
B>=8,
capacity <= 2*2+8-8 = 4,
clean >= 9.
```

So the new local lemma independently strengthens the already protected P4 exclusion.

## Result

Conditional on the named source-scoped triple-point no-consecutive-D1 premise and clean-line charging map, **no q=4 score-95 profile-3333 form survives**.

Combined with the protected earlier reductions, any normalized `n=18,T=95` witness must have

```
q >= 5
```

finite multiple points.

The companion replay `ci/validate_openmath_h1_12_q4_sector_closure.py` reconstructs the sector-to-shared-ray relation and all three global budget contradictions.

## Claim boundary

The sector-consistency identity and its finite local consequences are independently reconstructed.

The conclusion remains source-conditional because the no-consecutive-D1 fan premise and clean-line charging map retain their protected source scope. This artifact does not prove `T<=94`, does not certify optimality of the 93 construction, and has no MATHCERT effect. The q>=5 residual remains open.
