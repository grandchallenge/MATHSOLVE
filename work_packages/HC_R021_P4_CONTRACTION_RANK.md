# HC-R021-P4 — Exact contraction rank for the genus-four CM secant class

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent diagnostic:** `work_packages/HC_R021_P4_SEMIREGULARITY_DIAGNOSTICS.md`  
**State:** `CONTRACTION_RANK_EXACT__ATIYAH_RANK_OPEN`  
**Date:** 2026-09-16

## 1. Result

For the explicit class in Markman Example 11.2.7

```text
beta' = g^*Theta - (q/6)(g^{-1})^*(Theta^3),
```

with `Nm(f)=1`, `f^2 != 1`, and `hat_eta(f)=g^*`, the Hochschild/HKR contraction map

```text
c_beta' : HT^2(X) -> H_Omega^{-2}(X),
           xi |-> xi contraction beta'
```

has

```text
rank(c_beta') = 20,
dim ker(c_beta') = 8.
```

Consequently, for Markman's explicit glued coherent sheaf `F` with

```text
ch(F)=N beta',  N != 0,
```

the restricted semiregularity condition of Question 11.2.2 holds if and only if

```text
rank(ob_F)=20.
```

The remaining first-order question is therefore an exact rank computation for the Atiyah/ambient obstruction map; the cohomological side is completely determined.

## 2. Real-multiplication normal form

Markman writes

```text
Theta = Theta_sigma1 + Theta_sigma2
```

for the two real embeddings of the quadratic field `F`. The corresponding summands of `H^1(X,C)` have complex dimension two on `H^(1,0)`.

Let

```text
lambda = sigma1(f).
```

Since `Nm(f)=1`,

```text
sigma2(f)=lambda^(-1).
```

Markman proves

```text
g^*Theta = f^2 · Theta.
```

Thus, on the two real-multiplication blocks, the degree-two forms

```text
D := g^*Theta,
H := (g^(-1))^*Theta
```

have relative weights

```text
D : lambda^2, lambda^(-2),
H : lambda^(-2), lambda^2.
```

After a change of Hodge basis normalizing `D`, the pair takes the form

```text
D = sum_(i=1)^4 x_i y_i,
H = a(x_1 y_1 + x_2 y_2) + b(x_3 y_3 + x_4 y_4),
```

where

```text
a = lambda^(-4),
b = lambda^4.
```

Here the `x_i` are a basis of holomorphic one-forms and the `y_i` the corresponding `H^1(O_X)` basis.

Because `f^2 != 1` and `f` is real quadratic of norm one,

```text
a != b,
a b != 0.
```

Set

```text
c := -q/6 != 0.
```

Then

```text
beta' = D + c H^3.
```

The scalar normalization does not affect the rank calculation.

## 3. HKR source and semiregularity target

For an abelian fourfold,

```text
HT^2(X)
 = H^2(O_X)
   direct_sum H^1(T_X)
   direct_sum H^0(Lambda^2 T_X)
```

has dimensions

```text
6 + 16 + 6 = 28.
```

The degree-two semiregularity target is

```text
H_Omega^{-2}(X)
 = H^2(O_X)
   direct_sum H^3(Omega_X^1)
   direct_sum H^4(Omega_X^2)
```

with dimensions

```text
6 + 16 + 6 = 28.
```

Since `beta'` has only degree-two and degree-six components, contraction splits into two independent blocks:

```text
C_AC : H^2(O_X) direct_sum H^0(Lambda^2 T_X)
       -> H^3(Omega_X^1),

C_B  : H^1(T_X)
       -> H^2(O_X) direct_sum H^4(Omega_X^2).
```

There are no other degree-compatible components.

## 4. HC-R021-L006 — exact rank 20

### Statement

In the real-multiplication normal form above,

```text
rank(C_AC)=10,
rank(C_B)=10.
```

Hence

```text
rank(c_beta')=20,
dim ker(c_beta')=8.
```

### Proof

Use lexicographic exterior bases associated to `x_1,...,x_4` and `y_1,...,y_4`.

For `C_B`, a direct contraction calculation exhibits the following six linearly independent kernel vectors in `H^1(T_X)`:

```text
y_1 tensor t_1,
y_2 tensor t_2,
y_1 tensor t_2 + y_2 tensor t_1,
y_3 tensor t_3,
y_4 tensor t_4,
y_3 tensor t_4 + y_4 tensor t_3,
```

where `t_i` is dual to `x_i`. Therefore

```text
rank(C_B) <= 16-6 = 10.
```

On the complementary ten source basis vectors obtained by omitting the six vectors above, and on ten corresponding target basis vectors, the determinant of the contraction matrix is

```text
-1296 a^4 b^4 c^4 (a-b)^4.
```

This is nonzero because `a,b,c` are nonzero and `a!=b`. Hence

```text
rank(C_B) >= 10,
```

and therefore `rank(C_B)=10`.

For `C_AC`, two linearly independent kernel vectors are supported on the two real-multiplication blocks. Up to nonzero scalar multiples they have the form

```text
(-6 c a^2 b) y_1 wedge y_2 + t_1 wedge t_2,
(-6 c a b^2) y_3 wedge y_4 + t_3 wedge t_4.
```

Thus

```text
rank(C_AC) <= 12-2 = 10.
```

Again, in lexicographic exterior bases a ten-by-ten minor has determinant

```text
+1296 a^4 b^4 c^4 (a-b)^4,
```

which is nonzero. Hence

```text
rank(C_AC)=10.
```

The two target summands of `C_AC` and `C_B` are disjoint, so their ranks add:

```text
rank(c_beta') = 10+10 = 20.
```

Since both source and target have dimension 28,

```text
dim ker(c_beta')=8.
```

QED.

## 5. Structure of the eight-dimensional annihilator

The calculation also identifies the kernel qualitatively.

Six dimensions lie in the `H^1(T_X)` summand. They are the symmetric endomorphism directions internal to the two two-dimensional real-multiplication blocks:

```text
Sym^2(block_sigma1) direct_sum Sym^2(block_sigma2),
```

of dimensions `3+3`.

The remaining two dimensions mix

```text
H^2(O_X)
```

with

```text
H^0(Lambda^2 T_X)
```

inside each of the two real-multiplication blocks, with the scalar ratios displayed in the proof.

Thus the annihilator is not accidental numerical degeneracy; its dimension-eight structure is forced by the quadratic real-multiplication splitting.

## 6. Consequence for Markman's Question 11.2.2

By `HC-R021-L005`, Markman's restricted semiregularity condition for the explicit sheaf `F` is equivalent to

```text
ker(ob_F)=ker(c_beta').
```

The semiregularity compatibility theorem already gives

```text
ker(ob_F) subset ker(c_beta').
```

Therefore

```text
rank(ob_F) >= rank(c_beta') = 20.
```

Equality of kernels is now equivalent to either of the exact numerical statements

```text
dim ker(ob_F)=8
```

or

```text
rank(ob_F)=20.
```

A rank strictly greater than `20` would mean `ker(ob_F)` is a proper subspace of the eight-dimensional cohomological annihilator and would refute the restricted semiregularity condition for this explicit sheaf.

This corrects the direction of the useful falsification test: because `ker(ob_F) subset ker(c_beta')`, one cannot have `rank(ob_F)<20`. The candidate succeeds precisely at the **minimal possible** obstruction-map rank `20`; any larger rank fails the kernel-equality criterion.

## 7. Next exact task

The remaining first-order problem is no longer a pair of unknown ranks. It is:

```text
compute rank(ob_F) for the glued sheaf of Example 11.2.7,
```

knowing a priori that

```text
20 <= rank(ob_F) <= 28.
```

High-value approaches are now:

1. identify eight explicit ambient deformation directions in `ker(ob_F)`; this proves `rank(ob_F)=20` immediately;
2. compute the deformation functor of the gluing construction and show that all eight annihilator directions preserve the glued object to first order;
3. exhibit even one annihilator direction with nonzero `ob_F`; this refutes the explicit sheaf for Question 11.2.2.

The first route is the shortest positive route.

## 8. Claim boundary

```text
HC-R021-L006 = proved_in_solve_package_not_certified
rank_contraction_beta_prime = 20
annihilator_dimension_beta_prime = 8
rank_ob_F = open_in_[20,28]
Markman_Question_11_2_2_for_explicit_F = open
all_orders_transport = open
HC-R021-P4 = open
HC-R021-A8-CM4-C2 = unproved
full_hodge_conjecture = unproved
```

This result computes only the cohomological contraction side. It does not assert that the glued sheaf deforms in all eight annihilator directions, and it does not certify semiregularity or algebraicity transport.