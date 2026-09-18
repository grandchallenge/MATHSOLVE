# YM-D001-R005 — physical energy scale-setting normal form

## Metadata

- Campaign: `YM-001`.
- Parent debt: `YM-D001`.
- Work package: `YM-D001-PHYSICAL-SCALE-NORMAL-FORM`.
- Protected Solve baseline: `dfdf6beedb85022a4e031d5049c47ef75b116558`.
- Protected Programme baseline: `1f4ba5fabab01c084aefab201c5a4aa594d257fc`.
- Protected Forge source-review baseline: `267670385485b88be0556f6993dc171127139ae1`.
- Admitted predecessor: `YM-D001-R004` at protected merge `eacdde093d7f515f890f055cd46f32a7998fac1d`.
- R004 post-admission reconciliation: `dfdf6beedb85022a4e031d5049c47ef75b116558`.
- Certification: none; MATHCERT remains the sole certification authority.

## Selected target

R004 supplied one sufficient varying-Hilbert comparison theorem but assumed that all regulated generators were already expressed in one common physical energy normalization.

R005 isolates that normalization.

> What exact scalar datum converts a dimensionless regulated transfer/generator gap into a physical energy gap, and what condition is necessary and sufficient for one positive cutoff-uniform physical exclusion?

## Protected source boundary

The protected WP00 normalization audit already states:

- a fixed-lattice transfer gap is regulated evidence only;
- a cutoff-uniform physical gap must be expressed in fixed physical units;
- a positive dimensionless gap `delta(a)>0` at every cutoff is insufficient;
- in a convention where one lattice time step has physical size `a`, a lower bound of the form `inf delta(a)/a > 0` is required;
- the exact scaling formula depends on the transfer normalization and must be derived, not assumed.

The protected theorem ledger does not currently supply the missing Yang-Mills scale-setting theorem. `YM-T-100` is perturbative UV-concordance input only, while `YM-T-150` explicitly retains cutoff-uniform physical scaling as an open hypothesis.

## Result

Let `K_n >= 0` be a dimensionless self-adjoint regulated generator and let `tau_n>0` be the physical time represented by one unit of its dimensionless Euclidean evolution parameter.

Define

`H_n^phys := K_n / tau_n`.

If

`sigma(K_n) subset {0} union [delta_n,infinity)`,

then exactly

`sigma(H_n^phys) subset {0} union [delta_n/tau_n,infinity)`.

Therefore one common physical lower bound `Delta>0` exists eventually if and only if

`liminf_n delta_n/tau_n > 0`

for the actual regulated gaps, or is guaranteed by any proved lower bounds `underline_delta_n` satisfying

`liminf_n underline_delta_n/tau_n > 0`.

This is the exact scale-setting normal form needed by R004.

## Transfer-matrix form

If the regulated transfer operator is normalized as

`T_n = exp(-K_n)`

and its non-vacuum spectrum lies below `r_n<1`, then the corresponding dimensionless generator exclusion is

`delta_n >= -log(r_n)`.

Thus the physical lower bound is

`Delta_n^phys >= -log(r_n)/tau_n`.

A bound on `1-r_n` is not literally the physical energy gap; the logarithm is the exact transfer-to-generator conversion.

## Remaining Yang-Mills datum

R005 does not construct `tau_n`.

For the actual four-dimensional campaign, one still needs a theorem that binds the cutoff trajectory to a physical clock/length calibration. Depending on the construction, this may be expressed through:

- a physically normalized temporal lattice spacing;
- a renormalized anisotropy relation;
- a reference observable fixing one physical scale;
- an equivalent nonperturbative scale-setting construction.

The chosen datum must be tied to the same regulated theory and cutoff trajectory used for `H_n`.

## False-proof firewalls

1. `delta_n>0` for every cutoff does not imply a positive physical limit.
2. Bare coupling flow or perturbative asymptotic freedom does not by itself specify `tau_n` in physical units.
3. A lattice-spacing symbol in source coordinates is not automatically a nonperturbative cross-cutoff physical calibration.
4. The exact transfer energy is `-log r_n / tau_n`, not `(1-r_n)/tau_n` unless an approximation theorem is separately proved.
5. Changing `tau_n` while keeping the same dimensionless operators changes the physical gap; scale setting is therefore independent data.

## Disposition

`YM-D001-R005` closes the abstract scale-conversion theorem and reduces the application problem to one explicit missing scalar calibration `tau_n` along the Yang-Mills cutoff trajectory.

The smallest successor is `YM-D001-R006`: identify or construct a nonperturbative Yang-Mills reference-scale theorem that fixes `tau_a` (or an equivalent physical energy normalization) on the same family to which R004 will be applied.
