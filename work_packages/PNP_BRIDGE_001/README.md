# PNP-BRIDGE-001 — staged proof-bearing bridge suite

This package begins the exact bridge suite required by MATHSOLVE issue #148. It closes the carrier-only obligation and records why the remaining obligations are not yet theorem-backed.

## Proved result

`MathSolve/PNP/CarrierBridge.lean` kernel-checks the true-preimage map from total Boolean decision functions on finite bit strings to binary languages. It proves that the map is injective and that transporting sets of decision problems through it preserves and reflects class equality and inequality.

This discharges `PNP-BRIDGE-CARRIER-001` at the carrier level. It does not identify either imported `P` or imported `NP` with the Programme classes.

## Remaining boundary

The Programme lock is currently documentary: it does not expose a Lean definition of its deterministic multitape machine or its asymptotic runtime predicate. Therefore no kernel-checked theorem in this repository can yet state, much less prove, the required TM2 simulation or the full class equivalences.

The machine-model bridge must precede the class-extensional NP bridge. The polynomial-bound bridge also needs a formal Programme-side predicate before its two conversions can be given the exact target type required by the lock. Concrete endpoint parser, malformed-input, size, correctness, and reduction obligations remain endpoint-specific.

## Verification

```text
lake env lean MathSolve/PNP/CarrierBridge.lean
python ci/validate_pnp_bridge_001.py
python -m unittest ci/test_pnp_bridge_001.py -v
```

Passing these checks proves only the carrier bridge and the integrity of the remaining-obligation record. It does not prove `P = NP`, `P != NP`, either class correspondence, a simulation theorem, or any endpoint result, and it has no MATHCERT or promotion effect.
