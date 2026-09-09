# WP20 arithmetic reduction gate

## Protected starting point

Protected WP19 gives the exact selected target

`delta_2(E)=v_2(Fitt^1_{Z_2}(X_E))`,

where

`X_E := Sel_{2^infinity}^{Kum}(E/Q)^vee`.

WP20 proves that any genuine rank-one determinant deformation specializing to `X_E` has first derivative equal, in ideal valuation, to the first-Fitting contribution plus a Bockstein contribution.

This permits the missing reciprocity theorem to be split without changing the selected target.

## Arithmetic determinant datum

An admissible arithmetic determinant datum for a selected curve `E` consists of:

1. a DVR coefficient ring exactly `Z_2`, or a finite flat extension with an explicitly controlled norm back to `Z_2`;
2. a one-parameter complete local ring `S` with augmentation parameter `T` and `S/(T)=Z_2`;
3. a perfect two-term or stably two-term arithmetic complex whose square presentation is represented by `A_E(T)`;
4. a specialization identification

   `coker A_E(0) ~= X_E`

   or an exact finite-kernel/cokernel comparison whose complete `2`-adic defect is recorded;
5. a determinant element

   `Theta_E(T)=det A_E(T)`

   under a specified determinant-line trivialization;
6. proof that the local conditions in the specialization are the WP16B primitive Kummer conditions, or exact comparison formulas at every place.

No item in this list is supplied merely by the algebra theorem.

## Exact WP20 factorization

For such a datum, define the intrinsic rank-one Bockstein ideal

`B_E`

from

`ker A_E(0) -> X_E/Tor(X_E)`.

Then WP20 gives

`(coeff_T Theta_E(T))
 = Fitt^1_{Z_2}(X_E) * B_E`.

If the coefficient is nonzero,

`ord_2(coeff_T Theta_E(T))
 = v_2(Fitt^1_{Z_2}(X_E)) + v_2(B_E)`.

Thus the selected target follows from the single normalized derivative identity

`ord_2(coeff_T Theta_E(T)) - v_2(B_E) = delta_2(E)`.

This identity is equivalent to the WP19 target once the arithmetic determinant datum is established.

## Obligation D1 — primitive rank-one determinant realization

The first missing theorem is now:

`BSD-R2-A1-P2-PRIMITIVE-RANK1-DETERMINANT-REALIZATION`.

It must construct an arithmetic determinant datum with specialization exactly equal, or exactly comparable, to the protected primitive module `X_E`.

Mandatory clauses:

- literal `p=2`;
- good ordinary at `2`;
- selected surjective residual `S3` branch;
- primitive Kummer condition at `2`;
- primitive Kummer conditions at bad semistable primes;
- both WP13 Tamagawa regimes;
- no inversion of `2`;
- no `Fitt^0` substitution for the rank-one base specialization;
- exact treatment of any finite specialization kernel/cokernel.

The determinant may arise from a Selmer complex, Kato zeta element, Mazur-Tate element, Euler-system determinant, or another construction, but its exact integral relation to the specialization module must be proved.

## Obligation D2 — Bockstein/WP00 normalization

The second missing theorem is:

`BSD-R2-A1-P2-BOCKSTEIN-WP00-NORMALIZATION`.

For the determinant datum produced by D1, it must prove

`ord_2(coeff_T Theta_E(T)) - v_2(B_E)
 = ord_2(L'(E,1)/(Omega_E Reg_E))
   - sum_{ell|N} ord_2(c_ell)`.

Every correction entering either side must be explicit. Depending on the determinant construction this includes, as applicable:

- unit-root or ordinary interpolation factors at `2`;
- Kummer/Greenberg comparison at `2`;
- primitive/imprimitive Euler factors;
- Tamagawa factors at every bad prime;
- residual-conductor-drop factors from WP13 regime B;
- period and Manin factors;
- p-adic height/Bockstein regulator factors;
- comparison of any p-adic height with the WP00 Neron-Tate regulator;
- isogeny or lattice indices;
- normalization of the augmentation/derivative parameter.

No power of `2` may be absorbed into an unspecified unit.

## Conditional closure theorem `BSD-A1-WP20-CLOSE-001`

Assume D1 and D2 hold uniformly over the protected selected class.

Then `BSD-R2-A1` holds uniformly.

### Proof

D1 supplies the exact determinant datum. WP20 gives

`ord_2(coeff_T Theta_E)
 = v_2(Fitt^1(X_E)) + v_2(B_E)`.

D2 gives

`ord_2(coeff_T Theta_E)-v_2(B_E)=delta_2(E)`.

Subtracting the Bockstein valuation in the WP20 identity yields

`v_2(Fitt^1(X_E))=delta_2(E)`.

Protected WP19 identifies this equality with `BSD-R2-A1`. QED.

## Why this is a real reduction

WP19 removed the choice of a rank-one generator from the algebraic target. WP20 now removes another ambiguity: it shows exactly where a regulator-like factor must live in any determinant proof.

A rank-one determinant derivative cannot be compared directly to `Fitt^1(X_E)` without accounting for the Bockstein scalar. The scalar is not an optional normalization convention; it is the first-order motion of the free kernel into the free cokernel.

This explains why positive-rank determinant and Mazur-Tate formulas naturally require regulator/Bockstein terms and gives a precise place to audit every `2`-power.

## Current boundaries

The former single boundary

`MISSING_P2_RANK1_PRIMITIVE_FIRST_FITTING_RECIPROCITY_THEOREM`

is replaced by the strictly more resolved pair

`MISSING_P2_PRIMITIVE_RANK1_DETERMINANT_REALIZATION`

and

`MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`.

Neither is a source-nonexistence claim.

## Next source/construction discipline

Do not resume broad literature screening.

The next source query should ask only whether an existing literal-`p=2` theorem supplies D1, D2, or a separately auditable part of either obligation.

A theorem that only proves order of vanishing, only works for odd `p`, assumes Tamagawa prime to `p`, works after inverting `2`, or leaves the Bockstein/regulator factor unspecified does not close the corresponding obligation.
