# FIGURATE WP08 — exact 2-adic offset density and fixed coherent triple witnesses

**Programme:** [FIGURATE #3093](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3093); [WP08 #3125](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3125). **Tranche 008, 5 November 2026.** Exact elementary mathematics with reproducible tests. **No new mathematical-literature originality, independent specialist certification, or existence of global integer Type B triples claimed.**

## Two connected structural results

Let $k\ge4$ be an integer polygonal order divisible by four, with

$$
A=\frac{k}{2}-1\quad(\text{odd}),\qquad q=\frac{k}{4}-1,
\qquad D=A c+q^2
$$

for any integer offset $c$. The earlier exact normal form is $A P_k(t)+q^2=(At-q)^2$.

**Theorem A (exact offset density, every binary precision).** The number $N_k(n)$ of possible polygonal output residues modulo $2^n$ is independent of $k$ and given by

$$
N_k(n)=
\begin{cases}
(2^n+8)/6,& n\ge2\text{ even},\\
(2^n+10)/6,& n\ge1\text{ odd}.
\end{cases}
$$

Consequently $N_k(n)/2^n\to1/6$. The offsets $c\in\mathbb Z$ for which $D=A c+q^2$ is a square in the 2-adic integers $\mathbb Z_2$ also have (two-sided) natural density **$1/6$**, for every $k$ divisible by four.

**Theorem B (one fixed triple passes *all* binary congruence tests).** If $D=A c+q^2$ is a 2-adic square, there exist **three fixed, distinct, positive integers** $a,b,d$ (independent of the exponent $n$) such that, simultaneously for every $n\ge1$,

$$
ab+c,\quad ad+c,\quad bd+c
$$

are polygonal **residues** of order $k$ modulo $2^n$. This means all three Type B pair-output conditions are locally solvable at *every* power of two, for a single fixed triple of positive entries. It does **not** imply that those outputs equal actual positive-index polygonal integers. If $D$ is not a 2-adic square, this theorem makes **no converse claim** about Type B triples.

### Proof of Theorem A

The affine map $z\mapsto Az+q^2$ permutes the residues modulo $2^n$, because $A$ is odd. By the previously proved completed-square equivalence, its restriction bijects polygonal output residues onto quadratic residues modulo $2^n$. Therefore $N_k(n)=S(n)$, the number of distinct squares modulo $2^n$.

For $n\ge3$, split squares into *odd squares* and *multiples of four*. Exactly $2^{n-3}$ odd residue classes are squares modulo $2^n$ (the odd classes congruent to $1$ modulo eight). The residues of even squares are precisely $4$ times the square residues modulo $2^{n-2}$. Thus

$$
S(n)=2^{n-3}+S(n-2),\qquad S(1)=S(2)=2.
$$

Solving separately for even and odd $n$ gives the displayed closed formula and the limiting proportion $1/6$.

For the natural density assertion, the sets of permitted offsets are nested cylinder sets modulo powers of two. For a fixed exponent their integer density is exactly $S(n)/2^n$. In the limit, every 2-adic square is counted at all levels. The only potential nonuniform tail arises from transformed values $D$ divisible by very high powers of two; this tail occupies at most one residue class modulo $2^m$, of density $2^{-m}$, and tends to zero. Hence the integer set of offsets with a 2-adic-square transformed value has natural density $1/6$, independently of the odd affine transformation.

**Prior art:** The square-count formula is classical; Walter D. Stangl, [*Counting Squares in $\mathbb Z_n$* (1996)](https://www.jstor.org/stable/2690536), and [Wolfram MathWorld, *Square Number*](https://mathworld.wolfram.com/SquareNumber.html) record the same prime-power count. This is a **polygonal-image and Type B method corollary**, not an original square-count discovery.

### Proof of Theorem B: construct the *same* entries for every exponent

The 2-adic square criterion for a nonzero integer is precise: $D=2^{2j}u$ with $j\ge0$ and $u\equiv1\pmod8$ odd. Choose

$$
a=2^{j+2},\qquad b=2^{j+3},\qquad d=2^{j+4}.
\tag{1}
$$

All three are distinct and positive. Every pair product has 2-adic valuation at least $2j+5$. Since $A$ is odd, each transformed pair expression is

$$
A(xy+c)+q^2=D+Axy
=2^{2j}\bigl(u+2^{\ge5}\cdot v\bigr),
$$

for some integer $v$. Its valuation remains $2j$ and its odd unit stays $1\pmod8$. Hence **every** transformed pair expression is a square in $\mathbb Z_2$, and by the completed-square equivalence all three pair outputs are locally polygonal at *every* binary precision $2^n$. The entries in (1) do not depend on $n$.

The degenerate case $D=0$ is possible for integer offset $c$ **only when $k=4,c=0$**: since $A=2q+1$ and $\gcd(A,q)=1$, $A\mid q^2$ forces $A=1$, thus $q=0$. For this sole case choose the fixed triple $(1,4,16)$; its three pair products $4,16,64$ are actual squares (and hence square polygonal numbers).

This proves Theorem B. Unlike the earlier per-modulus construction using entry residue $(0,0,0)$, Theorem B supplies a **single triple of fixed positive integers with compatible output residues simultaneously at every exponent**. One must not mistake that result for the existence of an exact integer Type B triple.

### A practical exact offset test

For any integer $c$, compute $D=Ac+q^2$. The sufficient criterion for the preceding all-precision triple construction is

- $D=0$, or
- $v_2(D)$ is even and $D/2^{v_2(D)}\equiv1\pmod8$.

The function [`two_adic_square`](../research/figurate_wp08_2adic_density.py) checks exactly these alternatives with integer arithmetic, including negative offsets; [`fixed_coherent_triple`](../research/figurate_wp08_2adic_density.py) constructs the same three entries for every exponent. The density of offsets passing this test is exactly $1/6$.

This provides a rigorous **pruning rule for future 2-adic obstruction searches**: in the one-sixth offset class, no pure congruence obstruction at any power of two can prove nonexistence of Type B triples. Outside this class, further valuation analysis may or may not yield an obstruction; the complement is *not* a proven obstruction class.

## Reproduction and falsification boundaries

The [independent regression suite](../tests/test_figurate_wp08_2adic_density.py) evaluates the original polynomial directly to reconstruct polygonal-image counts for multiple orders through exponent 12; independently enumerates all square residues through exponent 12; checks negative integers against modular square roots; tests fixed coherent triples for **all exponents 1 through 16 and additionally 32 and 64** across thousands of order/offset cases; checks the actual $(1,4,16)$ square-output control; and verifies that every previous modulo-64 global obstruction lies outside the sufficient immunity class.

```sh
python3 -m research.figurate_wp08_2adic_density --k 8 --offset -8 --exponent 12
python3 -m research.figurate_wp08_2adic_density --k 12 --offset 1 --exponent 12
python3 -m unittest discover -s tests -p test_figurate_wp08_2adic_density.py -v
```

The tests are deterministic integer arithmetic; W&B logging, GPU execution and multi-seed ML experiments are not relevant to this mathematical verification. Protected CI and GitHub merge validate artifact integrity only, not mathematical originality or independent certification.

**Next research gate:** use the transformed simultaneous square equations to classify parameter families with **no 2-adic triple solution** (rather than just sufficient immunity), or compare the local obstruction hierarchy to Pell-equation global methods. The 1996 square-count formula and the completed-square discriminant are historical mathematics. Any external theorem-priority or specialist proof claim needs a separate source-semantic review.
