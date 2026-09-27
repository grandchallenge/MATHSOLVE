# OM26-H1 obligation graph

```text
H1-00 source lock [DONE]
       |
       v
H1-01 evaluator reproduction [DONE]
       |\
       | +--> H1-02 exact face criterion
       |          |\
       |          | +--> H1-03 small-n census
       |          | +--> H1-04 local-move calculus
       |          | +--> H1-05 realizability / stretchability gate
       |          |
       |          +------> H1-06 diversified n=18 search
       |                         |
       +-------------------------+
                                 v
                         H1-07 independent adversarial replay
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

Derive a mathematically explicit criterion for when three supporting lines bound a counted triangular face. Candidate simplifications such as adjacency of pairwise intersection vertices along all three support lines must be proved under the hill's allowed degeneracies or falsified with exact counterexamples before becoming trusted scorer logic.

Output: theorem/lemma statement, exact proof or bounded counterexample ledger, and executable property tests.

## H1-03 — small-n census and motif discovery

Use small `n` as cheap exact regimes to validate the scorer, enumerate or sample arrangement types, and discover motifs that survive straight-line realizability. This is reconnaissance, not evidence that a small-`n` pattern extrapolates to `n=18`.

## H1-04 — local-move calculus

Characterize score changes under controlled operations: moving one line, changing slope/intercept order, creating or resolving concurrence, introducing or removing parallelism, and projective normalization. Record moves by exact before/after arrangements and changed face certificates.

## H1-05 — realizability / stretchability gate

Combinatorial or pseudoline search is permitted only as a proposal generator. Every promoted candidate must be realized by actual rational straight lines. Failure to realize a combinatorial arrangement is a route result and must be recorded.

## H1-06 — diversified n=18 construction search

Run distinct search families rather than duplicate whole-problem agents:

- exact local mutation around valid arrangements;
- continuous parameter search followed by exact rationalization and replay;
- combinatorial arrangement search followed by the realizability gate;
- structured parametric families and projective normal forms;
- literature-guided constructions only after source/provenance intake.

## H1-07 — independent adversarial replay

Use a scorer implementation or logic path independent of the proposal generator. Recheck input validity, line distinctness, candidate intersections, face boundedness, interior crossing/subdivision, and final triangle count.

## H1-08 — candidate ladder

Maintain a content-addressed sequence of campaign candidates. A candidate may replace the current campaign leader only after H1-07 passes. The label is `campaign-best-observed`, never `best-known` without separately sourced literature evidence.

## H1-09 — CEI bounded contributions

Potential zero-context tasks include proving the face criterion, finding exact counterexamples to scorer shortcuts, studying realizability of a fixed combinatorial arrangement, or searching a bounded parameter family.

**Gate:** no CEI dispatch may be issued until the standing CEI conformance audit passes against the candidate dispatch/bootstrap, RESULT/1 grammar, `governance/ns_ci_intake_pr_controller.json`, `.github/workflows/ns-ci-intake-pr-controller.yml`, and the human-readable CEI page at exact SHAs. Raw return/receipt remains evidence, not truth.

## H1-10 — MATHCERT handoff

For a construction claim, hand off the exact `solution.json`, source lock, score certificate, independent replay, dependency/tool provenance, and semantic-fidelity record. If an optimality/upper-bound theorem is later claimed, it is a separate Cert object.

## H1-11 — live pre-submit concordance

Immediately before competition submission, re-read the live AutoLab hill and compare line count, bounds, schema, scoring rule, arithmetic semantics, and evaluator/version identity against the Forge capture. Any drift reopens Forge before submission.
