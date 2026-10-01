# OPENMATH-2026 handbook compliance audit — five fixed packets

**Audit date:** 2026-10-01  
**Protected MATHSOLVE source bind:** `50b88f51032a14aeae5c3969e14dd8c5a8728bac`  
**Handbook:** https://rsihouse.ai/openmath/handbook.pdf  
**Packets audited:** H1, H2, H4, H5, H6

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
| H1 | Exact rational reconstruction of published Bader 93-line-order result; independent exact scorer and public evaluator concordance at 93 | Prior mathematics. No M1/M3A open-problem credit as currently framed. M2 is possible only for a genuinely new formalization/reconstruction contribution. | **NOT SUBMISSION READY; M2 REFRAME POSSIBLE** |
| H2 | W89911 exact finite six-state witness independently replayed at 89,911 steps / 185 ones / span 541 | Potential finite computational partial only if novelty/open-status review establishes a new eligible contribution. Current records do not establish that. | **NOT SUBMISSION READY; NOVELTY/STATUS GATE OPEN** |
| H4 | Event-window 23-rule exact Collatz modular-descent catalog with self-contained derivation/verifier | Potential original formalized partial if independently replayed and shown novel relative to the frozen baseline. | **NOT SUBMISSION READY; STRONGEST M1-PARTIAL SALVAGE CANDIDATE** |
| H5 | Retained rational CHSH approximation, ratio 275807/195025; no universal Grothendieck bound claimed | No current open-problem advance established. M2 is not established because the packet does not identify a new reusable formalization family. | **NOT SUBMISSION READY; HOLD UNLESS FORMALIZATION CASE IS ESTABLISHED** |
| H6 | Exact replay of Laderman rank-23 decomposition; core 729 Brent identities pass; later replay found defects in ancillary narrative/experiment | Explicit prior mathematics. No M1/M3A credit as currently framed. M2 is possible for a genuinely new exact reusable formalization after trimming unsupported ancillary claims. | **NOT SUBMISSION READY; M2 REFRAME POSSIBLE** |

## Common Section 8 failures

All five packets currently fail the minimum-packet gate in at least these common fields:

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

## H1 — Kobon triangles / Bader 93 reconstruction

### Evidence present

- Exact candidate payload: `RH_BADER_RECONSTRUCTION_093/solution.json`, SHA-256 `e606799ad6c1296deedb475440d1eecbe86daba8a3af625718f55726f93da4d5`.
- Source attribution is explicit: published Johannes Bader order type, reconstructed from `zegalur/line-order` at pinned commit `2631b8793eb351be2ad6b8a91b7194eeb67e25bb`.
- Independent direct exact oracle returns 93.
- Authenticated AutoLab public evaluator returns 93, explicitly unofficial because the public Hill copy omits organizer-private fixtures.
- Event-window reconstruction was protected in MATHSOLVE on 2026-09-27 after the common opening/status-freeze time.
- Existing claim ledger correctly marks the 93 reconstruction as operational validation with `mathematical_effect=false`.

### Handbook audit

| Gate | Status | Reason |
|---|---|---|
| Identifiable event-window work | PARTIAL | Event-window reconstruction is timestamped, but the packet does not state the competition baseline commit/new-work delta explicitly. |
| Novel open-problem result | FAIL | The 93-triangle mathematics is explicitly sourced prior work. Handbook §5/§6 forbids new open-problem credit for known mathematics. |
| M2 eligibility | PARTIAL | A new exact rational reconstruction/formalization may be a plausible M2 contribution, but the packet lacks a source-theorem/formalization target record, prior formal-library search, and explicit genuinely-new formal contribution. |
| Exact formal/computational artifact | PARTIAL | Exact scorer, exact coordinates, source-order replay, and independent direct oracle exist. The competition-facing exact formal statement, axioms/trust note, complete pinned environment and build/reproduction account are not consolidated. |
| Independent rerun/check | PASS at GCL evidence level | Direct oracle and public evaluator concordance exist. This is not the official competition checker. |
| Statement fidelity / attribution | PASS for the bounded claim | Claim boundaries explicitly deny novelty, priority, global best-known, or optimality. |
| §8 identity/provenance/publication packet | FAIL | Required entrant/class/contribution/publication fields are absent. |
| §7.2 submission identity/report | FAIL | No submission ID or official final evaluator report. |

### Correct competition claim

Do **not** submit H1 as "93 triangles discovered/solved." If pursued, the only defensible current route is an M2 claim centered on the **new exact rational reconstruction and reusable exact verification artifact**, with Bader and upstream source fully attributed.

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

## H4 — Collatz modular descent

### Evidence present

- Independent event-window return on 2026-10-01 derives 309 bounded valid rules and a deterministic 23-rule containment-reduced catalog.
- Each listed rule is accompanied by an exact affine descent derivation and a self-contained standard-library verifier.
- The returned result reports zero validity disagreements across 1,016 bounded candidate prefixes.
- Candidate payload SHA-256: `b14c4804dae95df88ffa7dcef865205edd295e1f2e8c4daeba75333053a6673a`.
- The returned claim boundary correctly denies global Collatz convergence, hidden-target coverage, novelty, competition acceptance, or certification.

### Handbook audit

| Gate | Status | Reason |
|---|---|---|
| Identifiable event-window work | PASS | The 23-rule catalog is a concrete event-window result. |
| Exact statement | PASS in returned evidence | The finite residue-class descent lemmas and bounded enumeration scope are precise. |
| Independent trusted rerun/check | FAIL | Current protected adjudication is explicitly `ACCEPTED_EVIDENCE_WITHOUT_CLAIM_PROMOTION`; no mathematical claim was promoted because a trusted replay adapter is still required. |
| Novelty/open-status relative to freeze | FAIL / UNESTABLISHED | No literature/status review establishes which, if any, of the 23 lemmas or the reduced catalog is new mathematical progress. |
| Potential original-partial modality | PARTIAL | This is structurally compatible with a formalized partial/finite result if novelty and target correspondence are established, but the packet does not record modality/family/admission. |
| §8 identity/provenance/publication packet | FAIL | Common fields absent. |
| §7.2 submission identity/report | FAIL | No submission ID or official final evaluator report. |

### Correct competition claim

H4 is the strongest current candidate for an **original formalized partial** because the mathematical content was produced during the event and is sharply bounded. Before cutoff it requires: trusted independent replay, exact target-correspondence note, freeze-date novelty/status review, explicit modality/family, and the full §8 packet.

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

## H6 — 3×3 matrix multiplication tensor / Laderman

### Evidence present

- The retained payload is the known Laderman rank-23 decomposition, SHA-256 `164aec58e19c2bdd45cddc54c52ab66f5f91f5d0562e875709b1c6eb820ac79f`.
- Event-window exact replay verifies all 729 Brent identities and support 153 for the Laderman certificate.
- Follow-up replay confirms the core decomposition but identifies a false ancillary claim in the predecessor narrative and an incompletely specified rational-sandwich experiment.
- Repository boundaries explicitly attribute Laderman prior work and deny rank-22, rank-minimality, novelty, and priority claims.

### Handbook audit

| Gate | Status | Reason |
|---|---|---|
| Identifiable event-window work | PASS for the replay/formalization | The exact verification work is timestamped in-window. |
| Novel open-problem result | FAIL | The actual rank-23 decomposition is explicit prior mathematics. Handbook §5/§6 excludes it from new open-problem credit. |
| M2 eligibility | PARTIAL | The exact rational verifier/certificate may support an M2 formalization claim, but the packet lacks the required source-theorem target, prior formal-library search, and explicit genuinely-new reusable formal contribution. |
| Exact artifact | PARTIAL | Core 729-identity replay is strong, but ancillary predecessor claims require trimming. Current automated adjudications preserve evidence without claim promotion. |
| Independent rerun/check | PARTIAL | WP02 independently replays the core tensor claims and finds defects outside the core. A clean competition artifact must contain only the surviving exact core claim and its complete replay environment. |
| §8 identity/provenance/publication packet | FAIL | Common fields absent. |
| §7.2 submission identity/report | FAIL | No submission ID or official final evaluator report. |

### Correct competition claim

Do not submit H6 as a new rank-23 result. If pursued, reframe it as an M2 candidate for the **new exact reusable formalization/replay of Laderman's known decomposition**, remove the false ancillary statement and incomplete rational experiment, document prior formal-library search, and supply the complete §8 packet.

## Pre-cutoff action order

The handbook makes the following distinction critical: metadata can sometimes be cured, but new mathematics, repaired proofs, and late formalization cannot be added after cutoff.

Therefore the mathematical work that must close **before** cutoff is:

1. **H4:** trusted independent replay; target correspondence; novelty/status review; formal modality/family classification.
2. **H1 and H6:** decide whether to pursue M2; if yes, complete the actual new formalization claim, prior-library search, exact source theorem attribution, and self-contained formal/replay artifact.
3. **H2:** perform freeze-date novelty/status review of the exact W89911 mathematical statement before spending effort on submission packaging.
4. **H5:** require a demonstrated eligible mathematical/formalization delta before further submission work; otherwise hold.

In parallel, prepare once for all surviving packets: roster/class, affiliation/resource classification, author/contribution statement, tool/compute disclosures, outside-help/conflict statement, explicit baseline/event delta, and publication authority.

## Audit conclusion

**Zero of the five fixed packets presently satisfy the handbook's complete score-bearing submission requirements.**

This does not mean zero useful work exists. It means the earlier label “five immutable packets ready to submit” was too coarse. The correct state is:

- **H4:** plausible original-partial candidate, mathematically incomplete for submission until replay + novelty/status close.
- **H1/H6:** prior-math artifacts that require explicit M2 reclassification and completion as new formalizations.
- **H2:** exact finite witness with replay, but score eligibility is unresolved until novelty/status is established.
- **H5:** valid bounded artifact, but no eligible competition contribution has yet been established.

The organizer submission-route defect remains real, but it is no longer the only blocker. The handbook's mathematical and packet-completeness gates must be satisfied independently.
