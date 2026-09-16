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
P4-G: Does a same-Chern-character CM4 representative admit a finite derived symmetry
      G for which the resulting object is weakly G-semiregular?
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

### 5.2 Second secant factor in the source

The second CM4 class in Markman Example 11.2.7 is

```text
beta' = g^*Theta - (q/6)(g^{-1})^*(Theta^3).
```

Markman constructs a simple coherent sheaf with Chern character an integer multiple of `beta'` by choosing `N` generic translates of another secant sheaf, intersecting them with a curve `C'`, and gluing along intersection fibers.

The published construction does not supply a finite translation subgroup preserving the whole gluing datum or a weak-semiregularity proof. That omission matters for the **source object**, but finite equivariance of a same-ray replacement can be obtained without reconstructing the gluing.

## 6. Orbit-equivariant replacement

### HC-R021-L003 — finite-equivariant same-ray replacement

Let `F` be any coherent sheaf or perfect complex on a complex abelian variety `X` and let `H subset X` be a finite subgroup acting by translations. Define

```text
Ind_H(F) = direct_sum_{h in H} tau_h^* F.
```

Then:

1. `Ind_H(F)` admits a canonical `H`-linearization by reindexing the summands;
2. translations act trivially on singular cohomology, so

```text
ch(Ind_H(F)) = |H| ch(F);
```

3. if `F` is gluable (`Ext^{<0}(F,F)=0`) and is a coherent sheaf, the orbit sum is again a coherent sheaf and hence gluable;
4. every homogeneous secant/Chern-character condition depending only on the ray of `ch(F)` is unchanged.

### Proof

For `k in H`,

```text
tau_k^* Ind_H(F)
  = direct_sum_{h in H} tau_{k+h}^* F
  ~= direct_sum_{h in H} tau_h^* F,
```

where the final isomorphism is the permutation `h -> k+h`. These permutation isomorphisms satisfy the group law, giving an `H`-linearization.

For every translation `tau_h` of an abelian variety, `tau_h^*` is the identity on rational singular cohomology. Therefore

```text
ch(tau_h^*F)=ch(F)
```

and additivity of the Chern character gives statement 2. Statements 3 and 4 follow from finite direct sums and homogeneity.

QED.

### Application to the CM4 pair

Apply `HC-R021-L003` independently to both genus-four secant factors. In particular, for the source sheaf `E'` with

```text
ch(E') = N beta',
```

and any finite translation subgroup `H_2`, the orbit sum has

```text
ch(Ind_H2(E')) = |H_2| N beta'.
```

This remains on the exact `beta'` ray used by Markman's nonzero-Weil-projection criterion. Likewise the first secant factor can be replaced by a finite-equivariant orbit sum without moving its Chern-character ray.

Hence **finite equivariance and linearization are not the remaining obstruction**. The orbit-sum construction closes `P4-G2` at the level needed to preserve the cohomological secant criterion.

## 7. Why orbit equivariance does not solve P4

`HC-R021-L003` must not be promoted into a semiregularity statement.

For an induced orbit object, equivariant self-Ext contains morphisms among the orbit summands. Via induction/forgetful adjunction it is controlled by terms of the form

```text
Ext^2(F, tau_h^*F),  h in H,
```

not merely by a small invariant subspace of `Ext^2(F,F)`. A canonical linearization therefore does not imply that the semiregularity map in the invariant category is injective.

Equivalently, the implication

```text
finite H-linearization
    -/-> weak H-semiregularity
```

is forbidden.

This matters especially for an external product. Its degree-two self-Ext has Kunneth contributions of the forms

```text
Ext^2(F_1,F_1) tensor Ext^0(F_2,F_2),
Ext^1(F_1,F_1) tensor Ext^1(F_2,F_2),
Ext^0(F_1,F_1) tensor Ext^2(F_2,F_2).
```

Even factorwise control of invariant degree-two Ext does not automatically control the mixed `Ext^1 tensor Ext^1` term.

The all-orders question is therefore localized one step further:

```text
P4-G3: find a genuinely useful finite symmetry/representative for which the
       total external-product or Fourier-Mukai object is weakly G-semiregular.
```

## 8. Sixfold analogy and exact non-transfer

In the earlier split-Weil sixfold case, Markman explicitly proves that the relevant finite group action captures the image of the obstruction homomorphism and that semiregularity is injective on the invariant `Ext^2` subspace. Perry then transports that finite group through the derived equivalence and applies his theorem directly.

Those exact facts are not presently proved for the CM4 genus-four pair. Importing them would be a new hidden theorem and is forbidden by `HC-FP-007`.

The useful sixfold template is therefore not “add a finite group”; it is:

```text
construct a finite symmetry whose invariant Ext^2 is exactly small enough,
then prove semiregularity is injective on that controlled invariant space.
```

## 9. Refined P4 sub-obligations

The shortest current closure path is now:

```text
P4-G0  Perry specialization HC-R021-L002                         [SOLVE-PROVED, NOT CERTIFIED]
   |
   +--> P4-G1  finite-equivariant first-factor representative       [SOURCE / L003 AVAILABLE]
   |
   +--> P4-G2  finite-equivariant beta'-ray representative          [SOLVE-PROVED BY L003]
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

`P4-G3` is now the sole live algebraicity-transport obstruction on this route.

## 10. Next mathematical tests

Run these in order.

1. **Reject induced symmetries that do not shrink the obstruction space.** For the orbit-sum replacements of `L003`, compute the equivariant `Ext^2` through induction/forgetful adjunction. If the identity-sector kernel already contains a kernel of ordinary semiregularity, discard that group immediately.
2. **Exploit the source cyclic quotient.** For the first factor, use Markman's `G_1`-invariant partial-normalization object from Example 8.2.3 rather than an arbitrary orbit sum and compute `Ext^2` in the quotient/invariant category.
3. **Search for a non-induced second-factor symmetry.** Rebuild the `beta'` representative from orbit-stable geometric data only if this can genuinely reduce invariant `Ext^2`; mere orbit summation is no longer a useful target.
4. **Control the product mixed term.** For any candidate `G_1 x G_2`, compute the invariant contribution of `Ext^1 tensor Ext^1`. Do not infer product semiregularity from degree-two factorwise injectivity.
5. **Derived transport and Perry.** Only after weak equivariant semiregularity is established, transport the group through `Phi` as in Perry's sixfold argument and invoke Theorem 1.2.

## 11. Claim boundary

```text
HC-R021-P4_closed = false
HC-R021-L002 = proved_in_solve_package_not_certified
HC-R021-L003 = proved_in_solve_package_not_certified
finite_equivariant_same_ray_representatives = available
Perry_theorem_applicable_if_weak_G_semiregularity = true
weak_G_semiregularity_of_CM4_object = open
HC-R021-P5 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

This package does not claim that Perry's 2026 theorem proves the CM4 Hodge target. It proves that Perry eliminates the all-orders deformation problem **conditional on one exact equivariant-semiregularity property**, and that finite equivariance itself is easy to supply without changing the secant rays. The remaining construction debt is precisely weak equivariant semiregularity of a useful genus-four CM4 representative.
