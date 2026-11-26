# Native PNP-ABOVE replay execution contract (WP40 onward)

**Do not compile against CHAD's HDD-backed custody worktrees or /tmp.** The
binding MATHSOLVE AGENTS.md SSD placement rule applies to all local Lean
invocations, including absolute compiler paths in historical scripts.

1. Before reserving expensive work, check managed SSD workspace placement,
   toolchain pin, dependency cache completeness and the 2 GiB free-space
   reserve. Do not delete another worker's workspace to make room.
2. For CHAD, use the approved managed `gcl-lean-work` launcher with all
   compilation inputs/outputs on the SSD. Historical raw direct-runner scripts
   are not a managed launcher. When SSD staging cannot fit, choose an authorized
   native Linux alternate (e.g. an existing Colab CPU session); never fall back
   to raw HDD Lean.
3. Every new direct Python replay must call `direct_runner_guard()` before
   source staging and `preflight()` before creating its output directory.
   `PNP_REPLAY_PREFLIGHT.py` refuses WSL, checks the pinned compiler and
   dependency revisions, checks required entry objects and reserve, and records
   placement. It does not certify every cached binary or test physical SSD
   hardware. Use `bounded_run` and record exit, elapsed time, major faults and
   filesystem reads. A timeout is a named infrastructure failure, not a failed
   theorem. Do not blindly rerun an unchanged failing route.
4. For historical whole-package replay, use its exact historical checkout.
   In particular, WP35's strict transition guard rejects later PNP-ABOVE
   additions. Use WP35 protected revision
   `29697b84bcf40d3e487c19aa1c779064560a0dd8` for a fresh WP35 replay, then
   WP38A, WP38B and WP40 at the appropriate descendant. Check the historical
   transition before spending compute.
5. If a completed WP34 checkpoint exists from a later exact checkout, do not
   edit its receipt or relax the historical transition guard.
   `WP40_RECOVER_WP35.py` provides a separate source-matched incremental
   route: compare every historical Lean source to that checkout, compare all
   94 retained source/object pairs to protected source, then freshly check
   WP35Dense with its original source guard and axiom audit. Retain both
   receipts and report the incremental scope, not a full historical replay.
6. Before admission, run the placement regression tests, exact new-source
   replay, standard-axiom audit, and existing protected checks. Retain the
   exact source, status, placement and execution receipts. No new broad
   campaign CI job is required.

Local storage observation, 2026-11-26: the PNP upstream package tree requires
6,510,226,129 bytes; the existing managed SSD workspace has about 5 GiB free
before reserve, and its separate 4.35.0-rc3 toolchain staging is incomplete.
The CHAD local full staging route is not ready. This is a capacity condition,
not permission to bypass placement. The existing Colab recovery route has
successfully replayed all WP40 declarations. This runbook and guard close
the direct WP40 replay bypass; they do not retrofit archived scripts or
guarantee availability of every runner.
