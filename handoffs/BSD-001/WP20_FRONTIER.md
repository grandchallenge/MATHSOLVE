# BSD-001 WP20 frontier handoff

## Protected predecessor

Start from protected WP19 at

`grandchallenge/MATHSOLVE@4af233409188ce68a36a00db4716ea0daabb8c98`.

WP19 proves

`delta_2(E)=v_2(Fitt^1_{Z_2}(X_E))`

is exactly equivalent to the selected target, where

`X_E := Sel_{2^infinity}^{Kum}(E/Q)^vee`.

## WP20 result

WP20 proves the universal rank-one determinant identity.

For a DVR `R`, `S=R[[T]]`, and a square matrix

`A(T)=A_0+T A_1+...`

with `rank_K A_0=m-1`, set

`M=coker A_0`.

The coefficient `A_1` induces an intrinsic rank-one map

`beta_A:ker A_0 -> M/Tor(M)`.

Let `B_A` be its principal scalar ideal. Then

`(coeff_T det A(T)) = Fitt^1_R(M) B_A`.

For `R=Z_2`,

`ord_2(coeff_T det A(T))
 = v_2(Fitt^1_{Z_2}(M)) + v_2(B_A)`

whenever the coefficient is nonzero.

## Arithmetic consequence

For any exact arithmetic determinant datum specializing to the protected primitive module `X_E`, the selected target becomes

`ord_2(coeff_T Theta_E(T))-v_2(B_E)=delta_2(E)`.

Thus the missing theorem has split into two independent obligations.

### D1 — primitive determinant realization

Construct a literal-`p=2` arithmetic determinant/Selmer datum whose specialization is exactly `X_E`, or compute every finite comparison defect.

Boundary:

`MISSING_P2_PRIMITIVE_RANK1_DETERMINANT_REALIZATION`.

### D2 — Bockstein/WP00 normalization

For the D1 determinant datum prove exactly

`ord_2(coeff_T Theta_E)-v_2(B_E)
 = ord_2(L'(E,1)/(Omega_E Reg_E))
   - sum_{ell|N} ord_2(c_ell)`.

Boundary:

`MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`.

## Required read order for continuation

After re-fetching protected live state, read:

1. `handoffs/BSD-001/README.md`;
2. `work_packages/BSD_R2_A1_WP19_DERIVED_PRIMITIVE_FITTING/`;
3. `work_packages/BSD_R2_A1_WP20_RANK1_BOCKSTEIN_FACTORIZATION/`;
4. protected WP16B local-normalization matrix;
5. protected WP06/WP07/WP09/WP13 only when an arithmetic determinant route uses those interfaces;
6. current protected MATHFORGE BSD provider audits before importing any external theorem premise.

## Next source/construction rule

Do not perform another generic literature survey.

Search only for a theorem that supplies D1, D2, or a separately composable clause of one of them. In particular, inspect determinant/Bockstein or positive-rank Mazur-Tate/Kato results for whether their algebraic formalism survives at `p=2` even when their arithmetic theorem hypotheses do not.

Any new external theorem premise must be admitted through MATHFORGE before protected mathematical use.

## Claim firewall

- `BSD-R2-A1` remains `SELECTED_RESEARCH_TARGET_UNPROVED`.
- WP20 is pure algebra plus an exact conditional reduction.
- No arithmetic determinant or regulator comparison is inferred from the matrix theorem.
- No odd-prime theorem is specialized silently to `p=2`.
- No theorem-nonexistence claim is made.
- MATHCERT remains the only certification authority.
