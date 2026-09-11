# BSD-R2-A1-WP25 — local universal-norm representation of `rho_E`

## Metadata

- Campaign: `BSD-001`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Parent: protected `BSD-R2-A1-WP24-GLOBAL-HIT-POITOU-TATE-CHARACTER`.
- Protected MATHSOLVE baseline: `eac82bf2809ff70317a3542a58247e6a11299bc0`.
- Protected MATHFORGE source admission: `b09faf74936611616465186c8702ea0ce6f36828`.
- Admitted source audit: `sources/BSD-001/TAN_LOCAL_NORM_DUALITY_WP25_SOURCE_AUDIT.md` in MATHFORGE.
- Claim boundary: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.
- Primary type: exact local norm-duality representation theorem for the remaining WP24 scalar.

## Protected input

WP24 proves

`C_E = ker(chi_P|K_loc)`

for the rank-one local Tate character attached to a saturated Mordell-Weil generator `P`, and defines

`rho_E := len_Z2 im(chi_P|K_loc)`.

WP22-WP23 compute every factor of the finite ambient group `K_loc`.

MATHFORGE now protects Tan's exact local theorem interface:

`H^1(Gal(L/K),E(L))^vee
 ~= lim_F E(K)/N_{F/K}E(F)`

for arbitrary local Galois `L/K`, including the selected infinite local cyclotomic `Z_2` extensions.

## WP25 result

For each finite place `v`, let `F_{v,n}/Q_v` be the finite layers of the local cyclotomic extension represented by `Gamma_v`; at places where the decomposition group is trivial there is no defect.

Write

`N_{v,n} := N_{F_{v,n}/Q_v} E(F_{v,n}) subset E(Q_v)`.

The norm images form a nested sequence

`N_{v,n+1} subset N_{v,n}`.

Tan's protected duality identifies

`K_v^vee ~= lim_n E(Q_v)/N_{v,n}`.

Because protected WP22-WP23 prove every nonzero `K_v` finite, the inverse limit is finite. The transition maps between the finite quotients are surjective, hence every projection from the inverse limit is surjective. Their orders are therefore bounded by the order of the finite inverse limit. Since the quotient orders are nondecreasing, they eventually stabilize. Consequently the nested norm images themselves stabilize.

Define the local universal norm subgroup

`N_v^infty := intersection_n N_{v,n}`.

WP25 therefore obtains canonically

`U_v := E(Q_v)/N_v^infty ~= K_v^vee`.

For a saturated global generator `P`, let

`[P]_v in U_v`

be its local universal-norm obstruction class. Under the protected Tan pairing, the local component of the WP24 character is exactly evaluation against `[P]_v`.

Let

`S_def := {v : K_v != 0}`.

The restriction `chi_P|K_loc` corresponds under Pontryagin duality to the tuple

`u(P) := ([P]_v)_{v in S_def} in product_{v in S_def} U_v ~= K_loc^vee`.

Thus

`#im(chi_P|K_loc) = ord(u(P))`.

Define

`rho_v(P) := ord_2(ord([P]_v))`.

Because all groups are finite `2`-groups,

`rho_E = max_{v in S_def} rho_v(P)`.

The protected local sizes give the exact bounds

`rho_2(P) <= 2 ord_2(3-a_2)`,

and, for every odd bad semistable prime,

`rho_ell(P) <= ord_2(c_ell)`.

Odd good primes and the real place have zero local obstruction.

## New narrow boundary

WP25 replaces

`MISSING_P2_GLOBAL_HIT_CHARACTER_IMAGE_LENGTH`

by

`MISSING_P2_SATURATED_GENERATOR_LOCAL_UNIVERSAL_NORM_ORDER`.

The unknown is now the order of one explicit diagonal point in a finite product of exact local universal-norm quotients.

## Claim firewall

WP25 does not prove:

- a numerical or uniform closed formula for any `rho_v(P)` or for `rho_E`;
- that `P` is or is not a universal norm at any selected defect place;
- equality of `rho_E` with a regulator, height, Bockstein, Euler factor, or analytic term;
- D1a, D1c, or D2;
- `delta_2(E)=len_Z2 Sha(E/Q)[2^infinity]`;
- `BSD-R2-A1`;
- any MATHCERT certification, novelty, priority, patentability, or commercial claim.
