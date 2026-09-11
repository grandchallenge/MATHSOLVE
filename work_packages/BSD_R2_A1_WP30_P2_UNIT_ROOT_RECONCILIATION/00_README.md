# BSD-R2-A1 WP30 — p=2 twist/unit-root normalization reconciliation

## Status

Candidate work package for the protected BSD-001 selected research target.

Exact protected MATHSOLVE baseline:

`366130ecf0102ffb0fb5ea5821be4ace1b48bcc3`.

Exact protected MATHFORGE source authority:

`5b07785c9ca96ec0c2003bbe3ada46c807e50882`.

Programme owner: `grandchallenge/MATHSOLVE#164`.

## Purpose

Protected WP29 writes the remaining formal universal-norm quotient as

`F_2^norm ~= Gamma_2/(1-u)Gamma_2`

and defines the canonical finite depth `tau_form(P)`. WP29 intentionally treats `u` as an auxiliary twist scalar and proves only its valuation.

WP30 uses the newly protected literal-`p=2` source reconciliation to identify the convention exactly:

`u=alpha`,

where `alpha` is the protected WP07 `2`-adic unit root of

`X^2-a_2 X+2`.

Because `alpha` is a unit,

`1-alpha^(-1)=-alpha^(-1)(1-alpha)`,

so the three submodules are identical:

`(1-u)Gamma_2
 = (1-alpha)Gamma_2
 = (1-alpha^(-1))Gamma_2`.

Hence WP29's quotient and depth can be written directly in the WP07 unit-root normalization without changing any group, element order, or depth.

## Main conclusions

WP30 proves:

`F_2^norm
 ~= Gamma_2/(1-alpha^(-1))Gamma_2`.

The protected WP29 class `theta_form(P)` is the same quotient class under this exact equality of denominator submodules.

Therefore `tau_form(P)` is exactly the congruence depth of that class relative to the protected WP07 ordinary modulus `(1-alpha^(-1))`.

For the WP07 normalization

`e_2(E)=(1-alpha^(-1))^2`,

one has the exact principal-ideal equality

`(1-u)^2 Z_2=e_2(E)Z_2`.

This is local normalization concordance only.

## Boundary

WP30 does not evaluate `tau_form(P)` and does not prove that any arithmetic determinant contains, cancels, or differentiates `e_2(E)`.

The active D1b boundary remains

`MISSING_P2_TOROIDAL_FORMAL_COORDINATE_CONGRUENCE_DEPTH`.

D1a, D1c, D2, `BSD-R2-A1`, and MATHCERT certification remain open.
