# Theorem spine

## Theorem 1 — no quadratic 2-power torsion growth

Let `E/Q` have irreducible `E[2]`. For every quadratic extension `K/Q`,

`E(K)[2^infinity] = 0`.

In particular `E(K)[2^n]=0` for every `n >= 1`.

**Status:** `PROVED_IN_PACKAGE`.

## Theorem 2 — exact global eigenspace descent at every 2-power level

For every `n >= 1`, restriction induces isomorphisms

`H^1(Q,E[2^n])  ~=  H^1(K,E[2^n])^+`

and, after the standard `K`-identification of the twist,

`H^1(Q,E^d[2^n]) ~= H^1(K,E[2^n])^-`.

**Status:** `PROVED_IN_PACKAGE`.

## Theorem 3 — exact finite-level Selmer control

For every `n >= 1`, restriction induces short exact sequences

`0 -> Sel_{2^n}(E/Q) -> M_n^+ -> D_n^+ -> 0`,

`0 -> Sel_{2^n}(E^d/Q) -> M_n^- -> D_n^- -> 0`.

The localization maps give canonical injections

`D_n^+ -> direct_sum_v Delta_{v,n}^+`,

`D_n^- -> direct_sum_v Delta_{v,n}^-`.

If `v` splits in `K`, then `Delta_{v,n}^+ = Delta_{v,n}^- = 0`.

If `v` is nonsplit and `w|v`, then

`Delta_{v,n}^+ ~= H^1(Gal(K_w/Q_v),E(K_w))`

and

`Delta_{v,n}^- ~= H^1(Gal(K_w/Q_v),E^d(K_w))`,

where in the second line `E^d(K_w)` is viewed through the twisted descent action. For every `n >= 1`, these displayed isomorphisms identify the local defects with the same cohomology groups. Those groups are killed by `2`; hence each local defect is an `F_2`-vector space whose `Z_2`-length is independent of `n`.

Consequently `D_n^+` and `D_n^-` are finite `F_2`-vector spaces.

**Status:** `PROVED_IN_PACKAGE`.

## Theorem 4 — integral plus/minus replacement

For any finite `Z/2^nZ`-module `M` with involution `tau`, define

`M^+ = ker(tau-1)`, `M^- = ker(tau+1)`,

`I = M^+ intersect M^-`, and `Q = M/(M^+ + M^-)`.

Then

`0 -> I -> M^+ direct_sum M^- -> M -> Q -> 0`

is exact, where the first map is `x |-> (x,-x)` and the middle map is addition. Moreover `2I=0` and `2Q=0`.

Applied to `M=M_n`, this defines `I_n` and `Q_n` without division by `2`.

**Status:** `PROVED_IN_PACKAGE`.

## Corollary 5 — exact finite-length identity

For every `n >= 1`,

`len_Z2 Sel_{2^n}(E/K)`

`= len_Z2 Sel_{2^n}(E/Q) + len_Z2 Sel_{2^n}(E^d/Q)`

`  + dim_F2 D_n^+ + dim_F2 D_n^- - dim_F2 I_n + dim_F2 Q_n.`

No omitted unit or unrecorded power of `2` occurs.

**Status:** `PROVED_IN_PACKAGE`.

## Corollary 6 — exact large-n Sha-length identity

Assume `Sha(E/Q)[2^infinity]`, `Sha(E^d/Q)[2^infinity]`, and `Sha(E/K)[2^infinity]` are finite. Then, for every sufficiently large `n`,

`len_Z2 Sha(E/K)[2^infinity]`

`= len_Z2 Sha(E/Q)[2^infinity] + len_Z2 Sha(E^d/Q)[2^infinity]`

`  + dim_F2 D_n^+ + dim_F2 D_n^- - dim_F2 I_n + dim_F2 Q_n.`

The rank terms cancel because

`rank E(K) = rank E(Q) + rank E^d(Q)`.

**Status:** `PROVED_IN_PACKAGE`.

## Proposition 7 — split auxiliary field removes the dangerous local places

If the auxiliary quadratic field `K` is chosen so that every prime dividing `2N` splits in `K`, then

`Delta_{v,n}^+ = Delta_{v,n}^- = 0`

for `v=2` and every `v|N`, at every `n`. Thus neither the ordinary local condition at `2` nor any bad-prime condition contributes a descent correction at these places.

This is exact split-local transport; it is not a claim that a 2-power correction is a unit.

**Status:** `PROVED_IN_PACKAGE`.

## Remaining bridge

The descent theorem supplies no analytic-to-arithmetic equality. To reach `BSD-R2-A1`, one still needs an integral 2-primary Iwasawa/Euler-system length and an explicit reciprocity/Gross-Zagier/height comparison with all local normalizations.
