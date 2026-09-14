# BSD-R2-A1-WP56A — classical height/regulator descent

## Protected inputs

- MATHSOLVE protected base: `456656135cd425410d3b64d46d56d7702171f3b5`.
- MATHFORGE protected WP56 source admission: `6c2f7c8a9a1f646ad48eb1fd13eba845343bf6dd`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Selected claim: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

The package continues protected WP55A's exact identity

`L'(E,1)/(Omega_E Reg_E)
 = [2 A_E/(C_f^2 u_K^2 sqrt(|D_K|) Omega_E L(E^D,1))]
   * [hhat_K(P_K(f))/Reg_E]`.

Its task is only the second bracket.

## Result

Let `P` be a primitive generator of `E(Q)/E(Q)_tors`. Protected WP38 gives an exact isomorphism

`E(Q)/E(Q)_tors ->~ E(K)/E(K)_tors`.

Therefore there is a unique integer `m_K(f)`, up to simultaneous change of sign of the chosen generator, and torsion `T in E(K)_tors` such that

`P_K(f)=m_K(f) P + T`.

The integer is nonzero because protected WP09 has `L'(E/K,1) != 0` and the protected CST Gross–Zagier formula then forces the classical Heegner height to be nonzero.

Protected MATHFORGE WP56 gives the exact base-field convention conversion

`hhat_K(Q)=2 hhat_Q(Q)`

for the selected quadratic `K/Q` lane. The WP00 rank-one regulator is

`Reg_E=<P,P>_NT=hhat_Q(P)`.

Canonical-height quadraticity and torsion-insensitivity therefore give

`hhat_K(P_K(f))/Reg_E = 2 m_K(f)^2`.

Thus the complete protected WP55A identity becomes

`L'(E,1)/(Omega_E Reg_E)
 = 4 m_K(f)^2 A_E
   / (C_f^2 u_K^2 sqrt(|D_K|) Omega_E L(E^D,1))`.

No real scalar has been assigned a `2`-adic valuation merely by typography. The height/regulator factor itself, however, is now the ordinary integer `2 m_K(f)^2`, so its valuation is exactly

`1 + 2 ord_2(m_K(f))`.

## What this resolves

The ambiguity in the CST height-over-K versus WP00 regulator convention is closed exactly. Quadratic base change contributes no free-lattice index; the only remaining lattice datum in this factor is the genuine Heegner index `m_K(f)`.

## What remains open

WP56A does not determine `m_K(f)` or prove it odd. Protected WP10 already forbids a mechanical specialization of the screened odd-prime Heegner-primitivity chain to `p=2`.

The second WP55A scalar remains

`A_E/(C_f^2 u_K^2 sqrt(|D_K|) Omega_E L(E^D,1))`.

Its exact algebraic/rational normalization must be established before applying `ord_2` to it.

`BSD-R2-A1` remains unproved. D1c, D2a, D2e and MATHCERT certification remain open/outside this package.
