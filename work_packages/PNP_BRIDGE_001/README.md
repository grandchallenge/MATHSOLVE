# PNP-BRIDGE-001 — staged proof-bearing bridge suite

This package advances the exact bridge suite required by MATHSOLVE issue #148. It closes the carrier, polynomial-bound, and deterministic machine-model obligations and records the remaining NP-verifier and endpoint boundaries.

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

## Proved deterministic machine-model result

The model bridge now supplies both quantitative compiler directions between the pinned mathlib finite-TM2 presentation and the locked Programme deterministic multitape model.

- `MathSolve/PNP/TM2ForwardCompiler.lean` constructs `tm2ToProgrammeCompiler_constructive`. Its target Programme runtime is the exact startup cost plus a fixed source-machine statement factor times the imported TM2 runtime, and it proves the required affine simulation-overhead contract.
- `MathSolve/PNP/ProgrammeTM2ReverseCompiler.lean` constructs `programmeToTM2Compiler_constructive`. The reverse finite-TM2 interpreter includes explicit initialization, work-tape preservation, terminal cleanup, output transport, and an affine runtime bound in input length and source Programme runtime.
- `MathSolve/PNP/ModelBridgeClosure.lean` instantiates both compiler contracts to prove `importedTM2_iff_programmePolyTime_constructive`.

This discharges `PNP-BRIDGE-MODEL-001` for deterministic polynomial-time decision functions only. It does not prove an NP verifier/class equivalence, an endpoint theorem, `P = NP`, or `P != NP`.

## Remaining boundary

`PNP-BRIDGE-NP-001` is now the next native bridge target. It must transport the deterministic verifier semantics, self-delimiting input/witness pairing, polynomial witness-length bound, malformed-pair behavior, totality, and class carrier. The deterministic machine-model prerequisite is no longer the blocker.

Concrete endpoint parser, malformed-input, size, correctness, and reduction obligations remain endpoint-specific under `PNP-BRIDGE-ENDPOINT-001`.

## Verification

```text
lake env lean MathSolve/PNP/CarrierBridge.lean
lake env lean MathSolve/PNP/PolyBoundBridge.lean
lake env lean MathSolve/PNP/TM2ForwardCompiler.lean
lake env lean MathSolve/PNP/ProgrammeTM2ReverseCompiler.lean
lake env lean MathSolve/PNP/ModelBridgeClosure.lean
python ci/validate_pnp_bridge_001.py
python -m unittest ci/test_pnp_bridge_001.py -v
```

Passing these checks proves the carrier bridge, the two-way polynomial-bound presentation bridge, and deterministic polynomial-time equivalence between the pinned finite-TM2 and Programme machine presentations. It does not prove `P = NP`, `P != NP`, NP-verifier/class equivalence, an endpoint result, novelty, promotion eligibility, or any MATHCERT disposition.
