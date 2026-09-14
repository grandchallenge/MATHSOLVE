# BSD-001 canonical continuation handoff

## Authority and claim state

- Campaign: `BSD-001 — Birch-Swinnerton-Dyer selected rank-one 2-primary campaign`.
- Mathematical repository: `grandchallenge/MATHSOLVE`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Active WP60 execution tracker: `grandchallenge/MATHSOLVE#215`.
- External source authority: `grandchallenge/MATHFORGE`.
- Constitutional authority: protected `grandchallenge/INTELLECT`.
- Certification authority: `grandchallenge/MATHCERT` only.
- Selected target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

Use protected repository state as authority. Do not use mutable issues, conversation history, stale summaries, numerical evidence, or odd-prime theorems as substitute authority.

## Canonical read order

After re-fetching protected live heads, read:

1. this file;
2. `handoffs/BSD-001/WP60B_FRONTIER.md`;
3. `work_packages/BSD_R2_A1_WP60B_KRIZ_LI_TRANSPORT/00_README.md`;
4. `work_packages/BSD_R2_A1_WP60B_KRIZ_LI_TRANSPORT/01_KRIZ_LI_TRANSPORT_THEOREM.md`;
5. `work_packages/BSD_R2_A1_WP60B_KRIZ_LI_TRANSPORT/02_CLAIM_LEDGER.yaml`;
6. protected WP60A-A1 when the height-one-`(2)` determinant lane is needed;
7. `work_packages/BSD_R2_A1_WP60_P2_FRONTIER_RESEARCH_PROGRAM/01_EXECUTION_CONTRACT.md`;
8. protected MATHFORGE WP60B/WP60A/WP59 source records;
9. only then deeper protected predecessors required by the active lane.

## Governing invariant

For the selected rank-one class,

`delta_2(E)
 := ord_2(L'(E,1)/(Omega_E Reg_E))
    - sum_{ell|N} ord_2(c_ell)`.

Protected WP16A/WP16B/WP19 give

`v_2(Fitt^1_{Z_2}(X_E))
 = len_Z2 Sha(E/Q)[2^infinity]
 = lim_n(ord_2 #Sel_{2^n}(E/Q)-n)`.

The selected theorem is exactly

`delta_2(E)=v_2(Fitt^1_{Z_2}(X_E))`.

## Protected arithmetic reduction

Protected WP55A–WP58A give, for the fixed source-compatible parametrization,

`delta_2(E)
 = 1 + 2 ord_2(m_K(f))
   - ord_2(c_infinity(E^D))
   - ord_2(lambda_D)
   - sum_{ell|N}ord_2(c_ell)`,

where

`lambda_D=L(E^D,1)/Omega(E^D) in Q^x`

and

`ord_2(C_f)=0`.

Protected WP59 isolates

`R_2(E,K,f)=2ord_2(m_K(f))-ord_2(lambda_D)`

and records the bounded D2d source boundary.

## WP60A protected result

WP60A-A0 fixes all finite algebraic determinant/control factors. WP60A-A1 proves that, for a two-term perfect complex over a DVR with rank-one `H^1` and finite `H^2`, the inverse determinant line maps to

`Fitt^0(H^2) H^1`.

Thus a literal-`p=2` determinant lift of the fixed Kato class at the height-one prime `(2)` is exactly the missing one-sided Fitting divisibility, while determinant primitivity is equality.

Current WP60A boundaries:

- `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`;
- `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

Do not cycle through alternative determinant formalisms without new arithmetic input.

## WP60B exact Kriz–Li transport

Protected MATHFORGE WP60B admits the exact literal-`2` source condition for the same modular parametrization:

`((3-a_2)/2) log_{omega_f^KL}(P_KL(f)) != 0 mod 2`,

with

`f^*omega_f^KL=phi(q)dq/q`.

Protected WP58A gives

`f^*omega_E=+/- C_f phi(q)dq/q`,

so

`omega_f^KL=+/- C_f^(-1)omega_E`

with `C_f in Z_2^x`.

For the protected primitive generator `P`, define

`kappa_2(E,P):=((3-a_2)/2)log_{omega_E}(P)`.

WP60B proves

`kappa_2(E,P) in Z_2`

and the exact factorization

`KL_2(E,K,f)=u_f m_K(f) kappa_2(E,P)`,

where `u_f in Z_2^x`.

Therefore

`Kriz-Li (F)
 <=> [m_K(f) odd] AND [kappa_2(E,P) in Z_2^x]`.

The source Heegner point is indivisible by `2` exactly when `m_K(f)` is odd.

### WP60B disposition

`MIXED_BUT_NO_INDEPENDENT_K_VARYING_ESCAPE`.

The condition contains no second `K`-varying invariant that bypasses the Heegner-index parity. Its additional content is the fixed selected-curve local scalar `kappa_2(E,P)`.

## Refined live obligations

### KL-LOCAL

`MISSING_UNIFORM_KRIZ_LI_FIXED_LOCAL_LOG_UNIT`.

Determine whether

`kappa_2(E,P) in Z_2^x`

holds uniformly, or classify its failure exactly.

### KL-INDEX

`MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.

Produce a WP09-compatible auxiliary field with

`ord_2(m_K(f))=0`

uniformly for the selected class.

### D1c

- `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`;
- `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

### D2a

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

### D2d

`MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.

### D2e

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

D2e remains downstream.

## Effect on WP59 reopening form R3

R3 is not independent of R1. Any theorem forcing Kriz–Li `(F)` for a WP09-compatible field necessarily proves both the fixed `KL-LOCAL` unit condition and the `R1` Heegner-index parity for that field.

WP60B therefore does not itself reopen D2d.

## Immediate executable successor — WP60C

Run exact real-data reconnaissance on `KL-LOCAL` before another theorem search.

Required sequence:

1. use only real curves satisfying the protected selected hypotheses;
2. use the actual primitive Mordell–Weil generator;
3. reduce the unit test for
   `kappa_2(E,P)`
   to exact finite `2`-adic/formal-group arithmetic;
4. record deterministic machine-readable inputs and outputs;
5. treat a counterexample as decisive falsification of uniform `KL-LOCAL` unitness;
6. treat positive samples only as evidence for a sharper theorem target, never as proof.

Protected WP36 already provides finite exact formal-group infrastructure at `2`; reuse it where possible rather than introducing dummy data or floating-point approximations.

If WP60C falsifies uniform local unitness, record the exact counterexample and terminate that conjecture. If it survives a broad exact sample, identify the minimum finite local invariant controlling the unit condition and pursue a proof of that invariant.

## Claim firewall

Do not promote:

- `kappa_2(E,P)` to a unit without proof;
- `m_K(f)` to odd without proof;
- Kriz–Li `(F)` to a uniform selected-class fact;
- WP59 R1/R3/R4/R5 or D2d to resolved;
- `lambda_D` to a `2`-adic unit;
- determinant membership to determinant primitivity;
- computational evidence to theorem;
- source admission or CI success to MATHCERT certification;
- `BSD-R2-A1`, novelty, priority, patentability, or commercial claims.

## Execution doctrine

Proceed autonomously through bounded proof, falsification, exact computation, source admission when required, exact-head Adversary and Referee review, affected ordinary CI, protected merge, protected readback, issue #215/#164 maintenance, and handoff maintenance.

Recoverable connector, CI, formatting, source-access, compiler, Sage/PARI, logging, or computational failures are recovery events, not stopping conditions.

Bind every review, run, job, artifact, and merge to the current exact head. Repairs require fresh exact-head replay.

Stop only at a genuine named theorem/source/authority/authentication/safety/material-state/evidentiary boundary, target/normalization drift, or MATHCERT certification authority.
