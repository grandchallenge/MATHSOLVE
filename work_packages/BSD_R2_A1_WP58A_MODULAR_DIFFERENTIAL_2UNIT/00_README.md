# BSD-R2-A1-WP58A — modular-differential 2-unit control

## Protected inputs

- MATHSOLVE protected base: `200e3eeab4b3fb2b6fcfcde6b3ec2565879ed11e`.
- MATHFORGE protected WP58 source admission: `d588543151ddb458d627ac9b9fb37ec57cd90780`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Selected claim: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

Protected WP57A proves, for any source-compatible modular parametrization `f:X_0(N)->E`,

`L'(E,1)/(Omega_E Reg_E)
 = 2 m_K(f)^2 /(C_f^2 c_infinity(E^D) lambda_D)`

with

`lambda_D=L(E^D,1)/Omega(E^D) in Q^x`.

WP58A makes a permitted, explicit choice of `f` and proves that its modular-differential scalar has zero `2`-adic valuation.

## Result

Let `E_0` be the strong-Weil/optimal curve in the `Q`-isogeny class of the selected `E`. Protected MATHFORGE WP58 admits an optimal parametrization

`f_0:X_0(N)->E_0`

with exact positive Manin scalar one.

Choose a `Q`-isogeny

`psi:E_0->E`

of minimum degree among all such isogenies, and define

`f:=psi o f_0`.

Minimality forces `ker(psi)` to be cyclic. If `deg(psi)` were even, the dual isogeny `hat psi:E->E_0` would have cyclic even-order kernel and therefore a unique order-two subgroup stable under `G_Q`. This would give a rational `2`-isogeny out of `E`, contradicting the protected irreducibility (indeed surjectivity) of `E[2]`.

Hence `deg(psi)` is odd.

For minimal Néron differentials write

`psi^* omega_E = a_psi omega_0`,

`hat psi^* omega_0 = b_psi omega_E`.

Néron-model functoriality gives `a_psi,b_psi in Z\{0}`, and duality gives

`a_psi b_psi=deg(psi)`.

Thus `a_psi` is odd. Because the optimal Manin scalar is one,

`f^*omega_E = +/- a_psi 2*pi*i*phi(z)dz`,

so

`C_f=|a_psi|`

and therefore

`ord_2(C_f)=0`.

## Refined WP57A identity

For this fixed source-compatible parametrization,

`L'(E,1)/(Omega_E Reg_E)
 = 2 m_K(f)^2 /(c_infinity(E^D) lambda_D)`

on the `2`-adic valuation line, in the precise sense that the omitted `C_f^2` factor has valuation zero. Consequently

`ord_2(L'(E,1)/(Omega_E Reg_E))
 = 1 + 2 ord_2(m_K(f))
   - ord_2(c_infinity(E^D))
   - ord_2(lambda_D)`.

Thus

`delta_2(E)
 = 1 + 2 ord_2(m_K(f))
   - ord_2(c_infinity(E^D))
   - ord_2(lambda_D)
   - sum_{ell|N} ord_2(c_ell)`.

## Boundary after WP58A

The modular-differential contribution is resolved at `p=2`.

D2d narrows to

`MISSING_P2_HEEGNER_INDEX_AND_TWIST_LRATIO_VALUATION_CONTROL`.

The two substantive arithmetic residuals are now:

- `ord_2(m_K(f))`, for the explicitly chosen optimal-composite parametrization `f`;
- `ord_2(lambda_D)`.

The real-component factor is a finite explicit topological bit and the bad-prime Tamagawa valuations are already protected.

## Firewall

WP58A does not assert `C_f=1`; it proves only `ord_2(C_f)=0` for the chosen parametrization. It does not prove Heegner primitivity, evaluate `lambda_D`, assume rank-zero BSD for `E^D`, prove fixed-2 height nondegeneracy, close D1c or D2e, prove `BSD-R2-A1`, or certify anything in MATHCERT.
