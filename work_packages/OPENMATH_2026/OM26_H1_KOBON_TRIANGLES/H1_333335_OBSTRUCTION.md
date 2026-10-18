# H1 q=6 profile 333335 obstruction

**Record:** `OM26-H1-333335-OBSTRUCTION-001`  
**State:** `CONDITIONAL_PAPER_PROOF__FINITE_REPLAY_PASS__TRUSTED_MATHEMATICAL_ADAPTER_PENDING`

## Scope

Continue from the protected six-core necessary-state replay for an `n=18`, `T=95` normalized arrangement with six finite multiple points of multiplicities

```text
3,3,3,3,3,5.
```

As in the predecessor q=6 packet, this argument is conditional on the no-long-run local fan premise and the clean-line charging map in `H1_SIX_CORE_PREMISE_PROOF.md`. The pairwise-nonparallel scope is sufficient because `H1_PREMISE_SCOPE_DISPOSITION.md` binds the projective normalization bridge before these premises are used.

This tranche closes only profile `333335`. It does not close the other q=6 profiles or q>=7.

## 1. Exact finite reduction

The companion checker `ci/validate_openmath_h1_333335.py` independently re-enumerates all `2^15 = 32768` labeled simple graphs on the six cores and the exact sector-consistent local words used by the protected q=6 relaxation.

The relaxed profile has:

| D2 | graph candidates |
|---:|---:|
| 7 | 60 |
| 8 | 540 |
| 9 | 250 |
| 10 | 525 |

Total: `1375` labeled graph candidates.

The D2 graph is drawn by elementary straight segments, so it must be planar. In this six-vertex, at-most-ten-edge universe, Kuratowski's theorem makes planarity exact by checking for an unsubdivided `K5` or `K3,3`: a proper `K5` subdivision already has at least eleven edges, and a proper `K3,3` subdivision has at least seven vertices. The planarity filter leaves:

| D2 | planar candidates |
|---:|---:|
| 7 | 60 |
| 8 | 540 |
| 9 | 240 |
| 10 | 465 |

Next impose the elementary D2-triangle condition from `H1_SATURATED_PRISM_OBSTRUCTION.md`. If three D2 edges form a 3-cycle, then at each corner the two D2 rays bounding that geometric triangle must be adjacent in the full cyclic ray order. Otherwise an intervening arrangement ray meets the opposite elementary side in its relative interior.

The checker enumerates every exact sector-consistent local word, every assignment of the incident D2 graph edges to its D2 ray positions, and retains a graph only if every D2 3-cycle can satisfy that adjacency condition simultaneously with one of the protected global `(D1,B,U)` states.

After this filter:

```text
D2=7  -> 0
D2=8  -> 30
D2=9  -> 0
D2=10 -> 0
```

Thus only thirty labeled states remain.

## 2. The thirty survivors are exactly K3,3 minus one edge

Every survivor has

```text
D2 = 8
D1 = 20
B  = 16
U  = 1.
```

All thirty graphs are isomorphic to `K3,3-e`. The deleted edge has the quintuple core as one endpoint and one of the five triple cores as the other endpoint. Hence the degree pattern is:

```text
four triple cores: degree 3
one triple core:  degree 2
the quintuple core: degree 2.
```

For each labeled survivor the bipartition and deleted edge are unique. The thirty labelings are also counted directly: choose the degree-2 triple endpoint in `5` ways and then choose the other two triple cores on its side of the bipartition in `C(4,2)=6` ways, giving `5*6=30`.

## 3. Global equality fixes the local totals

For profile `333335`, total core multiplicity is

```text
I = 5*3 + 5 = 20.
```

At `D2=8`, the core-incidence inequality gives

```text
h <= I-D2 = 12,
```

so at least six of the eighteen arrangement lines are clean.

For every one of the thirty residual graphs the local dynamic program has exactly one assignment of `(d1(v),b(v))` summing to `(D1,B)=(20,16)`:

```text
four degree-3 triple cores: (3,3)
one degree-2 triple core:   (2,2)
degree-2 quintuple core:    (6,2).
```

The charge capacity is therefore

```text
2U + D1 - B = 2*1 + 20 - 16 = 6.
```

Clean-line demand and charge capacity are equal. Any realization must attain equality everywhere:

```text
h = 12,
clean = 6.
```

Recall why this matters. On a line containing `k` cores, at most `k-1` elementary segments can have two core endpoints. Summing over core-containing arrangement lines gives

```text
D2 <= sum(k-1) = I-h.
```

Equality `D2=I-h` means every repeated core-incidence saving is already accounted for by D2 elementary core-core segments. Any additional core-sharing line not decomposable into a consecutive chain of D2 segments makes this inequality strict.

## 4. Saturated triple cores force an extra core-pair line

At a degree-3 triple core the unique local totals are

```text
d2(v)=3, d1(v)=3, b(v)=3.
```

Exact sector enumeration leaves only the two rotations of the alternating six-ray word

```text
D1,D2,D1,D2,D1,D2.
```

Let `V` be any such degree-3 triple core, and take one of its D1 rays `VP`. The two neighboring rays are D2 rays ending at two D2-neighbor cores `A` and `B`.

Because `VP` is D1, it borders triangular faces on both sides. One of those triangles has sides on `VA` and `VP`; its opposite support is the arrangement line through `A` and the ordinary endpoint `P`. The other has sides on `VP` and `VB`; its opposite support is the arrangement line through `P` and `B`.

The point `P` is ordinary, so precisely one nonradial arrangement line passes through it. Therefore those two opposite supports are the same line:

```text
A, P, B are collinear on one arrangement line.
```

Thus an arrangement line joins the two D2 neighbors `A` and `B`.

In `K3,3-e`, the three neighbors of every degree-3 vertex lie in the opposite bipartition and are pairwise nonadjacent in the D2 graph. Hence this forced `AB` line is not itself a D2 edge. In fact the alternating word forces such a line for every pair among the three neighbors, but one is enough for the contradiction.

## 5. The forced line cannot hide inside a D2 chain

There is one remaining equality escape to exclude. A nonadjacent pair of cores could share a line without making `D2 < I-h` if the cores between them on that line formed a complete consecutive D2 chain. Every internal core of such a chain would have two antipodal D2 rays.

The finite local-word replay rules this out throughout the residual normal form:

- degree-3 triple state `(d2,d1,b)=(3,3,3)` has two alternating words and no antipodal D2 pair;
- degree-2 triple state `(2,2,2)` has eighteen sector-consistent words and none has antipodal D2 rays;
- degree-2 quintuple state `(2,6,2)` has ten sector-consistent words; its two D2 rays are adjacent, hence not antipodal.

Therefore no residual core can be an internal vertex of a collinear D2 chain. The forced line `AB` is a genuine additional core-incidence identification not accounted for by the eight D2 edges.

Consequently

```text
h <= 11.
```

Hence at least

```text
18-h >= 7
```

arrangement lines are clean, while the exact charge capacity is only six. Contradiction.

## Result

Conditional on the named six-core fan and clean-line charging premises, profile `333335` cannot realize an `n=18`, `T=95` arrangement.

The q=6 residual is reduced from

```text
333333, 333334, 333335, 333344
```

to

```text
333333, 333334, 333344.
```

No straight-line coordinate feasibility search remains for `333335`: the exact incidence obstruction eliminates the last thirty combinatorial survivors before that stage.

## Evidence

`H1_333335_OBSTRUCTION_RECEIPT.json` records:

- all 1375 relaxed labeled candidates;
- the exact planar counts by D2;
- the thirty post-triangle-filter survivors;
- the unique `K3,3-e` certificate for each survivor;
- the unique local `(D1,B)` assignment for each survivor;
- the no-antipodal-D2 local-word check;
- the exact `clean=capacity=6` equality antecedent.

Run:

```sh
python ci/validate_openmath_h1_333335.py
python -m unittest ci.test_openmath_h1_12_q5_profiles.H1333335ObstructionTest -v
```

## Claim boundary

This is a conditional Solve-level elimination, not a certification event. The finite checker verifies the exact graph/local-word reduction and all finite antecedents of the incidence proof. The real-geometric implication uses the paper-level fan/charging and ordinary-endpoint transverse-line arguments already declared in the predecessor chain.

It does not close q=6, address q>=7, prove a hill-global upper bound of 94, certify optimality of the 93-face construction, consume an external-agent lease, or submit anything to the competition.

The next internal target is profile `333344`, with `333334` and then `333333` retained as subsequent q=6 residuals unless a stronger common separator/incidence lemma collapses them together.
