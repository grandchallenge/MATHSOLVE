# Proof-obligation DAG

## Dependency graph

```text
C001  CCC substrate
 | \
 |  +----------> C003  reflection adequacy
 v                  |
C002 guarded laws   |
 |                  v
 |               C004  external refinement compatibility
 |                  |
 +--------+---------+
          v
       C005  one-step admission preservation
          |
          v
       C006  productive guarded iteration
```

## Obligations

### C001 — CCC substrate

Construct the direct presheaf presentation:

- stage-indexed carriers;
- restriction maps;
- natural transformations;
- identity and composition;
- terminal object and binary products;
- Kripke exponentials;
- evaluation;
- currying;
- the beta/eta equations needed by the downstream interpretation.

### C002 — guarded laws

Construct and prove:

- `Later` stage shift;
- `next : A -> Later A`;
- a guarded fixed-point section for `f : Later A -> A`;
- restriction coherence;
- the pointwise guarded unfold law.

### C003 — reflection adequacy

Construct an intrinsically typed object language with product, function, and guarded types. Define closed `Prog tau`, quotation as syntax identity/embedding where appropriate, and interpretation into the stage model. Prove the exact staged adequacy statement. Do not introduce semantic reification.

### C004 — external refinement compatibility

Define a non-vacuous relation domain of represented programs/morphisms. Prove:

- reflexivity;
- transitivity;
- scoped monotonicity under composition;
- scoped preservation by currying;
- scoped preservation by evaluation.

The relation domain must contain the represented objects used by C005.

### C005 — one-step preservation

State the checker/admission assumptions as parameters or hypotheses, not hidden axioms. Prove that an accepted replacement preserves the typed contract and external refinement invariant, while rejected proposals leave the state unchanged.

### C006 — iteration

Only after C005 closes, construct the guarded trace and prove productivity. C006 may not be used to strengthen C005 retroactively.

## Failure discipline

If any obligation forces a material change to the frozen M0 formal object, stop this DAG and return to INTELLECT. Do not repair the target silently inside the proof.
