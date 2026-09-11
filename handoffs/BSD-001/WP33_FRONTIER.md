# BSD-001 WP33 frontier

## Candidate predecessor identities

WP33 is authored from protected MATHSOLVE

`08042c26cee67ddc998163b35503c6d7bb2a0d96`

and corrected protected MATHFORGE source authority

`3966bccfe4c8e788f0ca978b5d62cd2e20119043`.

No WP33 conclusion is protected until exact-head review, affected CI, merge, and protected-main readback complete.

## Candidate WP33 result

For every odd bad semistable prime `ell|N`, let

`a_ell=+1`

for split multiplicative reduction and

`a_ell=-1`

for nonsplit multiplicative reduction.

WP33 proves

`len_Z2 E(Q_ell)^wedge_2
 = v2(ell-a_ell)+v2(c_ell)`.

The proof uses the protected Neron filtration. The formal subgroup is pro-`ell` and therefore uniquely `2`-divisible; the `2`-adic completion is consequently the maximal `2`-primary quotient of the finite Neron quotient `E(Q_ell)/E_1(Q_ell)`. Its order is

`(ell-a_ell)c_ell`,

because the connected multiplicative torus has `ell-1` rational points in the split case and `ell+1` in the nonsplit case.

Protected WP22 already gives

`len_Z2 K_ell^vee=v2(c_ell)`.

Therefore the exact surplus of the Burns–Macias point-completion term over the protected Tamagawa/control term is

`tau_ell=v2(ell-a_ell)`.

Summing over bad primes gives

`len_Z2 D_bad^BM
 = sum_{ell|N}v2(ell-a_ell)
   + sum_{ell|N}v2(c_ell)`.

## Candidate next boundary

At a multiplicative prime,

`v2(1-a_ell/ell)=v2(ell-a_ell)`

because `ell` is a `2`-adic unit.

This nominates, but does not prove, the exact next comparison:

`MISSING_P2_BURNS_MACIAS_TORIC_EULER_FACTOR_RECONCILIATION`.

The required next source/determinant tranche must determine the exact primitive/imprimitive analytic normalization used by the Burns–Macias determinant formalism and prove, with sign and determinant-line conventions fixed, whether the toric local factors account for the WP33 surplus.

Do not infer cancellation merely from equality of valuations.

## Other boundaries retained

- D1a `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
- D1c `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2 `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`;
- protected WP31 `MISSING_P2_FINITE_TWISTED_RECIPROCITY_EXPONENT`;
- `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`;
- MATHCERT-only certification authority.

## Claim firewall

WP33 is a local finite-group/Fitting calculation. It does not prove an analytic Euler-factor cancellation, a determinant generator, a regulator identity, BSD, novelty, or certification.
