# WP33 theorem — exact odd bad-prime `2`-adic point completion

## 1. Setup

Let `E/Q` lie in the protected selected `BSD-R2-A1` class. Let `ell|N` be an odd bad prime.

Protected semistability implies multiplicative reduction at `ell`. Put

`F := Q_ell`,

and define

`a_ell := +1`

for split multiplicative reduction and

`a_ell := -1`

for nonsplit multiplicative reduction.

Write

`E(F)^wedge_2 := inverse_limit_m E(F)/2^m E(F)`.

The corrected protected Burns–Macias Castillo source interface at MATHFORGE

`3966bccfe4c8e788f0ca978b5d62cd2e20119043`

shows that `E(F)^wedge_2` occurs as a finite nonarchimedean comparison term in equation (20).

WP33 computes that term.

## 2. Neron filtration

Protected WP22 supplies the exact Neron filtration

`0 -> E_1(F) -> E_0(F) -> Gbar(F_ell) -> 0`

and

`0 -> E_0(F) -> E(F) -> Phi(F_ell) -> 0`,

where:

- `E_1(F)` is the formal subgroup;
- `Gbar` is the connected identity component of the special fibre;
- `Phi` is the Neron component group.

For multiplicative reduction, `Gbar` is a one-dimensional torus.

Protected WP22 also imports the WP13 component calculation:

- split type `I_n`: `#Phi(F_ell)=c_ell=n`;
- nonsplit type `I_n`: Frobenius acts by `-1` on the geometric component group and `#Phi(F_ell)=c_ell=gcd(2,n)`.

## 3. The formal subgroup disappears from the `2`-adic completion

### Lemma `BSD-A1-WP33-FORMAL-KILL-001`

For every `m>=1`, multiplication by `2^m` is an automorphism of `E_1(F)`.

### Proof

The formal subgroup `E_1(F)` is pro-`ell`. Since `ell` is odd, multiplication by `2^m` is an automorphism on every finite `ell`-power quotient and hence on the inverse limit. QED.

Put

`Q_ell^Ner := E(F)/E_1(F)`.

This group is finite.

### Lemma `BSD-A1-WP33-FINITE-QUOTIENT-001`

For every `m>=1`, the quotient map induces an isomorphism

`E(F)/2^m E(F) ~= Q_ell^Ner / 2^m Q_ell^Ner`.

Consequently

`E(F)^wedge_2 ~= (Q_ell^Ner)^wedge_2`.

### Proof

Surjectivity is immediate.

Suppose `x in E(F)` maps to `2^m q(y)` in `Q_ell^Ner`, where `q:E(F)->Q_ell^Ner` is the quotient map. Then

`x-2^m y in E_1(F)`.

By the preceding lemma there is `z in E_1(F)` with

`x-2^m y = 2^m z`.

Hence

`x=2^m(y+z)`.

Thus the kernel is exactly `2^mE(F)`, proving the finite-level isomorphism. Passing to inverse limits gives the completion isomorphism. QED.

For a finite abelian group `Q`, its `2`-adic completion is its maximal `2`-primary quotient. Therefore

`#E(F)^wedge_2 = 2^(v2(#Q_ell^Ner))`.

No splitting of the Neron extension is required.

## 4. Order of the finite Neron quotient

The two Neron sequences give

`0 -> Gbar(F_ell)
   -> Q_ell^Ner
   -> Phi(F_ell)
   -> 0`.

Therefore

`#Q_ell^Ner
 = #Gbar(F_ell) * #Phi(F_ell)`.

It remains only to compute the rational points of the connected torus.

### Lemma `BSD-A1-WP33-TORUS-ORDER-001`

For multiplicative reduction,

`#Gbar(F_ell)=ell-a_ell`.

### Proof

In the split case, `Gbar ~= G_m`, so

`#Gbar(F_ell)=#F_ell^x=ell-1`.

Here `a_ell=+1`.

In the nonsplit case, the one-dimensional torus splits over `F_{ell^2}` and is the norm-one torus for the quadratic residue-field extension. Hence

`Gbar(F_ell)
 ~= ker(N:F_{ell^2}^x -> F_ell^x)`.

The norm on finite fields is surjective. Therefore

`#Gbar(F_ell)
 = (ell^2-1)/(ell-1)
 = ell+1`.

Here `a_ell=-1`. QED.

Combining the torus and component factors yields

`#Q_ell^Ner=(ell-a_ell)c_ell`.

## 5. Exact local completion theorem

### Theorem `BSD-A1-WP33-POINT-COMPLETION-001`

For every odd bad semistable prime `ell|N`,

`#E(Q_ell)^wedge_2
 = 2^(v2(ell-a_ell)+v2(c_ell))`.

Equivalently,

`len_Z2 E(Q_ell)^wedge_2
 = v2(ell-a_ell)+v2(c_ell)`.

Thus:

- split multiplicative:

  `len_Z2 E(Q_ell)^wedge_2
   = v2(ell-1)+v2(c_ell)`;

- nonsplit multiplicative:

  `len_Z2 E(Q_ell)^wedge_2
   = v2(ell+1)+v2(c_ell)`.

### Proof

By Lemma `BSD-A1-WP33-FINITE-QUOTIENT-001`, the `2`-adic completion is the maximal `2`-primary quotient of the finite group `Q_ell^Ner`.

The preceding section gives

`#Q_ell^Ner=(ell-a_ell)c_ell`.

Taking the `2`-part proves the order and length formulas. QED.

### Corollary `BSD-A1-WP33-FITTING-001`

One has

`Fitt^0_Z2(E(Q_ell)^wedge_2)
 = 2^(v2(ell-a_ell)+v2(c_ell)) Z_2`.

### Proof

For every finite `Z_2`-module `M`,

`v2(Fitt^0_Z2(M))=len_Z2(M)`.

Apply the theorem. QED.

## 6. Comparison with the protected odd local-control term

Protected WP22 proves

`len_Z2(K_ell^vee)=v2(c_ell)`

for the ambient primitive cyclotomic local-control kernel at the same odd bad prime.

Define the toric surplus

`tau_ell := v2(ell-a_ell)`.

### Corollary `BSD-A1-WP33-TORIC-SURPLUS-001`

For every odd bad prime,

`len_Z2 E(Q_ell)^wedge_2
 - len_Z2 K_ell^vee
 = tau_ell`.

Equivalently, at the level of fractional principal ideals,

`Fitt^0_Z2(E(Q_ell)^wedge_2)
 / Fitt^0_Z2(K_ell^vee)
 = 2^tau_ell Z_2`.

This identifies exactly what the Burns–Macias finite point-completion term contains beyond the already protected Tamagawa/control contribution.

It does not identify the toric surplus with an analytic determinant factor.

## 7. Total odd-bad term

Define

`D_bad^BM := direct_sum_{ell|N, ell odd} E(Q_ell)^wedge_2`.

The selected conductor is odd, so this is simply the sum over all bad primes.

Put

`tau_bad(E) := sum_{ell|N} v2(ell-a_ell)`.

### Corollary `BSD-A1-WP33-BAD-TOTAL-001`

One has

`len_Z2 D_bad^BM
 = tau_bad(E) + sum_{ell|N} v2(c_ell)`

and

`Fitt^0_Z2(D_bad^BM)
 = 2^(tau_bad(E)+sum_{ell|N}v2(c_ell)) Z_2`.

Protected WP22 gives

`len_Z2 K_bad^vee
 = sum_{ell|N}v2(c_ell)`.

Hence the exact total finite-place surplus is

`len_Z2 D_bad^BM - len_Z2 K_bad^vee
 = tau_bad(E)`.

## 8. Relation to the local Euler denominator: observation only

For multiplicative reduction the standard local Hasse-Weil factor has denominator

`1-a_ell ell^(-s)`.

At `s=1`, since `ell` is a `2`-adic unit,

`v2(1-a_ell/ell)=v2(ell-a_ell)=tau_ell`.

Thus the newly isolated toric surplus has the same `2`-adic valuation as the multiplicative local Euler denominator at `s=1`.

WP33 records only this elementary valuation equality. It does **not** prove that the Burns–Macias determinant normalization uses the corresponding primitive/imprimitive analytic factor with the sign and determinant-line convention required for cancellation.

That comparison is the next source/determinant obligation.

## 9. Refined determinant boundary

WP32 closed the specifically archimedean determinant-valuation defect.

WP33 now computes the odd bad-prime finite comparison terms exactly. The remaining finite-place determinant-normalization question is reduced to

`MISSING_P2_BURNS_MACIAS_TORIC_EULER_FACTOR_RECONCILIATION`.

This boundary asks for an exact source-compatible determinant comparison showing how the factors

`ell-a_ell`

enter when passing between the Burns–Macias perfect-complex determinant and the protected complete Hasse-Weil normalization.

Even if that boundary is closed, D1a, D1c, and D2 still require their separate exact constructions/comparisons.

## 10. Claim firewall

WP33 does not prove:

- cancellation of `tau_ell` or `tau_bad(E)` against an analytic Euler factor in the determinant line;
- exact identification of Burns–Macias `H^2` with the protected primitive module `X_E`;
- a primitive cyclotomic deformation specializing exactly to `X_E`;
- a height-one `(2)` analytic determinant generator;
- the WP20 Bockstein/WP00 normalization;
- the WP31 finite twisted-reciprocity exponent;
- `BSD-R2-A1`;
- theorem novelty, priority, patentability, commercial significance, or MATHCERT certification.
