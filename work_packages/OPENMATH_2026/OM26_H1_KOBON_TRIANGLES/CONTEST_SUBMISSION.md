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
