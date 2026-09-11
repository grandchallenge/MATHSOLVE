# WP35 theorem — primitive cyclotomic square presentation with exact augmentation defect

## 1. Protected setup

Let `E/Q` lie in the protected selected `BSD-R2-A1` class.

Let

`Q_infty/Q`

be the cyclotomic `Z_2`-extension,

`Gamma := Gal(Q_infty/Q)`,

and

`Lambda := Z_2[[Gamma]]`.

Choose a topological generator `gamma` of `Gamma` and put

`T := gamma-1`,

so that

`Lambda ~= Z_2[[T]]`.

Define the primitive classical Kummer dual Selmer modules

`X_infty := Sel_{2^infinity}^{Kum}(E/Q_infty)^vee`

and

`X_E := Sel_{2^infinity}^{Kum}(E/Q)^vee`.

Protected WP16B proves that `X_E` is a finitely generated rank-one `Z_2`-module. Put

`T_E := Tor_{Z_2}(X_E)`.

Protected WP19 proves

`Fitt^1_{Z_2}(X_E)=Fitt^0_{Z_2}(T_E)`.

Protected WP21 proves the exact augmentation-control sequence

`0 -> C_E^vee
   -> (X_infty)_Gamma
   -> X_E
   -> 0`.                                      `(C)`

Protected WP24 and its successors prove that `C_E^vee` is finite and compute its length in terms of the protected local-control data.

Protected MATHFORGE WP35 at

`4cf5f8838541fb15296619ead3aaaf298198fe65`

admits Greenberg's literal-`p=2` source interfaces for the same classical Kummer Selmer object:

- `X_infty` is finitely generated torsion over `Lambda`;
- `X_infty` has no nonzero finite `Lambda`-submodule.

No analytic characteristic-ideal equality is used below.

## 2. Projective dimension one

### Theorem `BSD-A1-WP35-PD1-001`

The `Lambda`-module `X_infty` has projective dimension one.

### Proof

The ring

`Lambda ~= Z_2[[T]]`

is a regular local ring of Krull dimension two, with maximal ideal

`m=(2,T)`.

The module `X_infty` is finitely generated and torsion, so

`dim_Lambda X_infty <= 1`.

It is nonzero: otherwise `(X_infty)_Gamma=0`, contradicting the protected exact sequence `(C)` because its quotient `X_E` has `Z_2`-rank one.

Suppose `depth_Lambda X_infty=0`. Over a Noetherian local ring, depth zero means the maximal ideal is an associated prime. Hence `X_infty` contains a nonzero submodule isomorphic to

`Lambda/m ~= F_2`.

That is a nonzero finite `Lambda`-submodule, contradicting the protected WP35 source-qualified finite-submodule exclusion.

Therefore

`depth_Lambda X_infty >= 1`.

Since depth is at most module dimension and the module is nonzero torsion,

`depth_Lambda X_infty=1`.

A regular local ring has finite global dimension equal to its Krull dimension. Hence `X_infty` has finite projective dimension, and the Auslander-Buchsbaum formula gives

`pd_Lambda X_infty
 = depth Lambda - depth X_infty
 = 2-1
 = 1`.

QED.

## 3. Square finite-free presentation

### Corollary `BSD-A1-WP35-SQUARE-001`

There is an integer `r>=1` and an exact sequence

`0 -> Lambda^r --A(T)--> Lambda^r -> X_infty -> 0`.        `(P)`

In particular, `X_infty` is represented by a two-term perfect complex of finite free `Lambda`-modules.

### Proof

Projective dimension one gives a finite projective resolution

`0 -> P_1 -> P_0 -> X_infty -> 0`.

Finite projective modules over the local ring `Lambda` are finite free, so write

`P_1 ~= Lambda^a`,

`P_0 ~= Lambda^b`.

Tensoring with the fraction field of `Lambda` and using that `X_infty` is torsion gives

`a=b`.

Call the common rank `r`. Since `X_infty` is nonzero, `r>=1` after removing any common contractible free summands if necessary. This gives `(P)`.

QED.

The square presentation is not canonical. Changing free bases replaces `A(T)` by

`U(T)A(T)V(T)`

with `U,V in GL_r(Lambda)`. Protected WP20 proves that the first-order ideal factorization used below is invariant under such basis changes.

## 4. Augmentation specialization

Put

`R:=Lambda/(T) ~= Z_2`

and

`A_0:=A(0)`.

Define

`M_0:=coker(A_0:R^r -> R^r)`.

### Lemma `BSD-A1-WP35-AUGMENT-001`

There is a canonical isomorphism

`M_0 ~= (X_infty)_Gamma`.

### Proof

Tensor the right-exact part of `(P)` with `R=Lambda/(T)`:

`R^r --A_0--> R^r -> X_infty tensor_Lambda R -> 0`.

Therefore

`coker(A_0) ~= X_infty tensor_Lambda R`.

For a compact `Lambda`-module, tensoring by the augmentation quotient is the topological coinvariant quotient, so

`X_infty tensor_Lambda R ~= (X_infty)_Gamma`.

QED.

Combining this with protected WP21 gives the canonical exact sequence

`0 -> C_E^vee -> M_0 -> X_E -> 0`.                 `(S)`

Because `C_E^vee` is finite and `X_E` has rank one over `R`, the module `M_0` also has rank one.

Consequently

`rank_{Q_2}(A_0)=r-1`.                             `(R1)`

Indeed, the cokernel of `A_0` has `Q_2`-dimension one after tensoring with `Q_2`.

Thus the exact corank-one hypothesis of protected WP20 is satisfied.

## 5. The finite specialization defect is exactly `C_E^vee`

### Lemma `BSD-A1-WP35-TORSION-001`

The exact sequence `(S)` induces a canonical short exact sequence of finite `Z_2`-modules

`0 -> C_E^vee
   -> Tor_R(M_0)
   -> T_E
   -> 0`.                                          `(T)`

### Proof

The module `C_E^vee` is finite, hence torsion, so its image in `M_0` lies in `Tor_R(M_0)`.

Let `x in T_E`. Choose a lift `m in M_0` under `(S)`. Since `x` is torsion, there is `n>=0` with

`2^n x=0`.

Hence

`2^n m in C_E^vee`.

Because `C_E^vee` is finite, some further power `2^k` kills `2^n m`. Thus

`2^{n+k}m=0`,

so `m in Tor_R(M_0)`. Therefore

`Tor_R(M_0) -> T_E`

is surjective.

Its kernel is the kernel of `M_0 -> X_E`, namely `C_E^vee`, because that finite module already lies in `Tor_R(M_0)`.

This proves `(T)`. QED.

### Corollary `BSD-A1-WP35-LENGTH-001`

`len_R Tor_R(M_0)
 = len_R C_E^vee + len_R T_E`.                     `(L)`

This is immediate from `(T)`.

## 6. Exact first-Fitting factorization at augmentation

Protected WP19 proves for any rank-one finite-generated `Z_2` module with finite torsion, by the same DVR structure calculation used there, that its first Fitting ideal is the zeroth Fitting ideal of its torsion submodule.

Applying that calculation to `M_0` and using `(T)` gives:

### Theorem `BSD-A1-WP35-FITTING-001`

`Fitt^1_R(M_0)
 = Fitt^0_R(C_E^vee) * Fitt^1_R(X_E)`.             `(F)`

### Proof

Since `M_0` has rank one and finite torsion,

`Fitt^1_R(M_0)=Fitt^0_R(Tor_R(M_0))`.

Over the DVR `R=Z_2`, a finite module `N` satisfies

`Fitt^0_R(N)=2^{len_R N}R`.

Thus `(L)` gives

`Fitt^0_R(Tor_R(M_0))
 = 2^{len C_E^vee + len T_E}R
 = Fitt^0_R(C_E^vee) * Fitt^0_R(T_E)`.

Protected WP19 identifies

`Fitt^0_R(T_E)=Fitt^1_R(X_E)`.

Substitution proves `(F)`. QED.

Therefore the complete finite discrepancy between augmentation specialization of the primitive cyclotomic square presentation and the protected base module `X_E` is precisely `C_E^vee`. No additional finite specialization factor is present.

## 7. Composition with the protected WP20 determinant theorem

Write

`A(T)=A_0 + T A_1 + T^2 A_2 + ...`.

By `(R1)`, protected WP20 applies to this exact square presentation. Let

`B_A`

be WP20's intrinsic rank-one Bockstein ideal attached to the first-order map

`ker(A_0) -> M_0/Tor_R(M_0)`.

### Theorem `BSD-A1-WP35-DET-001`

One has the exact ideal identity

`(coeff_T det A(T))R
 = Fitt^0_R(C_E^vee)
   * Fitt^1_R(X_E)
   * B_A`.                                         `(D)`

### Proof

Protected WP20 gives

`(coeff_T det A(T))R
 = Fitt^1_R(M_0) * B_A`.

Insert `(F)`. QED.

If the coefficient `coeff_T det A(T)` is nonzero, then `(D)` gives the conditional valuation identity

`v_2(coeff_T det A(T))
 = len_R C_E^vee
   + len_R T_E
   + v_2(B_A)`.                                    `(V)`

No valuation is assigned when the coefficient is zero.

Protected WP16A/WP16B give

`len_R T_E = lim_n (ord_2 #Sel_{2^n}(E/Q)-n)`.

Protected WP24 gives

`len_R C_E^vee
 = 2v_2(3-a_2)
   + sum_{ell|N}v_2(c_ell)
   - rho_E`,

with later protected work refining `rho_E` and WP31 reducing the remaining place-2 datum to the finite twisted-reciprocity exponent. These protected formulas can be substituted into `(V)` when their remaining local datum is evaluated; WP35 does not evaluate it.

## 8. D1a closure

Protected WP21 defined D1a as the need to construct an exact primitive cyclotomic perfect/determinant realization over `Lambda` whose specialization is the primitive Kummer object, or to account exactly for every finite specialization defect, in a form compatible with WP20.

WP35 supplies exactly that object:

- `(P)` is a literal-`p=2` square finite-free `Lambda` presentation of the protected primitive cyclotomic dual Selmer module;
- `(S)` specializes it to the exact protected base primitive module `X_E` with kernel exactly `C_E^vee`;
- `(T)` and `(F)` compute the complete finite augmentation defect;
- `(D)` composes the presentation directly with WP20's determinant/Bockstein factorization.

Accordingly the boundary

`MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`

is closed in its square-presentation plus exact specialization-defect-accounting sense.

This does not close the analytic determinant or Bockstein normalization obligations below.

## 9. Remaining determinant-side boundaries

### D1c — analytic determinant generator at `(2)`

WP35 constructs an algebraic determinant presentation but does not prove that

`det A(T)`

or any unit multiple of it is the protected analytic/Euler-system determinant generator with the correct height-one `(2)` exponent.

The controlling boundary remains

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

### D2 — Bockstein to WP00 normalization

WP35 carries the intrinsic Bockstein ideal `B_A` but does not identify it with the protected WP00 regulator/period normalization.

The controlling boundary remains

`MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`.

### Local WP31 boundary

The finite twisted-reciprocity exponent remains unevaluated:

`MISSING_P2_FINITE_TWISTED_RECIPROCITY_EXPONENT`.

Its contribution enters through the already protected exact formula for `len C_E^vee`; it is not a new specialization defect.

## 10. Claim firewall

WP35 does not prove:

- a cyclotomic main conjecture at the height-one prime `(2)`;
- equality of `det A(T)` with a Kato, Mazur-Swinnerton-Dyer, or other analytic `2`-adic L-function;
- nonvanishing of the first determinant coefficient;
- equality of `B_A` with a p-adic height, complex regulator, or WP00 normalization;
- a value of the WP31 twisted-reciprocity exponent;
- `BSD-R2-A1`;
- theorem novelty, priority, patentability, commercial significance, or MATHCERT certification.

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED` remains unchanged.