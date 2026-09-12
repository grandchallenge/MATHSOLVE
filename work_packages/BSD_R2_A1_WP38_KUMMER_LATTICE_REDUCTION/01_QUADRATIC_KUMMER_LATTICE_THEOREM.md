# WP38 theorem — no quadratic base-change index in the rank-one Mordell–Weil lattice

## 1. Protected setup

Let `E/Q` lie in the protected selected `BSD-R2-A1` class and let `K/Q` be the protected WP09 auxiliary imaginary quadratic field.

Protected facts used here are only:

1. `rank E(Q)=1`;
2. `rank E(K)=1`;
3. protected WP06 proves `E(K)[2^infinity]=0`.

Let

`G := Gal(K/Q) = {1,tau}`

and let

`T_K := E(K)_tors`,

`M_K := E(K)/T_K`.

Then `T_K` is finite of odd order and `M_K` is free of rank one over `Z`.

## 2. The involution is trivial on the free quotient

### Lemma `BSD-A1-WP38-TAU-FREE-001`

The action of `tau` on `M_K` is the identity.

### Proof

The natural map

`E(Q)/E(Q)_tors -> M_K`

is injective: an element of `E(Q)` mapping to torsion in `E(K)` is already torsion in `E(Q)`.

The source is free of rank one because `rank E(Q)=1`. Hence its image is a nonzero rank-one subgroup of the rank-one free group `M_K`.

An involution of a rank-one free `Z`-module acts by either `+1` or `-1`. Since every rational point is fixed by `tau`, the involution fixes the nonzero image of `E(Q)/E(Q)_tors`; therefore it cannot act by `-1`. Thus it acts by `+1` on all of `M_K`. QED.

## 3. Odd torsion kills the descent obstruction

### Lemma `BSD-A1-WP38-H1-TORS-001`

`H^1(G,T_K)=0`.

### Proof

Protected WP06 gives `E(K)[2^infinity]=0`, so the finite group `T_K` has odd order. Hence multiplication by `|G|=2` is an automorphism of `T_K`.

For a finite group `G`, cohomology `H^i(G,M)` for `i>0` is annihilated by `|G|`. Since multiplication by `2` is invertible on `T_K`, the only subgroup of `H^1(G,T_K)` both annihilated by `2` and on which multiplication by `2` is invertible is zero.

Equivalently, one can see the vanishing explicitly. If `t in T_K` is a `1`-cocycle value for `tau`, then

`(1+tau)t=0`.

Choose an integer `a` such that multiplication by `2a` is the identity on `T_K`. Put `s=-a t`. Then

`(tau-1)s=t`,

so every cocycle is a coboundary. QED.

## 4. Exact free-lattice descent

### Theorem `BSD-A1-WP38-MW-LATTICE-001`

Restriction induces an isomorphism

`E(Q)/E(Q)_tors  ->~  E(K)/E(K)_tors`.

### Proof

Injectivity was established in Lemma `TAU-FREE-001`.

For surjectivity, let `P in E(K)`. Since `tau` acts trivially on `M_K`, the difference

`t := tau(P)-P`

lies in `T_K`.

The relation `tau^2=1` gives

`(1+tau)t=0`,

so `t` is a `1`-cocycle. By Lemma `H1-TORS-001`, there is `s in T_K` with

`t=(tau-1)s`.

Therefore

`tau(P-s)=P-s`.

A `K`-rational point fixed by `Gal(K/Q)` is `Q`-rational, so `P-s in E(Q)`. Thus the class of `P` modulo `T_K` has a rational representative. Every element of `M_K` is therefore in the image of `E(Q)/E(Q)_tors`.

The map is an isomorphism. QED.

## 5. Exact `2`-adic Kummer lattice consequence

### Corollary `BSD-A1-WP38-Z2-LATTICE-001`

The natural base-change map induces an isomorphism of free rank-one `Z_2`-modules

`E(Q) tensor_Z Z_2  ->~  E(K) tensor_Z Z_2`.

### Proof

Tensor Theorem `MW-LATTICE-001` with `Z_2`. Finite odd torsion tensors to zero over `Z_2`, so the displayed modules are precisely the `2`-adic completions of the respective Mordell–Weil free quotients. QED.

## 6. What this does and does not identify

The corollary eliminates one possible source of a hidden factor of `2` in WP37's D2b comparison: **quadratic base change itself does not enlarge the primitive global Mordell–Weil `Z_2` lattice.**

In particular, if `P_Q` is a primitive generator of `E(Q)/tors`, its image is primitive in `E(K)/tors`.

However, this does not prove that a chosen Heegner point `P_H in E(K)` is primitive. One may still have

`P_H = m P_Q + torsion`

with `ord_2(m)>0`; that Heegner index is genuine arithmetic data and remains part of the later Gross–Zagier/normalization comparison.

Nor does this theorem identify

`E(K) tensor Z_2`

with the full source-compatible Nekovář extended/ordinary Selmer cohomology lattice. WP37 explicitly kept that distinction. Finite local-condition and extended-Selmer comparison terms can still change the integral lattice even when the underlying Mordell–Weil free line is the same.

## 7. D2b reduction

Protected WP37 stated D2b as the exact comparison between the Nekovář `K`-Selmer lattice and the protected primitive Kummer/WP20 lattice.

Theorem `MW-LATTICE-001` and Corollary `Z2-LATTICE-001` prove that the **global Mordell–Weil base-change component of this comparison has index one**.

Therefore the surviving D2b boundary is concentrated in the exact map from the primitive Kummer Mordell–Weil lattice to the source-compatible Nekovář extended/ordinary Selmer lattice, including all local-condition and extended-cohomology terms:

`MISSING_P2_NEKOVAR_EXTENDED_TO_PRIMITIVE_KUMMER_LOCAL_INDEX`.

No global quadratic free-lattice correction may be inserted into that remaining comparison.

## 8. Claim firewall

This theorem does not prove:

- `Sha(E/K)[2^infinity]=0` or any new Sha finiteness statement;
- equality of primitive Kummer and Greenberg/ordinary local conditions;
- equality of primitive Kummer and Nekovář extended Selmer cohomology;
- primitivity of the Heegner point;
- nondegeneracy of a `2`-adic height;
- D1c, D2c, D2d, or D2e;
- `BSD-R2-A1`;
- MATHCERT certification.
