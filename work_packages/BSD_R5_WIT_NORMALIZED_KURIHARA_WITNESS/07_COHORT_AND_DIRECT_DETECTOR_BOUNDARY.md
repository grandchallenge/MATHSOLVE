# BSD R5-WIT — expanded cohort local stratification and direct residual-detector reduction

## 1. Scope and exact inputs

Operation: `BSD-R5-WIT` / `grandchallenge/MATHSOLVE#282`.

Use without reopening:

- protected R5-RECIP local theorem `BSD-R5-RECIP-LOCAL-FORMAL-TORS-002` and Corollary `LOCAL-TEXP-003`;
- protected R5-PRIM finite detection `BSD-R5-PRIM-FINITE-DETECT-005`;
- protected WP60T literal-`2` derivative construction and first-component identity;
- the pinned WP18A/ecdata models already used by the deterministic cohort runner;
- the admitted local-torsion classification already consumed by this package.

For every effective cohort curve below, direct point counting gives `q_2=4`, hence good ordinary reduction with `a_2=-1`. Protected R5-RECIP gives exactly one nonzero formal rational point of order two and

`2^(t_2-1) | q_2=4`,

so `1 <= t_2 <= 3`.

The exact arithmetic checks are replayed by `08_COHORT_LOCAL_T2_CERTIFICATE.py`.

## 2. `61a1`: `t_2=1`

Model:

`[1,0,0,-2,1]`.

The affine two-division polynomial has no root modulo `16`, excluding any second nonformal rational point of order two.

The non-two-torsion fourth-division factor has the unique root class

`x == 4 (mod 16)`.

Any integral lift is congruent to `4` or `20` modulo `32`. The corresponding Weierstrass quadratic discriminant is

`20 (mod 32)`

in both cases. A `2`-adic square of valuation two is `4 (mod 32)`, so this is not a square. Hence there is no rational point of order four.

Together with the protected unique formal order-two point,

`E_61a1(Q_2)[2^infinity] ~= Z/2Z`,

and therefore

`t_2(61a1)=1`.

## 3. `83a1`: `t_2=1`

Model:

`[1,1,1,1,0]`.

The affine two-division polynomial has roots modulo `16`, but no root modulo `32`. Therefore it has no `Z_2`-root and there is no second rational point of order two.

The fourth-division factor has the unique root class

`x == 11 (mod 16)`.

The two lifts modulo `32`, namely `11` and `27`, both give y-discriminant

`12 (mod 32)`.

This has valuation two but quotient `3 mod 8`, hence is not a square in `Q_2`. Thus no rational point of order four exists.

Therefore

`E_83a1(Q_2)[2^infinity] ~= Z/2Z`

and

`t_2(83a1)=1`.

## 4. `201b1`: `t_2=2`

Model:

`[1,0,0,-1,2]`.

The two-division polynomial has no root modulo `16`.

The fourth-division factor has the unique root class

`x == 10 (mod 16)`,

and its derivative is odd there. Hensel therefore gives a unique `Z_2`-root. Both possible residues modulo `32` give y-discriminant

`4 (mod 32)`,

so the discriminant is a `Q_2`-square and an exact-order-four point exists.

The exact-order-eight factor constructed from the standard division-polynomial recurrence has no root modulo `16`. Hence no rational point of order eight exists.

Thus

`E_201b1(Q_2)[2^infinity] ~= Z/4Z`

and

`t_2(201b1)=2`.

## 5. `89a1`: `t_2=3`

Model:

`[1,1,1,-1,0]`.

The two-division polynomial has no root modulo `16`.

The fourth-division factor has a simple root

`x == 15 (mod 16)`

with y-discriminant `4 mod 32`, so an exact-order-four point exists.

For the exact-order-eight factor `G8`, the certificate evaluates at `x=4` and obtains

`v_2(G8(4))=6`, `v_2(G8'(4))=2`.

Since

`v_2(G8(4)) > 2 v_2(G8'(4))`,

the generalized Hensel criterion gives a `Q_2`-root of `G8` congruent to `4 mod 16`. Its y-discriminant is odd and congruent to `1 mod 8`, hence is a `Q_2`-square. Therefore an exact-order-eight point exists.

The protected bound `t_2<=3` then forces

`E_89a1(Q_2)[2^infinity] ~= Z/8Z`

and

`t_2(89a1)=3`.

## 6. Consequence for the expanded Kurihara cohort

The exact green PARI replay on branch head `47f7bfcbdc4e505d6ff72773ca1e13bb8f868190` found no single-prime normalized witness through `ell<=500` on any effective cohort member:

- `53a1`: no hit;
- `61a1`: no hit;
- `83a1`: no hit;
- `89a1`: no hit;
- `201b1`: no hit;
- `203b1`: no hit.

The aggregate output is exactly `DISCOVERY_HITS []`.

The local stratification now separates the meaning of this result.

- `53a1`, `61a1`, `83a1`, `203b1` have `t_2=1`; the normalized Kurihara coordinate is not forced to vanish, but the exact bounded searches found only arithmetic cancellation.
- `79a1` and `201b1` have `t_2=2`.
- `89a1` has `t_2=3`.

For every `t_2>=2` curve, protected R5-RECIP proves `Delta_n^(2)=0 mod 2` at every admitted derivative level. Wider search on that coordinate is therefore mathematically pointless.

No nonexistence theorem is inferred for the `t_2=1` curves from the finite scans.

## 7. Alternative finite residual detector already present in the protected stack

Protected WP60T proves, for every admitted rank-one Euler system `c` and every coefficient level `m`,

`kappa_m(c)_1 = c_Q mod 2^m`.

Specialize to the integral Kato Euler system and `m=1`. Then

`kappa_1^Kato{}_1 = c_Q^Kato mod 2`.

Protected R5-PRIM finite detection requires only one nonzero legitimate finite cyclotomic residual image; finite-layer basis status is not required.

Therefore the following implication is already protected:

`c_Q^Kato mod 2 != 0`

implies

`kappa_1^Kato != 0`,

hence supplies the finite residual witness required to reopen R5-RES.

This detector bypasses the normalized local dual-exponential/Kurihara coordinate completely and therefore is not annihilated merely because `t_2>=2`.

## 8. Current source boundary for the direct detector

The protected source estate admits integral literal-`2` Kato Euler-system classes and literal-`2` cyclotomic explicit reciprocity. It does not presently prove

`c_Q^Kato mod 2 != 0`

on the selected analytic-rank-one anomalous ordinary lane.

This distinction is substantive:

- at analytic rank one, the trivial-character dual-exponential interpolation is zero because `L(E,1)=0`;
- known Perrin-Riou/Beilinson-Kato rank-one nonvanishing comparisons located in the current source screen impose odd-prime hypotheses;
- the protected finite derivative/Fitting audits likewise do not provide a literal-`2` primitive base-class theorem.

Accordingly the direct route reduces R5-WIT to the narrower theorem/evidence boundary

`MISSING_P2_BASE_KATO_CLASS_MOD2_NONVANISHING_ON_SELECTED_RANK_ONE_LANE`.

A valid discharge is any source-admitted literal-`2` theorem or exact legitimate computation proving `c_Q^Kato mod 2 !=0` for a selected instance, or another finite Kato/Kolyvagin component nonzero modulo two.

## 9. Claim firewall

This record does not establish R5-RES, R5-PRIM, D2d, BSD-R2-A1, novelty/priority, public certification, or MATHCERT certification. The negative finite Kurihara scans are evidence only and are not promoted to a global nonvanishing or nonexistence theorem.
