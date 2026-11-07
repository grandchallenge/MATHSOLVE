# FIGURATE WP09-025 — primitive odd-modulus Pell criterion for the anchor family

**Research scope:** For every integer $m\ge0$, gives an **exact necessary-and-sufficient primitive Pell norm and odd-residue criterion** for a positive exact Type B seed with fixed first entries $(a,b)=(1,k-2)$, offset $c=2$, first polygonal index $r=2$, and order $k=16m+4$. It also provides a complete finite YES/NO decision on a much smaller representative and modular search domain. This does **not** establish that the resulting norm/residue criterion succeeds for every $m$, or that other first pairs are classified. Internal producer mathematics only; independent MATHCERT certification and external novelty remain separate.

Parent: [FIGURATE WP09 #3145](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145). Builds explicitly on the previously protected fixed-first-pair norm theorem WP09-013, complete fixed-pair decision WP09-023 and forced anchor index branches WP09-024. The general finite-orbit treatment of generalized Pell equations is classical; see [Brian Conrad, Generalized Pell equation](https://virtualmath1.stanford.edu/~conrad/154Page/handouts/genpell.pdf). The contribution here is the **specific polygonal-index lattice normalization and its exact consequences**, not discovery of Pell units.

## Theorem — exact primitive odd-ray equivalence

Fix $m\ge0$ and put

$$
A=8m+1,\qquad k=16m+4=2A+2,\qquad
q=k-2=2A,\qquad H=8m(m+1)+1.
$$

Every valid exact positive Type B extension of $(1,q)$ at offset two and first index two is equivalent, by the formulas below, to an integer solution of the following **primitive constrained Pell norm**:

$$
x^2-2Ay^2=-2(2A-1)H,
$$

$$
2x\equiv2y\equiv1\pmod A.
$$

Precisely: any positive distinct exact Type B extension $(1,q,d)$ with positive indices $(2,s,t)$ produces **strictly positive integers**

$$
x=At-\frac{A-1}{2},\qquad
y=As-\frac{A-1}{2},
$$

satisfying both conditions. Conversely, **any strictly positive integer norm solution $(x,y)$ meeting those two congruences produces an infinite Pell orbit containing exact positive distinct Type B extensions**, with first entries $(1,q)$, offset two and first index two. The inverse formulas are

$$
t=\frac{x+(A-1)/2}{A},\qquad
s=\frac{y+(A-1)/2}{A},\qquad
d=P_k(s)-2.
$$

For sufficiently far-forward Pell multiples these are positive integers, $d$ is positive and distinct from both 1 and $q$, and all three polygonal equations hold. (At a small initial solution, nonpositivity or a collision is possible, so the forward-unit step is essential.)

Thus this is a complete **if-and-only-if seed-existence criterion for the entire recurring anchor family**, with $m$ as a free parameter. It is not a classification of which values of $m$ satisfy the primitive norm/residue criterion.

## Proof — exact normalization, not a heuristic filter

The WP09-013 general fixed-first-pair equation has $R=2(k-2)=4A$, $L=k-4=2(A-1)$, and

$$
\Delta=8(k-2)c+L^2=32H,\qquad
N=a(a-b)\Delta=-(2A-1)32H.
$$

For $a=1$, its coordinates are $X=Rt-L$ and $S=Rs-L$, satisfying

$$
X^2-2AS^2=-32(2A-1)H.
$$

Because $A=8m+1$, $L=2(A-1)$ is divisible by 16 and $R=4A$ is divisible by four. Thus **every actual exact seed has $4\mid X$ and $4\mid S$**. Define $x=X/4$ and $y=S/4$. Dividing the norm identity by 16 proves the primitive norm equation. The lattice conditions $X\equiv S\equiv-L\pmod R$ reduce exactly to

$$
x\equiv y\equiv-\frac{A-1}{2}
             \equiv\frac{A+1}{2}\pmod A,
$$

which is equivalent to $2x\equiv2y\equiv1\pmod A$ because $A$ is odd. This proves necessity and the forward formulas.

Conversely, given a positive primitive norm solution in the prescribed residue class, set $X=4x$ and $S=4y$. The congruences imply positive integral $s,t$ via the inverse formulas whenever the coordinates are sufficiently large. The scaled norm identity yields

$$
P_k(t)-2=q(P_k(s)-2).
$$

This follows directly by expanding the completed-square identity; it is **not** an inference from local congruences. Then defining $d=P_k(s)-2$ gives both remaining exact polygonal pair equations automatically. The first pair is exact because $P_k(2)=k=q+2$.

Finally, $q=16m+2$ is **nonsquare** (its residue modulo sixteen is two). Let $\varepsilon=U+V\sqrt q>1$ be the fundamental positive integral norm-one unit. Its multiplication matrix is integral and has determinant one, so the induced action modulo the **odd** integer $A$ is invertible and has a finite period $T$. Replacing $(x,y)$ by $\varepsilon^{jT}(x+y\sqrt q)$ leaves the primitive norm, strict positivity, and both modulo-$A$ residue conditions unchanged, and sends both coordinates to infinity. Hence eventually $s,t,d$ are positive, $d\notin\{1,q\}$ and all three pair equations are exactly satisfied. Infinitely many different $d$ result. This proves sufficiency and the infinite amplification claim. QED.

## Finite complete decision and complexity distinction

WP09-023 already shows how to enumerate a complete finite set of positive generalized-Pell representatives in a fundamental unit region and then inspect a complete finite modular unit orbit. Here apply that theorem **to the smaller norm**

$$
N_{\mathrm{primitive}}=-2(2A-1)H
$$

instead of the original norm $16N_{\mathrm{primitive}}$, and check just the single residue target $(2^{-1},2^{-1})\pmod A$.

The resulting orbit has **at most $A^2$ modular states**, compared with at most $(4A)^2=16A^2$ states under the WP09-024 anchor modulus $R=4A$, or $(8A)^2=64A^2$ under WP09-023's original anchor modulus $2R$. The normalized representative bound is also reduced because the norm absolute value is divided by 16. This is a worst-case state-size reduction, not a claim that all units or discriminants admit fast decisions.

The [exact normalized implementation](https://github.com/grandchallenge/MATHSOLVE/blob/main/research/figurate_wp09_odd_ray_lattice_025.py) uses the earlier protected complete representative algorithm, enumerates each primitive Pell orbit modulo $A$ and constructs an actual exact seed when an orbit meets the prescribed class. It refuses to report NO if an explicitly configured complete representative bound is exceeded. The [independent regression tests](https://github.com/grandchallenge/MATHSOLVE/blob/main/tests/test_figurate_wp09_odd_ray_lattice_025.py) verify the normalization for 55 order classes, the residue-class equivalence for 35 classes, **exact YES/NO equivalence with the prior complete decider** for orders $20,36,52,68,84,100,308$, and positive exact seed construction. They also independently check the known order-308 seed and the negative *fixed-anchor* control at order 68. Neither a negative fixed-anchor result nor a computational guard proves global parameter nonexistence across all possible first pairs.

## What is fulfilled and what remains genuinely open

**Fulfilled:** A rigorous, universally parameterized exact equivalence between the anchor Type B existence problem and one normalized norm equation with a single odd-modulus target residue class. A complete finite decision for each specified $m$ is implemented and tested. A positive answer implies infinitely many genuine exact triples, not just norm solutions. The nontrivial four-coordinate/16-norm simplification is proved, and the full modular-orbit state cap is reduced by a factor of sixteen relative to WP09-024.

**Unresolved:** A closed classification of those $m$ for which this primitive equation and odd residue condition are solvable; a family-wide obstruction or sufficient theorem not requiring instance-by-instance Pell orbit enumeration; a theorem showing that a different first pair always works when the recurring anchor fails; and universal local-to-global existence or nonexistence. These are **mathematical evidence boundaries**, not platform or execution blockers. The next substantive research tool should examine the principal ideal/ray-class conditions for the quadratic order of $\sqrt{2A}$, carefully handling non-squarefree $A$ and the conductor. Do not mistake ideal-principality over the maximal order for integrality in a nonmaximal order.

External comparison: the general finiteness of generalized Pell solution classes, and continued-fraction algorithms for them, are classical and must not be claimed as original GCL discoveries. The new polygonal normalization is an internal contribution, with external originality still unassessed.
