# BSD-001 frontier after WP58A

## Protected anchors

- MATHSOLVE pre-WP58A protected head: `200e3eeab4b3fb2b6fcfcde6b3ec2565879ed11e`.
- MATHFORGE WP58 protected source head: `d588543151ddb458d627ac9b9fb37ec57cd90780`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.

This frontier becomes authoritative only after the containing WP58A candidate is protected and read back from `main`.

## WP58A result

Protected WP57A proves, for any source-compatible modular parametrization `f:X_0(N)->E`,

`L'(E,1)/(Omega_E Reg_E)
 = 2 m_K(f)^2 /(C_f^2 c_infinity(E^D) lambda_D)`

with

`lambda_D=L(E^D,1)/Omega(E^D) in Q^x`.

Let `E_0` be the optimal curve in the selected `Q`-isogeny class. Protected MATHFORGE WP58 admits Česnavičius's semistable optimal Manin theorem, so an optimal parametrization

`f_0:X_0(N)->E_0`

has positive Manin scalar exactly one.

Choose a minimum-degree `Q`-isogeny

`psi:E_0->E`

and set `f=psi o f_0`.

WP58A proves:

1. minimum degree forces `ker(psi)` cyclic;
2. if `deg(psi)` were even, the cyclic kernel of the dual isogeny `hat psi:E->E_0` would contain a unique Galois-stable order-two subgroup, contradicting protected irreducibility of `E[2]`;
3. therefore `deg(psi)` is odd;
4. for Néron differentials, `psi^*omega_E=a_psi omega_0` and `hat psi^*omega_0=b_psi omega_E` with `a_psi b_psi=deg(psi)`, hence `a_psi` is odd;
5. the composite parametrization has `C_f=|a_psi|`, so

   `ord_2(C_f)=0`.

Thus, for this fixed source-compatible parametrization,

`ord_2(L'(E,1)/(Omega_E Reg_E))
 = 1 + 2 ord_2(m_K(f))
   - ord_2(c_infinity(E^D))
   - ord_2(lambda_D)`

and

`delta_2(E)
 = 1 + 2 ord_2(m_K(f))
   - ord_2(c_infinity(E^D))
   - ord_2(lambda_D)
   - sum_{ell|N} ord_2(c_ell)`.

No assertion `C_f=1` is made; only its `2`-adic valuation is resolved.

## D2d disposition

D2d narrows to

`MISSING_P2_HEEGNER_INDEX_AND_TWIST_LRATIO_VALUATION_CONTROL`.

The two remaining substantive arithmetic quantities are:

1. `ord_2(m_K(f))` for the fixed optimal-composite parametrization;
2. `ord_2(lambda_D)` for `lambda_D=L(E^D,1)/Omega(E^D)`.

The term `ord_2(c_infinity(E^D))` is an explicit real-topology bit. The odd-bad-prime Tamagawa valuations are already protected.

## Narrow executable successors

### WP59A — twist L-ratio valuation

Determine `ord_2(lambda_D)` at literal `p=2` without substituting rank-zero BSD. Prefer an exact modular-symbol or integral rank-zero arithmetic theorem. A result only after inverting `2`, or only up to an unspecified `2`-unit, is insufficient.

The current auxiliary-field freedom may be used only within the protected WP09 local splitting/nonvanishing constraints. If a new theorem guarantees a twist with controlled mod-2 algebraic L-value under those simultaneous local conditions, admit it through MATHFORGE before use.

### WP59B — Heegner-index valuation

Determine `ord_2(m_K(f))` for the fixed optimal-composite parametrization. Protected WP10 remains a firewall against mechanically specializing the standard odd-prime rank-lowering/primitivity chain to `p=2`.

### Parallel D1c lane

Continue only the narrow literal-`p=2`, height-one-`(2)` analytic determinant-generator search. Do not reopen broad odd-prime reconnaissance.

## Other live boundaries

- D1c: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.
- D2a: `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2b: `RESOLVED_WP52A_FINITE_COMPARISON_DETERMINANT`.
- D2c: `RESOLVED_WP54A_GLOBAL_QORD_RECONCILIATION`.
- D2e: `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.
- `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

No rank-zero BSD theorem, MATHCERT certification, novelty, priority, patentability, or commercial claim is promoted.
