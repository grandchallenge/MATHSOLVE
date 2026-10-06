# OM26-H1 H1-14 — exact semialgebraic construction squeeze

**Tracker:** #935  
**Protected predecessor:** `MATHSOLVE/main@9a663535a86ec82521b69a8ef96d444e7e2b9c4c`  
**Seed:** `RH_BADER_RECONSTRUCTION_093`  
**Seed blob:** `bb244e4b0422922ae9f85cc4facb2109c33162b3`  
**State:** `TRANCHE1_EXECUTED__NO_94__EXACT_NEGATIVE_ROUTE_EVIDENCE`

## Purpose

H1-13 retained three bounded searches around the verified score-93 arrangement and found no score-94 proposal. H1-14 adds an exact continuous-geometry layer between discrete proposal generation and the existing exact GCL scorers.

Wolfram is used only to answer exact semialgebraic feasibility questions. It is not a scorer, a proof authority, or a certification surface.

## Pipeline

```text
protected 93 seed
  -> deterministic near-miss atlas
  -> abstract determinant-sign cell scoring
  -> exact Wolfram Resolve / FindInstance
  -> rational line witness, if any
  -> GCL exact scorer
  -> independent replay only if score >= 94

infeasible cell
  -> retained bounded obstruction / route evidence
```

## W0 — seed lock

The tranche is bound to the protected 18-line rational seed in
`candidates/RH_BADER_RECONSTRUCTION_093/solution.json`. The ordinary exact
proposal scorer returns 93 before any search action.

All seed lines use the normalization `[a,-1000,c]`, so a moving line may be
written `[m,-1000,b]`. Passing through a fixed arrangement vertex and becoming
parallel to a fixed line are therefore polynomial/linear wall events in
`(m,b)`.

## W1 — near-miss atlas

`H1_14_NEAR_MISS_ATLAS.json` exhausts all `C(18,3)=816` triples at the seed.

It records:

- 93 counted triangular faces;
- 48 improper triples (parallel pair or concurrence in the defining triple);
- 675 proper nonfaces;
- no proper nonface with exactly one blocking line;
- exactly 60 proper nonfaces with exactly two blocking lines.

For each two-blocker target the atlas identifies the unique single determinant
sign that each blocker must cross to stop cutting the target triangle, records
the exact wall coefficients/distance proxy, and evaluates the corresponding
abstract orientation cell.

A key structural result is uniform across all 60 cases:

- flipping either blocker wall alone gives abstract score 90;
- flipping both minimal blocker walls gives abstract score 89.

Thus a score-94 construction cannot be obtained merely by opening one of the
nearest missing faces while holding all other oriented relations fixed.

## W2 — Wolfram translation cross-check

`wolfram_94_semialgebraic.py` emits exact `Resolve`/`FindInstance` problems
using the same determinant signs as the protected Python wall search.

For one moving line the generated system fixes every pairwise
parallel/nonparallel sign and every triple determinant sign except explicitly
declared wall crossings. For multiple moving lines, determinant constraints
containing more than one moving line remain symbolic and are solved jointly.

The first large direct four-variable CAD attempt was factored rather than treated
as a blocker. Exact single-line feasibility was solved first, and only a target
whose two blocker exits were independently feasible was promoted to a coupled
four-variable solve.

## W3 — ranked exact single-blocker tranche

The ten two-blocker targets closest by the deterministic wall-distance proxy
were tested, for 20 required blocker exits total.

Exact `Resolve[Exists[..., Reals]]` dispositions:

- 14 required single-blocker cells are infeasible;
- 6 are feasible;
- only target `[0,4,14]` has both required blocker exits independently feasible.

The exact inputs and dispositions are retained in
`H1_14_WOLFRAM_TRANCHE1_RECEIPT.json`.

## W4 — first coupled four-variable cell

For target `[0,4,14]`, move lines 6 and 11 while preserving all seed
orientation signs except:

- `[0,6,14]`;
- `[0,4,11]`.

Wolfram found the rational witness

```text
line 6:  [430,-1000,-217]
line 11: [-489,-1000,-1969/1406]
```

which is materialized integrally as

```text
line 11: [-687534,-1406000,-1969].
```

Exact GCL rescoring gives 89, agreeing with the abstract-cell prediction.

This is useful negative evidence: the exact cell exists geometrically, but the
minimal coordinated wall crossing loses five net faces relative to the seed.

## W5 — bounded repair prefilter

For the same first coupled target, the discrete orientation prefilter was
expanded by allowing, independently for each moving blocker, either no extra
determinant wall or one additional determinant wall beyond the two required
exits.

This exhausts `120 x 120 = 14,400` abstract cells in that bounded repair
neighborhood. The best abstract score remains 89. Therefore none is eligible
for costly four-/five-line symbolic escalation under the tranche rule.

## Escalation rule

A higher-dimensional Wolfram solve is launched only when the abstract
orientation cell can reach at least 94. This tranche produced no such cell, so
the authorized W4/W5 escalation gate correctly remained closed.

The next construction search should enlarge the topology move set rather than
increase continuous optimization dimension inside this exhausted local family.

## Interaction with H1-12

Negative semialgebraic cells may suggest incidence lemmas for the separate
score-95 upper-bound route, but no H1-14 search result is automatically imported
as an H1-12 theorem. Proof, independent replay, and MATHCERT boundaries remain
unchanged.

## Claim boundary

This tranche establishes only bounded route evidence around the protected
score-93 seed. It does **not** prove that 94 is impossible, that 93 is optimal,
or that the reported upper bound 94 is valid for the unrestricted hill semantics.
No Wolfram output has certification authority.
