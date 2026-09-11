# BSD-001 WP35 frontier

## Candidate predecessor identities

WP35 is authored from protected MATHSOLVE

`9708080c76eb118232d2afb497e2c4803498224d`

and protected MATHFORGE source authority

`4cf5f8838541fb15296619ead3aaaf298198fe65`.

No WP35 conclusion is protected until exact-head review, affected CI, protected merge, and protected-main readback complete.

## Candidate WP35 result

Let

`X_infty := Sel_{2^infinity}^{Kum}(E/Q_infty)^vee`

and

`Lambda=Z_2[[Gamma]] ~= Z_2[[T]]`.

Greenberg's protected WP35 source interface gives:

- `X_infty` is finitely generated torsion over `Lambda`;
- `X_infty` has no nonzero finite `Lambda`-submodule.

Since `Lambda` is regular local of dimension two, the absence of finite submodules forces depth one. Auslander-Buchsbaum therefore gives

`pd_Lambda X_infty=1`.

Hence there is a square finite-free presentation

`0 -> Lambda^r --A(T)--> Lambda^r -> X_infty -> 0`.

At augmentation,

`M_0:=coker A(0) ~= (X_infty)_Gamma`.

Protected WP21 gives

`0 -> C_E^vee -> M_0 -> X_E -> 0`.

The finite kernel is exactly the torsion correction:

`0 -> C_E^vee -> Tor(M_0) -> T_E -> 0`.

Therefore

`Fitt^1(M_0)
 = Fitt^0(C_E^vee) Fitt^1(X_E)`.

Protected WP20 then gives

`(coeff_T det A(T)) Z_2
 = Fitt^0(C_E^vee)
   Fitt^1(X_E)
   B_A`.

This closes

`MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`

in the exact square-presentation plus specialization-defect-accounting sense, subject to candidate review and protection.

## What remains

The decisive global determinant frontier is now no longer existence of a primitive cyclotomic square presentation.

Two independent determinant-side obligations remain:

1. D1c `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`:
   identify an integral analytic/Euler-system determinant generator with the algebraic presentation determinant, including the height-one prime `(2)`.
2. D2 `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`:
   identify WP20's intrinsic Bockstein ideal with the protected rank-one regulator/period normalization.

The local lane remains:

- WP31 `MISSING_P2_FINITE_TWISTED_RECIPROCITY_EXPONENT`.

This local datum contributes through the already protected formula for `len C_E^vee`; it is not an additional cyclotomic specialization defect.

## Recommended successor

On the determinant side, proceed to D1c without reopening D1a. The source query must be exact: find a literal-`p=2` integral analytic/Euler-system determinant theorem for the selected non-CM ordinary two-dimensional representation that controls the height-one prime `(2)`, or construct the missing `(2)` exponent directly.

Do not substitute Kato's away-from-`(2)` divisibility for this obligation: the protected WP17B audit already records the odd-prime hypothesis on Kato's all-height-one upgrade.

In parallel, the WP31 local exponent may be attacked independently by an exact degree-two/degree-four local reciprocity calculation.

`BSD-R2-A1` remains `SELECTED_RESEARCH_TARGET_UNPROVED`; MATHCERT remains the sole certification authority.