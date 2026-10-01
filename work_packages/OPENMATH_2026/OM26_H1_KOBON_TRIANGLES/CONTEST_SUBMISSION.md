# H1 contest submission transaction

User authorization: 2026-10-01, submit valid entries now; contest account **jimsteeg**.

First payload: `candidates/RH_BADER_RECONSTRUCTION_093/solution.json`.
SHA-256: `e606799ad6c1296deedb475440d1eecbe86daba8a3af625718f55726f93da4d5`.
Fresh exact oracle replay: 18 lines, 93 bounded triangular faces, PASS.
Attribution: reconstruction of published Bader order data, not a new discovery or optimality claim.

Execute the existing `OPENMATH Kobon Bader 93 reconstruction` workflow on
protected main with `submit_to_leaderboard=true`. Pull the live hill, repeat
source-order, direct-oracle and AutoLab concordance checks, require authenticated
nickname jimsteeg, then submit the generated report using the official CLI.
PR runs and default dispatches do not submit. The run retains the report and
server response. Record a submission only after the server accepts it and its
identifier/leaderboard entry is read back. Do not resubmit a successful transaction
because an unrelated check or documentation update failed.

An AutoLab leaderboard submission is distinct from organizer acceptance of a
formal competition result. The current official handbook supplies the organizer
review route, requiring exact artifacts, provenance and an immutable submission
record. The public event website presently does not link its competition-specific
workspace. Do not invent such a namespace or treat a paper proof as already
approved. The deadline is 2026-10-02 21:00 America/Vancouver.

The six other lanes require individual payload and live-evaluator readiness.
H2 has an accepted 89,911-step witness; H4 has a reduced 23-rule catalog;
H5 has exact rational witnesses; H6 has exact rank-23 certificates. H3's
published seed is prior work, with current algebraic corrections distinct from
an improved score. H7 has no compiled complete proof and must not be submitted
with proof holes. Continue preparing and evaluating these lanes after H1's
server result; preserve genuine blockers instead of counting prepared files as
submissions. Existing fan/prism research and GCL Cert review do not gate this
explicitly authorized leaderboard transaction.

First dispatch `36849889699` verified jimsteeg and score 93 but the server rejected the working-tree report: HTTP 400, no tree_hash. It created no accepted leaderboard entry. Submission now uses committed-version final evaluation and requires both tree_hash and official=true before sending. A stale H2 historical validator exposed by the routing change is repaired to recognize its already-admitted WP04 successor while retaining WP02 history and requiring accepted/closed WP03.

Second dispatch `36850436082` failed before submission: the public hill lacks private evaluator data and explicitly requires an AutoLab Climb for an official score. Both dispatches produced zero accepted leaderboard entries. The replacement dispatch registers fixed H1/H2/H4/H5/H6 code in native jimsteeg Climbs, disables generated ideas, caps new Climb cost at zero, and reads back each exact solution and job ID. This registers evaluation jobs; it does not count queued jobs as official scores or organizer acceptance. Activation/compute must follow as a distinct bounded transaction.
