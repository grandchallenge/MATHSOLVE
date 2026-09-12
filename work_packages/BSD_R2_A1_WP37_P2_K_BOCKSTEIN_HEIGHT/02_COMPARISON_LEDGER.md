# WP37 exact D2 comparison ledger

| Obligation | Protected input | What is already exact | What remains | Status |
|---|---|---|---|---|
| `D2a` fixed-`p=2` height nondegeneracy | MATHFORGE WP37 Nekovář; MATHSOLVE WP09 Disegni | the first cyclotomic height exists literally at `p=2` over totally imaginary `K`; its ideal is canonical | prove the first height on the selected rank-one line is nonzero, or replace it with a literal-`p=2` derived-height theorem | `OPEN_THEOREM` |
| `D2b` height lattice -> primitive Kummer lattice | WP16B, WP20, WP21, WP35, WP36 | primitive Kummer determinant and control defect are exact; WP36 makes `len C_E^vee` finitely computable | identify Nekovář's source-compatible extended/ordinary lattice with the protected primitive determinant, including exact index | `OPEN_COMPARISON` |
| `D2c` Disegni interpolation factors | WP09 corrected p-adic Gross–Zagier | exact source formula and applicability at `p=2` | evaluate `ord_2(e_{2,infinity}^{-1} Q)` and reconcile with protected unit-root/local terms | `OPEN_NORMALIZATION` |
| `D2d` classical/WP00 normalization | WP05/WP00 classical analytic package | complex rank one, finite Sha, classical target normalization fixed | reconcile the same Heegner line with complex Gross–Zagier/WP00 factors; do not identify p-adic and real heights | `OPEN_NORMALIZATION` |
| `D2e` exact descent `K -> Q` | WP06 | local quadratic-descent defect groups vanish at all places dividing `2N` because they split in `K`; finite-level plus/minus identity is exact | retain/evaluate integral overlap/quotient terms and twist contribution in the final normalized identity | `OPEN_DESCENT` |
| `D1c` analytic determinant at `(2)` | WP17B, WP35 | Kato away-from-`(2)` control; algebraic square presentation | literal-`p=2` analytic characteristic/determinant generator at height-one `(2)` or equivalent exact reciprocity theorem | `OPEN_THEOREM` |

## Nonnegotiable firewall

- “Defined modulo `Z_2^x`” is enough for valuation/ideal statements, not for a preferred generator.
- A p-adic height is not a Néron–Tate height.
- Nondegeneracy is not inferred from complex analytic rank one.
- Split local descent at `2N` does not justify division by `2` in the global plus/minus decomposition.
- No odd-prime main-conjecture or derived-height theorem may be specialized silently to `p=2`.
