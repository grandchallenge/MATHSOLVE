# Resource and failed-route ledger

## Fixed environment

- Lean toolchain: `leanprover/lean4:v4.29.1`
- mathlib commit: `5e932f97dd25535344f80f9dd8da3aab83df0fe6`
- MATHSOLVE route-open base: `b0854bb7770296b610b655753bc62b27365b27bb`
- upstream formal-object SHA-256: `1fca7a5e5bba2f4b59ccf9288a6a01129652091f86071c7be70022ea076d0edc`

## Resource discipline

M1 prioritizes a small directly inspectable model. Do not import a large abstract guarded-topos development merely to shorten local definitions unless the direct route is shown to be materially blocked.

The first implementation tranche is limited to the stage substrate, products, `Later`, `next`, and guarded fixed-point section. Exponentials, typed interpretation, refinement, and admission are added only in proof-order sequence.

## Failed-route ledger

### FR-001 — ambient order enrichment inferred from executable refinement

**Disposition:** terminated at M0 review.

The original M0 wording allowed the external parity refinement relation to be read as evidence for ambient order enrichment of `Set^(omega^op)`. This route was rejected. M1 uses an external certified preorder on an explicit represented relation domain.

### FR-002 — stronger `Pos`/CPO` presheaf model by default

**Disposition:** deferred, not failed.

A genuinely ordered presheaf model may be investigated only if the smaller M0 model fails a required theorem obligation. Switching to it would change the exact formal object and requires upstream re-review.

## Stop conditions

Record a new failed-route entry and stop before changing the frozen target if:

- Kripke exponential construction cannot be made to satisfy the required laws in the chosen direct representation;
- guarded fixed-point construction requires an unstated classical or semantic oracle outside the declared model;
- reflection adequacy forces semantic reification;
- the external refinement domain becomes vacuous or does not contain the represented programs/morphisms used by the admission theorem;
- checker soundness cannot remain an explicit assumption at the one-step boundary.
