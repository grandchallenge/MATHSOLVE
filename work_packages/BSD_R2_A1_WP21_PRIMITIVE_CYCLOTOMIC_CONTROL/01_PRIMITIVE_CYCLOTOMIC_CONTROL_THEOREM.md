# WP21 theorem — primitive cyclotomic control with exact local defect

## 1. Setup

Let `E/Q` lie in the protected selected `BSD-R2-A1` class. Put

`A := E[2^infinity]`.

Let

`Q_infty/Q`

be the cyclotomic `Z_2`-extension and write

`Gamma := Gal(Q_infty/Q) ~= Z_2`.

For a place `v` of `Q`, choose a place `w` of `Q_infty` above `v` and put

`Gamma_v := Gal(Q_{infty,w}/Q_v)`,

where the notation means the decomposition group of `w`; it is a closed subgroup of `Gamma`.

At every finite or infinite algebraic extension `F` considered below, the phrase `primitive Kummer Selmer group` means the kernel defined using the full local Kummer image at every place. No Greenberg, strict, relaxed, unramified, or imprimitive replacement is made.

For an infinite algebraic extension such as `Q_infty`, continuous cohomology and the local Kummer condition are understood as direct limits over finite subextensions.

## 2. No `2`-power torsion over the cyclotomic tower

### Theorem `BSD-A1-WP21-TORSION-001`

For the selected residual branch,

`E(Q_infty)[2^infinity]=0`.

Equivalently,

`A^{G_{Q_infty}}=0`.

### Proof

Protected WP12 gives a surjective residual representation

`rho_2:G_Q -> GL_2(F_2) ~= S3`.

The group `GL_2(F_2)` acts transitively on the three nonzero vectors of `E[2]`. The stabilizer of any nonzero vector has order `2`, hence index `3`.

Therefore, for every nonzero point `P in E[2]`, its field of definition `Q(P)` has degree

`[Q(P):Q]=3`.

Every finite subextension of the cyclotomic `Z_2`-extension `Q_infty/Q` has degree a power of `2`. Hence no degree-`3` field `Q(P)` can lie inside `Q_infty`. Thus

`E[2](Q_infty)=0`.

Now suppose `R in E(Q_infty)` has order `2^n` for some `n>=1`. Then

`2^(n-1) R`

is a nonzero point of `E[2](Q_infty)`, contradiction. Therefore no nonzero `2`-power torsion point is rational over `Q_infty`, proving the claim. QED.

## 3. Global restriction is an isomorphism

### Theorem `BSD-A1-WP21-GLOBAL-001`

Restriction induces an isomorphism

`res_global:H^1(Q,A) -> H^1(Q_infty,A)^Gamma`.

### Proof

Inflation-restriction for

`1 -> G_{Q_infty} -> G_Q -> Gamma -> 1`

gives the exact segment

`0 -> H^1(Gamma,A^{G_{Q_infty}})
   -> H^1(Q,A)
   -> H^1(Q_infty,A)^Gamma
   -> H^2(Gamma,A^{G_{Q_infty}})`.

By Theorem `BSD-A1-WP21-TORSION-001`,

`A^{G_{Q_infty}}=0`.

Both outer cohomology groups are therefore zero. The restriction map is an isomorphism. QED.

This theorem is stronger than merely asserting injectivity: on the protected `S3` branch there is no global control kernel and no global control cokernel in degree one.

## 4. Exact local Kummer quotient

Let `F` be a local field of characteristic zero, or a directed union of such fields inside a fixed algebraic closure.

For each `n`, the Kummer sequence gives

`0 -> E(F)/2^n E(F)
   -> H^1(F,E[2^n])
   -> H^1(F,E)[2^n]
   -> 0`.

Passing to the direct limit over `n` gives

`0 -> E(F) tensor (Q_2/Z_2)
   -> H^1(F,A)
   -> H^1(F,E)[2^infinity]
   -> 0`.

The image of the first arrow is exactly the infinite-level classical Kummer local condition. Hence:

### Lemma `BSD-A1-WP21-LOCAL-QUOTIENT-001`

There is a canonical identification

`H^1(F,A)/H^1_Kum(F,A)
 ~= H^1(F,E)[2^infinity]`.

No good-ordinary hypothesis is used in this identification and no ordinary local condition appears.

## 5. Local restriction kernels

For a base place `v`, let

`W_v := H^1(Q_v,E)[2^infinity]`

and

`W_{infty,w} := H^1(Q_{infty,w},E)[2^infinity]`.

Define

`K_v := ker(W_v -> W_{infty,w}^{Gamma_v})`.

### Lemma `BSD-A1-WP21-LOCAL-KERNEL-001`

There is a canonical identification

`K_v = H^1(Gamma_v,E(Q_{infty,w}))[2^infinity]`,

where the right side denotes the `2`-primary torsion subgroup of the indicated continuous cohomology group.

### Proof

Inflation-restriction for the extension `Q_{infty,w}/Q_v`, applied to the discrete Galois module `E(overline{Q_v})`, gives an injection

`H^1(Gamma_v,E(Q_{infty,w}))
 -> H^1(Q_v,E)`

whose image is exactly the kernel of

`H^1(Q_v,E) -> H^1(Q_{infty,w},E)^{Gamma_v}`.

Intersecting this exact kernel with the `2`-primary torsion subgroup of `H^1(Q_v,E)` gives precisely

`ker(H^1(Q_v,E)[2^infinity]
     -> H^1(Q_{infty,w},E)[2^infinity]^{Gamma_v})`.

Because the injection is a homomorphism, the elements in its image that are killed by a power of `2` are exactly the image of

`H^1(Gamma_v,E(Q_{infty,w}))[2^infinity]`.

This proves the claimed identification. QED.

At the real place the cyclotomic `Z_2`-extension is totally real and the local field remains `R`; the corresponding restriction is the identity, so its local kernel is zero.

## 6. Global localization notation

Define the base local quotient target

`L_Q := product_v H^1(Q_v,E)[2^infinity]`,

with the localization map

`loc_Q:H^1(Q,A) -> L_Q`

obtained from Lemma `BSD-A1-WP21-LOCAL-QUOTIENT-001` at every place.

Likewise let

`L_infty := product_w H^1(Q_{infty,w},E)[2^infinity]`,

and use the corresponding localization map

`loc_infty:H^1(Q_infty,A) -> L_infty`.

Only the components reached by a global cohomology class matter in the argument; equivalently one may use the usual restricted product formulation. No finiteness assertion about the unrestricted product is needed.

Local restriction gives a map

`res_loc:L_Q -> L_infty^Gamma`.

Set

`K_loc := ker(res_loc)`.

After choosing one `w|v` for each `v`, the kernel is represented placewise by the `K_v` above; the permutation of primes over `v` is absorbed by the standard decomposition-group identification.

Define the **primitive local control defect**

`C_E := im(loc_Q) intersect K_loc`

as a subgroup of `L_Q`.

This definition is intrinsic: it is the part of the local restriction kernel that is actually hit by global classes.

## 7. Exact primitive control theorem

Write

`Sel_Q := Sel_{2^infinity}^{Kum}(E/Q)`

and

`Sel_infty := Sel_{2^infinity}^{Kum}(E/Q_infty)`.

### Theorem `BSD-A1-WP21-CONTROL-001`

Restriction gives a canonical short exact sequence

`0 -> Sel_Q
   -> Sel_infty^Gamma
   -> C_E
   -> 0`.

### Proof

By Theorem `BSD-A1-WP21-GLOBAL-001`, every element of

`H^1(Q_infty,A)^Gamma`

has a unique preimage in `H^1(Q,A)`.

The localization maps commute with restriction. Therefore a base Selmer class restricts to a `Gamma`-invariant primitive Selmer class, giving an injective map

`Sel_Q -> Sel_infty^Gamma`.

Now take `y in Sel_infty^Gamma`. Let `x in H^1(Q,A)` be its unique global preimage. Since `y` satisfies every primitive Kummer local condition upstairs,

`res_loc(loc_Q(x))=loc_infty(y)=0`.

Hence

`loc_Q(x) in im(loc_Q) intersect K_loc = C_E`.

This defines a homomorphism

`Sel_infty^Gamma -> C_E`.

Its kernel consists exactly of those `y` whose unique base preimage `x` has `loc_Q(x)=0`, namely those `x in Sel_Q`. Thus the kernel is the image of `Sel_Q`.

Conversely, let `z in C_E`. By definition, `z=loc_Q(x)` for some `x in H^1(Q,A)`, and `res_loc(z)=0`. The global restriction `y=res_global(x)` therefore has zero localization upstairs, so

`y in Sel_infty^Gamma`.

The constructed map sends `y` to `z`. Hence the map to `C_E` is surjective. The sequence is exact. QED.

### Consequence

The base-to-cyclotomic failure of primitive Selmer control is **purely local** on the selected residual branch. No additional global `H^1` control module exists.

This does not imply that `C_E` is zero.

## 8. Pontryagin-dual specialization sequence

Define

`X_infty := Sel_infty^vee`

as a compact module over

`Lambda := Z_2[[Gamma]]`.

Let

`(X_infty)_Gamma`

denote its topological coinvariants.

For a discrete `Gamma`-module `D`, Pontryagin duality identifies

`(D^Gamma)^vee ~= (D^vee)_Gamma`.

Pontryagin duality is exact on the discrete torsion groups appearing in the short exact sequence above. Thus:

### Corollary `BSD-A1-WP21-DUAL-CONTROL-001`

There is a canonical short exact sequence of compact `Z_2`-modules

`0 -> C_E^vee
   -> (X_infty)_Gamma
   -> X_E
   -> 0`,

where protected WP16B's base module is

`X_E = Sel_{2^infinity}^{Kum}(E/Q)^vee`.

Hence the augmentation specialization of the primitive cyclotomic dual Selmer module maps **onto the exact protected base object**. Its complete specialization kernel is `C_E^vee`.

## 9. What WP21 proves about D1

Protected WP20's D1 asked for a literal-`p=2` primitive determinant datum specializing to `X_E`, or exact accounting of every comparison defect.

WP21 removes the global specialization uncertainty. Any cyclotomic primitive determinant route now has only the following specialization defect:

`C_E^vee = (im(loc_Q) intersect K_loc)^vee`,

with placewise ambient local kernels

`K_v = H^1(Gamma_v,E(Q_{infty,w}))[2^infinity]`.

Thus a future theorem may either:

1. prove `C_E=0`;
2. compute `C_E` exactly and carry its Fitting/length contribution;
3. construct a determinant complex whose specialization triangle already contains this local defect and hence retains it automatically.

No other global control term may be inserted without justification.

## 10. Refined determinant frontier

WP21 does not prove that `X_infty` is a torsion or projective-dimension-one `Lambda`-module, nor that it admits the square presentation required to apply the literal matrix form of WP20.

It also does not construct an analytic determinant generator.

The remaining D1 work is therefore split into:

### D1a — primitive cyclotomic perfect/determinant realization

Prove an exact perfect-complex or square-presentation realization over `Lambda` whose cohomology/specialization is the primitive Kummer object above and which is compatible with WP20's determinant/Bockstein factorization.

Boundary:

`MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`.

### D1b — local control-defect evaluation

Determine the exact finite/integral contribution of

`C_E = im(loc_Q) intersect K_loc`,

including the place `2` and every bad semistable prime, with both WP13 Tamagawa regimes retained.

Boundary:

`MISSING_P2_PRIMITIVE_LOCAL_CONTROL_DEFECT_EVALUATION`.

### D1c — analytic determinant generator at `(2)`

Identify an integral analytic/Euler-system determinant element and determine its height-one `(2)` exponent, rather than only its localization away from `(2)`.

Boundary:

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

D2 remains separately:

`MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`.

## 11. Claim firewall

WP21 proves only the exact control sequence above. It does not prove:

- `C_E=0` or finite;
- Mazur's control theorem at `p=2`;
- equality of Kummer and Greenberg local conditions;
- a formula for `C_E` in terms of Tamagawa numbers;
- `Lambda`-torsionness or perfectness of `X_infty`;
- a cyclotomic main conjecture at the height-one prime `(2)`;
- an analytic determinant identity;
- the WP20 D2 regulator/complex-period comparison;
- `BSD-R2-A1`;
- any MATHCERT certification.
