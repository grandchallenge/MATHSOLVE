# BSD-R2-A1-WP57A — exact area/twist rationalization

## Protected inputs

- MATHSOLVE protected base: `ae694de9c18c6c2ff3e46002bc8ed008f7b4fb01`.
- MATHFORGE protected WP57 source head: `ed91d13e13ec3577493548466b1411fc70b2693d`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Selected claim: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

Protected WP56A gives

`L'(E,1)/(Omega_E Reg_E)
 = 4 m_K(f)^2 A_E
   / (C_f^2 u_K^2 sqrt(|D_K|) Omega_E L(E^D,1))`.

WP57A converts the remaining real area/period/twist scalar to an exact rational line without using rank-zero BSD for `E^D`.

## Main result

Let `Omega_E^-` be the Pal/WP57 imaginary period associated with a primitive anti-invariant integral homology generator, and let `|Omega_E^-|` denote its positive magnitude.

An elementary classification of the real period lattice gives exactly

`A_E = Omega_E |Omega_E^-| / 2`.

Protected MATHFORGE WP57 gives, on the selected semistable auxiliary lane,

`Omega(E^D)
 = c_infinity(E^D) |Omega_E^-| / sqrt(|D_K|)`,

because Pal's minimal-model correction is exactly `tilde u=1`.

Define

`lambda_D := L(E^D,1)/Omega(E^D)`.

Protected MATHFORGE WP57 places `lambda_D` in `Q^x`; protected WP09 gives it nonzero. The already-admitted Cai–Shu–Tian normalization defines `C_f` as a positive integer. The selected imaginary quadratic field has `u_K=1` because `2` splits and therefore `K` is neither `Q(i)` nor `Q(sqrt(-3))`.

Consequently

`L'(E,1)/(Omega_E Reg_E)
 = 2 m_K(f)^2
   / (C_f^2 c_infinity(E^D) lambda_D)`

as an exact nonzero rational identity.

Hence the 2-adic valuation is now legitimate and exact:

`ord_2(L'(E,1)/(Omega_E Reg_E))
 = 1 + 2 ord_2(m_K(f))
   - 2 ord_2(C_f)
   - ord_2(c_infinity(E^D))
   - ord_2(lambda_D)`.

Thus

`delta_2(E)
 = 1 + 2 ord_2(m_K(f))
   - 2 ord_2(C_f)
   - ord_2(c_infinity(E^D))
   - ord_2(lambda_D)
   - sum_{ell|N} ord_2(c_ell)`.

No rank-zero BSD identity for the twist is used.

## Refined boundary

D2d is narrowed to

`MISSING_P2_HEEGNER_INDEX_MODULAR_DIFFERENTIAL_AND_TWIST_LRATIO_VALUATION_CONTROL`.

The remaining inputs are now ordinary integral/rational valuations:

- `ord_2(m_K(f))`;
- `ord_2(C_f)`;
- `ord_2(lambda_D)`;
- the explicit topological bit `ord_2(c_infinity(E^D))`;
- the already-protected Tamagawa ledger.

## Firewall

WP57A does not assert:

- `m_K(f)` is odd or primitive at `p=2`;
- `C_f=1` or even `ord_2(C_f)=0`;
- `lambda_D` is integral or a 2-adic unit;
- a rank-zero BSD formula for `E^D`;
- fixed-2 p-adic-height nondegeneracy;
- a height-one `(2)` analytic determinant generator;
- the final WP06 normalization descent;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, priority, patentability, or commercial claims.
