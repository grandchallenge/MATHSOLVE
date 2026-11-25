# PNP-ABOVE WP17 — unconditional source-native diagonal-game no-advantage replay

**Claim level:** general theorem in the original source-native MIPRE synchronous/tensor-product/commuting model. This is **negative necessary-condition research evidence**, not an executable hard-game construction, quantum compression, P-versus-NP proof or independent public mathematical certification.

## Exact locked source identity

- Original upstream: `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970`, original Lean 4.35.0-rc3 and pinned mathlib/MIPStarRE.
- Protected MATHSOLVE parent: WP16 source merge `f25d8da67c48d88c2729c5fd454386667999253b`.
- First proof-bearing exact WP17 candidate `c825e6837d63f6be26e78253cb000b24ad090ee8`. The [Lean proof](WP17_UnconditionalDiagonalNoGap.lean) is Git blob `86ece0db534e18327ad380a542e7636bc0d746fa`, SHA-256 `218d9252d9490fcfd3e2a2aaad185b4d7ae8d86f281ccd88b9a2416cb2b5eed5`.
- Imported protected original source Git blobs: WP08 `45b9fa687fad92bf1b1d4be2809473e0c4f9957d`, WP09 `3b64353814fd70a77810e51f2d04cbcfb4271def`, WP10 `860ad60fca4e99fcd836eec748fa419efd0701b2`, WP11 `088a731db4a7a1a21097a593958706df6b8a488b`, WP12 `c509e7e96383c7cb8199d7a9095b915a6d4db759`, WP13 `711e3e7938ea8c6682778252062adfc920ff4dbd`, WP14 `939f801c874e1e9acc6223a24eb055888466d51b`, WP15 `3e7d4905f6483acbbbafd173c735da17671dcc67`, WP16 `c576f71397ce86013e07fad08e480bcff294ef3e`.
- Fail-closed reproducer: [WP17_REPLAY.sh](WP17_REPLAY.sh); [axiom auditor](WP17_AXIOM_AUDIT.py); [scope and theorem gate](WP17_UNCONDITIONAL_DIAGONAL_VALUE_THEOREM.md).

## Exact original-source Lean replay

Proof-bearing candidate source-native replay from GCL CONTROL CHAD-local capture `f0e369bebc384cb6af6449e1635ca3f7` at `/tmp/gcl-pnp-wp17-source-c825e68`, exit 0:

```text
CHECKING_SOURCE_NATIVE_WP08
CHECKING_SOURCE_NATIVE_WP09
CHECKING_SOURCE_NATIVE_WP10
CHECKING_SOURCE_NATIVE_WP11
CHECKING_SOURCE_NATIVE_WP12
CHECKING_SOURCE_NATIVE_WP13
CHECKING_SOURCE_NATIVE_WP14
CHECKING_SOURCE_NATIVE_WP15
CHECKING_SOURCE_NATIVE_WP16
CHECKING_SOURCE_NATIVE_WP17
WP17_STANDARD_AXIOMS_ONLY_PASS count=17
WP17_SOURCE_NATIVE_UNCONDITIONAL_DIAGONAL_NO_GAP_PASS
exit 0
```

The axiom auditor examines **17 distinct** `PNPAbove.WP17` theorem declarations via original Lean `#print axioms`, allowing only the standard `propext`, `Classical.choice` and `Quot.sound`. No `sorryAx`, custom MIPRE axiom or generated `native_decide` axiom appears. All ten modules compile against original upstream MIPRE and original native `MIPRE.SynchronousGame`, `MIPRE.TensorProductStrategy`, `MIPRE.CommutingStrategy` and their original Born/tracial value definitions; no substitute game model is introduced.

## Exact mathematical disposition and strict boundaries

For *any original finite synchronous game with a nonempty answer alphabet* whose law has **zero probability on unequal question pairs** (not assuming all diagonal questions are reachable or winnable), the WP17 theorem computes

```text
feasibleMass G = sum_x μ(x,x) · indicator[there exists an answer a accepted on (x,x)]
syncValue G = feasibleMass G
quantumValue G.toGame = feasibleMass G
commValue G = feasibleMass G
```

The optimal native value may be **strictly below 1** for games with unsatisfiable sampled diagonal questions. A one-dimensional, question-dependent **deterministic classical** strategy attains this exact optimum, selecting accepted equal answers where they exist. Independent original-source Born-rule and commuting-trace upper bounds show no quantum or commuting strategy can exceed the optimum, even on unwinnable questions. This completely **removes WP16's feasibility hypothesis for the value-comparison conclusion**.

For **every original WP14 source sampler parameter and every answer budget**, the identical-player CL law proved in protected WP16 is diagonal. WP17 therefore proves that **any mathematical replacement synchronous decision predicate**, whether diagonally feasible or not, leaves the native synchronous, tensor-product quantum and commuting values all **equal**. In particular, the fixed WP14 question distribution **cannot support a quantum-vs-classical gap, no matter how the synchronous decision predicate is changed**.

This is confined to **diagonal-supported original synchronous games with nonempty answer alphabets**. WP17 does not construct an executable `Cost.Prog` for the arbitrary predicate, assert all conditional CL samplers are diagonal, prove a general theorem for other nonlocal game models, or resolve any compression/transfer/SAT complexity problem. It supplies a **necessary sampler change**: non-diagonal Alice/Bob question support is required in the target setting; additional source-native discrimination and genuine soundness/value-gap proof are still indispensable. Parent PNP #1136 and programme PNP-001 remain open; no independent mathematical certification or P-versus-NP claim.

**Admission status:** source-proof replay above is not the final receipt-bearing exact-head replay, mandatory protected checks, source readback or protected public evidence projection. Those remain separately required and will be recorded after successful admission.
