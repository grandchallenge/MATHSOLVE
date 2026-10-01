# OPENMATH-2026 CEX job board

This page is a human projection of the protected machine registry.

## Current seven-hill independent-agent lifecycle

| Assignment | Hill | State | Dispatch | Agent | Return issue |
|---|---|---|---|---|---|
| `OM26-H1-H1-12` | `OM26-H1` | `ACCEPTED` | `OM26-H1-H1-12-IA-001` | `INDEPENDENT-AGENT-001` | #498 |
| `OM26-H1-WP01` | `OM26-H1` | `ACCEPTED` | `OM26-H1-WP01-IA-001` | `INDEPENDENT-AGENT-101` | #553 |
| `OM26-H1-WP02` | `OM26-H1` | `LEASED_NOT_LAUNCHED` | `OM26-H1-WP02-IA-001` | `INDEPENDENT-AGENT-102` | #563 |
| `OM26-H2-WP01` | `OM26-H2` | `ACCEPTED` | `OM26-H2-WP01-IA-001` | `INDEPENDENT-AGENT-002` | #505 |
| `OM26-H2-WP02` | `OM26-H2` | `ACCEPTED` | `OM26-H2-WP02-IA-001` | `INDEPENDENT-AGENT-008` | #526 |
| `OM26-H2-WP03` | `OM26-H2` | `ACCEPTED` | `OM26-H2-WP03-IA-001` | `INDEPENDENT-AGENT-009` | #537 |
| `OM26-H2-WP04` | `OM26-H2` | `LEASED_NOT_LAUNCHED` | `OM26-H2-WP04-IA-001` | `INDEPENDENT-AGENT-204` | #561 |
| `OM26-H3-WP01` | `OM26-H3` | `ACCEPTED` | `OM26-H3-WP01-IA-001` | `INDEPENDENT-AGENT-003` | #506 |
| `OM26-H3-WP02` | `OM26-H3` | `ACCEPTED` | `OM26-H3-WP02-IA-001` | `INDEPENDENT-AGENT-302` | #545 |
| `OM26-H3-WP03` | `OM26-H3` | `LEASED_NOT_LAUNCHED` | `OM26-H3-WP03-IA-001` | `INDEPENDENT-AGENT-303` | #562 |
| `OM26-H4-WP01` | `OM26-H4` | `ACCEPTED` | `OM26-H4-WP01-IA-001` | `INDEPENDENT-AGENT-004` | #507 |
| `OM26-H4-WP02` | `OM26-H4` | `LEASED_NOT_LAUNCHED` | `OM26-H4-WP02-IA-001` | `INDEPENDENT-AGENT-402` | #559 |
| `OM26-H5-WP01` | `OM26-H5` | `ACCEPTED` | `OM26-H5-WP01-IA-001` | `INDEPENDENT-AGENT-005` | #508 |
| `OM26-H5-WP02` | `OM26-H5` | `LEASED_NOT_LAUNCHED` | `OM26-H5-WP02-IA-001` | `INDEPENDENT-AGENT-502` | #560 |
| `OM26-H6-WP01` | `OM26-H6` | `ACCEPTED` | `OM26-H6-WP01-IA-001` | `INDEPENDENT-AGENT-006` | #509 |
| `OM26-H6-WP02` | `OM26-H6` | `ACCEPTED` | `OM26-H6-WP02-IA-001` | `INDEPENDENT-AGENT-602` | #548 |
| `OM26-H6-WP03` | `OM26-H6` | `LEASED_NOT_LAUNCHED` | `OM26-H6-WP03-IA-001` | `INDEPENDENT-AGENT-603` | #556 |
| `OM26-H7-WP01` | `OM26-H7` | `ACCEPTED` | `OM26-H7-WP01-IA-001` | `INDEPENDENT-AGENT-007` | #510 |
| `OM26-H7-WP02` | `OM26-H7` | `ACCEPTED` | `OM26-H7-WP02-IA-001` | `INDEPENDENT-AGENT-702` | #551 |
| `OM26-H7-WP03` | `OM26-H7` | `LEASED_NOT_LAUNCHED` | `OM26-H7-WP03-IA-001` | `INDEPENDENT-AGENT-703` | #557 |

The lifecycle is `READY -> LAUNCHED -> RETURNED -> CAPTURED -> REPLAYED -> ADJUDICATED -> ADVANCED`. Intake alone creates no mathematical claim effect.

## Current task links

- H1: https://github.com/grandchallenge/MATHSOLVE/blob/804ef99fdb7f4708540b334e740364acef1dc5ed/handoffs/OPENMATH-2026/launch/OM26-H1-WP02.md
- H2: https://github.com/grandchallenge/MATHSOLVE/blob/11859afbf40e6774748f352732e39301ec4e0f27/handoffs/OPENMATH-2026/launch/OM26-H2-WP04.md
- H3: https://github.com/grandchallenge/MATHSOLVE/blob/d8d80928fa9f8ad004347da5ba3cc7af60d237cc/handoffs/OPENMATH-2026/launch/OM26-H3-WP03.md
- H4: https://github.com/grandchallenge/MATHSOLVE/blob/46f5a0821442a62684779bf9b3ede5a96cfa633a/handoffs/OPENMATH-2026/launch/OM26-H4-WP02.md
- H5: https://github.com/grandchallenge/MATHSOLVE/blob/040e41741f734eaacc2f01df983b200fad243a43/handoffs/OPENMATH-2026/launch/OM26-H5-WP02.md
- H6: https://github.com/grandchallenge/MATHSOLVE/blob/9e1fa1503985e4babfb8a521797b459b6d2c0537/handoffs/OPENMATH-2026/launch/OM26-H6-WP03.md
- H7: https://github.com/grandchallenge/MATHSOLVE/blob/cde5860a23c7cde9b830e16995f5757e65613166/handoffs/OPENMATH-2026/launch/OM26-H7-WP03.md

## Launcher contract

Canonical mode is `LINK_IN_RELAY_OUT`. Voluntary participants use a registered immutable task URL. GCL may optionally launch its own workers. The worker returns one complete `GCL-RETURN-RELAY/1` payload. Authenticated GCL infrastructure owns durable GitHub intake.

## Claim boundary

Automatic fallback adjudication may preserve evidence and advance a replay-closure successor without promoting the predecessor mathematics. MATHCERT certification and competition submission remain separate authorities.
