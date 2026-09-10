# WP21 refined D1 construction gate

## Protected result used

WP21 proves

`0 -> C_E^vee -> (X_infty)_Gamma -> X_E -> 0`,

where

`X_infty := Sel_{2^infinity}^{Kum}(E/Q_infty)^vee`,

`X_E := Sel_{2^infinity}^{Kum}(E/Q)^vee`,

and

`C_E := im(loc_Q) intersect K_loc`.

The ambient placewise local control kernels are exactly

`K_v = H^1(Gamma_v,E(Q_{infty,w}))[2^infinity]`.

Protected WP20 proves that once an arithmetic square/perfect determinant realization specializes to the desired rank-one module, its first derivative splits into the first-Fitting factor and a Bockstein factor.

## D1 is no longer one theorem

The original D1 boundary

`MISSING_P2_PRIMITIVE_RANK1_DETERMINANT_REALIZATION`

is now replaced by three narrower obligations.

### D1a — primitive cyclotomic perfect determinant realization

Construct a literal `p=2` perfect Selmer complex or equivalent finite projective presentation over

`Lambda := Z_2[[Gamma]]`

for the **primitive classical Kummer** cyclotomic structure, with augmentation specialization compatible with the WP21 sequence.

Sufficient output would be either:

1. a perfect complex of amplitude suitable for a determinant line, together with an exact identification of its specialized rank-one cohomology with `(X_infty)_Gamma` and hence the WP21 quotient to `X_E`; or
2. a square `Lambda`-presentation `A(T)` of the relevant module/derived object to which WP20 applies directly.

The construction must not substitute the Greenberg ordinary condition at `2` or delete bad-prime Kummer conditions unless the exact comparison complex is carried along.

Boundary:

`MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`.

### D1b — primitive local control-defect evaluation

Determine the exact contribution of

`C_E = im(loc_Q) intersect K_loc`

to the base first-Fitting ideal.

At a minimum, prove whether `C_E` is finite and determine its `Z_2` length/Fitting ideal. A useful theorem may compute the ambient local groups first and then prove which part lies in the global localization image.

The difficult places are not to be guessed away:

- at `2`, good ordinary reduction does not imply residual distinguishedness, and WP06/WP07 forbid silently replacing Kummer by Greenberg;
- at bad semistable `ell|N`, both WP13 regimes remain in scope, including even Tamagawa/residual-conductor drop;
- the real place has zero restriction kernel in the cyclotomic tower and requires no further defect.

Boundary:

`MISSING_P2_PRIMITIVE_LOCAL_CONTROL_DEFECT_EVALUATION`.

### D1c — analytic determinant generator at the height-one prime `(2)`

Once D1a supplies a determinant line/object, identify the arithmetic analytic/Euler-system element in that determinant and determine its integral divisor at the height-one prime containing `2`.

Protected Kato WP17B supplies genuine ordinary control away from `(2)`, but its all-height-one integral upgrade assumes `p!=2`. Therefore away-from-`(2)` information is insufficient.

Boundary:

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

## D2 remains independent

Even after D1a–D1c, protected WP20 still requires the exact Bockstein-to-WP00 comparison:

`ord_2(coeff_T Theta_E)-v_2(B_E)=delta_2(E)`.

Boundary:

`MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`.

The protected BKS audit validates this architecture but is globally odd-prime. The protected Perrin–Riou source-family audit supplies no source basis to import the historical rank-one formula at `p=2`.

## Preferred order from here

The smallest construction order is:

1. D1b local algebra/control, because WP21 has made its exact target explicit and some local terms may be computable without a main conjecture;
2. D1a perfect/determinant realization, carrying the D1b complex rather than assuming it vanishes;
3. D1c height-one `(2)` analytic generator/control;
4. D2 exact Bockstein/WP00 normalization.

If D1b produces a nonzero defect, it is not a failure of the route. Its exact determinant/Fitting contribution must be incorporated into D1a/D2.

## Claim firewall

This gate is a theorem-construction decomposition. It does not prove any of D1a–D1c or D2, and it does not alter `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.