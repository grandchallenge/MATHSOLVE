# YM-D003-MRS-R002-R2P1-C2-HV — horizontal and anisotropic vertical link sums

Status: `CLOSED__HORIZONTAL_AND_ANISOTROPIC_VERTICAL_ONE_STEP_SUMS_FINITE`

Parent: `YM-D003-MRS-R002-R2P1-C2 — LINK_TREE_SUMMABILITY`

Protected source:
Magnen–Rivasseau–Sénéor, Section VII, especially Eq. (VII.1) and the immediately following anisotropic vertical-expansion power counting.

## C2-H — horizontal spatial link sum

MRS states that the sliced small-field propagator in an anisotropic slice j=(i,alpha) satisfies a spatial-decay estimate of the form

`|C_j(x-y)| <= K_0 M^i M^alpha * D_{i,alpha}(x-y)`

where `D_{i,alpha}` is a product of polynomially decaying dimensionless factors and the decay exponent q is a large integer.

The horizontal cluster construction uses these decaying propagator/link kernels, and Section VII explicitly identifies link decay as the mechanism by which boxes attached to a fixed box are summed.

### Native lemma C2-H.1

Let a box lattice at fixed (i,alpha) have bounded local multiplicity and let a nonnegative link kernel satisfy

`D(Delta,Delta') <= K (1+d(Delta,Delta'))^{-q}`

for a box distance d on a lattice of finite dimension d_eff, with q>d_eff.

Then

`sup_Delta sum_{Delta'} D(Delta,Delta') < infinity`.

### Proof

The number of boxes at distance in [n,n+1) is O((1+n)^{d_eff-1}). Hence the shell sum is bounded by

`K C sum_{n>=0} (1+n)^{d_eff-1-q}`,

which converges for q>d_eff. QED.

The MRS cutoff construction permits a large decay exponent q and Eq. (VII.1) supplies precisely such dimensionless polynomial spatial decay. Therefore, after passing from points to the corresponding fixed-scale boxes and absorbing finite box-volume/local-multiplicity constants,

`L_H := sup_Delta sum_{Delta'} D_H(Delta,Delta') < infinity`

uniformly in terminal ultraviolet depth rho.

This conclusion uses only fixed-scale decay and does not require global polymer convergence.

## C2-V — anisotropic alpha-direction sum

MRS performs the relevant power counting explicitly.

For the worst derivative trilinear vertex, parity forces at least two such vertices. The pair has the same power counting as a quartic vertex. The source then concludes that a contribution at anisotropic scale alpha attached to a box at scale alpha' can be resummed while:
- spending one coupling constant against the number of finer boxes;
- retaining an adjustable small factor at least of order Lambda;
- retaining an additional factor at least `M^{-(i-alpha)}`.

The source explicitly states that this remaining factor makes the sum over alpha performable and that the dominant contribution comes from alpha=i.

### Native lemma C2-V.1

For M>1,

`sum_{alpha<=i} M^{-(i-alpha)} = sum_{k>=0} M^{-k} = 1/(1-M^{-1})`.

Therefore any vertical-link family majorized by

`D_V(alpha -> i) <= K_V Lambda M^{-(i-alpha)}`

has

`L_V <= K_V Lambda/(1-M^{-1})`.

The bound is independent of terminal ultraviolet depth rho.

This is exactly the functional role required by C1. The constant K_V absorbs the finite local multiplicity and source-admitted power-counting factors; no new scale exponent is introduced.

## Interaction with C1

C1 reduced rooted tree growth to

`q = epsilon C_comb (L_H + L_V + L_M + L_BG) < 1`.

C2-H/V now discharge finiteness and rho-uniformity of L_H and L_V. The smallness of the full q still depends on:
- C2-M: Mayer-link one-step sum L_M;
- C2-BG: background determinant/root activity L_BG;
- the quantitative allocation of the adjustable per-box small factor epsilon.

## Disposition

`C2_H_CLOSED__C2_V_CLOSED__C2_M_AND_C2_BG_ACTIVE`

No claim of complete R2P1-C summability follows yet.
