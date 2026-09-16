# BSD R5-LIFT equivariant replay — source and dependency note

## Protected provider authority

The exact protected source authority is

`grandchallenge/MATHFORGE@de2c83c2c440ac357b183b9e1018e9f69c58e1d9`.

It contains:

1. `sources/BSD-001/BKS_P2_EQUIVARIANT_DETERMINANT_R5_LIFT_SOURCE_AUDIT.md`;
2. `sources/BSD-001/KATAOKA_SANO_BASIC_EULER_P2_R5_LIFT_SOURCE_AUDIT.md`.

The provider records only proof architecture and exact replay obligations. It does not itself prove a literal-2 theorem.

## External theorem architecture admitted by the provider

Kataoka-Sano Theorem 3.20 reduces basicness to the finite diagram

`Euler systems -> Kolyvagin systems -> exterior-bidual H^1`

with lower path

`det^{-1} RΓ -> Stark systems -> Kolyvagin systems`.

At fixed finite `R_{m,n}`, the source identifies:

- large auxiliary products through its Lemma 3.22 / BSS Lemma 3.9;
- finite-free global presentations through Proposition 3.23, using local `H^2` vanishing and residual invariant vanishing;
- determinant-to-Stark through Theorem 3.25;
- Stark-to-Kolyvagin through Theorem 3.28 / BSS Theorem 5.2(i);
- Euler-system derivative through Theorem 3.29 / BSS Corollary 6.13.

The published theorem assumes `p>=5`; this package does not invoke that statement literally. It replaces each small-prime-sensitive input with protected literal-2 arguments.

## Protected MATHSOLVE dependencies

### WP60J

Provides the exact selected residual BSS hypotheses and proves the full image

`im(rho_{E,2-adic})=GL_2(Z_2)`

from the protected primitive multiplicative transvection and residual surjectivity. It also proves the residual auxiliary-field `H^1` vanishing and the rank-one `tau` quotient.

The current package uses full image to identify the image over each cyclotomic layer as a determinant-condition subgroup containing `SL_2(Z/2^m)`.

### WP60M

Provides the exact base-coefficient all-level defect theorem: formal H3.2(iii) is false, its restriction kernel has one nonzero class, and the fixed odd multiplicative local condition excludes that class from every selected modified primal and dual Selmer group.

### WP60R

Provides the characteristic-two replacement architecture: quotient-character detection, pairwise localization, odd-relation control, iterative dual killing, connected core graphs, finite core-vertex freeness, and the selected regulator replay over `Z/2^m`.

The current package lifts the *proof mechanism* to `R_{m,n}`; it does not cite the base-ring conclusion as if scalar extension were automatic.

### WP60S

Provides the protected inverse-limit compatibility model for Stark/Kolyvagin systems. The current package adds the independent cyclotomic-layer index `n` and uses the natural finite quotient maps of the Kataoka-Sano diagram.

### WP60T

Provides the selected literal-2 derivative architecture, including `H^0` and Frobenius-injectivity checks and the first-component identity for admitted Euler systems.

### WP32

Provides the integral real-place literal-2 comparison cone. It has equal degree-one and degree-two `Z_2` lengths and a unit determinant/Fitting factor. The current package induces that integral perfect correction to `Z_2[Gamma_n]` before finite coefficient reduction; it does not infer a finite group-ring unit merely from equal cardinalities and does not promote the comparison to a canonical generator trivialization.

### WP35 and WP46A

WP35 supplies the primitive cyclotomic square presentation and retains its exact specialization defect. WP46A identifies the good-ordinary strict higher local term as supported at `(2,gamma-1)`. Hence that term disappears at the height-one localization `(2)`, where `gamma-1` is a unit.

### WP60A-A1

Provides the exact algebraic translation at `Lambda_(2)`: determinant membership is the one-sided Fitting inequality `R5-LIFT`; determinant-generator status is the separate primitivity equality `R5-PRIM`.

## New proof content in this package

This package supplies, rather than imports:

1. local complete-intersection/Gorenstein structure of `R_{m,n}`;
2. equivariant survival of the fixed rank-one `tau` quotient;
3. the cyclotomic-layer `SL_2` cohomology bound and unique defect;
4. the exact trivial-or-order-two auxiliary cyclotomic kernel analysis;
5. Shapiro-compatible exclusion of the unique defect from actual selected Selmer classes;
6. the socle/Nakayama lift of WP60R localization and core-graph machinery;
7. the integral-group-ring real-place correction and equivariant determinant-to-Stark replay;
8. equivariant regulator replay over `R_{m,n}`;
9. the literal-2 finite basicness statement and compatible inverse passage;
10. the support argument showing that the genuine good-ordinary correction does not alter the height-one `(2)` lattice.

## Claim discipline

No external source is represented as proving the literal-2 conclusion. No finite-level base-ring theorem is silently promoted to a group-ring theorem. No valuation-zero correction is called canonically trivial. No primitivity conclusion is inferred from membership.
