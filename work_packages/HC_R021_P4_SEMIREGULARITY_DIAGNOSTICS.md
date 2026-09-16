# HC-R021-P4 — Semiregularity diagnostics for the genus-four second factor

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent P4 reduction:** `work_packages/HC_R021_P4_PERRY_EQUIVARIANT_REDUCTION.md`  
**State:** `DIAGNOSTIC_LEMMAS_PROVED__CORE_KERNEL_COMPUTATION_OPEN`  
**Date:** 2026-09-16

## 1. Purpose

Determine what kind of semiregularity statement is mathematically plausible for the explicit second secant factor in Markman Example 11.2.7, and reduce the source question to a finite linear-algebra/deformation calculation.

The result is twofold:

1. full ordinary semiregularity is dimensionally impossible for a broad parameter range;
2. the weaker condition that Markman actually asks for is exactly a kernel-equality problem in `HT^2(X)`.

Neither result proves the required all-orders algebraicity transport.

## 2. Source object

Let `X` be the principally polarized Jacobian of a genus-four curve with principal polarization `Theta`. Let `g` be the automorphism in Markman Example 11.2.7 and put

```text
D := g^*Theta,
H := (g^{-1})^*Theta.
```

Both `D` and `H` are ample integral divisor classes and

```text
D^4 = H^4 = Theta^4 = 4! = 24.
```

Markman constructs a **simple coherent sheaf** `F` with

```text
ch(F) = N beta',
beta' = D - (q/6) H^3,
```

where `q` and `N` are positive integers.

Because `X` is abelian,

```text
td(X)=1,
K_X = O_X.
```

## 3. HC-R021-L004 — ordinary-semiregularity dimension obstruction

For the above `F`, set

```text
I := integral_X D H^3.
```

Then

```text
chi(F,F) = (N^2 q/3) I,
```

and

```text
dim Ext^2(F,F) >= (N^2 q/3) I - 2 >= 8 q N^2 - 2.
```

Consequently, if

```text
q N^2 >= 4,
```

then `F` cannot be ordinarily semiregular.

### Proof

Duality changes the sign of the odd Chern-character components. Since `beta'` has only degree-two and degree-six terms,

```text
ch(F^vee) = N[-D + (q/6)H^3].
```

Riemann-Roch on the abelian fourfold gives

```text
chi(F,F)
 = integral_X ch(F^vee) ch(F)
 = (N^2 q/3) integral_X D H^3.
```

The sheaf is simple, so

```text
ext^0(F,F)=1.
```

Serre duality and `K_X=O_X` give

```text
ext^4(F,F)=1,
ext^3(F,F)=ext^1(F,F).
```

Hence

```text
chi(F,F)=2-2 ext^1(F,F)+ext^2(F,F),
```

so

```text
ext^2(F,F)=chi(F,F)+2 ext^1(F,F)-2
           >= chi(F,F)-2.
```

The Khovanskii-Teissier inequality for the ample classes `D,H` gives

```text
(D H^3)^4 >= D^4 (H^4)^3 = 24^4,
```

thus

```text
I >= 24.
```

Therefore

```text
ext^2(F,F) >= 8 q N^2 - 2.
```

For an abelian fourfold, the target of the degree-two semiregularity map has dimension

```text
sum_{p=0}^2 h^{p,p+2}
 = C(4,0)C(4,2) + C(4,1)C(4,3) + C(4,2)C(4,4)
 = 6 + 16 + 6
 = 28.
```

Ordinary semiregularity would require an injection

```text
Ext^2(F,F) -> H^2(O_X) direct_sum H^3(Omega_X^1) direct_sum H^4(Omega_X^2),
```

so `ext^2(F,F)<=28`. If `qN^2>=4`, however,

```text
ext^2(F,F) >= 30,
```

which is impossible.

QED.

### Interpretation

This does not show that the target route fails. It shows why demanding full semiregularity of the explicit second factor is generally the wrong problem. Markman's Question 11.2.2 deliberately asks for injectivity only on the ambient-obstruction image.

The dimension test leaves the tiny cases `qN^2<=3` undecided.

## 4. HC-R021-L005 — restricted semiregularity is a kernel equality

Let `E` be a coherent/perfect object on a smooth projective variety in the Buchweitz-Flenner/HKR setting. Write

```text
ob_E : HT^2(X) -> Ext^2(E,E)
```

for the ambient Atiyah/evaluation obstruction map and

```text
c_E : HT^2(X) -> H_Omega^{-2}(X)
```

for contraction with `ch(E)`.

The semiregularity compatibility diagram gives

```text
c_E = sigma_E o ob_E.
```

Therefore

```text
sigma_E restricted to Im(ob_E) is injective
```

if and only if

```text
ker(ob_E) = ker(c_E).
```

### Proof

Compatibility immediately gives

```text
ker(ob_E) subset ker(c_E).
```

If `sigma_E` is injective on `Im(ob_E)` and `c_E(x)=0`, then

```text
sigma_E(ob_E(x))=0,
```

so `ob_E(x)=0`; hence the two kernels are equal.

Conversely, if the kernels are equal and `y=ob_E(x)` satisfies `sigma_E(y)=0`, then `c_E(x)=0`, so `x in ker(c_E)=ker(ob_E)` and `y=0`.

QED.

This is the content of the mechanism behind Markman arXiv:2502.03415, Lemma 8.3.4 and Remark 8.3.5, specialized to the non-surjective case.

## 5. Application to Markman's Question 11.2.2

Markman arXiv:2509.23079, Question 11.2.2 asks for a second secant sheaf `F_2` for which

```text
sigma_F2 | Im(at_F2)
```

is injective. For the explicit Example 11.2.7 sheaf `F` this is, by `HC-R021-L005`, exactly the statement

```text
ker(ob_F) = ann(ch(F)) intersect HT^2(X).
```

Because

```text
ch(F)=N beta'
```

with `N != 0`, scaling does not change the contraction kernel. Thus the right-hand side depends only on the explicit cohomology class

```text
beta' = g^*Theta - (q/6)(g^{-1})^*(Theta^3).
```

The source question has therefore been reduced to comparing:

1. the geometric deformation kernel of the explicit glued sheaf `F`;
2. the explicitly computable annihilator of `beta'` under the `HT^2` action.

Equivalently, since the first kernel is already contained in the second by the compatibility theorem, it suffices to prove equality of their dimensions or equality of the ranks of

```text
ob_F
```

and

```text
(•) contraction beta'.
```

## 6. Relation to the Perry route

`HC-R021-L005` is a sharper **first-order/restricted-obstruction** target than full semiregularity. It is not yet a replacement for `HC-R021-P4-G3`.

Perry's all-orders smoothness proof uses injectivity of the semiregularity map on the complete obstruction group of the relevant invariant-category object at each small extension. To replace weak `G`-semiregularity by `L005`, one must additionally prove that every successive obstruction arising in the desired family remains in the controlled ambient-obstruction image.

Accordingly there are now two non-exclusive closure routes:

```text
Route G:
  useful finite symmetry
    -> weak G-semiregularity
    -> Perry Theorem 1.2
    -> all-orders algebraicity transport

Route A:
  ker(ob_F)=ann(ch(F)) in HT^2
    -> restricted semiregularity on Im(ob_F)
    -> prove all successive family obstructions remain in that image
    -> all-orders algebraicity transport
```

Route G currently has a ready all-orders theorem but an open equivariant-semiregularity calculation. Route A has a smaller linear first-order target but an additional all-orders obstruction-image-stability theorem to prove.

## 7. Immediate next calculation

The highest-value next calculation is now exact:

```text
compute rank[(•) contraction beta' : HT^2(X) -> H_Omega^{-2}(X)],
```

then compute or bound `rank(ob_F)` for the glued Example 11.2.7 sheaf.

A strict rank deficit

```text
rank(ob_F) < rank((•) contraction beta')
```

would refute Markman's proposed second factor immediately. Equality, together with the known kernel inclusion, would prove the restricted semiregularity condition asked in Question 11.2.2.

## 8. Claim boundary

```text
HC-R021-L004 = proved_in_solve_package_not_certified
HC-R021-L005 = proved_in_solve_package_not_certified
ordinary_semiregularity_of_F_for_qN2_ge_4 = refuted_by_dimension
Markman_Question_11_2_2_for_explicit_F = open
all_orders_transport = open
HC-R021-P4 = open
HC-R021-A8-CM4-C2 = unproved
full_hodge_conjecture = unproved
```

No claim is made that the explicit glued sheaf satisfies the kernel equality. The package converts that question into a finite exact rank/kernel problem and proves that full ordinary semiregularity is generally too strong.