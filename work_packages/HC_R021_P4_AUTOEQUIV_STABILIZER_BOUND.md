# HC-R021-P4 — Full autoequivalence-stabilizer bound for the coherent second factor

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent protected revision:** `20358ac7630b4c9a6033e352a3a9a425f82bd3fb`  
**State:** `SECOND_FACTOR_WEAK_EQUIVARIANT_ROUTE_PRUNED_FOR_qN_GE_4`  
**Date:** 2026-09-16

## 1. Purpose

Strengthen `HC-R021-L011`, which treated only a transitive pure-translation symmetry of the Example 11.2.7 gluing.

Perry's theorem permits a finite subgroup of the full identity-component autoequivalence group

```text
X x X-hat,
```

acting by translation followed by tensoring with a degree-zero line bundle. A priori this leaves open the possibility that adding twists produces a much larger useful symmetry than the translation group.

For the actual coherent second-factor gluing this does not happen. The support geometry forces the projection of every finite autoequivalence stabilizer to the translation factor to be faithful and of order at most `N`.

Consequently the invariant `Ext^2` lower bound of `L011` survives for **every** finite translation-plus-twist symmetry preserving the coherent gluing. For `qN>=4`, even weak equivariant semiregularity of the second-factor object is dimensionally impossible.

This is a factorwise no-go only. It does not rule out a genuinely eight-dimensional symmetry of the final external-product/Orlov object.

## 2. Setup

Let `E` be a simple coherent Example 11.2.7 gluing on the abelian fourfold `X`, with

```text
ch(E)=N[D-(q/6)H^3],
q,N>0.
```

Its top-dimensional support is the union of the `N` translated principal-divisor supports of the secant constituents:

```text
Supp_3(E)=Z_1 union ... union Z_N.
```

The additional curve used in the gluing has smaller dimension and does not change this set of irreducible top-dimensional support components.

Let

```text
G subset X x X-hat
```

be a finite subgroup acting by

```text
(x,P): F |-> tau_x^* F tensor P
```

and assume `E` admits a `G`-equivariant structure.

Write

```text
p_X : G -> X
```

for projection to the translation factor.

## 3. Translation stabilizers of the divisor components are trivial

Each `Z_j` has principal polarization class `D`. If translation by `x` preserves `Z_j`, then

```text
tau_x^* O_X(Z_j) ~= O_X(Z_j).
```

Thus `x` lies in the kernel of the polarization homomorphism associated with `O_X(Z_j)`. Because the class is principal, that kernel is trivial.

Hence

```text
Stab_X(Z_j) = {0}
```

for every top-dimensional support component.

This is the support calculation already used in `HC-R021-L011`.

## 4. Pure twists cannot stabilize E

### HC-R021-L017a

If

```text
E tensor P ~= E
```

for `P in Pic^0(X)`, then `P=O_X`.

### Proof

A pure twist does not permute the support components. Restrict the isomorphism to the generic rank-one locus on any component `Z_j`. The Example 11.2.7 constituent is rank-one torsion-free on its integral principal divisor support, and `E` agrees with that constituent away from the lower-dimensional gluing locus. Passing to the rank-one reflexive hull on `Z_j` therefore gives

```text
P|Z_j ~= O_Zj.
```

It remains to show that restriction

```text
Pic^0(X) -> Pic^0(Z_j)
```

is injective.

Let `P` be nontrivial in `Pic^0(X)` and suppose `P|Z_j` were trivial. Tensoring

```text
0 -> O_X(-Z_j) -> O_X -> O_Zj -> 0
```

by `P` gives

```text
0 -> P(-Z_j) -> P -> O_Zj -> 0.
```

For nontrivial `P in Pic^0(X)`, `H^0(X,P)=0`. On the other hand, by Serre duality and Kodaira vanishing on the abelian fourfold,

```text
H^1(X,P(-Z_j))
  ~= H^3(X,P^{-1}(Z_j))^* = 0,
```

because `P^{-1}(Z_j)` is ample. The resulting cohomology sequence would force

```text
H^0(Z_j,O_Zj)=0,
```

contradicting connectedness of the ample divisor.

Therefore `P` must be trivial.

QED.

## 5. HC-R021-L017 — the full finite stabilizer has order at most N

### Statement

For every finite subgroup `G subset X x X-hat` preserving `E`, the translation projection

```text
p_X : G -> X
```

is injective and

```text
|G| <= N.
```

### Proof

The kernel of `p_X` consists of pure twists preserving `E`; it is trivial by `L017a`. Hence `p_X` is injective.

The translation subgroup `p_X(G)` acts on the `N` top-dimensional components `Z_j`. If a nonzero element fixed one component, it would lie in its translation stabilizer, which is trivial by Section 3. Thus the action on every component orbit is free.

Every orbit therefore has cardinality `|G|`. Since there are only `N` components,

```text
|G| <= N.
```

QED.

## 6. Invariant Euler characteristic

Because `p_X` is faithful, every nonidentity element of `G` has a nonzero translation component. The equivariant Lefschetz trace of such an element on

```text
RHom_X(E,E)
```

vanishes: the graph of a nontrivial translation has empty intersection with the diagonal. Tensoring by a degree-zero line bundle does not create fixed points.

Therefore averaging characters gives

```text
chi(Ext^*(E,E)^G) = chi(E,E)/|G|.
```

Since `E` is simple and `X` is an abelian fourfold, equivariant Serre duality yields

```text
ext_G^0 = ext_G^4 = 1,
ext_G^3 = ext_G^1.
```

Hence

```text
ext_G^2
 = chi(E,E)/|G| + 2 ext_G^1 - 2
 >= chi(E,E)/|G| - 2.
```

`HC-R021-L004` gives

```text
chi(E,E) = (N^2 q/3) I,
I = integral_X D H^3 >= 24.
```

Combining with `|G|<=N` gives

```text
dim Ext^2(E,E)^G
 >= 8 q N - 2.
```

Thus the lower bound from the pure-translation calculation is in fact valid for every finite identity-component autoequivalence symmetry preserving this coherent second-factor gluing.

## 7. Weak equivariant semiregularity is impossible for qN >= 4

Perry's geometrization of a finite subgroup of the identity-component autoequivalence group identifies the relevant connected component of the invariant category with a twisted derived category of a connected finite étale cover of the quotient by the translation image.

In the present case that cover is again an abelian fourfold. A Brauer twist is Morita-invisible to Hochschild homology. Hence

```text
dim HH_-2(Dperf(X)^G) = 28,
```

the ordinary abelian-fourfold value

```text
6 + 16 + 6.
```

If

```text
qN >= 4,
```

then Section 6 gives

```text
dim Ext^2(E,E)^G >= 30.
```

For any equivariant lift `E_tilde` in the invariant category,

```text
Ext^2(E_tilde,E_tilde) ~= Ext^2(E,E)^G.
```

Therefore its semiregularity map cannot be injective into a 28-dimensional `HH_-2` target. Thus `E` is not weakly `G`-semiregular for any such finite `G`.

In particular, the explicit source tranche of `HC-R021-L012` has `N=6`, so `qN>=6` and is included in this no-go theorem.

## 8. Consequence for Route G

This eliminates the strategy

```text
make the coherent second factor weakly G-semiregular
        |
        +--> use it as a factorwise input to the final external product.
```

for every Example 11.2.7 gluing with `qN>=4`.

A viable Route G must instead exploit genuinely eight-dimensional structure of the **total** external-product/Orlov object, where the invariant obstruction theory is not the second-factor obstruction theory alone.

The mixed

```text
Ext^1(F_1,F_1) tensor Ext^1(F_2,F_2)
```

summand therefore cannot be bypassed by proving weak equivariant semiregularity of the two factors independently.

## 9. Scope and firewalls

This result does not prove that the final eightfold object fails weak equivariant semiregularity.

It does not rule out:

- a symmetry whose useful effect appears only after taking the external product;
- a non-coherent/non-formal same-ray perfect complex not having the Example 11.2.7 support geometry;
- the direct `D20` route;
- an all-orders deformation argument not based on Perry equivariant semiregularity.

It does rule out enlarging the useful symmetry of the coherent second factor by adding degree-zero twists: the support geometry keeps the group order at most `N`.

## 10. Current disposition

```text
HC-R021-L017 = proved_in_solve_package_not_certified
full_finite_autoequiv_stabilizer_order <= N
second_factor_invariant_Ext2 >= 8qN-2
second_factor_weak_G_semiregularity_impossible_if_qN_ge_4
explicit_N6_second_factor_weak_G_route = pruned
final_eightfold_G3 = open
D20_nonempty = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 11. Sources

- Eyal Markman, arXiv:2509.23079, Example 11.2.7.
- Alexander Perry, arXiv:2604.00511v2, Definition 2.6, Lemma 2.7, Section 5, and Theorem 1.2 / Theorem 6.3.
- `work_packages/HC_R021_P4_SEMIREGULARITY_DIAGNOSTICS.md` (`HC-R021-L004`).
- `work_packages/HC_R021_P4_EQUIVARIANT_DIMENSION_OBSTRUCTION.md` (`HC-R021-L011`).
- Standard equivariant Lefschetz trace formula, Serre duality, and Kodaira vanishing on abelian varieties.
