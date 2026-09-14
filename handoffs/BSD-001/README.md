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
2. `handoffs/BSD-001/WP60D_FRONTIER.md`;
3. `work_packages/BSD_R2_A1_WP60D_SURVIVING_ROUTE_REDUCTION/00_README.md`;
4. `work_packages/BSD_R2_A1_WP60D_SURVIVING_ROUTE_REDUCTION/01_SURVIVING_ROUTE_REDUCTION_THEOREM.md`;
5. `work_packages/BSD_R2_A1_WP60D_SURVIVING_ROUTE_REDUCTION/02_CLAIM_LEDGER.yaml`;
6. `handoffs/BSD-001/WP60B_FRONTIER.md` and the WP60B theorem package for the Kriz–Li obstruction;
7. protected WP60A-A1 for the height-one-`(2)` determinant lane;
8. `work_packages/BSD_R2_A1_WP60_P2_FRONTIER_RESEARCH_PROGRAM/01_EXECUTION_CONTRACT.md`;
9. protected MATHFORGE WP60B/WP60A/WP59 source records;
10. only then deeper predecessors required by the active lane.

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

## Protected arithmetic reduction

Protected WP55A–WP58A give

`delta_2(E)
 = 1 + 2ord_2(m_K(f))
   - ord_2(c_infinity(E^D))
   - ord_2(lambda_D)
   - sum_{ell|N}ord_2(c_ell)`,

where

`lambda_D=L(E^D,1)/Omega(E^D) in Q^x`

and `ord_2(C_f)=0` for the fixed source-compatible parametrization.

Protected WP59 defines

`R_2(E,K,f)=2ord_2(m_K(f))-ord_2(lambda_D)`.

## WP60A protected determinant result

WP60A-A0 fixes the finite algebraic determinant/control factors. WP60A-A1 proves that the inverse determinant line of the relevant rank-one two-term complex maps to

`Fitt^0(H^2)H^1`.

Thus the remaining determinant lane is exactly:

- `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`;
- `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

Do not restart generic determinant-formalism reconnaissance without new arithmetic input.

## WP60B protected Kriz–Li obstruction

Protected MATHFORGE WP60B admits Kriz–Li's literal-`2` condition

`((3-a_2)/2)log_{omega_f^KL}(P_KL(f)) != 0 mod 2`.

Protected MATHSOLVE WP60B transports it to

`KL_2(E,K,f)=u_f m_K(f)kappa_2(E,P)`,

with `u_f in Z_2^x` and

`kappa_2(E,P):=((3-a_2)/2)log_{omega_E}(P)`.

The selected good-ordinary-at-`2` hypothesis implies

`log_{omega_E}(E_1(Q_2)) subset 4Z_2`,

hence

`kappa_2(E,P) in 2Z_2`.

Therefore Kriz–Li Assumption `(F)` cannot hold on the protected selected lane.

Disposition:

`KRIZ_LI_F_LOCALLY_OBSTRUCTED_ON_SELECTED_GOOD_ORDINARY_LANE`.

Retire WP59 reopening form R3 on this selected branch:

`R3_RETIRED_FOR_SELECTED_GOOD_ORDINARY_LANE_BY_WP60B_LOCAL_OBSTRUCTION`.

This is a theorem about the selected good-ordinary local hypotheses only; it is not a general impossibility claim for other reduction types.

## WP60D surviving-route reduction

For every WP09-compatible quadratic field `K` with discriminant `D`, quadratic twisting preserves the real component count:

`c_infinity(E^D)=c_infinity(E)`.

Combining this with protected WP57A/WP58A gives the exact identity

`R_2(E,K,f)
 = ord_2(L'(E,1)/(Omega_E Reg_E))
   -1
   +ord_2(c_infinity(E))`.

Hence `R_2(E,K,f)` is independent of the auxiliary field `K`.

Equivalently,

`R_2(E,K,f)
 = delta_2(E)
   +sum_{ell|N}ord_2(c_ell)
   -1
   +ord_2(c_infinity(E))`.

Therefore the selected BSD equality is equivalent, for every WP09-compatible field, to

`R_2(E,K,f)
 = v_2(Fitt^1_{Z_2}(X_E))
   +sum_{ell|N}ord_2(c_ell)
   -1
   +ord_2(c_infinity(E))`.

Record the exact R4 classification:

`R4_EQUIVALENT_TO_FIXED_BASE_ANALYTIC_LEADING_TERM_VALUATION`.

R4 remains logically live, but it is not an auxiliary-field escape route. Do not search for a special `K` to change the combined residual; its value is fixed by the base curve.

## WP59 route map after WP60B/WP60D

### R1 — live

Exact literal-`p=2` Heegner-index control remains genuine field-dependent arithmetic information.

Current parity boundary:

`MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.

Protected WP60B proves

`P_K(f) is indivisible by 2 <=> m_K(f) is odd`.

### R2 — live

Exact twist-L-ratio valuation remains genuine field-dependent arithmetic input:

`MISSING_EXACT_WP00_TWIST_LRATIO_VALUATION_UNDER_WP09_CONSTRAINTS`.

Broad twist-value literature screening was already performed in WP59. Future R2 work must be theorem construction or a narrowly identified candidate, not another generic source sweep.

### R3 — retired on selected lane

`R3_RETIRED_FOR_SELECTED_GOOD_ORDINARY_LANE_BY_WP60B_LOCAL_OBSTRUCTION`.

### R4 — live but reduced

`R4_EQUIVALENT_TO_FIXED_BASE_ANALYTIC_LEADING_TERM_VALUATION`.

A theorem computing the fixed base analytic leading-term valuation could still close R4, but auxiliary-field variation cannot.

### R5 — live

Protected WP60A-A1 leaves:

- `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`;
- `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

## Other live boundaries

- D2a: `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2d: `MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.
- D2e: downstream `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

`BSD-R2-A1` remains unproved.

## WP60C disposition

The original WP60C question whether `kappa_2(E,P)` might be a unit is superseded by WP60B: it is uniformly even. Do not spend the primary lane sampling an already-proved proposition.

Computation may be redirected toward real selected-curve evidence relevant to R1/R2, but computational evidence remains non-promotive.

## Highest-value continuation after WP60D

Do not continue auxiliary-field searches for R4. Prefer genuinely new exact information in this order:

1. R5 / D1c: literal-`p=2` height-one-`(2)` Kato/Fitting divisibility or determinant primitivity, if a new proof mechanism can be constructed;
2. R1: literal-`p=2` Heegner-index parity by a mechanism independent of Kriz–Li `(F)`;
3. R2: exact WP00 twist-L-ratio valuation under the full WP09 splitting constraints;
4. D2a: fixed-`2` height nondegeneracy only if a genuinely new theorem interface or proof mechanism appears;
5. direct fixed-base R4 only if a theorem computes the base analytic leading-term valuation itself.

A successor must preserve exact normalization and every power of `2`.

## Claim firewall

Do not promote:

- `m_K(f)` to odd without proof;
- `lambda_D` to a `2`-adic unit or to any exact valuation without proof;
- auxiliary-field invariance of `R_2` to a numerical value of `R_2`;
- R4 reduction to R4 closure;
- R1, R2, R4, R5, D2a, D2d, or D2e to resolved without exact protected proof;
- computational evidence to theorem;
- source admission or CI success to MATHCERT certification;
- `BSD-R2-A1`, novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, exact computation, source admission when required, exact-head Adversary and Referee review, affected ordinary CI, protected merge/readback, issue #215/#164 maintenance, and handoff maintenance.

Recoverable connector, CI, logging, formatting, source-access, compiler, or computational failures are recovery events, not stopping conditions. Bind every review, run, job, artifact, and merge to the current exact head. Repairs require fresh exact-head replay.

Stop only at a genuine named theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target or normalization drift, or MATHCERT authority boundary.
