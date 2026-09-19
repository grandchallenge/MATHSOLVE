# YM-D001-R003 — interscale generator comparison audit

## Metadata

- Campaign: `YM-001`.
- Parent debt: `YM-D001`.
- Work package: `YM-D001-INTERSCALE-GENERATOR-INTERFACE`.
- Protected Solve baseline: `c6c2af433dd4e0c60f0eba5f217736ef7c611b2d`.
- Protected Programme baseline: `1f4ba5fabab01c084aefab201c5a4aa594d257fc`.
- Protected Forge source-review baseline: `267670385485b88be0556f6993dc171127139ae1`.
- Admitted predecessors:
  - `YM-D001-R001` at `5b137761c217f96e4cf9afaf270b897025b44480`;
  - `YM-D001-R002` at `f5d7ef5506786d2592d99ae6e75160acbe762dfc`.
- R002 reconciliation checkpoint: `c6c2af433dd4e0c60f0eba5f217736ef7c611b2d`.
- Certification: none; MATHCERT remains the sole certification authority.

## Restricted target

R002 established that the currently admitted fixed-regulator evidence cannot instantiate R001 because no cutoff-indexed physically normalized generator/state-space interface is supplied.

R003 asks the next smaller structural question:

> Do the remaining admitted Yang-Mills theorem interfaces provide a mathematically typed bridge from the fixed-cutoff transfer operators to a cutoff-refined physical generator family and then to the reconstructed continuum Hamiltonian?

The candidate estate is the protected chain

`YM-T-010 -> YM-T-090 -> YM-T-120`

augmented by the independently audited fixed-regulator record `YM-T-190`.

## Result

No admitted interface closes that chain.

The first exact missing object is:

`YM-D001-O004 = MISSING_INTERSCALE_GENERATOR_COMPARISON_MORPHISM`.

The current protected theorem conclusions do not supply comparison maps, embeddings, identifications, or a generalized convergence structure that transports the regulated transfer/Hamiltonian spaces across cutoff refinement and into the limiting reconstructed physical Hilbert space.

This is a theorem-interface noncomposition result. It is not a claim that such maps cannot be constructed.

## Interface decomposition

### Fixed regulator: YM-T-010

`YM-T-010` yields physical positivity and a positive self-adjoint transfer matrix for a lattice approximation at fixed lattice spacing.

Its protected composition state is `COMPOSABLE_ONLY_AT_FIXED_REGULATOR`.

The theorem record does not provide:

- a single physical energy normalization across cutoff values;
- cross-cutoff Hilbert-space maps;
- a resolvent comparison map;
- convergence of generators as the lattice spacing tends to zero.

### Euclidean multiscale RG: YM-T-090

`YM-T-090` is four-dimensional and multiscale, but its protected conclusion is the construction of localized effective actions and recursive coupling renormalization in a small-field approximation.

Its protected composition state is

`NONCOMPOSABLE_UNTIL_LARGE_FIELDS_AND_LIMITS_CLOSED`.

This is an RG interface between Euclidean effective descriptions. The protected theorem conclusion does not construct physical Hilbert spaces or an interscale family of self-adjoint transfer generators, and it does not identify its RG maps with operators that intertwine the `YM-T-010` transfer matrices.

### Continuum reconstruction: YM-T-120

`YM-T-120` reconstructs a positive Hilbert-space QFT with translations and Hamiltonian only after a complete continuum Schwinger hierarchy satisfying the selected Osterwalder-Schrader hypotheses has been established.

Its protected composition state is

`NONCOMPOSABLE_UNTIL_COMPLETE_OS_PROFILE_PROVED`.

It therefore supplies the target-side reconstruction interface, not maps from the regulated lattice Hilbert spaces into the reconstructed continuum Hilbert space.

### Fixed-regulator d=4 manuscript: YM-T-190

The protected Forge audit of `YM-SRC-019` records an explicit lattice spacing `a` in a fixed regulated Wilson-lattice model, but also records that continuum survival `a -> 0` remains to be proved.

It therefore does not supply the missing interscale generator comparison.

## The missing diagram

To feed R001 directly, one needs a rigorously defined comparison diagram of the form

`
(regulated Euclidean data at a)
        |
        | reconstruction / transfer operator
        v
(K_a, H_a^phys)
        |
        | J_a or generalized comparison
        v
(K, H)
`

together with a cutoff trajectory `a -> 0`, a physical energy normalization, and a convergence statement for the identified resolvents.

The exact mathematical implementation need not literally use bounded maps `J_a`; a varying-Hilbert-space resolvent/Mosco/form comparison framework could replace them. But the comparison structure and its spectral-stability theorem must be explicit.

No currently admitted theorem conclusion supplies that vertical comparison.

## Second missing object: scale setting

The audit also retains

`YM-D001-O005 = MISSING_PHYSICAL_ENERGY_SCALE_SETTING`.

Even if one indexed fixed-cutoff transfer matrices by lattice spacing, the protected estate does not supply one declared physical time/energy conversion that turns their spectral data into a common cutoff-independent energy normalization along the target continuum trajectory.

This is independent of the interscale comparison-map problem.

## Cross-debt ownership

The missing interface straddles, but does not collapse, three debts:

- `YM-D003` must construct/control the actual four-dimensional continuum trajectory and limiting Euclidean theory;
- `YM-D002` must establish the complete limiting OS profile if the physical Hilbert space and Hamiltonian are obtained by reconstruction;
- `YM-D001` must connect the regulated physical spectral data to that same limiting Hamiltonian through a comparison/convergence theorem.

`YM-D005` remains separate: a regulated or continuum correlation-decay rate cannot be promoted to the full non-vacuum spectral bottom without its converse/completeness interface.

## False-proof firewalls

1. Euclidean RG maps between effective actions are not automatically Hilbert-space intertwiners between transfer generators.
2. A continuum OS reconstruction theorem does not retroactively identify the regulated Hilbert spaces with the reconstructed limit.
3. A lattice-spacing symbol `a` is not itself a physical scale-setting theorem.
4. Indexing transfer matrices by cutoff does not establish convergence of their generators.
5. An unverified or already-audited noncomposable complete-solution claim cannot fill this interface by assertion.

## Disposition

`YM-D001-R003` establishes a sharper application boundary:

> before a uniform physical spectral lower bound or strong-resolvent limit can be proved, the campaign needs an explicit interscale generator-comparison framework and physical energy scale setting.

The smallest successor is `YM-D001-R004`: choose the comparison formalism itself. Either construct a common-Hilbert/intertwining realization for the regulated generators, or formulate a varying-Hilbert-space convergence theorem strong enough to preserve the R001 spectral exclusion.
