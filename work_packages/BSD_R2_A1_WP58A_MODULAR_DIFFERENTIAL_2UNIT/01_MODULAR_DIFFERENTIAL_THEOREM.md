# WP58A theorem — selected modular-differential scalar is a 2-unit

## 1. Setup

Let `E/Q` lie in the protected selected `BSD-R2-A1` class. In particular:

- `E` is semistable of squarefree conductor `N`;
- the residual representation

  `rho_bar_{E,2}:G_Q->GL_2(F_2)`

  is irreducible and, by protected WP12, surjective;
- protected WP57A has placed the analytic quotient on the exact rational line

  `L'(E,1)/(Omega_E Reg_E)
   = 2 m_K(f)^2 /(C_f^2 c_infinity(E^D) lambda_D)`

  for every source-compatible modular parametrization `f:X_0(N)->E`.

Let `E_0/Q` denote the new elliptic optimal quotient in the isogeny class of `E`.

Protected MATHFORGE WP58 admits Česnavičius's semistable Manin theorem. Hence there is an optimal modular parametrization

`f_0:X_0(N)->E_0`

and a minimal Néron differential `omega_0` such that

`(1)
 f_0^*omega_0 = +/- 2*pi*i*phi(z)dz`.

Thus the positive optimal Manin scalar is exactly one, including at `p=2`.

## 2. Minimum-degree isogeny has cyclic kernel

Choose a `Q`-isogeny

`psi:E_0->E`

of minimum positive degree among all `Q`-isogenies from `E_0` to `E`.

### Lemma `BSD-A1-WP58-CYCLIC-001`

`ker(psi)` is cyclic as a finite subgroup of `E_0(Qbar)`.

### Proof

Any finite subgroup of an elliptic curve over characteristic zero has abstract structure

`Z/aZ x Z/bZ`

with `a|b`. If `a>1`, then the subgroup contains the full `a`-torsion `E_0[a]`: both groups have order `a^2`, and the two invariant factors supply two independent points of exact `a`-power structure. Equivalently, the noncyclic common divisor in the invariant factors is precisely a multiplication-by-`a` factor.

Since `ker(psi)` is Galois stable, the isogeny then factors as

`E_0 --[a]--> E_0 --psi'--> E`

with

`deg(psi')=deg(psi)/a^2 < deg(psi)`,

contradicting minimality. Hence `a=1` and the kernel is cyclic. QED.

A more intrinsic formulation is that every isogeny factors as multiplication by the largest full torsion subgroup contained in its kernel followed by a cyclic isogeny; minimum degree removes the multiplication factor.

## 3. The degree is odd

Let

`hat psi:E->E_0`

be the dual isogeny. Since `ker(psi)` is cyclic, `ker(hat psi)` is cyclic of the same order `deg(psi)`.

### Lemma `BSD-A1-WP58-ODD-ISOGENY-001`

`deg(psi)` is odd.

### Proof

Assume `2|deg(psi)`. A cyclic finite group of even order has a unique subgroup of order two. Because `ker(hat psi)` is defined over `Q`, the absolute Galois group preserves the kernel; uniqueness forces it to preserve its order-two subgroup.

That subgroup lies in `E[2]` and is a one-dimensional `F_2`-subspace stable under `G_Q`. Hence `E[2]` is reducible as an `F_2[G_Q]`-module.

This contradicts the protected selected residual hypothesis. Therefore `deg(psi)` is odd. QED.

Notice that this argument uses irreducibility only on the selected curve `E`; no residual claim about the optimal curve `E_0` is needed.

## 4. Néron-differential transport

Let `omega_E` be the protected WP00 minimal Néron differential on `E`. Since isogenies of elliptic curves over `Q` extend uniquely to morphisms of Néron models over `Z`, pullback preserves global invariant differentials. The rank-one modules of invariant Néron differentials therefore give nonzero integers `a_psi,b_psi` with

`(2)
 psi^*omega_E = a_psi omega_0`,

`(3)
 hat psi^*omega_0 = b_psi omega_E`.

The dual-isogeny identity

`hat psi o psi = [deg(psi)]`

implies on invariant differentials

`a_psi b_psi = deg(psi)`

up to the harmless simultaneous sign convention; in absolute value,

`(4)
 |a_psi| |b_psi| = deg(psi)`.

Since the right-hand side is odd, both `a_psi` and `b_psi` are odd.

### Lemma `BSD-A1-WP58-DIFF-001`

`ord_2(a_psi)=0`.

QED.

## 5. Choice of the CST parametrization

Define

`f:=psi o f_0:X_0(N)->E`.

This is a modular parametrization sending the cusp at infinity to the identity and is therefore admissible in the protected Cai–Shu–Tian/WP55–WP57 chain.

Using (1) and (2),

`f^*omega_E
 = f_0^*(psi^*omega_E)
 = +/- a_psi 2*pi*i*phi(z)dz`.

The positive CST scalar for this parametrization is therefore

`C_f=|a_psi|`.

### Theorem `BSD-A1-WP58-CF-2UNIT-001`

For the explicitly chosen optimal-composite parametrization `f=psi o f_0`,

`ord_2(C_f)=0`.

This theorem does not claim `C_f=1`. Odd factors coming from the isogeny from the optimal curve to the selected curve may remain.

## 6. Consequence for the protected rational identity

Protected WP57A gives

`L'(E,1)/(Omega_E Reg_E)
 = 2 m_K(f)^2 /(C_f^2 c_infinity(E^D) lambda_D)`.

Applying `ord_2` and Theorem `CF-2UNIT-001` gives

### Corollary `BSD-A1-WP58-DELTA-REDUCTION-001`

`ord_2(L'(E,1)/(Omega_E Reg_E))
 = 1 + 2 ord_2(m_K(f))
   - ord_2(c_infinity(E^D))
   - ord_2(lambda_D)`.

Hence

`delta_2(E)
 = 1 + 2 ord_2(m_K(f))
   - ord_2(c_infinity(E^D))
   - ord_2(lambda_D)
   - sum_{ell|N} ord_2(c_ell)`.

The modular-differential scalar has disappeared only at the level of `2`-adic valuation, by an exact oddness proof. It has not been set equal to one.

## 7. Exact remaining D2d boundary

The previous boundary

`MISSING_P2_HEEGNER_INDEX_MODULAR_DIFFERENTIAL_AND_TWIST_LRATIO_VALUATION_CONTROL`

narrows to

`MISSING_P2_HEEGNER_INDEX_AND_TWIST_LRATIO_VALUATION_CONTROL`.

The remaining substantive arithmetic inputs are:

1. `ord_2(m_K(f))` for the fixed optimal-composite Heegner point;
2. `ord_2(lambda_D)` for `lambda_D=L(E^D,1)/Omega(E^D)`.

The term `c_infinity(E^D)` is a directly computable real-topology factor, and the odd-bad-prime Tamagawa valuations are already protected.

## 8. Firewall

WP58A does not prove:

- `C_f=1`;
- `m_K(f)` is odd or one;
- any value or unit property of `lambda_D`;
- rank-zero BSD for `E^D`;
- fixed-`2` p-adic-height nondegeneracy;
- a height-one `(2)` analytic determinant generator;
- the final WP06 normalization descent;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
