# BSD-001 frontier after WP40

## Protected predecessor

MATHSOLVE WP39:

`3d9e94d2b0f06d0e93387f959a0e32c6346e0d21`.

No new external theorem premise is used in WP40. The theorem uses the already-protected literal-`p=2` Greenberg Poitou–Tate/global-local orthogonality interface.

## WP40 closure

Let

`R_K := U_Kum/U_str`

be the finite compact local quotient from WP39, and let

`R_K^dual := U_str^perp/U_Kum^perp`.

WP40 proves a perfect finite pairing

`R_K x R_K^dual -> Q_2/Z_2`.

For the compact global hit `J_K subset R_K`, define the dual global hit

`D_K := im((G_A intersect U_str^perp) -> R_K^dual)`.

Then

`ann(J_K)=D_K`.

Consequently, if

`j_K:=len_Z2 J_K`,

`d_K:=len_Z2 D_K`,

one has exactly

`j_K+d_K
 = 2 ord_2(3-a_2)
   + 2 sum_{ell|N} ord_2(c_ell)`.

Thus the K-side Greenberg/Kummer comparison is determined once `D_K` is evaluated.

## Live boundaries

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

### D1c

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

### D2a

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

### D2b

`MISSING_P2_DUAL_GLOBAL_HIT_OVER_K`.

The former compact image problem is now exactly complementary to the finite dual global hit `D_K`.

### D2c

`MISSING_P2_DISEGNI_INTERPOLATION_FACTOR_VALUATIONS`.

### D2d

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.

### D2e

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Immediate successor

Two bounded continuations are executable.

### WP41A — merge D2a and D2b if justified

Starting from protected WP37 Nekovář Bockstein-height formalism, determine whether the dual global hit `D_K` is canonically an image, cokernel, radical, or other exact finite quotient of the first cyclotomic Bockstein map/height complex.

Do not infer such an identification merely because both constructions use Selmer duality. If a new arithmetic comparison theorem is required, admit it through MATHFORGE first.

The ideal outcome is an exact formula

`d_K = length(explicit Bockstein/height defect)`

that remains valid even when the first height is degenerate. This would combine the present D2a and D2b boundaries into one integral defect.

### WP41B — Disegni ordinary-normalization cancellation

The corrected Disegni source already shows in Proposition 4.3.4 that, for ordinary test vectors, the ordinary toric pairing absorbs the `p`-interpolation factor. In the selected trivial-weight lane `e_infinity=1`, so test whether the Theorem-B factor

`e_{2,infinity}^{-1} Q`

can be replaced exactly by the ordinary pairing `Q^ord` for a source-compatible ordinary test-vector choice. Then decompose `Q^ord` place by place and compute its `2`-adic valuation without hiding measure or bad-prime factors.

Any new source premise beyond the already-admitted Disegni theorem must be admitted through MATHFORGE.

## Claim firewall

Do not promote:

- `D_K=0` or `J_K=R_K`;
- any rank-one scalar description of the dual global hit without proving the required rank/torsion statement;
- a formal analogy between Poitou–Tate and Bockstein to an equality of finite modules;
- p-adic-height existence to nondegeneracy;
- an ordinary-pairing normalization to a unit claim before computing all local factors;
- an odd-prime theorem to `p=2`;
- BSD or MATHCERT certification.
