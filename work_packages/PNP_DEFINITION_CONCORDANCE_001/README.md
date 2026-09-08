# PNP-DEFINITION-CONCORDANCE-001

This Solve-owned package closes the vague “definition audit pending” state by comparing the exact imported Lean definitions behind `ComplexityTheory.P_ne_NP` with the protected Programme P-versus-NP lock.

## Result

The imported source is materially aligned on binary inputs, exact input length, total halting, Boolean output, deterministic verification, uniform finite machines, and polynomially bounded witnesses. The upstream theorem has only the separation orientation `P != NP`, and its `by sorry` body is explicitly treated as a placeholder rather than proof evidence.

The audit does **not** establish theorem-level equivalence. Five explicit bridges remain open:

1. Boolean decision functions versus language sets;
2. finite TM2 versus the Programme multitape model;
3. `Polynomial Nat` evaluation bounds versus the Programme asymptotic bound;
4. class-extensional equivalence of the two NP verifier presentations; and
5. parsing, malformed-input, size, correctness, and reduction obligations for any concrete NP-complete endpoint.

The exact machine-readable findings and source identities are in `concordance.json`. The next bounded Solve target is `PNP-BRIDGE-001`, a proof-bearing bridge suite. The MATHCERT route remains `pending`.

## Verification

```text
python ci/validate_pnp_definition_concordance.py
python -m unittest ci/test_pnp_definition_concordance.py -v
```

Passing these checks proves only structural integrity and preservation of the stated boundary. It does not resolve P versus NP or certify any mathematical claim.
