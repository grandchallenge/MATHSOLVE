# MS-ROUTE-STATE-001 — Producer handoff and Cert adjudication split

## Status

Implementation candidate under MATHSOLVE issue #87 and MATH-PROGRAMME issue #178.

## Problem

The existing campaign manifests preserve the status that MATHSOLVE assigned when it produced each MATHCERT handoff packet. That producer-origin status is part of the packet's content-addressed history.

A later MATHCERT review can change the current route disposition without changing the historical packet. The two states are therefore different:

- `handoff_state` records what MATHSOLVE submitted or had ready at the pinned producer revision;
- `route_state` records the current MATHCERT intake or adjudication disposition at the pinned Cert registry revision.

Using `handoff_state` as the JUDGMENT or INTEGRATION gate incorrectly rejects a later qualification unless the producer history is rewritten.

## Current exact authority

The current Cert overlay pins:

- repository: `grandchallenge/MATHCERT`;
- commit: `0258e4f0bca0d90fac05b62aeef108f16dccffdd`;
- path: `governance/certification_routes.json`;
- Git blob: `5b3e8d48b9f6c5b03ed3dc439bf9e43876e017b1`.

The overlay is `contracts/mathcert_current_routes.json`. Its schema is `schemas/mathcert_current_routes.schema.json`.

The historical campaign manifests and handoff packets are not rewritten by this work package. Their older Cert-contract references remain provenance for the producer snapshot. They are not the current adjudication authority.

## Current route matrix

| Campaign | Producer handoff | Current Cert route | Qualification scope |
|---|---:|---:|---|
| UC-001 | ready | ready | none |
| NS-CI-001 | ready | qualified | qualified_interface_only |
| HC-001 | ready | ready | none |
| BSD-001 | pending | pending | none |
| PNP-001 | pending | pending | none |
| RH-001 | pending | qualified | qualified_interface_only |
| YM-001 | pending | pending | none |
| OZ-001 | pending | pending | none |

The RH producer manifest contains a historical blocker stating that MATHCERT had not yet replayed the target. That sentence is true only at the manifest's producer revision. The current overlay supersedes it for present-state decisions: MATHCERT has qualified the exact interface, while `RH-T-000` remains unproved.

## Gate semantics

`ci/validate_current_cert_routes.py` defines the current gates.

- SPECIFICATION, REALIZATION, and CONFRONTATION require valid governed coverage.
- JUDGMENT and INTEGRATION require an adjudicated current `route_state`.
- CLAIM_PROMOTION requires both a positive current route state and `promotion.eligible: true` in the campaign manifest.

A `qualified_interface_only` route may pass the interface-level JUDGMENT or INTEGRATION gate. It does not make the mathematical target true and does not make the campaign promotion-eligible.

## Fail-closed checks

The validator rejects:

1. an obsolete or mutated current MATHCERT registry identity;
2. missing or extra governed campaigns;
3. manifest or handoff Git-blob drift;
4. handoff state that differs from the immutable packet;
5. route state that differs from the pinned current matrix;
6. a positive route state without an exact Cert output and qualification scope;
7. an intake-only route carrying an adjudicated output;
8. any implication that the mathematical target is proved;
9. a campaign without current promotion blockers;
10. the superseded RH assertion that no independent replay has occurred.

Mutation tests cover the producer/adjudicator substitution that escaped the earlier validator.

## Claim boundary

This work package corrects governance-state representation. It does not prove any campaign target, convert interface qualification into theorem proof, change the eight-campaign active portfolio, admit VGSE-001, or authorize novelty, priority, patentability, mechanical, manufacturing, or commercial claims.
