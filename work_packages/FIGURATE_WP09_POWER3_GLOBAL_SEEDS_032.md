# FIGURATE WP09-032 — a uniform 3-power square-conductor global Type B family

**Parent:** [FIGURATE WP09 #3145](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145). **Dependencies:** protected WP09-025 (primitive anchor norm/ray equivalence), WP09-027 (actual-order oriented ray formulation), and WP09-029–031 (conductor arithmetic). **New bounded mathematical claim:** for **every integer e >= 1**, the odd square-conductor case **f=3^e** has a prescribed norm ideal in its *correct oriented ray class*. Therefore the exact positive Type B anchor admits **infinitely many distinct extensions at every polygonal order k=2*9^e+2**, with offset c=2 and the fixed first pair (1, 2*9^e). This is a parameter-uniform existence theorem, not a universal Type B classification, external novelty claim or independently certified result.

## 1. Statement and scope

Write

$$
f=3^e,\quad A=f^2=9^e,\quad
m=(A-1)/8,\quad
k=16m+4=2A+2,\quad H=(A^2+6A+1)/8.
$$

For all e >= 1 there are infinitely many **distinct positive integers d**, with d different from 1 and 2A, and positive integer indices s,t such that

$$
P_k(2)=2A+2,\qquad
P_k(s)=d+2,\qquad
P_k(t)=2Ad+2.
$$

Equivalently, (1, 2A, d) is an exact Type B triple of order k and offset 2. Every such claim includes *all three* positive polygonal indices and the distinctness of entries; it is not an inference from congruences alone.

More strongly, setting D=2A, N=-2(2A-1)H, O_f=Z[f sqrt(2)], and I=A O_f=f^2 Z + f^3 Z sqrt(2), the ideal norm fibre at |N| contains an integral invertible ideal in the **oriented ray class** of (rho), where

$$
r=(A+1)/2,\qquad
\rho=r(1+f\sqrt2)\in O_f.
$$

This is a positive infinite-family answer to the target-class *realization* problem identified after WP09-031. It does not assert that the other ideals of the same norm occupy that class, nor that arbitrary f or arbitrary squarefree part have such a representative.

## 2. Explicit norm representative

Let u=3+2 sqrt(2), the positive norm-one unit of Z[sqrt(2)]. Define

$$
\alpha=\frac{(1+f\sqrt2)(f^2+u)}2
 =\frac{f^2+4f+3}{2}
  +\frac{f^3+3f+2}{2}\sqrt2.
$$

Both coefficients are integers because f is odd, and both are strictly positive. The norm calculation is exact:

$$
N_{K/\mathbf Q}(f^2+u)
 =(f^2+3)^2-8=f^4+6f^2+1=8H,
$$

$$
N_{K/\mathbf Q}(\alpha)
 =\frac{(1-2f^2)(8H)}4
 =-2(2A-1)H=N<0.
$$

The element alpha belongs to the **maximal** order Z[sqrt(2)], but its sqrt(2)-coefficient need not be divisible by f, so this norm identity alone is NOT a valid solution in O_f. The remainder of the proof corrects the coefficientwise ray by a positive unit.

## 3. Elementary 3-adic lifting lemma

Put L=4*3^(2e-1) and T=fL=4*3^(3e-1). Then

$$
u^L\equiv1+f^2 b_e\sqrt2\pmod{f^3\mathbf Z[\sqrt2]},
\qquad 3\nmid b_e,
$$

and u^T is 1 modulo f^3 in both coefficients.

**Proof.** First,

$$
u^4=577+408\sqrt2,\qquad
v_3(408)=1,\qquad 577\equiv1\pmod3.
$$

Suppose z=a+b sqrt(2) is a norm-one unit with a=1 mod 3 and v_3(b)=n>=1. The imaginary coefficient of z^3 is b(3a^2+2b^2). Since v_3(3a^2+2b^2)=1, cubing raises v_3(b) by **exactly one**. Also z^3 still has scalar coefficient congruent to 1 mod 3. Inductively, the sqrt(2)-coefficient of u^(4*3^j) has valuation j+1.

Apply this with j=2e-1: its sqrt(2)-coefficient is f^2 b_e, with b_e invertible modulo f. If u^L=a+b sqrt(2), its norm-one identity implies

$$
(a-1)(a+1)=2b^2.
$$

As a is 1 modulo 3, a+1 is a 3-adic unit. Hence v_3(a-1)=2v_3(b)=4e, so a is 1 modulo f^3. This proves the displayed congruence. Taking j=3e-1 similarly gives u^T=1 modulo f^3. QED.

Because (f^2 sqrt(2))^2 is divisible by f^3, powers of the first congruence satisfy

$$
u^{Lj}\equiv1+jf^2b_e\sqrt2\pmod{f^3}.
$$

Choose the **unique** j in {0,...,f-1} solving

$$
j b_e\equiv-2\pmod f.
$$

The inverse exists because 3 does not divide b_e. This is explicit, finite modular arithmetic for **every** e>=1, not an unproved Pell-orbit search.

## 4. The exact conductor-sensitive ray hit

Work modulo f^3 Z[sqrt(2)], where rho is invertible since its norm is coprime to f. Cancellation of (1+f sqrt(2)) yields

$$
\alpha/\rho=(f^2+u)/(1+f^2).
$$

The denominator 1+f^2 is invertible modulo f^3, and elementary multiplication (discarding only multiples of f^3) gives

$$
\frac{f^2+u}{1+f^2}
\equiv u(1+2f^2)(1-2f^2\sqrt2)
\equiv u(1+2f^2)u^{Lj}
\pmod{f^3}.
$$

The scalar h=1+2f^2 lies in the *actual-order ray scalar subgroup*
{1+f^2 j (mod f^3) : j mod f} of WP09-031. Let

$$
E=T-1-Lj\quad (0\le E<T),\qquad
\beta=\alpha u^E.
$$

Since u^T=1 modulo f^3, the preceding identities imply

$$
\beta\equiv\rho(1+2f^2)\pmod{f^3\mathbf Z[\sqrt2]}.
$$

The scalar coefficient of rho*(2f^2) is divisible by f^2 and its sqrt(2)-coefficient is 2 f^3 r, divisible by f^3. Thus, **in the actual order**,

$$
\boxed{\beta\in O_f,\qquad \beta\equiv\rho\pmod{f^2 O_f}.}
$$

This is the step not implied by maximal-order principality. Norm beta=N, and the first real embedding of beta is positive (both alpha and u are positive there), while the conjugate is negative because N<0. Hence its integral ideal (beta) has norm |N|, is invertible (the norm is coprime to f), and occupies the oriented ray class of (rho). Indeed beta/rho has positive real signs and is 1 in the localized ray quotient.

This proves the target-class realization theorem without class-group enumeration, generalized-Pell representative searches or case-by-case factorization.

## 5. Recovering infinitely many exact positive Type B triples

Write beta=x+y sqrt(D)=x+fy sqrt(2) with x,y integers. The preceding congruence says

$$
x\equiv y\equiv r=(A+1)/2\pmod A,\qquad
x^2-Dy^2=N.
$$

The coefficients x,y are positive: alpha and u^E have positive coefficients in Z[sqrt(2)], E>=0, and beta's radical coefficient is divisible by f>0.

WP09-025 gives the *exact* inverse polygonal-index formulas

$$
s=\frac{y+(A-1)/2}{A},\quad
t=\frac{x+(A-1)/2}{A},\quad
d=P_k(s)-2,\quad
P_k(n)=A n(n-1)+n.
$$

The ray congruences ensure s,t are integers. If the initial beta were too small for positivity or distinctness, multiply it by u^(qT), q>=0: this preserves norm and the **same coefficientwise ray**, keeps both coefficients positive, and sends both indices to infinity. For every sufficiently large q the resulting d is positive and different from 1 and 2A. The exact norm identity, not a local argument, proves P_k(t)=2A*d+2. Since the indices grow, distinct q yield distinct d. This proves infinitely many positive triples for **every** e>=1. QED.

## 6. Exact algorithm, independent replay and boundaries

The [integer-exact certificate source](https://github.com/grandchallenge/MATHSOLVE/blob/main/research/figurate_wp09_power3_global_seeds_032.py) computes b_e modulo f, the modular inverse j and the constructive E using logarithmic modular unit powering. It verifies the norm and full conductor ray. For small witnesses it can build beta and check the three polygonal identities; a witness-size guard raises explicitly rather than returning false nonexistence. The proof works for unbounded e even when a literal witness would have an enormous number of digits.

The [independent regressions](https://github.com/grandchallenge/MATHSOLVE/blob/main/tests/test_figurate_wp09_power3_global_seeds_032.py) recompute modular unit powers with an independent 2x2 matrix oracle, verify unit valuations/periods, verify the explicit norm identity independently, and invert the three polygonal outputs with a discriminant and integer square root oracle. Positive-index constructed triples are replayed at e=1,2, with exact modular checks for further exponents. Baseline data:

| e | f | k | Constructive E | Unit period T | Status |
|---:|---:|---:|---:|---:|:---|
| 1 | 3 | 20 | 23 | 36 | Explicit positive seed |
| 2 | 9 | 164 | 863 | 972 | Explicit positive seed |
| 3 | 27 | 1460 | 25,271 | 26,244 | Exact norm/ray certificate |
| 4 | 81 | 13,124 | 463,643 | 708,588 | Exact norm/ray certificate |
| 5 | 243 | 118,100 | 4,172,795 | 19,131,876 | Exact norm/ray certificate |

These exponents are **not** claimed minimal; e=1 recovers an existing positive family by a different, deliberately explicit generator. No claim is made that all odd f, all m, or all Type B first pairs are now classified. This is an **infinite successful subfamily** of the previously unresolved target-class realization problem, not a proof of universal local-to-global equivalence. Independent MATHCERT certification, proof-level literature comparison and priority assessment remain separate. Protected CI, direct test replay and merge/readback are execution evidence that must be reported only after observed.

**Next mathematical obligation:** seek analogous uniform realizations or a true global obstruction for other prime-power and mixed conductors, and then analyze general A=f^2 a_0 with nontrivial maximal-order narrow class group. Keep the FIGURATE programme and WP09 parent open.
