# BSD-001 frontier after WP30

## Candidate identity

Work package:

`BSD-R2-A1-WP30-P2-TWIST-UNIT-ROOT-RECONCILIATION`.

Protected MATHSOLVE baseline used to author this package:

`366130ecf0102ffb0fb5ea5821be4ace1b48bcc3`.

Protected MATHFORGE source authority:

`5b07785c9ca96ec0c2003bbe3ada46c807e50882`.

Programme owner:

`grandchallenge/MATHSOLVE#164`.

## Exact result

WP30 proves the convention identity

`u=alpha`,

where `u` is the Hall/Tan one-dimensional twist scalar and `alpha` is the protected WP07 ordinary unit root.

Hence

`(1-u)Gamma_2
 = (1-alpha)Gamma_2
 = (1-alpha^(-1))Gamma_2`.

The protected WP29 quotient may therefore be written exactly as

`F_2^norm
 ~= Gamma_2/(1-alpha^(-1))Gamma_2`.

The selected class `theta_form(P)` is unchanged, and the protected finite invariant `tau_form(P)` is now an exact congruence depth relative to the WP07 unit-root modulus.

For the WP07 normalization

`e_2(E)=(1-alpha^(-1))^2`,

WP30 proves the exact principal-ideal equality

`(1-u)^2 Z_2=e_2(E)Z_2`.

This is local normalization concordance only.

## Active local boundary

The convention boundary is closed. The remaining D1b local element boundary is still

`MISSING_P2_TOROIDAL_FORMAL_COORDINATE_CONGRUENCE_DEPTH`.

The selected hypotheses do not impose a value of this depth. A successor must therefore either:

1. compute the selected toroidal class by an exact element-level theorem; or
2. compare the depth exactly to another protected arithmetic invariant that determines it.

## Reusable D1c/D2 clause

Any future determinant/interpolation theorem using the WP07 factor may now reuse the exact local equality

`(1-u)Z_2=(1-alpha^(-1))Z_2`.

Do not re-open this convention question unless a future theorem uses a genuinely different Frobenius normalization.

## Other protected boundaries unchanged

- D1a: `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`.
- D1c: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.
- D2: `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`.
- `BSD-R2-A1` remains `SELECTED_RESEARCH_TARGET_UNPROVED`.
- No MATHCERT certification is authorized.

## Claim firewall

WP30 does not convert ideal concordance into determinant cancellation, Bockstein equality, p-adic height comparison, or BSD. No power of `2` may be discarded under the phrase `up to a unit` outside the exact ideal statements proved here.
