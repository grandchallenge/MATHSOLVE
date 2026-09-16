# HC-R021-A8-SW-Q3 — Generic split-Weil eightfold target

**Campaign:** `HC-001`  
**Theorem-spine node:** `HC-R021`  
**State:** `SELECTED_RESEARCH_TARGET__UNPROVED`  
**Selection date:** 2026-09-16  
**Coefficient ring:** `Q`  
**Cycle equivalence:** rational equivalence  
**Nontrivial codimension:** `p = 4` in complex dimension `8`

## 1. Exact restricted class

Fix

```text
K = Q(sqrt(-3)).
```

Let `M_split,3` be the connected component of the moduli space of polarized complex abelian eightfolds of split Weil type for `K` that contains the `X x X-hat` base point produced by the split-Weil construction in Markman, *Secant sheaves and Weil classes on abelian varieties*, Sections 4, 8, and 12, with the Section-12 integer equal to `3`.

The split condition is part of the definition. In the quadratic-imaginary case and dimension `2n=8`, Markman's cited discriminant criterion identifies it with the split discriminant coset `(-1)^n = 1` in

```text
Q^x / Nm_(K/Q)(K^x).
```

Define `C_8,3` to be the members `(A, eta, h)` of this component satisfying the generic Hodge-ring condition used in Markman's Equation (1.1):

```text
Hdg^8(A,Q)
  = Im[Sym^4(H^(1,1)(A,Q)) -> H^8(A,Q)]
    direct_sum HW(A,eta),
```

and, equivalently for this target, no additional codimension-four rational Hodge classes occur beyond the divisor-generated summand and the Weil subspace.

This condition is an explicit restriction of the variety class. No statement is made for special members where the Hodge ring jumps.

## 2. HC-R021 theorem statement

> **HC-R021-A8-SW-Q3.** For every `(A, eta, h)` in `C_8,3`, and every
>
> ```text
> alpha in H^8(A,Q) intersect H^(4,4)(A),
> ```
>
> construct a rational codimension-four algebraic cycle
>
> ```text
> z = sum_i q_i [Z_i] in CH^4(A) tensor Q
> ```
>
> such that
>
> ```text
> cl_Q^4(z) = alpha.
> ```

The arbitrary-input quantifier is over every rational codimension-four Hodge class on every member of the explicitly restricted class `C_8,3`.

## 3. Why this target is admitted

The current source refresh changes the July 2026 target boundary.

- Abelian fourfolds are no longer admissible research targets: Markman's Theorem 1.2 supplies algebraicity of their Weil classes, and the current Hodge-ring results imply the Hodge conjecture for all abelian varieties of dimension at most five.
- Split-Weil abelian sixfold Weil classes are already algebraic by the same theorem.
- Non-split Weil sixfolds remain closer in dimension, but current sources do not provide an executable cycle-construction mechanism. Mostaed's 2026 analysis instead isolates the absence of the `K`-secant structure and uncontrolled discriminant as active obstructions.
- Markman's Section 12 supplies an explicit algebraic secant object for a split-Weil dimension-eight attempt and identifies one exact missing deformation-theoretic condition, Question 11.4.

The selected target therefore trades dimension for a materially better construction interface. It is the smallest source-current lane found in this tranche that is both open and attached to a concrete algebraic object rather than only to a detector, period computation, motivic substitute, or arithmetic comparison.

No novelty or priority claim is made. This target is deliberately close to Markman's published/preprint construction programme.

## 4. Construction reduction for an arbitrary input class

Let `(A,eta,h)` be in `C_8,3` and let `alpha` be an arbitrary rational `(4,4)` class. By the defining generic Hodge-ring condition,

```text
alpha = delta + gamma,
```

where

```text
delta in Im Sym^4(H^(1,1)(A,Q)),
gamma in HW(A,eta).
```

### 4.1 Divisor-generated summand

By Lefschetz `(1,1)`, every rational class in `H^(1,1)(A,Q)` is the rational first Chern class of a divisor. Products of these divisor classes are cycle classes of intersections/products in the Chow ring. Hence `delta` has a rational codimension-four algebraic-cycle preimage.

This use of Lefschetz `(1,1)` does not extrapolate the divisor theorem to the Weil summand.

### 4.2 Weil summand

For Weil type, `HW(A,eta)` is one-dimensional over `K`. The `K` action comes from actual rational endomorphisms of the abelian variety and therefore acts in cohomology through algebraic graph correspondences.

Consequently, it is enough to construct **one nonzero algebraic class**

```text
gamma_0 in HW(A,eta).
```

Then the `K` orbit and rational linear combinations produce every `gamma in HW(A,eta)` by algebraic correspondences.

Thus the theorem-grade construction problem is reduced to a nonzero Weil-class construction that survives throughout the specified component.

## 5. Markman secant-object route specialized to `K=Q(sqrt(-3))`

Let `(X,Theta)` be a principally polarized abelian fourfold. Markman's Section 12 takes an odd integer `m >= 3`; specialize to

```text
m = 3,
K = Q(sqrt(-3)),
r = (m+9)/2 = 6.
```

Choose six generic translates

```text
D_i,  i in Z/6Z,
```

of the theta divisor with the stated smooth-intersection conditions. Set

```text
Z_i = D_i intersect D_(i+1),
Z = union_i Z_i,
```

and let

```text
nu : Z_tilde -> Z
```

be Markman's partial normalization along the prescribed isolated self-intersection points.

The algebraic derived object

```text
F = [ O_X -> nu_* O_(Z_tilde) ] tensor O_X(Theta)
```

has Chern character in the rational secant plane

```text
B = span_Q { exp(sqrt(-3) Theta), exp(-sqrt(-3) Theta) }.
```

The general strategy then seeks two suitable secant objects `F_1,F_2`, forms the Fourier-Mukai/Orlov transform

```text
E = Phi(F_1 boxtimes F_2^vee)
```

on `X x X-hat`, and uses the normalized Chern character

```text
kappa(E) = ch(E) exp(-c_1(E)/rank(E)).
```

The desired middle component must have a nonzero projection to `HW` rather than lying entirely in the divisor algebra.

## 6. Exact proof-obligation DAG

```text
R021-P0  exact class C_8,3 and generic Hodge-ring decomposition
   |
   +--> R021-P1  algebraic preimage for every divisor-polynomial delta
   |
   +--> R021-P2  Section-12 secant object is admissible for the strategy
   |       |
   |       +--> P2a  produce two algebraic coherent/derived secant objects F1,F2
   |       +--> P2b  Fourier-Mukai object E has nonzero rank or an admissible normalized class
   |       +--> P2c  verify Markman condition (2b): kappa(E) remains Hodge in the target deformation directions
   |       +--> P2d  verify condition (2c): kappa_4(E) has a nonzero HW projection
   |
   +--> R021-P3  weak semiregularity at first order
   |       |
   |       +--> R021-L001  PROVED BELOW
   |
   +--> R021-P4  all-orders deformation bridge
   |       |
   |       +--> P4a  prove Question 11.4 in the needed coherent/twisted/derived scope
   |              OR
   |       +--> P4b  prove full semiregularity for the specific E
   |
   +--> R021-P5  deform the algebraic nonzero HW class through the entire selected component
   |
   +--> R021-P6  use algebraic K-action to generate every gamma in HW(A,eta)
   |
   +--> R021-P7  combine delta and gamma to construct z for arbitrary alpha
```

No edge from `P3` to `P5` is admitted without `P4`.

## 7. Substantive proof attempt: first-order weak semiregularity

### HC-R021-L001 — first-order obstruction vanishing on the evaluation image

Let `Y` be a smooth projective variety and `E` an algebraic coherent object in the scope where the Hochschild evaluation map and semiregularity map are defined. Write

```text
ev_E : HH^2(Y) -> Ext^2(E,E)
```

for evaluation and

```text
sigma_E : Ext^2(E,E) -> SR(E)
```

for the semiregularity map. Assume

```text
sigma_E restricted to Im(ev_E)
```

is injective.

Let `xi in HH^2(Y)` be a first-order ambient/categorical deformation direction for which the corresponding infinitesimal variation of `ch(E)` vanishes in the semiregularity target; under HKR this is the condition

```text
xi contraction ch(E) = 0.
```

Then the obstruction to deforming `E` in the direction `xi` vanishes:

```text
ev_E(xi) = 0.
```

### Proof

The Buchweitz-Flenner/Markman compatibility diagram used in Markman's Section 11.4 gives

```text
sigma_E(ev_E(xi)) = xi contraction ch(E).
```

The right side is zero by the Hodge-preserving hypothesis. Therefore

```text
sigma_E(ev_E(xi)) = 0.
```

But `ev_E(xi)` lies in `Im(ev_E)`, and `sigma_E` is injective on that image. Hence

```text
ev_E(xi) = 0.
```

This proves the first-order obstruction vanishes. QED.

### Exact scope of the lemma

`HC-R021-L001` is only a first-order statement. It does **not** prove Markman's Question 11.4 and does not produce an analytic or algebraic family of deformations of `E`.

The remaining mathematical content is all-orders: one must show that the obstruction classes for successive thickenings remain controlled by the evaluation image in a functorial way, or bypass that requirement by proving full semiregularity for the specific Section-12 object.

This distinction is the current algebraicity obstruction. Treating first-order vanishing as a relative algebraic cycle would trigger `HC-FP-007`.

## 8. Immediate falsification tests for the selected route

Before attempting a global deformation theorem, the following checks can kill the route cheaply.

1. **Derived-object admissibility.** Section 12 exhibits an algebraic derived object, while the semiregularity theorem used in the sixfold proof is stated for coherent/twisted sheaves. The route must either realize the required class by an admissible sheaf or prove the deformation interface for the derived object actually used.
2. **Nonzero Weil projection.** For `K` quadratic, Markman's Section 10 reduces condition `(2c)` to a finite statement in the decomposition of `B tensor B`. The chosen `F_1,F_2` must have a tensor component outside `BB_0`. If every admissible Section-12 pair lands in `BB_0`, this target route fails before deformation theory.
3. **Rank/normalization.** The use of `kappa(E)=ch(E)exp(-c_1(E)/rank(E))` requires a legitimate nonzero rank or a separately proved replacement invariant.
4. **Generic-locus closure.** The theorem is restricted to `C_8,3`; no step may claim special fibers with additional Hodge classes.
5. **All-orders bridge.** First-order obstruction vanishing is insufficient. A proof must close the Artin/analytic deformation tower or provide an explicit relative algebraic cycle.

These are the next mathematical tasks, in that order.

## 9. HC-R021 admission rubric

1. exact variety class — **pass**, `C_8,3` above;
2. exact dimension — **pass**, `8`;
3. exact codimension — **pass**, `4`;
4. coefficient ring `Q` — **pass**;
5. cycle equivalence — **pass**, rational equivalence;
6. nontrivial beyond boundary cases — **pass**;
7. source-defined unsolved boundary — **pass**, Markman Section 12 / Question 11.4;
8. actual cycle-construction mechanism — **pass with open obligations**, algebraic secant object -> Fourier-Mukai object -> normalized Chern class -> HW projection;
9. route to cohomological equality — **pass as proof DAG**, divisor decomposition plus HW generation;
10. arbitrary-input quantifier — **pass**, every `alpha` in the restricted class;
11. deformation/specialization control — **open material obligation P4-P5**;
12. false-proof resistance — **pass with HC-FP-007 active until P4 closes**;
13. prior-art distance — **pass for research selection; novelty not claimed**;
14. formalizable finite/algebraic sub-obligations — **pass**, `B tensor B` projection, Chern-character identities, intersection combinatorics;
15. information value on failure — **high**, failure localizes to object admissibility, HW projection, or semiregularity rather than generic Hodge detection;
16. implication into HC-P03 — **direct restricted instance if P0-P7 close**;
17. non-implications — **explicit**, no all-eightfold, all-special-fiber, all-abelian, or universal Hodge conclusion;
18. MATHCERT boundary — **new Cert handoff only after a substantive theorem closes; current WP00 certificate is not reopened**.

## 10. Current mathematical disposition

```text
full_hodge_conjecture_proved = false
restricted_target_selected = true
HC-R021-A8-SW-Q3_proved = false
HC-R021-L001_first_order_lemma = proved_in_solve_package_not_certified
current_blocking_obligation = R021-P2 then R021-P4
```

The next highest-value action is not a period computation. It is to resolve `P2a-P2d` for the explicit `m=3` Section-12 secant object and then determine whether the weak semiregularity condition can be promoted from the first-order lemma above to the all-orders deformation statement required by `P4`.

## 11. Sources

- Eyal Markman, *Secant sheaves and Weil classes on abelian varieties*, arXiv:2509.23403v2, especially Sections 1.1, 4, 10, Question 11.4, Section 11.5, and Section 12: https://arxiv.org/abs/2509.23403
- Eyal Markman, *Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds*, arXiv:2502.03415v2: https://arxiv.org/abs/2502.03415
- Amir Mostaed, *McMullen's Curve, the Weil Locus, and the Hodge Conjecture for Abelian Sixfolds*, arXiv:2603.20268: https://arxiv.org/abs/2603.20268

The source locators above define the research boundary. They do not confer certification or novelty.
