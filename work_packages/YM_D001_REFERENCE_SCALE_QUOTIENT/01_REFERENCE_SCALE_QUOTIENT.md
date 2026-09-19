# YM-D001-R006-L001 — reference-scale quotient theorem

## Statement

For each `n`, let

- `delta_n>0` be the exact dimensionless spectral gap of a regulated target generator;
- `epsilon_n>0` be a dimensionless reference energy defined in the same regulated model;
- `tau_n>0` be the physical Euclidean time represented by one dimensionless evolution unit.

Define

`Delta_n := delta_n/tau_n`

and

`M_n := epsilon_n/tau_n`.

Then

`Delta_n = (delta_n/epsilon_n) M_n`.

Consequently:

### Sufficient positive-gap criterion

If

`liminf delta_n/epsilon_n = c > 0`

and

`liminf M_n = m > 0`,

then

`liminf Delta_n >= c m > 0`.

### Convergent reference-scale form

If

`M_n -> M_ref`

for some

`0 < M_ref < infinity`,

then:

- `liminf delta_n/epsilon_n>0` implies a positive cutoff-uniform physical target gap;
- if `delta_n/epsilon_n -> L`, then `Delta_n -> L M_ref`;
- if `delta_n/epsilon_n -> 0`, then `Delta_n -> 0`.

## Proof

The exact identity

`Delta_n = (delta_n/epsilon_n) M_n`

follows from

`Delta_n=delta_n/tau_n`

and

`M_n=epsilon_n/tau_n`.

For the first claim, choose numbers

`0<c'<c`

and

`0<m'<m`.

By the definition of liminf, for all sufficiently large `n`,

`delta_n/epsilon_n >= c'`

and

`M_n >= m'`.

Therefore

`Delta_n >= c'm'`

eventually.

Letting `c'↑c` and `m'↑m` gives

`liminf Delta_n >= cm>0`.

If `M_n -> M_ref in (0,infinity)`, the remaining statements follow from ordinary product limits and the exact identity.

QED.

## Corollary — fixing units by a proved reference scale

Suppose a theorem identifies the regulated reference energies `epsilon_n` with one finite nonzero continuum physical scale, up to a free choice of units.

Choose a unit convention

`M_ref=mu>0`.

If the scale-setting theorem licenses the calibration

`tau_n=epsilon_n/mu`,

then the target physical gap is

`Delta_n=mu * delta_n/epsilon_n`.

Thus the absolute clock variable drops out and the continuum gap problem is reduced to a dimensionless ratio.

The corollary is conditional on the reference-scale theorem. It does not create that theorem.

## FP1 — circular scale fixing

Set

`epsilon_n=delta_n`.

Choose any desired number

`mu>0`

and define

`tau_n=epsilon_n/mu=delta_n/mu`.

Then

`Delta_n=delta_n/tau_n=mu`

for every `n`.

Thus one can obtain any desired positive “physical gap” merely by defining physical units with the target gap itself.

This proves that scale setting by the target spectral gap is circular and evidentially empty.

## FP2 — an uncontrolled reference scale proves nothing

Take

`delta_n/epsilon_n=1`

for every `n`, but let

`M_n=1/n`.

Then

`Delta_n=1/n ->0`.

A positive or even constant dimensionless ratio does not prove a physical gap unless the reference scale itself is independently bounded away from zero in physical units.

## FP3 — a divergent reference scale does not identify a finite continuum theory

Take again

`delta_n/epsilon_n=1`

but `M_n=n`.

Then

`Delta_n=n`.

This does not produce the required finite physical mass scale. It instead shows that a reference observable with no finite continuum normalization cannot serve as the missing R005 calibration.

## Non-circularity contract

For use in `YM-001`, a reference-scale theorem must publish a dependency route showing that its finite nonzero continuum value is not proved using:

- the target physical Hamiltonian gap;
- an inverse correlation length already identified with that gap;
- exponential clustering whose rate was obtained from the gap;
- any theorem whose hypotheses include the desired positive mass scale.

A reference scale may be correlated with the eventual mass gap; it may not be **logically defined or proved nonzero by assuming it**.

## Protected-estate audit

At protected Programme head `1f4ba5fabab01c084aefab201c5a4aa594d257fc` and Forge head `267670385485b88be0556f6993dc171127139ae1`, the admitted theorem/source estate contains no four-dimensional pure-YM reference-scale theorem meeting the above contract.

The estate contains:

- fixed-regulator transfer and correlation results;
- partial four-dimensional Euclidean RG information;
- perturbative asymptotic freedom;
- conditional OS reconstruction interfaces;
- audited noncomposable complete-solution claims.

None proves a finite nonzero, non-circular physical reference scale on the same controlled four-dimensional continuum trajectory.

Therefore R006 closes the abstract ratio reduction while leaving the application object open.
