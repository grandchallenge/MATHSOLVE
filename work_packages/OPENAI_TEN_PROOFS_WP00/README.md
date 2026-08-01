# OPENAI-TEN-PROOFS-WP00 — Semantic audit route

## Current status

`semantic_audit_authorized_no_handoffs`.

The original `pre_route_candidate.json` is retained as the historical intake record. The current state is governed by `umbrella_sync.json`.

## Current authority

- MATHFORGE evidence merge: `72452f4579749448169cacf9f2ab22a4df2bb182`;
- official root: `e62211d28e3a9131950c89caa6542cfe5eff3bca`;
- official tree: `2f8e7ac5ae7f157b6b1de636c2c343b1c7a7e365`;
- review-remedy merge: `bffb7d63476d79e86665ec5a74d554794e24357e`;
- Programme synchronization tracker: MATH-PROGRAMME #200;
- semantic audit tracker: MATHFORGE #50.

The disconnected root `6fefffdbab0dfa726fcfde6cefae23aa7a1888f3` remains historical intake evidence only.

## Replay and semantic gates

Trusted replay is clear for 12/12 corrected result-family configurations, including 8,710 elaboration jobs, 12/12 Comparator passes, 12/12 Lean-kernel acceptances, 9/9 required Nanoda acceptances, and 41/41 theorem-level axiom reports.

Source acquisition is present. Source-to-Lean semantic equivalence and nonvacuity remain clear for 0/12 result families.

MATHSOLVE may now participate in result-family concordance work, but it may not emit a MATHCERT handoff until the individual family clears both replay and semantic/nonvacuity review.

## First semantic tranche

1. `OTP-F-EHRHART`
2. `OTP-J1-COMPACTNESS`
3. `OTP-J2-TWO-DEGENERATE`

Permanent and GapCVP remain blocked repair lanes.

## Aggregate integration debt

The `All.lean` namespace collision on `replicate_to_periodic_packing` remains a separate integration obligation. It does not reopen the successful corrected-target replay and does not clear any semantic gate.

## Routing boundary

- statement concordance may begin;
- result-family MATHCERT handoffs: zero and prohibited until individual clearance;
- aggregate MATHCERT handoff: prohibited;
- statement-equivalence claims: prohibited until governed clearance;
- mathematical-result promotion: prohibited.

## Claim boundary

This package governs semantic-audit readiness. It is not an active campaign manifest, MATHCERT handoff, certification output, source-equivalence finding, proof, novelty record, or aggregate “ten proofs certified” claim.
