# FIGURATE WP09-026 — complete linear-gcd criterion for the primitive Pell ray

**Research scope:** For the recurring anchor $(k,c,a,b,r)=(16m+4,2,1,k-2,2)$, the WP09-025 primitive Pell norm-representative criterion has an **exact algebraic solution of its entire modular unit-orbit problem**. No orbit enumeration is needed. This is a uniform theorem for all integers $m\ge0$, not a universal claim that an anchor exists for each $m$. Parent: [FIGURATE WP09 #3145](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145). External priority and independent MATHCERT certification remain unasserted.

## Setup

Let $A=8m+1$ (odd), $q=2A$, $H=8m(m+1)+1$. The protected WP09-025 equivalence reduces exact anchor existence to a positive integer solution of

$$
x^2-qy^2=-2(2A-1)H,\qquad 2x\equiv2y\equiv1\pmod A.
$$

Write $r=2^{-1}\pmod A$, represented by $(A+1)/2$. Let $\varepsilon=U+V\sqrt q>1$ be the fundamental positive integral norm-one unit, so $U^2-qV^2=1$. Fix any positive integral representative $(x_0,y_0)$ of the primitive norm equation. Put $g=\gcd(V,A)$.

## Theorem A — closed-form necessary and sufficient ray criterion

**The entire forward unit orbit of $(x_0,y_0)$ contains the required residue pair $(r,r)\pmod A$ if and only if at least one of the following TWO branches holds:**

**Even-power branch**

$$
x_0\equiv r\pmod A,\qquad y_0\equiv r\pmod g.
$$

**Odd-power branch**

$$
x_0\equiv Ur\pmod A,\qquad y_0\equiv Ur\pmod g.
$$

The tests are complete, necessary and sufficient for the *whole infinite orbit*. They need only gcd computations and integer congruences. A successful branch supplies a constructive nonnegative power of the Pell unit. Failure of both branches **for all complete norm representatives** proves unbounded nonexistence for this specified anchor first pair, not merely a negative finite search. A failure of a computational resource guard is not such a proof.

## Proof — the even/odd Pell matrix degenerates to linear shears

On coefficient vectors $(x,y)$, unit multiplication is the integral matrix

$$
T=\begin{pmatrix}U&qV\\ V&U\end{pmatrix},\qquad\det T=1.
$$

Since $q=2A$, modulo the odd integer $A$ we have $qV\equiv0$ and $U^2\equiv1$. Therefore

$$
T\equiv
\begin{pmatrix}U&0\\ V&U\end{pmatrix}\pmod A,
$$

and by direct multiplication, **for every integer $j\ge0$**,

$$
T^{2j}\equiv\begin{pmatrix}1&0\\2jUV&1\end{pmatrix}\pmod A,
$$

$$
T^{2j+1}\equiv
\begin{pmatrix}U&0\\(2j+1)V&U\end{pmatrix}\pmod A.
$$

For an even exponent $2j$, the first coordinate is always $x_0\bmod A$. The second equals $y_0+2jUVx_0\bmod A$. It follows that the even orbit can hit $(r,r)$ only if $x_0\equiv r\pmod A$. Under this condition, $x_0$ is invertible modulo $A$ because $r$ is, and so are $2$ and $U$ (because $A$ is odd and $U^2\equiv1$). Hence

$$
\gcd(2UVx_0,A)=\gcd(V,A)=g.
$$

The linear congruence $2UVx_0j\equiv r-y_0\pmod A$ has an integer solution **if and only if** $g\mid(r-y_0)$, which is exactly the even-power criterion.

For an odd exponent $2j+1$, the first coordinate is $Ux_0$. Since $U^{-1}\equiv U\pmod A$, the first coordinate equals $r$ precisely when $x_0\equiv Ur\pmod A$. In that case $x_0$ is again invertible and the second coordinate condition is

$$
2Vx_0j\equiv r-(Uy_0+Vx_0)\pmod A.
$$

Its coefficient has gcd $g$ with $A$. Since $V\equiv0\pmod g$ and $U^2\equiv1\pmod g$, the gcd-solvability condition is equivalent to $y_0\equiv Ur\pmod g$. This proves the odd-power criterion and its sufficiency. QED.

## Theorem B — explicit unit exponent without orbit traversal

For either qualifying branch, let $c_0$ be its coefficient of $j$ and $d_0$ its right-hand side, as displayed in the proof. Set $g_0=\gcd(c_0,A)$ (equal to $g$ on a qualifying branch). The smallest nonnegative solution of $c_0j\equiv d_0\pmod A$ is

$$
j\equiv(d_0/g_0)\,(c_0/g_0)^{-1}\pmod{A/g_0},
$$

with the convention $j=0$ when $A/g_0=1$. Use exponent $2j$ for the even branch or $2j+1$ for the odd branch. The full Pell action modulo $A$ returns to the identity after $2A/g$ steps (possibly earlier), because $T^{2(A/g)}$ is the identity by the shear formula. Thus subsequent powers $n+2\ell A/g$ preserve the target residue and eventually give the required positive indices and a positive distinct third entry by WP09-025.

This computes **an exact constructive exponent**, not merely a Boolean outcome. Fast binary powering of the unit can apply that exponent, although the resulting integers may be enormous.

## Computational comparison and acceptance tests

The [exact linear-gcd implementation](https://github.com/grandchallenge/MATHSOLVE/blob/main/research/figurate_wp09_linear_ray_026.py) provides three independent forms of the same claim: (i) closed-form even/odd congruence conditions; (ii) a modular linear-congruence solver returning the least exponent; and (iii) direct fast modular exponentiation verifying the hit. The [regression suite](https://github.com/grandchallenge/MATHSOLVE/blob/main/tests/test_figurate_wp09_linear_ray_026.py) independently compares the theorem against the earlier **fully enumerated** primitive Pell ray for 30 parameter classes, multiple arbitrary representatives per class, and 20 direct power steps; checks linear congruence solutions against exhaustive modular oracles; and replays the complete anchor existence decisions and exact positive seeds at orders 4, 20, 36, 52, 68, 84, 100 and 308.

The previous WP09-025 orbit phase could require up to $A^2$ state inspections per representative. The new method uses at most **two gcd-solvability checks per representative**, with integer bit complexity determined by the sizes of $A,U,V,x_0,y_0$. This is not a polynomial-time bound for the entire anchor decision: the classical generalized-Pell representative enumeration and fundamental-unit computation remain potentially expensive. The resource-guard-fail behavior is unchanged.

## Mathematical originality and successor

The generalized Pell equation, unit orbits, and their finite representative classes are classical; see [Brian Conrad, Generalized Pell equation](https://virtualmath1.stanford.edu/~conrad/154Page/handouts/genpell.pdf). Here the new internal result is the **exact reduction of the polygonal-index residue action to a unipotent shear over the odd modulus $A$ and its consequent two-gcd criterion**. No external novelty or independent mathematical certification is asserted.

**The remaining substantive mathematical boundary is the primitive norm-representative existence problem as $A$ varies.** The ray orbit is now solved completely. To progress toward a family-wide existence/nonexistence classification, study principality and oriented ray conditions for the quadratic order of $\sqrt{2A}$, including non-squarefree $A$ and conductor effects. The small first-pair oracle does not classify all possible first pairs. Neither a universal local-to-global principle nor an unbounded obstruction for all locally compatible parameter families has been proved.
