# BSD-R2-A1 WP39 — exact extended/Greenberg to primitive Kummer comparison over `K`

## State

`PROVED_BOUNDED_REDUCTION`

Protected predecessors:

- MATHSOLVE WP38: `efac1b7eaa9b7d1da42c9d33fbb73516fec93a42`;
- MATHFORGE WP39 source admission: `9de5bac5a18193b9453146dd0db9dee2f34ab06a`.

## Purpose

WP38 proved that the global rank-one Mordell–Weil free lattice does not acquire an index under the protected quadratic base change `K/Q`. The surviving D2b discrepancy was therefore the exact comparison between Nekovář's source-compatible extended/ordinary Selmer lattice over `K` and the classical primitive Kummer lattice.

WP39 makes this comparison explicit.

## Main result

For `T=T_2(E)` over the protected WP09 field `K`, good ordinary reduction at the two places above `2` and the protected vanishing of `E(K)[2^infinity]` imply

`H~^1_f(K,T) ~= S_T^str(K)`.

Nekovář's literal-`p=2` §9.6 comparison then gives a canonical injection

`H~^1_f(K,T) -> S_2(E/K)`

into the compact classical Kummer Selmer module. Define

`J_K := coker(H~^1_f(K,T) -> S_2(E/K))`.

Equivalently, `J_K` is the image of the classical compact Selmer group in the explicit local comparison module. Then

`0 -> H~^1_f(K,T) -> S_2(E/K) -> J_K -> 0`

is exact and `J_K` is finite.

The complete ambient local target has exact `Z_2`-length

`2 ord_2(3-a_2) + 2 sum_{ell|N} ord_2(c_ell)`.

Therefore

`0 <= len_Z2 J_K
   <= 2 ord_2(3-a_2) + 2 sum_{ell|N} ord_2(c_ell)`.

The upper bound is not promoted to equality.

## D2b reduction

WP39 replaces

`MISSING_P2_NEKOVAR_EXTENDED_TO_PRIMITIVE_KUMMER_LOCAL_INDEX`

by the exact finite incidence problem

`MISSING_P2_KUMMER_GREENBERG_GLOBAL_HIT_SUBGROUP_OVER_K`.

All local factor sizes are now explicit. The only remaining D2b datum is which elements of that finite ambient local module are hit by the global compact Kummer Selmer group.

## Claim firewall

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

WP39 does not prove:

- `J_K` equals the whole ambient local target;
- global localization surjectivity;
- fixed-`2` height nondegeneracy;
- Heegner-point primitivity;
- exact Disegni interpolation factors;
- classical/WP00 height normalization;
- final quadratic descent;
- D1c;
- BSD or MATHCERT certification.
