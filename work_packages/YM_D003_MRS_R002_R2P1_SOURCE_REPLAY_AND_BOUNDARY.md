# YM-D003-MRS-R002-R2P1 — native source replay and exact theorem boundary

Date: 2026-10-03

Disposition:

`REDUCED__MISSING_MRS_SPECIFIC_RENORMALIZED_1PI_TWO_POINT_POLYMER_NORM_AND_SUBGRAPH_BOUND`

Protected source authorities:

- MATHFORGE `90254084f3d06dcaad1a6a950039396ea85c23f9`
- MATHFORGE `9b6413a7ca5972b7d724ea8f1594c01b8f46cf45`

## Objective attempted

R2P1 asks for the smallest non-circular theorem sufficient to construct the MRS exact mass recursion:

1. define the renormalized local 1PI two-point polymer/subgraph sector;
2. define its relevant `A^2/2` projection;
3. prove a UV-depth-uniform subgraph bound;
4. derive the exact running mass recursion and root/fixed-point theorem.

The primary question in this replay is whether MRS Section V.E/VII already contains enough quantitative estimates to prove step 3 after source reconstruction, or whether step 3 is genuinely new mathematics.

## What MRS supplies

### Renormalization locus

After horizontal and vertical decoupling at a scale, MRS says one is in a position to renormalize the divergent two- and four-point contributions.

It says a Mayer expansion is first required to make those contributions translation invariant and explicitly refers the details of that Mayer expansion to Rivasseau `[R]`.

Once hard-core constraints have been removed, the divergent contributions are cancelled by counterterms.

This gives a clear conceptual grammar for the relevant local sector, but not a theorem-grade MRS-specific norm or bound.

### Exact relevant mass requirement

The same Section V.E distinguishes the relevant mass operator from the marginal terms and states that the mass counterterm must be fixed exactly by a fixed-point method.

Therefore the two-point renormalization and exact mass recursion are not independent pieces: the exact mass choice is part of the renormalized relevant two-point flow.

### Section VII convergence criterion

MRS opens Section VII by saying it **summarizes the reasons for convergence**.

For the Mayer/polymer expansion it identifies the standard sufficient pattern:

- an adjustable small constant per box;
- resummability of all polymers containing a fixed box using decay of the links.

MRS says the structure of these sums is basically similar to the case in `[R]`, except for the important new anisotropic-lattice feature.

### MRS-specific quantitative ingredients

Section VII does supply real model-specific estimates.

It writes a scale-sliced small-field propagator bound with strong spatial decay (VII.1).

It then performs power counting on the worst derivative trilinear vertex, uses parity to force such vertices to occur at least in pairs, and obtains an effective power counting comparable to a quartic vertex.

For the auxiliary anisotropic vertical expansion, it concludes that the contributions can be resummed while retaining a small factor and a further scale-decaying factor.

For horizontal links, it states that spatial decay is enough to resum the links.

For vertices with five or more legs, power counting supplies the necessary irrelevant scale factor.

These estimates explain why the new anisotropic/link structures are not expected to destroy convergence.

### The exact unresolved two-/four-point statement

When MRS reaches the relevant/marginal exceptional sector, the paper states that in the case of two- and four-point functions, **renormalization performs the same task in the usual way**.

No accompanying MRS theorem defines a normed renormalized two-point polymer/subgraph family or states a cutoff-depth-uniform bound on it.

The paper's own introductory qualification remains in force: it does not provide all convergence proofs in detail and assumes familiarity with the constructive arguments in `[R]`.

## Comparison with the scalar template

The scalar FMRS1 critical-mass construction cited by MRS is more explicit at exactly this point:

- its mass counterterm is defined from zero-external-momentum 1PI two-point Mayer graphs;
- its running mass bound is obtained from a theorem controlling the corresponding two-/four-point subgraph sums.

Therefore the proof template itself confirms that a theorem-grade two-point subgraph bound is load-bearing for the exact mass recursion.

The MRS paper gives power-counting and polymer-resummation rationale but not an MRS analogue of that scalar subgraph theorem.

## What cannot be inferred

The Section VII estimates do **not**, by themselves, authorize GCL to invent:

- an exact Banach/polymer norm for the renormalized two-point sector;
- the power of the running coupling in the two-point bound;
- the precise scale weight of the relevant subtraction;
- a Lipschitz constant with respect to `b`;
- a UV-depth-uniform constant;
- a background-field-uniform 1PI response estimate.

Those quantities are exactly what a native proof must establish.

Assigning them without a source theorem or a fresh derivation would turn the MRS proof sketch into an unproved theorem by notation.

## Exact missing theorem

The smallest currently justified native theorem is:

### R2P1-C — MRS renormalized two-point subgraph theorem

For fixed admissible infrared regulator `R` and sufficiently small coupling, define a normed MRS-specific family of renormalized local 1PI two-point polymer/subgraph amplitudes after Mayer hard-core removal and relevant local subtraction.

Prove a scale-recursive estimate with all of the following properties:

1. **summability:** the norm controls the sum over polymers/subgraphs containing a fixed root box;
2. **renormalized relevance control:** after extracting the local `A^2/2` part, the remainder gains the scale decay required by the MRS induction;
3. **UV-depth uniformity:** constants are independent of the terminal ultraviolet depth `rho` for all sufficiently large `rho`;
4. **mass-response control:** the extracted relevant coefficient has enough bounded/Lipschitz or nondegenerate dependence on the running mass counterterm to close the exact mass recursion;
5. **background/gauge compatibility:** the bound remains valid with the MRS background-dependent propagator and gauge-restoring counterterm organization;
6. **Section VI compatibility:** the exact selected quadratic counterterm preserves the normalization/stability interface used in the large-field effective potential.

The exact norm and scale exponents are part of the theorem to be derived. They are not fixed by the existing source packet.

## R2P1-A/B status

The source is sufficient to identify the conceptual grammar:

- divergent two-/four-point objects arise after horizontal/vertical decoupling;
- Mayer expansion removes hard-core constraints to make the divergent pieces translation invariant;
- local counterterms cancel the relevant/marginal parts;
- the quadratic relevant part is the mass channel that must be tuned exactly.

However, a formal 1PI/polymer grammar suitable for proof still has to be reconstructed in the exact MRS notation. R2P1-A/B are therefore **typed conceptually but not theoremized**.

## R2P1 disposition

`R2P1_REDUCED_TO_C__MISSING_MRS_SPECIFIC_RENORMALIZED_1PI_TWO_POINT_POLYMER_NORM_AND_SUBGRAPH_BOUND`

This is a substantive mathematical boundary, not a source-access failure.

The primary paper is available and directly tells us where it stops: the exceptional two-/four-point sector is delegated to “usual” renormalization machinery while Section VII gives a convergence summary rather than the missing theorem.

## Next legitimate native action

A new proof must now build R2P1-C.

The appropriate proof architecture is a simultaneous induction, not a sequential assumption of global convergence:

`renormalized local two-point subgraph bound`
+
`running mass-counterterm bound`
→ next-scale two-point bound
→ next-scale mass bound.

This mirrors the logical structure of the scalar template while requiring every estimate to be re-proved in the MRS SU(2), anisotropic, background-dependent gauge setting.

## Claim boundary

No claim is made that R2P1-C is false or impossible.

No claim is made that MRS's source-stated UV construction is false.

The result is narrower: the theorem needed to make the exact mass recursion rigorous is not contained in the source packet and cannot be obtained by a citation-only transfer. It requires new MRS-specific constructive mathematics.
