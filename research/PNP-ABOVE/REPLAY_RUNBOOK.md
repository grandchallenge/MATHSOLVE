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

## Managed CHAD route (WP47 onward)

The 2026-11-28 storage expansion provides adequate staging space. The
4.35.0-rc3 toolchain is installed under the dedicated SSD toolchain directory
and registered through the managed launcher. The pinned MIPRE archive is
staged at `/mnt/gcl-lean-work/workspaces/pnp-mipre-5926bdff-wp47`.
Do not infer cache readiness merely from the presence of that directory.
Use the managed adapter's preflight and the actual replay receipt.

`PNP_REPLAY_MANAGED.py` verifies every tracked upstream blob against the
exact staged Git tree, verifies the staged manifest and package revisions,
checks for modified tracked package sources, validates resolved Lean search
paths on the dedicated SSD volumes, and checks the available reserve. It
runs Lean exclusively using `gcl-lean-work run WORKSPACE lake env lean`.
It installs a temporary SSD-local import namespace for each fresh replay,
then removes that link on normal exit. It refuses an existing namespace or
output path rather than overwriting retained evidence. Use only one active
replay per staged workspace. Existing import caches are retained trusted
build inputs; this adapter does not independently rebuild every upstream
library or authenticate every cached binary. The new protected predecessor
and candidate modules are freshly checked from exact source.

Example, from a locked GCL checkout, with a new output directory:

```
W=/mnt/gcl-lean-work/workspaces/pnp-mipre-5926bdff-wp47
python3 research/PNP-ABOVE/WP47_REPLAY.py --managed-ssd "$W" "$PWD" "$W/replay-wp47-fresh"
```

Run `python3 -m unittest test_pnp_replay_managed.py test_pnp_replay_preflight.py`
from `research/PNP-ABOVE` for the placement regression controls. Later native
tranches should reuse this adapter and source-matched SSD cache, retaining
their own exact predecessor/source locks. Do not reallocate Colab for a
ready local cache; when preflight refuses, classify the actual condition and
use the approved alternate only if necessary. Never run HDD Lean directly.
