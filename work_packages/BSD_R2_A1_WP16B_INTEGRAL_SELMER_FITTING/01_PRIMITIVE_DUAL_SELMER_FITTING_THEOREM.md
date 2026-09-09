# Primitive dual-Selmer/Fitting realization theorem

## 1. Setup and coefficient ring

Let `E/Q` lie in the selected `BSD-R2-A1` class. Use the protected inputs:

- `rank E(Q)=1`;
- `#E(Q)_tors` is odd;
- `Sha(E/Q)` is finite;
- protected WP16A gives exact finite-level Kummer sequences and stabilization.

Set

`R := Z_2`,

and for each `n >= 1` write

`S_n := Sel_{2^n}(E/Q)`.

All finite-level Selmer groups in this package use the classical Kummer local condition at every place.

## 2. The primitive classical local condition

For every place `v` of `Q` and `n >= 1`, define

`H^1_Kum(Q_v,E[2^n])`

as the image of the local Kummer map

`E(Q_v)/2^n E(Q_v) -> H^1(Q_v,E[2^n])`.

Then

`S_n = ker(H^1(Q,E[2^n]) -> product_v H^1(Q_v,E[2^n])/H^1_Kum(Q_v,E[2^n]))`.

The phrase `primitive classical` means exactly this levelwise choice. No finite place is deleted and no bad-prime local condition is replaced by an imprimitive one.

The real place is included. At `v=2`, this is the Kummer condition, not a Greenberg ordinary condition. At every bad semistable `ell | N`, it is the full Kummer image, not an unramified substitute.

## 3. Direct-limit Selmer object

Use the natural maps induced by the inclusions

`E[2^n] -> E[2^(n+1)]`.

On the left side of the Kummer exact sequence these correspond to

`E(Q)/2^n E(Q) -> E(Q)/2^(n+1)E(Q),   x -> 2x`,

and on the Tate-Shafarevich term to the natural inclusion

`Sha(E/Q)[2^n] -> Sha(E/Q)[2^(n+1)]`.

Define

`Sel_{2^infinity}^{Kum}(E/Q) := colim_n S_n`.

Filtered direct limits are exact in abelian groups. Therefore the finite-level Kummer sequences give

`0 -> colim_n E(Q)/2^nE(Q)`

`  -> Sel_{2^infinity}^{Kum}(E/Q)`

`  -> colim_n Sha(E/Q)[2^n] -> 0`.

The right direct limit is

`Sha(E/Q)[2^infinity]`.

The left direct limit is canonically

`D_E := E(Q) tensor (Q_2/Z_2)`.

Indeed, the transition maps are multiplication by `2`, which is the standard direct system realizing tensor product with `Q_2/Z_2`. Protected rank one and odd rational torsion imply that `D_E` is a divisible `2`-primary group of corank one; after choosing a basis of the free quotient of `E(Q)`, one obtains a noncanonical isomorphism

`D_E ~= Q_2/Z_2`.

No such basis is part of the invariant.

Thus the canonical direct-limit Kummer sequence is

`0 -> D_E`

`  -> Sel_{2^infinity}^{Kum}(E/Q)`

`  -> Sha(E/Q)[2^infinity] -> 0`.      `(K_inf)`

No BSD leading-term identity is used.

## 4. Pontryagin dual and the saturated free line

For a discrete `2`-primary abelian group `M`, write

`M^vee := Hom(M,Q_2/Z_2)`.

Because `Q_2/Z_2` is divisible, it is injective as an abelian group. Therefore applying `Hom(-,Q_2/Z_2)` to `(K_inf)` is exact and reverses arrows:

`0 -> Sha(E/Q)[2^infinity]^vee`

`  -> X_E`

`  -> L_E -> 0`,      `(X)`

where

`X_E := Sel_{2^infinity}^{Kum}(E/Q)^vee`

and

`L_E := D_E^vee`.

Since `D_E` is divisible of corank one, `L_E` is a free rank-one `Z_2`-module. Equivalently, after a basis choice one may identify `L_E ~= Z_2`, but WP16B does not choose such a basis.

Thus `X_E` is a finitely generated `Z_2`-module of rank one, and `(X)` supplies its canonical saturated free quotient as the abstract rank-one module `L_E`.

## 5. The canonical torsion module

Let

`T_E := Tor_{Z_2}(X_E)`.

### Theorem 5.1

There is a canonical equality of submodules of `X_E`, through the injection in `(X)`,

`T_E = Sha(E/Q)[2^infinity]^vee`.

### Proof

The injected module `Sha(E/Q)[2^infinity]^vee` is finite because protected WP05 gives finiteness of `Sha(E/Q)`. Hence it is contained in `T_E`.

Conversely, let `x in T_E`. Its image in the quotient `L_E` is torsion. Since `L_E` is free over `Z_2`, it is torsion-free. Therefore that image is zero. Hence `x` lies in the kernel of `X_E -> L_E`, which by exactness of `(X)` is `Sha(E/Q)[2^infinity]^vee`.

Thus the two submodules are equal. QED.

### Corollary 5.2

The saturated rank-one free quotient is canonically

`X_E/T_E ~= L_E`.

It is free of rank one over `Z_2`. An identification with literal `Z_2`, or a splitting of `(X)`, requires a basis choice and is unnecessary for the invariant.

## 6. Exact length realization

Pontryagin duality preserves the elementary divisors of a finite `2`-primary group. Explicitly, the dual of `Z/2^aZ` is again cyclic of order `2^a`. Therefore

`len_{Z_2} T_E = len_{Z_2} Sha(E/Q)[2^infinity]`.

Protected WP16A proves

`lim_n s_n(E) = len_{Z_2} Sha(E/Q)[2^infinity]`,

where

`s_n(E) := ord_2 #Sel_{2^n}(E/Q) - n`.

Hence

`boxed:  lim_n s_n(E) = len_{Z_2} T_E`.      `(L)`

This is the requested exact integral realization of the stabilized finite-level length.

## 7. Exact zeroth Fitting ideal

Let a finite `Z_2`-module `M` have elementary-divisor decomposition

`M ~= direct_sum_i Z_2/(2^{a_i})`,

with the empty sum allowed for `M=0`.

For a cyclic summand,

`Fitt^0_{Z_2}(Z_2/(2^a)) = (2^a)`.

Zeroth Fitting ideals multiply under finite direct sums. Therefore

`Fitt^0_{Z_2}(M) = (2^{sum_i a_i})`

`                    = 2^{len_{Z_2} M} Z_2`.

Applying this to `T_E` and using `(L)` gives

`boxed: Fitt^0_{Z_2}(T_E)`

`       = 2^{lim_n s_n(E)} Z_2`.      `(F)`

This is equality of ideals, not equality of chosen generators. A generator can be multiplied by a `2`-adic unit without changing the ideal; therefore there is no hidden valuation ambiguity.

### Important rank-one normalization

Do **not** use `Fitt^0_{Z_2}(X_E)` as the invariant. The module `X_E` has positive rank, so its zeroth Fitting ideal does not encode the desired finite length. WP16B removes the saturated free rank-one quotient first and applies `Fitt^0` to the canonical torsion submodule `T_E`.

Likewise, replacing the saturated free quotient by the `Z_2`-span of a possibly nonprimitive Mordell-Weil or Heegner point can introduce a nonzero `2`-adic index. Such an index is a substantive future defect and may not be declared a unit.

## 8. Exact reformulation of the selected target

Recall

`delta_2(E) := ord_2(L'(E,1)/(Omega_E Reg_E))`

`              - sum_{ell|N} ord_2(c_ell)`.

For a nonzero ideal `I = 2^m Z_2`, define

`v_2(I) := m`.

Equation `(F)` gives

`v_2(Fitt^0_{Z_2}(T_E)) = lim_n s_n(E)`.

Protected WP16A already proves that `BSD-R2-A1` is equivalent to

`delta_2(E) = lim_n s_n(E)`.

Therefore the selected still-unproved equality is equivalent to

`boxed: delta_2(E) = v_2(Fitt^0_{Z_2}(T_E))`.      `(BSD-Fitt)`

No direction of `(BSD-Fitt)` is proved here beyond the algebraic identification of its right side with the protected Sha length.

## 9. Tamagawa normalization

The module `T_E` is built from primitive Kummer local conditions at every bad prime. No factor `c_ell` is separately divided out of, or multiplied into, the algebraic module.

Protected WP13 proves the exact `2`-adic Tamagawa valuations and identifies the even-Tamagawa primes with residual-conductor drop. Those values remain explicitly on the analytic side through the definition of `delta_2(E)`.

WP16B makes no unproved assertion that changing from primitive Kummer local conditions to an imprimitive external Selmer structure creates a defect equal to `product c_ell` or to its `2`-part. A WP17 theorem using different local conditions must compute that comparison exactly before it can be composed with `(BSD-Fitt)`.

## 10. Local condition at `2`

Protected WP06 records the failure mode:

`finite classical Kummer condition != automatically Greenberg ordinary condition at 2`.

WP16B therefore fixes the Kummer condition at `2` as part of the invariant. The selected curve has good ordinary reduction at `2`, but good ordinarity alone is not an authorization to replace the local condition.

A future theorem phrased with the connected-etale ordinary condition must prove one of:

1. exact equality with the Kummer condition in the relevant finite/integral object;
2. an exact finite kernel/cokernel comparison with its full `2`-adic length;
3. a determinant/Fitting comparison that explicitly carries the local defect.

The protected WP07 observation that the standard residual `p`-distinguished condition fails at `p=2` must remain part of the applicability check for any ordinary theorem.

## 11. Archimedean and bad-prime completeness

The real place is included in the levelwise Kummer definition. No archimedean `2`-factor is silently suppressed.

For every bad semistable `ell | N`, the full local Kummer image is retained. In particular, WP16B does not classify an even Tamagawa factor as a unit merely because an external odd-prime theorem would do so.

## 12. WP17 theorem query exported by WP16B

A candidate WP17 theorem is relevant only if, after MATHFORGE source admission, it controls one of the following at `p=2` over the protected WP09 field `K`:

1. the exact analogue of `Fitt^0(Tor X_E)` for the primitive classical rank-one dual Selmer module over `K`;
2. a Selmer-complex determinant/Fitting invariant proved exactly comparable to that primitive torsion ideal;
3. a one-sided divisibility for such an ideal together with a primitivity or reverse-divisibility theorem sufficient to determine its valuation.

The applicability check must retain:

- literal inclusion of `p=2`;
- coefficient ring and self-duality hypotheses;
- local condition at every place above `2`;
- bad-prime primitive/imprimitive comparison;
- every Tamagawa and residual-conductor correction;
- the saturated rank-one free direction rather than an unverified generator sublattice;
- exact quadratic descent through protected WP06;
- exact analytic normalization needed to reach `delta_2(E)`.

A theorem only up to a unit is admissible only if the statement is an equality of ideals whose valuation is thereby exact, or if the remaining unit ambiguity is proved irrelevant to the specific valuation. A missing power of `2` is never a unit ambiguity.

## 13. Claim boundary

This theorem is an exact representation theorem. It does not prove the analytic-to-arithmetic equality `(BSD-Fitt)`.

Accordingly

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`

remains unchanged, and MATHCERT certification remains outside this package.
