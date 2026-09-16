# BSD-001 canonical continuation handoff

## Cold start

Protected repository state is operational authority. Re-fetch live protected heads before mutation, then read:

1. `.gcl/campaigns/BSD-001/CAMPAIGN_STATE.json`;
2. `.gcl/operations/BSD-R5-RECIP/OPERATION.json`;
3. `handoffs/BSD-001/R5_RECIP_FRONTIER.md`;
4. `work_packages/BSD_R5_RECIP_P2_NORMALIZED_RECIPROCITY/01_LITERAL_P2_LOCAL_LATTICE_THEOREM.md`;
5. `work_packages/BSD_R5_RECIP_P2_NORMALIZED_RECIPROCITY/02_LITERAL_P2_SYMBOL_AND_RECIPROCITY_THEOREM.md`;
6. `work_packages/BSD_R5_RECIP_P2_NORMALIZED_RECIPROCITY/03_CLAIM_LEDGER.yaml`.

Campaign: `BSD-001 — Birch-Swinnerton-Dyer selected rank-one 2-primary campaign`. Programme owner: `grandchallenge/MATHSOLVE#164`; parent tracker: `#215`; current operation: `#278` (`BSD-R5-RECIP`). Exact operation base: `7d72d4f8aec2019a8eefb4db4fe151e4f14b1211`. Mathematical predecessor: protected R5-RES completion `24081fcc1b212d33dd865cc5512a837b8101faf1`. Protected source authority: `grandchallenge/MATHFORGE@cd814844128167d0e4cdb48f69f9d01c6c0be883`.

The candidate closes only

`MISSING_P2_NORMALIZED_ANOMALOUS_ORDINARY_KATO_KURIHARA_RECIPROCITY`.

It proves the selected literal-2 local dual-exponential lattice, the selected 2-saturated modular-element normalization with exact real-period factor, the scaled KKS derivative replay, and the finite normalized reciprocity identity

`xi_n(exp^*(loc^s_2(kappa_n^Kato))) = u_n * Delta_n^(2)`

with `Delta_n^(2)=2^t_2 delta_tilde_n`.

No nonzero `Delta_n^(2)` witness is asserted. If the candidate is protected, the next theorem is

`MISSING_P2_NORMALIZED_FINITE_KURIHARA_NONVANISHING_WITNESS`.

If `t_2>=2`, the proved half-integrality bound forces this particular normalized Kurihara witness to vanish modulo 2 for every index; that sublane requires a different residual witness. This is not a global Kato-class vanishing theorem.

R5-LIFT remains protected. R5-PRIM and R5-RES remain unestablished. Do not promote D2d, `BSD-R2-A1`, novelty/priority, public certification, or MATHCERT certification.

Run the R5-RECIP preflight and certificate named by the operation contract before exact-head review. Governed-artifact changes after freeze invalidate the freeze and affected exact-head evidence.
