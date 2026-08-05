# EUCLID-GCD-E2E-001 — Solve stage

## Concrete run

The deterministic producer receives `252` and `105` and emits:

\[
252=2\cdot105+42,\qquad
105=2\cdot42+21,\qquad
42=2\cdot21+0,
\]

together with

\[
-2\cdot252+5\cdot105=21.
\]

## Status labels

**Object:** the greatest common divisor.

**Construction:** the Euclidean division trace.

**Witness:** the integer coefficients `-2` and `5`.

**Candidate certificate:** the committed JSON record carrying the protected Forge identities, inputs, trace, result, witness, solver contract, and non-certification boundary.

The producer computes. It does not certify its own output.

## Protected input

The Solve stage consumes the protected MATHFORGE merge `3622bac82a39cdb9e82ec463919d9e6927c1ec0e`, including:

- `sources/EUCLID-GCD-E2E-001/forge_package.json`, Git blob `079b68fb5651e0d2eee0a7b2002454d34673d84c`;
- `provider_manifests/EUCLID-GCD-E2E-001.json`, Git blob `a103b2c85dbd67973da43656fed5af567c5b7074`.

## Determinism contract

The implementation uses Python integer arithmetic, no network access, and no randomness. Re-running the canonical command must reproduce the committed candidate byte-for-byte.

## Certification boundary

MATHCERT must use an independent checker that does not import or execute `solve/euclid_gcd.py`. It must verify provider identity, all trace equations and bounds, terminal normalization, divisibility, the Bézout equality, and the formal soundness theorem.

No novelty, priority, first-formalization, historical-verbatim-equivalence, or certificate-acceptance claim is made.

## Chaidez continuity

The final Programme reader will begin with the concrete divisions, but the exact theorem statement, source record, proof trace, claim ledger, and technical appendix remain authoritative. Future illuminated plates are pedagogical only. The Book VII documentary stage remains blocked pending exact source lock.
