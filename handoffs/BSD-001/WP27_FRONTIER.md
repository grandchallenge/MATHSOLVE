# BSD-001 frontier after WP27

## Status and authority

This is the continuity record for the WP27 candidate. It becomes protected only after exact-head admission to MATHSOLVE `main` and protected readback.

- Campaign: `BSD-001`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Candidate protected-base MATHSOLVE head: `47365c058f4362684327bdb268d98c0981e2f001`.
- Protected MATHFORGE source authority: `b09faf74936611616465186c8702ea0ce6f36828`.
- Selected target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.
- Mathematical certification remains a MATHCERT function.

## Protected chain entering WP27

WP25 gives, for every finite place,

`U_v ~= K_v^vee`

and represents the global character-image length by the local generator obstruction orders.

WP26 evaluates every odd bad local term exactly:

`rho_ell(P)=ord_2(ord(comp_ell(P)))`.

Thus

`rho_E=max(rho_2(P),rho_bad(P))`,

with all structural uncertainty concentrated at `2`.

WP23 and its protected Greenberg source interface give

`#K_2=(3-a_2)^2`

and record that Greenberg's proof obtains this square as two exact finite pieces: the Kummer/ordinary discrepancy and the connected-ordinary restriction kernel.

## WP27 representation

Put

`R_2=E_tilde(F_2)[2^infinity]`.

Define

`D_2=Im(lambda_2)/Im(kappa_2)`

and let `J_2` be the connected-ordinary restriction kernel occurring in Greenberg's factorization.

WP27 proves

`D_2 ~= R_2`,

`J_2 ~= H^1(Gamma_2,R_2)`,

and the exact kernel extension

`0 -> D_2 -> K_2 -> J_2 -> 0`.

Both end terms have order `3-a_2`.

Dualizing through protected WP25 yields the exact universal-norm filtration

`0 -> J_2^vee -> U_2 -> D_2^vee -> 0`.

No splitting is asserted.

For

`x_2(P)=[P]_2 in U_2`,

let

`q_2(P)`

be its quotient image in `D_2^vee` and write

`ord(q_2(P))=2^{r_2(P)}`.

Then

`y_2(P):=2^{r_2(P)}x_2(P)`

lies in `J_2^vee`; write

`ord(y_2(P))=2^{s_2(P)}`.

WP27 proves exactly

`rho_2(P)=r_2(P)+s_2(P)`.

Consequently

`rho_E=max(r_2(P)+s_2(P),rho_bad(P))`,

and

`len_Z2(C_E^vee)
 = 2 ord_2(3-a_2)
   + sum_{ell|N} ord_2(c_ell)
   - max(r_2(P)+s_2(P),rho_bad(P))`.

## New structural boundary

The former place-`2` order boundary

`MISSING_P2_GOOD_ORDINARY_SATURATED_GENERATOR_UNIVERSAL_NORM_ORDER_AT_2`

is replaced by

`MISSING_P2_SATURATED_GENERATOR_POSITION_IN_GOOD_ORDINARY_CONTROL_EXTENSION`.

The problem is no longer to determine the abstract size or filtration of `U_2`. It is to identify the two exact coordinates of the saturated generator inside that filtration.

## Preferred successor

Do not assume the filtration splits.

The next bounded reconnaissance should ask only for compatibility of local norm duality with the good-ordinary reduction/formal filtration:

1. whether the quotient coordinate `q_2(P)` is represented by an exact reduction-theoretic class of `P`;
2. whether, after killing that quotient coordinate, the residual class `y_2(P)` is represented by an exact connected/formal universal-norm quotient;
3. whether either identification is valid literally at `p=2` in the cyclotomic `Z_2` extension.

The closest source leads already identified are J. W. Jones, *On the local norm map for abelian varieties with good ordinary reduction* (J. Algebra 138 (1991), 420–423), and height-one formal-group norm results. They are reconnaissance leads only; no theorem from them is admitted or used in WP27.

Any external compatibility premise must route through MATHFORGE before downstream use.

## Other boundaries remain

- D1a: `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
- D1c: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2: `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`.

WP27 does not merge these boundaries with the local position problem.

## Claim firewall

WP27 does not prove:

- any value of `r_2(P)`, `s_2(P)`, or `rho_2(P)`;
- a split decomposition of `U_2`;
- literal-reduction or formal-logarithm interpretations of the two coordinates;
- an equality with a regulator, height, Bockstein, Euler factor, or analytic term;
- D1a, D1c, or D2;
- `BSD-R2-A1`;
- any MATHCERT certification, novelty, priority, patentability, or commercial claim.

## Continuation rule

Before successor mutation, re-fetch protected state. Use WP27 only if its exact bytes have been admitted to protected MATHSOLVE `main`. Continue through bounded source admission where needed, exact-head non-authoring/read-only Adversary and Referee review, affected ordinary CI/GCL checks, protected merge, protected readback, and #164 maintenance.
