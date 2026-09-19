# HC-R021-P4 — Perry equivariant-semiregularity reduction

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent protected revision:** `5b1778981ca3696501718934be27bf91b547ab00`  
**State:** `P4_REDUCED__WEAK_EQUIVARIANT_SEMIREGULARITY_OPEN`  
**Date:** 2026-09-16

## 1. Purpose

Reduce the all-orders algebraicity-transport obligation `HC-R021-P4` to the narrowest theorem-grade conditions exposed by Alexander Perry's 2026 equivariant semiregularity theorem.

The result of this tranche is a reduction, not a proof of `HC-R021-A8-CM4-C2`.

## 2. Perry theorem interface

Source:

- Alexander Perry, *The semiregularity theorem for equivariant noncommutative varieties*, arXiv:2604.00511, Theorem 1.2 and Theorem 6.3: https://arxiv.org/abs/2604.00511

Let

```text
f : A -> S
```

be a smooth proper family of complex abelian varieties with `0 in S(C)`. Let

```text
G subset A_0 x A_0^vee
```

be finite and act on `Dperf(A_0)` by translations and tensoring by degree-zero line bundles. Perry's Theorem 1.2 applies when a perfect complex `E_0` is weakly `G`-semiregular, has

```text
Ext^i(E_0,E_0)=0  for i<0,
```

and there is an algebraic rational class `B_0` such that

```text
w_0 = exp(B_0) ch(E_0)
```

extends to a global flat section of the even rational cohomology local system and remains Hodge along `S`.

The theorem then gives:

1. a twisted-perfect deformation of `E_0` over an etale neighborhood of the base point;
2. algebraicity of the transported class `w_s` for **every** `s in S(C)`.

Perry defines `G`-semiregularity by injectivity of the degree-two semiregularity map on `Ext^2(E_0,E_0)^G`. Weak `G`-semiregularity asks for semiregularity of the corresponding equivariant object in the invariant category. `G`-semiregularity implies weak `G`-semiregularity.

The theorem is therefore global **along the chosen family `S`**, but it does not by itself identify an abstract period-domain component with one algebraic family. That family-coverage interface is recorded separately below.

## 3. HC-R021-L002 — Perry closure criterion along a family

Let

```text
A_0 = X x X-hat,
E_0 = Phi(F_1 boxtimes F_2^vee)
```

be the exact genus-four CM4 object of Markman arXiv:2509.23079, Example 11.2.7 and Lemma 11.2.8.

Fix a connected smooth proper algebraic family

```text
f : A -> S
```

through `A_0` inside the selected CM/Weil deformation locus such that Markman's flat class `kappa(E_0)` extends along `S` and remains Hodge.

Assume there exists a finite group

```text
G subset A_0 x A_0^vee
```

for which `E_0` is weakly `G`-semiregular.

Then `HC-R021-P4` closes **along this family `S`**: the transported normalized class is algebraic on every fiber of `S`.

### Proof

Markman's object has nonzero rank `r`. Put

```text
B_0 = -c_1(E_0)/r.
```

Since `E_0` is algebraic, `B_0` is an algebraic rational degree-two class and

```text
exp(B_0) ch(E_0) = kappa(E_0).
```

Markman supplies Hodge persistence of the flat deformation of `kappa(E_0)` under the relevant CM/Weil deformations.

The source factors are coherent sheaves, up to derived dual on the second factor. A coherent sheaf has no negative self-Ext. Derived duality preserves self-Ext degree, the external-product Kunneth decomposition preserves vanishing in negative total degree, and Orlov/Fourier-Mukai equivalence preserves Ext groups. Hence

```text
Ext^i(E_0,E_0)=0  for i<0.
```

Under weak `G`-semiregularity, Perry Theorem 1.2 therefore applies to `f:A->S` with `w_0=kappa(E_0)` and makes `kappa(E_0)` algebraic on every fiber of `S`.

Markman also proves that the degree-four component has a nonzero projection to the Weil subspace. Its divisor-product component is algebraic. Subtracting that component gives one nonzero algebraic Weil class on every fiber of `S`.

QED.

### Exact scope

`HC-R021-L002` does **not** by itself say that every point of the abstract set `C_CM4` lies in one algebraic family `S` carrying the required global flat section. To conclude the full target from familywise algebraicity, one must also discharge `HC-R021-P4-G6` below.

## 4. Family-coverage interface — HC-R021-P4-G6

The selected class `C_CM4` was defined through a connected period-domain/deformation component. Perry works over a smooth proper algebraic family.

The required global interface is:

> cover the selected Hodge-generic locus by connected algebraic families of polarized abelian varieties with the prescribed CM/Weil structure, containing or connected by overlaps to the source point, so that Markman's flat Weil class is represented by the corresponding global section of the Gauss-Manin local system.

A standard level-structure/PEL-moduli realization is the expected route, but this package does not silently promote that standard background into a checked campaign theorem. Before `HC-R021-P4` is marked closed globally, the exact moduli/family carrier used for `C_CM4` must be named and its coverage of the target quantifier recorded.

**State:** `STANDARD_MODULI_INTERFACE__REQUIRES_EXPLICIT_BINDING`.

This is not presently the difficult deformation-theoretic obstruction; `P4-G3` remains the active research frontier. It is nevertheless a required closure edge.

## 5. What Perry removes from the open obligation

Once weak equivariant semiregularity and the family interface are established, the following need not be proved ad hoc:

- an Artin obstruction tower for `E_0`;
- propagation of `HC-R021-L001` by hand to all orders;
- a separate algebraization theorem for formal liftings;
- a new perfect-complex semiregularity theorem.

The active deformation-theoretic question is therefore:

```text
P4-G3: does a useful same-Chern-character CM4 representative admit
       a finite derived symmetry G for which it is weakly G-semiregular?
```

## 6. Finite symmetry reconnaissance

### 6.1 First secant factor

Markman's CM4 construction uses the genus-four secant class

```text
alpha_0 = Theta - (q/6) Theta^3,
```

with `q` a positive integer.

Markman arXiv:2502.03415, Example 8.2.3, gives in dimension four an alternative object with the same Chern character built from a cyclic translation group of order `q+1`. The partial-normalization data can be chosen invariant and the object descends to the quotient.

This provides a genuinely geometric finite symmetry, but not by itself weak equivariant semiregularity.

### 6.2 Second secant factor

The second CM4 ray is

```text
beta' = g^*Theta - (q/6)(g^{-1})^*(Theta^3).
```

Markman Example 11.2.7 constructs a simple coherent sheaf on this ray by generic translates and gluing. The source does not provide a useful finite symmetry or semiregularity proof for that object.

Finite equivariance of a same-ray replacement, however, is easy and is separated from semiregularity by `HC-R021-L003`.

## 7. HC-R021-L003 — finite-equivariant same-ray replacement

Let `F` be a coherent sheaf or perfect complex on an abelian variety `X`, and let `H subset X` be a finite translation subgroup. Define

```text
Ind_H(F) = direct_sum_{h in H} tau_h^*F.
```

Then:

1. `Ind_H(F)` has a canonical `H`-linearization by permutation of the summands;
2. translations act trivially on rational singular cohomology, so

```text
ch(Ind_H(F)) = |H| ch(F);
```

3. if `F` is coherent, the orbit sum is coherent and has no negative self-Ext;
4. any homogeneous secant/Chern-character condition depending only on the ray of `ch(F)` is preserved.

### Proof

For `k in H`, translation permutes the orbit summands:

```text
tau_k^* Ind_H(F)
  = direct_sum_h tau_(k+h)^*F
  ~= direct_sum_h tau_h^*F.
```

The reindexing isomorphisms satisfy the group law. Since every translation is cohomologically trivial on an abelian variety, all translated summands have the same Chern character; additivity gives the formula above. The remaining statements follow from finite direct sums and homogeneity.

QED.

Applied to the `beta'` source sheaf `E'`, this gives

```text
ch(Ind_H(E')) = |H| N beta',
```

so the Markman nonzero-Weil-projection criterion remains on the same ray.

Thus finite equivariance and linearization are available. They are not the live obstruction.

## 8. Why orbit equivariance is insufficient

For an induced orbit object, equivariant self-Ext contains cross-orbit terms. Through induction/forgetful adjunction it is controlled by groups of the form

```text
Ext^2(F, tau_h^*F),  h in H,
```

rather than only by a small subspace of `Ext^2(F,F)`.

Therefore

```text
finite H-linearization
    -/-> weak H-semiregularity.
```

For an external product, degree-two self-Ext also contains the Kunneth summands

```text
Ext^2(F_1,F_1) tensor Ext^0(F_2,F_2),
Ext^1(F_1,F_1) tensor Ext^1(F_2,F_2),
Ext^0(F_1,F_1) tensor Ext^2(F_2,F_2).
```

Factorwise degree-two injectivity does not control the mixed `Ext^1 tensor Ext^1` contribution.

The sixfold precedent works because Markman proves injectivity on the relevant invariant obstruction space; adding a group is not enough.

## 9. Refined proof obligations

```text
P4-G0  Perry specialization / HC-R021-L002                  [SOLVE-PROVED, FAMILYWISE]
   |
   +--> P4-G1  finite-equivariant first-factor ray          [AVAILABLE]
   |
   +--> P4-G2  finite-equivariant beta'-ray representative  [SOLVE-PROVED BY L003]
   |
   +--> P4-G3  weak G-semiregularity of a useful total
   |            representative, including mixed Ext^1 term   [OPEN]
   |
   +--> P4-G4  transport G through Orlov equivalence         [THEOREM INTERFACE AVAILABLE]
   |
   +--> P4-G5  apply Perry along each bound family           [CONDITIONAL ON G3]
   |
   +--> P4-G6  bind algebraic family/moduli coverage of
   |            the full C_CM4 target quantifier             [STANDARD INTERFACE; UNBOUND]
   |
   +--> P5     algebraic nonzero Weil class on each target   [CONDITIONAL ON G5+G6]
```

The active research obstruction is `P4-G3`; `P4-G6` is a closure interface that must be made explicit before any global theorem claim.

## 10. Next mathematical tests

1. Reject induced symmetries that do not shrink the invariant obstruction space by computing equivariant `Ext^2` via induction/forgetful adjunction.
2. Use Markman's non-induced cyclic quotient object from Example 8.2.3 as the first-factor model.
3. Seek a genuinely symmetric `beta'` representative whose invariant `Ext^2` is smaller than that of the naive orbit sum.
4. For any candidate product, compute the invariant mixed `Ext^1 tensor Ext^1` contribution explicitly.
5. Once `P4-G3` closes, bind `P4-G6` to an exact algebraic moduli/family carrier and invoke Perry familywise.

## 11. Claim boundary

```text
HC-R021-P4_closed = false
HC-R021-L002 = proved_in_solve_package_not_certified_familywise
HC-R021-L003 = proved_in_solve_package_not_certified
finite_equivariant_same_ray_representatives = available
weak_G_semiregularity_of_useful_CM4_representative = open
P4_G6_family_coverage = unbound_standard_interface
HC-R021-P5 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

Perry's theorem gives algebraicity at every point of a **specified smooth proper family** when its hypotheses hold. This package does not silently identify that family with the whole abstract period-domain component. The remaining substantive research debt is weak equivariant semiregularity; the remaining global-scope bookkeeping debt is explicit family coverage.