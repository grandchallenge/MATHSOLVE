# YM-D003-MRS-R002-R2P1-C3-C — Taylor remainder gain

Status: `PROVED__C3_CLOSED`

Parent: `YM-D003-MRS-R002-R2P1-C3`

## Natural slice coordinates

For a fixed MRS slice `j=(i,alpha)`, use the anisotropic dimensionless coordinate norm encoded by the decay factors in Eq. (VII.1). Denote this norm by `|x|_j`, and let `|p|_j,*` be its dual dimensionless momentum norm.

C3-B proves that the fully summed renormalized two-point kernel has uniform spatial moments through order three in this dimensionless metric, hence uniformly bounded momentum derivatives through order three.

## Full local projector

Let `K_j^(2)(p)` denote the translation-invariant renormalized two-point kernel after the C2 Mayer step.

Define `P_2,loc K_j^(2)` to be its Taylor jet through degree two at zero external momentum, projected onto the source-admitted quadratic local basis:

- `A^2/2`;
- `A(-Delta)A`;
- `(dA)^2`.

The `A^2/2` component is separately denoted `P_mass K_j^(2)` and is the only component entering the exact mass-tuning equation.

Define

`R_2 K_j^(2) = (1-P_2,loc)K_j^(2)`.

## Theorem C3-C.1

There is a rho-uniform constant `C_3` such that, for external momentum inside the low-momentum domain of slice `j`,

`|R_2 K_j^(2)(p)| <= C_3 |p|_j,*^3`.

The same estimate holds componentwise in the finite SU(2)/Lorentz tensor decomposition admitted by the quadratic counterterm basis.

### Proof

By C3-B, all third momentum derivatives of the absolutely summed finite-cutoff kernel exist and are bounded uniformly in terminal ultraviolet depth. Apply the multivariable Taylor theorem with integral remainder through degree two in the dimensionless slice momentum coordinates. The degree-zero and degree-two local terms are precisely those retained by `P_2,loc`; any degree-one terms are absent from the source-admitted Euclidean/parity-compatible local quadratic basis and, in any event, are included in the full Taylor jet before projection if present. The integral remainder is bounded by the supremum of third derivatives times `|p|_j,*^3`. Uniformity follows from C3-B. QED.

## Scale-gain interpretation

When a two-point contribution generated at slice `j` is evaluated on an external mode of strictly lower momentum scale, `|p|_j,* < 1`. The remainder therefore carries a positive power of the external/internal scale ratio. This is the irrelevant gain needed for the subsequent scale induction.

No isotropic exponent is invented: the gain is expressed in the exact dimensionless norm dual to the anisotropic decay geometry already present in MRS Eq. (VII.1).

## Consequence

C3 is closed after correcting its original formulation:

1. mass projection alone is not the full localization;
2. the complete quadratic local projector removes the relevant and marginal two-point Taylor jet;
3. C3-B supplies uniform third derivatives;
4. Taylor's theorem supplies the positive-power remainder gain;
5. the mass coefficient remains separately available for the exact recursion.

## Disposition

`R2P1_C3_CLOSED__FULL_TWO_POINT_LOCALIZATION_AND_WEIGHTED_TAYLOR_GAIN_PROVED`

The next node is C4: simultaneous induction for the local two-point coefficients and the running mass counterterm, with quantitative mass response/nondegeneracy sufficient for exact zero-mass tuning.
