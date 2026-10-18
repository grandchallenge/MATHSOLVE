# H1 six-core replay closure: internal bounded evidence

**Record:** `OM26-H1-Q6-INTERNAL-REPLAY-001`  
**Source:** MATHSOLVE `99757ce4a816a2f845609d74d31fc0f86a7355a2`, `handoffs/OPENMATH-2026/launch/OM26-H1-WP02.md`  
**Executor:** current-context GCL internal executor. This is not an independent zero-context return and does not consume `OM26-H1-WP02-IA-001` or its first-result lock.

## Result and method

The embedded predecessor program was executed verbatim and reproduced all 14 coarse profiles, the five surviving profiles, and every stated graph count. A separate implementation in `ci/validate_openmath_h1_q6_replay.py` then visited all 32,768 labeled simple graphs directly. It uses integer sector masks and cyclic bit operations, rather than the predecessor's Boolean sector tuples, and counts each graph individually rather than multiplying a degree-vector histogram. Its output reproduces every protected count under the stated sector/fan/charge relaxation.

These are separate implementations in the same authoring system. They do not provide reserved mathematical independence. Both check the same declared relaxation; concordance does not prove that the relaxation faithfully models the geometry.

| Profile | Surviving D2 values under Euler bound |
|---|---|
| 333333 | 3 through 12 |
| 333334 | 5 through 12 |
| 333335 | 7 through 10 |
| 333344 | 6 through 10 |
| 333444 | 9 |

The remaining nine coarse profiles have no state in this relaxation. Without the Euler bound, the all-triple profile also has 105 graphs at D2=13 and 15 at D2=14. The slack-bearing all-triple star survives with D1=12, blocked=7, U=0. Thus the replay does not close q=6.

## Full graph planarity in the 333444 profile

All 70 survivors in this profile are cubic on six labeled vertices, with D2=9 and exact local totals D1=24, blocked=24, U=3. Exhaustive replay supplies a certificate for each graph: either a complete bipartition into two triples, or two disjoint triangles connected by a perfect matching.

Exactly 10 graphs are K3,3: an unordered partition of six labels into equal triples gives binomial(6,3)/2=10 choices. Such a graph cannot be the embedded elementary core graph. In a simple bipartite planar graph, every face has length at least four, so Euler's relation gives E<=2V-4=8; K3,3 has nine edges.

The remaining 60 graphs are triangular prisms. Choose the unordered pair of vertex triples in 10 ways and a matching between them in 3!=6 ways. Two concentric triangles with corresponding vertices joined give a planar embedding. The exhaustive certificates verify that these two classes cover all 70 graphs. Consequently full graph planarity reduces this profile from 70 to 60 labeled graph candidates. Graph planarity is weaker than compatibility with arrangement lines, prescribed multiplicities, ray orders and triangular-face semantics.

## Conditional saturation obligation

Retain the predecessor's charging assumptions explicitly. For 333444, total multiplicity I=21 and D2=9 imply h<=I-D2=12, so at least six of the eighteen arrangement lines are clean. The relaxed capacity is 2U+D1-blocked=6. If that charge map is valid, six clean lines must each consume one of the six available charge slots: h=12, exactly six clean lines, and all three unused segments receive both ordinary-endpoint charges. No D1 segment supplies an eligible clean-line charge slot. This is a necessary equality condition, not a proof of impossibility.

## Deterministic continuation

First resolve the six-core applicability of the no-long-run fan and clean-line charge map. If either premise fails, retain the exact counterexample and demote deductions that depend on it. Conditional on those premises, attack the prism case through global opposite-ray matching, line incidence and the saturated six-charge/three-unused-segment configuration. Preserve the all-triple star and other profiles as separate residuals; do not mistake closure of one profile for closure of q=6 or q>=7.

The existing independent Cert tracker [MATHCERT #345](https://github.com/grandchallenge/MATHCERT/issues/345) concerns `OM26-H1-CON-002`, the exact 93-triangle reconstruction. It does not certify these six-core premises. Its fresh non-authoring executor requirement remains unresolved.

## Reproduction and evidence

Run from the repository root:

```sh
python ci/validate_openmath_h1_q6_replay.py --verify-receipt work_packages/OPENMATH_2026/OM26_H1_KOBON_TRIANGLES/H1_Q6_INTERNAL_REPLAY_RECEIPT.json
python -m unittest ci.test_openmath_h1_12_q5_profiles -v
```

The durable JSON receipt carries the replay source hash, all profile counts, the all-triple witness, all 70 cubic graph certificates and unresolved premises. The existing Solve checks workflow already executes the extended test module; no new workflow or controller is introduced.

Same-system non-authoring read-only Adversary pass checked the graph classification, saturation arithmetic, relaxation scope and absence of a realizability inference. The Referee pass checked reproducibility, source identity, lease preservation and the separation from MATHCERT. These logical audits do not constitute independent Cert review.

No unconditional score upper bound, realizability theorem, certification, optimality, novelty, competition submission or external-agent launch is asserted. Existing historical records and claim ledger remain unchanged.
