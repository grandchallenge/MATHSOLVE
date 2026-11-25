# FIGURATE WP09-033 — uniform target-ray realization for mixed 3/5/7-power conductors

**Parent:** [FIGURATE-WP09 #3145](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145). **Protected predecessors:** WP09-025 (primitive Pell criterion), WP09-027 (conductor-sensitive ideal/ray equivalence), WP09-028 (individual ideal-fibre decisions), WP09-031 (full oriented square-conductor ray groups), and WP09-032 (uniform powers-of-three construction).

**Precisely bounded theorem:** the required oriented ray class is represented by an integral ideal of the prescribed norm for **every positive odd conductor**

$$
f=3^a5^b7^c,\qquad a,b,c\ge0,\qquad a+b+c>0.
$$

Consequently for **every such conductor** there are infinitely many positive exact Type B triples with polygonal order $k=2f^2+2$, offset $c_{\mathrm{off}}=2$, and fixed first pair $(1,2f^2)$. This establishes *mixed* conductor families (including $f=15,21,35,105$) and other prime-power subfamilies ($5^b,7^c$). It does **not** establish arbitrary odd conductors, arbitrary initial pairs, general all-$m$ local-to-global equivalence, independent MATHCERT certification, or literature originality.

## 1. Exact anchor and assertion

Set $A=f^2$ and $m=(A-1)/8$, an integer since $f$ is odd. Let

$$
H=(A^2+6A+1)/8,\quad D=2A,\quad N=-2(2A-1)H<0,
$$

$$
K=\mathbb Q(\sqrt2),\quad
\mathcal O_f=\mathbb Z[f\sqrt2],\quad
I=f^2\mathcal O_f=f^2\mathbb Z+f^3\mathbb Z[\sqrt2],
$$

$$
r=(A+1)/2,\qquad \rho=r(1+f\sqrt2)\in\mathcal O_f.
$$

The theorem produces a **specific** element $\beta\in\mathcal O_f$ with norm $N$, positive in the first real embedding, negative in the conjugate embedding, and

$$
\beta\equiv\rho\pmod{I}.
$$

Its integral principal ideal $(\beta)$ therefore has norm $|N|$ and lies in the **correct oriented ray class** of $(\rho)$. It is invertible and prime to the conductor because $\gcd(N,f)=1$ (as in WP09-027). Thus the target norm-ideal fibre is **actually realized**, not merely locally admissible or an abstract group element. WP09-025 and WP09-027 then imply infinitely many exact positive Type B extensions of $(1,2A)$.

## 2. Elementary primitive unit bases at three primes

Take the totally positive norm-one unit

$$
u=3+2\sqrt2,\qquad N_{K/\mathbb Q}(u)=1.
$$

The following identities require only exact multiplication:

| Prime $p$ | Base exponent $t_p$ | $u^{t_p}=x_p+y_p\sqrt2$ | $x_p\equiv1\pmod p$ | $v_p(y_p)$ |
| ---: | ---: | :--- | :---: | ---: |
| 3 | 4 | $577+408\sqrt2$ | yes | 1 |
| 5 | 6 | $19601+13860\sqrt2$ | yes | 1 |
| 7 | 3 | $99+70\sqrt2$ | yes | 1 |

**Lifting lemma.** For any $p\in\{3,5,7\}$ and any $j\ge0$, write

$$
u^{t_p p^j}=a_j+b_j\sqrt2.
$$

Then $a_j\equiv1\pmod p$, $v_p(b_j)=j+1$, and $v_p(a_j-1)=2(j+1)$.

**Proof.** The base table proves the assertions at $j=0$ except the last identity. The norm-one equation

$$
(a_j-1)(a_j+1)=2b_j^2
$$

and $a_j+1\equiv2\pmod p$ imply the last identity whenever $v_p(b_j)\ge1$. For the induction, the radical coefficient of $(a+b\sqrt2)^p$ is

$$
p a^{p-1}b+
\binom p3\,2a^{p-3}b^3+
\binom p5\,2^2a^{p-5}b^5+\cdots.
$$

For $p=3$, the two terms are $3a^2b+2b^3$; the first has valuation $v_p(b)+1$ and the second has strictly larger valuation. For $p=5,7$, every term beyond the first has valuation at least $v_p(b)+2$: terms with an odd power of $b$ have at least $b^3$ and the intermediate binomial coefficients are divisible by $p$ (the final $b^p$ term is even more highly divisible). Hence the first term alone fixes the valuation, raising it by exactly one. The scalar remains $1$ modulo $p$, and the norm-one factorization again proves its valuation. QED.

## 3. Simultaneous lifting for mixed conductors

Write $e_p=v_p(f)>0$ for primes dividing $f$, and define an explicit common exponent

$$
L=\operatorname{lcm}_{p\mid f}
\bigl(t_p p^{2e_p-1}\bigr).
$$

**Crucial compatibility:** for $p=3,5,7$ dividing $f$,

$$
v_p(L)=2e_p-1.
$$

Indeed $t_3=4$, $t_5=6$, $t_7=3$. None is divisible by its own prime. The only other-prime contribution among these base periods is a single factor of $3$ in $t_5$ or $t_7$, already covered by $3^{2e_3-1}$ whenever $3\mid f$. No other base period supplies extra powers of $5$ or $7$. Therefore, for each $p^{e_p}\parallel f$, the lifting lemma and multiplication by the $p$-coprime cofactor $L/(t_p p^{2e_p-1})$ imply

$$
u^L\equiv1+f^2 B\sqrt2\pmod{f^3\mathbb Z[\sqrt2]},
\qquad \gcd(B,f)=1.
$$

The scalar is $1$ modulo $p^{3e_p}$ because its difference from one has valuation at least $4e_p\ge3e_p$. The radical coefficient has **exact** $p$-adic valuation $2e_p$, so dividing it by $f^2$ produces a unit modulo every $p\mid f$. The Chinese remainder theorem combines these congruences simultaneously.

Define $B$ modulo $f$ as the radical coefficient of $u^L$ divided by $f^2$. Let $j$ be the **unique integer between $1$ and $f-1$** such that

$$
jB\equiv2\pmod f,
$$

and put $n=Lj$ and $E=n-1\ge0$. Because $(f^2\sqrt2)^2$ is divisible by $f^3$, binomial expansion gives

$$
u^n\equiv1+2f^2\sqrt2\pmod{f^3\mathbb Z[\sqrt2]}.
$$

No generalized-Pell representative enumeration, full class-group tabulation or large unconstrained search is required.

## 4. Explicit norm ideal and **actual order** ray hit

For **every odd** $f$, define the positive first-embedding element

$$
\alpha=\frac{(1+f\sqrt2)(f^2+u)}{2}
=\frac{f^2+4f+3}{2}+
 \frac{f^3+3f+2}{2}\sqrt2.
$$

Both coefficients are integers. Its norm is exactly

$$
N(\alpha)=\frac{(1-2f^2)(f^4+6f^2+1)}4
=-2(2A-1)H=N.
$$

The element $\alpha$ **need not belong to** $\mathcal O_f$ and is not yet a ray witness. Correct it by setting

$$
\beta=\alpha u^E,\qquad E=Lj-1.
$$

Modulo $f^3\mathbb Z[\sqrt2]$, because $u^{-1}=3-2\sqrt2$,

$$
u^n+f^2u^{n-1}\equiv
1+2f^2\sqrt2+f^2(3-2\sqrt2)
=1+3f^2.
$$

Consequently

$$
\beta
=\frac{1+f\sqrt2}{2}\bigl(u^n+f^2u^{n-1}\bigr)
\equiv\frac{1+f\sqrt2}{2}(1+3f^2)
\pmod{f^3\mathbb Z[\sqrt2]}.
$$

But $\rho=(1+f^2)(1+f\sqrt2)/2$. Their difference on the right is

$$
f^2(1+f\sqrt2)\in f^2\mathcal O_f=I.
$$

Since $f^3\mathbb Z[\sqrt2]\subset I$, this establishes the **full coefficientwise conductor-order congruence**, not just congruence in the maximal order:

$$
\boxed{\beta\in\mathcal O_f,\quad \beta\equiv\rho\pmod I,\quad N(\beta)=N.}
$$

The first real embedding of $\beta$ is positive and its norm negative, so it has the same real-sign orientation as $\rho$. Thus $(\beta)$ is an integral invertible norm-$|N|$ ideal in the **target oriented ray class**, as demanded by WP09-027. QED.

## 5. Infinitely many actual positive-index Type B triples

Write $\beta=x+fy\sqrt2=x+y\sqrt D$. The ray says $x\equiv y\equiv r\pmod A$. WP09-025 gives the exact integer formulas

$$
s=\frac{y+(A-1)/2}{A},\qquad
t=\frac{x+(A-1)/2}{A},\qquad
d=P_k(s)-2,\quad P_k(z)=Az(z-1)+z.
$$

The norm identity implies *exactly*, not merely locally,

$$
P_k(2)=2A+2,\quad
P_k(s)=d+2,\quad
P_k(t)=2Ad+2.
$$

All congruences needed for integral $s,t$ follow from the ray. The positive coefficients of $\alpha$ and $u^E$ imply $x,y>0$. To guarantee positivity and pairwise distinctness in every case, use the ray-preserving period $T=fL$: the formula for $u^L$ implies $u^{fL}\equiv1\pmod{f^3}$, so replacing $\beta$ by $\beta u^{qT}$, $q\ge0$, preserves the exact norm and ray, while $s,t,d$ tend to infinity. Every sufficiently large $q$ supplies a positive, distinct exact Type B triple, and distinct $q$ give distinct $d$. QED.

## 6. Reproducibility and bounded evidence

- [Exact certificate and optional full-integer constructor](https://github.com/grandchallenge/MATHSOLVE/blob/main/research/figurate_wp09_mixed_conductor_realization_033.py) uses the proven finite unit-lifting exponent and a modular inverse, and checks the stronger full order-ray congruence. It reuses the protected integer ring-power utilities of WP09-032 but not its power-of-three-specific construction.
- [Independent arithmetic tests](https://github.com/grandchallenge/MATHSOLVE/blob/main/tests/test_figurate_wp09_mixed_conductor_realization_033.py) implement the unit action as a separate two-by-two matrix, independently recompute norms and polygonal indices from discriminants, cover 26 prime-power/mixed conductor combinations, compare the $3^e$ subfamily with WP09-032, and verify that unsupported primes/size guards do **not** return mathematical nonexistence.
- Replay: \`PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v tests.test_figurate_wp09_mixed_conductor_realization_033\`.

| Conductor $f$ | Polygonal order $k=2f^2+2$ | Common lift $L$ | Constructive unit exponent $E$ | Type B statement |
| ---: | ---: | ---: | ---: | :--- |
| 3 | 20 | 12 | 23 | Earlier WP09-032 subfamily |
| 5 | 52 | 30 | 29 | Uniform $5$-power subfamily |
| 7 | 100 | 21 | 62 | Uniform $7$-power subfamily |
| 15 | 452 | 60 | 419 | Mixed $3\cdot5$ conductor |
| 21 | 884 | 84 | 419 | Mixed $3\cdot7$ conductor |
| 35 | 2452 | 210 | 6719 | Mixed $5\cdot7$ conductor |
| 105 | 22052 | 420 | 1679 | Mixed $3\cdot5\cdot7$ conductor |

These exponents are constructive, not necessarily minimal. Explicit original witnesses in some small $k$ were already known; the claimed mathematical gain is the **uniform mixed-conductor ray realization**. Source/test creation alone is not evidence of executed tests; exact-head CI, CHAD replay, protected merge and public-document admission must be independently observed before asserting closure.

**Boundaries and successor:** this is a **sufficient family**, not an iff criterion for arbitrary odd $f$. Unsupported prime factors (including cases where the above primitive-lift argument does not apply) are classified as **outside theorem scope**, never as globally impossible. The next substantive question is to formulate a prime-general primitive-unit criterion and determine its precise obstructions, or find a truly global failure of the target class despite all-place norm compatibility. General $A=f^2a_0$ with $a_0\ne1$, other first pairs, Type A/C results, external priority and independent MATHCERT certification remain open.
