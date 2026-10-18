# R-H — Bader 93 reconstruction

**State:** `EXECUTION_CANDIDATE__H1_07_PENDING`

The protected Forge literature audit identifies an externally reported straight-line-realizable 93-triangle order type for `n=18`, attributed to Johannes Bader. The exact order table is preserved in `BADER_93_ORDER_TABLE.json` from `zegalur/line-order@2631b879...`.

Following the LineOrder straightening formulation, GCL reconstructed a numerical realization, then rounded the slope/intercept representation to a common denominator 1000. The resulting integer line coefficients are stored at `candidates/RH_BADER_RECONSTRUCTION_093/solution.json`.

The numerical optimizer is not trusted. Promotion requires three exact checks:

1. `verify_bader_93_order.py` proves every consecutive published crossing-order inequality using the exact integer determinant form of the LineOrder `F` predicate and verifies the three published parallel pairs;
2. the independent exact direct-interior oracle returns 93;
3. the authenticated AutoLab public evaluator returns 93 for the identical `solution.json`.

The reconstructed rational coefficients are GCL-generated. They are not attributed to Bader and are not claimed to be the original coordinates used to establish stretchability.

No best-known, optimality, novelty, priority, official competition-acceptance, or certification claim is made by this reconstruction.
