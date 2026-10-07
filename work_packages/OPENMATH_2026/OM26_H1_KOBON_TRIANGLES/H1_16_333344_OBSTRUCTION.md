# H1-16 — H1-14 face-loss mining and q=6 profile 333344 obstruction

**Trackers:** #956
**Protected predecessor:** MATHSOLVE/main@5c11f38912d96b63e42340d3207a2467be8b9441
**State:** CONDITIONAL_PAPER_PROOF__FINITE_REPLAY_PASS__TRUSTED_MATHEMATICAL_ADAPTER_PENDING

## Scope

This tranche has two logically separate outputs.

First, it mines the exact H1-14 determinant-wall data around the protected 93-triangle seed for reusable local motifs. Those observations are seed-local and are not promoted to general theorems.

Second, it continues the protected H1-12 six-core programme for profile

```text
3,3,3,3,4,4.
```

The profile elimination remains conditional on the six-core no-long-run fan and clean-line charging premises already recorded in `H1_SIX_CORE_PREMISE_PROOF.md`, together with the elementary-D2 planarity/triangle-adjacency and ordinary-endpoint transverse-line arguments used in the protected predecessor chain.

## A. Exact H1-14 face-loss motif

`mine_h1_14_face_losses.py` exhausts the sixty distinct determinant walls used to open the sixty closest two-blocker nonfaces in the protected 93 arrangement.

For every one of the sixty single wall crossings:

- the abstract score changes from 93 to 90;
- exactly three existing triangular faces are lost;
- no new triangular face is gained;
- each lost face shares exactly two lines with the flipped determinant triple.

Moreover, the three lost faces cover the three two-line subsets of the flipped triple one-for-one.

For every one of the sixty paired blocker exits:

- the intended target triangle is gained;
- exactly five old faces are lost;
- the two single-wall three-face loss sets overlap in exactly one old face;
- the resulting abstract score is therefore 89.

This is a uniform exact pattern in the protected seed's orientation cell. It is retained as a conjecture generator only. No claim is made that every determinant-wall crossing in every high-scoring arrangement pays the same toll.

## B. Finite reduction for profile 333344

The checker `ci/validate_openmath_h1_333344.py` independently visits all `2^15 = 32768` labeled simple graphs on six cores and reuses the exact local fan-word machinery of the protected q=6 replay.

The protected relaxation contains:

| D2 | relaxed labeled candidates |
|---:|---:|
| 6 | 327 |
| 7 | 765 |
| 8 | 2464 |
| 9 | 1510 |
| 10 | 1077 |

Exact six-vertex planarity reduces only the last two rows:

| D2 | planar labeled candidates |
|---:|---:|
| 6 | 327 |
| 7 | 765 |
| 8 | 2464 |
| 9 | 1500 |
| 10 | 1017 |

Imposing the elementary-D2-triangle adjacency condition leaves only:

```text
D2 = 7 : 36 labelings
D2 = 8 : 90 labelings
```

Thus 126 labeled states remain.

Their D2 graphs have only two structural forms:

1. `D2=8`: `K3,3 - e`.
2. `D2=7`: `K3,3` with two adjacent edges deleted.

For the `D2=8` states the missing edge has multiplicity roles:

```text
triple--triple       36
triple--quadruple    48
quadruple--quadruple  6
```

The `D2=7` states split according to the multiplicity of the common endpoint of the two missing edges, exactly as recorded in the receipt.

## C. Forced neighbor-pair lines and incidence excess

Whenever a D1 ray is flanked by two D2 rays at a core, the ordinary far endpoint of that D1 side is shared by the two adjacent triangular sectors. Ordinariness forces their opposite supports to be the same arrangement line. Hence the two corresponding D2-neighbor cores lie on one arrangement line.

The checker enumerates every compatible local word and every assignment of D2 neighbors to D2 ray positions. It records all such forced neighbor-pair collinearities.

A raw count of forced pairs is not enough: several pairs may lie on one full arrangement line, and existing D2 elementary edges can form collinear chains. To avoid overcounting, the checker solves an exact finite line-cover relaxation.

For each residual state it allows every favorable collinearity compatible with:

- the forced neighbor-pair relations;
- all existing D2 edges;
- degree at most two for D2 edges carried by one line;
- no D2 cycle on one line;
- antipodal D2 continuation at every internal core of a collinear D2 chain;
- distinct full lines sharing at most one core.

For a line block containing `k` cores and `e` D2 elementary edges, its excess cost is

```text
(k - 1) - e.
```

Summed over the cover, this is a lower bound on the strictness of

```text
D2 <= I - h.
```

All residual states are eliminated immediately when this minimum incidence excess exceeds the clean-line charge slack, except six labeled equality cases.

## D. Unique equality normal form

The six equality cases all have

```text
D2 = 8
D1 = 20
B  = 16
U  = 3
slack = 4.
```

Their D2 graph is `K3,3-e`, and the missing edge joins the two quadruple cores. Therefore the four triple cores have D2-degree three and the two quadruple cores have degree two.

The local totals are uniquely

```text
four triple cores:     (d1,b) = (3,3)
two quadruple cores:   (d1,b) = (4,2).
```

For these local states:

- no D2 pair can continue antipodally through a core;
- the forced neighbor-pair set is independent of the admissible local-word choice;
- the exact minimum incidence excess is four;
- exhaustive enumeration of **every** cost-four line cover gives a unique labeled normal form.

That normal form consists of:

- eight separate D2 edge-support lines; and
- one three-core line through each of the two `K3,3` bipartitions.

No alternative cost-four cover survives the finite constraints.

## E. Final multiplicity contradiction

Take any triple core `V` in an equality candidate.

Its three D2 neighbors are exactly the three cores in the opposite `K3,3` bipartition. The unique equality line cover puts those three opposite cores on one full arrangement line `L`.

The three D2 elementary segments from `V` to those three distinct points lie on three distinct arrangement lines through `V`: if two used the same support, that support would meet `L` in two distinct points and hence coincide with `L`, forcing `V` onto `L` and destroying the elementary D2 configuration.

The equality cover simultaneously puts `V` on the full arrangement line through the other two cores in its own bipartition. This line is distinct from the three D2 supports.

Hence at least four distinct arrangement lines pass through `V`, contradicting that `V` is a triple point.

Therefore the six equality candidates are impossible.

## Result

Conditional on the named protected premise chain, profile `333344` cannot realize an `n=18, T=95` arrangement.

The q=6 residual is reduced from

```text
333333, 333334, 333344
```

to

```text
333333, 333334.
```

## Evidence

Run:

```sh
python work_packages/OPENMATH_2026/OM26_H1_KOBON_TRIANGLES/mine_h1_14_face_losses.py --output /tmp/h1_16_face_loss.json
python ci/validate_openmath_h1_333344.py
```

Durable evidence:

- `H1_16_FACE_LOSS_MINING.json`
- `H1_333344_OBSTRUCTION_RECEIPT.json`

## Claim boundary

The H1-14 face-loss motif is seed-local evidence only. The 333344 result is a conditional Solve-level elimination under the explicitly named six-core geometric/charging premises. It does not close q=6, address q>=7, establish a hill-global upper bound of 94, prove optimality of the 93 construction, establish novelty or priority, consume a reserved independent-agent disposition, or constitute MATHCERT certification.
