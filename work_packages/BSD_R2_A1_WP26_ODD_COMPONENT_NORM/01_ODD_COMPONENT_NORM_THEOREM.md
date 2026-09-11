# WP26 theorem — odd multiplicative universal norms are the 2-primary Neron component

## 1. Setup

Let `ell|N` be an odd bad prime of a protected selected curve. Semistability gives multiplicative reduction of type `I_n`.

Put

`F := Q_ell`.

Protected WP22 proves that the completion of the global cyclotomic `Z_2`-extension at `ell` is the unramified `Z_2`-extension of `F`. Reindex its finite layers as

`F_m/F`,

`[F_m:F]=2^m`,

with

`G_m:=Gal(F_m/F)`.

Let `k_m/k` be the residue extension.

Let `E_0(F_m)` be the subgroup reducing to the connected identity component of the Neron special fibre and let `Phi` be the Neron component group. Protected WP22 gives

`0 -> E_0(F_m) -> E(F_m) -> Phi(k_m) -> 0`

and proves

`H^1(G_m,E_0(F_m))=0`,

`H^2(G_m,E_0(F_m))=0`.

Protected WP25 defines the stabilized universal-norm quotient

`U_ell := E(F)/N_ell^infty`

and proves

`U_ell ~= K_ell^vee`.

The aim of WP26 is to identify this quotient and the class of the saturated generator `P` exactly in terms of the component map.

No new external theorem premise is used.

## 2. Finite norm quotient and Tate cohomology

For a finite cyclic group `G`, write `hat H^i(G,-)` for Tate cohomology.

Cyclic periodicity identifies

`hat H^0(G_m,E_0(F_m))
 ~= H^2(G_m,E_0(F_m))=0`

and

`hat H^1(G_m,E_0(F_m))
 ~= H^1(G_m,E_0(F_m))=0`.

Apply the long exact Tate-cohomology sequence to

`0 -> E_0(F_m) -> E(F_m) -> Phi(k_m) -> 0`.

### Lemma `BSD-A1-WP26-TATE-COMPONENT-001`

The component map induces a canonical isomorphism

`E(F)/N_{F_m/F}E(F_m)
 ~= Phi(k_m)^{G_m}/N_{k_m/k}Phi(k_m)`.

### Proof

The vanishing above gives the exact segment

`0 -> hat H^0(G_m,E(F_m))
   -> hat H^0(G_m,Phi(k_m))
   -> 0`.

Thus the middle map is an isomorphism.

Because `F_m/F` is Galois,

`E(F_m)^{G_m}=E(F)`,

so

`hat H^0(G_m,E(F_m))
 = E(F)/N_{F_m/F}E(F_m)`.

Likewise

`hat H^0(G_m,Phi(k_m))
 = Phi(k_m)^{G_m}/N_{k_m/k}Phi(k_m)`.

The isomorphism is induced by the Neron component map, so it also identifies the class of a point in `E(F)` with the corresponding component class modulo component norms. QED.

## 3. Split multiplicative reduction

Assume split multiplicative reduction of type `I_n`. Protected WP13/WP22 identify

`M := Phi(k_m) ~= Z/nZ`

at every layer, with trivial `G_m` action. Hence

`Phi(k_m)^{G_m}=M`

and the norm is multiplication by

`|G_m|=2^m`.

### Theorem `BSD-A1-WP26-SPLIT-NORM-001`

For every `m>=0`,

`E(F)/N_{F_m/F}E(F_m)
 ~= M/2^m M`.

If

`n=2^a q`, `q` odd,

then for every `m>=a`,

`2^m M=M_odd`,

where `M_odd` is the unique maximal odd-order subgroup of `M`. Therefore

`U_ell ~= M/M_odd`,

the canonical `2`-primary quotient of the rational Neron component group.

### Proof

The finite-layer formula follows immediately from Lemma `BSD-A1-WP26-TATE-COMPONENT-001` and trivial action.

Write the canonical primary decomposition

`M=M[2^infinity] direct_sum M_odd`.

For `m>=a`, multiplication by `2^m` annihilates the `2`-primary summand and is an automorphism of the odd-order summand. Hence its image is exactly `M_odd`.

Thus the finite norm quotient is eventually constant with value `M/M_odd`. Protected WP25 identifies that eventual value with `U_ell`. QED.

### Corollary `BSD-A1-WP26-SPLIT-POINT-001`

Let

`comp_ell(P) in Phi(k)=M`

be the Neron component of the saturated global generator. Then `[P]_ell in U_ell` is its image in

`M/M_odd`.

Consequently

`rho_ell(P)
 = ord_2(ord(comp_ell(P)))`.

### Proof

Lemma `BSD-A1-WP26-TATE-COMPONENT-001` is induced by the component map at every finite stage. Passing to the stable quotient therefore sends `P` to the image of `comp_ell(P)` modulo `M_odd`.

For a finite cyclic group, projection to the `2`-primary quotient removes exactly the odd part of an element's order. Hence the order of the image is the `2`-primary part of the order of `comp_ell(P)`. Taking `ord_2` gives the formula. QED.

Protected WP13 gives `c_ell=n` in this case, so the formula automatically satisfies

`rho_ell(P)<=ord_2(c_ell)`.

## 4. Nonsplit multiplicative reduction

Assume nonsplit multiplicative reduction of type `I_n`. Put again

`M:=Phi(kbar) ~= Z/nZ`.

Protected WP13/WP22 prove that arithmetic Frobenius acts on `M` by `-1`. For every `m>=1`, the residue degree `2^m` is even, so

`Phi(k_m)=M`.

A generator `sigma` of `G_m` acts as `-1`. Hence

`Phi(k_m)^{G_m}=M[2]`

and

`N=1+sigma+...+sigma^(2^m-1)=0`

on `M`.

Protected WP13 identifies the rational component group as

`Phi(k)=M[2]`

with order

`c_ell=gcd(2,n)`.

### Theorem `BSD-A1-WP26-NONSPLIT-NORM-001`

For every `m>=1`,

`E(F)/N_{F_m/F}E(F_m)
 ~= M[2]
 = Phi(k)`.

Thus the finite norm quotients are already stable from the first nontrivial `2`-power layer, and

`U_ell ~= Phi(k)`.

### Proof

Apply Lemma `BSD-A1-WP26-TATE-COMPONENT-001`. The invariant subgroup is `M[2]` and the norm image is zero, giving the displayed quotient. Stability and the WP25 universal-norm identification follow immediately. QED.

### Corollary `BSD-A1-WP26-NONSPLIT-POINT-001`

The class `[P]_ell in U_ell` is exactly the rational component

`comp_ell(P) in Phi(k)=M[2]`.

Consequently

`rho_ell(P)=ord_2(ord(comp_ell(P)))`.

In particular:

- if `n` is odd, `Phi(k)=0`, `c_ell=1`, and `rho_ell(P)=0`;
- if `n` is even, `Phi(k)~=Z/2Z`, `c_ell=2`, and `rho_ell(P)` is `1` precisely when `P` lies on the nonidentity rational component.

### Proof

The finite-layer Tate isomorphism is induced by the component map and the quotient is already `Phi(k)`. The order statement follows. QED.

## 5. Uniform odd-prime theorem

Let

`Phi_ell := Phi_ell(F_ell)`

be the rational Neron component group at an odd bad prime, and let

`Phi_ell,odd`

be its maximal odd-order subgroup.

### Theorem `BSD-A1-WP26-ODD-COMPONENT-001`

For every odd bad semistable prime `ell|N`, there is a canonical identification

`U_ell
 ~= Phi_ell/Phi_ell,odd`.

Under this identification,

`[P]_ell`

is the image of the Neron component `comp_ell(P)`. Therefore

`rho_ell(P)
 = ord_2(ord(comp_ell(P)))`.

### Proof

In the split case this is Theorem `BSD-A1-WP26-SPLIT-NORM-001` and its point corollary. In the nonsplit case `Phi_ell` has order `1` or `2`, so its odd subgroup is trivial and the assertion is Theorem `BSD-A1-WP26-NONSPLIT-NORM-001`. QED.

### Compatibility with WP13 regimes

The formula retains the exact WP13 distinction:

- split `I_n`: `Phi_ell ~= Z/nZ`, `c_ell=n`, and arbitrary depth `ord_2(c_ell)=ord_2(n)` can occur;
- nonsplit `I_n`: `#Phi_ell=gcd(2,n)`, so the rational `2`-primary component depth is truncated to at most one factor of `2` even when the geometric inertia depth is larger.

Thus WP26 does not replace residual-conductor or inertia-depth data by Tamagawa data; it uses the rational Neron component exactly where the universal norm quotient demands it.

## 6. Global consequence for the WP25 scalar

Define the exact odd-component observable

`rho_bad(P)
 := max_{ell|N} ord_2(ord(comp_ell(P)))`,

with the maximum over an empty or all-zero collection taken to be `0`.

### Corollary `BSD-A1-WP26-RHO-001`

Protected WP25's scalar satisfies

`rho_E=max(rho_2(P),rho_bad(P))`.

Hence protected WP24's exact control-defect length becomes

`len_Z2(C_E^vee)
 = 2 ord_2(3-a_2)
   + sum_{ell|N} ord_2(c_ell)
   - max(rho_2(P),rho_bad(P))`.

### Proof

Protected WP25 gives

`rho_E=max_v rho_v(P)`.

Odd good primes and the real place contribute zero. Theorem `BSD-A1-WP26-ODD-COMPONENT-001` evaluates every odd bad term. The only remaining local term is `v=2`. Substitute. QED.

## 7. Refined D1b frontier

The former boundary

`MISSING_P2_SATURATED_GENERATOR_LOCAL_UNIVERSAL_NORM_ORDER`

is now split into:

1. exact finite arithmetic data
   `rho_bad(P)`, determined by the Neron components of the saturated global generator at odd bad primes;
2. one remaining structural local quantity
   `rho_2(P)`.

The remaining structural D1b boundary is therefore

`MISSING_P2_GOOD_ORDINARY_SATURATED_GENERATOR_UNIVERSAL_NORM_ORDER_AT_2`.

This is a place-`2` problem. No odd-prime theorem-shape uncertainty remains in D1b.

## 8. Next representation at `2`

Protected WP23 gives

`#U_2=(3-a_2)^2`

and Greenberg's proof records two finite factors of size `#E_tilde(F_2)[2^infinity]`: the finite Kummer-versus-connected-ordinary discrepancy and the connected-ordinary restriction kernel.

A successor should determine an exact extension or filtration of `U_2` dual to those two factors and locate `[P]_2` within it. The target is the order of `[P]_2`, not merely the order of `U_2`.

No decomposition, splitting, formal-logarithm formula, or Bockstein identity at `2` is asserted in WP26.

## 9. Claim firewall

WP26 does not prove:

- a value of `rho_2(P)`;
- that `U_2` splits as a product of two reduction groups;
- a formal-group or logarithmic formula for `[P]_2`;
- equality of `rho_E`, `rho_2(P)`, or `rho_bad(P)` with a regulator, height, Bockstein, Euler factor, or analytic quantity;
- D1a `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
- D1c `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2 `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`;
- `delta_2(E)=len_Z2 Sha(E/Q)[2^infinity]`;
- `BSD-R2-A1`;
- any MATHCERT certification, novelty, priority, patentability, or commercial claim.
