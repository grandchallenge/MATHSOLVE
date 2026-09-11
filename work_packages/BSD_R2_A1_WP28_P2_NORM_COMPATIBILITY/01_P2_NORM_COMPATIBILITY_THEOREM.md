# WP28 theorem — concrete reduction/formal universal-norm coordinates at `2`

## 1. Setup and protected source interface

Let `E/Q` lie in the protected selected `BSD-R2-A1` class and let

`L := Q_{infty,2}`

be the completion at `2` of the cyclotomic `Z_2`-extension. Write

`Gamma_2 := Gal(L/Q_2) ~= Z_2`

and let

`L_n/Q_2`

be the finite layer of degree `2^n`.

Protected WP25 defines

`N_2^infinity
 := intersection_n N_{L_n/Q_2} E(L_n)`

and

`U_2 := E(Q_2)/N_2^infinity`.

It proves canonically

`U_2 ~= K_2^vee`.

Protected WP23 gives

`#U_2=#K_2=(3-a_2)^2`.

Protected WP07 gives

`#E_tilde(F_2)=3-a_2 in {2,4}`.

Protected MATHFORGE commit

`e5c49ee60ba300cff8026ddf65059c3049ab1226`

admits Tan's literal-`p=2`, totally ramified, good-ordinary universal-norm filtration. The exact source interfaces used below are:

1. the reduction/formal-group sequence induces the universal-norm sequence;
2. for a totally ramified `Z_p`-extension with good ordinary reduction, the formal universal-norm quotient injects into the full universal-norm quotient;
3. the quotient map is induced by the literal reduction map;
4. the corresponding cohomology and norm sequences are exact Pontryagin duals;
5. these statements are literal at `p=2`.

No new external theorem premise is used.

## 2. Formal universal norms

Let

`Ehat(m_{Q_2})`

be the formal subgroup of `E(Q_2)`, where

`m_{Q_2}=2 Z_2`.

For each finite layer put

`N_{2,n}^form
 := N_{L_n/Q_2} Ehat(m_{L_n})
    subset Ehat(m_{Q_2})`.

Define the formal universal-norm subgroup

`N_2^form
 := intersection_n N_{2,n}^form`

and the formal universal-norm quotient

`F_2^norm
 := Ehat(m_{Q_2})/N_2^form`.

Tan's protected theorem supplies an injective map

`iota_2:F_2^norm -> U_2`

induced by the inclusion of the formal subgroup into `E(Q_2)`.

## 3. The reduction universal-norm quotient

The local cyclotomic extension `L/Q_2` is totally ramified. Therefore every `L_n` has residue field `F_2`.

The reduction exact sequence at each layer is

`0 -> Ehat(m_{L_n})
   -> E(L_n)
   -> E_tilde(F_2)
   -> 0`.

On the common residue group, the norm from `L_n/Q_2` is the sum over the `2^n` Galois conjugates. Because the residue-field action is trivial, this norm is multiplication by `2^n`.

Define

`N_2^red
 := intersection_n 2^n E_tilde(F_2)`.

### Lemma `BSD-A1-WP28-RED-NORM-001`

One has

`N_2^red=0`.

Consequently the reduction universal-norm quotient is canonically

`E_tilde(F_2)/N_2^red
 ~= E_tilde(F_2)`.

### Proof

Protected WP07 gives

`#E_tilde(F_2) in {2,4}`.

Thus `E_tilde(F_2)` is a finite `2`-group. If its exponent is `2^e`, then

`2^n E_tilde(F_2)=0`

for all `n>=e`. Hence the intersection over all `n` is zero. QED.

## 4. Exact concrete norm filtration

Tan's protected good-ordinary norm theorem gives the exact sequence induced by the formal/reduction sequence. With Lemma `BSD-A1-WP28-RED-NORM-001`, it specializes as follows.

### Theorem `BSD-A1-WP28-NORM-FILTRATION-001`

There is a canonical short exact sequence

`0 -> F_2^norm
   --iota_2--> U_2
   --red_2--> E_tilde(F_2)
   -> 0`.

The map `red_2` is induced by literal reduction of local points.

Moreover

`#F_2^norm=3-a_2`.

### Proof

The exact sequence and injectivity of `iota_2` are exactly the protected Tan good-ordinary universal-norm interface after specializing to

`K=Q_2`, `L=Q_{infty,2}`, `p=2`.

By Lemma `BSD-A1-WP28-RED-NORM-001`, the right-hand reduction quotient is the full finite group `E_tilde(F_2)`.

Protected WP23/WP25 give

`#U_2=(3-a_2)^2`,

and protected WP07 gives

`#E_tilde(F_2)=3-a_2`.

Taking orders in the finite short exact sequence yields

`#F_2^norm
 = #U_2/#E_tilde(F_2)
 = 3-a_2`. QED.

### Remark on WP27

Protected WP27 gives another exact two-step filtration of the same middle group `U_2`, obtained by dualizing Greenberg's control-kernel factorization. WP28 does not identify the individual named WP27 maps with `iota_2` and `red_2` merely from equality of the end-term orders. The present theorem is an independent concrete filtration supplied by Tan's protected map-level universal-norm theorem.

## 5. Literal reduction coordinate of the saturated generator

Let

`P in E(Q)`

be a saturated generator of the rank-one free quotient used in protected WP24-WP27.

View `P` in `E(Q_2)`. Since `E` has good reduction at `2`, the Neron reduction map is defined on every point of `E(Q_2)`. Let

`Pbar_2 := red(P) in E_tilde(F_2)`.

Protected WP25 defines

`x_2(P):=[P]_2 in U_2`.

Because the quotient map in Theorem `BSD-A1-WP28-NORM-FILTRATION-001` is induced by literal reduction,

`red_2(x_2(P))=Pbar_2`.

Define

`r_red(P)
 := ord_2(ord(Pbar_2))`.

The convention is `ord(0)=1`, so `r_red(P)=0` if `P` reduces to the identity.

### Lemma `BSD-A1-WP28-RED-COORD-001`

The quotient class of `x_2(P)` in the concrete filtration has order

`2^{r_red(P)}`.

In particular,

`0 <= r_red(P) <= ord_2(3-a_2)`.

### Proof

The quotient class is literally `Pbar_2`. By definition its order has `2`-adic valuation `r_red(P)`. Since `Pbar_2` lies in a group of order `3-a_2`, the bound follows. QED.

## 6. The remaining formal class

By definition of `r_red(P)`,

`2^{r_red(P)} Pbar_2=0`.

Therefore

`2^{r_red(P)} x_2(P)`

lies in

`ker(red_2)=im(iota_2)`.

Since `iota_2` is injective, there is a unique element

`z_form(P) in F_2^norm`

such that

`iota_2(z_form(P))
 = 2^{r_red(P)}x_2(P)`.

Define

`s_form(P)
 := ord_2(ord(z_form(P)))`.

### Theorem `BSD-A1-WP28-P2-ORDER-001`

One has exactly

`rho_2(P)=r_red(P)+s_form(P)`.

Moreover

`0 <= s_form(P) <= ord_2(3-a_2)`.

### Proof

Write

`ord(x_2(P))=2^t`.

The quotient image of `x_2(P)` has order `2^{r_red(P)}`. Thus `r_red(P)` is the least nonnegative integer `r` such that

`2^r x_2(P)`

lies in the formal subgroup `im(iota_2)`.

Its unique formal preimage at that first entrance is `z_form(P)`, of order `2^{s_form(P)}`.

Therefore

`2^{r_red(P)+s_form(P)}x_2(P)=0`,

so

`t <= r_red(P)+s_form(P)`.

Conversely, if

`2^m x_2(P)=0`,

then its quotient is zero, forcing

`m>=r_red(P)`.

Write

`m=r_red(P)+u`.

Injectivity of `iota_2` then gives

`2^u z_form(P)=0`,

so

`u>=s_form(P)`.

Hence

`m>=r_red(P)+s_form(P)`

for every annihilating exponent. Thus

`t=r_red(P)+s_form(P)`.

Protected WP25 defines

`rho_2(P)=ord_2(ord(x_2(P)))=t`.

The bound on `s_form(P)` follows from

`#F_2^norm=3-a_2`. QED.

## 7. Complete D1b representation after WP28

Protected WP26 defines the exact odd-prime arithmetic observable

`rho_bad(P)
 := max_{ell|N} ord_2(ord(comp_ell(P)))`.

It proves

`rho_E=max(rho_2(P),rho_bad(P))`.

Substitute Theorem `BSD-A1-WP28-P2-ORDER-001`.

### Corollary `BSD-A1-WP28-GLOBAL-001`

One has

`rho_E
 = max(r_red(P)+s_form(P), rho_bad(P))`.

Consequently protected WP24's exact specialization-defect formula becomes

`len_Z2(C_E^vee)
 = 2 ord_2(3-a_2)
   + sum_{ell|N} ord_2(c_ell)
   - max(r_red(P)+s_form(P),rho_bad(P))`.

Every term except `s_form(P)` is now finite arithmetic data directly determined by:

- `a_2`;
- the Tamagawa numbers;
- the Neron components of `P` at odd bad primes;
- the literal reduction of `P` modulo `2`.

The only unresolved local structural term in D1b is the order of the reduction-killed generator class in the formal universal-norm quotient.

## 8. Tan's ambient formal quotient and what remains unknown

The protected Tan source also gives, in dimension one, an abstract ambient description of the formal universal-norm quotient in terms of a Frobenius twist scalar `u`:

`F_2^norm ~= Gamma_2/(1-u)Gamma_2`

under Tan's conventions.

WP28 records this only as an available protected source interface. It does not identify Tan's scalar `u` with the protected WP07 unit root `alpha` or `alpha^(-1)`, and it does not identify the element `z_form(P)` with an explicit coordinate under that abstract isomorphism.

Knowing the order of the ambient formal quotient does not determine the order of `z_form(P)`.

## 9. Refined boundary

The former boundary

`MISSING_P2_SATURATED_GENERATOR_POSITION_IN_GOOD_ORDINARY_CONTROL_EXTENSION`

is replaced by the strictly narrower boundary

`MISSING_P2_FORMAL_UNIVERSAL_NORM_ORDER_OF_REDUCTION_KILLED_GENERATOR`.

A successor must evaluate

`s_form(P)=ord_2(ord(z_form(P)))`

or identify it exactly with another protected arithmetic invariant without losing a power of `2`.

A formal logarithm, explicit norm-coordinate theorem, or a rigorously normalized comparison with the WP20 Bockstein factor may be relevant, but none is presently asserted.

## 10. Claim firewall

WP28 does not prove:

- a value of `s_form(P)` or `rho_2(P)`;
- a splitting of the concrete universal-norm sequence;
- a canonical equality between WP28's concrete coordinates and WP27's abstract coordinate names;
- an element-level formula for `z_form(P)` under Tan's `Gamma_2/(1-u)Gamma_2` description;
- `u=alpha` or `u=alpha^(-1)`;
- a formal logarithm, p-adic height, regulator, or Bockstein formula;
- D1a `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
- D1c `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2 `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`;
- `delta_2(E)=len_Z2 Sha(E/Q)[2^infinity]`;
- `BSD-R2-A1`;
- any MATHCERT certification, novelty, priority, patentability, or commercial claim.
