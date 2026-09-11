# WP25 theorem — exact local universal-norm representation of `rho_E`

## 1. Setup

Let `E/Q` lie in the protected selected `BSD-R2-A1` class. Let

`Q_infty/Q`

be the cyclotomic `Z_2`-extension. For each finite place `v`, choose a place `w|v` of `Q_infty` and write

`F_v := Q_v`,

`F_{v,infty} := Q_{infty,w}`,

`Gamma_v := Gal(F_{v,infty}/F_v)`.

When `Gamma_v` is nontrivial, protected WP21-WP23 identify the ambient primitive local-control group as

`K_v := H^1(Gamma_v,E(F_{v,infty}))[2^infinity]`.

Protected WP22 proves that for odd `v=ell`, the local extension is either trivial for no selected finite prime or, after the decomposition-group identification, an unramified `Z_2`-extension; protected WP23 treats `v=2`.

Protected WP24 fixes a saturated generator

`P in E(Q)`

of the rank-one free quotient and defines the global local-Tate character

`chi_P|K_loc : K_loc -> Q_2/Z_2`,

with

`rho_E := len_Z2 im(chi_P|K_loc)`.

Protected MATHFORGE commit

`b09faf74936611616465186c8702ea0ce6f36828`

admits Ki-Seng Tan's exact local Galois-cohomology/norm-duality interface. For an arbitrary local Galois extension `L/K` and a dual pair of abelian varieties, the source gives a Pontryagin duality between

`H^1(Gal(L/K),A(L))`

and the source-defined compact projective limit of finite norm quotients. For an elliptic curve, the principal polarization identifies the dual abelian variety with `E` itself.

No other external theorem premise is used in WP25.

## 2. Finite local layers and norm images

For each nontrivial `Gamma_v ~= Z_2`, choose the standard cofinal tower of finite layers

`F_{v,n}/F_v`, `n>=0`,

with

`Gal(F_{v,n}/F_v) ~= Z/2^n Z`.

Define

`N_{v,n} := N_{F_{v,n}/F_v} E(F_{v,n}) subset E(F_v)`.

Norm transitivity gives

`N_{v,n+1} subset N_{v,n}`.

Set

`Q_{v,n} := E(F_v)/N_{v,n}`.

The inclusion of norm images gives a natural surjection

`Q_{v,n+1} -> Q_{v,n}`.

Tan's protected infinite-extension theorem gives canonically

`H^1(Gamma_v,E(F_{v,infty}))^vee
 ~= inverse_limit_n Q_{v,n}`.

### Lemma `BSD-A1-WP25-PRO2-001`

The group

`H^1(Gamma_v,E(F_{v,infty}))`

is `2`-primary torsion. Hence it equals the protected group `K_v`.

### Proof

Tan's infinite-extension cohomology is the direct limit of

`H^1(Gal(F_{v,n}/F_v),E(F_{v,n}))`.

For a finite group, positive-degree cohomology is annihilated by the group order. Here the group order is `2^n`. Therefore every element at every finite stage is killed by a power of `2`, and every element of the direct limit is `2`-primary torsion.

Protected WP21 defines `K_v` as the `2`-primary torsion of this same continuous local cohomology group. Thus the groups are equal. QED.

### Corollary `BSD-A1-WP25-PRO-NORM-DUAL-001`

There is a canonical Pontryagin-dual isomorphism

`K_v^vee ~= inverse_limit_n Q_{v,n}`.

## 3. Stabilization of the local norm quotients

Protected WP22-WP23 prove every nonzero `K_v` finite. Hence its Pontryagin dual is finite.

### Lemma `BSD-A1-WP25-NORM-STABILIZATION-001`

For every finite place `v`, the nested norm images `N_{v,n}` eventually stabilize. If

`N_v^infty := intersection_n N_{v,n}`,

then for all sufficiently large `n`,

`N_{v,n}=N_v^infty`,

and canonically

`K_v^vee ~= E(F_v)/N_v^infty`.

### Proof

If `K_v=0`, Corollary `BSD-A1-WP25-PRO-NORM-DUAL-001` says the inverse limit of the `Q_{v,n}` is zero. The transition maps are surjective. For an inverse system of nonempty finite groups with surjective transition maps, every projection from the inverse limit to a finite stage is surjective: starting from any chosen element at stage `n`, recursively choose lifts at all higher stages. Hence every `Q_{v,n}` is zero. Thus `N_{v,n}=E(F_v)` for every `n`, and the claim holds.

Now suppose `K_v` is nonzero. The inverse limit

`Q_v^pro := inverse_limit_n Q_{v,n}`

is finite because it is Pontryagin-dual to finite `K_v`. As above, every projection

`Q_v^pro -> Q_{v,n}`

is surjective. Therefore

`#Q_{v,n} <= #Q_v^pro`

for every `n`.

On the other hand, the natural transition maps

`Q_{v,n+1} -> Q_{v,n}`

are surjective, so

`#Q_{v,n+1} >= #Q_{v,n}`.

Thus the nondecreasing sequence of positive integers `#Q_{v,n}` is bounded and eventually constant. For sufficiently large `n`, the surjection

`Q_{v,n+1} -> Q_{v,n}`

is an isomorphism.

But this map is the quotient map induced by the inclusion

`N_{v,n+1} subset N_{v,n}`.

Its kernel is

`N_{v,n}/N_{v,n+1}`.

Therefore eventual isomorphism forces

`N_{v,n+1}=N_{v,n}`.

Hence the norm images stabilize to their intersection `N_v^infty`. The inverse system is then eventually constant, so

`Q_v^pro ~= E(F_v)/N_v^infty`.

Combining with Corollary `BSD-A1-WP25-PRO-NORM-DUAL-001` gives the claimed canonical duality. QED.

## 4. Exact local universal-norm quotient

Define

`U_v := E(F_v)/N_v^infty`.

### Theorem `BSD-A1-WP25-LOCAL-DUAL-001`

For every finite place `v`,

`U_v ~= K_v^vee`

canonically under the protected local Tate pairing.

In particular, `U_v` is a finite `2`-primary group. Moreover:

1. at `v=2`,

   `#U_2=(3-a_2)^2`,

   so

   `len_Z2 U_2 = 2 ord_2(3-a_2)`;

2. at every odd bad semistable prime `ell|N`,

   `#U_ell=2^{ord_2(c_ell)}`,

   so

   `len_Z2 U_ell=ord_2(c_ell)`;

3. at every odd good prime, `U_ell=0`;

4. the real place contributes no local control group.

### Proof

The canonical duality is Lemma `BSD-A1-WP25-NORM-STABILIZATION-001`. The size statements follow by Pontryagin duality from protected WP22-WP23, which compute the corresponding `K_v` exactly. QED.

## 5. The saturated generator as a norm-obstruction class

For every finite place `v`, let

`P_v in E(F_v)`

be the image of the fixed saturated global generator `P`. Define

`[P]_v := P_v mod N_v^infty in U_v`.

At a place with `U_v=0`, this class is zero.

Let

`S_def := {v finite : U_v != 0}`.

Protected WP22-WP23 show

`S_def subset {2} union {ell:ell|N}`.

Define the finite product

`U_loc := product_{v in S_def} U_v`.

By Theorem `BSD-A1-WP25-LOCAL-DUAL-001` and finite-product duality,

`U_loc ~= K_loc^vee`.

Set

`u(P) := ([P]_v)_{v in S_def} in U_loc`.

## 6. Compatibility with the WP24 character

### Theorem `BSD-A1-WP25-CHARACTER-DUAL-001`

Under the canonical Pontryagin-dual identification

`K_loc^vee ~= U_loc`,

the WP24 character

`chi_P|K_loc`

corresponds exactly to

`u(P)`.

### Proof

Protected WP24 defines the local component of `chi_P` by pairing an element of the primitive local quotient with the localized compact Kummer class of `P`.

The protected MATHFORGE Tan audit admits the exact compatibility between this local Tate pairing and norm duality: under the identification

`K_v^vee ~= inverse_limit_n E(F_v)/N_{v,n}`,

evaluation against the localized compact Kummer class of `P` is evaluation against the compatible norm-quotient class of `P_v`.

Lemma `BSD-A1-WP25-NORM-STABILIZATION-001` identifies that compatible projective-limit class with the ordinary stabilized universal-norm class

`[P]_v in U_v`.

The global WP24 character on `K_loc` is the sum of the finitely many local Tate pairings. Pontryagin duality for a finite direct product identifies this sum-character with the tuple of the local dual elements. Therefore it corresponds exactly to

`([P]_v)_{v in S_def}=u(P)`. QED.

## 7. Exact order formula for `rho_E`

For each finite place define

`rho_v(P) := ord_2(ord([P]_v))`,

where the identity element has order `1` and hence contributes `0`.

### Lemma `BSD-A1-WP25-CHARACTER-ORDER-001`

Let `G` be a finite abelian group and `chi in G^vee`. Then

`#im(chi)=ord(chi)`

as an element of the character group.

### Proof

The image of `chi:G->Q/Z` is a finite cyclic group. The order of the homomorphism `chi` in `Hom(G,Q/Z)` is the least positive integer `m` such that `m chi=0`, equivalently the exponent of its cyclic image. For a finite cyclic group, exponent equals cardinality. QED.

### Theorem `BSD-A1-WP25-RHO-001`

One has exactly

`2^{rho_E}=ord(u(P))`.

Equivalently,

`rho_E = max_{v in S_def} rho_v(P)`.

### Proof

By definition,

`rho_E=len_Z2 im(chi_P|K_loc)=ord_2 #im(chi_P|K_loc)`.

Theorem `BSD-A1-WP25-CHARACTER-DUAL-001` identifies the character with the element `u(P)` of the Pontryagin dual. Lemma `BSD-A1-WP25-CHARACTER-ORDER-001` therefore gives

`#im(chi_P|K_loc)=ord(u(P))`.

Every `U_v` is a finite `2`-group. The order of an element of a finite direct product is the least common multiple of the orders of its components. Since every component order is a power of `2`, their least common multiple is the largest one. Hence

`ord_2 ord(u(P)) = max_v ord_2 ord([P]_v)`.

This is the asserted formula. QED.

## 8. Exact local bounds

### Corollary `BSD-A1-WP25-BOUNDS-001`

The local obstruction lengths satisfy

`0 <= rho_2(P) <= 2 ord_2(3-a_2)`

and for every odd bad semistable prime `ell|N`,

`0 <= rho_ell(P) <= ord_2(c_ell)`.

At every odd good prime and at the real place the contribution is zero.

Consequently

`0 <= rho_E <= max(2 ord_2(3-a_2), max_{ell|N} ord_2(c_ell))`.

### Proof

The order of an element divides the order of its finite ambient group. Apply Theorem `BSD-A1-WP25-LOCAL-DUAL-001` to the local classes `[P]_v`, then use Theorem `BSD-A1-WP25-RHO-001`. QED.

The upper bound is deliberately a maximum rather than the total ambient length. A single character into `Q_2/Z_2` has cyclic image, so its order is governed by the largest local component order, not by the product of all local group orders.

## 9. Updated exact control length

Combining protected WP24 with Theorem `BSD-A1-WP25-RHO-001` gives

`len_Z2(C_E^vee)
 = 2 ord_2(3-a_2)
   + sum_{ell|N} ord_2(c_ell)
   - max_{v in S_def} rho_v(P)`.

This formula is exact. It does not evaluate any `rho_v(P)`.

## 10. Refined frontier

The former scalar boundary

`MISSING_P2_GLOBAL_HIT_CHARACTER_IMAGE_LENGTH`

is now represented as the exact local universal-norm problem

`MISSING_P2_SATURATED_GENERATOR_LOCAL_UNIVERSAL_NORM_ORDER`.

The remaining D1b information is no longer an abstract global incidence subgroup or an abstract character image. It is the order of the explicit tuple

`u(P)=([P]_v)_v`

of local universal-norm classes of the saturated rank-one Mordell-Weil generator.

A successor may attack these local classes directly. At odd multiplicative primes, the protected WP22 component-group computation suggests a finite Neron-component description; at `2`, protected WP23 shows the ambient quotient has order `(3-a_2)^2`. Those structural suggestions are not promoted here to formulas for `[P]_v`.

Any theorem identifying a local class with a component-group coordinate, formal logarithm, norm index, height, Bockstein value, or regulator must be proved or separately source-admitted before use.

## 11. Relation to WP20

WP20's intrinsic Bockstein ideal `B_E` is a first-order determinant invariant. WP25's `u(P)` is an exact local universal-norm obstruction tuple.

Both are rank-one integral objects, but WP25 proves no equality between them. In particular, no cancellation with the WP20 Bockstein or with the WP00 regulator is authorized by the present theorem.

## 12. Claim firewall

WP25 does not prove:

- a value of any `rho_v(P)` or of `rho_E`;
- that the saturated generator is a universal norm at any nonzero-defect place;
- a Neron-component formula for `[P]_ell`;
- a formal-group/logarithmic formula for `[P]_2`;
- equality of `rho_E` with a regulator, height, Bockstein, Euler factor, or analytic quantity;
- D1a `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
- D1c `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2 `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`;
- `delta_2(E)=len_Z2 Sha(E/Q)[2^infinity]`;
- `BSD-R2-A1`;
- any MATHCERT certification, novelty, priority, patentability, or commercial claim.
