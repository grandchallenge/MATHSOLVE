# WP22 theorem — odd-prime cyclotomic local control and Tamagawa depth

## 1. Setup

Let `E/Q` lie in the protected selected semistable odd-conductor class. Let

`Q_infty/Q`

be the cyclotomic `Z_2`-extension. Fix an odd prime `ell`, choose a place `w|ell` of `Q_infty`, and write

`F := Q_ell`,

`F_infty := Q_{infty,w}`,

`Gamma_ell := Gal(F_infty/F)`.

Protected WP21 defines the ambient local primitive-control kernel

`K_ell := H^1(Gamma_ell,E(F_infty))[2^infinity]`.

We compute it exactly.

## 2. The local cyclotomic tower at an odd prime

### Lemma `BSD-A1-WP22-UNRAM-001`

For every odd prime `ell`, `F_infty/F` is an unramified `Z_2`-extension.

### Proof

The global cyclotomic `Z_2`-extension is unramified away from `2`, so the completion at `ell` is unramified.

Its decomposition group is a closed subgroup of `Gamma ~= Z_2`. It is not trivial. Indeed, if `ell` split completely in every layer, then its Frobenius class would be trivial in every finite real `2`-power cyclotomic quotient. Equivalently, for arbitrarily large `r`, the odd integer `ell` would satisfy

`ell == +/- 1 (mod 2^r)`.

That would force `ell=1` or `ell=-1` as a `2`-adic integer, impossible for a positive rational prime.

Every nonzero closed subgroup of `Z_2` is open and isomorphic to `Z_2`. Hence `Gamma_ell ~= Z_2`, and the local extension is the unique unramified `Z_2`-extension of `Q_ell`. QED.

After reindexing, let

`F_m/F`

be the finite unramified layer of degree

`d_m := 2^m`,

with cyclic Galois group

`G_m := Gal(F_m/F)`.

Let `k_m/k` be the corresponding residue-field extension.

## 3. Vanishing for the connected identity component

Let `E_0(F_m)` be the subgroup reducing to the identity component of the Neron special fibre, and `E_1(F_m)` the formal subgroup. There is an exact reduction sequence

`0 -> E_1(F_m)
   -> E_0(F_m)
   -> Gbar(k_m)
   -> 0`,

where `Gbar` is the connected identity component of the special fibre. In the semistable case, `Gbar` is either an elliptic curve (good reduction) or a one-dimensional torus (multiplicative reduction).

### Lemma `BSD-A1-WP22-FORMAL-001`

For `i>0`, the `2`-primary part of

`H^i(G_m,E_1(F_m))`

is zero; in fact the finite cyclic Tate cohomology of `E_1(F_m)` is zero.

### Proof

The formal group `E_1(F_m)` is a pro-`ell` group. Since `ell` is odd, multiplication by

`|G_m|=2^m`

is an automorphism of `E_1(F_m)`.

Finite-group Tate cohomology is annihilated by the group order. Because multiplication by that same order is invertible on the coefficient group, every Tate cohomology group must vanish. QED.

### Lemma `BSD-A1-WP22-REDUCTION-001`

For the connected special-fibre group `Gbar`,

`H^1(G_m,Gbar(k_m))=0`

and

`Gbar(k)/N_{k_m/k}Gbar(k_m)=0`.

Consequently the cyclic `H^2` group also vanishes.

### Proof

Let `phi` denote arithmetic Frobenius on `Gbar` over an algebraic closure of the residue field.

The endomorphism

`phi-1`

has kernel `Gbar(k)`, which is finite. Its differential is `-1`, because the differential of Frobenius is zero in characteristic `ell`. Hence `phi-1` is a separable isogeny and therefore surjective on algebraic-closure points.

Let

`N := 1+phi+...+phi^(d_m-1)`.

One has

`(phi-1)N = phi^(d_m)-1`.

Both `phi-1` and `phi^(d_m)-1` are isogenies. Hence `N` is also an isogeny and is surjective on algebraic-closure points.

For cyclic cohomology,

`H^1(G_m,Gbar(k_m))
 = ker(N:Gbar(k_m)->Gbar(k)) / (phi-1)Gbar(k_m)`.

Take `x` in the norm kernel. Surjectivity of `phi-1` gives `y in Gbar(kbar)` with

`(phi-1)y=x`.

Then

`(phi^(d_m)-1)y = N x = 0`,

so `y in Gbar(k_m)`. Hence `x` is a coboundary and `H^1=0`.

For norm-surjectivity, take `z in Gbar(k)`. Choose `y in Gbar(kbar)` with `N y=z`. Then

`(phi^(d_m)-1)y = (phi-1)z = 0`,

so `y in Gbar(k_m)`. Thus every `z` is a norm.

For a finite cyclic group, degree-two cohomology is the Tate norm quotient, so it vanishes as well. QED.

### Corollary `BSD-A1-WP22-E0-001`

For the finite unramified layer,

`H^1(G_m,E_0(F_m))=0`

and

`H^2(G_m,E_0(F_m))=0`.

### Proof

Apply the long exact cohomology sequence to

`0 -> E_1(F_m) -> E_0(F_m) -> Gbar(k_m) -> 0`

and use the two preceding lemmas. QED.

## 4. Reduction to the Neron component group

Let `Phi` be the component group of the Neron model. There is an exact sequence

`0 -> E_0(F_m) -> E(F_m) -> Phi(k_m) -> 0`.

The previous corollary gives:

### Lemma `BSD-A1-WP22-COMPONENT-001`

There is a canonical isomorphism

`H^1(G_m,E(F_m)) ~= H^1(G_m,Phi(k_m))`.

### Proof

The relevant part of the cohomology sequence is

`H^1(G_m,E_0(F_m))
 -> H^1(G_m,E(F_m))
 -> H^1(G_m,Phi(k_m))
 -> H^2(G_m,E_0(F_m))`.

Both outer terms vanish. QED.

For good reduction, `Phi=0`; hence the local cohomology vanishes at every finite layer.

For multiplicative type `I_n`, protected WP13 supplies the component-group structure and Tamagawa formulas. Geometrically

`Phi(kbar) ~= Z/nZ`.

Frobenius acts by `+1` in the split multiplicative case and by `-1` in the nonsplit multiplicative case. For `m>=1`, `d_m` is even, so `Phi(k_m)=Z/nZ` in either case.

## 5. Split multiplicative calculation

Assume split multiplicative reduction of type `I_n`. Put

`M := Z/nZ`.

The generator `sigma` of `G_m` acts trivially on `M`. Therefore

`H^1(G_m,M)
 = ker(d_m:M->M)`.

This is the subgroup killed by `2^m`, hence is cyclic of order

`gcd(n,2^m)`.

As `m` increases, these groups are compatible under inflation and exhaust the `2`-primary subgroup of `M`. Passing to the unramified `Z_2` tower gives

`H^1(Gamma_ell,E(F_infty))[2^infinity]
 ~= (Z/nZ)[2^infinity]`.

Therefore

`#K_ell = 2^{v_2(n)}`.

Protected WP13 proves `c_ell=n` for split multiplicative reduction. Hence

`#K_ell = 2^{v_2(c_ell)}`.

## 6. Nonsplit multiplicative calculation

Assume nonsplit multiplicative reduction of type `I_n`. Again put

`M := Z/nZ`.

For `m>=1`, a generator `sigma` of the unramified cyclic group acts on the geometric component group as `-1`. Because `d_m` is even,

`N=1+sigma+...+sigma^(d_m-1)=0`

on `M`, while

`(sigma-1)M = 2M`.

Thus

`H^1(G_m,M)=M/2M`.

The inflation maps are the natural identity on this quotient, so the group is already stable from the first even layer. Consequently

`K_ell ~= (Z/nZ)/2(Z/nZ)`

on its `2`-primary side.

Its order is

`gcd(2,n)`.

Protected WP13 proves that for nonsplit multiplicative type `I_n`,

`c_ell=gcd(2,n)`.

Therefore again

`#K_ell = 2^{v_2(c_ell)}`.

## 7. Good-reduction calculation

### Theorem `BSD-A1-WP22-GOOD-001`

If `ell` is odd and `E` has good reduction at `ell`, then

`K_ell=0`.

### Proof

For good reduction the component group is zero. Lemma `BSD-A1-WP22-COMPONENT-001` therefore gives

`H^1(G_m,E(F_m))=0`

at every finite unramified `2`-power layer. Any continuous cocycle of `Gamma_ell` with values in `E(F_infty)` has finite image and is represented at some finite stage. Hence the direct-limit continuous cohomology is zero. QED.

## 8. Bad-prime theorem

### Theorem `BSD-A1-WP22-TAMAGAWA-001`

For every odd bad semistable prime `ell|N`, the WP21 ambient local control kernel is finite and satisfies

`#K_ell = 2^{v_2(c_ell)}`.

More precisely:

- split multiplicative `I_n`:
  `K_ell ~= (Z/nZ)[2^infinity]`;
- nonsplit multiplicative `I_n`:
  `K_ell ~= ((Z/nZ)/2(Z/nZ))[2^infinity]`.

In both cases

`len_{Z_2}(K_ell^vee)=v_2(c_ell)`

and

`Fitt^0_{Z_2}(K_ell^vee)=2^{v_2(c_ell)} Z_2`.

### Proof

Combine the split and nonsplit calculations with protected WP13. Pontryagin duality preserves the elementary divisors of the finite `2`-primary group, and the standard finite `Z_2` Fitting calculation gives the final ideal identity. QED.

## 9. Total bad-prime ambient defect

Define

`K_bad := product_{ell|N} K_ell`.

The product is finite because the conductor has finitely many prime divisors.

### Corollary `BSD-A1-WP22-BAD-TOTAL-001`

One has

`len_{Z_2}(K_bad^vee)
 = sum_{ell|N} v_2(c_ell)`

and

`Fitt^0_{Z_2}(K_bad^vee)
 = 2^{sum_{ell|N} v_2(c_ell)} Z_2`.

Thus the exact Tamagawa term subtracted in

`delta_2(E)
 = ord_2(L'(E,1)/(Omega_E Reg_E))
   - sum_{ell|N} v_2(c_ell)`

is exactly the total ambient bad-prime local-control length in the primitive cyclotomic specialization problem.

This is an identification of the **ambient local defect**, not yet of the globally realized control quotient `C_E`.

## 10. Relation to WP21's actual control module

Protected WP21 defines

`C_E := im(loc_Q) intersect K_loc`.

WP22 proves that all odd good components of `K_loc` vanish and that the bad odd components form the finite group `K_bad` computed above. The only remaining ambient local component is the place `2`:

`K_2 = H^1(Gamma_2,E(Q_{infty,2}))[2^infinity]`.

Hence, after the harmless real place is removed,

`K_loc` is supported on

`{2} union {ell: ell|N and 2|c_ell}`

at the `2`-primary level, with the exact bad-prime lengths above.

WP22 does **not** prove that

`C_E = K_2 x K_bad`

or that the projection of `C_E` to `K_bad` is surjective. Determining the globally hit subgroup requires a separate global-local/Poitou-Tate argument.

## 11. Refined D1b boundary

The former D1b obligation

`MISSING_P2_PRIMITIVE_LOCAL_CONTROL_DEFECT_EVALUATION`

is now reduced to two narrower questions:

1. `MISSING_P2_GOOD_ORDINARY_LOCAL_CONTROL_KERNEL_AT_2`;
2. `MISSING_P2_GLOBAL_HIT_SUBGROUP_OF_LOCAL_CONTROL_KERNELS`.

The odd-prime ambient calculation is closed.

## 12. Claim firewall

WP22 does not prove:

- the value, finiteness, or vanishing of `K_2`;
- `C_E=K_loc`;
- surjectivity of global localization onto bad-prime control classes;
- Kummer/Greenberg equality at `2`;
- a primitive cyclotomic perfect determinant complex;
- a height-one `(2)` analytic determinant generator;
- the WP20 Bockstein/WP00 normalization;
- `BSD-R2-A1`;
- any MATHCERT certification.
