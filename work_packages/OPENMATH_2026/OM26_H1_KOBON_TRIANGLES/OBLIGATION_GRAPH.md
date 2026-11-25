# OM26-H1 obligation graph

```text
H1-00 source lock [DONE]
       |
       v
H1-01 evaluator reproduction [DONE]
       |\
       | +--> H1-02 exact face criterion [DONE]
       |          |\
       |          | +--> H1-03 small-n census
       |          | +--> H1-04 local-move calculus
       |          | +--> H1-05 realizability / stretchability gate
       |          |
       |          +------> H1-06 diversified n=18 search [TRANCHE-2 DONE]
       |                         |
       +-------------------------+
                                 v
                         H1-07 independent adversarial replay [TRANCHE-2 DONE]
                                 |
                                 v
                         H1-08 candidate ladder
                                 |
                     +-----------+-----------+
                     |                       |
                     v                       v
              H1-09 CEI lanes          H1-10 MATHCERT packet
              (audit-gated)                  |
                                             v
                                   H1-11 live pre-submit concordance
```

## H1-00 — source and semantic lock

**State:** DONE. Bound to MATHFORGE protected commit `73f1890387eec56eb6be31f8c00f10b6a5a56383` and the exact blob identities in `HILL_LOCK.json`.

## H1-01 — evaluator reproduction

**State:** DONE. The independent exact scorer and authenticated AutoLab public working-tree evaluator both return 16 on the identical baseline `solution.json` (SHA-256 `fee1fa08e700ba5849c3d1849cc10d2d3a50a44b3d838d560cd08f9a0de2b271`). AutoLab public snapshot: `7d3f1d91dcb8`. Evidence: `BASELINE_INTERNAL_RECEIPT.json`, `BASELINE_AUTOLAB_RECEIPT.json`, run `36354367463` / job `108719011813`.

The AutoLab result is an unofficial local/public-tree score because private evaluator regression fixtures are not distributed. This is sufficient for the baseline semantic-concordance gate; it is not an official competition score.

## H1-02 — exact face criterion

**State:** DONE at Solve level. `FACE_CRITERION.md` proves the arrangement-edge/nondegenerate-3-cycle criterion. `kobon_direct_oracle.py` supplies an independent exact sign-based interior-crossing oracle. The bounded falsification campaign passed 210 exhaustive degeneracy-pool subsets, 360 seeded random exact arrangements across n=3..8, and the locked fixtures. MATHCERT adjudication remains separate.

## H1-03 — small-n census and motif discovery

Use small `n` as cheap exact regimes to validate the scorer, enumerate or sample arrangement types, and discover motifs that survive straight-line realizability. This is reconnaissance, not evidence that a small-`n` pattern extrapolates to `n=18`.

## H1-04 — local-move calculus

Characterize score changes under controlled operations: moving one line, changing slope/intercept order, creating or resolving concurrence, introducing or removing parallelism, and projective normalization. Record moves by exact before/after arrangements and changed face certificates.

## H1-05 — realizability / stretchability gate

Combinatorial or pseudoline search is permitted only as a proposal generator. Every promoted candidate must be realized by actual rational straight lines. Failure to realize a combinatorial arrangement is a route result and must be recorded.

## H1-06 — diversified n=18 construction search

**Tranche 1:** DONE. R-D exact local mutation (seed 3, 3000 iterations) produced score 86 at iteration 1443. R-G exact two-parameter structured search evaluated 525 cases and produced score 58 at alpha=-3, beta=20. Both exact candidates are preserved.

**Tranche 2:** DONE. Protected Forge literature reconnaissance identified the externally reported Johannes Bader 93-triangle order table. R-H reconstructed that order type as an explicit rational straight-line arrangement with small integer coefficients. Exact order constraints, direct-oracle face count, and authenticated AutoLab public-evaluator count all passed at 93. The reconstruction is GCL-generated and is not attributed as Bader's original coordinate realization.

## H1-07 — independent adversarial replay

**Tranche 1:** DONE. The independent direct-interior oracle and authenticated AutoLab public evaluator both returned 86 for R-D and 58 for R-G.

**Tranche 2:** DONE. The sourced-order verifier checked 282 exact adjacency constraints with minimum positive integer margin 19,680,000 and the three intended parallel pairs. The independent direct-interior oracle returned 93 and the authenticated AutoLab public evaluator returned 93 for the identical rational reconstruction. No discrepancy was observed. R-H is promoted to `campaign-best-observed = 93`; this is not a best-known, optimality, novelty, official competition, or certification claim.

## H1-08 — candidate ladder

Maintain a content-addressed sequence of campaign candidates. A candidate may replace the current campaign leader only after H1-07 passes. The label is `campaign-best-observed`, never `best-known` without separately sourced literature evidence.

## H1-09 — CEI bounded contributions

Potential zero-context tasks include proving the face criterion, finding exact counterexamples to scorer shortcuts, studying realizability of a fixed combinatorial arrangement, or searching a bounded parameter family.

**Gate:** no CEI dispatch may be issued until the standing CEI conformance audit passes against the candidate dispatch/bootstrap, RESULT/1 grammar, `governance/ns_ci_intake_pr_controller.json`, `.github/workflows/ns-ci-intake-pr-controller.yml`, and the human-readable CEI page at exact SHAs. Raw return/receipt remains evidence, not truth.

## H1-10 — MATHCERT handoff

For a construction claim, hand off the exact `solution.json`, source lock, score certificate, independent replay, dependency/tool provenance, and semantic-fidelity record. If an optimality/upper-bound theorem is later claimed, it is a separate Cert object.

## H1-11 — live pre-submit concordance

Immediately before competition submission, re-read the live AutoLab hill and compare line count, bounds, schema, scoring rule, arithmetic semantics, and evaluator/version identity against the Forge capture. Any drift reopens Forge before submission.


## H1-14 — Wolfram-assisted semialgebraic 94 search

**State:** TRANCHES 1-2 COMPLETE — NO 94 FOUND — BOUNDED NEGATIVE ROUTE EVIDENCE.

The protected 93 seed has no proper one-blocker missing triangular support: the nearest nonfaces are exactly 60 support triples with two blocking lines. The exact closest-cell layer generated 120 rational blocker representatives and 60 paired representatives; the best individual score was 90 and the best paired score was 89. A depth-one coupled subdivision then posed 2,040 single mutual-event transitions, of which 28 adjacent subcells were exactly feasible; the best score was 86.

Selected exact semialgebraic cells were independently instantiated with the hosted Wolfram Language connector over rational variables, then replayed by the GCL integer-determinant scorer. The raw four-variable hosted-kernel attempt failed as tooling and was recovered by event-cell decomposition; it is not infeasibility evidence.

The 4-5 active-line escalation gate is not triggered because no coupled witness is competitive with the protected 93 seed. The next route action is to feed the exact lost-face/event patterns into H1-04/H1-12 obstruction analysis and reopen deeper coupled CAD only if a structural argument identifies a specific cell.

These search results do not establish an upper bound, optimality of 93, novelty, or MATHCERT certification.


## H1-15 - compound order-type 94 construction search

**State:** COMPLETE - NO 94 FOUND - BOUNDED NEGATIVE ROUTE EVIDENCE.

H1-15 enlarges the construction move set rather than increasing the continuous dimension inside the exhausted H1-14 event cells. Compound projective macros are organized around an anchor line, may traverse score valleys without H1-13's drop=4 cutoff, and may use a bounded off-anchor bridge mutation. Only a combinatorial endpoint at score at least 94 is eligible for exact straight-line reconstruction and independent GCL replay. Failure is route evidence only.

The completed pass covered all 18 anchors, visited 38,718 beam states and 631,968 transitions, permitted one off-anchor bridge and imposed no affine-score drop cutoff. No combinatorial endpoint exceeded 93, so no exact reconstruction or promotion call was triggered. This does not exhaust all compound order types or prove an upper bound.

Tracker: #955.

## H1-16 - face-loss mining and 333344 obstruction

**State:** CONDITIONAL PAPER PROOF + FINITE REPLAY PASS; TRUSTED MATHEMATICAL ADAPTER/CERTIFICATION PENDING.

The H1-14 event-cell losses have been mined exactly. All 60 required single blocker exits lose exactly three seed faces and gain none; all 60 paired exits lose five old faces and gain exactly the intended target. This is seed-local evidence only.

Separately, the protected q=6 machinery reduces profile `333344` from 6,143 relaxed labeled candidates to 126 planarity/elementary-triangle-compatible states. Exact incidence-excess minimization leaves six equality cases, all `K3,3-e` with the missing edge between the two quadruple cores. Exhaustive minimum-cover replay forces one three-core line on each bipartition; a triple core would then lie on its three distinct D2 supports plus its bipartition line, contradicting multiplicity three. Conditional on the named six-core premises, `333344` is excluded.

The q=6 residual is now `333333`, `333334`; q>=7 remains open. No hill-global <=94 or MATHCERT claim follows.

Tracker: #956.
