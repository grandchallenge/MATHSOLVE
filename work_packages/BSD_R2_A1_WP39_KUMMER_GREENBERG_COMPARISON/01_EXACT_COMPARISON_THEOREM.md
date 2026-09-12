# WP39 theorem — exact finite extended/Greenberg-to-Kummer comparison over the protected field `K`

## 1. Protected setup

Let `E/Q` lie in the protected selected `BSD-R2-A1` class, let `K/Q` be the protected WP09 imaginary quadratic field, and put

`T := T_2(E)`.

Protected facts used below:

1. `2` and every prime `ell|N` split in `K`;
2. `E` has good ordinary reduction at the two places of `K` above `2`;
3. WP06 proves `E(K)[2^infinity]=0`;
4. WP38 proves that quadratic base change introduces no index in the rank-one Mordell–Weil free lattice;
5. protected MATHFORGE WP39 at `9de5bac5a18193b9453146dd0db9dee2f34ab06a` admits Nekovář §§9.6.1–9.6.7 literally at `p=2` for the exact comparison used here;
6. protected MATHFORGE Greenberg local control computes the finite good-ordinary Kummer/ordinary local discrepancy literally at `p=2`.

Write

`H_K^ext := H~^1_f(K,T)`

for Nekovář's source-compatible extended compact Selmer cohomology and

`S_K^Kum := S_2(E/K)`

for the compact classical `2`-primary Kummer Selmer module.

## 2. The extended correction vanishes at good ordinary `2`

For each place `w|2`, let

`0 -> T_w^+ -> T -> T_w^- -> 0`

be the good-ordinary filtration.

Nekovář Lemma 9.6.7.6(i), as admitted by protected MATHFORGE WP39, gives

`H^0(K_w,V_w^-)=0`,

where `V=T tensor Q_2`. Since `T_w^-` embeds into `V_w^-`,

`H^0(K_w,T_w^-)=0`.

Protected WP06 gives

`T^{G_K}=T_2(E(K)[2^infinity])=0`.

### Theorem `BSD-A1-WP39-EXTENDED-STRICT-001`

The canonical map in Nekovář Lemma 9.6.3 induces an integral isomorphism

`H_K^ext ~= S_T^str(K)`.

### Proof

Lemma 9.6.3 gives the exact sequence

`0 -> H~^0_f(K,T) -> T^{G_K}`

`   -> direct_sum_{w|2} H^0(K_w,T_w^-)`

`   -> H~^1_f(K,T) -> S_T^str(K) -> 0`.

The middle two terms vanish by the protected facts above. Exactness therefore makes the final arrow an isomorphism. QED.

### Consequence

There is no separate exceptional-zero/degree-zero lattice correction in D2b for the selected good-ordinary `p=2` auxiliary lane. Any remaining difference from the primitive Kummer lattice is the strict-Greenberg-versus-Kummer comparison itself.

## 3. Classical compact Kummer comparison

Protected MATHFORGE WP39 admits Nekovář Lemma 9.6.7.3(i), which gives an exact injection

`0 -> S_T^str(K) -> S_K^Kum`

followed by the explicit local comparison map.

Define the ambient finite module

`R_K :=`

` direct_sum_{w|2} R_w`

` direct_sum direct_sum_{v|N} R_v`,

where

`R_w := H^1(K_w,T_w^-)_tors`

for `w|2`, and

`R_v := H^1(K_v,T)/H^1_ur(K_v,T)`

for bad `v not|2`.

Good primes away from `2N` have zero `2`-primary Tamagawa length and may be omitted from the finite `2`-primary target.

Let

`lambda_K : S_K^Kum -> R_K`

be the induced comparison map and define the **actual global hit subgroup**

`J_K := im(lambda_K)`.

### Theorem `BSD-A1-WP39-COMPARISON-001`

There is a canonical short exact sequence

`0 -> H_K^ext -> S_K^Kum -> J_K -> 0`.

In particular, `J_K` is finite and

`len_Z2 J_K`

is exactly the integral lattice index between the source-compatible Nekovář compact height lattice and the classical compact Kummer Selmer lattice.

### Proof

By Theorem `EXTENDED-STRICT-001`, `H_K^ext` is canonically the strict Greenberg group `S_T^str(K)`. Nekovář Lemma 9.6.7.3(i) identifies this strict group with the kernel of the map from the classical compact Kummer Selmer group to the displayed local comparison target. Replacing the codomain by the actual image `J_K` therefore gives the short exact sequence. Finiteness follows from Lemma 9.6.7.3(ii)-(iv) and the finite good-ordinary local term in (iii). QED.

## 4. Exact size of the ambient local target

Put

`m_2 := ord_2(3-a_2)`.

Protected WP07 gives

`#E_tilde(F_2)=3-a_2`.

The already-admitted Greenberg local theorem identifies the finite Kummer/ordinary discrepancy at each good-ordinary place over `Q_2` with the `2`-primary reduction group. Hence

`len_Z2 R_w = m_2`

for each `w|2`.

Because `2` splits in `K`, there are exactly two such places. Therefore

`sum_{w|2} len_Z2 R_w = 2m_2`.

For an odd bad rational prime `ell|N`, protected WP09 makes `ell` split into two places of `K`, both locally equal to `Q_ell`. Nekovář Lemma 9.6.7.3(ii) gives

`len_Z2 R_v = ord_2(c_ell)`

at each of those two places. Therefore

`sum_{v|ell} len_Z2 R_v = 2 ord_2(c_ell)`.

### Theorem `BSD-A1-WP39-AMBIENT-LENGTH-001`

The finite ambient comparison module has exact length

`len_Z2 R_K
 = 2 ord_2(3-a_2)
   + 2 sum_{ell|N} ord_2(c_ell)`.

Consequently

`0 <= len_Z2 J_K
   <= 2 ord_2(3-a_2)
      + 2 sum_{ell|N} ord_2(c_ell)`.

### Proof

The decomposition defining `R_K` is a direct sum of finite modules. Add the exact local lengths computed above. Since `J_K` is a subgroup of `R_K`, its length is at most the ambient length. QED.

## 5. No hidden global free-lattice factor

Protected WP38 proves

`E(Q) tensor Z_2 ~= E(K) tensor Z_2`.

Thus Theorem `COMPARISON-001` cannot contain any additional power of `2` coming merely from enlargement of the rank-one Mordell–Weil free lattice under quadratic base change.

The finite integer

`j_K := len_Z2 J_K`

is therefore the complete **local/Selmer-complex** index left in D2b.

This statement does not assert that a chosen Heegner point is primitive. A Heegner point may still have a nontrivial index inside the common rank-one Mordell–Weil lattice; that is a separate D2c/D2d normalization datum.

## 6. Refined D2b theorem boundary

The former boundary

`MISSING_P2_NEKOVAR_EXTENDED_TO_PRIMITIVE_KUMMER_LOCAL_INDEX`

is resolved into the exact finite invariant `j_K` and the narrower evaluation problem

`MISSING_P2_KUMMER_GREENBERG_GLOBAL_HIT_SUBGROUP_OVER_K`.

A successor no longer needs to identify or size any ambient local correction factor. It must determine only the image subgroup

`J_K=im(lambda_K)`

or equivalently its length `j_K`.

The natural next representation is Poitou–Tate/global-local incidence: characterize `J_K` as an annihilator or character kernel against the dual rank-one direction, while keeping the Greenberg/Kummer local-condition distinction explicit.

## 7. Claim firewall

WP39 does not prove:

- `J_K=R_K`;
- any specific value of `j_K`;
- global localization surjectivity;
- fixed-`2` height nondegeneracy;
- Heegner-point primitivity;
- an analytic determinant generator at height-one `(2)`;
- exact Disegni interpolation/test-vector valuations;
- equality of a `2`-adic height with the WP00 real regulator;
- the final WP06 quadratic descent;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
