# MS-ROUTE-STATE-001 — Producer handoff and Cert adjudication split

## Status

Protected governance mechanism, updated by `MS-UC-CLOSEOUT-001` after the bounded UC qualification and provider-identity correction.

## Problem

The existing campaign manifests preserve the status that MATHSOLVE assigned when it produced each MATHCERT handoff packet. That producer-origin status is part of the packet's content-addressed history.

A later MATHCERT review can change the current route disposition without changing the historical packet. The two states are therefore different:

- `handoff_state` records what MATHSOLVE submitted or had ready at the pinned producer revision;
- `route_state` records the current MATHCERT intake or adjudication disposition at the pinned Cert registry revision.

Using `handoff_state` as the JUDGMENT or INTEGRATION gate incorrectly rejects a later qualification unless the producer history is rewritten.

## Current exact authority

The current Cert overlay pins:

- repository: `grandchallenge/MATHCERT`;
- commit: `64e042ddb1147338ad7868a2847715fe7c1c079d`;
- path: `governance/certification_routes.json`;
- Git blob: `cf876f43ae824f965a3aedf411671c110c380028`.

The overlay is `contracts/mathcert_current_routes.json`. Its schema is `schemas/mathcert_current_routes.schema.json`.

The historical campaign manifests and handoff packets are not rewritten as adjudication records. Their older Cert-contract references remain provenance for the producer snapshot. They are not the current adjudication authority.

The UC manifest was separately repaired to correct the exact README artifact identity at its cited source commit. That provider-integrity repair does not change the immutable handoff status.

## Current route matrix

| Campaign | Producer handoff | Current Cert route | Qualification scope |
|---|---:|---:|---|
| UC-001 | ready | qualified | qualified_restricted_claims_only |
| NS-CI-001 | ready | qualified | qualified_interface_only |
| HC-001 | ready | ready | none |
| BSD-001 | pending | pending | none |
| PNP-001 | pending | pending | none |
| RH-001 | pending | qualified | qualified_interface_only |
| YM-001 | pending | pending | none |
| OZ-001 | pending | pending | none |

The UC qualification covers only two restricted Lean theorems and exact finite replay through `n <= 4`. `UC-FRANKL` and proof obligation `UC-P04` remain open, and the campaign remains ineligible for claim promotion.

The RH producer manifest contains a historical blocker stating that MATHCERT had not yet replayed the target. That sentence is true only at the manifest's producer revision. The current overlay supersedes it for present-state decisions: MATHCERT has qualified the exact interface, while `RH-T-000` remains unproved.

## Gate semantics

`ci/validate_current_cert_routes.py` defines the current gates.

- SPECIFICATION, REALIZATION, and CONFRONTATION require valid governed coverage.
- JUDGMENT and INTEGRATION require an adjudicated current `route_state`.
- CLAIM_PROMOTION requires both a positive current route state and `promotion.eligible: true` in the campaign manifest.

A restricted or interface-only qualification may pass its bounded JUDGMENT or INTEGRATION gate. It does not make the mathematical target true and does not make the campaign promotion-eligible.

## Fail-closed checks

The validator rejects:

1. an obsolete or mutated current MATHCERT registry identity;
2. missing or extra governed campaigns;
3. manifest or handoff Git-blob drift;
4. handoff state that differs from the immutable packet;
5. route state that differs from the pinned current matrix;
6. a positive route state without the exact campaign-specific Cert output and qualification scope;
7. an intake-only route carrying an adjudicated output;
8. any implication that the mathematical target is proved;
9. a campaign without current promotion blockers;
10. the superseded RH assertion that no independent replay has occurred;
11. regression of the corrected UC README identity or substitution of a different UC certificate.

Mutation tests cover producer/adjudicator substitution, stale UC provider identity, Cert-output substitution, qualification-scope drift, route-state regression, and qualification-to-proof inflation.

## Claim boundary

This work package governs producer history, current adjudication, and exact artifact identity. It does not prove any campaign target, convert restricted or interface qualification into theorem proof, change the eight-campaign active portfolio, admit VGSE-001, or authorize novelty, priority, patentability, mechanical, manufacturing, or commercial claims.
