# HC-R021-P4 — Weak equivariant semiregularity cannot bypass the second-factor D20 condition

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent protected revision:** `20358ac7630b4c9a6033e352a3a9a425f82bd3fb`  
**State:** `ROUTE_G_REBASED_DOWNSTREAM_OF_SECOND_FACTOR_RANK20`  
**Date:** 2026-09-16

## 1. Purpose

Determine whether Perry's weak equivariant semiregularity can provide a genuinely independent bypass around the unresolved second-factor rank-20 condition.

It cannot.

For finite groups inside the identity component of the autoequivalence group of an abelian variety, the invariant category has the same rational Hodge/Hochschild size as the original abelian variety, and the forgetful map is an isomorphism on the relevant Hochschild target. Hence weak `G`-semiregularity is equivalent to `G`-semiregularity in this setting.

Applied to Markman's external-product object, every second-factor contraction-kernel direction produces a `G`-invariant degree-two obstruction of the total object. If any of the eight second-factor Yoneda classes is nonzero, its total obstruction has zero ordinary semiregularity trace and contradicts weak `G`-semiregularity.

Thus the second factor must already satisfy the eight-relation/rank-20 condition before the final object can be weakly equivariantly semiregular.

## 2. Perry's invariant category for abelian identity-component actions

Let `A` be a complex abelian variety and let

```text
G subset A x A-hat
```

be a finite subgroup acting on `Dperf(A)` by translations and degree-zero twists. Such a `G` is finite abelian.

Perry Proposition 5.19, as used in the proof of Theorem 1.2, gives an equivalence

```text
Dperf(A)^G ~= Dperf(N,gamma),
```

where `N` is an abelian variety isogenous to the quotient by the translation image of `G` and `gamma` is a Brauer class on `N`.

In particular `N` has the same complex dimension and the same Betti/Hodge numbers as `A`.

## 3. The forgetful map is a rational Hodge isomorphism

Perry Lemma 3.3 gives, for the forgetful functor

```text
Forg : Dperf(A)^G -> Dperf(A),
```

an isomorphism of rational weight-zero Hodge structures

```text
Ktop(Dperf(A)^G)^(G-hat) tensor Q
   ~= Ktop(Dperf(A))^G tensor Q.
```

The `G`-action on rational cohomology/topological K-theory of `A` is trivial:

- translations are homotopic to the identity;
- tensoring by a torsion degree-zero line bundle has rational Chern character `1`.

Hence

```text
Ktop(Dperf(A))^G tensor Q
 = Ktop(A) tensor Q.
```

On the invariant-category side, the equivalence with `Dperf(N,gamma)` and the twisted Chern-character/Hodge comparison identify

```text
Ktop(Dperf(A)^G) tensor Q
```

with the rational even cohomology of `N`. Since `N` is isogenous to `A`, this vector space has the same dimension as `Ktop(A) tensor Q`.

Therefore its `G-hat`-invariant subspace already has the full dimension of the ambient vector space. Consequently

```text
Ktop(Dperf(A)^G)^(G-hat) tensor Q
 = Ktop(Dperf(A)^G) tensor Q,
```

and `Forg` induces an isomorphism on the entire rational topological K-theory Hodge structure.

Passing to the associated graded of the noncommutative Hodge filtration yields, in particular, an isomorphism

```text
Forg_* : HH_-2(Dperf(A)^G) -> HH_-2(A).
```

Equivalently, there are no additional degree-minus-two Hodge directions in the invariant category that are invisible after forgetting equivariance.

This is consistent with Perry's coefficient calculation: for nonidentity translation components the fixed locus is empty, while for a pure nontrivial torsion twist the relevant degree-zero line-bundle cohomology vanishes.

## 4. HC-R021-L018a — weak and ordinary G-semiregularity coincide here

Let `E_tilde` be a `G`-equivariant lift of an object `E in Dperf(A)`. Since `|G|` is invertible,

```text
Ext^2(E_tilde,E_tilde) ~= Ext^2(E,E)^G.
```

Functoriality of the semiregularity morphism gives a commutative square

```text
Ext^2(E_tilde,E_tilde)  --sigma_Etilde--> HH_-2(Dperf(A)^G)
        |                                      |
        v                                      v Forg_*
Ext^2(E,E)              --sigma_E-------> HH_-2(A).
```

The left vertical map identifies the source with `Ext^2(E,E)^G`, and Section 3 proves the right vertical map is an isomorphism.

Therefore

```text
E_tilde semiregular in Dperf(A)^G
```

if and only if

```text
sigma_E is injective on Ext^2(E,E)^G.
```

Thus, for finite subgroups of `A x A-hat`, Perry's weak `G`-semiregularity and `G`-semiregularity conditions coincide.

## 5. External-product obstruction from the second factor

Return to Markman's source fourfold `X` and let

```text
F_1 := E_0,
F_2 := E-prime,
P := F_1 boxtimes F_2^vee in Dperf(X x X).
```

Assume `F_2` has Chern character a nonzero integer multiple of `beta-prime`. Let

```text
xi in ker[c_beta-prime : HT^2(X) -> H_Omega^-2(X)].
```

Via the second-factor inclusion of Hochschild cohomology, regard `xi` as a class

```text
xi_2 in HT^2(X x X).
```

Naturality and the Kunneth rule for the Hochschild action give

```text
ob_P(xi_2)
 = id_F1 boxtimes ob_F2(xi)
```

under the Kunneth summand

```text
Ext^0(F_1,F_1) tensor Ext^2(F_2,F_2)
 subset Ext^2(P,P).
```

Since `F_1` is nonzero, the Kunneth map shows

```text
ob_P(xi_2)=0  iff  ob_F2(xi)=0.
```

On the cohomological side,

```text
xi_2 contraction ch(P)
 = ch(F_1) tensor (xi contraction ch(F_2))
 = 0.
```

Hence semiregularity compatibility gives

```text
sigma_P(ob_P(xi_2))=0.
```

## 6. The obstruction is invariant under every identity-component finite symmetry

Let

```text
G subset (X x X) x (X x X)-hat
```

be any finite subgroup acting through the identity component of the autoequivalence group and suppose `P` admits a `G`-equivariant structure.

Translations and degree-zero twists act trivially on rational Hochschild cohomology. Thus `xi_2` is `G`-fixed. Equivariance/naturality of the Hochschild action then implies

```text
ob_P(xi_2) in Ext^2(P,P)^G.
```

If `P` were weakly `G`-semiregular, `L018a` would make the ordinary semiregularity map injective on this invariant Ext group. Since its value on `ob_P(xi_2)` is zero, we would obtain

```text
ob_P(xi_2)=0,
```

and therefore

```text
ob_F2(xi)=0.
```

This holds for every `xi` in the contraction kernel of `F_2`.

## 7. HC-R021-L018 — final weak equivariance forces the second-factor rank-20 condition

### Statement

Let `F_2` be an object on the source abelian fourfold with

```text
ch(F_2)=M beta-prime,
M != 0,
```

and let `P=E_0 boxtimes F_2^vee`. If `P`, or its image under Markman's Orlov equivalence, is weakly `G`-semiregular for any finite identity-component autoequivalence subgroup `G`, then

```text
ker(ob_F2)=ker(c_beta-prime).
```

Equivalently,

```text
rank(ob_F2)=20
```

and all eight `HC-R021-L007` kernel relations vanish for `F_2`.

### Proof

General semiregularity compatibility always gives

```text
ker(ob_F2) subset ker(c_beta-prime).
```

Section 6 proves the reverse inclusion from weak `G`-semiregularity of the total external-product object. Hence the kernels are equal. `HC-R021-L006` gives the rank `20` conclusion.

Derived equivalence does not change the statement: functoriality transports the semiregularity map, Hochschild action, equivariant structure, and obstruction class through Markman's Orlov equivalence.

QED.

## 8. Consequence for the proof DAG

Route G is not an independent bypass around the direct first-order frontier.

The correct ordering is

```text
second-factor rank 20 / eight relations          [REQUIRED]
        |
        +--> coherent D20 point, or non-formal
        |    perfect-complex analogue
        |
        v
construct useful finite symmetry of total object
        |
        v
G3: weak G-semiregularity of final eightfold     [OPEN]
        |
        v
Perry all-orders algebraicity transport          [CONDITIONAL]
```

`L017` remains useful: it proves that for the coherent second factor in the source-relevant `qN>=4` range, one cannot establish the required total weak semiregularity by first proving factorwise weak semiregularity. `L018` is stronger conceptually: even a genuinely total weakly equivariant solution must already contain the second-factor rank-20 cancellation.

## 9. Immediate corollaries

1. The rank-22 split control `P_beta` of `L015` cannot be rescued by any finite identity-component symmetry after taking the external product: its nonzero `k_7,k_8` obstructions survive as invariant total obstructions.
2. Every split line-bundle complex ruled out by `L016` is likewise excluded from the Perry Route G, not merely from coherent `D20`.
3. The active mathematical frontier is therefore the construction of a second-factor object with the eight-relation/rank-20 property. Equivariance becomes relevant only after that first-order condition is met.

## 10. Scope

This result does not prove that a rank-20 second factor exists.

It does not prove that rank `20` is sufficient for weak `G`-semiregularity of the final object: the remaining total obstruction space, especially the mixed

```text
Ext^1(E_0,E_0) tensor Ext^1(F_2,F_2)
```

summand, must still be controlled.

It also does not replace the all-orders hypotheses of Perry's theorem.

## 11. Current disposition

```text
HC-R021-L018 = proved_in_solve_package_not_certified
weak_G_equals_G_semiregularity_for_finite_identity_component_actions_on_abelian_varieties = true
final_weak_G_semiregularity_implies_second_factor_rank20 = true
route_G_independent_bypass_of_D20 = false
rank22_split_control_rescuable_by_equivariance = false
second_factor_rank20_exists = open
final_G3_after_rank20 = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 12. Sources

- Alexander Perry, arXiv:2604.00511v2, Definition 2.6, Lemma 2.7, Lemma 3.3, Proposition 5.19, and Theorem 1.2.
- Eyal Markman, arXiv:2509.23079, Example 11.2.7 and Lemma 11.2.8.
- `work_packages/HC_R021_P4_CONTRACTION_RANK.md` (`HC-R021-L006`).
- `work_packages/HC_R021_P4_ATIYAH_RANK_REDUCTION.md` (`HC-R021-L007`).
- `work_packages/HC_R021_P4_LINE_BUNDLE_CONTROL.md` (`HC-R021-L015`).
- `work_packages/HC_R021_P4_SPLIT_LINE_BUNDLE_NO_GO.md` (`HC-R021-L016`).
- `work_packages/HC_R021_P4_AUTOEQUIV_STABILIZER_BOUND.md` (`HC-R021-L017`).
