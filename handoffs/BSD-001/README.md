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
8. `work_packages/BSD_R2_A1_WP18C_ANALYTIC_DELTA2/`;
9. protected WP06, WP07, WP09, WP12, WP13 and WP15 when composing the next uniform theorem step;
10. the current protected MATHFORGE BSD provider manifest and admitted source audits before any new external theorem/computation interface is used.

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

## WP18B — exact `Sel_2` computation and full tower consequence

WP18B is protected at MATHSOLVE

`6a9502b3a9e280b8593484f71cf4f21ff50eac97`.

The computation interface is protected in MATHFORGE at

`35837626ec887737f26f0acc5d9de48c5fd4db83`.

The exact computation ran on MATHSOLVE head

`c4a4fcc7339991becf7210f8978afb64e440ccdd`

with GitHub Actions run `34321076589`, job `102367621468`, SageMath `10.8`, and digest-pinned image

`sagemath/sagemath@sha256:e2e4747b0e1ea8753a9cb5a399314a8b2c25fcefaf69ba85b22ee075829d09ea`.

For both `53a1` and `203b1`, Sage/PARI, Sage/mwrank, and direct eclib all give

`dim_F2 Sel_2(E/Q)=1`,

hence

`#Sel_2(E/Q)=2`.

Rank one and odd torsion give `#E(Q)/2E(Q)=2`; the level-2 Kummer exact sequence therefore gives

`Sha(E/Q)[2]=0`.

Protected finiteness of Sha then forces

`Sha(E/Q)[2^infinity]=0`.

Consequently, for every `n>=1`,

`#Sel_{2^n}(E/Q)=2^n`,

`s_n(E)=0`,

`T_E=0`,

and

`Fitt^0_{Z_2}(T_E)=Z_2`.

This is an exact deduction, not numerical stabilization.

## WP18C — exact analytic `delta_2` and A/B atlas closure

The exact analytic source interface is protected in MATHFORGE at

`6b0bc6444bcf675c1b7774caa1f719efabdd49f6`.

Admitted source audit:

`sources/BSD-001/GJPST_RANK1_ANALYTIC_SHA_WP18C_SOURCE_AUDIT.md`.

The admitted GJPST theorem interface gives, for every rank-one elliptic curve over `Q` of conductor at most `1000`, the exact WP00-normalized identity

`#Sha(E)_an = 1`.

The source audit verifies exact concordance with WP00 for the finite Hasse-Weil `L`-function, whole-real-locus minimal-model period, Neron-Tate regulator, Tamagawa factors, and rational torsion-square denominator. The known Lawson-Wuthrich correction concerns a later odd-prime cohomology/Kolyvagin argument and is outside this admitted interface.

For rank one, the admitted identity is

`1 = L'(E,1) * (#E(Q)_tors)^2 / (Omega_E Reg_E product_{ell|N} c_ell)`.

Both controls have trivial rational torsion. Therefore

`ord_2(L'(E,1)/(Omega_E Reg_E)) = sum_{ell|N} ord_2(c_ell)`.

Hence WP18C proves exactly

`delta_2(53a1)=0`,

with analytic leading-quotient valuation `0`, and

`delta_2(203b1)=0`,

with analytic leading-quotient valuation `1` cancelling the exact Tamagawa valuation `1`.

Combining only with protected WP18B gives the individual-control equalities

`delta_2(53a1)=v_2(Fitt^0_{Z_2}(T_53a1))=0`,

`delta_2(203b1)=v_2(Fitt^0_{Z_2}(T_203b1))=0`.

Thus the minimal WP18 A/B diagnostic atlas is mathematically closed at the exact level. The regime-B even-Tamagawa/residual-conductor-drop correction is present on the analytic side and cancels exactly on `203b1`.

This does not prove the selected-class theorem and does not constitute MATHCERT certification.

## Exact local-condition contract

The governing invariant remains the primitive classical Kummer condition at every place and finite level:

`im(E(Q_v)/2^n E(Q_v) -> H^1(Q_v,E[2^n]))`.

The following substitutions remain forbidden without an exact comparison theorem:

- Kummer at `2` -> Greenberg/ordinary connected-etale;
- primitive bad-prime Kummer -> unramified/strict/relaxed/imprimitive;
- saturated rank-one quotient -> span of a possibly nonprimitive generator;
- `Fitt^0(T_E)` -> `Fitt^0(X_E)`.

Every finite kernel, cokernel, index, determinant, Tamagawa factor, or local correction must retain its complete `2`-adic length.

## Active frontier after WP18

The diagnostic atlas no longer carries an open evidentiary boundary. The active substantive frontier returns to the uniform theorem problem:

`BSD-R2-A1-S3-K-INTEGRAL-FITTING-CONTROL`.

Surviving provider/theorem debt:

`P2_GOOD_ORDINARY_IRREDUCIBLE_S3_EXACT_MU_OR_PRIMITIVE_FITTING_CONTROL`.

The exact remaining mathematical task is to prove uniformly over the protected selected class

`delta_2(E)=v_2(Fitt^0_{Z_2}(T_E))`

without bounded-conductor individual verification.

## Immediate next executable tranche

Do not continue adding individual atlas controls merely for volume. WP18 has already separated the normalization issue from the genuine theorem debt.

The next tranche must target the surviving uniform defect directly. Preferred order:

1. use the protected WP09 auxiliary field `K`, WP06 discrepancy accounting, WP07 local-at-2 correction surface, and WP16B primitive Fitting invariant to state the narrowest exact integral control theorem that would close the selected class;
2. identify the precise missing implication at the height-one prime `(2)` / relative-mu or primitive Fitting level;
3. screen or derive only theorem interfaces that act on the selected good-ordinary, irreducible/surjective `E[2] ~= S3` branch;
4. route every genuinely new external theorem premise through MATHFORGE before use;
5. reject results that are only odd-prime, reducible-residual, supersingular, imprimitive, or valid only after inverting `2` unless an exact comparison theorem removes the discrepancy.

The governing boundary is the theorem debt itself:

`MISSING_UNIFORM_P2_PRIMITIVE_FITTING_CONTROL_ON_GOOD_ORDINARY_S3_BRANCH`.

This is a substantive theorem/source boundary, not evidence that the theorem does not exist.

## Claim firewall

- `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED` remains unchanged.
- WP18C proves individual-control equalities only.
- GJPST analytic `#Sha_an` is not treated as arithmetic Sha evidence.
- WP18B remains the independent arithmetic proof for the controls.
- No floating-point recognition is used as standalone exactness evidence.
- Two examples do not establish uniform selected-class Fitting control.
- “Up to a unit” may not hide a power of `2`.
- Kummer and Greenberg local conditions remain distinct until exactly compared.
- Source admission is not MATHCERT certification.
- No novelty, priority, patentability, or commercial claim follows.

## Execution and continuity

Proceed autonomously through bounded proof, falsification, exact-source admission when needed, exact-head non-authoring/read-only Adversary and Referee review, affected CI, protected merge, protected readback, and issue/handoff maintenance.

Recoverable tooling, connector, CI, formatting, logging, source-access, or computational-environment failures are not stopping conditions. Apply the recovery ladder.

Stop only for a genuine theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target or normalization drift, or MATHCERT certification authority. Before stopping, name the exact boundary.
