# MS-GOV-REV00 — Post-merge Council review of MS-GOV-WP00

## Review status

`CORRECTIVE_REVIEW_VALIDATED`

Reviewed object: merged `grandchallenge/MATHSOLVE#71` at merge commit `ec7c60bfa51850d7fb11bd5a3a24ca834352366e`.

Corrective head: `5b84627b31df04a9177c12bfb988e3bf6213ddcf`.

Validation: Solve checks run `30406924372` completed successfully.

## Council review

**Status:** reviewed with required corrections applied and validated.

The recursive manifest is the correct governing abstraction. Native and retrospective coverage remain distinct. The original implementation was not yet sufficient because it permitted repository commits to stand in for artifact hashes and did not distinguish a complete Cert disposition from positive certification.

The reviewed contract now:

- derives campaign coverage from the checked-in Programme reference registry;
- accepts file or tree content identities, never a repository commit as the artifact digest;
- requires distinct ledger artifacts for distinct roles;
- validates local MATHSOLVE Git blob and SHA-256 identities against repository bytes;
- requires failed-route and resource ledgers for computational campaigns;
- validates the standard MATHCERT packet against its schema;
- separates Judgment, Integration, and Claim Promotion gates.

## Adversary review

**Status:** reviewed; blocking mutations added and green.

The review rejects:

1. an active campaign omitted from the manifest set;
2. a retrospective route with no migration debt;
3. file-content drift behind a stable path;
4. reuse of a repository commit as an artifact digest;
5. one path presented simultaneously as several independent ledgers;
6. a computational package without resource or failed-route ledgers;
7. a partial handoff presented as Judgment-ready;
8. a rejected disposition presented as positive promotion support.

## Formalist review

**Status:** reviewed.

The following identities are separate:

- repository snapshot: `commit_sha`;
- artifact content: `git_blob_sha1`, `git_tree_sha1`, or `sha256`;
- artifact role: claim ledger, proof-obligation DAG, failed-route ledger, resource ledger, or certificate packet.

The handoff-state lattice is:

- incomplete: `pending`, `partial`, `not_applicable`;
- complete but not necessarily positive: `ready`, `submitted`, `rejected`, `proof_debt`;
- positive certification: `certified`, `qualified`.

A claim-promotion gate accepts only the positive states, and every packet in an eligible campaign must itself be certified or qualified.

## Amanuensis review

**Status:** reviewed.

Continuity actions:

- native UC, NS-CI, and HC records now point to actual files rather than repository roots or directories;
- missing native claim, proof-obligation, failed-route, and resource ledgers were created where applicable;
- retrospective BSD, PNP, RH, YM, and OZ records now preserve exact Programme file and Git blob identities;
- the MATHCERT template is a schema-valid, content-addressed example;
- no historical Programme artifact was copied into competing authority;
- migration debt and reopening conditions remain explicit.

## Referee review

**Status:** technically approved; Programme promotion remains conditional.

The exact corrective head passed repository checks, including schema, manifest, template, identity, and adversarial validation. Final cross-repository promotion still requires:

1. MATH-PROGRAMME PR `#119` to pin this exact provider head and the eight reviewed manifest blob identities;
2. Programme waiver and claim-promotion semantics to pass the complete policy workflow;
3. INTELLECT PR `#5` to remain concordant on positive Cert promotion.

## Claim boundary

This review governs campaign lineage and certification routing. It certifies no mathematical theorem and does not upgrade any campaign's mathematical status.
