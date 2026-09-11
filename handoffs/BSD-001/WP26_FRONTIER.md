# BSD-001 frontier after WP26

## Status and authority

This is the continuity record for the WP26 candidate. It acquires protected status only after exact-head admission to MATHSOLVE `main` and protected readback.

- Campaign: `BSD-001`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Candidate protected-base MATHSOLVE head: `0e8040f6036b95a1f963fcf955a92bb46631c3c4`.
- Protected source head: `grandchallenge/MATHFORGE@b09faf74936611616465186c8702ea0ce6f36828`.
- Selected target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.
- Mathematical certification remains exclusively a MATHCERT function.

## Protected chain entering WP26

WP25 proves

`U_v := E(Q_v)/N_v^infty ~= K_v^vee`

and

`rho_E=max_v rho_v(P)`,

where `[P]_v` is the class of a saturated rank-one generator in `U_v` and

`rho_v(P):=ord_2(ord([P]_v))`.

## WP26 odd-prime evaluation

For every odd bad semistable prime `ell|N`, let

`Phi_ell(F_ell)`

denote the rational Neron component group over the residue field `F_ell`, and let

`comp_ell(P) in Phi_ell(F_ell)`

be the component of the saturated global generator.

WP26 uses only protected WP22 vanishing for the connected Neron subgroup and finite cyclic Tate cohomology to prove

`U_ell ~= Phi_ell(F_ell)/Phi_ell(F_ell)_odd`.

The universal-norm class `[P]_ell` is exactly the image of `comp_ell(P)` in this canonical `2`-primary quotient. Thus

`rho_ell(P)
 = ord_2(ord(comp_ell(P)))`.

Split multiplicative `I_n` retains arbitrary `2`-depth through the cyclic rational component group of order `n=c_ell`. Nonsplit multiplicative retains only the rational Frobenius-fixed component group of order `gcd(2,n)=c_ell`.

Define

`rho_bad(P)
 := max_{ell|N} ord_2(ord(comp_ell(P)))`.

Then

`rho_E=max(rho_2(P),rho_bad(P))`

and

`len_Z2(C_E^vee)
 = 2 ord_2(3-a_2)
   + sum_{ell|N} ord_2(c_ell)
   - max(rho_2(P),rho_bad(P))`.

## New structural frontier

All odd-prime universal-norm theorem shape is closed. The remaining structural D1b boundary is

`MISSING_P2_GOOD_ORDINARY_SATURATED_GENERATOR_UNIVERSAL_NORM_ORDER_AT_2`.

The exact unknown is the order of

`[P]_2 in U_2`,

where protected WP23/WP25 give

`#U_2=(3-a_2)^2`.

## Preferred next tranche

Do not return to broad literature screening.

Use the protected Greenberg local-control proof as the starting point. It factors the place-`2` kernel order into two exact factors, each of size `#E_tilde(F_2)[2^infinity]`:

1. the finite classical-Kummer versus connected-ordinary discrepancy;
2. the connected-ordinary restriction kernel.

Seek an exact short exact sequence or filtration on the **dual norm quotient** `U_2` corresponding to those two factors. Then locate the saturated generator class `[P]_2` in that filtration.

The immediate theorem query is not `#U_2`; that is already protected. It is the order of one element of `U_2`.

Any new local formal-group/norm theorem premise must first be admitted through MATHFORGE. A source or derivation must explicitly include residue characteristic `2`; an odd-prime norm theorem may not be specialized silently.

Do not assume the two Greenberg factors split as a direct product. Do not infer `[P]_2` from `a_2` alone.

## Other boundaries remain

- D1a: `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
- D1c: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2: `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`.

## Claim firewall

WP26 does not prove:

- a value of `rho_2(P)`;
- a splitting of `U_2`;
- a formal-logarithm formula at `2`;
- equality of any norm-order observable with a regulator, height, Bockstein, or analytic term;
- D1a, D1c, or D2;
- `delta_2(E)=len_Z2 Sha(E/Q)[2^infinity]`;
- `BSD-R2-A1`;
- any MATHCERT certification, novelty, priority, patentability, or commercial claim.

## Continuation rule

Before successor mutation, re-fetch protected state. Use WP26 only if its exact theorem bytes are protected on MATHSOLVE `main`. Continue through bounded proof, MATHFORGE admission where required, exact-head non-authoring/read-only Adversary and Referee passes, affected CI/GCL checks, protected merge, protected readback, and #164/handoff maintenance.

Stop only at a genuine theorem, source, authority, authentication, safety, material-state, target-drift, or MATHCERT boundary, and name that boundary exactly.
