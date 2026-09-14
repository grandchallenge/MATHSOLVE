# BSD-001 frontier after WP57A

## Protected anchors

- MATHSOLVE pre-WP57A protected head: `ae694de9c18c6c2ff3e46002bc8ed008f7b4fb01`.
- MATHFORGE WP57 protected source head: `ed91d13e13ec3577493548466b1411fc70b2693d`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.

This frontier becomes authoritative only after the containing WP57A candidate is protected and read back from `main`.

## WP57A result

Protected WP56A gave

`L'(E,1)/(Omega_E Reg_E)
 = 4 m_K(f)^2 A_E
   /(C_f^2 u_K^2 sqrt(|D_K|) Omega_E L(E^D,1))`.

WP57A proves the exact complex-torus identity

`A_E=Omega_E |Omega_E^-|/2`.

Protected MATHFORGE WP57 gives, with the selected-lane Pal correction exactly equal to one,

`Omega(E^D)=c_infinity(E^D)|Omega_E^-|/sqrt(|D_K|)`

and admits

`lambda_D:=L(E^D,1)/Omega(E^D) in Q^x`.

The protected 2-split auxiliary field has `u_K=1`, and the admitted CST differential scalar `C_f` is a positive integer. Therefore

`L'(E,1)/(Omega_E Reg_E)
 = 2 m_K(f)^2
   /(C_f^2 c_infinity(E^D) lambda_D)`

exactly in `Q^x`, so

`ord_2(L'(E,1)/(Omega_E Reg_E))
 = 1 + 2 ord_2(m_K(f))
   - 2 ord_2(C_f)
   - ord_2(c_infinity(E^D))
   - ord_2(lambda_D)`.

Consequently

`delta_2(E)
 = 1 + 2 ord_2(m_K(f))
   - 2 ord_2(C_f)
   - ord_2(c_infinity(E^D))
   - ord_2(lambda_D)
   - sum_{ell|N} ord_2(c_ell)`.

No rank-zero BSD formula for `E^D` enters this reduction.

## D2d disposition

D2d is narrowed to

`MISSING_P2_HEEGNER_INDEX_MODULAR_DIFFERENTIAL_AND_TWIST_LRATIO_VALUATION_CONTROL`.

The remaining arithmetic unknowns are:

1. `ord_2(m_K(f))` — genuine literal-p=2 Heegner index/primitivity data;
2. `ord_2(C_f)` — the exact modular-differential/Manin scalar contribution;
3. `ord_2(lambda_D)` — the rank-zero twist's rational modular-symbol quotient, without assuming its BSD evaluation.

The topological term `ord_2(c_infinity(E^D))` is explicit once the real connectedness of the twist is fixed. The bad-prime Tamagawa term is already in the protected local ledger.

## Narrow executable successors

### WP58A — modular-differential 2-unit control

Determine whether `ord_2(C_f)=0` on the protected selected branch.

The preferred route is exact isogeny-class transport:

1. pass from the optimal strong-Weil parametrization to the selected curve;
2. use the protected irreducible/surjective `E[2]` hypothesis to rule out every even-degree rational isogeny in the isogeny class;
3. retain the optimal Manin constant theorem with its exact semistable hypotheses;
4. prove that every remaining differential-scaling factor has odd degree, hence contributes no power of `2`.

Any external theorem asserting the optimal Manin constant must be admitted through MATHFORGE before use. Do not set `C_f=1` by convention.

### WP58B — rank-zero twist L-ratio valuation

Determine `ord_2(lambda_D)` at literal `p=2` without assuming rank-zero BSD. Candidate routes must be source-sharp: modular symbols, p=2 Euler/Kolyvagin systems, or exact rank-zero Fitting/finite-Selmer control. If a theorem only determines the ratio up to a 2-unit or after inverting 2, it is insufficient.

### H1 — Heegner index

Continue the literal-p=2 Heegner-index lane independently. Protected WP10 remains a firewall against mechanically specializing odd-prime primitivity results.

## Other live boundaries

- D1c: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.
- D2a: `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2b: `RESOLVED_WP52A_FINITE_COMPARISON_DETERMINANT`.
- D2c: `RESOLVED_WP54A_GLOBAL_QORD_RECONCILIATION`.
- D2e: `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.
- `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

No MATHCERT certification, novelty, priority, patentability, or commercial claim is promoted.
