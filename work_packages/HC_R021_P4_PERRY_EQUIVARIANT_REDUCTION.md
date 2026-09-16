# HC-R021-P4 — Perry equivariant-semiregularity reduction

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent protected revision:** `5b1778981ca3696501718934be27bf91b547ab00`  
**State:** `P4_REDUCED__WEAK_EQUIVARIANT_SEMIREGULARITY_OPEN`  
**Date:** 2026-09-16

## 1. Purpose

Sharpen the all-orders algebraicity-transport obligation `HC-R021-P4` using the 2026 equivariant semiregularity theorem of Alexander Perry.

The prior formulation allowed three broad closure paths:

1. prove ordinary semiregularity of Markman's CM4 object;
2. prove that the weaker first-order injectivity condition propagates through the full deformation functor;
3. construct a relative algebraic replacement directly.

Perry's theorem supplies a fourth and substantially narrower path:

> exhibit a finite derived symmetry group for which the Markman object is weakly equivariantly semiregular.

If that condition is proved, the all-orders deformation and algebraicity transport required by `P4` follow from an existing theorem. The current package proves this reduction. It does not prove the missing weak equivariant semiregularity condition.

## 2. External theorem used

Source:

- Alexander Perry, *The semiregularity theorem for equivariant noncommutative varieties*, arXiv:2604.00511, Theorem 1.2 and Theorem 6.3: https://arxiv.org/abs/2604.00511

For the abelian-variety specialization, let

```text
f : A -> S
```

be a smooth proper family of complex abelian varieties, let `0 in S(C)`, and let

```text
G subset A_0 x A_0^vee
```

be finite, acting on `Dperf(A_0)` through translations and tensoring by degree-zero line bundles. If a perfect complex `E_0` is weakly `G`-semiregular, has

```text
Ext^i(E_0,E_0) = 0  for i < 0,
```

and an algebraic rational class `B_0 in H^2(A_0,Q(1))` is such that

```text
w_0 = exp(B_0) ch(E_0)
```

remains Hodge along `S`, then Perry proves:

1. `E_0` deforms as a twisted perfect complex over an etale neighborhood of `0`;
2. the flat class `w_0` remains algebraic along the family.

Perry defines `G`-semiregularity by injectivity of the degree-two semiregularity map on `Ext^2(E_0,E_0)^G`, and weak `G`-semiregularity by semiregularity of a corresponding equivariant object in the invariant category. `G`-semiregularity implies weak `G`-semiregularity.

Perry also applies the theorem directly to Markman's earlier split-Weil sixfold construction, where a finite translation group and equivariant semiregularity had already been established.

## 3. Specialized closure lemma

### HC-R021-L002 — Perry closure criterion for the CM4 object

Let

```text
A_0 = X x X-hat
```

and let

```text
E_0 = Phi(F_1 boxtimes F_2^vee)
```

be the exact genus-four CM4 object of Markman arXiv:2509.23079, Example 11.2.7 and Lemma 11.2.8, used in `HC-R021-A8-CM4-C2`.

Assume there exists a finite subgroup

```text
G subset A_0 x A_0^vee
```

such that `E_0` is weakly `G`-semiregular for the induced action on `Dperf(A_0)`.

Then the all-orders algebraicity-transport obligation `HC-R021-P4` closes on the selected deformation component. Consequently, the nonzero Weil projection of `kappa_2(E_0)` gives the required algebraic nonzero Weil class on every target fiber in the selected Hodge-generic locus.

### Proof

Markman's object has nonzero rank `r`. Set

```text
B_0 = -c_1(E_0)/r.
```

Because `E_0` is algebraic, `c_1(E_0)` is algebraic and therefore `B_0` is an algebraic rational degree-two class. Hence

```text
exp(B_0) ch(E_0) = kappa(E_0).
```

Markman proves that the flat deformation of `kappa(E_0)` remains of Hodge type under the relevant CM/Weil deformations. Thus Perry's Hodge-persistence hypothesis is satisfied.

It remains to verify the negative-Ext hypothesis. The source factors are coherent sheaves, up to derived dual on the second factor. For a coherent sheaf `F` on a smooth projective variety,

```text
Ext^i(F,F)=0  for i<0.
```

Derived duality preserves self-Ext degree. The external-product Kunneth decomposition therefore gives

```text
Ext^i(F_1 boxtimes F_2^vee, F_1 boxtimes F_2^vee)=0  for i<0.
```

Orlov/Fourier-Mukai equivalence preserves Ext groups, so

```text
Ext^i(E_0,E_0)=0  for i<0.
```

Under the additional hypothesis that `E_0` is weakly `G`-semiregular, every hypothesis of Perry's abelian-variety theorem is therefore satisfied. Perry yields a twisted perfect deformation and algebraicity of the flat class `kappa(E_0)` along the family.

In degree four, Markman proves that `kappa_2(E_0)` lies in

```text
(divisor-product classes) + HW(A_0,eta)
```

with nonzero projection to `HW`. Algebraicity of the transported `kappa_2`, together with algebraicity of the divisor-product summand, gives one nonzero algebraic class in the transported Weil subspace. This is precisely the algebraicity-transport output required by `P4` and the input required by `P5`.

QED, conditional only on weak `G`-semiregularity.

## 4. What Perry removes from the open obligation

The following are no longer independent proof debts if weak equivariant semiregularity is established:

- construction of an ad hoc Artin obstruction tower;
- proof that the first-order `HC-R021-L001` condition propagates by hand;
- conversion of formal liftings to algebraic objects by an independent argument;
- extension of ordinary coherent-sheaf semiregularity to the Fourier-Mukai perfect complex by hand.

Perry's theorem packages those steps, including twisted perfect-complex deformation and algebraicity of the Hodge-persistent normalized Chern character.

Accordingly, the live mathematical question becomes:

```text
P4-G: Does Markman's exact CM4 object E_0 admit a finite derived symmetry
      G for which E_0 is weakly G-semiregular?
```

## 5. Source reconnaissance for finite symmetry

### 5.1 First secant factor

Markman's CM4 construction uses a genus-four secant class

```text
alpha_0 = Theta - (q/6) Theta^3,
```

with `q` a positive integer.

The earlier source

- Eyal Markman, *Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds*, arXiv:2502.03415, Example 8.2.3: https://arxiv.org/abs/2502.03415

constructs, for dimension four, an alternative secant object with the same Chern character which is built from a cyclic translation group `G_1` of order `q+1`. The partial-normalization data can be chosen `G_1`-invariant and the resulting object descends to the quotient `X/G_1`.

This is useful but does **not** by itself prove weak `G_1`-semiregularity. The same source explicitly warns that the more direct ideal-sheaf representative with this Chern character is unlikely to be semiregular and that injectivity on the invariant `Ext^2` can hold for at most finitely many parameters by a dimension-growth argument.

Thus:

```text
finite equivariance of a representative: available;
weak equivariant semiregularity: not established.
```

### 5.2 Second secant factor

The second CM4 class in Markman Example 11.2.7 is

```text
beta' = g^*Theta - (q/6)(g^{-1})^*(Theta^3).
```

Markman constructs a simple coherent sheaf with Chern character an integer multiple of `beta'` by choosing `N` generic translates of another secant sheaf, intersecting them with a curve `C'`, and gluing along intersection fibers.

The published construction does not supply:

- a finite translation subgroup preserving the whole gluing datum;
- a linearization of the resulting sheaf under such a subgroup;
- injectivity of semiregularity on invariant `Ext^2`;
- weak semiregularity of an equivariant object in an invariant category.

This second factor is therefore currently the sharper symmetry bottleneck.

### 5.3 The sixfold analogy does not silently transfer

In the earlier split-Weil sixfold case, Markman explicitly proves that the relevant finite group action captures the image of the obstruction homomorphism and that semiregularity is injective on the invariant `Ext^2` subspace. Perry then transports that finite group through the derived equivalence and applies his theorem directly.

Those exact facts are not presently proved for the CM4 genus-four pair. Importing them would be a new hidden theorem and is forbidden by `HC-FP-007`.

## 6. Why naive group averaging is insufficient

Given a sheaf `F`, one can force a finite-group equivariant object by replacing it with an orbit sum

```text
Ind_G(F) = direct_sum_{g in G} g^*F.
```

Translations act trivially on cohomology, so this only scales the Chern character and can preserve a secant-plane condition. But this construction does not imply weak equivariant semiregularity.

The invariant deformation space of the induced object contains morphisms between distinct orbit summands. Equivariance therefore does not by itself make

```text
sigma : Ext^2(Ind_G(F),Ind_G(F))^G -> HH_{-2}
```

injective. The required statement is a deformation-theoretic property, not a representation-theoretic averaging identity.

No promotion is allowed from

```text
G-equivariant
```

to

```text
weakly G-semiregular.
```

## 7. Refined P4 sub-obligations

The shortest current closure path is now:

```text
P4-G0  Perry specialization HC-R021-L002                         [SOLVE-PROVED, NOT CERTIFIED]
   |
   +--> P4-G1  choose a finite symmetry for a first secant representative
   |            with the required alpha_0 Chern character          [PARTIAL: equivariant representative exists]
   |
   +--> P4-G2  construct a compatible finite symmetry/linearization
   |            for a beta' representative                          [OPEN]
   |
   +--> P4-G3  prove the outer product is weakly G-semiregular,
   |            or prove weak G-semiregularity directly after Phi   [OPEN]
   |
   +--> P4-G4  transport G through the Orlov equivalence             [THEOREM INTERFACE AVAILABLE]
   |
   +--> P4-G5  apply Perry Theorem 1.2 to kappa(E_0)                 [CONDITIONAL ON G3]
   |
   +--> P5     obtain one algebraic nonzero Weil class per fiber     [CONDITIONAL ON G5]
```

`P4-G2` and `P4-G3` are the current material frontier.

## 8. Next mathematical tests

Run these in order.

1. **Symmetry reconstruction of Example 11.2.7.** Determine whether the generic-translate/gluing construction can be replaced by an orbit construction under a finite translation subgroup without changing the ray of `beta'` or destroying simplicity/gluability.
2. **Invariant Ext calculation.** For any such equivariant replacement, compute the `G`-invariant part of `Ext^2` before attempting full Ext calculations.
3. **Semiregularity restriction.** Compute the degree-two semiregularity map on that invariant subspace. A dimension obstruction already kills the route if the invariant source exceeds the available Hochschild target in the relevant grading.
4. **Product criterion.** If both secant factors are equivariantly controlled, prove weak `G_1 x G_2`-semiregularity of the external product, including the mixed `Ext^1 tensor Ext^1` summand. Do not assume factorwise degree-two injectivity controls the mixed term.
5. **Derived transport.** Only after step 4, transport the group through `Phi` as in Perry's sixfold argument and invoke Theorem 1.2.

## 9. Claim boundary

```text
HC-R021-P4_closed = false
HC-R021-L002 = proved_in_solve_package_not_certified
Perry_theorem_applicable_if_weak_G_semiregularity = true
weak_G_semiregularity_of_CM4_object = open
HC-R021-P5 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

This package does not claim that Perry's 2026 theorem proves the CM4 Hodge target. It proves that Perry eliminates the all-orders deformation problem **conditional on one exact equivariant-semiregularity property**, and it localizes the remaining construction debt to finite symmetry and invariant `Ext^2`/semiregularity for the genus-four CM4 secant pair.
