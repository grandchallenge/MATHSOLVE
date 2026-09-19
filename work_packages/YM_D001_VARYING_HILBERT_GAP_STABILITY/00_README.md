# YM-D001-R004 — varying-Hilbert spectral-exclusion stability

## Metadata

- Campaign: `YM-001`.
- Parent debt: `YM-D001`.
- Work package: `YM-D001-VARYING-HILBERT-GAP-STABILITY`.
- Protected Solve baseline: `57ca4fab8fe04b83da3c2c0dbc2a3a76860c8170`.
- Protected Programme routing baseline: `1f4ba5fabab01c084aefab201c5a4aa594d257fc`.
- Admitted predecessors:
  - `YM-D001-R001`: common-Hilbert strong-resolvent gap stability;
  - `YM-D001-R002`: current fixed-regulator evidence is insufficient to instantiate R001;
  - `YM-D001-R003`: the protected estate lacks an interscale generator-comparison morphism and common physical scale setting.
- Certification: none; MATHCERT remains the sole certification authority.

## Selected target

R003 exposed two missing inputs:

1. a comparison formalism for regulated physical generators living on cutoff-dependent Hilbert spaces;
2. physical time/energy scale setting across cutoffs.

R004 takes only the first, smaller target.

> Give a sufficient varying-Hilbert-space comparison theorem under which one common positive spectral exclusion survives the cutoff limit.

The theorem is abstract. It does not construct the Yang-Mills Hilbert spaces, identification maps, scale setting, uniform regulated gap, or continuum Hamiltonian.

## Result

The candidate proves the following.

Let `K_n` and `K` be complex Hilbert spaces, let `H_n >= 0` on `K_n` and `H >= 0` on `K` be self-adjoint, and fix one `Delta > 0`.

Assume eventually

`sigma(H_n) subset {0} union [Delta,infinity)`.

Set

`B_n=(I+H_n)^(-1)`, `B=(I+H)^(-1)`.

Suppose there are bounded identification maps

`J_n : K -> K_n`

such that

1. `J_n^* J_n -> I_K` strongly; and
2. for every `psi in K`,
   `||B_n J_n psi - J_n B psi||_{K_n} -> 0`.

Then

`sigma(H) subset {0} union [Delta,infinity)`.

Thus the R001 spectral-exclusion theorem extends to varying Hilbert spaces once the identifications are asymptotically isometric and the bounded resolvents asymptotically intertwine.

## Why the intertwining condition matters

Mere convergence of compressed resolvents

`J_n^* B_n J_n -> B`

is insufficient, even if every `J_n` is an exact isometry.

An exact two-dimensional counterexample mixes the regulated vacuum and excited sectors under compression and produces a scalar limiting energy strictly inside `(0,Delta)`.

The missing hypothesis is not cosmetic: the identification subspaces must become dynamically compatible with the regulated resolvents.

## Why asymptotic isometry matters

Without nondegenerate identification, the intertwining condition can be made vacuous. For example, `J_n=0` intertwines every pair of resolvents but conveys no spectral information.

The condition `J_n^*J_n -> I` prevents this collapse.

## Relation to R001

R001 is recovered by taking

`K_n=K`, `J_n=I`.

R004 does not weaken the need for a uniform physical `Delta`. It changes only the state-space comparison layer.

## Yang-Mills boundary

To apply R004 to YM, future work must still construct:

- actual regulated physical Hilbert spaces `K_a`;
- self-adjoint physical generators `H_a`;
- identification maps or another comparison framework that implies the R004 intertwining condition;
- one common physical energy normalization across cutoffs;
- one cutoff- and volume-uniform `Delta>0`;
- the target limiting physical Hamiltonian `H`;
- any required vacuum-sector control.

R004 therefore closes an abstract comparison-formalism lemma, not `YM-D001`.

## Smallest successor

After R004, the smallest remaining D001 target is not another topology lemma. It is the independent scale-setting input:

`YM-D001-R005 = PHYSICAL_ENERGY_SCALE_SETTING`.

Only after comparison and scale setting are both available is it meaningful to seek a cutoff-uniform physical gap estimate on the actual regulated Yang-Mills family.
