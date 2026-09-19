# PNP-BRIDGE-001 — staged proof-bearing bridge suite

This package advances the exact bridge suite required by MATHSOLVE issue #148. It closes the carrier and polynomial-bound obligations and records why the remaining obligations are not yet theorem-backed.

## Proved carrier result

`MathSolve/PNP/CarrierBridge.lean` kernel-checks the true-preimage map from total Boolean decision functions on finite bit strings to binary languages. It proves that the map is injective and that transporting sets of decision problems through it preserves and reflects class equality and inequality.

This discharges `PNP-BRIDGE-CARRIER-001` at the carrier level. It does not identify either imported `P` or imported `NP` with the Programme classes.

## Proved polynomial-bound result

`MathSolve/PNP/PolyBoundBridge.lean` formalizes the Programme bound presentation on the exact finite-binary carrier and `List Bool.length` size measure. A witness consists of fixed natural `constant`, `exponent`, `threshold`, and `lowCap` values. The low-length clause explicitly bounds every input below the threshold; the eventual clause is exactly `cost input <= constant * input.length ^ exponent`.

The file proves:

- every pinned imported `Polynomial Nat` evaluation bound gives a Programme witness, choosing threshold `1`, low cap `p.eval 0`, coefficient-sum constant `p.eval 1`, and exponent `p.natDegree`;
- every Programme witness gives one `Polynomial Nat`, `C lowCap + C constant * X^exponent`, which bounds every input length;
- therefore the two bound presentations are equivalent.

The natural-polynomial direction handles arbitrary natural coefficients, not only monomials. The finite exceptional prefix is not discarded. The file includes explicit `#print axioms` reports for the domination lemma and both conversion directions.

This discharges `PNP-BRIDGE-POLYBOUND-001` only. It does not change the machine model, prove a TM2/multitape simulation, or identify either imported class with a Programme class.

## Remaining boundary

`PNP-BRIDGE-MODEL-001` still requires a pinned Programme-side Lean definition of the locked deterministic multitape machine, its exact step cost, total-decider semantics, and a polynomial-overhead simulation interface against the imported finite TM2 model.

`PNP-BRIDGE-NP-001` remains blocked by that machine bridge. Its later proof must additionally transport the deterministic verifier, self-delimiting input/witness pairing, witness-length bound, malformed-pair behavior, totality, and class carrier.

Concrete endpoint parser, malformed-input, size, correctness, and reduction obligations remain endpoint-specific under `PNP-BRIDGE-ENDPOINT-001`.

## Verification

```text
lake env lean MathSolve/PNP/CarrierBridge.lean
lake env lean MathSolve/PNP/PolyBoundBridge.lean
python ci/validate_pnp_bridge_001.py
python -m unittest ci/test_pnp_bridge_001.py -v
```

Passing these checks proves only the carrier bridge and the two-way polynomial-bound presentation bridge. It does not prove `P = NP`, `P != NP`, either imported-to-Programme class correspondence, a machine simulation, an NP-verifier equivalence, an endpoint result, or any MATHCERT or promotion disposition.
