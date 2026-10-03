# WP08 Proof Debt Register

Date: 2026-09-25

| Debt ID | Obligation | Status | Evidence / next gate |
|---|---|---|---|
| WP08-D001 | Decide whether arbitrary finite union-closed families admit exact D003-complement representation. | Closed negative | `p04_no_universal_exact_functionalPreorder_representation`; explicit three-point obstruction. |
| WP08-D002 | Extend the Frankl-facing result from functional preorders to arbitrary finite partial orders. | Closed locally | `posetIdealFamily_exists_rare` and `posetIdeal_complement_frankl`; maximal-element erasure injection. |
| WP08-D003 | Express arbitrary finite closure systems by closure operators / implication bases and isolate the first non-poset obstruction. | Closed locally | Canonical closure operator and finite implication basis are checked; single binary implication `{a,b}->c` is a closure system not representable by unary implications; D002 erasure fails at the forced conclusion; bounded example still satisfies the rare-element/complement endgame. |
| WP08-D004 | Build an incidence-preserving interface to the WP05 minimum-counterexample lattice spine. | Active synthesis, unadjudicated | All four blind returns and the adversarial return are durably protected. Blind cohort `UC-WP08-D004-BLIND-COHORT-001` is closed on evidence completeness; synthesis is allowed, but no contributor claim is yet admitted. |

## D003 movement

Every finite closure system on an explicit carrier now has an exact finite
implication normal form.

```text
finite closure system
  -> canonical closure operator
  -> fixed points = closed members
  -> all valid finite implications P -> q
  -> exact model-family recovery.
```

Unary implications are insufficient for arbitrary closure systems because their
model families are union-closed. The minimal checked non-unary example is the
single binary implication

```text
{a,b} -> c.
```

Its closed-set family is not union-closed and therefore cannot arise from a
finite unary basis.

The D002 erasure map fails exactly where expected:

```text
{a,b,c} \ {c} = {a,b},
```

and `{a,b}` violates the binary implication. Thus maximal-element erasure is
not a universal closure-system proof mechanism.

The same example nevertheless has a rare element. D003 therefore separates:

```text
failure of the D002 mechanism
  !=
failure of the Frankl-facing conclusion.
```

## Current frontier

D004 must connect the exact closure/implication representation to WP05 without
discarding the element-set incidence matrix that defines frequencies.

The required object is not merely an abstract finite lattice. It is a finite
closure/lattice object equipped with an explicit incidence map and exact
frequency transport.

```text
UC-P04 = OPEN
UC-FRANKL = OPEN_PROBLEM
```

## D004 governed fan-out

The D004 plan is now decomposed into five independent evidence lanes under the
Controlled Epistemic Interface.

```text
WP01 principal incidence              blind
WP02 join-irreducible incidence       blind
WP03 implication semantics            blind
WP04 WP05 frequency translation       blind
WP05 adversarial representation audit adversarial
```

WP01-WP04 are cohort `UC-WP08-D004-BLIND-COHORT-001`. Synthesis is prohibited
before cohort closure. WP05 may not consume blind returns before integration.

The dispatch registry is under
`contributions/UC-001/WP08_D004_INCIDENCE_INTERFACE/`. The immutable task
content is bound to commit `283a82b53c36c999805805df94fde24e0af578ee`.

The activation sequence completed fail-closed. The CEI UC intake profile is
protected at Programme commit `c70bf336ec598bb8654cc465306c6cf3a871341e`;
the task packet is protected at Solve commit
`7ce9e3b93c92510d574dd6ff9d31d6716915f8fc`; issues #721-#725 were verified
byte-for-byte against their protected bootstraps; and the activation receipt
records those identities before the dispatches were moved to
`READY_FOR_GITHUB_COMMENT`.


## D004 evidence-complete transition

All five external returns are protected on exact evidence checkpoint
`4504220dbb33e01038854ceb7fdd869eecf7e4cd`. The four-member blind cohort is closed with no missing-return
exception, and WP05's adversarial replay is also protected.

The closure receipt is:

`contributions/UC-001/WP08_D004_INCIDENCE_INTERFACE/COHORT_CLOSURE_RECEIPT.json`

This opens internal synthesis only. Every contributor disposition remains
`received_unadjudicated`; no certification or universal Frankl/UC-P04 claim
follows from cohort closure.
