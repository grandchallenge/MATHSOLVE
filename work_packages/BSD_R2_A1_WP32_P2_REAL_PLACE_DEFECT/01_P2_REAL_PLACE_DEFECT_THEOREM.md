# WP32 theorem — the p=2 real-place comparison defect has zero determinant length

## 1. Setup and admitted source interface

Let `E/Q` lie in the protected selected `BSD-R2-A1` branch and put

`T := T_2(E)`.

Protected MATHFORGE commit

`6f5059836de4330a37f6de8baec5634f889921c4`

admits the Burns–Macias Castillo literal-`p=2` perfect Selmer-complex interface.

For `F=k=Q`, the auxiliary Galois group `G=Gal(F/k)` is trivial. Their Proposition 2.8 and equation (20) compare a perfect Nekovar-style Selmer complex with the classical `2`-adic Selmer complex. The comparison contains the archimedean terms

`cok H^0(kappa_2)`,

`H^1(R,T)`,

and

`H^2(R,T)`.

The source audit authorizes exact downstream calculation of these terms. It does not authorize their silent deletion.

Define

`c_infty(E) := #pi_0(E(R))`.

For an elliptic curve over `R`,

`c_infty(E) in {1,2}`.

Put

`epsilon_infty(E) := ord_2(c_infty(E)) in {0,1}`.

WP32 computes the complete specifically archimedean `p=2` comparison contribution.

## 2. The full archimedean lattice is available over Q

For the unique real place of `Q`, Burns–Macias Castillo define

`H_infty(E/Q)
 = H^0(R,H_1(E(C),Z))`.

Their source comparison (16) is the `G_R`-equivariant integral comparison

`H_1(E(C),Z) tensor Z_2 ~= T`.

Because the auxiliary group `G` is trivial, every finite free `Z_2`-module is projective. We may therefore take the full source-compatible archimedean lattice

`X'_infty := H_infty(E/Q)_2
 := Z_2 tensor_Z H_infty(E/Q)`.

This is stronger than the generic source requirement that `X'` merely be a projective submodule of finite `2`-power index.

### Lemma `BSD-A1-WP32-H0-KAPPA-001`

For this full lattice choice,

`H^0(kappa_2): X'_infty -> H^0(R,T)`

is an isomorphism. In particular,

`cok H^0(kappa_2)=0`.

### Proof

Write `c` for complex conjugation. Since `Z_2` is flat over `Z`, tensoring with `Z_2` commutes with the kernel of `c-1` on the finite free group `H_1(E(C),Z)`. Hence

`Z_2 tensor_Z H^0(R,H_1(E(C),Z))
 ~= H^0(R,Z_2 tensor_Z H_1(E(C),Z))`.

The admitted comparison (16) identifies the module on the right with

`H^0(R,T)`.

By construction `kappa_2` is induced by that same comparison isomorphism. Thus its degree-zero map is exactly the displayed isomorphism. QED.

## 3. First real cohomology is the real component group

### Lemma `BSD-A1-WP32-H1-REAL-001`

There is a canonical isomorphism

`H^1(R,T) ~= E(R)^wedge_2`,

where the right side is the pro-`2` completion.

### Proof

For every `n>=1`, Kummer theory gives

`0 -> E(R)/2^n E(R)
   -> H^1(R,E[2^n])
   -> H^1(R,E)[2^n]
   -> 0`.

Pass to the inverse system under multiplication by `2` on the torsion coefficients.

The finite groups `H^1(R,E)[2^n]` are killed by `2`, because `Gal(C/R)` has order `2`. Their transition maps in this inverse system are induced by multiplication by `2`, hence their inverse limit is zero.

The finite invariant groups in degree zero form a Mittag-Leffler system, so the inverse-limit Kummer sequence has no residual `lim^1` obstruction. Therefore

`H^1(R,T)
 ~= inverse_limit_n E(R)/2^n E(R)
 = E(R)^wedge_2`.

QED.

### Lemma `BSD-A1-WP32-COMPONENT-COMPLETION-001`

There is a canonical isomorphism

`E(R)^wedge_2 ~= pi_0(E(R))`.

Consequently

`#H^1(R,T)=c_infty(E)`

and

`len_Z2 H^1(R,T)=epsilon_infty(E)`.

### Proof

The identity component `E(R)^0` is a real circle group and is divisible. Hence multiplication by `2^n` is surjective on `E(R)^0` for every `n`.

The component group `pi_0(E(R))` has order `1` or `2`. Therefore for every `n>=1`,

`E(R)/2^n E(R) ~= pi_0(E(R))`.

The transition maps on these quotients are the identity under this identification, so the inverse limit is `pi_0(E(R))`. Combine with the preceding lemma. QED.

Thus explicitly:

- if `E(R)` is connected, `H^1(R,T)=0`;
- if `E(R)` has two connected components, `H^1(R,T) ~= Z/2Z`.

## 4. Second real cohomology is dual to the first

The principal polarization of `E` gives the perfect Weil pairing

`< , > : T x T -> Z_2(1)`.

Complex conjugation acts on `Z_2(1)` by `-1`.

For `G_R=Gal(C/R)=<c>` and any `G_R`-module `M`, cyclic Tate cohomology gives

`H^1(R,M)=hat H^1(G_R,M)`

and

`H^2(R,M)=hat H^0(G_R,M)`.

In the present case these groups are finite.

### Lemma `BSD-A1-WP32-REAL-DUALITY-001`

The Weil pairing induces a perfect pairing

`H^1(R,T) x H^2(R,T) -> (1/2 Z_2)/Z_2 ~= Z/2Z`.

Hence

`H^2(R,T) ~= H^1(R,T)^vee`

canonically up to the principal-polarization identification of `E` with its dual.

### Proof

Use the cyclic descriptions

`H^1(R,T)=ker(1+c)/(c-1)T`

and

`H^2(R,T)=T^c/(1+c)T`.

For representatives `x in ker(1+c)` and `y in T^c`, define

`([x],[y]) |-> (1/2)<x,y> mod Z_2`.

If `x` is changed by `(c-1)t`, then, using `cy=y` and the sign action on the Weil-pairing target,

`<(c-1)t,y> = -2<t,y>`.

Its half is integral, so the class modulo `Z_2` is unchanged.

If `y` is changed by `(1+c)t`, then, using `cx=-x`,

`<x,(1+c)t> = 2<x,t>`.

Again its half is integral. Thus the pairing descends to the indicated Tate cohomology groups.

The Weil pairing is unimodular on the free rank-two `Z_2`-lattice `T`. The standard two-periodic cyclic resolution then shows that the induced pairing between the two finite Tate cohomology groups is nondegenerate on both sides; equivalently, the annihilator of either quotient is exactly the denominator defining the other quotient. Hence it is perfect. QED.

### Corollary `BSD-A1-WP32-H2-REAL-001`

One has

`#H^2(R,T)=c_infty(E)`

and

`len_Z2 H^2(R,T)=epsilon_infty(E)`.

Explicitly:

- if `E(R)` is connected, `H^2(R,T)=0`;
- if `E(R)` has two connected components, `H^2(R,T) ~= Z/2Z`.

## 5. The archimedean comparison cone

Let

`D_infty(E)
 := Cone(
      X'_infty[0]
      -> tau_{<=2} RGamma(R,T)
    )`.

This is the bounded archimedean comparison cone underlying the corresponding part of Burns–Macias Castillo equation (20).

### Theorem `BSD-A1-WP32-ARCH-CONE-001`

The cohomology of `D_infty(E)` is

`H^0(D_infty(E))=0`,

`H^1(D_infty(E)) ~= H^1(R,T)`,

`H^2(D_infty(E)) ~= H^2(R,T)`,

and vanishes outside these displayed degrees.

Consequently

`len_Z2 H^1(D_infty(E))
 = len_Z2 H^2(D_infty(E))
 = epsilon_infty(E)`.

### Proof

Apply the long exact cohomology sequence to the defining cone.

Lemma `BSD-A1-WP32-H0-KAPPA-001` says the degree-zero map from `X'_infty` to `H^0(R,T)` is an isomorphism. Since `X'_infty[0]` has no higher cohomology, the remaining assertions follow immediately. The length statement is the combination of Lemma `BSD-A1-WP32-COMPONENT-COMPLETION-001` and Corollary `BSD-A1-WP32-H2-REAL-001`. QED.

## 6. Zero determinant valuation of the p=2 real-place defect

For a finite `Z_2`-module `M`, write

`Fitt(M):=Fitt^0_{Z_2}(M)`.

Since `Z_2` is a DVR,

`Fitt(M)=2^{len_Z2 M} Z_2`.

### Theorem `BSD-A1-WP32-ARCH-FITTING-001`

The archimedean comparison cone satisfies

`Fitt(H^2(D_infty(E)))
 / Fitt(H^1(D_infty(E)))
 = Z_2`

as a fractional ideal of `Z_2`.

Equivalently, its alternating `2`-adic length is zero:

`len_Z2 H^2(D_infty(E))
 - len_Z2 H^1(D_infty(E))
 = 0`.

Therefore the specifically archimedean finite `p=2` comparison defect contributes no net `2`-adic determinant valuation.

### Proof

Both finite groups have length `epsilon_infty(E)`. Their zeroth Fitting ideals are therefore both

`2^{epsilon_infty(E)} Z_2`.

Their quotient is the unit fractional ideal and the difference of lengths is zero. QED.

### Important scope of the conclusion

This is a valuation/Fitting-ideal conclusion. WP32 does not construct a canonical determinant-line trivialization and does not identify the unit relating two determinant generators.

In particular, the theorem does not authorize deletion of the whole real-place interface from an exact generator comparison. It proves only that this interface contributes valuation zero after the full source-compatible archimedean lattice is used.

## 7. Relation to the protected WP00 period convention

The protected BSD-001 normalization uses the whole-real-locus minimal-model Neron period `Omega_E`.

WP32 does not modify that convention and does not divide `Omega_E` by `c_infty(E)`.

The equality of the two real cohomological lengths shows that no *additional* net determinant valuation arises from the p=2 real-place comparison cone. It does not prove the separate D2 comparison between the WP20 Bockstein ideal and the protected analytic normalization

`L'(E,1)/(Omega_E Reg_E)`.

Any exact period/Bockstein comparison must retain the protected whole-real-locus convention.

## 8. Refined determinant frontier

WP32 closes the bounded subproblem

`MISSING_P2_PERFECT_SELMER_ARCHIMEDEAN_VALUATION_CORRECTION`.

It does not close canonical D1a. The remaining determinant-side work must still provide a literal-`p=2` cyclotomic perfect determinant datum whose specialization is exactly the protected primitive Kummer module `X_E`, or compute every remaining finite-place comparison defect.

Thus D1a remains

`MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`.

D1c remains

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

D2 remains

`MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`.

Protected WP31's independent local boundary also remains

`MISSING_P2_FINITE_TWISTED_RECIPROCITY_EXPONENT`.

## 9. Next bounded route

The determinant-side successor should compare the newly admitted literal-`p=2` perfect Selmer complex with the protected primitive Kummer module at the finite places, with special attention to:

1. the exact local conditions at `2` and the protected WP21-WP31 control spine;
2. odd bad-prime finite comparison terms and their relation to the protected WP13/WP22/WP26 Tamagawa/component calculations;
3. whether, after those finite-place corrections, a two-term perfect specialization has rank-one cokernel exactly `X_E`;
4. only then, whether that perfect specialization admits the required cyclotomic deformation and first-order Bockstein comparison.

No new broad literature screen is authorized by this theorem.

## 10. Claim firewall

WP32 does not prove:

- an exact isomorphism `H^2(SCS) ~= X_E`;
- vanishing of finite-place comparison terms;
- a cyclotomic perfect determinant realization;
- an analytic determinant generator at height one `(2)`;
- a value of the protected WP31 twisted-reciprocity exponent;
- equality of the WP20 Bockstein ideal with a Neron-Tate regulator, p-adic height, real period, or local factor;
- `delta_2(E)=len_Z2 Sha(E/Q)[2^infinity]`;
- `BSD-R2-A1`;
- theorem novelty, priority, patentability, commercial significance, or MATHCERT certification.
