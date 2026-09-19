# YM-D001-R006 — non-circular reference-scale quotient reduction

## Metadata

- Campaign: `YM-001`.
- Parent debt: `YM-D001`.
- Work package: `YM-D001-REFERENCE-SCALE-QUOTIENT`.
- Protected Solve baseline: `3bd2a2722df603143f832c0da5b18983213e8ced`.
- Protected Programme baseline: `1f4ba5fabab01c084aefab201c5a4aa594d257fc`.
- Protected Forge source-review baseline: `267670385485b88be0556f6993dc171127139ae1`.
- Admitted predecessor: `YM-D001-R005` at protected merge `7459be7ffdec1161388b9bfe5f23d19ae9df526e`.
- R005 post-admission reconciliation: `3bd2a2722df603143f832c0da5b18983213e8ced`.
- Certification: none; MATHCERT remains the sole certification authority.

## Selected target

R005 proved that a dimensionless regulated gap `delta_n` becomes the physical gap `delta_n/tau_n`, but the actual Yang-Mills clock calibration `tau_n` remains missing.

R006 asks whether the explicit clock can be eliminated in favor of one independently controlled physical reference scale.

> If the same regulated theory contains a dimensionless reference energy `epsilon_n` whose physical value is known independently and non-circularly, what exact condition on `delta_n/epsilon_n` is sufficient for a positive physical gap?

## Protected source boundary

The protected WP00 dossier already forbids a circular route that fixes the continuum scaling by a correlation length whose positivity is the desired mass-gap conclusion.

A search of the protected YM Programme/Solve/Forge estate at the baselines above found no admitted four-dimensional pure-YM theorem for a Sommer scale, gradient-flow scale, string-tension scale, or other non-circular reference observable that is proved to have a finite nonzero continuum physical value on the target cutoff trajectory.

Thus R006 proves only the abstract ratio theorem and identifies the exact application datum still missing.

## Result

Let

- `delta_n>0` be the exact dimensionless target spectral gap;
- `epsilon_n>0` be a dimensionless reference energy in the **same regulated theory and cutoff trajectory**;
- `tau_n>0` be the physical time calibration from R005.

Define physical energies

`Delta_n^phys = delta_n/tau_n`

and

`M_n^ref = epsilon_n/tau_n`.

Then exactly

`Delta_n^phys = (delta_n/epsilon_n) M_n^ref`.

Therefore, if

`liminf delta_n/epsilon_n > 0`

and the reference scale has an independently proved positive physical lower bound

`liminf M_n^ref > 0`,

then the target physical gaps have a positive liminf.

If moreover

`M_n^ref -> M_ref in (0,infinity)`,

then the physical mass-gap question is reduced to the dimensionless ratio `delta_n/epsilon_n`.

## Reference-scale normalization form

If one has proved that the reference observable converges to a finite nonzero continuum value up to an arbitrary choice of units, one may choose a convention

`M_ref = mu > 0`

and set

`tau_n := epsilon_n/mu`

along the regulated family.

Then

`Delta_n^phys = mu * delta_n/epsilon_n`.

This is a valid change of units only after the reference observable is independently proved to define the same finite nonzero continuum scale. It is not a method for manufacturing that theorem.

## Circularity firewall

The choice

`epsilon_n = delta_n`

is invalid as independent evidence.

If one declares the target gap itself to be the reference and chooses

`tau_n=delta_n/mu`,

then automatically

`Delta_n^phys=mu`.

The claimed “proof” of a positive mass gap would then be true by the definition of the scale. It contains no independent spectral information.

The same firewall applies to any reference observable whose finite nonzero continuum value is known only through a theorem already assuming the target mass gap.

## Remaining Yang-Mills obligation

A valid R006 application requires a reference scale satisfying all of:

1. same four-dimensional pure-YM regulated family and cutoff trajectory;
2. gauge-invariant and mathematically defined at each regulator;
3. independently controlled through the relevant volume and continuum limits;
4. finite and nonzero in the limiting physical theory;
5. no proof dependency on the desired physical mass gap or an equivalent positive correlation length;
6. enough normalization information to relate its dimensionless regulated value to physical units.

No such protected theorem is currently present in the campaign estate.

## Disposition

R006 proves the **reference-scale quotient theorem** and sharpens the application obstruction to

`MISSING_NONCIRCULAR_4D_YM_REFERENCE_SCALE_THEOREM`.

The next material work should not add another abstract unit-conversion lemma. It must either:

- construct such a reference scale natively as part of the four-dimensional continuum theory, which couples R006 to `YM-D003`; or
- admit a source theorem supplying it through the governed Forge/Programme route.

Until then, R004 and R005 cannot be instantiated on the actual Yang-Mills family.
