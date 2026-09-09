# BSD-R2-A1-WP18A — verified reconnaissance cohort

## Purpose

WP18A qualifies a minimal two-curve diagnostic cohort spanning both protected WP13 local regimes. It establishes only the exact local baseline needed before finite `2^n`-Selmer measurements begin.

This package is diagnostic. It does not prove `BSD-R2-A1`, compute the missing Fitting equality, certify any numerical BSD instance, or use analytic Sha as arithmetic evidence.

## Protected context

- Campaign: `BSD-001`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Authoring baseline: `grandchallenge/MATHSOLVE@1b5de80fa631f8065dbdbef5c7da187653120491`.
- Constitutional authority head at preflight: `grandchallenge/INTELLECT@f4610c37b7a010e0032666fe73f35eebb4b7a218`.
- Current selected claim: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.
- WP16A finite-level observable and WP16B primitive Fitting invariant remain the governing representation.

## Pinned external data provenance

The cohort identifiers, minimal models, stored ranks and torsion values are taken from John Cremona's `ecdata` repository at exact commit

`25cec5ecfec8b9f016eb1631ac633194c2bed39f`.

Material files:

- `docs/curves.1-1000.html` — minimal model, stored rank and torsion order;
- `allbsd/bsd.1-1000` — rank-one BSD table used only to corroborate the `r=1` analytic-rank reconnaissance datum;
- `docs/index.html` — format documentation.

The local arithmetic below is recomputed in-package by `verify_cohort.py` using integer arithmetic. No external local-reduction theorem is imported beyond the already-protected WP13 dictionary.

## Selected-hypothesis hard filter

Every atlas member must satisfy:

1. semistable over `Q`;
2. odd conductor;
3. good ordinary reduction at `2`;
4. irreducible `E[2]`;
5. analytic rank exactly one.

For the two curves below, the pinned tables also record algebraic rank one and trivial rational torsion.

Because the conductor is odd, reduction at `2` is good. The verifier counts points over `F_2`; both curves have

`#E(F_2)=4`,

so

`a_2 = 2 + 1 - 4 = -1`.

Thus both are ordinary at `2`.

Trivial rational torsion excludes rational `2`-torsion. Over `F_2`, a reducible two-dimensional Galois representation has an invariant line whose unique nonzero vector is fixed. Hence `E[2]` is irreducible for both cohort members. Protected WP12 then identifies the selected residual image with `GL_2(F_2) ~= S3`.

## Regime A control — `53a1`

Pinned minimal model:

`[1,-1,1,0,0]`.

The verifier recomputes

`Delta_min = -53`.

Thus the only bad-prime depth is

`n_53 = ord_53(Delta_min) = 1`.

Protected WP13 gives:

- `ord_2(c_53)=0`;
- residual conductor `N(rho_bar_{E,2})=53`;
- no residual-conductor drop.

Therefore `53a1` is a valid WP13 **regime A** control.

## Regime B control — `203b1`

Pinned minimal model:

`[1,1,1,0,-2]`,

that is

`y^2 + xy + y = x^3 + x^2 - 2`.

The verifier recomputes

`Delta_min = -1421 = -7^2 * 29`,

while

`N = 203 = 7 * 29`.

Therefore

`n_7=2`,

`n_29=1`.

Protected WP13 gives:

- `ord_2(c_7)=1`;
- `ord_2(c_29)=0`;
- the even-Tamagawa support is exactly `{7}`;
- residual conductor

  `N(rho_bar_{E,2}) = 29`;

- conductor drop

  `203 / 29 = 7`.

This is a valid WP13 **regime B** control.

The older Cremona table also lists the local Kodaira pattern `I_2, I_1` and component factors `2,1` for `203B1`; the protected claim here does not depend on that historical table because WP13 plus the recomputed discriminant depths already determines the required `2`-adic Tamagawa information.

## Recovery correction

During exploratory screening, the legacy compact file `allbsd/bsd.1-1000` was temporarily misread as though its approximate `rational factor` column were the Tamagawa product. The pinned format documentation states instead that the compact columns are conductor, class, rank, period, `L^(r)(1)/r!`, regulator, rational factor and analytic Sha.

That exploratory interpretation is rejected.

No cohort classification in this package uses that column as Tamagawa data. Regime classification is derived from the exact minimal discriminant depths and protected WP13.

## Reproducible verification

Run:

```bash
python work_packages/BSD_R2_A1_WP18A_RECON_COHORT/verify_cohort.py
```

Expected exact results:

- `53a1`: `Delta=-53`, `a_2=-1`, regime A, residual conductor `53`;
- `203b1`: `Delta=-7^2*29`, `a_2=-1`, regime B, even-Tamagawa support `{7}`, residual conductor `29`.

## What WP18A does not measure

WP18A deliberately does not populate:

- `#Sel_{2^n}`;
- `s_n(E)`;
- observed stabilization index;
- Cassels-Tate data;
- normalized `delta_2(E)`;
- `epsilon_n(E)=delta_2(E)-s_n(E)`.

Those belong to the immediate successor WP18B and must be obtained independently of BSD. In particular, an analytic Sha value from a database may not be substituted for a finite-level Selmer computation.

## Exact successor

`BSD-R2-A1-WP18B — finite 2^n-Selmer measurement on the verified A/B cohort`.

The next operational objective is to obtain reproducible exact finite-level Selmer data for `53a1` and `203b1`, at increasing `n`, with enough provenance to compute `s_n(E)` without assuming BSD.

If a computational package's mathematical algorithm is relied upon beyond routine execution, its correctness interface must be source-audited as required by the WP18 plan.

## Claim firewall

- `BSD-R2-A1` remains unproved.
- Cohort qualification is not certification.
- No numerical equality is a proof of BSD.
- No analytic Sha value is finite-Selmer evidence.
- No odd-prime theorem is specialized to `p=2`.
- No source or software result is promoted beyond the strength actually checked.
