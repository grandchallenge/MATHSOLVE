# BSD-001 canonical continuation handoff

## Cold start

Protected repository state is operational authority. Re-fetch live protected heads before mutation, then read:

1. `.gcl/campaigns/BSD-001/CAMPAIGN_STATE.json`;
2. `.gcl/operations/BSD-R5-WIT/OPERATION.json`;
3. `handoffs/BSD-001/R5_WIT_FRONTIER.md`;
4. `work_packages/BSD_R5_WIT_NORMALIZED_KURIHARA_WITNESS/07_COHORT_AND_DIRECT_DETECTOR_BOUNDARY.md`;
5. `work_packages/BSD_R5_WIT_NORMALIZED_KURIHARA_WITNESS/09_CLAIM_LEDGER.yaml`;
6. protected provider `grandchallenge/MATHFORGE@3a097cf5f1ad5e12eeba83a08dccfbf7bc49b5f4`.

Campaign: `BSD-001 — Birch-Swinnerton-Dyer selected rank-one 2-primary campaign`. Programme owner: `grandchallenge/MATHSOLVE#164`; parent tracker: `#215`; current operation: `#282` (`BSD-R5-WIT`). Exact operation base: `8e692aaca7b0932c412a03eb33985ba5994b1d5f`. Protected R5-RECIP completion overlay: `9c9bd9077f8b269277366c7ee81dcdcd7f701217`. Protected source authority: `grandchallenge/MATHFORGE@3a097cf5f1ad5e12eeba83a08dccfbf7bc49b5f4`.

## R5-WIT candidate result

The operation entered on

`MISSING_P2_NORMALIZED_FINITE_KURIHARA_NONVANISHING_WITNESS`.

It proves exact local stratification on the selected/diagnostic cohort:

- `t_2=1`: `53a1`, `61a1`, `83a1`, `203b1`;
- `t_2=2`: `79a1`, `201b1`;
- `t_2=3`: `89a1`.

Protected R5-RECIP then makes the normalized Kurihara coordinate identically zero modulo two on every certified `t_2>=2` instance. This does not imply global residual Kato/Kolyvagin vanishing.

Exact PARI/GP reconnaissance found no single-prime normalized hit through `ell<=2000` on the two controls and none through `ell<=500` on the deterministic expanded cohort. These finite negative scans are not a nonexistence theorem on the `t_2=1` lane.

Protected WP60T supplies the direct bypass

`kappa_1^Kato{}_1 = c_Q^Kato mod 2`.

Hence `c_Q^Kato mod 2 != 0` would itself be a legitimate finite residual witness under protected R5-PRIM finite detection and would bypass the normalized Kurihara/local-regulator coordinate.

The protected MATHFORGE source audit does not currently supply a literal-`2` theorem or exact computation proving that indivisibility statement on the selected rank-one anomalous ordinary lane.

Candidate disposition:

`BLOCKED`

on

`MISSING_P2_BASE_KATO_CLASS_MOD2_NONVANISHING_ON_SELECTED_RANK_ONE_LANE`.

R5-LIFT and R5-RECIP remain protected. R5-RES and R5-PRIM remain unestablished. Do not promote D2d, `BSD-R2-A1`, novelty/priority, public certification, or MATHCERT certification.

Before review, run the R5-WIT preflight and exact certificates named by the operation contract. Governed-artifact changes after freeze invalidate the freeze and exact-head logical reviews.
