# OPENMATH-2026 CEX job board

This page is a human projection of the protected machine registry.

## Current seven-hill independent-agent lifecycle

| Assignment | Hill | State | Dispatch | Agent | Return issue |
|---|---|---|---|---|---|
| `OM26-H1-H1-12` | `OM26-H1` | `ACCEPTED` | `OM26-H1-H1-12-IA-001` | `INDEPENDENT-AGENT-001` | #498 |
| `OM26-H1-WP01` | `OM26-H1` | `LEASED_NOT_LAUNCHED` | `OM26-H1-WP01-IA-001` | `INDEPENDENT-AGENT-101` | #553 |
| `OM26-H2-WP01` | `OM26-H2` | `ACCEPTED` | `OM26-H2-WP01-IA-001` | `INDEPENDENT-AGENT-002` | #505 |
| `OM26-H2-WP02` | `OM26-H2` | `ACCEPTED` | `OM26-H2-WP02-IA-001` | `INDEPENDENT-AGENT-008` | #526 |
| `OM26-H2-WP03` | `OM26-H2` | `LEASED_NOT_LAUNCHED` | `OM26-H2-WP03-IA-001` | `INDEPENDENT-AGENT-009` | #537 |
| `OM26-H3-WP01` | `OM26-H3` | `ACCEPTED` | `OM26-H3-WP01-IA-001` | `INDEPENDENT-AGENT-003` | #506 |
| `OM26-H3-WP02` | `OM26-H3` | `LEASED_NOT_LAUNCHED` | `OM26-H3-WP02-IA-001` | `INDEPENDENT-AGENT-302` | #545 |
| `OM26-H4-WP01` | `OM26-H4` | `LEASED_NOT_LAUNCHED` | `OM26-H4-WP01-IA-001` | `INDEPENDENT-AGENT-004` | #507 |
| `OM26-H5-WP01` | `OM26-H5` | `LEASED_NOT_LAUNCHED` | `OM26-H5-WP01-IA-001` | `INDEPENDENT-AGENT-005` | #508 |
| `OM26-H6-WP01` | `OM26-H6` | `ACCEPTED` | `OM26-H6-WP01-IA-001` | `INDEPENDENT-AGENT-006` | #509 |
| `OM26-H6-WP02` | `OM26-H6` | `LEASED_NOT_LAUNCHED` | `OM26-H6-WP02-IA-001` | `INDEPENDENT-AGENT-602` | #548 |
| `OM26-H7-WP01` | `OM26-H7` | `ACCEPTED` | `OM26-H7-WP01-IA-001` | `INDEPENDENT-AGENT-007` | #510 |
| `OM26-H7-WP02` | `OM26-H7` | `ACCEPTED` | `OM26-H7-WP02-IA-001` | `INDEPENDENT-AGENT-702` | #551 |
| `OM26-H7-WP03` | `OM26-H7` | `LEASED_NOT_LAUNCHED` | `OM26-H7-WP03-IA-001` | `INDEPENDENT-AGENT-703` | #557 |

The lifecycle is `READY -> LAUNCHED -> RETURNED -> CAPTURED -> REPLAYED -> ADJUDICATED -> ADVANCED`. Intake alone creates no mathematical claim effect.

## Current launcher links

- H1: https://github.com/grandchallenge/MATHSOLVE/blob/fe2af74372e39dbde29cdd46b0b9c80e8af7ebe6/handoffs/OPENMATH-2026/launch/OM26-H1-WP01.md
- H2: https://github.com/grandchallenge/MATHSOLVE/blob/e64c93148ddecbc8e51352c24926898e42b8ea10/handoffs/OPENMATH-2026/launch/OM26-H2-WP03.md
- H3: https://github.com/grandchallenge/MATHSOLVE/blob/fcb5c5c013fadb94e24029e7638ff978945f8d05/handoffs/OPENMATH-2026/launch/OM26-H3-WP02.md
- H4: https://github.com/grandchallenge/MATHSOLVE/blob/f2c23b010687052ee442a2d7fc1991a2c4d2700b/handoffs/OPENMATH-2026/launch/OM26-H4.md
- H5: https://github.com/grandchallenge/MATHSOLVE/blob/f2c23b010687052ee442a2d7fc1991a2c4d2700b/handoffs/OPENMATH-2026/launch/OM26-H5.md
- H6: https://github.com/grandchallenge/MATHSOLVE/blob/aa6ed5e8ae980cf03efc506441376a754c552ba8/handoffs/OPENMATH-2026/launch/OM26-H6-WP02.md
- H7: https://github.com/grandchallenge/MATHSOLVE/blob/ec9b1ce1b24206840ab88d0e4094bb4571e9afa3/handoffs/OPENMATH-2026/launch/OM26-H7-WP03.md

## Launcher contract

Canonical mode is `LINK_IN_RELAY_OUT`. The launcher hands the worker one registered immutable task URL. The worker returns one complete `GCL-RETURN-RELAY/1` payload. Authenticated GCL infrastructure owns durable GitHub intake.

## Claim boundary

Automatic fallback adjudication may preserve evidence and advance a replay-closure successor without promoting the predecessor mathematics. MATHCERT certification and competition submission remain separate authorities.
