# WP30 theorem — exact reconciliation of the formal-norm twist and ordinary unit root

## 1. Protected inputs

Let `E/Q` lie in the protected selected BSD-R2-A1 branch.

Protected WP07 defines `alpha in Z_2^x` as the unique unit root of

`X^2-a_2 X+2`

and proves

`ord_2(1-alpha^(-1))=ord_2(3-a_2)`.

For the normalization-specific local multiplier

`e_2(E):=(1-alpha^(-1))^2`,

WP07 proves

`ord_2(e_2(E))=2 ord_2(3-a_2)`.

Protected WP29 gives an isomorphism

`F_2^norm ~= Gamma_2/(1-u)Gamma_2`

for the Hall/Tan twist scalar `u`, and defines the canonical congruence depth `tau_form(P)` of the selected formal class.

Protected MATHFORGE commit

`5b07785c9ca96ec0c2003bbe3ada46c807e50882`

source-qualifies, literally at `p=2`, the shared Mazur/Tan Frobenius convention and proves in the one-dimensional ordinary elliptic specialization that

`u=alpha`.

## 2. Exact denominator reconciliation

### Theorem `BSD-A1-WP30-UNITROOT-001`

Under the protected conventions,

`u=alpha`.

Consequently

`(1-u)Z_2=(1-alpha)Z_2=(1-alpha^(-1))Z_2`.

The same equalities hold after multiplication on the free rank-one `Z_2`-module `Gamma_2`:

`(1-u)Gamma_2
 = (1-alpha)Gamma_2
 = (1-alpha^(-1))Gamma_2`.

### Proof

The first equality is the protected source reconciliation.

Because `alpha` is a unit,

`1-alpha^(-1)
 = (alpha-1)/alpha
 = -alpha^(-1)(1-alpha)`.

The multiplier `-alpha^(-1)` is a unit in `Z_2`. Therefore `(1-alpha)` and `(1-alpha^(-1))` generate the same principal ideal. Multiplying that ideal equality through the free rank-one module `Gamma_2` gives the submodule equality. QED.

## 3. Formal universal-norm quotient in WP07 normalization

### Corollary `BSD-A1-WP30-NORM-QUOTIENT-001`

There are exact quotient identifications

`F_2^norm
 ~= Gamma_2/(1-alpha)Gamma_2
 = Gamma_2/(1-alpha^(-1))Gamma_2`.

Here the final equality is literal equality of quotient groups because the denominator submodules are equal.

### Proof

Protected WP29 gives

`F_2^norm ~= Gamma_2/(1-u)Gamma_2`.

Apply Theorem `BSD-A1-WP30-UNITROOT-001`. QED.

## 4. The protected selected element

Let

`theta_form(P)`

be the protected WP29 toroidal class corresponding to the reduction-killed formal point `z_form(P)`.

### Corollary `BSD-A1-WP30-TAU-CONCORDANCE-001`

The protected invariant `tau_form(P)` is exactly the truncated congruence depth of `theta_form(P)` relative to the WP07 unit-root modulus

`(1-alpha^(-1))Gamma_2`.

Equivalently, after choosing any topological generator of `Gamma_2` and a scalar representative `t_form(P)`, one may compute

`tau_form(P)
 = min(
     ord_2(1-alpha^(-1)),
     ord_2(t_form(P))
   )`.

This is the same invariant already proved canonical in WP29.

### Proof

WP29 defines `tau_form(P)` using the quotient by `(1-u)Gamma_2`. Theorem `BSD-A1-WP30-UNITROOT-001` proves this denominator is exactly `(1-alpha^(-1))Gamma_2`. No quotient map, class, scalar lift, or element order changes. Substitute the equal denominator. QED.

## 5. Exact local-factor ideal concordance

### Theorem `BSD-A1-WP30-LOCAL-FACTOR-IDEAL-001`

For the protected WP07 normalization

`e_2(E)=(1-alpha^(-1))^2`,

one has exactly

`(1-u)^2 Z_2
 = (1-alpha)^2 Z_2
 = (1-alpha^(-1))^2 Z_2
 = e_2(E) Z_2`.

### Proof

Square the principal-ideal equalities of Theorem `BSD-A1-WP30-UNITROOT-001` and apply the definition of `e_2(E)`. QED.

### Important limitation

This is an equality of local principal ideals. It does not assert that a future arithmetic determinant contains `e_2(E)`, that a control defect cancels it, or that its generator equals a Bockstein/regulator scalar.

## 6. Compatibility with protected WP29 formula

Put

`m_2:=ord_2(3-a_2)`.

Protected WP07 and WP30 now give

`m_2=ord_2(1-alpha^(-1))=ord_2(1-u)`.

Protected WP29 therefore remains exactly

`rho_2(P)
 = r_red(P)+m_2-tau_form(P)`,

but the modulus defining `tau_form(P)` is now source-bound to the same ordinary unit-root convention as WP07.

Likewise

`rho_E
 = max(
     r_red(P)+m_2-tau_form(P),
     rho_bad(P)
   )`

and the protected WP24 control-defect formula remains

`len_Z2(C_E^vee)
 = 2m_2
   + sum_{ell|N}ord_2(c_ell)
   - rho_E`.

WP30 changes no value in these formulas. It removes only the auxiliary normalization ambiguity in the formal denominator.

## 7. What WP30 closes

WP30 closes the convention question

`MISSING_P2_TWIST_MATRIX_TO_UNIT_ROOT_NORMALIZATION`.

The active local element boundary remains

`MISSING_P2_TOROIDAL_FORMAL_COORDINATE_CONGRUENCE_DEPTH`.

The result also supplies a reusable exact local-normalization clause for any future D1c or D2 theorem: the Hall/Tan formal modulus and one WP07 ordinary interpolation factor are the same principal ideal.

## 8. Claim firewall

WP30 does not prove:

- a value of `tau_form(P)`;
- a canonical scalar representative of `theta_form(P)`;
- a formal-logarithm formula for that class;
- a p-adic-height, regulator, or WP20 Bockstein identity;
- that an arithmetic determinant contains or cancels `e_2(E)`;
- D1a `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
- D1c `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2 `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`;
- `BSD-R2-A1`;
- any MATHCERT certification, novelty, priority, patentability, or commercial claim.
