# MS-MC-WP00 — MATHCERT handoff coverage

## Identity

- Parent audit: `grandchallenge/MATH-PROGRAMME#123`
- MATHSOLVE issue: `grandchallenge/MATHSOLVE#73`
- Governing Cert provider: `grandchallenge/MATHCERT` at merge `3854dd1b4f6e162a7e74c3da1993f022ee691e5e`
- Cert route registry: `governance/certification_routes.json`
- Cert route-registry Git blob: `065f0531e4d763b389b207d4922d5a85b4335ee3`

## Coverage

Every governed campaign now has one content-addressed MATHSOLVE-to-MATHCERT packet:

| Campaign | Packet state | Meaning |
|---|---|---|
| UC-001 | ready | Restricted Lean claims and bounded exact replay are packaged for intake. |
| NS-CI-001 | ready | Scaling and interface claims are packaged; the A2 bridge remains unproved. |
| HC-001 | ready | Statement identity, package arguments, and semantic replay are packaged. |
| BSD-001 | pending | The selected target is unproved and historical Solve work remains programme-embedded. |
| PNP-001 | pending | The terminal target is registered; no terminal proof packet exists. |
| RH-001 | pending | RH-T-000 is registered; no terminal proof packet exists. |
| YM-001 | pending | Open-status and gate claims are registered; continuum obligations remain open. |
| OZ-001 | pending | Intake incompleteness and irrationality proof debt are registered. |

A pending packet is an explicit not-ready record. It is not a MATHCERT submission or disposition.

## State semantics

- `pending`: packet records blockers and reopening conditions;
- `ready`: MATHSOLVE has constructed a complete packet against the pinned Cert contract;
- `submitted`: MATHCERT has acknowledged intake;
- `certified`, `qualified`, `rejected`, `proof_debt`: MATHCERT adjudicated the exact packet.

Judgment and Integration require an adjudicated state. `ready` and `submitted` cannot satisfy those gates.

Positive claim promotion requires `certified` or `qualified`. A rejected or proof-debt packet closes lineage but cannot support acceptance or combination.

## Validation

The reviewed validator:

- recursively validates all campaign manifests;
- validates all eight packet files against one schema;
- verifies packet and manifest Git blob identities;
- verifies the exact MATHCERT contract commit and registry blob;
- rejects orphan or missing campaign packets;
- rejects target-claim, status, route, or campaign mismatch;
- requires work-package certification ledgers to equal manifest packet artifacts;
- rejects pending packets without blockers;
- rejects intake states at Judgment and Integration.

## Claim boundary

Packet creation and schema success do not certify mathematics. MATHCERT remains the sole certification provider and has not adjudicated these newly created packets in this work package.
