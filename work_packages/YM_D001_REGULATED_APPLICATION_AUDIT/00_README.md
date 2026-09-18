# YM-D001-R002 — regulated-evidence application audit

## Metadata

- Campaign: `YM-001`.
- Parent debt: `YM-D001`.
- Work package: `YM-D001-REGULATED-APPLICATION-AUDIT`.
- Protected Solve baseline: `ebbb049295c39281cc30a2b8e2a1d01f7fb66005`.
- Protected Programme routing baseline: `1f4ba5fabab01c084aefab201c5a4aa594d257fc`.
- Protected Forge source-review baseline: `267670385485b88be0556f6993dc171127139ae1`.
- Admitted predecessor theorem: `YM-D001-R001` at protected merge `5b137761c217f96e4cf9afaf270b897025b44480`.
- Target state: `SELECTED_RESTRICTED_TARGET__SOURCE_SUFFICIENCY_FALSIFICATION`.
- Certification: none; MATHCERT remains the sole certification authority.

## Selected question

The admitted theorem `YM-D001-R001` says that one common spectral exclusion in fixed physical units survives strong convergence of the negative-point resolvents, once the regulated Hamiltonians have already been put on an identified comparison Hilbert space.

The next bounded question is therefore not another abstract operator-topology lemma. It is:

> Do the currently admitted Yang-Mills inputs `YM-T-010` and `YM-T-030` actually provide the regulated operator family, physical scaling, state-space comparison, uniform spectral exclusion, and convergence data needed to instantiate `YM-D001-R001`?

This package audits that question against the protected Programme theorem ledger, the protected Forge source-scope review, and the primary theorem statement for Shen–Zhu–Zhu.

## Result

They do not.

The first exact obstruction is:

`YM-D001-O001 = MISSING_CONTINUUM_INDEXED_PHYSICAL_HAMILTONIAN_FAMILY`.

The current protected evidence does not supply a family

`(a, V) -> H_{a,V}^{phys}`

of nonnegative self-adjoint generators in one declared physical energy normalization, together with comparison maps into a common Hilbert space or generalized comparison framework.

This obstruction is prior to proving a uniform gap or strong-resolvent convergence: without the regulated operator family and its comparison maps, those statements are not yet well-typed.

## Evidence split

### YM-T-010

The protected Programme ledger records `YM-T-010` as reflection positivity and a positive self-adjoint transfer matrix for lattice gauge approximations at **fixed lattice spacing**. Its composition state is explicitly

`COMPOSABLE_ONLY_AT_FIXED_REGULATOR`.

Its retained residual hypotheses include the thermodynamic limit, continuum limit, OS reconstruction of the limiting theory, and spectral stability.

Thus `YM-T-010` supplies a fixed-regulator transfer-operator interface. It does not supply a cutoff-indexed physical Hamiltonian family, cross-regulator state-space identification, or generator convergence.

### YM-T-030

The protected Programme ledger records `YM-T-030` as an infinite-volume **fixed-regulator strong-coupling** lattice result. The primary source is:

Hao Shen, Rongchan Zhu, Xiangchan Zhu, *A Stochastic Analysis Approach to Lattice Yang-Mills at Strong Coupling*, Communications in Mathematical Physics 400 (2023), 805–851, DOI `10.1007/s00220-022-04609-1`, arXiv `2204.12737v1`.

The source model is written with **unit lattice spacing** and action

`S(Q) = N beta Re sum_p Tr(Q_p)`.

Its strong-coupling Assumption 1.1 requires, in dimension `d=4`,

- for `SU(N)`: `|beta| < 1/48`;
- for `SO(N)`: `|beta| < (N-2)/(96N)`.

Corollary 1.6 proves exponential covariance decay for separated smooth cylinder observables,

`Cov(f,g) <= C exp(-c_N d(Lambda_f,Lambda_g)) (...)`,

where the distance is lattice graph distance and `c_N` depends on the source strong-coupling constants, `N`, and `d`.

That is a rigorous lattice correlation-decay result. It is **not** a theorem of the form

`sigma(H_a) subset {0} union [Delta,infinity)`

for a cutoff-indexed Hamiltonian family in fixed physical units, and the paper does not provide the regulator-to-continuum generator convergence needed by R001.

## Why the obstruction is first

R001 requires the following data before its spectral-stability conclusion can even be invoked:

1. physically rescaled nonnegative self-adjoint regulated generators;
2. a common comparison Hilbert space or a rigorously specified generalized comparison framework;
3. one fixed positive `Delta` in the same physical energy units;
4. strong convergence of the bounded resolvents to the target continuum resolvent.

The current evidence supplies none of these as a cross-regulator package. In particular, `YM-T-030` has unit lattice spacing rather than a theorem parameter `a -> 0`, while `YM-T-010` remains fixed-regulator. Therefore the current records cannot instantiate item 1 together with item 2, so items 3 and 4 cannot yet be posed for that evidence.

## Secondary noncomposition findings

### Correlation gap is not automatically a Hamiltonian spectral gap

The source calls Corollary 1.6 a mass-gap result, but its proved statement is exponential decay of covariance in lattice spatial distance for a large class of cylinder observables. The current protected evidence contains no theorem identifying its decay constant with the bottom of the spectrum of the `YM-T-010` transfer generator for the full physical non-vacuum sector.

Promoting the covariance exponent directly to the `Delta` required by R001 would cross the existing `YM-D005` observable-completeness/spectral-converse firewall.

### Strong-coupling domain is not a continuum-trajectory theorem

`YM-T-030` is proved in an explicit strong-coupling neighborhood of `beta=0`. The protected `YM-T-150` route, by contrast, requires a trajectory approaching the asymptotically free continuum theory.

This package does **not** assert a theorem that no useful continuation from the strong-coupling region can exist. It records the narrower exact fact: no currently admitted source theorem supplies a cutoff trajectory that remains inside the hypotheses of `YM-T-030` while also reaching the required four-dimensional continuum target.

### Infinite volume is not continuum

`YM-T-030` does discharge an infinite-volume limit at fixed regulator under its hypotheses. That limit may not be substituted for `a -> 0`; thermodynamic and ultraviolet limits remain distinct obligations.

## False-proof firewalls

1. Do not identify the lattice covariance exponent `c_N` with a physical Hamiltonian spectral gap without a theorem connecting the same observable class to the transfer-generator spectrum.
2. Do not restore a physical lattice spacing by dimensional analysis and declare `c_N/a` to be a cutoff-uniform physical gap. The source theorem does not supply the required scale-setting trajectory.
3. Do not compose a fixed-regulator transfer-matrix theorem with a separate fixed-regulator spatial-correlation theorem as though they already act on one cutoff-indexed family with common domains and Hilbert-space comparison maps.
4. Do not treat the infinite-volume limit as the continuum limit.
5. Do not infer that the strong-coupling theorem applies along the asymptotically free continuum trajectory merely because both concern lattice Yang-Mills.

## Disposition

`YM-D001-R002` succeeds as a **falsification of current-evidence sufficiency**.

It does not discharge `YM-D001`. It reduces the next search to a concrete missing interface:

> construct or locate a theorem that supplies a cutoff-indexed, physically normalized family of regulated generators with explicit state-space comparison, before asking whether one common spectral exclusion and strong-resolvent convergence can be proved.

The natural successor is `YM-D001-R003`: search the admitted source estate for such a regulator-to-generator interface, and if none exists, isolate whether the missing construction belongs irreducibly to `YM-D002`/OS reconstruction or `YM-D003`/continuum construction.
