# WP55A exact classical Gross–Zagier / WP00 normalization theorem

## 1. Protected hypotheses and notation

Work on the protected selected BSD-R2-A1 lane.

Let `E/Q` have conductor `N`, analytic rank one, and protected WP00 minimal Néron differential `omega_E`. Let the protected WP09 auxiliary field be

`K=Q(sqrt(D_K))`,

with `D_K` fundamental, `(D_K,2N)=1`, every prime dividing `2N` split in `K`, and

`L(E^D,1) != 0`.

Let `phi` be the normalized weight-two newform associated to `E`. Let

`f:X_0(N)->E`

be a modular parametrization sending the cusp at infinity to `O`.

The protected MATHFORGE WP55 admission supplies, in the conductor-one trivial-character specialization of Cai–Shu–Tian Theorem 1.1,

`(GZ)
 L'(E/K,1)
 = [8*pi^2 (phi,phi)_{Gamma_0(N)} /(u_K^2 sqrt(|D_K|))]
   * [hhat_K(P_K(f))/deg(f)]`.

Here `hhat_K` is retained in the exact source convention: the Néron–Tate height over `K`.

Protected WP09 supplies

`(BC)
 L(E/K,s)=L(E,s)L(E^D,s)`

in the campaign's finite-L convention. Since `L(E,1)=0` and `L(E^D,1)!=0`, differentiation at `s=1` gives

`(BC')
 L'(E/K,1)=L'(E,1)L(E^D,1)`.

## 2. Archimedean area attached to the WP00 differential

Define

`A_E := (i/2) integral_{E(C)} omega_E wedge overline(omega_E)`.

This is a positive real number determined by the protected WP00 minimal Néron differential.

Retain the source modular-differential scalar `C_f>0` by

`(M)
 f^*omega_E = +/- C_f * 2*pi*i*phi(z) dz`.

No specialization `C_f=1` is made.

## 3. Exact modular-area identity

### Proposition

With the above normalizations,

`(A)
 4*pi^2 C_f^2 (phi,phi)_{Gamma_0(N)} = deg(f) A_E`.

### Proof

Because `f` is a finite holomorphic morphism of compact Riemann surfaces,

`integral_{X_0(N)(C)} f^*((i/2)omega_E wedge overline(omega_E))
 = deg(f) A_E`.

Using `(M)`,

`(i/2) f^*omega_E wedge overline(f^*omega_E)
 = 4*pi^2 C_f^2 |phi(z)|^2 dx dy`.

The cusp set has measure zero, and the source Petersson normalization is

`(phi,phi)_{Gamma_0(N)}
 = integral_{Gamma_0(N)\H} |phi(z)|^2 dx dy`.

Integrating gives `(A)` exactly. There is no quotient by a unit, no omitted component factor, and no completed-L normalization in this step. QED.

## 4. Elimination of Petersson norm and modular degree

From `(A)`,

`(phi,phi)_{Gamma_0(N)}/deg(f)
 = A_E/(4*pi^2 C_f^2)`.

Substitute into `(GZ)`:

`(GZ-area)
 L'(E/K,1)
 = [2 A_E/(C_f^2 u_K^2 sqrt(|D_K|))]
   * hhat_K(P_K(f))`.

The factors `deg(f)` and `(phi,phi)` have disappeared only because they have been replaced by the exact geometric identity `(A)`.

## 5. Exact WP00 quotient

Combine `(GZ-area)` with `(BC')`:

`L'(E,1)
 = [2 A_E hhat_K(P_K(f))]
   /[C_f^2 u_K^2 sqrt(|D_K|) L(E^D,1)]`.

The WP00 registry defines

`Omega_E = integral_{E(R)} |omega_E|`

and, in rank one,

`Reg_E = <P,P>_NT`

for a `Z`-basis `P` of `E(Q)/E(Q)_tors`.

Therefore:

### Theorem WP55A

`(WP55A)
 L'(E,1)/(Omega_E Reg_E)
 = R_GZ/WP00(E,K,f)`

with

`R_GZ/WP00(E,K,f)
 := [2 A_E/(C_f^2 u_K^2 sqrt(|D_K|) Omega_E L(E^D,1))]
    * [hhat_K(P_K(f))/Reg_E]`.

Every factor in `R_GZ/WP00` is explicit and named. This is an equality in positive real numbers under the protected analytic-rank-one hypotheses.

## 6. Exact 2-adic target statement

The protected campaign quantity is

`delta_2(E)
 = ord_2(L'(E,1)/(Omega_E Reg_E))
   - sum_{ell|N}ord_2(c_ell)`.

The equality `(WP55A)` is an exact real normalization identity. A symbol `ord_2(R_GZ/WP00)` may be used downstream **only after** an algebraicity/rationality theorem identifies the relevant quotient in a number field or rational line with a specified embedding/normalization. WP55A does not manufacture a 2-adic valuation of an arbitrary real number.

Thus WP55A narrows D2d to the exact arithmetic comparison needed to transport `R_GZ/WP00` into the protected rational/2-adic determinant line.

## 7. Relation to protected WP54A

WP54A proves independently

`Q^ord
 = (u_K/h_K) prod_{ell|N}(1+ell^(-1))`.

WP55A does **not** divide `(WP55A)` by `Q^ord`, nor infer cancellation of `u_K`, `h_K`, bad-prime factors, Tamagawa factors, or periods. Such cancellation is permitted only inside a later theorem that places both formulae on the same exact determinant/reciprocity line.

## 8. D2d narrowing

The old boundary

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`

is replaced by

`MISSING_EXACT_CLASSICAL_GZ_WP00_RESIDUAL_SCALAR_COMPARISON`.

A theorem closing this boundary must do enough to identify, with no hidden factor of two,

`R_GZ/WP00(E,K,f)`

with the exact classical scalar required by the protected p-adic/determinant comparison. At minimum it must control:

1. the source `K`-height versus the WP00 `Q`-regulator, including Mordell–Weil index and base-field height convention;
2. the area/real-period/twist-central-value factor;
3. the modular-differential scalar `C_f`;
4. the exact relation of the classical Heegner point to the protected Disegni ordinary Heegner object if that relation is used;
5. every power of `2` during the eventual WP06 descent.

## 9. Non-claims

WP55A does not prove a rank-zero BSD formula for `E^D`; does not assert `C_f=1`; does not identify real and p-adic heights; does not prove fixed-`2` height nondegeneracy; does not close D1c or D2e; does not prove `BSD-R2-A1`; and does not certify any theorem in MATHCERT.
