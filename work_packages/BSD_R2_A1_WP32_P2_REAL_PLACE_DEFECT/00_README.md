# BSD-R2-A1 WP32 — p=2 real-place defect cancellation

## Status

Candidate mathematical work package. No claim is protected until exact-head review, affected CI, protected merge, and readback complete.

## Exact protected inputs

- MATHSOLVE protected base: `6f34bba352024d864fd83c98b0532e8c71002e24`.
- MATHFORGE source authority: `6f5059836de4330a37f6de8baec5634f889921c4`.
- Admitted source audit:
  `sources/BSD-001/BURNS_MACIAS_P2_SELMER_ARCHIMEDEAN_DEFECT_WP32_SOURCE_AUDIT.md`.
- Protected WP20 rank-one determinant/Bockstein reduction.
- Protected WP16B/WP19 primitive module
  `X_E = Sel_{2^infinity}^{Kum}(E/Q)^vee`.

## Purpose

Burns–Macias Castillo provide a literal-`p=2` integral perfect Selmer complex over `Q`, but their comparison with classical arithmetic modules contains finite real-place terms.

WP32 computes the specifically archimedean `p=2` comparison defect exactly and asks only whether it changes the `2`-adic determinant valuation.

It does not attempt the finite-place primitive comparison, the cyclotomic determinant construction, the height-one `(2)` analytic generator, or the Bockstein/WP00 normalization.

## Result under candidate review

Let

`c_infty(E) := #pi_0(E(R)) in {1,2}`

and

`epsilon_infty(E) := ord_2(c_infty(E)) in {0,1}`.

For the full source-compatible archimedean lattice

`X'_infty := H_infty(E/Q)_2`,

WP32 proves:

1. `cok H^0(kappa_2)=0`;
2. `H^1(R,T_2E) ~= pi_0(E(R))`;
3. `H^2(R,T_2E)` is Pontryagin-dual to `H^1(R,T_2E)`;
4. therefore
   `len_Z2 H^1(R,T_2E)=len_Z2 H^2(R,T_2E)=epsilon_infty(E)`;
5. the associated archimedean comparison cone has zero alternating `Z_2`-length and unit fractional Fitting ideal.

Hence the specifically real-place `p=2` defect contributes no net `2`-adic determinant valuation.

## Remaining boundaries

WP32 does not close:

- D1a `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
- D1c `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2 `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`;
- D1b `MISSING_P2_FINITE_TWISTED_RECIPROCITY_EXPONENT` from protected WP31.

The next determinant-side tranche must move to the finite-place / primitive-Kummer comparison and then to a cyclotomic deformation. It must not reintroduce an archimedean valuation correction already eliminated here.

## Claim firewall

No exact determinant generator, analytic identity, regulator comparison, BSD equality, theorem novelty, or MATHCERT certification is asserted by this work package.