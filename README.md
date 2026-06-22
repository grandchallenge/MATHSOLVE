# MATHSOLVE

MATHSOLVE is the tactical orchestration pillar of the Grand Challenge mathematics stack.

It decides which mathematical moves to try, when to invoke search or exact computation, and how to route provisional evidence toward certification. It does not own the final proof boundary.

Work Packages carry stable knowledge graph and versioned classification mapping
references from MATH-PROGRAMME. Those references provide navigation and
provenance; they do not change claim status or certification.

## Programme links

MATH-PROGRAMME is the front door and policy source for this pillar.

- [MATH-PROGRAMME Pages home](https://grandchallenge.github.io/MATH-PROGRAMME/)
- [Programme Atlas](https://grandchallenge.github.io/MATH-PROGRAMME/PROGRAMME_ATLAS/)
- [Three-pillar architecture overview](https://github.com/grandchallenge/MATH-PROGRAMME/blob/main/ARCHITECTURE_OVERVIEW.md)
- [MATHSOLVE pillar doctrine](https://github.com/grandchallenge/MATH-PROGRAMME/blob/main/MATHSOLVE_SPEC.md)
- [Grand Challenge Work Package Standard](https://github.com/grandchallenge/MATH-PROGRAMME/blob/main/GRAND_CHALLENGE_WORK_PACKAGE_STANDARD.md)
- [Cross-pillar lanes](https://grandchallenge.github.io/MATH-PROGRAMME/CROSS_PILLAR_LANES/)
- [Groebner and EXPSPACE doctrine](https://grandchallenge.github.io/MATH-PROGRAMME/GROEBNER_EXPSPACE_DOCTRINE/)
- [Claim-boundary doctrine](https://grandchallenge.github.io/MATH-PROGRAMME/CLAIM_BOUNDARY_DOCTRINE/)
- [Resource Budget Policy](https://grandchallenge.github.io/MATH-PROGRAMME/RESOURCE_BUDGET_POLICY/)

## Gröbner tactic orchestration

MATHSOLVE now includes a Gröbner tactic orchestration doctrine for polynomial subproblems. The lane connects MATHFORGE discovery artifacts to MATHCERT certification artifacts:

```text
MATHFORGE  -> generate candidate algebraic witnesses
MATHSOLVE  -> decide when to invoke them tactically
MATHCERT   -> check, certify, and preserve the proof boundary
```

MATHSOLVE may choose a Gröbner-style tactic when a local proof obligation can be phrased as polynomial identity checking, normal-form computation, ideal membership, ideal equality, elimination, radical membership, or finite-truncation algebra.

See `docs/grobner_tactic_orchestration.md`.

## TROPIC-GROEBNER orchestration

MATHSOLVE also includes a TROPIC-GROEBNER route for sparse, valuation-aware, or toric polynomial obligations where the weight choice should be treated as a tactical decision before exact certification.

```text
support / valuation audit
  -> candidate weights
  -> weighted initial ideals
  -> retained or rejected route records
  -> MATHCERT tropical-initial-ideal certificate
```

See `docs/tropic_groebner_orchestration.md` and `work_packages/TROPIC_GROEBNER_001.md`.
