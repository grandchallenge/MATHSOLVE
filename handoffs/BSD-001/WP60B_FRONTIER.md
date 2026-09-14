# BSD-001 WP60B frontier — Kriz–Li normalization classified

## Entering protected state

- MATHSOLVE: `8b7ba4e5d888f68ffdaeab748d7d94d764f286fa`.
- MATHFORGE: `a8f72ed64755777870a300053e11659fb1dfff1b`.
- Tracker: `grandchallenge/MATHSOLVE#215`.
- Owner: `grandchallenge/MATHSOLVE#164`.
- Selected target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

## WP60B result

For the protected primitive generator `P`, set

`kappa_2(E,P):=((3-a_2)/2) log_{omega_E}(P)`.

WP60B proves:

1. `kappa_2(E,P) in Z_2`;
2. for the fixed WP58A parametrization,
   `KL_2(E,K,f)=u_f m_K(f) kappa_2(E,P)`
   with `u_f in Z_2^x`;
3. therefore
   `Kriz-Li (F)
    <=> [m_K(f) odd] AND [kappa_2(E,P) in Z_2^x]`;
4. the source Heegner point is indivisible by `2` exactly when `m_K(f)` is odd.

Disposition:

`MIXED_BUT_NO_INDEPENDENT_K_VARYING_ESCAPE`.

Kriz–Li `(F)` does not contain a second field-varying invariant that bypasses the Heegner-index parity. Its extra content is the fixed local scalar `kappa_2(E,P)`.

## Refined obligations

### KL-LOCAL

`MISSING_UNIFORM_KRIZ_LI_FIXED_LOCAL_LOG_UNIT`

Determine whether

`kappa_2(E,P) in Z_2^x`

holds uniformly on the selected class. This is a fixed local problem and can be attacked computationally without varying `K`.

### KL-INDEX

`MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`

Produce, uniformly for the selected class, a WP09-compatible field `K` with

`ord_2(m_K(f))=0`.

This is the genuine auxiliary-field problem.

## Effect on WP59 reopening form R3

R3 is not an independent escape from R1. A theorem forcing `(F)` for a WP09-compatible field would necessarily prove the `R1` parity component plus the fixed `KL-LOCAL` unit condition.

D2d therefore remains closed to routine replay.

## Immediate successor

Execute WP60C exact real-data reconnaissance on `KL-LOCAL` first:

1. select real curves satisfying the protected selected hypotheses;
2. use the protected primitive Mordell–Weil generator;
3. compute `a_2` and the exact finite precision needed to decide
   `kappa_2(E,P) mod 2`;
4. record deterministic machine-readable results;
5. use counterexamples, if any, to kill a uniform local-unit conjecture immediately;
6. do not infer a theorem from positive samples.

If exact computation infrastructure cannot evaluate the local logarithm directly, reduce the unit test to finite formal-group arithmetic modulo the minimum power of `2` needed and implement that finite criterion.

## Other live theorem boundaries

- `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.
- `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- `MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.
- `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION` downstream.

## Claim firewall

Do not promote `kappa_2` to a unit, `m_K(f)` to odd, R3 to resolved, D2d to reopened, `BSD-R2-A1`, or any MATHCERT claim without exact protected proof.
