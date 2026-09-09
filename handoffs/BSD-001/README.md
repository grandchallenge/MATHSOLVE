# BSD-001 native continuation handoff

## Target repository and authority

- Target repository: `grandchallenge/MATHSOLVE`.
- Current programme owner: `grandchallenge/MATHSOLVE#164`.
- Constitutional authority remains the protected GCL authority chain already bound by the campaign.
- Source/provider admission remains MATHFORGE-owned.
- Mathematical certification remains MATHCERT-only.
- `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

Do not treat mutable issue text or conversational history as mathematical authority.

## Canonical continuation files

Read in this order after re-fetching protected live state:

1. `handoffs/BSD-001/README.md`;
2. `handoffs/BSD-001/RESEARCH_PLAN_WP16_WP18.md`;
3. `handoffs/BSD-001/TAKEOVER_PROMPT_WP16_WP18.md`;
4. `work_packages/BSD_R2_A1_WP16A_FINITE_SELMER_STABILIZATION/`;
5. `work_packages/BSD_R2_A1_WP16B_INTEGRAL_SELMER_FITTING/`;
6. `work_packages/BSD_R2_A1_WP18A_RECON_COHORT/`;
7. `work_packages/BSD_R2_A1_WP18B_SELMER2/`;
8. protected WP06, WP07, WP09, WP12, WP13 and WP15 when composing the next theorem step;
9. the current protected MATHFORGE BSD provider manifest and admitted source audits before any new external theorem/computation interface is used.

## Protected mathematical chain

- WP05 fixes the target/source interfaces, supplies rank one and finite Sha, and proves odd rational torsion.
- WP06 records every quadratic `p=2` descent discrepancy and forbids identifying finite Kummer and Greenberg ordinary local conditions at `2` without proof.
- WP07 fixes the good-ordinary local-at-2 correction surface.
- WP08 isolates the cyclotomic height-one `(2)` / relative-mu defect.
- WP09 supplies the protected auxiliary imaginary quadratic field `K` and the admitted nonvanishing / p-adic Gross-Zagier interfaces.
- WP10 closes the mechanical odd-prime Heegner-primitivity route.
- WP11 gives conditional `C3` control; WP12 eliminates `C3`, leaving residual image `GL_2(F_2) ~= S3`.
- WP13 proves the exact Tamagawa/inertia-depth dictionary and identifies residual-conductor drop with even-Tamagawa support.
- WP14 closes Chao Li applicability.
- WP15 proves finite Sha has square order and that parity/modulo-square information does not determine the unsquared length.
- WP16A proves for every `n>=1`

  `#Sel_{2^n}(E/Q) = 2^n #Sha(E/Q)[2^n]`,

  `s_n(E) := ord_2 #Sel_{2^n}(E/Q) - n = ord_2 #Sha(E/Q)[2^n]`,

  and

  `lim_n s_n(E) = len_Z2 Sha(E/Q)[2^infinity]`.

- WP16B fixes the primitive integral invariant. With

  `X_E := Sel_{2^infinity}^{Kum}(E/Q)^vee`,

  `L_E := (E(Q) tensor (Q_2/Z_2))^vee`,

  `T_E := Tor_{Z_2}(X_E)`,

  it proves

  `T_E = Sha(E/Q)[2^infinity]^vee`,

  `len_Z2 T_E = lim_n s_n(E)`,

  and

  `Fitt^0_{Z_2}(T_E) = 2^{lim_n s_n(E)} Z_2`.

Thus the selected unresolved equality is exactly

`delta_2(E) = v_2(Fitt^0_{Z_2}(T_E))`,

where

`delta_2(E) := ord_2(L'(E,1)/(Omega_E Reg_E)) - sum_{ell|N} ord_2(c_ell)`.

## WP17 source result

MATHFORGE WP17A-WP17C are protected. Their bounded source diagnosis does not assert theorem nonexistence.

The surviving uniform provider debt is

`P2_GOOD_ORDINARY_IRREDUCIBLE_S3_EXACT_MU_OR_PRIMITIVE_FITTING_CONTROL`.

Do not reopen broad generic literature reconnaissance unless a new theorem specifically addresses this debt.

## WP18A — verified A/B cohort

WP18A is protected at MATHSOLVE

`6d44e401e584498992c78f053992bde1dcba2452`.

### Regime A control: `53a1`

- minimal model `[1,-1,1,0,0]`;
- conductor `53`;
- rank one; trivial rational torsion;
- `Delta_min=-53`;
- `a_2=-1`, hence good ordinary at `2`;
- protected WP13: `ord_2(c_53)=0`, residual conductor `53`.

### Regime B control: `203b1`

- minimal model `[1,1,1,0,-2]`;
- conductor `203=7*29`;
- rank one; trivial rational torsion;
- `Delta_min=-7^2*29`;
- `a_2=-1`, hence good ordinary at `2`;
- protected WP13: `ord_2(c_7)=1`, `ord_2(c_29)=0`, even-Tamagawa support `{7}`, residual conductor `29`.

Protected WP12 supplies residual surjectivity for both controls.

The legacy compact Cremona BSD `rational factor` column is not a Tamagawa product. WP18A records and rejects that earlier exploratory misreading.

## WP18B — exact `Sel_2` computation and full tower consequence

The computation interface is protected in MATHFORGE at

`35837626ec887737f26f0acc5d9de48c5fd4db83`.

The exact computation ran on MATHSOLVE head

`c4a4fcc7339991becf7210f8978afb64e440ccdd`

with GitHub Actions run `34321076589`, job `102367621468`, SageMath `10.8`, and digest-pinned image

`sagemath/sagemath@sha256:e2e4747b0e1ea8753a9cb5a399314a8b2c25fcefaf69ba85b22ee075829d09ea`.

For **both** `53a1` and `203b1`, three interfaces agree:

- Sage/PARI `selmer_rank = 1`;
- Sage/mwrank `selmer_rank = 1`;
- direct eclib `selmer_rank = 1`.

Hence for each curve

`#Sel_2(E/Q)=2`.

Rank one and odd torsion give `#E(Q)/2E(Q)=2`; the level-2 Kummer exact sequence therefore gives

`Sha(E/Q)[2]=0`.

Protected finiteness of Sha then forces

`Sha(E/Q)[2^infinity]=0`.

Consequently, for every `n>=1`,

`#Sel_{2^n}(E/Q)=2^n`,

`s_n(E)=0`,

and protected WP16B gives

`T_E=0`,

`Fitt^0_{Z_2}(T_E)=Z_2`.

This is an exact deduction, not numerical stabilization. No 4- or 8-descent is needed once the level-2 result and finite-Sha input are fixed.

The specialized selected equality for either atlas control is therefore equivalent to

`delta_2(E)=0`.

WP18B proves the arithmetic side of that specialized equality. It does not prove the analytic side and does not prove `BSD-R2-A1`.

## Exact local-condition contract

The governing invariant remains the primitive classical Kummer condition at every place and finite level:

`im(E(Q_v)/2^n E(Q_v) -> H^1(Q_v,E[2^n]))`.

The following substitutions remain forbidden without an exact comparison theorem:

- Kummer at `2` -> Greenberg/ordinary connected-etale;
- primitive bad-prime Kummer -> unramified/strict/relaxed/imprimitive;
- saturated rank-one quotient -> span of a possibly nonprimitive generator;
- `Fitt^0(T_E)` -> `Fitt^0(X_E)`.

Every finite kernel, cokernel, index, determinant, Tamagawa factor, or local correction must retain its complete `2`-adic length.

## Current frontiers

### Uniform theorem frontier

`BSD-R2-A1-S3-K-INTEGRAL-FITTING-CONTROL`

with provider debt

`P2_GOOD_ORDINARY_IRREDUCIBLE_S3_EXACT_MU_OR_PRIMITIVE_FITTING_CONTROL`.

This remains the substantive route toward the selected-class theorem.

### Diagnostic atlas frontier

`BSD-R2-A1-WP18C-ANALYTIC-DELTA2-NORMALIZATION`.

Named evidentiary boundary:

`MISSING_EXACT_NORMALIZED_DELTA2_ON_VERIFIED_A_B_COHORT`.

This boundary is now purely analytic for the two controls because their arithmetic/Fitting side is exactly zero/unit.

## Immediate next executable tranche — WP18C

For `53a1` and `203b1`, compute or rigorously bound under the fixed WP00 normalization

`ord_2(L'(E,1)/(Omega_E Reg_E))`

strongly enough to determine the exact integer

`delta_2(E)`.

Requirements:

1. preserve the exact WP00 period/derivative/regulator normalization;
2. source-audit any analytic computation interface before governed use;
3. retain enough precision or rigorous enclosure to determine the exact `2`-adic valuation rather than recognize a decimal heuristically;
4. subtract the protected WP13 Tamagawa valuations exactly;
5. report `epsilon(E)=delta_2(E)-0` only as atlas evidence unless independently proved;
6. do not use database analytic Sha or the BSD formula to infer the answer.

The expected diagnostic question is whether the analytic side also gives `delta_2(E)=0` in both regimes.

## Claim firewall

- `BSD-R2-A1` remains unproved.
- WP18B is exact for the two controls, not uniform selected-class Fitting control.
- No analytic Sha value is finite-Selmer evidence.
- No BSD leading-term identity is assumed.
- Numerical agreement is not proof or certification.
- “Up to a unit” may not hide a power of `2`.
- Kummer and Greenberg local conditions remain distinct until exactly compared.
- Source admission is not MATHCERT certification.
- No novelty, priority, patentability, or commercial claim follows.

## Execution and continuity

Proceed autonomously through bounded proof, computation, falsification, exact-source admission when needed, exact-head non-authoring/read-only Adversary and Referee review, affected CI, protected merge, protected readback, and issue/handoff maintenance.

Recoverable tooling, connector, CI, formatting, logging, source-access, or computational-environment failures are not stopping conditions. Apply the recovery ladder.

Stop only for a genuine theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target or normalization drift, or MATHCERT certification authority. Before stopping, name the exact boundary.
