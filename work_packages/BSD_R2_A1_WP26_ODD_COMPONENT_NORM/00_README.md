# BSD-R2-A1-WP26 — odd multiplicative universal norms via Neron components

## Metadata

- Campaign: `BSD-001`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Parent: protected `BSD-R2-A1-WP25-LOCAL-UNIVERSAL-NORM`.
- Protected MATHSOLVE baseline: `0e8040f6036b95a1f963fcf955a92bb46631c3c4`.
- Protected source baseline: `grandchallenge/MATHFORGE@b09faf74936611616465186c8702ea0ce6f36828`.
- Claim boundary: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.
- Primary type: internal exact evaluation of all odd multiplicative WP25 universal-norm classes in Neron-component terms.

## Protected input

WP25 proves for every finite place

`U_v := E(Q_v)/N_v^infty ~= K_v^vee`

and for a saturated global rank-one generator `P`,

`rho_E=max_v rho_v(P)`,

where

`rho_v(P):=ord_2(ord([P]_v))`.

WP22 already proves for each odd unramified `2`-power layer that the connected Neron subgroup `E_0` has vanishing cyclic `H^1` and `H^2`. Hence its Tate norm quotient vanishes.

## WP26 result

Let `ell|N` be an odd multiplicative prime of type `I_n`, and let

`comp_ell:E(Q_ell)->Phi_ell(F_ell)`

be the Neron component map.

WP26 proves at every finite unramified layer `F_m/Q_ell` that

`E(Q_ell)/N E(F_m)
 ~= Phi_ell(F_{ell^{2^m}})^{G_m}/N Phi_ell(F_{ell^{2^m}})`.

For split multiplicative reduction, with geometric component group `M=Z/nZ`, this is

`M/2^m M`,

which stabilizes to the canonical `2`-primary quotient

`M/M_odd`.

For nonsplit multiplicative reduction, Frobenius acts by `-1`; for every `m>=1`, the quotient is

`M[2] = Phi_ell(F_ell)`,

already stable.

Thus uniformly

`U_ell ~= Phi_ell(F_ell)/Phi_ell(F_ell)_odd`.

Under this canonical identification, `[P]_ell` is the `2`-primary image of `comp_ell(P)`. Consequently

`rho_ell(P)
 = ord_2(ord(comp_ell(P)))`.

For nonsplit reduction this is `0` or `1`; for split reduction it is the exact `2`-primary order of the component of `P` in the cyclic group of order `c_ell=n`.

Define

`rho_bad(P)
 := max_{ell|N} ord_2(ord(comp_ell(P)))`.

Then protected WP25 becomes

`rho_E=max(rho_2(P),rho_bad(P))`.

Therefore

`len_Z2(C_E^vee)
 = 2 ord_2(3-a_2)
   + sum_{ell|N} ord_2(c_ell)
   - max(rho_2(P),rho_bad(P))`.

## New narrow boundary

All odd-prime universal-norm classes are now exact finite Neron-component data. The remaining structural D1b boundary is

`MISSING_P2_GOOD_ORDINARY_SATURATED_GENERATOR_UNIVERSAL_NORM_ORDER_AT_2`.

The odd component values remain curve-specific arithmetic data, but no theorem-shape uncertainty remains there.

## Claim firewall

WP26 does not prove:

- a value of `rho_2(P)`;
- a formal-group/logarithmic description of `[P]_2`;
- equality of any local norm order with a regulator, height, Bockstein, or analytic factor;
- D1a, D1c, or D2;
- `delta_2(E)=len_Z2 Sha(E/Q)[2^infinity]`;
- `BSD-R2-A1`;
- any MATHCERT certification, novelty, priority, patentability, or commercial claim.
