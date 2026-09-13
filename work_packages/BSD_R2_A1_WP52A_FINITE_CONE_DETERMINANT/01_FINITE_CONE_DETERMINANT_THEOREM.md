# WP52A theorem — exact determinant contribution of the strict/Kummer finite cone

## 1. Protected setup

Retain protected WP48A and WP51A. Write

`C_str := C_str,0`,

`C_Kum := C_Kum,0`.

Protected WP48A supplies a canonical exact triangle

`C_str -> C_Kum -> Q_fin -> C_str[1]`

with

`Q_fin ~= V_K[-1]`

and a canonical short exact sequence

`0 -> R_K -> V_K -> Zloc -> 0`.

Here `V_K` is finite.

Protected WP39 gives

`len_Z2 R_K
 = 2 m_2 + 2 sum_{ell|N} ord_2(c_ell)`,

where

`m_2 := ord_2(3-a_2)`.

Protected WP48A gives

`Zloc = direct_sum_{w|2} Z_w^str`.

Each `Z_w^str`, after specialization to `Z_2`, has length `m_2`, and the protected auxiliary field has exactly two places over `2`. Thus

`len_Z2 Zloc = 2 m_2`.

No new arithmetic premise is introduced in WP52A.

## 2. Relative determinant valuation

Because `Q_fin` has finite cohomology, it becomes acyclic after tensoring with `Q_2`. Therefore

`C_str tensor Q_2 -> C_Kum tensor Q_2`

is a quasi-isomorphism and canonically identifies their rational determinant lines.

For a finite perfect `Z_2`-complex `C`, define its cohomological determinant valuation by

`v_det(C)
 := sum_i (-1)^i len_Z2 H^i(C)`.

This is additive in exact triangles. Equivalently, it is the valuation of the integral determinant lattice relative to the canonical rational trivialization, with the displayed cohomological sign convention.

### Lemma `BSD-A1-WP52A-SHIFT-001`

If a finite module `F` is placed in cohomological degree one, so that the complex is `F[-1]`, then

`v_det(F[-1]) = -len_Z2 F`.

### Proof

The only nonzero cohomology group is

`H^1(F[-1])=F`.

The definition gives

`v_det(F[-1])=(-1)^1 len_Z2 F=-len_Z2 F`.

QED.

## 3. Exact strict-to-Kummer determinant correction

### Theorem `BSD-A1-WP52A-DET-CONE-001`

Under the rational determinant-line identification induced by

`C_str -> C_Kum`,

the relative integral determinant valuation is

`v_det(C_Kum/C_str)
 = -len_Z2 V_K`.

Equivalently, in the reverse Kummer-to-strict direction,

`v_det(C_str/C_Kum)
 = +len_Z2 V_K`.

### Proof

Determinant additivity for the exact triangle gives

`det(C_Kum)
 ~= det(C_str) tensor det(Q_fin)`.

After tensoring with `Q_2`, the finite third term is acyclic, so the first two determinant lines acquire the canonical common rationalization. The relative integral valuation is therefore exactly the determinant valuation of `Q_fin`.

Protected WP48A gives

`Q_fin ~= V_K[-1]`.

Apply Lemma `SHIFT-001`:

`v_det(Q_fin)=-len_Z2 V_K`.

This proves the forward formula. The reverse formula changes the sign. QED.

## 4. Exact numerical value

### Theorem `BSD-A1-WP52A-VK-LENGTH-001`

One has

`len_Z2 V_K
 = 4 ord_2(3-a_2)
   + 2 sum_{ell|N} ord_2(c_ell)`.

### Proof

From the protected short exact sequence

`0 -> R_K -> V_K -> Zloc -> 0`,

length additivity gives

`len V_K = len R_K + len Zloc`.

Protected WP39 gives

`len R_K
 = 2 ord_2(3-a_2)
   + 2 sum_{ell|N} ord_2(c_ell)`.

Protected WP48A gives one specialized strict higher term of length

`ord_2(3-a_2)`

at each of the two places of `K` above `2`, so

`len Zloc=2 ord_2(3-a_2)`.

Adding gives the displayed formula. QED.

## 5. Why `j_K` and `d_K` are not determinant inputs

Protected WP39 and WP40 define

`j_K := len_Z2 J_K`,

`d_K := len_Z2 D_K`

and prove

`j_K+d_K=len_Z2 R_K`.

Protected WP50A and WP51A further identify the complementary finite correction structurally through the strict degree-two silent kernel and Matlis/Pontryagin duality.

Those refinements do not alter the determinant triangle. Its finite third term is `V_K[-1]`, not `J_K[-1]`, `D_K[-1]`, or a direct sum chosen from them.

Numerically,

`len V_K
 = len R_K + len Zloc
 = j_K+d_K+len Zloc`.

The determinant therefore depends only on the already-protected sum `j_K+d_K`, together with the separately known local higher term `Zloc`. No individual value of `j_K` or `d_K` occurs.

### Corollary `BSD-A1-WP52A-D2B-CLOSE-001`

The WP51A boundary

`MISSING_P2_FINITE_MATLIS_CORRECTION_EVALUATION_OR_CANCELLATION_IN_DETERMINANT_NORMALIZATION`

is closed for the determinant normalization governed by the protected strict/Kummer comparison triangle.

The exact replacement datum is

`DET_STRICT_KUMMER_CORRECTION
 = 4 ord_2(3-a_2)
   + 2 sum_{ell|N} ord_2(c_ell)`

in the Kummer-to-strict direction, with the opposite sign in the strict-to-Kummer direction.

No theorem evaluating `d_K` separately is required for this determinant-line comparison.

## 6. Compatibility with protected WP20

Protected WP20 requires that every finite specialization kernel/cokernel be retained exactly when an arithmetic determinant datum is compared with the primitive Kummer specialization.

WP52A supplies precisely such an exact finite comparison correction for the protected strict/Kummer bridge. It does not alter WP20's intrinsic rank-one Bockstein ideal, which is defined on the free kernel and free quotient after torsion is removed.

This is consistent with WP51A: the finite Matlis correction is invisible to the first `Z_2`-valued height but remains present in the determinant complex through the full finite comparison cone. WP52A evaluates that entire finite determinant contribution without requiring a separate `d_K` calculation.

## 7. Surviving boundaries

After WP52A the principal unresolved obligations remain:

- D1c: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2a: `MISSING_P2_K_HEIGHT_NONDEGENERACY`;
- D2c: `MISSING_P2_DISEGNI_SPLIT_BAD_PRIME_NEWVECTOR_QORD_FACTORS`;
- D2d: `MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`;
- D2e: `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

D2b is resolved by the exact finite-cone determinant correction above.

## 8. Claim firewall

WP52A does not prove:

- `D_K=0`, `J_K=R_K`, or `K_K^sil=0`;
- fixed-`2` first-height nondegeneracy;
- an analytic determinant generator at the height-one prime `(2)`;
- global `Q^ord=1`;
- the classical Gross–Zagier/WP00 normalization;
- final quadratic descent;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
