# BSD-R2-A1-WP09 — auxiliary-K and corrected Disegni applicability

## Metadata

- Campaign: `BSD-001`.
- Work package: `BSD-R2-A1-WP09-DISEGNI-APPLICABILITY`.
- Native owner: `grandchallenge/MATHSOLVE#147`.
- Parent: `BSD-R2-A1-WP08-2MU-FIREWALL`.
- Protected Solve baseline: `e43e40e8ee7585149af7935712166ac8bf684584`.
- Protected Forge baseline: `d287f457537540a69eb9446bd71567db5e334fbd`.
- Protected Programme provider import: `b9219009c37ab12077a13f10dead8276836ad28b`.
- Selected claim: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

## Material result

Under the selected BSD-R2-A1 hypotheses, the admitted auxiliary-quadratic nonvanishing interface supplies an imaginary quadratic field

`K = Q(sqrt(D))`

with `D` fundamental, `(D,2N)=1`, `2` split in `K`, every prime `ell|N` split in `K`, and

`L(E^D,1) != 0`.

Because `ord_{s=1} L(E,s)=1` and

`L(E/K,s) = L(E,s)L(E^D,s)`, 

this auxiliary base change has analytic rank exactly one.

For this all-split auxiliary lane, the corrected Disegni Theorem B is applicable at `p=2` to the weight-two modular representation of `E` with trivial Hecke character. The applicability check is proved separately in `02_DISEGNI_APPLICABILITY.md`.

Consequently the campaign now has, for suitable test vectors with nonzero denominator, the exact source-normalized p-adic Gross-Zagier identity

`h_V(P_Pi(f1), P_{Pi^vee}(f2)) / (f3,f4)_Pi`

`= e_{2,infinity}(V_(pi,1))^(-1) * L'_2(V_(pi,1),0) * Q((f1 tensor f2)/(f3 tensor f4)).`

This is a p-adic height-to-p-adic-L-derivative identity. It is not the WP00 complex BSD leading-term identity.

## Source authority

The proof uses only the bounded provider interfaces protected in MATHFORGE:

- `sources/BSD-001/DISEGNI_PADIC_GROSS_ZAGIER_SOURCE_AUDIT.md`, blob `09506e79cf9f07579921966c11bd513f4351887c`;
- `sources/BSD-001/FRIEDBERG_HOFFSTEIN_AUXILIARY_K_SOURCE_AUDIT.md`, blob `2455f56e3069759c0882de6b4580664538c70043`.

MATH-PROGRAMME PR #913 imported the refreshed protected Forge identity through the native merge queue. Protected Programme readback is `b9219009c37ab12077a13f10dead8276836ad28b`. The provider-promotion gate for this package is therefore cleared.

## What this closes

WP09 closes:

1. existence of a single auxiliary imaginary quadratic field satisfying the selected `2N` splitting and twist-nonvanishing requirements;
2. exact analytic-rank-one base change in that lane;
3. the corrected Disegni hypothesis check at `p=2` for that lane;
4. availability of the p-adic Gross-Zagier formula in the source's normalization.

## What remains open

WP09 does not establish:

- nonvanishing of the p-adic derivative or p-adic height;
- equality of a p-adic height with the WP00 Neron-Tate regulator;
- an exact conversion of the p-adic derivative into `L'(E,1)/(Omega_E Reg_E)`;
- the WP08 relative-mu / height-one `(2)` component;
- an exact integral 2-primary Heegner/Kolyvagin index formula computing Sha and Tamagawa valuations;
- `BSD-R2-A1`;
- MATHCERT certification.

The surviving frontier is recorded in `05_NEXT_TARGET.md`.