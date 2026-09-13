# BSD-001 frontier after WP51A

## Protected inputs

- MATHSOLVE WP50A: `e078beae05252c4152787fc812e0823b14c23fac`.
- MATHFORGE WP51 strict-H2 duality admission: `79302cdc05f3f11c56e048f68e9095d3280872a7`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.

## WP51A closure

Let

`S_str^dual := H~^1_f(K,A^*(1);Delta_str^perp)`

and let

`N_K := (K_K^sil)^perp`

under the protected literal-`p=2` Matlis/Pontryagin pairing with strict `H~^2_f(K,T;Delta_str)`.

Then

`0 -> N_K -> S_str^dual -> D_K -> 0`

canonically.

The first Nekovar height uses the separate `Z_2`-valued degree-(2,1) lattice duality pairing after the cyclotomic Bockstein. Because `K_K^sil` is finite and `Z_2` is torsion-free, this pairing kills `K_K^sil`. Hence the first height factors through

`H~^2_f(K,T;Delta_str)/tors`.

Therefore the finite WP40 correction and fixed-`2` first-height nondegeneracy do not formally merge. `D_K` is a finite Matlis/Pontryagin correction invisible to the first integral height.

## Live boundaries

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

### D1c

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

### D2a

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

### D2b

`MISSING_P2_FINITE_MATLIS_CORRECTION_EVALUATION_OR_CANCELLATION_IN_DETERMINANT_NORMALIZATION`.

Write

`d_K:=len_Z2 D_K=len_Z2 K_K^sil`.

WP40 already proves

`j_K+d_K
 = 2 ord_2(3-a_2)
   + 2 sum_{ell|N} ord_2(c_ell)`.

What remains is not a height-radical comparison. A successor must either evaluate `d_K` exactly or prove an exact determinant comparison in which the finite Matlis correction cancels against another identified finite term. A total-length identity alone is insufficient unless the determinant comparison is proved to depend only on that total.

### D2c

`MISSING_P2_DISEGNI_SPLIT_BAD_PRIME_NEWVECTOR_QORD_FACTORS`.

### D2d

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.

### D2e

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Immediate successor WP52A

Audit the integral determinant comparison from the strict `K`-side Selmer complex to the protected primitive Kummer determinant target. Track the finite subquotients `J_K` and `D_K` through determinant functor exact triangles. Determine whether the determinant correction is:

1. `d_K` separately;
2. `j_K` separately;
3. only the protected total `j_K+d_K=len R_K`; or
4. canceled by a canonically dual finite determinant term.

No cancellation may be inferred from perfect duality alone.

## Parallel successor WP52B

Continue the split semistable bad-prime/newvector `Q^ord` factor calculation with all measures, local L-factors, denominator pairings, Tamagawa scalars, and powers of `2` retained.

## Firewall

WP51A does not prove `D_K=0`, `K_K^sil=0`, `N_K=Sel_A^{Kum}(K)`, height nondegeneracy, an exact value/cancellation of `d_K`, D1c, global `Q^ord=1`, WP00 normalization, final descent, BSD, or certification.
