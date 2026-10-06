# H1-14 — Wolfram-assisted semialgebraic 94 search

**Protected reconciliation base:** `MATHSOLVE/main@91c4a7879ad5b51077fdba9cb1f5e9367bc4a7e0` (research initiated at `9a663535a86ec82521b69a8ef96d444e7e2b9c4c`; prior fresh rebase `92bc84a2e5dd34ccb68c4db6ed035a30f63b6117`)  
**Seed:** `RH_BADER_RECONSTRUCTION_093`, SHA-256 `e606799ad6c1296deedb475440d1eecbe86daba8a3af625718f55726f93da4d5`  
**Authority:** MATHSOLVE proposal/search route only. No certification or optimality authority.

## Objective

Search for an exact rational 18-line arrangement with at least 94 counted bounded triangular faces by using Wolfram for semialgebraic feasibility between combinatorial proposal generation and the existing exact GCL scorers.

The route does not ask Wolfram to optimize all 54 homogeneous coefficients. The protected 93 seed has line form `[a_i,-1000,c_i]`, so a moving nonvertical line is represented by the two exact parameters `(m,b)` in `[m,-1000,b]`.

## Pipeline

1. Lock and replay the protected 93 seed.
2. Build an exact near-miss atlas over all support triples.
3. Rank the closest missing faces by blocking-line event distance.
4. Express target-vertex crossings, parallelism, and fixed-vertex concurrence as exact polynomial/linear conditions.
5. Use Wolfram `FindInstance`/`Reduce` over `Rationals`/`Reals` for selected cells and coupled cells.
6. Rationalize every feasible witness immediately.
7. Run the existing exact determinant scorer; any score >=94 must additionally pass the independent direct oracle and the external evaluator before campaign promotion.
8. Preserve exact infeasible/negative cells as route evidence and feed reusable incidence obstructions to H1-12.

## Event geometry

For a moving line `L=(m,-1000,b)` and two fixed lines `Lj=(a_j,-1000,c_j)`, `Lk=(a_k,-1000,c_k)`,

```text
det(L,Lj,Lk)/1000
 = (c_j-c_k)m + (a_k-a_j)b + (a_j c_k-c_j a_k).
```

Thus every fixed-vertex concurrence wall is a line in `(m,b)` parameter space. Parallelism with fixed line `j` is `m=a_j`.

The protected seed contains three intended parallel pairs, so a local route must distinguish retaining the parallel wall from entering either adjacent open half-plane.

## Tranche 1: exact near-miss and closest dual cells

`build_94_near_miss_atlas.py` deterministically regenerates the full exact protected near-miss atlas; `H1_14_NEAR_MISS_ATLAS_SUMMARY.json` durably records its aggregate invariants. There is no proper support triple blocked by only one line. The nearest nonfaces are 60 triples blocked by exactly two lines.

`search_94_dual_cells.py` crosses, for each blocker, the unique target-vertex wall that removes its crossing. Along that wall it computes the exact one-dimensional event decomposition and chooses an open segment minimizing changes to all other fixed-arrangement event relations. It then steps rationally into the target-unblocked side and rescales to an integer line.

This is intentionally a bounded first layer. Two independently selected blocker cells have a four-dimensional Cartesian product that can be further cut by their mutual parallel/concurrence surfaces. Therefore one canonical paired representative does not exhaust the coupled product cell.

## Wolfram validation

The hosted Wolfram kernel independently validated representative linear semialgebraic cells with exact `FindInstance[..., Rationals]`:

- an adjacent target-wall cell with no additional fixed event change;
- a target-wall cell requiring one additional fixed-vertex event change;
- a target-wall cell requiring release of one protected parallel relation.

The exact GCL scorer then rescored the resulting rational line replacements. These validation witnesses are recorded in `H1_14_WOLFRAM_VALIDATION.json`.

A raw four-variable formula requiring all 93 old faces plus the proposed 94th face was too large for the hosted kernel in one call. Under the continuity doctrine this was treated as a recoverable tooling failure, not a stopping condition; the route was factored into exact dual cells and the coupled-cell layer below.

## Tranche 2: coupled-cell subdivision

For the highest-ranked products from Tranche 1:

1. retain both individual blocker cells as exact linear inequality systems;
2. add the mutual blocker-blocker parallel wall and the 16 fixed-line concurrence surfaces `det(Lp,Lq,Lj)=0`;
3. enumerate feasible adjacent coupled subcells with Wolfram;
4. obtain exact rational witnesses;
5. exact-rescore each witness;
6. recursively expand only subcells whose score is competitive with 93.

The coupled surfaces are the only new event geometry after the individual cells are fixed. This prevents a return to blind four-dimensional coefficient gridding.

## Promotion gate

A Wolfram result is proposal evidence only. A candidate with score >=94 must satisfy:

```text
exact rational 18-line artifact
→ primary exact scorer >=94
→ independent direct oracle agrees
→ external evaluator replay agrees
→ exact-head protected review
```

No negative search result establishes `K(18)<=93` or `K(18)<=94`.

## Current result

The full 60-target canonical closest-cell replay is negative: best individual representative 90; best canonical paired representative 89.

The depth-one mutual coupled-cell subdivision is also complete: 2,040 single mutual-event flips were posed across the 60 products, 28 adjacent coupled subcells were exactly feasible, and the best exact score was 86. Because this layer produced no witness competitive with the protected 93 seed, the planned 4–5 active-line escalation gate is **not triggered**. Deeper coupled CAD remains available only if a later structural argument identifies a particular product cell worth reopening.

The construction route therefore hands its exact lost-face/event patterns back to H1-12/local-move analysis while preserving all negative receipts. None of these negative searches is an upper-bound or optimality proof.

## Tranche 3: strict-cell quantifier elimination

The ten closest two-blocker targets were ranked by the sum of the blocker-to-required-wall distances in the normalized `[m,-1000,b]` chart. For each of their 20 blocker exits, `h1_14_resolve_queries.py` generates the strict sign cell that preserves every seed pair/triple orientation involving the moving line except the one required target-vertex determinant sign.

The hosted Wolfram kernel evaluated these cells with exact
`Resolve[Exists[{m,b}, constraints], Reals]`. Fourteen strict cells are empty and six are nonempty. Only target `[0,4,14]` has both strict exits independently nonempty.

The corresponding joint four-variable strict cell is itself rationally realizable:
line 6 may be replaced by `[430,-1000,-217]` and line 11 by
`[-687534,-1406000,-1969]`. Exact GCL rescoring gives 89.

This strengthens the local diagnosis without changing the promotion posture:
merely removing both target blockers while preserving all other seed orientation
relations cannot produce 94. A successful nearby construction must cross
additional event walls. The exact booleans and witness are retained in
`H1_14_RESOLVE_CLASSIFICATION.json`.

These are strict-cell statements only. A `False` result does not exclude paths
that cross additional event walls, and no result is an upper-bound or
certification claim.
