# OPENMATH successor return-transport incident — 2026-10-02

## Scope

Affected automatically generated replay-closure successor packets:

- OM26-H1-WP31 / issue #608
- OM26-H3-WP05 / issue #613
- OM26-H5-WP04 / issue #616

A contemporaneous control packet, OM26-H6-WP05 / issue #618, completed durable return successfully.

## Observed failure

The three affected agent sessions completed visibly to the Human Steward, but no durable GitHub return comment was created on the exact INTENDED_RETURN issue. No controller intake branch was created because the GitHub evidence substrate never received a return.

The completed H1-WP31, H3-WP05, and H5-WP04 result bodies are not recoverable from protected repository state or durable account context. Their mathematical claims therefore remain unadjudicated and must not be reconstructed or promoted.

## Root cause

`ci/openmath_lifecycle_candidate.py` generated replay-closure successor launch packets with:

`GITHUB_ACCESS_REQUIRED: NO`

while the same packet later required an authenticated GitHub issue comment or authorized authenticated relay before work. This contradicted the frozen `LINK_IN_RELAY_OUT` transport contract, which requires participant-environment authenticated comment capability before substantive work.

The H6-WP05 control succeeded because its worker nevertheless used the authenticated GitHub relay and produced issue comment #5951785225. That successful control isolates the defect upstream of GitHub intake/controller processing.

## Remediation

1. Generated successors now declare:
   - `GITHUB_ACCESS_REQUIRED: PARTICIPANT_ENVIRONMENT_AUTHENTICATED_COMMENT_CAPABILITY`
   - `RETURN_COMPLETION_RECEIPT_REQUIRED: GITHUB_ISSUE_COMMENT_URL`
2. Generated return instructions now state that an assignment is not complete until the durable comment URL is obtained and the posted comment is read back from INTENDED_RETURN.
3. A regression test asserts the generated successor transport header and rejects `GITHUB_ACCESS_REQUIRED: NO`.
4. Only genuinely unlaunched successor packets are re-pinned to corrected immutable artifacts. Already executed/lost-result assignments retain their original exact task identities.

## Governance boundary

This incident record does not reconstruct lost mathematical evidence, accept any missing result, or create claim effect. H1-WP31, H3-WP05, and H5-WP04 remain unresolved at the evidence boundary until fresh independently attributable evidence is produced under a valid transport contract.
