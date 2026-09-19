# Claim ledger

No entry in this ledger is a MATHCERT certification.

| Claim ID | Statement | Current status | Required evidence |
| --- | --- | --- | --- |
| `RSI-CCC-C001` | The direct stage-indexed model realizes the Cartesian-closed surface required by M1. | `OPEN` | Lean definitions and checked product/exponential/evaluation/currying laws. |
| `RSI-CCC-C002` | The model realizes the declared `Later`, `next`, and guarded fixed-point laws. | `PARTIAL` | Checked `Later`/`next` plus guarded fixed-point section and unfold/coherence theorems. |
| `RSI-CCC-C003` | The admitted intrinsically typed object language satisfies quotation/interpreter adequacy. | `OPEN` | Checked syntax, interpretation, and `run (quote t) = next ([[t]])`. |
| `RSI-CCC-C004` | The external admitted-program/morphism refinement relation is a preorder and satisfies the scoped compatibility laws used by M1. | `OPEN` | Checked reflexivity/transitivity and scoped composition/currying/evaluation compatibility; relation domain must include the objects used by C005. |
| `RSI-CCC-C005` | Under explicit fixed-kernel hypotheses, one accepted guarded self-replacement step preserves the declared invariant. | `OPEN` | Checked one-step admission theorem with checker soundness, certificate validity, evaluation-context integrity, and resource assumptions explicit. |
| `RSI-CCC-C006` | Repeated guarded application of the proved step yields the intended productive trace. | `BLOCKED_BY_C005` | Guarded trace construction after C005 closes. |

## Promotion rule

A status may advance from `OPEN` or `PARTIAL` only after the exact Lean artifact has been checked in CI and bound into the campaign evidence. `COMPLETE_IN_SOLVE` still means “constructed and mechanically checked in MATHSOLVE,” not “certified.”
