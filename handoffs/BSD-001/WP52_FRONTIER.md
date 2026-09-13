# BSD-001 frontier after WP52A

## Protected predecessors

- MATHSOLVE WP51A protected head: `3b34edc3e66c4be86a4319bc71da39bb5fc055f0`.
- MATHFORGE WP51 protected head: `79302cdc05f3f11c56e048f68e9095d3280872a7`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.

## WP52A result

The exact finite strict/Kummer comparison triangle is

`C_str,0 -> C_Kum,0 -> Q_fin ->`,

with

`Q_fin ~= V_K[-1]`

and

`0 -> R_K -> V_K -> Zloc -> 0`.

Hence the two finite-level Selmer complexes are rationally quasi-isomorphic and their integral determinant-line ratio is controlled exactly by `Q_fin`.

With cohomological determinant valuation

`v_det(C)=sum_i (-1)^i len_Z2 H^i(C)`

for a finite complex,

`v_det(C_Kum/C_str) = -len_Z2 V_K`,

and in the reverse direction

`v_det(C_str/C_Kum) = +len_Z2 V_K`.

The exact finite length is

`len_Z2 V_K
 = 4 ord_2(3-a_2)
   + 2 sum_{ell|N} ord_2(c_ell)`.

Although WP39/WP40 decompose the local incidence through

`j_K+d_K=len_Z2 R_K`,

the determinant functor sees the complete finite cone `V_K`, not separate values of `j_K` or `d_K`. Therefore the WP51A finite-Matlis determinant debt is closed.

## D2b disposition

`D2b = RESOLVED_WP52A_FINITE_COMPARISON_DETERMINANT`.

`D_K`, `J_K`, and `K_K^sil` remain meaningful structural invariants. WP52A does not prove that any of them vanish. It proves only that their separate lengths are not independent inputs to the protected strict/Kummer determinant normalization.

## Live unresolved boundaries

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

### D1c

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

### D2a

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

### D2c

`MISSING_P2_DISEGNI_SPLIT_BAD_PRIME_NEWVECTOR_QORD_FACTORS`.

### D2d

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.

### D2e

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Immediate successors

### WP53A — split bad-prime `Q^ord` factor normalization

For every split semistable odd bad prime `ell|N`, compute Disegni's normalized local ordinary/newvector toric factor with the exact protected conventions. Retain:

- split versus nonsplit multiplicative type;
- Steinberg twist;
- local Haar measure;
- local `L`-factor normalizations;
- denominator pairing;
- Tamagawa-sensitive powers of `2`;
- any newvector scaling.

The target is an exact product formula for the remaining bad-prime contribution to `Q^ord`, not an assertion that the factors are units.

### WP53B — height-one `(2)` analytic determinant screen

Maintain the narrow D1c search only: an admissible route must be literal at `p=2`, retain the height-one prime containing `2`, and produce an analytic determinant/characteristic generator compatible with the protected primitive rank-one determinant datum. Do not reopen broad odd-prime main-conjecture reconnaissance.

## Firewall

Do not promote:

- finite-cone determinant closure to `D_K=0` or height nondegeneracy;
- local `Q^ord_2=1` to global `Q^ord=1`;
- any split bad-prime factor to a unit without exact calculation;
- source admission to mathematical certification;
- `BSD-R2-A1`, novelty, priority, patentability, or commercial claims.
