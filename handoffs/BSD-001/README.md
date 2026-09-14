# BSD-001 canonical continuation handoff

## Authority and claim state

- Campaign: `BSD-001 — Birch-Swinnerton-Dyer selected rank-one 2-primary campaign`.
- Mathematical repository: `grandchallenge/MATHSOLVE`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Active tracker: `grandchallenge/MATHSOLVE#215`.
- Source authority: `grandchallenge/MATHFORGE`.
- Constitutional authority: protected `grandchallenge/INTELLECT`.
- Certification authority: `grandchallenge/MATHCERT` only.
- Selected target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

Use protected repository state as authority. Do not use mutable issue text, stale summaries, numerical evidence, or odd-prime theorems as substitute authority.

## Canonical read order

After re-fetching protected live heads, read:

1. this file;
2. `handoffs/BSD-001/WP60B_FRONTIER.md`;
3. `work_packages/BSD_R2_A1_WP60B_KRIZ_LI_TRANSPORT/00_README.md`;
4. `work_packages/BSD_R2_A1_WP60B_KRIZ_LI_TRANSPORT/01_KRIZ_LI_TRANSPORT_THEOREM.md`;
5. `work_packages/BSD_R2_A1_WP60B_KRIZ_LI_TRANSPORT/02_CLAIM_LEDGER.yaml`;
6. protected WP60A-A1 for the height-one-`(2)` determinant lane;
7. `work_packages/BSD_R2_A1_WP60_P2_FRONTIER_RESEARCH_PROGRAM/01_EXECUTION_CONTRACT.md`;
8. protected MATHFORGE WP60B/WP60A/WP59 records;
9. only then deeper predecessors needed by the active lane.

## Governing invariant

`delta_2(E)
 := ord_2(L'(E,1)/(Omega_E Reg_E))
    - sum_{ell|N}ord_2(c_ell)`.

Protected WP16A/WP16B/WP19 give

`v_2(Fitt^1_{Z_2}(X_E))
 = len_Z2 Sha(E/Q)[2^infinity]
 = lim_n(ord_2 #Sel_{2^n}(E/Q)-n)`.

The selected theorem is exactly

`delta_2(E)=v_2(Fitt^1_{Z_2}(X_E))`.

## Current arithmetic reduction

Protected WP55A–WP58A give

`delta_2(E)
 = 1 + 2ord_2(m_K(f))
   - ord_2(c_infinity(E^D))
   - ord_2(lambda_D)
   - sum_{ell|N}ord_2(c_ell)`,

where

`lambda_D=L(E^D,1)/Omega(E^D) in Q^x`

and `ord_2(C_f)=0` for the fixed source-compatible parametrization.

Protected WP59 isolates

`R_2(E,K,f)=2ord_2(m_K(f))-ord_2(lambda_D)`.

## WP60A protected result

WP60A-A0 fixes the finite algebraic determinant/control factors. WP60A-A1 proves that the inverse determinant line of the relevant rank-one two-term complex maps to

`Fitt^0(H^2)H^1`.

Thus the remaining determinant lane is exactly:

- `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`;
- `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

Do not restart generic determinant-formalism reconnaissance without new arithmetic input.

## WP60B exact source transport

Protected MATHFORGE WP60B admits Kriz–Li's literal-`2` condition

`((3-a_2)/2)log_{omega_f^KL}(P_KL(f)) != 0 mod 2`,

with

`f^*omega_f^KL=phi(q)dq/q`.

Protected WP58A gives

`f^*omega_E=+/- C_f phi(q)dq/q`,

so

`omega_f^KL=+/- C_f^(-1)omega_E`

with `C_f in Z_2^x`.

For the protected primitive generator `P`, define

`kappa_2(E,P):=((3-a_2)/2)log_{omega_E}(P)`.

WP60B proves the exact factorization

`KL_2(E,K,f)=u_f m_K(f)kappa_2(E,P)`,

with `u_f in Z_2^x`.

## WP60B ordinary local obstruction

The selected class has good ordinary reduction at `2`. For a minimal integral Weierstrass model, WP60B proves the coefficient `A_1` is odd. The formal invariant differential then gives

`log_{omega_E}(E_1(Q_2)) subset 4Z_2`.

Since `[3-a_2]P` reduces to the identity,

`kappa_2(E,P)
 = (1/2)log_{omega_E}([3-a_2]P)
 in 2Z_2`.

Therefore

`KL_2(E,K,f) in 2Z_2`

for every selected curve and every WP09-compatible field.

### Exact disposition

`KRIZ_LI_F_LOCALLY_OBSTRUCTED_ON_SELECTED_GOOD_ORDINARY_LANE`.

Kriz–Li Assumption `(F)` cannot hold on the protected selected branch. This is a theorem about the current good-ordinary local hypotheses, not a general impossibility claim for other reduction types.

## WP59 reopening contract after WP60B

Retire `R3` on the selected branch:

`R3_RETIRED_FOR_SELECTED_GOOD_ORDINARY_LANE_BY_WP60B_LOCAL_OBSTRUCTION`.

Surviving D2d reopening routes are:

- `R1`: exact literal-`p=2` Heegner-index control;
- `R2`: exact WP00-normalized twist-L-ratio valuation under all WP09 constraints without an unavailable rank-zero seed;
- `R4`: a direct exact theorem for `R_2(E,K,f)`;
- `R5`: literal-`p=2` height-one-`(2)` main-conjecture/reciprocity control specializing to the protected determinant line.

D2d remains

`MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.

## Genuine Heegner-index boundary

Protected WP12 implies `E(K)[2]=0` for quadratic `K`; hence the torsion subgroup has odd order. Combined with

`P_K(f)=m_K(f)P+T`,

WP60B proves

`P_K(f) is indivisible by 2 <=> m_K(f) is odd`.

The live parity boundary is therefore

`MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.

## Other live boundaries

- `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.
- `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- `MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.
- `MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.
- downstream `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## WP60C disposition

The original WP60C question whether `kappa_2(E,P)` might be a unit is superseded: WP60B proves it is uniformly even. Do not spend the primary lane sampling an already-proved proposition.

If computation is used, redirect it toward surviving R1/R2/R4 structure and use only real selected curves and WP09-compatible fields. Computational evidence remains non-promotive.

## Highest-value continuation

After exact-head protection of WP60B, proceed to a surviving theorem route rather than more Kriz–Li forcing. Prefer a route with genuinely new exact information:

1. Heegner-index parity (`R1` component);
2. twist-L-ratio valuation (`R2`);
3. a combined residual identity (`R4`);
4. height-one-`(2)` Fitting divisibility/primitivity (`R5`/D1c);
5. fixed-`2` height nondegeneracy (D2a) if a new literal-`2` theorem interface appears.

## Claim firewall

Do not promote `m_K(f)` to odd, `lambda_D` to a unit, any surviving WP59 route to resolved, D2d, `BSD-R2-A1`, or MATHCERT certification. The local impossibility result concerns only Kriz–Li `(F)` under the protected selected good-ordinary-at-`2` hypotheses.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, exact computation, source admission when required, exact-head Adversary and Referee review, ordinary CI, protected merge/readback, issue maintenance, and canonical handoff maintenance.

Recoverable connector, CI, logging, formatting, source-access, compiler, or computational failures are recovery events, not stopping conditions. Bind all evidence to the current exact head. Stop only at a genuine named theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target drift, or MATHCERT authority boundary.
