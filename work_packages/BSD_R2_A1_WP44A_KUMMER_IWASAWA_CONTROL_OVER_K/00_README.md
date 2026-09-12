# BSD-R2-A1 WP44A — primitive Kummer Iwasawa control over `K`

## State

`PROVED_BOUNDED_MODULE_LEVEL_CONTROL`

## Protected predecessors

- MATHSOLVE protected baseline: `608250fd6e666ef73064505ed83f4ff9629803d9`.
- WP21: exact primitive classical-Kummer cyclotomic control over `Q`.
- WP25–WP28: exact local universal-norm quotients and the good-ordinary place-`2` filtration.
- WP39/WP40: exact finite strict-Greenberg/classical-Kummer comparison over the protected imaginary quadratic field `K` and its Poitou–Tate annihilator description.
- WP43A: literal-`p=2` strict-Greenberg cyclotomic augmentation/Bockstein naturality over `K`.

No new external theorem premise is used in this package.

## Result

Let

`K_infty := K Q_infty`

and

`Gamma_K := Gal(K_infty/K) ~= Z_2`.

WP44A proves:

1. `E(K_infty)[2^infinity]=0`;
2. the WP21 primitive-Kummer control argument transports integrally to `K` at `p=2`, giving

   `0 -> Sel_K^Kum -> (Sel_Kinfty^Kum)^Gamma_K -> C_K^Kum -> 0`;

3. after Pontryagin duality,

   `0 -> (C_K^Kum)^vee -> (X_Kinfty^Kum)_Gamma_K -> X_K^Kum -> 0`;

4. at every relevant local place `w` of `K`, the norm-compatible local-point module

   `M_w^Kum := inverse_limit_n E(K_{n,w})^hat_2`

   is a literal integral `Z_2[[Gamma_w]]`-module whose base projection has cokernel exactly the protected local universal-norm quotient `U_w`;
5. because the protected field `K` splits every prime dividing `2N`, the local quotient `U_w` is canonically transported from the corresponding protected `Q_v` calculation of WP25–WP28.

Thus the campaign no longer lacks a Kummer cyclotomic module or exact cohomological specialization over `K`.

## What remains

WP44A does **not** yet construct a perfect Selmer-complex local-condition object for the compact classical-Kummer lattice used in WP39, and it does not identify the derived strict-to-Kummer comparison cone with WP39/WP40.

The surviving D2b boundary is narrowed to

`MISSING_P2_COMPACT_KUMMER_IWASAWA_COMPLEX_LIFT_AND_DERIVED_SPECIALIZATION_OVER_K`.

A successor must:

1. lift the norm-limit Kummer local modules to a controlled/perfect local-condition complex compatible with Nekovář's strict complex;
2. compute derived augmentation, including any `Tor_1`/coinvariant kernel rather than assuming it vanishes;
3. identify the specialized strict-to-Kummer comparison cone map-by-map with the finite WP39 local target and global hit `J_K`;
4. reconcile the extra good-ordinary formal universal-norm term at each place above `2` rather than silently discarding it.

## Claim firewall

This package does not prove:

- that the compact Kummer Iwasawa Selmer complex is already perfect;
- that ordinary coinvariants are the same as derived augmentation;
- that a `Tor_1` or coinvariant kernel vanishes;
- that the full local augmentation defect equals WP39's local target at every place;
- `D_K` equals a Bockstein image/radical;
- fixed-`2` height nondegeneracy;
- D1c;
- global `Q^ord=1`;
- the WP00 real normalization or final quadratic descent;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.