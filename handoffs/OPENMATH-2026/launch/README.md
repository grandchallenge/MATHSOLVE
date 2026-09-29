# OPENMATH-2026 current zero-context launch links

Canonical mode is `LINK_IN_RELAY_OUT`.

The launcher verifies the protected lease and hands the independent zero-context worker one immutable public task URL. The worker reads that document, executes the bounded task, and returns the required `GCL-RETURN-RELAY/1` payload. No human work-package copy/paste is part of the protocol.

| Hill | Current immutable task | Executable now |
|---|---|---|
| H1 | https://github.com/grandchallenge/MATHSOLVE/blob/f2c23b010687052ee442a2d7fc1991a2c4d2700b/handoffs/OPENMATH-2026/launch/OM26-H1.md | No — previous contribution accepted; no successor lease |
| H2 | https://github.com/grandchallenge/MATHSOLVE/blob/e64c93148ddecbc8e51352c24926898e42b8ea10/handoffs/OPENMATH-2026/launch/OM26-H2-WP03.md | Yes — WP03 / Agent 009 / issue #537 |
| H3 | https://github.com/grandchallenge/MATHSOLVE/blob/f2c23b010687052ee442a2d7fc1991a2c4d2700b/handoffs/OPENMATH-2026/launch/OM26-H3.md | Yes — WP01 / Agent 003 / issue #506 |
| H4 | https://github.com/grandchallenge/MATHSOLVE/blob/f2c23b010687052ee442a2d7fc1991a2c4d2700b/handoffs/OPENMATH-2026/launch/OM26-H4.md | Yes — WP01 / Agent 004 / issue #507 |
| H5 | https://github.com/grandchallenge/MATHSOLVE/blob/f2c23b010687052ee442a2d7fc1991a2c4d2700b/handoffs/OPENMATH-2026/launch/OM26-H5.md | Yes — WP01 / Agent 005 / issue #508 |
| H6 | https://github.com/grandchallenge/MATHSOLVE/blob/f2c23b010687052ee442a2d7fc1991a2c4d2700b/handoffs/OPENMATH-2026/launch/OM26-H6.md | Yes — WP01 / Agent 006 / issue #509 |
| H7 | https://github.com/grandchallenge/MATHSOLVE/blob/f2c23b010687052ee442a2d7fc1991a2c4d2700b/handoffs/OPENMATH-2026/launch/OM26-H7.md | Yes — WP01 / Agent 007 / issue #510 |

Rules:

1. Every hill is a first-class current lane.
2. Historical dispatch/bootstrap files under `handoffs/OPENMATH-2026/jobs/` remain frozen provenance.
3. Each executable linked task is self-contained.
4. The canonical agent-facing input is the immutable URL, not copied task text.
5. GitHub authentication is not required for public task read.
6. If the worker cannot read the task URL, launcher-side exact hydration is the fallback; the human operator does not shuttle task text.
7. Default result transport is `GCL-RETURN-RELAY/1`; authenticated GCL infrastructure owns durable intake.
8. H1 remains non-executable until a new protected successor lease exists.
