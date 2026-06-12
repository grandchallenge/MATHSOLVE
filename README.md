# MATHSOLVE

MATHSOLVE is the tactical orchestration pillar of the Grand Challenge mathematics stack.

It decides which mathematical moves to try, when to invoke search or exact computation, and how to route provisional evidence toward certification. It does not own the final proof boundary.

## Gröbner tactic orchestration

MATHSOLVE now includes a Gröbner tactic orchestration doctrine for polynomial subproblems. The lane connects MATHFORGE discovery artifacts to MATHCERT certification artifacts:

```text
MATHFORGE  -> generate candidate algebraic witnesses
MATHSOLVE  -> decide when to invoke them tactically
MATHCERT   -> check, certify, and preserve the proof boundary
```

MATHSOLVE may choose a Gröbner-style tactic when a local proof obligation can be phrased as polynomial identity checking, normal-form computation, ideal membership, ideal equality, elimination, radical membership, or finite-truncation algebra.

See `docs/grobner_tactic_orchestration.md`.
