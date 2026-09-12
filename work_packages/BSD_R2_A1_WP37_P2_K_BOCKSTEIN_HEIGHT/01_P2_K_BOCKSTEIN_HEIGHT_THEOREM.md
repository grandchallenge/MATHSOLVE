# WP37 theorem — the literal-`p=2` cyclotomic Bockstein-height object over `K`

## 1. Protected setup

Let `E/Q` lie in the protected selected `BSD-R2-A1` class. Let `K/Q` be the auxiliary imaginary quadratic field protected in WP09. Thus:

- `K` is imaginary quadratic and hence totally imaginary;
- `2` and every prime dividing `N` split in `K`;
- `L(E^d,1) != 0` for the quadratic twist attached to `K/Q`;
- `rank E(K)=1` and the protected finite-level quadratic descent of WP06 applies exactly.

Let

`T := T_2(E)`

and let

`K_infty/K`

be the cyclotomic `Z_2`-extension. Write

`Gamma_K := Gal(K_infty/K)`,

`Lambda_K := Z_2[[Gamma_K]]`.

Let

`C_K,iw`

denote the source-compatible ordinary Selmer complex of Nekovář for `T` over `K_infty`, and let

`C_K := C_K,iw tensor^L_{Lambda_K} Z_2`

be its augmentation specialization.

All statements below concern this source-compatible Selmer complex. They do not identify it silently with the protected primitive classical Kummer module over `Q`.

## 2. Literal `p=2` applicability

Protected MATHFORGE WP37 admits Nekovář, *Selmer complexes*, §§8.5 and 11.1, at exact protected MATHFORGE head

`eceaf6f0f2e10e5bd48afd1ca57f9245669202de`.

The source's duality hypothesis allows `p=2` when the base field is totally imaginary. Since `K` is imaginary quadratic, the source applies without specializing an odd-prime theorem.

### Theorem `BSD-A1-WP37-P2-APPLICABILITY-001`

The cyclotomic Bockstein morphism

`beta_K : C_K -> C_K[1] tensor_Z2 Gamma_K`

and the associated Nekovář Selmer-complex height pairing are defined integrally at `p=2` over the protected field `K`.

### Proof

The protected source audit verifies the literal `p=2` branch of Nekovář's setup under the hypothesis that the base field is totally imaginary. WP09 gives precisely such a `K`. Section 11.1.3 constructs the Bockstein morphism from the augmentation extension, and §11.1.4 composes it with Selmer-complex duality to define the height. No odd-prime specialization is used. QED.

## 3. Rank-one integral height ideal

Use the Weil pairing to identify the dual representation in the self-dual elliptic setting, with the source-compatible dual local conditions. Let

`L_K := H~^1_f(K,T)/tors`

and let

`L_K^dual`

be the corresponding torsion-free rank-one quotient on the dual side whenever the source hypotheses give rank one. The protected analytic rank-one input and standard Kummer injection determine the arithmetic rank-one line, but this theorem does not yet identify `L_K` with a particular primitive Kummer lattice.

Choose:

- a primitive basis `x` of `L_K`;
- a primitive basis `y` of `L_K^dual`;
- a topological generator `gamma` of `Gamma_K`, which identifies the rank-one `Z_2` module `Gamma_K` with `Z_2`.

Write

`eta_K(x,y;gamma) in Z_2`

for the scalar of Nekovář's first cyclotomic height under these choices.

Define the principal ideal

`H_K := (eta_K(x,y;gamma)) subset Z_2`.

### Theorem `BSD-A1-WP37-HEIGHT-IDEAL-001`

`H_K` is independent of all three primitive choices. More precisely, replacing `x`, `y`, or `gamma` by another primitive choice multiplies `eta_K` by an element of `Z_2^x`. Hence the principal ideal `H_K` and the extended valuation

`h_K := ord_2(H_K) in Z_{>=0} union {infinity}`

are canonical for the specified Selmer-complex local conditions.

### Proof

Each rank-one free `Z_2` module has primitive bases differing by multiplication by a unit. The height is `Z_2`-bilinear in the two Selmer arguments, so replacing `x` or `y` by a primitive basis multiplies the scalar by a unit. A topological generator of the procyclic group `Gamma_K ~= Z_2` differs from another by multiplication by an element of `Z_2^x`; the induced coordinate on the rank-one target changes by the inverse unit. Therefore the generated principal ideal is unchanged. If the scalar is zero, every primitive change keeps it zero, giving extended valuation `infinity`. QED.

### Firewall

The theorem produces an exact **ideal**, not a canonical element. It therefore preserves every power of `2` while making no unsupported claim about a preferred determinant-line generator. This is sufficient for length questions but not for D1c.

## 4. Relation to the Bockstein spectral sequence

Protected MATHFORGE WP37 also admits Nekovář §§11.6–11.7. For a DVR `A` and `Lambda=A[[T]]`, the source defines the leading term of a characteristic power series modulo `A^x` and proves an exact valuation identity. Applied with `A=Z_2`, this gives an exact integer invariant.

### Theorem `BSD-A1-WP37-LEADING-LENGTH-001`

Assume the local orthogonality, perfectness, finite-generation, low-degree vanishing, and support hypotheses required by Nekovář §11.7 for `C_K,iw`.

Then:

1. the Bockstein filtration on the specialized Selmer cohomology has exact `Z_2`-lengths;
2. the `2`-adic valuation of the source-defined algebraic characteristic leading term is exactly the source Euler/filtration length of §11.6–11.7;
3. if the first height on the rank-one free line is nondegenerate, the first Bockstein stage is the minimal rank-one leading stage;
4. if `H_K=(0)`, this minimal first-height conclusion is unavailable and the simple-leading-term route has acquired extra order of vanishing.

### Proof

Items (1)–(3) are the literal content of the admitted §11.6–11.7 interface specialized to the DVR `Z_2`: Lemma 11.6.8 identifies the valuation of the characteristic leading term with the integer `a_A`, and Proposition 11.7.6 identifies the relevant filtered lengths under its stated hypotheses. The first height is induced by the first Bockstein differential, so nondegeneracy gives the minimal first-height case. If `H_K=(0)`, the rank-one scalar of that first differential vanishes, so that nondegeneracy hypothesis fails; no later-stage equality is inferred by this package. QED.

## 5. Exact comparison to protected WP20

Protected WP20 is an abstract rank-one determinant theorem over

`S=Z_2[[T]]`.

For a square presentation `A(T)` whose specialization has rank defect one, it defines a Bockstein ideal `B_A` and proves

`(coeff_T det A(T)) = Fitt^1_Z2(M_0) * B_A`.

Protected WP35 supplies the projective-dimension-one square-presentation input for the primitive classical cyclotomic Kummer module over `Q`; protected WP21/WP36 retain and compute its specialization-control correction.

Nekovář WP37 supplies a Bockstein-height ideal over `K`, but the two Bockstein ideals live on Selmer complexes with not-yet-identified integral lattices and local conditions.

Define the **comparison obligation** `J_{K/Q}` to mean the exact determinant/local-condition comparison required to transport `H_K` to the WP20/WP35 Bockstein ideal after incorporating:

- the ordinary-versus-primitive local-condition comparison at the places above `2`;
- the finite bad-prime local terms;
- the exact WP21/WP36 specialization-control defect;
- restriction/corestriction and integral plus/minus descent from `K` to `Q`.

This is a named obligation, not an assumed unit.

### Theorem `BSD-A1-WP37-D2-REDUCTION-001`

The former broad boundary

`MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`

splits, on the protected imaginary-quadratic lane, into the following necessary comparison problems:

`D2a = MISSING_P2_K_HEIGHT_NONDEGENERACY`,

`D2b = MISSING_P2_K_HEIGHT_TO_PRIMITIVE_KUMMER_LATTICE`,

`D2c = MISSING_P2_DISEGNI_INTERPOLATION_FACTOR_VALUATIONS`,

`D2d = MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_FACTOR_RECONCILIATION`,

`D2e = MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

No additional real-place `p=2` duality defect occurs over `K` itself.

Moreover WP06 proves that, because every place dividing `2N` splits in `K`, the finite-level quadratic-descent **local** defect groups at `2` and at every bad prime vanish. Therefore D2e has no hidden local descent correction at those places; the integral plus/minus overlap and quotient terms of WP06 remain to be retained exactly.

### Proof

The existence of the p=2 Bockstein-height object and its canonical ideal is Theorems `P2-APPLICABILITY-001` and `HEIGHT-IDEAL-001`. The admitted Disegni theorem in WP09 supplies only a normalized p-adic height-to-p-adic-L-derivative equality with explicit interpolation/test-vector factors, so D2c is necessary. The WP00 target uses the complex derivative divided by the Néron–Tate regulator, not the p-adic height, so D2d is necessary and p-adic and real heights may not be identified directly. The protected target is over `Q`, so D2e is necessary. The lattice/local-condition mismatch between the Nekovář complex over `K` and the primitive Kummer determinant over `Q` is exactly D2b. Finally, the first-height leading-term route requires nondegeneracy, giving D2a.

WP06 Proposition 7 proves that splitting of every place dividing `2N` kills the local quadratic-descent defects there at every finite `2`-power level. Its integral plus/minus theorem separately retains the overlap/quotient groups rather than dividing by `2`, so those terms cannot be erased. QED.

## 6. Composition with protected Disegni

WP09 proves the corrected Disegni theorem applies at `p=2` over the same protected `K` and gives

`h_V(P_Pi(f1),P_{Pi^vee}(f2)) / (f3,f4)_Pi`

`= e_{2,infinity}(V_(pi,1))^(-1) * L'_2(V_(pi,1),0) * Q((f1 tensor f2)/(f3 tensor f4)).`

After exact identification of the geometric Heegner line with the Nekovář integral height lattice, this supplies a route

`Bockstein ideal H_K`
`-> p-adic height of the protected Heegner line`
`-> p-adic L-derivative`,

but only with the displayed interpolation and test-vector factors retained.

### Corollary `BSD-A1-WP37-PGZ-COMPOSITION-001`

The question whether a literal-`p=2` Bockstein-height formalism exists in the preferred auxiliary lane is closed.

The remaining problem is arithmetic normalization/nondegeneracy, not existence of the p=2 height construction.

## 7. Surviving frontier

WP37 does not change D1c:

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

For D2, the narrow next boundary is

`MISSING_P2_K_HEIGHT_NONDEGENERACY_AND_INTEGRAL_NORMALIZATION_COMPARISON`.

A successful successor must either:

1. prove the fixed-`p=2` nondegeneracy and compute D2b–D2e exactly; or
2. bypass p-adic-height nondegeneracy with a determinant/derived-height theorem that is itself literal at `p=2` and preserves the same integral normalization data.

`BSD-R2-A1` remains `SELECTED_RESEARCH_TARGET_UNPROVED`.