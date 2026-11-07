# FIGURATE WP09-023 — a uniform finite Pell-lattice decision for fixed first pairs

**Research claim:** necessary-and-sufficient **decidability** of exact positive Type B seed existence **for any specified exact first pair with nonsquare product**. This is a bounded producer theorem, not a universal local-to-global existence theorem, a practical complexity bound, independent MATHCERT certification, or a literature-originality claim. Parent: [FIGURATE WP09 #3145](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145).

## 1. The constrained problem

Fix integers $k\ge3$, $c$, and **distinct positive** integers $a,b$ with $ab+c=P_k(r)$ at a positive integer $r$. Write

$$
R=2(k-2),\quad L=k-4,\quad Q=ab,\quad
\Delta=8(k-2)c+L^2,\quad N=a(a-b)\Delta.
$$

Assume that $Q$ is **not a perfect square**. The first-pair extension to positive distinct $d$ with positive indices $s,t$ is controlled by

$$
X^2-QS^2=N,\qquad S=Rs-L,\quad X=a(Rt-L).
$$

A norm-equation solution is insufficient unless it also lies in the **integral polygonal index lattice**, gives integral $d=(P_k(s)-c)/a$, and satisfies positivity and distinctness. This WP makes those constraints decidable by finite arithmetic.

## 2. Theorem — exact finite fixed-pair criterion

Let $\varepsilon=U+V\sqrt Q>1$ be the minimal positive integral norm-one unit, $U^2-QV^2=1$. Put $M=2aR$.

**Case $N=0$.** There are no solutions with $X,S>0$, since $X^2=QS^2$ contradicts nonsquare $Q$ for nonzero integers $X,S$. Hence no positive Type B extension exists for this fixed pair.

**Case $N\ne0$.** Set $B=\sqrt{|N|}$. Every positive integral norm solution $(X,S)$ lies on the forward orbit of a positive integral solution $(X_0,S_0)$ satisfying

$$
0<S_0,\quad 0<X_0,\qquad
B<X_0+\sqrt Q\,S_0\le\varepsilon B.
$$

Consequently it is sufficient to enumerate finitely many solutions of $X_0^2-QS_0^2=N$ in this region. For convenient entirely integer arithmetic, the committed implementation enumerates the slightly larger finite range $1\le S_0\le H$ where

$$
E=U+V(\lfloor\sqrt Q\rfloor+1),\qquad
B_+=\lfloor\sqrt{|N|}\rfloor+1,
$$

$$
H=1+\left\lfloor\frac{EB_+}{\sqrt Q}\right\rfloor.
$$

The last floor is computed exactly by integer square root of $\lfloor (EB_+)^2/Q\rfloor$. This upper bound is conservative, possibly extremely large, but is **complete**. A configured compute cap is only a guard: when $H$ exceeds it, the program raises an explicit error and **does not return a negative decision**.

For each enumerated positive norm representative, compute its residue orbit under

$$
\begin{pmatrix}X\\S\end{pmatrix}
\longmapsto
\begin{pmatrix}U&QV\\V&U\end{pmatrix}
\begin{pmatrix}X\\S\end{pmatrix}
\pmod M.
$$

The matrix has determinant one, so the orbit is **purely periodic** modulo $M$, with at most $M^2$ states. An orbit contains a permissible seed if and only if at least one residue pair satisfies all three tests:

1. $a\mid X$ and $(X/a+L)\equiv0\pmod R$;
2. $(S+L)\equiv0\pmod R$;
3. with integer $s=(S+L)/R$, the condition $P_k(s)\equiv c\pmod a$.

**Conclusion.** A fixed pair $(a,b)$ admits an exact positive distinct Type B extension **if and only if one of the finitely many enumerated norm representatives has a residue orbit meeting these tests**. When this happens, there are infinitely many extensions with the same first pair by forward Pell multiplication. When none meets them, there is **no** extension for that fixed pair, not merely none below a search bound.

## 3. Proof of the finite and sufficient reduction

For any positive norm solution define $\alpha=X+\sqrt Q\,S>0$ and $\beta=X-\sqrt Q\,S=N/\alpha$. With $B=\sqrt{|N|}$, positivity of both $X,S$ is equivalent to $\alpha>B$: for $N>0$, $\alpha>\sqrt N$ is precisely $S>0$; for $N<0$, it ensures $X>0$, while $S>0$ follows. Multiplication by $\varepsilon^{-1}$ preserves integral coordinates, the norm, and the positive real embedding. Starting with any $\alpha>B$, multiply backward by $\varepsilon^{-1}$ until $B<\alpha_0\le\varepsilon B$. This gives the claimed normalized representative, and all forward powers recover the original solution.

Since $X_0>0$, we have $S_0<\alpha_0/\sqrt Q\le\varepsilon B/\sqrt Q < EB_+/\sqrt Q$, establishing the explicit finite integer search bound $H$. Every representative is found by looping over $S_0$ and asking whether $QS_0^2+N$ is a positive integer square. The larger search range does not create false positives: each enumerated point itself solves the norm equation.

For the residue test, $X$ modulo $M$ decides $a\mid X$ and $(X/a+L)\equiv0\pmod R$, while $S$ modulo $M$ decides the integrality of $s=(S+L)/R$ and its value modulo $2a$. The identity

$$
P_k(n+2a)\equiv P_k(n)\pmod a
$$

holds for **every** integer $n$ because $P_k(n)=n+(k-2)n(n-1)/2$. Hence condition 3 depends only on $S\bmod M$. All conditions are therefore periodic along the Pell orbit.

If the norm orbit meets the residue lattice at index $j$, every future $j+\ell T$ with $T$ its finite residue period meets the same conditions. For large $\ell$, the positive unit growth sends $S$ and $X$ to infinity, so $s,t$ are positive and $d=(P_k(s)-c)/a$ is a positive integer distinct from $a,b$. The original norm identity and the exact first-pair equation then give $P_k(t)=bd+c$; all three Type B equations hold. This proves **sufficiency**, not merely necessity.

Conversely, any exact positive seed produces a positive norm solution, whose backward normalization lies in the enumerated finite region. The residue orbit contains the actual seed state, so the algorithm returns YES. If no candidate orbit meets the lattice, existence is impossible for this fixed pair. QED.

## 4. Arithmetic controls and scope

- **Positive:** $(k,c,a,b,r)=(84,2,1,82,2)$, $(100,2,1,98,2)$ and $(308,2,1,306,2)$. The algorithm returns YES; independent direct polygonal arithmetic checks the constructed exact seed. These pairs were established globally in earlier protected FIGURATE work.
- **Negative fixed pair:** $(68,2,1,66,2)$ returns NO after **complete norm representative enumeration**; the result is scoped to that first pair. WP09-012 already exhibits an odd-prime obstruction to the corresponding parameter family, so this is a regression control, not a novel global obstruction.
- **Adversarial:** square $Q$ is explicitly rejected; $N=0$ is handled; incomplete searches raise instead of silently reporting NO; and index-integrality checks are independently compared with polynomial arithmetic.

The decision procedure may be inefficient when $\varepsilon$ or $|N|$ is large. It **does not** decide the existence of a seed over **all possible first pairs** unless an additional theorem bounds or classifies those pairs. It does not assert that local compatibility at every modulus implies a global seed. The solver must not confuse a failed resource guard with a mathematical NO.

## 5. Research deliverables and next theorem obligations

Reproduction:

    python3 -m unittest -v tests.test_figurate_wp09_uniform_pell_lattice_023

The producer source is [research/figurate_wp09_uniform_pell_lattice_023.py](https://github.com/grandchallenge/MATHSOLVE/blob/main/research/figurate_wp09_uniform_pell_lattice_023.py), with [independent arithmetic regressions](https://github.com/grandchallenge/MATHSOLVE/blob/main/tests/test_figurate_wp09_uniform_pell_lattice_023.py).

The next structural obligation is **not another isolated enormous Pell seed**. It is to classify first-pair choices uniformly, especially $(a,b)=(1,k-2)$ at $c=2,r=2$, or prove a finite reduction across all admissible first pairs in a parameter subfamily. A second route is to classify which norm-representative classes can meet the index lattice using congruence and descent rather than exhaustive orbit traversal. Protected research integration is not mathematical certification; specialist MATHCERT review and external priority checking remain separate.
