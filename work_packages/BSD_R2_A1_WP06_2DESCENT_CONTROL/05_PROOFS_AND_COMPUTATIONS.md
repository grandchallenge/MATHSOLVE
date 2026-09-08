# Proofs and exact deductions

## Proof of Theorem 1

Let `V=E[2]`. The image `H` of `G_Q` in `GL_2(F_2)` acts irreducibly on `V`. Since `GL_2(F_2)` is isomorphic to `S_3`, an irreducible subgroup is either a subgroup of order `3` or all of `S_3`: a subgroup of order `1` or `2` fixes a nonzero vector and is reducible.

Let `K/Q` be quadratic. Because `G_K` is normal of index `2` in `G_Q`, its image `H_K` is a normal subgroup of `H` of index dividing `2`.

- If `H` has order `3`, then `H_K=H`.
- If `H=S_3`, then `H_K` is either `S_3` or `A_3`.

Both an order-3 subgroup and `S_3` act on the three nonzero vectors of `V` without a common fixed vector. Hence

`V^{G_K}=0`,

so `E(K)[2]=0`.

If `P` had order `2^m` for some `m>1`, then `2^{m-1}P` would be a nonzero point of order `2` in `E(K)`, contradiction. Therefore `E(K)[2^infinity]=0`.

## Proof of Theorem 2

Apply inflation-restriction to `A_n=E[2^n]` for the exact sequence

`1 -> G_K -> G_Q -> G -> 1`.

It gives

`0 -> H^1(G,A_n^{G_K}) -> H^1(Q,A_n) -> H^1(K,A_n)^G -> H^2(G,A_n^{G_K}).`

Theorem 1 gives `A_n^{G_K}=E(K)[2^n]=0`, so both outside terms vanish. Therefore restriction is an isomorphism onto the plus eigenspace.

For the quadratic twist, `E^d[2^n]` is `A_n` with the `G_Q` action multiplied by `chi`. After restriction to `G_K`, the coefficients are identified with `A_n`. A lift of the nontrivial element `tau` acts with the extra factor `chi(tau)=-1`. Thus invariants for the twisted action correspond exactly to classes satisfying `tau x=-x` for the ordinary action. Inflation-restriction gives the minus isomorphism.

## Proof of Theorem 3: local defect

For a nonsplit local extension `L/F = K_w/Q_v`, the Kummer sequence gives a commutative diagram whose rows end in

`0 -> E(F)/2^nE(F) -> H^1(F,E[2^n]) -> H^1(F,E)[2^n] -> 0`

and the analogous sequence over `L`.

By definition, a class belongs to the relaxed local condition precisely when its image in `H^1(F,E)[2^n]` becomes zero after restriction to `L`. Hence

`Delta_{v,n}^+ ~= ker(H^1(F,E)[2^n] -> H^1(L,E)[2^n]).`

Inflation-restriction for the `G=Gal(L/F)` action on `E(L)` identifies the kernel of

`H^1(F,E) -> H^1(L,E)`

with `H^1(G,E(L))`. Cohomology in positive degree for a finite group of order `2` is killed by `2`, so its `2^n`-torsion is the whole group for every `n>=1`. Therefore

`Delta_{v,n}^+ ~= H^1(G,E(L))`.

The same argument with the twisted action proves the minus statement.

At a split place the local algebra is `F x F`, `G` exchanges the two factors, and restriction transports the Kummer condition exactly. Hence the local defect is zero.

## Proof of Theorem 3: global exactness

Theorem 2 identifies global cohomology over `Q` with the appropriate eigenspace over `K`. Under this identification, membership in `M_n^+` is exactly membership in every relaxed plus local condition. Thus

`M_n^+ ~= Sel_{F_n^+}(Q,E[2^n])`.

The ordinary Selmer structure is contained in the relaxed structure. Localization modulo the ordinary local conditions has kernel exactly `Sel_{2^n}(E/Q)`. Therefore the quotient `D_n^+` injects into the direct sum of the local quotients `Delta_{v,n}^+`. The minus case is identical for the twist.

Since every local quotient is killed by `2`, so are `D_n^+` and `D_n^-`.

## Proof of Theorem 4

The kernel of addition

`M^+ direct_sum M^- -> M`

consists of pairs `(x,y)` with `y=-x`. Such a pair lies in the domain exactly when `x` belongs to both `M^+` and `M^-`. This gives the kernel `I` via `x |-> (x,-x)`. The cokernel is, by definition, `Q=M/(M^++M^-)`.

If `x in I`, then `tau x=x` and `tau x=-x`, hence `2x=0`.

For any `m in M`,

`2m = (1+tau)m + (1-tau)m`.

The first summand lies in `M^+` and the second in `M^-`. Therefore `2Q=0`.

This proves the exact sequence and the exponent-2 bounds without constructing an integral projector.

## Proof of Corollary 5

Take `Z_2`-lengths in the two short exact sequences of Theorem 3 and in the exact sequence of Theorem 4. Because `D_n^+`, `D_n^-`, `I_n`, and `Q_n` are killed by `2`, their `Z_2`-lengths equal their `F_2`-dimensions. Substitution gives the stated identity.

## Proof of Corollary 6

For a number field `F`, the Kummer sequence gives

`0 -> E(F)/2^nE(F) -> Sel_{2^n}(E/F) -> Sha(E/F)[2^n] -> 0`.

Theorem 1 removes 2-primary torsion over `K`; irreducibility also removes it over `Q`, and `E^d[2]` is the same mod-2 representation, so it is removed for the twist as well.

If the relevant `Sha[2^infinity]` is finite, then for all sufficiently large `n`,

`len Sel_{2^n}(E/F) = n rank E(F) + len Sha(E/F)[2^infinity].`

Over `Q`, rational eigenspace decomposition is legitimate after tensoring Mordell-Weil groups with `Q`, so

`rank E(K)=rank E(Q)+rank E^d(Q)`.

Insert these three formulas into Corollary 5. The coefficients of `n` cancel, leaving the exact Sha-length identity.

## Proof of Proposition 7

If `v` splits in `K`, the completed algebra is a product of two copies of `Q_v`. Restriction is the diagonal transport for the plus branch and the signed diagonal transport for the twist branch. In either case the Kummer condition over the product is satisfied exactly when the original local Kummer condition is satisfied. Hence both relaxed quotients are zero.

The same argument applies to the ordinary 2-divisible-group local condition at `v=2`: when `2` splits, there is no nontrivial local field extension and therefore no local descent discrepancy to compute.

## External concordance

Kramer's local norm-index calculations and Morgan-Paterson's mod-2 exact sequence agree with the `n=1` shadow of the theorem above. They are not needed to justify the all-`n` proof.