# BSD-R2-A1-WP27 — good-ordinary place-2 control filtration

## Metadata

- Campaign: `BSD-001`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Parent: protected `BSD-R2-A1-WP26-ODD-COMPONENT-NORM`.
- Protected MATHSOLVE baseline: `47365c058f4362684327bdb268d98c0981e2f001`.
- Protected MATHFORGE source authority: `b09faf74936611616465186c8702ea0ce6f36828`.
- Source interface: protected `GREENBERG_P2_PRIMITIVE_LOCAL_CONTROL_SOURCE_AUDIT.md`.
- Claim boundary: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.
- Primary type: exact place-`2` filtration theorem for the remaining local universal-norm obstruction.

## Protected input

WP25 identifies

`U_2 := E(Q_2)/N_2^infinity ~= K_2^vee`,

where `K_2` is the primitive classical-Kummer local restriction kernel.

WP23 and its protected Greenberg source audit prove that the base good-ordinary local-control calculation factors through the connected-ordinary quotient. The proof retains two finite pieces:

1. the finite Kummer-versus-connected-ordinary discrepancy;
2. the connected-ordinary restriction kernel.

Each has order

`#E_tilde(F_2)[2^infinity] = 3-a_2`.

WP26 proves that all odd-prime local generator obstructions are already explicit Neron-component data. The remaining structural D1b question is therefore the position of the saturated generator in `U_2`.

## WP27 result

Put

`R_2 := E_tilde(F_2)[2^infinity]`.

Let

`D_2 := Im(lambda_2)/Im(kappa_2)`

be Greenberg's finite Kummer/ordinary discrepancy and let

`J_2`

be the connected-ordinary restriction kernel in the factorization of the classical-Kummer restriction map.

WP27 proves canonically

`D_2 ~= R_2`,

`J_2 ~= H^1(Gamma_2,R_2)`,

and an exact sequence

`0 -> D_2 -> K_2 -> J_2 -> 0`.

The cyclotomic local extension at `2` is totally ramified, so the residue group `R_2` is unchanged along the tower and the source calculation gives

`#D_2=#J_2=3-a_2`.

Dualizing and using protected WP25 gives the exact filtration

`0 -> J_2^vee -> U_2 -> D_2^vee -> 0`.

No splitting is asserted.

For the saturated global generator `P`, write

`x_2(P):=[P]_2 in U_2`

and let

`q_2(P)`

be its image in `D_2^vee`. Define

`r_2(P):=ord_2(ord(q_2(P)))`.

Then

`2^{r_2(P)} x_2(P) in J_2^vee`.

Call this element

`y_2(P):=2^{r_2(P)}x_2(P)`

and define

`s_2(P):=ord_2(ord(y_2(P)))`.

WP27 proves exactly

`rho_2(P)=r_2(P)+s_2(P)`.

Both coordinates satisfy

`0 <= r_2(P), s_2(P) <= ord_2(3-a_2)`.

Thus the previously opaque place-`2` order is represented by the exact position of one point in a two-step finite extension.

## Refined boundary

WP27 replaces

`MISSING_P2_GOOD_ORDINARY_SATURATED_GENERATOR_UNIVERSAL_NORM_ORDER_AT_2`

with

`MISSING_P2_SATURATED_GENERATOR_POSITION_IN_GOOD_ORDINARY_CONTROL_EXTENSION`.

The next theorem must identify or compute the two extension coordinates of `[P]_2`. In particular, a successor must prove any claimed relationship between `q_2(P)` and literal reduction of `P`, or between `y_2(P)` and a connected/formal norm or logarithmic class.

## Claim firewall

WP27 does not prove:

- a value of `r_2(P)`, `s_2(P)`, or `rho_2(P)`;
- that `U_2` splits as `J_2^vee x D_2^vee`;
- that `q_2(P)` is literally the reduction of `P`;
- that `y_2(P)` is a formal-group logarithm or connected norm index;
- equality with a regulator, height, Bockstein, Euler factor, or analytic term;
- D1a, D1c, or D2;
- `delta_2(E)=len_Z2 Sha(E/Q)[2^infinity]`;
- `BSD-R2-A1`;
- any MATHCERT certification, novelty, priority, patentability, or commercial claim.
