# HC-WP01 — Native false-proof atlas

**Campaign:** `HC-001`  
**State:** `COMPLETE_FOR_HC-R021_SELECTION`  
**Executable ledger:** `campaign_ledgers/HC-001/false_proof_atlas.json`

## Objective

Turn the Forge WP00 false-proof seeds into Solve-owned route tests. Each fixture identifies the tempting argument, exact invalid step, silently inserted theorem or assumption, rejection scope, surviving route, and theorem-spine node.

A candidate proof route fails WP01 if it triggers a fixture and cannot point to an explicit theorem or algebraic construction that closes the hidden step.

## Coverage

The native ledger covers coefficient drift, rationality drift, divisor extrapolation, inverse-Lefschetz and Kunneth-projector circularity, Hodge-locus and deformation substitution, numerical-period and Tate substitution, topological-versus-algebraic Chern generation, Abel-Jacobi incompleteness, projective-to-Kahler drift, absolute/motivated substitution, generic-to-every-fiber quantifier drift, and effectivity strengthening.

## HC-R021 result

`HC-R021-A8-CM4-C2` passes the coefficient, projective-domain, rationality, projector, Hodge-locus, numerical, Tate, motivated, and effectivity fixtures under its exact statement.

One fixture remains deliberately active:

```text
HC-FP-007 / HC-O013 — deformation substitution.
```

Markman's construction proves that the normalized characteristic class remains Hodge under the relevant Weil-type deformations; it does not prove that the class remains algebraic. The route may cross that edge only through semiregularity, an equivalent all-orders deformation theorem for the specific object, or an explicit relative algebraic replacement.

`HC-R021-L001` closes only the first-order implication under weak injectivity of the semiregularity map on the ambient-obstruction image. It does not discharge the all-orders fixture.

The target also avoids `HC-FP-014` by restricting the theorem to the Hodge-generic locus. No statement for special fibers with extra rational Hodge classes is implied.

## Closure

WP01 is complete for current target selection. Reopen it if the target formulation or construction mechanism changes enough to introduce a new semantic bridge or a failure mode not represented by the ledger.
