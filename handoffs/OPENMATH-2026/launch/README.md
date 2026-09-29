# OPENMATH-2026 current zero-context agent scripts

These are the current launcher-facing scripts for the seven peer hill lanes.

| Hill | Current script | Executable now |
|---|---|---|
| H1 | `OM26-H1.md` | No — previous contribution accepted; no successor lease |
| H2 | `OM26-H2.md` | Yes — WP02 / Agent 008 / issue #526 |
| H3 | `OM26-H3.md` | Yes — WP01 / Agent 003 / issue #506 |
| H4 | `OM26-H4.md` | Yes — WP01 / Agent 004 / issue #507 |
| H5 | `OM26-H5.md` | Yes — WP01 / Agent 005 / issue #508 |
| H6 | `OM26-H6.md` | Yes — WP01 / Agent 006 / issue #509 |
| H7 | `OM26-H7.md` | Yes — WP01 / Agent 007 / issue #510 |

Rules:

1. Every hill is a first-class current lane.
2. Historical dispatch/bootstrap files under `handoffs/OPENMATH-2026/jobs/` remain frozen provenance and are not current launcher scripts.
3. Every executable script is self-contained and does not require agent GitHub access.
4. Default agent return is `GCL-RETURN-RELAY/1` to the launcher.
5. Authenticated GCL infrastructure owns durable intake to the exact protected return issue.
6. H1 must not be relaunched until a new protected successor lease exists.
