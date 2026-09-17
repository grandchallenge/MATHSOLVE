# BSD R5-WIT — selected-lane local `t_2` stratification

## 1. Protected inputs

Use:

- protected R5-RECIP, which proves that every selected good-ordinary local curve has exactly one nonzero formal rational point of order two and that `1 <= t_2 <= 3` once combined with the bounded good-ordinary local-torsion classification;
- the protected Ozeki–Yoshida provider interface at `grandchallenge/MATHFORGE@2a112e28026d33062ea314c55e69c157bf9ae863`;
- the protected `79a1` ecdata input at `grandchallenge/MATHFORGE@aeb6588785e70bb7477cdcf44b018c150674c8e4`.

The admitted external record for `79a1` is:

- conductor `N=79`;
- minimal model `[1,1,1,-2,0]`;
- rank one;
- rational torsion order one.

All local deductions below are recomputed here.

## 2. `79a1` lies in the selected hard filter

The conductor `79` is odd and squarefree, hence the curve is semistable and has good reduction at `2`.

Counting the reduced model over `F_2` gives four points, so

`q_2=#E(F_2)=4`, `a_2=3-q_2=-1`.

Thus reduction at `2` is ordinary.

The protected input records trivial rational torsion. Hence `E(Q)[2]=0`. A reducible two-dimensional representation over `F_2` has an invariant line, whose unique nonzero vector is fixed; therefore the global residual module `E[2]` is irreducible. The protected BSD-001 residual theorem then supplies the selected residual image used elsewhere in the campaign.

The pinned rank-one record supplies the selected rank-one qualification. Thus `79a1` is a valid selected-lane instance for the present local test.

## 3. Exact local two-primary torsion

For the generalized Weierstrass model

`y^2 + xy + y = x^3 + x^2 - 2x`,

the standard invariants are

`(b2,b4,b6,b8)=(5,-3,1,-1)`

and the minimal discriminant is

`Delta=79`.

Since `79 == 7 mod 8`, it is not a square in `Q_2`. The cubic two-division algebra therefore does not split completely over `Q_2`. Protected R5-RECIP already supplies one nonzero `Q_2`-rational formal point of order two; consequently this is the unique nonzero local point of order two.

The non-two-torsion factor of the fourth division polynomial is

`F4(x)=2x^6+5x^5-15x^4+10x^3-10x^2-2x+2`.

At `x=9`,

`v_2(F4(9))=9`

while

`F4'(9)=831121`

is odd. Hensel's lemma therefore gives a unique `x_4 in Z_2` with

`F4(x_4)=0`, `x_4 == 9 mod 512`.

For fixed `x`, the equation is quadratic in `y`; its discriminant is

`D(x)=(x+1)^2+4(x^3+x^2-2x)`.

Because `x_4 == 9 mod 16`, direct reduction gives

`D(x_4) == 4 mod 32`.

Hence `v_2(D(x_4))=2` and `D(x_4)/4 == 1 mod 8`, so `D(x_4)` is a square in `Q_2`. Therefore the fourth-division root lifts to a `Q_2`-rational point of exact order four.

To exclude order eight, use the standard division-polynomial recurrence. After removing the lower-order factors `psi_2` and the non-two-torsion fourth-division factor, every point of exact order eight has integral `x` satisfying

`F8(x)=0`,

where

`F8(x) = 2x^24 + 20x^23 - 179x^22 + 286x^21 - 2233x^20 - 12628x^19 - 20258x^18 + 2516x^17 + 129778x^16 - 53740x^15 - 402579x^14 + 203910x^13 + 737583x^12 - 733572x^11 - 265664x^10 + 793848x^9 - 631968x^8 + 405604x^7 - 278299x^6 + 160286x^5 - 63385x^4 + 16188x^3 - 2570x^2 + 228x - 8`.

Exact enumeration gives

`F8(x) != 0 mod 16`

for every `x mod 16`. Hence `F8` has no root in `Z_2`, and there is no `Q_2`-rational point of exact order eight.

The admitted good-ordinary classification leaves, in the presence of exactly one nonzero order-two point and an order-four point, only cyclic `Z/4Z` or `Z/8Z`. The preceding order-eight exclusion therefore proves:

### Theorem `BSD-R5-WIT-T2-79A1-001`

`E_79a1(Q_2)[2^infinity] ~= Z/4Z`,

so

`t_2(79a1)=2`.

## 4. Selected-lane stratification

The protected control theorem in this package proves

`t_2(53a1)=t_2(203b1)=1`,

whereas `T2-79A1-001` proves

`t_2(79a1)=2`.

Therefore the BSD-001 selected hard filter does **not** force a single local exponent. In particular it does not force `t_2=1`.

### Corollary `BSD-R5-WIT-T2-STRATIFY-002`

The selected class contains at least two genuine local strata:

- a `t_2=1` stratum, represented by `53a1` and `203b1`;
- a `t_2=2` stratum, represented by `79a1`.

## 5. Consequence for the normalized Kurihara route

Protected R5-RECIP proves

`Delta_n^(2)=2^t_2 * delta_tilde_n`

and proves that if `t_2>=2`, then

`Delta_n^(2)=0 mod 2`

for every admitted finite derivative level.

Hence on `79a1`:

### Corollary `BSD-R5-WIT-79A1-WITNESS-OBSTRUCTION-003`

`Delta_n^(2)=0 mod 2`

for every admitted finite derivative index `n`.

Thus a normalized Kurihara mod-2 witness cannot establish residual Kato/Kolyvagin nonvanishing uniformly on the full selected class.

This is an obstruction to this witness, not a vanishing theorem for the residual Kato/Kolyvagin class. No inference about the global residual class is authorized on `79a1` from the vanishing of `Delta_n^(2)`.

## 6. Refined frontier

R5-WIT is therefore intrinsically stratified:

1. on `t_2=1`, the active direct obligation remains to exhibit a legitimate finite derivative level with `Delta_n^(2) != 0 mod 2`;
2. on `t_2>=2`, the normalized local-regulator witness is annihilated and a different protected residual witness is required.

The corresponding exact theorem boundaries are

`MISSING_P2_T2_EQ_1_NORMALIZED_FINITE_KURIHARA_NONVANISHING_WITNESS`

and

`MISSING_P2_T2_GE_2_ALTERNATIVE_RESIDUAL_KATO_KOLYVAGIN_WITNESS`.

Neither is resolved by the present local stratification theorem.

## 7. Claim firewall

This theorem does not establish residual Kato/Kolyvagin nonvanishing, R5-RES, R5-PRIM, D2d, BSD-R2-A1, novelty/priority, public certification, or MATHCERT certification.
