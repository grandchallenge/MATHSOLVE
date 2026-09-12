# BSD-R2-A1 WP37 — literal-`p=2` Bockstein height over the protected imaginary quadratic lane

## State

`PROVED_BOUNDED_REDUCTION`

This work package continues protected WP36 without changing the campaign claim state.

Protected inputs:

- MATHSOLVE WP06 exact quadratic `2`-descent control;
- MATHSOLVE WP09 protected imaginary quadratic field `K` and corrected Disegni applicability;
- MATHSOLVE WP16B/WP19/WP20 integral primitive Selmer/Fitting/Bockstein invariants;
- MATHSOLVE WP21–WP36 exact local/control corrections;
- MATHFORGE protected source admission `eceaf6f0f2e10e5bd48afd1ca57f9245669202de`, admitting Nekovář's literal-`p=2` totally-imaginary Selmer-complex Bockstein-height interface.

## Purpose

WP36 leaves two principal determinant-side obligations:

- D1c `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2 `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`.

WP37 attacks D2 in the preferred arena already fixed by WP09. It proves that the formal `p=2` Bockstein-height object exists over `K`, identifies exactly what is basis-invariant at integral level, and replaces the broad D2 label by a smaller explicit comparison ledger.

WP37 does **not** prove a `p=2` main conjecture, p-adic height nondegeneracy, an analytic determinant generator at `(2)`, or the selected BSD equality.

## Main result

Let `K/Q` be the protected WP09 imaginary quadratic field. Because `K` is totally imaginary, Nekovář's Selmer-complex duality and cyclotomic height construction applies literally at `p=2`.

For the source-compatible cyclotomic Selmer complex of `T_2(E)` over `K`, the height pairing is the Bockstein morphism followed by Selmer-complex duality. On any rank-one free source-compatible quotient, choosing primitive bases and a topological generator of the cyclotomic Galois group gives a scalar in `Z_2`; changing any of these primitive choices multiplies the scalar by a unit. Consequently its principal ideal and its `2`-adic valuation are canonical.

Nekovář's leading-term formalism supplies exact valuation/length information when the corresponding first height is nondegenerate. It does not select a canonical determinant generator, and therefore does not close D1c.

## Exact D2 reduction

The remaining D2 obligation is decomposed into four explicit interfaces:

1. `K-LATTICE`: compare the Nekovář extended/Greenberg rank-one lattice over `K` with the protected primitive Kummer lattice and WP20 Bockstein ideal, retaining all finite local and control indices;
2. `PGZ-NORM`: evaluate every `2`-adic valuation in Disegni's interpolation/test-vector factor `e_{2,infinity}^{-1} Q` and match it to the protected local ledger;
3. `CLASSICAL-NORM`: compare the same Heegner-point line with the protected complex Gross–Zagier/WP00 Néron–Tate normalization without equating p-adic and real heights;
4. `DESCENT`: descend the resulting exact integer identity through WP06, retaining the integral plus/minus overlap/quotient terms and every power of `2`.

There is an additional necessary dichotomy: if the first Nekovář height on the rank-one line is zero, the minimal leading-order statement fails and the present simple-leading-term route cannot close D2. Nondegeneracy at the fixed prime `2` is therefore a theorem obligation, not a normalization convention.

The exact successor boundary is

`MISSING_P2_K_HEIGHT_NONDEGENERACY_AND_INTEGRAL_NORMALIZATION_COMPARISON`.

D1c remains independently

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

## Claim firewall

`BSD-R2-A1` remains `SELECTED_RESEARCH_TARGET_UNPROVED`.

No numerical evidence, parity result, modulo-square statement, odd-prime theorem, or equality up to a unit is promoted to exact `2`-primary BSD. No MATHCERT certification is claimed.