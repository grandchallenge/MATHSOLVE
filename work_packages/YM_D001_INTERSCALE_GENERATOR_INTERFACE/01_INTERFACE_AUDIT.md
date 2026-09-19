# YM-D001-R003 — protected theorem-interface composition audit

## 1. Bound estate

This audit is restricted to protected theorem/source interfaces already admitted to the YM campaign:

- MATH-PROGRAMME theorem ledger at `1f4ba5fabab01c084aefab201c5a4aa594d257fc`;
- MATHFORGE source-scope review at `267670385485b88be0556f6993dc171127139ae1`;
- MATHFORGE theorem-body audit for `YM-SRC-019`;
- protected Solve R001/R002 results.

No new external theorem is imported.

## 2. Required R003 interface

A direct common-Hilbert realization would require data

`I = (a_n, K_n, H_n, J_n, K, H, s_n)`

where:

- `a_n -> 0` is the cutoff sequence;
- `K_n` is the physical regulated Hilbert space;
- `H_n` is the regulated nonnegative self-adjoint generator;
- `s_n > 0` gives the physical energy normalization if it is not already absorbed into `H_n`;
- `J_n` supplies comparison of `K_n` with one limiting/comparison Hilbert space `K`;
- `H` is the target continuum Hamiltonian;
- the comparison is strong enough to state and prove convergence of the negative-point resolvents.

This tuple is only a type signature. A different varying-Hilbert-space formalism is acceptable if it supplies equivalent comparison and spectral-stability content.

## 3. Candidate interfaces

| Record | What it supplies | What R003 still needs |
| --- | --- | --- |
| `YM-T-010` | fixed-regulator reflection positivity and positive self-adjoint transfer matrix | cutoff family, physical generator normalization, interscale Hilbert comparison, convergence |
| `YM-T-090` | 4d small-field localized effective actions and recursive coupling renormalization | large-field closure, physical Hilbert/generator construction, transfer-RG intertwining, continuum limit |
| `YM-T-120` | continuum Hilbert space/translations/Hamiltonian after complete OS hypotheses | the limiting Schwinger hierarchy plus maps from regulated physical spaces to the reconstructed limit |
| `YM-T-190` | fixed-regulator 4d Wilson-lattice sector/correlation structure; lattice spacing present in source | continuum survival, physical spectral bridge, interscale generator comparison |

No row supplies the missing comparison arrow.

## 4. Type-mismatch proof

The protected conclusion of `YM-T-010` has codomain “positive self-adjoint transfer matrix at fixed regulator.”

The protected conclusion of `YM-T-090` has codomain “localized Euclidean effective actions and recursive coupling renormalization.”

The protected conclusion of `YM-T-120` has codomain “reconstructed continuum Hilbert-space QFT and Hamiltonian,” conditional on a complete continuum OS hierarchy.

For these statements to compose into R001, at least one theorem must identify an RG refinement step with a comparison operation on the physical transfer/generator spaces, or must otherwise provide a generalized convergence relation between the regulated generators and the reconstructed Hamiltonian.

No protected conclusion supplies such an identification.

Therefore the composition

`YM-T-010 ; YM-T-090 ; YM-T-120`

is not currently typed as a theorem chain from regulated transfer matrices to a convergent family of physical Hamiltonians.

The Forge audit of `YM-T-190` does not repair the chain: it explicitly leaves continuum survival open.

Hence the admitted estate does not currently instantiate an R001 comparison/convergence framework.

## 5. Why this is stronger than R002

R002 found that `YM-T-010` and `YM-T-030` did not already provide the required cutoff-indexed physical generator family.

R003 searches the remaining plausible bridge interfaces and locates the precise missing arrow:

`regulated physical generator spaces -> limiting physical generator space`.

The issue is not merely absence of a named Hamiltonian `H_a`. Even if one constructs a generator separately at every fixed cutoff, there is no admitted theorem specifying how those varying physical spaces/operators are compared as the cutoff changes.

## 6. Physical scale-setting boundary

A comparison map alone is insufficient. The energy normalization must also be common.

The protected theorem ledger contains coupling normalization, lattice distance, and RG coupling recursion in their source conventions, but no theorem conclusion provides the physical time/energy scale `s_n` needed to compare spectral exclusions across cutoffs along the target continuum trajectory.

Accordingly the R003 frontier has two independent open inputs:

1. interscale generator comparison;
2. physical energy scale setting.

## 7. Non-use of noncomposable claimed solutions

The protected Forge audit already dispositions recent claimed complete-solution routes:

- the `YM-SRC-018` continuum-gap argument has an unclosed spectral inequality step;
- `YM-SRC-019` explicitly leaves continuum mass-gap survival open.

R003 therefore does not use those records to manufacture the missing comparison theorem.

## 8. Result

The exact R003 disposition is

`MISSING_INTERSCALE_GENERATOR_COMPARISON_MORPHISM + MISSING_PHYSICAL_ENERGY_SCALE_SETTING`.

This result does not say that either object is impossible. It identifies the next theorem objects that must exist before the admitted R001 spectral-stability result can be applied to the four-dimensional campaign.
