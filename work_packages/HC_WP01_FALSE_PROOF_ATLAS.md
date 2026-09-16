# HC-WP01 — Native false-proof atlas

**Campaign:** `HC-001`  
**State:** `COMPLETE_FOR_HC-R021_SELECTION`  
**Executable ledger:** `campaign_ledgers/HC-001/false_proof_atlas.json`

## Objective

Turn the Forge WP00 false-proof seeds into Solve-owned route tests. Each fixture now identifies the tempting argument, exact invalid step, silently inserted theorem or assumption, rejection scope, surviving route, and theorem-spine node.

A candidate proof route fails WP01 if it triggers a fixture and cannot point to an explicit theorem or algebraic construction that closes the hidden step.

## Coverage

The native ledger covers:

- rational-to-integral coefficient drift;
- complex `(p,p)` to rational-class drift;
- higher-codimension divisor extrapolation;
- inverse-Lefschetz and Kunneth-projector circularity;
- Hodge-locus and deformation substitution;
- numerical-period substitution;
- Tate specialization/lifting substitution;
- topological-versus-algebraic Chern generation;
- Abel-Jacobi incompleteness;
- projective-to-Kahler drift;
- absolute/motivated-to-algebraic substitution;
- generic-to-every-fiber quantifier drift;
- effectivity strengthening.

## HC-R021 result

`HC-R021-A8-SW-Q3` passes the coefficient, domain, rationality, projector, Hodge-locus, numerical, Tate, motivated, and effectivity fixtures under its exact statement.

One fixture remains deliberately active:

```text
HC-FP-007 / HC-O013 — deformation substitution.
```

The route may use deformation only after it proves an adequate semiregularity or relative-cycle theorem. `HC-R021-L001` closes the first-order obstruction only; it does not discharge the all-orders deformation fixture.

The target also avoids `HC-FP-014` by explicitly restricting the theorem to the generic Hodge-ring locus. No statement for special fibers with additional Hodge classes is implied.

## Closure

WP01 is complete for current target selection. Reopen it only if the target formulation or construction mechanism changes enough to introduce a new semantic bridge or a new failure mode not represented by the ledger.
