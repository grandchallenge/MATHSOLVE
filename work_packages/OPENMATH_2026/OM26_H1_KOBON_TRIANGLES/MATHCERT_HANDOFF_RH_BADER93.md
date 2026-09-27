# OM26-H1 MATHCERT handoff — R-H 93-triangle reconstruction

**State:** `PREPARED__PROTECTED_SOLVE_BIND_PENDING`

Requested Cert object: independently replay the exact candidate `RH_BADER_RECONSTRUCTION_093/solution.json` and adjudicate only the statement that this exact `n=18` rational straight-line arrangement has 93 counted triangular faces under the locked hill semantics.

## Source and producer evidence

- Forge literature audit: `grandchallenge/MATHFORGE@9e00c45fd665546b813f9234314a63eddbec854d`.
- External order table: `zegalur/line-order@2631b8793eb351be2ad6b8a91b7194eeb67e25bb`, `generate_gallery.py` blob `551747de426042e1542fa4b8f55c1383a9afe157`.
- Candidate Git blob: `bb244e4b0422922ae9f85cc4facb2109c33162b3`.
- Candidate SHA-256: `e606799ad6c1296deedb475440d1eecbe86daba8a3af625718f55726f93da4d5`.
- `BADER_93_SOURCE.json` and `BADER_93_ORDER_TABLE.json`.
- `H1_07_RH_BADER93_REPLAY_RECEIPT.json`.
- GitHub Actions run `36359791747`, job `108734545943`.

## Provenance distinction

The order type and attribution are external. The integer coefficients are a GCL reconstruction obtained from the published order table and LineOrder straightening formulation. Do not attribute the coefficients themselves to Johannes Bader.

## Explicit exclusions

Do not infer that 93 is globally best known, optimal, novel, first, officially accepted by AutoLab, or publication-ready. The literature audit separately records a simple-arrangement upper bound of 94 with a still-open transfer question to the hill's degeneracy semantics.

After this PR is protected, bind this packet to its exact protected Solve commit in MATHCERT as a separate successor to the earlier 86-triangle intake.
