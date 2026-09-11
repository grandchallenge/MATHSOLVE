# BSD-001 frontier after WP28

## Status and authority

This is the continuity record for the WP28 candidate. It becomes protected only after exact-head admission to MATHSOLVE `main` and protected readback.

- Campaign: `BSD-001`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Candidate protected-base MATHSOLVE head: `8628ad1d612b45e5254dcf5fa7165b986c371000`.
- Protected MATHFORGE source authority: `e5c49ee60ba300cff8026ddf65059c3049ab1226`.
- Selected target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.
- Mathematical certification remains a MATHCERT function.

## Protected chain entering WP28

WP25 identifies every local control group with an exact stabilized universal-norm quotient.

WP26 evaluates every odd bad local generator obstruction by the Neron component of the saturated generator:

`rho_bad(P)
 = max_{ell|N} ord_2(ord(comp_ell(P)))`.

WP27 gives an exact abstract two-step filtration of `U_2` and proves that the order depth of `[P]_2` is the sum of its two extension-coordinate depths. It intentionally leaves the coordinates abstract.

MATHFORGE now protects Tan's literal-`p=2`, totally ramified, good-ordinary reduction/formal universal-norm filtration.

## WP28 concrete place-2 filtration

Let

`F_2^norm
 := Ehat(2 Z_2) /
    intersection_n N_{L_n/Q_2} Ehat(m_{L_n})`.

WP28 proves the exact sequence

`0 -> F_2^norm
   -> U_2
   -> E_tilde(F_2)
   -> 0`,

where the quotient map is induced by literal reduction.

Protected WP07 gives

`#E_tilde(F_2)=3-a_2 in {2,4}`,

and protected WP23/WP25 give

`#U_2=(3-a_2)^2`.

Therefore

`#F_2^norm=3-a_2`.

For the saturated global generator, define

`Pbar_2=red(P) in E_tilde(F_2)`,

`r_red(P)=ord_2(ord(Pbar_2))`.

Let

`x_2(P)=[P]_2 in U_2`.

Then

`2^{r_red(P)}x_2(P)`

lies in the formal norm subgroup. Let

`z_form(P) in F_2^norm`

be its unique formal preimage and set

`s_form(P)=ord_2(ord(z_form(P)))`.

WP28 proves

`rho_2(P)=r_red(P)+s_form(P)`.

Thus

`rho_E=max(r_red(P)+s_form(P),rho_bad(P))`

and

`len_Z2(C_E^vee)
 = 2 ord_2(3-a_2)
   + sum_{ell|N} ord_2(c_ell)
   - max(r_red(P)+s_form(P),rho_bad(P))`.

## New substantive boundary

The former abstract position boundary

`MISSING_P2_SATURATED_GENERATOR_POSITION_IN_GOOD_ORDINARY_CONTROL_EXTENSION`

is replaced by

`MISSING_P2_FORMAL_UNIVERSAL_NORM_ORDER_OF_REDUCTION_KILLED_GENERATOR`.

All other terms in the D1b formula are now finite arithmetic data:

- local trace `a_2`;
- Tamagawa numbers;
- odd-prime Neron components of `P`;
- literal reduction of `P` modulo `2`.

The remaining unknown is exactly the order of one explicit element in the finite formal universal-norm quotient.

## Preferred successor

Do not resume broad BSD literature screening.

The next bounded task should determine whether the protected Tan formal quotient can be made element-explicit for

`2^{r_red(P)}P`,

not just group-explicit.

The protected source gives an ambient isomorphism, in dimension one, of the form

`F_2^norm ~= Gamma_2/(1-u)Gamma_2`

for Tan's Frobenius twist scalar `u`. The next source/construction question is:

> Is there a literal-`p=2` element-level norm-coordinate or formal-logarithm theorem that identifies the class of a base formal point in this quotient, with all normalization factors explicit?

A candidate theorem must preserve the difference between:

- the ambient group order;
- the element order of `z_form(P)`;
- Tan's scalar `u`;
- the protected unit root `alpha`;
- any WP20 Bockstein/regulator scalar.

Do not identify any two of these merely because their valuations coincide.

If a source supplies only the ambient quotient and not the point class, it does not close the new boundary.

## Other boundaries remain

- D1a: `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
- D1c: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2: `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`.

## Claim firewall

WP28 does not prove:

- a value of `s_form(P)` or `rho_2(P)`;
- an element-level formal logarithm/norm-coordinate formula;
- `u=alpha` or `u=alpha^(-1)`;
- an equality with a regulator, height, Bockstein, Euler factor, or analytic term;
- D1a, D1c, or D2;
- `BSD-R2-A1`;
- any MATHCERT certification, novelty, priority, patentability, or commercial claim.

## Continuation rule

Before successor mutation, re-fetch protected state. Use WP28 only if its exact bytes have been protected on MATHSOLVE `main`. Any new external element-level theorem premise must first be admitted through MATHFORGE. Continue through exact-head Adversary/Referee review, affected CI/GCL checks, protected merge/readback, and #164 maintenance.
