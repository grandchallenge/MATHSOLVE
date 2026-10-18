# YM-D003-MRS-R002-R2P1-C3-B — weighted spatial moments

Status: `PROVED__FIXED_FINITE_MOMENTS_UNIFORM_IN_RHO`

Parent: `YM-D003-MRS-R002-R2P1-C3`

## Objective

Upgrade the closed C2 absolute/rooted summability estimate to a fixed finite spatial-moment estimate sufficient for momentum differentiation of the renormalized two-point kernel.

## Input

C2 supplies:

- a rooted spanning-tree majorant for the horizontal/vertical pre-Mayer polymers;
- a convergent native Mayer expansion;
- an adjustable small box activity;
- rho-uniform one-step horizontal and vertical sums.

MRS Eq. (VII.1) supplies polynomial spatial decay with a large integer decay exponent. Hence, for every fixed moment order `r` below the available decay reserve, the horizontal link kernel has a finite weighted one-step sum

`L_H^(r) := sup_Delta sum_Delta' (1+d(Delta,Delta'))^r D_H(Delta,Delta') < infinity`,

uniformly in terminal ultraviolet depth `rho`.

The anisotropic vertical links do not create an uncontrolled macroscopic spatial displacement; their scale sum was already proved geometric in C2-V.

## Lemma C3-B.1 — weighted tree bound

Fix an integer `r >= 1` within the decay reserve. For a connected pre-Mayer polymer `P`, let

`diam(P)`

be the box-metric diameter of its support.

Then, after choosing the adjustable box activity sufficiently small, there is a finite constant `C_r`, independent of `rho`, such that

`sup_Delta0 sum_{P:Delta0 in supp(P)} |z(P)| (1+diam(P))^r <= C_r`.

### Proof

Choose a spanning tree `T` of the occupied-box incidence graph as in C1/C2. For any two boxes in `P`, their distance is bounded by the sum of horizontal geometric edge lengths along the tree path; vertical scale edges contribute only their already-summed local/scale factor.

For a tree with `n` occupied boxes and nonnegative horizontal edge lengths `l_e`,

`diam(P)^r <= (sum_{e in T} l_e)^r <= n^(r-1) sum_{e in T} l_e^r`.

In the rooted tree sum, designate the edge carrying `l_e^r`. Its target sum is bounded by `L_H^(r)`. Every other horizontal edge is bounded by `L_H`, every vertical edge by `L_V`, and the local constructor multiplicity is bounded by `C_comb`.

The remaining factor `n^r` is polynomial in polymer size. The C2 proof permits an exponential reweighting of polymer size because the per-box activity is adjustable: for any fixed `eta>0`,

`n^r <= C(r,eta) exp(eta n)`.

Choose the box activity small enough that the C2 branching parameter remains strictly below one after the extra `exp(eta)` charge per occupied box. The resulting geometric tree sum is finite uniformly in `rho`.

The native Mayer step preserves this weighted bound because its incompatibility criterion was proved with an exponential support-size weight. Thus the post-Mayer connected activities inherit the same fixed finite diameter moment. QED.

## Corollary C3-B.2 — differentiability of the two-point kernel

For every fixed `r` within the decay reserve, the absolutely summed finite-cutoff two-point kernel has bounded momentum derivatives through order `r`, uniformly in terminal ultraviolet depth `rho`, after expressing momenta in the natural dimensionless coordinates of the corresponding slice.

Indeed, differentiating a Fourier factor produces powers of coordinate separation, controlled by Lemma C3-B.1. Absolute weighted summability permits termwise differentiation.

## Required order for C3

Take `r=3`. This is sufficient for a Taylor remainder after subtracting a complete local jet through degree two. If the exact MRS symmetry analysis proves evenness strongly enough to eliminate cubic terms, a fourth-order gain may later be recorded, but C3 does not depend on that strengthening.

## Disposition

`C3_B_CLOSED__UNIFORM_THIRD_MOMENT_AND_THREE_MOMENTUM_DERIVATIVES_AVAILABLE`

The remaining C3 obligation is C3-C: bind the source-admitted quadratic tensor projector to the exact anisotropic slice coordinates and turn the Taylor remainder into the required inter-scale suppression factor.
