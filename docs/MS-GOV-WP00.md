# MS-GOV-WP00 — MATHSOLVE Handoff and Conformance Upgrade

## Result

MATHSOLVE now has a repository-local governing specification aligned with the canonical MATH-PROGRAMME doctrine, recursive campaign manifests for all eight active campaigns, generalized programme-reference validation, exact GitHub lineage requirements, and a standard MATHCERT handoff packet.

## Campaign coverage

Native MATHSOLVE coverage:

- `UC-001`;
- `NS-CI-001`;
- `HC-001`.

Retrospective registration of Programme-embedded Solve work:

- `BSD-001` under issue #66;
- `PNP-001` under issue #67;
- `RH-001` under issue #68;
- `YM-001` under issue #69;
- `OZ-001` under issue #70.

Retrospective registration preserves exact historical repository and commit identity. It does not claim that the work was originally executed in MATHSOLVE. Each manifest records migration debt requiring future theorem-spine, route-selection, failure-accounting, and target-development work to occur here.

## Recursive manifest contract

`schemas/campaign_manifest.schema.json` requires:

- Programme parent repository, issue, and commit;
- at least one exact MATHFORGE input;
- MATHSOLVE provider issue and commit;
- recursively nested Work Packages;
- source repository and commit for each Work Package;
- digest-bearing artifact references;
- claim and proof-obligation ledgers;
- failed-route and resource ledgers for computational campaign types;
- MATHCERT handoff state;
- promotion blockers;
- disposal and reopening conditions.

The pair `(repository, commit_sha, path)` identifies the artifact location. `git_blob_sha1` or `sha256` is preferred for individual immutable files. `git_commit_sha1` is admitted for an inherited bundle and must equal the declared commit.

## Promotion discipline

The validator fails closed when:

- an active campaign is absent;
- campaign or Work Package IDs collide;
- native work points outside MATHSOLVE;
- retrospective work erases its historical source repository;
- commit and digest identities drift;
- a computational package lacks failed-route or resource ledgers;
- promotion is marked eligible while blockers remain;
- promotion is marked eligible without a ready MATHCERT handoff packet.

A manifest can be valid while its mathematical promotion remains blocked. Structural registration does not promote a claim.

## Generalized CI

`ci/validate_solve.py` no longer relies on a Union-Closed-only fallback. `contracts/programme_reference_registry.json` supplies deterministic references for every registered campaign and may be enriched by a sibling MATH-PROGRAMME knowledge-graph checkout.

`ci/validate_campaign_manifests.py` and its adversarial tests cover the recursive provider layer. The main Solve workflow runs both legacy claim-ledger validation and the new campaign-manifest gate.

## MATHCERT handoff

`schemas/mathcert_handoff.schema.json` and `templates/mathcert_handoff.json` require:

- exact target claims and support types;
- source commit;
- claim and proof-obligation artifact identities;
- checker target and inputs;
- explicit acceptance and rejection conditions;
- handoff status;
- reopening conditions.

MATHSOLVE prepares the packet. MATHCERT owns the certification result.

## Claim boundary

This governance work does not certify any mathematical result. All eight campaign manifests remain `promotion.eligible: false` for their stated mathematical blockers. The Odd-zeta manifest remains blocked at source intake.

## Next obligation

After this branch is reviewed:

1. pin each manifest by exact Git blob identity in MATH-PROGRAMME MP-MS-WP00;
2. migrate the next active stage of BSD, PNP, RH, YM, and OZ into native MATHSOLVE Work Packages;
3. replace commit-bundle identities with file-level SHA-256 or Git blob identities where practical;
4. emit claim-specific MATHCERT packets as claims become handoff-ready;
5. project the resulting lineage into AETHER only after GitHub-first conformance is stable.
