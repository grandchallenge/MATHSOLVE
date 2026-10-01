# OPENMATH-2026 handbook compliance audit — seven hills

**Audit date:** 2026-10-01  
**Protected MATHSOLVE baseline bind:** `50b88f51032a14aeae5c3969e14dd8c5a8728bac`  
**Current protected closure head:** `187ce0debe76cb960724a6078b16660a11531941`  
**Handbook:** https://rsihouse.ai/openmath/handbook.pdf  
**Hills audited:** H1, H2, H3, H4, H5, H6, H7

## Controlling handbook gates

This audit applies the following competition requirements:

1. Only formalized results count; every accepted claim must pass an approved formal checker plus mathematical review of exact statement, novelty, scope, and attribution (§1).
2. Only identifiable mathematics contributed during the competition window counts as event output. Earlier mathematics remains prior work even if uploaded during the event. Pre-existing work requires a timestamped baseline commit and explicit new-work delta (§6).
3. Known mathematics receives no new open-problem credit. A new formalization of known mathematics may qualify for M2 if the formal contribution itself is new, faithful, useful, reusable, and made during the window; M2 requires identification of the source theorem, prior formal libraries searched, and the genuinely new formal contribution (§3.2, §5, §6).
4. Every score-bearing artifact needs the exact formal statement, pinned prover/library versions, reproducible build instructions, declared axioms/dependencies, code/certificates, and no proof holes or undeclared trust shortcuts. Computer-assisted work needs the precise reduction, environment, code/certificate, and independent rerun/check (§7.1).
5. Every claimed result must use the competition submission workflow and carry submission ID, Hill version/tree hash, Climb link, immutable final commit, and final evaluator report (§7.2).
6. The minimum packet must contain identity/target, artifact/proof, provenance, and publication-authority fields (§8).
7. New mathematics, repaired proofs, new theorems, or late formalization cannot be added after the final cutoff as an administrative cure (§8).

Status vocabulary: **PASS** = evidence sufficient at the audited source bind; **PARTIAL** = material evidence exists but the handbook packet is incomplete; **FAIL** = a required gate is presently unsatisfied; **N/A** = not applicable to the proposed classification.

## Executive disposition

| Hill | Current mathematical core | Competition classification at this bind | Audit disposition |
|---|---|---|---|
| H1 | Bader 93 payload is prior work, but event-window H1-12 accepted a source-conditional q≤5 exclusion for hypothetical score-95 arrangements; H1-13 adds bounded negative searches | Bader93 itself earns no event open-problem credit. H1-12 is a distinct event-window formalized-partial candidate, conditional on named predecessor premises. | **PARTIAL-RESULT CANDIDATE; NOVELTY/COMPETITION REVIEW PENDING** |
| H2 | W89911 exact finite six-state witness independently replayed at 89,911 steps / 185 ones / span 541 | Potential finite computational partial only if novelty/open-status review establishes a new eligible contribution. Current records do not establish that. | **NOT SUBMISSION READY; NOVELTY/STATUS GATE OPEN** |
| H3 | Exact weighted-K4 density oracles, structural identities, search representation, and a counterexample repairing an internal parameter-count claim | No canonical-target advance is currently established; no reference-beating certificate is retained. | **NO SCORE-BEARING TARGET ADVANCE; RESEARCH INFRASTRUCTURE ONLY** |
| H4 | Event-window 23-rule exact Collatz modular-descent catalog; trusted independent replay reconstructs 309 bounded rules and exactly the retained 23-rule reduction | Bounded exact formalized-partial candidate. Mechanism is prior mathematics; exact finite catalog novelty remains for competition review. | **TECHNICALLY CLOSED INTERNALLY; OFFICIAL ROUTE/HUMAN FIELDS PENDING** |
| H5 | Retained rational CHSH approximation, ratio 275807/195025; no universal Grothendieck bound claimed | No current open-problem advance established. M2 is not established because the packet does not identify a new reusable formalization family. | **NOT SUBMISSION READY; HOLD UNLESS FORMALIZATION CASE IS ESTABLISHED** |
| H6 | Exact replay of Laderman rank-23 support-153 decomposition | The organizer Hill itself identifies Laderman rank 23 as the supplied baseline and calls rank 22 or a new lower-support rank-23 decomposition progress. Our retained payload is therefore baseline prior work, not Hill progress. | **HOLD; NO SCORE-BEARING DELTA ESTABLISHED** |
| H7 | Both `ap_subprogression_of_le` and `ap_frequently_iff_every_length` are proved and pinned-compiled in Lean 4.33.1 with exactly the allowed axioms | Event-window formalization directly connected to the canonical target's conclusion; mathematical novelty is not claimed, and competition classification remains for review. | **D3/D4 FORMALLY CLOSED; HUMAN/EXTERNAL FIELDS PENDING** |

## Common Section 8 failures

All seven hill lanes currently fail the minimum-packet gate in at least these common fields:

- competition submission/version identifier;
- explicit problem/family ID in the competition namespace;
- explicit primary modality;
- registered human roster and entrant class;
- affiliation/resource classification;
- complete author/contribution statement;
- explicit baseline commit and event-window delta in competition terms;
- material AI/tool/compute/credit disclosure in one submission-facing record;
- outside-help/conflict disclosure;
- attribution approval and publication authority;
- competition submission ID;
- immutable competition final commit/report;
- official final evaluator report.

The absence of the organizer-published submission workflow is an external transfer blocker, but it does **not** excuse the internal mathematical/formalization gates. The artifacts must be complete before cutoff even if organizer reruns or administrative link repair happen later.

## H1 — Kobon triangles

### Two distinct tracks

The 93-triangle Bader reconstruction is explicitly prior work and is not claimed as an event discovery.

The event-window mathematics is separate:

- **H1-02:** the arrangement-graph face criterion is Solve-proof-complete and survived bounded falsification against 210 exhaustive degenerate subsets plus 360 seeded random arrangements.
- **H1-12 / OM26-H1-RED-023:** accepted source-conditional reduction. Conditional on the named predecessor local-fan/no-consecutive-D1 and clean-line charging premises, the sole q=5 score-95 equality normal form is unrealizable. Therefore any normalized n=18,T=95 witness satisfying those premises must have q>=6 finite multiple points.
- **H1-13:** three bounded search tranches found no score-94 candidate in their explicit neighborhoods. These are negative route evidence only, never an upper-bound proof.

Public freeze-date sources place n=18 at best-known 93 with upper bound 94. A scoped search found no exact published match for the q<=5 source-conditional exclusion; this is not proof of novelty.

### Handbook disposition

| Gate | Status | Reason |
|---|---|---|
| Event-window identifiable mathematics | PASS | H1-12 is timestamped, adjudicated, and materially narrows the hypothetical score-95 configuration space. |
| Exact statement/dependencies | PASS/PARTIAL | The accepted statement and predecessor dependencies are explicit. The dependencies remain source-scoped and must not be silently discharged. |
| Replay/falsification | PASS at Solve level | H1-12 adjudicator checks pass; H1-02 has independent exact oracle/falsification evidence. |
| Novelty/status | UNRESOLVED | No exact match found in scoped search, but competition mathematical review remains authoritative. |
| Prior-work separation | PASS | Bader93 is explicitly excluded from the event novelty claim. |
| §8 packet | PARTIAL | Technical draft exists; human roster/class/publication-authority fields remain pending. |
| §7.2 route/report | FAIL EXTERNALLY | Organizer competition workflow/submission ID/final report still absent. |

### Correct competition claim

If submitted, H1 should lead with the exact H1-12 source-conditional reduction, not the Bader93 construction. It must state literally that q>=6 remains open and that no global upper bound or optimality result follows.

## H2 — Busy Beaver 6 finite witness

### Evidence present

- W89911 is independently replayed under protected evaluator semantics: exactly 89,911 transitions, 185 ones, tape span 541, all six non-halting states reached.
- The result was captured during the competition window on 2026-09-29.
- The adjudication explicitly rejects the broader exact-search-validation claim and accepts only W89911 and W8021 as finite witnesses.
- Candidate payload SHA-256: `f8eaa4dbcbc3ecb18f8ddd1734cffe0079457ff3e26a51a25e81f3f6e988ead2`.

### Handbook audit

| Gate | Status | Reason |
|---|---|---|
| Identifiable event-window work | PASS | Return and accepted finite witness are timestamped during the window. |
| Exact statement | PASS | The bounded W89911 machine claim is precise and replayed. |
| Exact formal/computational artifact | PASS/PARTIAL | The finite witness itself has independent exact replay; the wider search proof was rejected and must not accompany the claim as established. Competition-facing environment/axiom/trust packaging remains incomplete. |
| Novelty/open-status relative to freeze | FAIL / UNESTABLISHED | Current records do not show the required literature/status comparison demonstrating that the accepted finite witness constitutes new mathematical progress rather than merely another valid lower-bound witness. |
| Modality/family/admission | FAIL | No explicit competition modality/family/admission record in the packet. |
| §8 identity/provenance/publication packet | FAIL | Common fields absent. |
| §7.2 submission identity/report | FAIL | No submission ID or official final evaluator report. |

### Correct competition claim

The only admissible H2 claim at this bind is the finite W89911 witness. The rejected exact-search claim must stay excluded. Do not claim open-problem progress until a freeze-date novelty/status review establishes that this witness advances an eligible registered target.

## H3 — Clique-cluster Ramsey multiplicity

### Evidence present

- WP01 built independent exact integer/rational density oracles for the weighted two-color blow-up (K_4) density and established extensive internal concordance and structural identities.
- The frozen reference comparison was implemented exactly, but no retained candidate beats the reference bound.
- WP02 found an exact counterexample to the predecessor's unrestricted finite-group parameter-count formula: for (H = \mathbb{Z}_2 \times \mathbb{Z}_2), the stated representation needs five independent parameters, not four. It supplies the corrected inversion-orbit count.
- Both protected adjudications are `ACCEPTED_EVIDENCE_WITHOUT_CLAIM_PROMOTION`; accepted mathematical claims remain empty.

### Handbook audit

| Gate | Status | Reason |
|---|---|---|
| Identifiable event-window work | PASS | The density-oracle work and parameter-count counterexample were produced during the competition window. |
| Canonical-target mathematical advance | FAIL | No reference-beating certificate, new Ramsey multiplicity bound, or other accepted advance on the registered target is established. |
| Auxiliary counterexample | PARTIAL / NARROW | The parameter-count counterexample repairs our own search representation. Under §5, refuting an auxiliary assertion earns only the narrower contribution; it does not refute the registered target. |
| Independent trusted replay/check | FAIL | Current automated adjudications preserve evidence without claim promotion; full protected evaluator concordance is not replayably established from the returned packet. |
| Novelty/open-status relative to freeze | FAIL / UNESTABLISHED | No literature/status review establishes an eligible new mathematical contribution. |
| Potential M3B route | UNESTABLISHED | A separately admitted nontrivial parent-linked variation would need its own canonical record and admission before scoring; none exists. |
| §8 identity/provenance/publication packet | FAIL | Common fields absent. |
| §7.2 submission identity/report | FAIL | No submission ID or official final evaluator report. |

### Correct competition claim

Do not submit H3 merely because the evaluator/search infrastructure is strong. At this bind there is no score-bearing advance on the canonical target. Continue H3 only if it can produce a reference-beating certificate, another directly relevant formalized advance, or a separately admitted nontrivial variation before cutoff.

## H4 — Collatz modular descent

### Evidence now closed

The retained payload contains 23 exact accelerated-Collatz residue-class descent rules. A second independent replay on PR #593 reconstructs the complete bounded search region k=2..8, depth=1..4:

- 1,016 candidate prefixes checked;
- 309 valid bounded rules;
- direct trajectory and independent affine-coefficient implementations agree;
- deterministic containment reduction reproduces exactly the retained 23 rules;
- full-catalog SHA-256 is `951521f5064f0842993e895648b2b8bde2b29dda0d47c9d586ddac498bfa4f55`;
- exact-head replay passes on GitHub Actions.

### Handbook disposition

| Gate | Status | Reason |
|---|---|---|
| Event-window work | PASS | The finite catalog/reduction was produced during the event. |
| Exact bounded statement | PASS | The 23 rules and bounded classification are exact. |
| Trusted independent replay | PASS | Full bounded catalog and reduction independently reconstructed. |
| Target correspondence | PASS | Rules are exactly the certificate type scored by the registered Hill. |
| Novelty/status | UNRESOLVED | Residue/stopping-time mechanisms are classical. No exact match for this 23-rule bounded reduced catalog was found in scoped sources, but absence is not proof of novelty. |
| §8 technical packet | PASS/PARTIAL | H4 Section 8-shaped technical draft exists; human authority fields remain pending. |
| §7.2 official route/report | FAIL EXTERNALLY | No organizer submission ID or official held-out report. |

### Correct competition claim

Present only the exact finite certificate collection and bounded classification. Do not claim a new general Collatz theorem or global convergence result. Competition review should determine whether the finite classification merits P1/P2 formalized-partial credit or overlaps prior work too heavily.

## H5 — Grothendieck witness

### Evidence present

- WP01 independently reproduced the organizer source example at ratio 7/5 and established source-example checker concordance.
- The later retained contest payload has ratio `275807/195025` and SHA-256 `72703ab868d55a460f8adbfdd137afbbdd044a0aea5f2267516c4805b541901e`.
- Repository boundaries explicitly state that the retained payload is a rational CHSH approximation and **not** a new universal Grothendieck bound.

### Handbook audit

| Gate | Status | Reason |
|---|---|---|
| Identifiable event-window work | PARTIAL | WP01 is timestamped in-window, but the current competition packet does not provide a complete derivation/provenance chain from WP01's replayed 7/5 source example to the later 275807/195025 retained payload. |
| Exact statement | PARTIAL | The finite witness ratio is pinned, but its submission-facing derivation and correspondence record are incomplete. |
| Independent trusted rerun/check | FAIL | WP01 automated adjudication preserved evidence without mathematical claim promotion pending trusted replay. The retained later candidate has no separate promoted replay record in the audited source. |
| Novel open-problem advance | FAIL / UNESTABLISHED | The packet expressly makes no new universal bound claim and contains no freeze-date novelty/status analysis establishing mathematical progress. |
| M2 eligibility | FAIL / UNESTABLISHED | No source-theorem formalization family, prior formal-library search, or genuinely-new reusable formalization contribution is identified. |
| §8 identity/provenance/publication packet | FAIL | Common fields absent. |
| §7.2 submission identity/report | FAIL | No submission ID or official final evaluator report. |

### Correct competition claim

Do not currently present H5 as an open-problem advance. It should remain on hold unless a genuine, reviewable M2 formalization contribution or other new eligible mathematical delta can be identified and completed before cutoff.

## H6 — 3×3 matrix multiplication tensor

The retained payload is exactly known Laderman rank-23 prior work with support 153. The organizer Hill itself states that Laderman rank 23 is the supplied baseline and identifies a rank-22 certificate or a new exact rank-23 decomposition with lower support as meaningful progress.

Our exact 729-Brent-identity replay is useful validation but does not create a competition delta. H6 is therefore **held**, not promoted as a score-bearing candidate. A separate M2 formalization route would require a genuinely new reusable formalization plus prior-library review; it is lower priority than H1/H4/H7.

## H7 — Erdős Problem 3

### H7-D3 formally closed

The direct bridge theorem

`ap_subprogression_of_le`

now has a complete no-`sorry` Lean proof. Exact pinned execution used Lean 4.33.1 in organizer image
`ghcr.io/ottogin/lean-mathlib@sha256:964547ad81e109c78545512867bae70b710c55d833078674878faad7de0ebb85`.

Exact-head run `36878983982`, job `110425613259`, passed. Lean printed exactly:

`[propext, Classical.choice, Quot.sound]`

which is the evaluator's full allowed axiom set. No proof hole remains.

H7-D4, the equivalence between frequently/unbounded AP lengths and existence of every exact finite AP length, has also passed pinned replay. Run `36879690920`, job `110427986166`, compiled D3 and D4 with no proof holes and exactly `[propext, Classical.choice, Quot.sound]`.

### Handbook disposition

| Gate | Status | Reason |
|---|---|---|
| Event-window formalization | PASS | D3 was constructed and proved during the competition window. |
| Exact pinned formal check | PASS | D3 and D4 both pass the exact Lean/image/axiom gate. |
| Direct target correspondence | PASS | D3 supports the canonical target's exact-length reformulation. |
| Parent conjecture solved | NO | The divergent-reciprocal-sum implication remains untouched. |
| Novelty/formal-library status | UNRESOLVED | No exact existing lemma was found in scoped source search, but that does not establish novelty. |
| D4 | PASS | Exact-length equivalence is pinned-compiled on top of D3. |
| §8 / official route | PARTIAL/EXTERNAL | Technical packet and official competition transaction still required. |

### Correct competition claim

D3 and D4 are narrow reusable formalization/reduction results, not a solution of Erdős Problem 3. They are plausible M2 or narrow formalized-partial artifacts if organizer novelty/usefulness review supports that classification.

## Pre-cutoff action order

The handbook makes the following distinction critical: metadata can sometimes be cured, but new mathematics, repaired proofs, and late formalization cannot be added after cutoff.

Therefore the mathematical work that must close **before** cutoff is:

1. **H4:** internal mathematical/replay gates closed; finish human Section 8 fields and official competition route/report.
2. **H1:** treat H1-12 as the event-window partial; finish novelty/status and Section 8 packet without conflating it with Bader93.
3. **H7:** D3 and D4 are formally closed; only organizer novelty/usefulness classification, human Section 8 authority fields, and the official competition route/report remain.
4. **H2:** retain only as a low-priority exact finite Hill artifact; it does not improve known BB(6) lower bounds.
5. **H3:** continue only if a canonical-target advance or separately admitted nontrivial variation emerges.
6. **H6/H5:** hold unless a genuinely eligible new delta is established.

In parallel, prepare once for all surviving packets: roster/class, affiliation/resource classification, author/contribution statement, tool/compute disclosures, outside-help/conflict statement, explicit baseline/event delta, and publication authority.

## Audit conclusion

**Zero of the seven hill lanes presently satisfy the handbook's complete score-bearing submission requirements.**

This does not mean zero useful work exists. It means the earlier label “five immutable packets ready to submit” was too coarse. The correct state is:

- **H4:** internally replay-closed bounded finite-classification candidate; external route/human fields remain.
- **H1:** Bader93 is prior work, but H1-12 is a distinct accepted event-window source-conditional partial candidate.
- **H7:** D3 and D4 are pinned-Lean proved with allowed axioms; technical formalization closure is complete.
- **H2:** exact finite witness but not a known-state BB(6) advance; low priority.
- **H3:** strong exact search/evaluator infrastructure but no current canonical-target advance.
- **H6:** retained payload equals the organizer's Laderman baseline; hold.
- **H5:** no eligible competition contribution established.

The organizer submission-route defect remains real, but it is no longer the only blocker. The handbook's mathematical and packet-completeness gates must be satisfied independently.
