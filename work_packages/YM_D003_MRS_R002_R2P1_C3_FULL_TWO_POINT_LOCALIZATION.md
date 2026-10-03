# YM-D003-MRS-R002-R2P1-C3 — full two-point localization and remainder gain

Status: `SHARPLY_REFINED__A2_ONLY_LOCALIZATION_INSUFFICIENT`

Protected base: `grandchallenge/MATHSOLVE@1c1c5ae5eb8785888fc0272ad0af5bfe3b4c86a7`

## Correction to the original C3 statement

The earlier proof DAG said that C3 should obtain an irrelevant remainder by subtracting only the local `A^2/2` relevant part of the renormalized two-point kernel.

That is too weak for the full two-point sector.

The protected MRS counterterm grammar contains the relevant quadratic mass operator together with marginal quadratic momentum-dependent operators. In the notation of the source these include the `A^2` mass term and quadratic derivative/wave-function structures of the `A(-Delta)A` and `(dA)^2` type.

Therefore an `A^2/2`-only subtraction may isolate the mass channel needed by MT1, but it leaves marginal quadratic Taylor coefficients in the two-point remainder. Such a remainder cannot be declared irrelevant merely from the mass subtraction.

## Correct decomposition

For each finite-cutoff renormalized 1PI two-point kernel `K_i^(2)` at scale `i`, define two distinct projections.

### Mass projection

`P_mass K_i^(2)` is the local zero-derivative quadratic coefficient in the normalization of MRS Eq. (III.1), i.e. the `A^2/2` channel.

This is the coefficient that feeds the exact mass recursion and MT1.

### Full local two-point projector

`P_2,loc K_i^(2)` is the complete local Taylor jet through superficial degree two, restricted to the quadratic tensor structures admitted by the MRS counterterm basis.

It contains:

- the relevant `A^2/2` mass component;
- the marginal `A(-Delta)A`-type component;
- the marginal `(dA)^2`-type component;
- no operator outside the source-admitted quadratic local basis.

The genuinely irrelevant remainder is

`R_2 K_i^(2) := (1 - P_2,loc) K_i^(2)`.

The mass component is retained separately as

`P_mass P_2,loc K_i^(2)`.

## C3 proof architecture

C3 is now split into three obligations.

### C3-A — local projector concordance

Prove that the finite-cutoff two-point kernel admits the above source-concordant local decomposition and that the projector commutes with the already-defined subtraction-forest bookkeeping at the level required by the scale induction.

### C3-B — weighted moment bound

Strengthen the closed C2 rooted majorant to control sufficiently many spatial moments of the renormalized two-point kernel, uniformly in terminal ultraviolet depth `rho`.

The source permits a large polynomial decay exponent `q` in the sliced propagator bound. Therefore the intended native lemma is that the C2 tree argument survives multiplication by a fixed finite power of polymer diameter after lowering the available decay exponent by that power.

### C3-C — Taylor remainder gain

Use C3-B to justify termwise momentum differentiation of the absolutely summable finite-cutoff two-point expansion. Subtract `P_2,loc` and apply Taylor's theorem to obtain a positive power of the dimensionless external momentum over the internal scale.

Only this full-localization remainder may be used as the irrelevant two-point remainder in C4.

## Claim boundary

This refinement does not alter the exact mass channel. It prevents the mass projection from being confused with full two-point renormalization.

C3 is not yet closed by this file. The next load-bearing native estimate is C3-B: a rho-uniform weighted spatial-moment bound for the already-summable C2 two-point polymer family.

## Disposition

`C3_A2_ONLY_FORMULATION_FALSIFIED_AS_FULL_REMAINDER_STATEMENT__FULL_QUADRATIC_LOCAL_PROJECTOR_REQUIRED__C3_B_WEIGHTED_MOMENT_BOUND_ACTIVE`
