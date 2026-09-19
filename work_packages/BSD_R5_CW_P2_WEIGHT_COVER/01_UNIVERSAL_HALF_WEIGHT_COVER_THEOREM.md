# Universal literal-p=2 half-weight cover theorem

## Theorem identifier

`BSD-R5-CW-P2-HALF-WEIGHT-005`.

## 1. The principal 2-adic weight group

Put

`Gamma := 1+4 Z_2`.

Every unit `u in Z_2^*` is congruent to either `1` or `-1` modulo four.
Hence, uniquely,

`u = epsilon g`, with `epsilon in {+1,-1}` and `g in Gamma`.

Thus

`Z_2^* = {+1,-1} x Gamma`.

The element `5` is a topological generator of `Gamma`.  Indeed, for every
`n>=0`, the lifting-the-exponent identity gives

`v_2(5^(2^n)-1)=n+2`.

Therefore the image of `5` has exact order `2^n` in

`Gamma/(1+2^(n+2) Z_2)`,

whose order is also `2^n`.  Passing to the inverse limit gives a topological
isomorphism

`Z_2 -> Gamma,  a |-> 5^a`.

## 2. Squaring

The square of `5^a` is `25^a`.  The same valuation calculation, now with
`25`, shows that `25` topologically generates `1+8 Z_2`.  Hence

`sq: Gamma -> 1+8 Z_2,  g |-> g^2`

is a topological group isomorphism.

It is not an automorphism of `Gamma`: its image is the proper subgroup
`1+8 Z_2`.  For example `5 in Gamma` is not congruent to `1` modulo
eight and therefore is not a square in `Gamma`.

This is the exact literal-`2` failure of the odd-prime operation of dividing
the universal principal-unit character by two inside the same weight group.

## 3. Weight algebra and square-root cover

Let

`Lambda := Z_2[[Gamma]]`.

Using the topological generator `gamma=5`, identify

`Lambda ~= Z_2[[T]]`

by sending the universal group-like element `[gamma]` to

`U:=1+T`.

Define

`Lambda_half := Lambda[Y]/(Y^2-U)`.

Because the defining polynomial is monic of degree two,

`Lambda_half = Lambda direct_sum Lambda Y`

as a `Lambda`-module.  In particular `Lambda_half` is finite free of rank
two, hence finite flat.

Set `S:=Y-1`.  The relation `Y^2=1+T` becomes

`T=2S+S^2`.

Eliminating `T` gives an isomorphism of complete local `Z_2`-algebras

`Lambda_half ~= Z_2[[S]]`,

under which the structure map is

`Z_2[[T]] -> Z_2[[S]],   T |-> 2S+S^2`.

Consequently `Lambda_half` is complete Noetherian local, with maximal ideal

`n=(2,S)=(2,T,Y-1)`.

Modulo two the structure map is

`F_2[[T]] -> F_2[[S]],   T |-> S^2`.

It is therefore not etale at the closed residual point.  Equivalently, the
discriminant of `Y^2-U` is `4U`, which is not a unit.

## 4. The universal half-character

Since `Y=1+S in 1+n`, for every `a in Z_2` the binomial series

`Y^a := sum_{k>=0} binom(a,k) S^k`

converges `n`-adically in `Lambda_half`.

Using the topological parameterization `Gamma={5^a:a in Z_2}`, define

`kappa_half(5^a):=Y^a`.

The binomial identities, first for integral exponents and then by continuity,
show that `kappa_half` is a continuous character

`Gamma -> Lambda_half^*`.

Let `kappa:Gamma -> Lambda^*` be the universal weight character.  After base
change to `Lambda_half`,

`kappa(5^a)=U^a=(Y^2)^a=(Y^a)^2`.

Therefore

`kappa_half^2 = kappa`.

## 5. Universal property

Let `A` be a complete local `Lambda`-algebra with structure map
`phi:Lambda->A`.  Continuous local `Lambda`-algebra homomorphisms

`Lambda_half -> A`

are in natural bijection with elements `y in 1+m_A` satisfying

`y^2=phi(U)`.

The map sends a homomorphism to the image of `Y`.  Conversely, such a `y`
determines a unique `Lambda`-algebra homomorphism by the quotient universal
property.  Since `y` is congruent to one, the map is local and continuous.

For each such `y`, the formula

`5^a |-> y^a`

defines the corresponding continuous half-character, and its square is the
base-changed universal character.

Thus `Lambda_half` represents the functor of local square roots of the
universal principal weight character.

## 6. Exact consequence for the Colmez–Wang route

The algebraic obstruction

`MISSING_P2_COLMEZ_WANG_UNIVERSAL_HALF_WEIGHT_CHARACTER`

is closed: a canonical universal square-root cover exists and retains integral
finite-flat control.

What remains is not the existence of the half-character.  It is whether the
specific Colmez–Wang Chapter-15 constructions used to globalize the family Kato
class replay after this ramified finite-flat base change, including the
deformation/Hecke module, Poitou–Tate, density, specialization and integrality
steps.

The exact successor boundary is

`MISSING_P2_COLMEZ_WANG_SQUARE_ROOT_COVER_CHAPTER15_GLOBALIZATION_COMPATIBILITY`.

The independent later boundary

`MISSING_P2_COLMEZ_WANG_DENOMINATOR_REMOVAL_WITH_NONPROCYCLIC_UNITS`

is unchanged.

## 7. Claim firewall

No statement here proves a literal-`2` Colmez–Wang Kato comparison, a nonzero
residual modular-symbol component, `c_Q^Kato mod 2 != 0`, R5-RES, R5-PRIM,
D2d, BSD-R2-A1, or MATHCERT certification.
