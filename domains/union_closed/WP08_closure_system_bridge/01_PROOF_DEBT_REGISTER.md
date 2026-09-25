# WP08 Proof Debt Register

Date: 2026-09-25

| Debt ID | Obligation | Status | Evidence / next gate |
|---|---|---|---|
| WP08-D001 | Decide whether arbitrary finite union-closed families admit exact D003-complement representation. | Closed negative | `p04_no_universal_exact_functionalPreorder_representation`; explicit three-point obstruction. |
| WP08-D002 | Extend the Frankl-facing result from functional preorders to arbitrary finite partial orders. | Closed locally | `posetIdealFamily_exists_rare` and `posetIdeal_complement_frankl`; maximal-element erasure injection. |
| WP08-D003 | Express arbitrary finite closure systems by closure operators / implication bases and isolate the first non-poset obstruction. | Closed locally | Canonical closure operator and finite implication basis are checked; single binary implication `{a,b}->c` is a closure system not representable by unary implications; D002 erasure fails at the forced conclusion; bounded example still satisfies the rare-element/complement endgame. |
| WP08-D004 | Build an incidence-preserving interface to the WP05 minimum-counterexample lattice spine. | Open / next | Must retain abstract closure/lattice order and concrete ground-element incidence simultaneously. |

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
