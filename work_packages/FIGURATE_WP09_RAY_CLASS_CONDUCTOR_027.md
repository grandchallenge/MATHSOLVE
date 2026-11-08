# FIGURATE WP09-027 — conductor-safe ideal norms and oriented ray principality

**Research boundary.** This establishes the quadratic-order reformulation of the recurring FIGURATE anchor problem; it does not compute all ray class groups, classify all parameters, claim a universal local-to-global principle, or assert independent MATHCERT certification. Parent: [WP09 #3145](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145).

## Exact setup

For every $m\ge0$ set

$$
A=8m+1,\quad D=2A,\quad H=8m(m+1)+1,\quad N=-2(2A-1)H.
$$

The protected WP09-025 criterion says that the order-$k=16m+4$, offset-$c=2$ anchor $(a,b,r)=(1,k-2,2)$ has an exact positive distinct extension iff there is an integer solution $x,y>0$ to

$$
x^2-Dy^2=N,\qquad x\equiv y\equiv r\pmod A,\qquad r=(A+1)/2.
$$

## Theorem A — conductor and norm coprimality

Write uniquely $A=f^2 a_0$ with $a_0$ odd squarefree and $f$ odd. Set $d=2a_0$, squarefree and congruent to 2 modulo four. Then

$$
K=\mathbf Q(\sqrt d),\quad
\mathcal O_K=\mathbf Z[\sqrt d],\quad
\mathcal O=\mathbf Z[\sqrt D]
=\mathbf Z[f\sqrt d]=\mathbf Z+f\mathcal O_K.
$$

The conductor is $f\mathcal O_K$, the field discriminant is $4d=8a_0$, and the order discriminant is $4D=8A=f^2(4d)$.

The identity $8H=A^2+6A+1$ gives $\gcd(A,H)=1$. Since $\gcd(A,2(2A-1))=1$, **$\gcd(A,N)=1$**. Every integral $\mathcal O$-ideal of norm $|N|$ is therefore prime to the conductor (because $f\mid A$), and is invertible. Such ideals extend and contract bijectively with integral ideals of the same norm in $\mathcal O_K$ coprime to $f$.

**Proof.** Square-part extraction and $d\equiv2\pmod4$ give the maximal order and exact conductor by the displayed integral bases. The discriminants follow by the basis index $f$. The identity for $H$ follows by substituting $m=(A-1)/8$. The gcd claims are immediate. For prime-to-conductor ideals the standard extension/contraction theorem for quadratic orders applies. QED.

This does **not** make congruence modulo $A\mathcal O_K$ interchangeable with the required congruence modulo $A\mathcal O$: the ray modulus itself contains conductor primes.

## Theorem B — all-place compatibility iff an invertible ideal of the required norm exists

For this whole family $(k,c)=(16m+4,2)$, the following statements are equivalent:

1. The protected WP09-012 Type B criterion is everywhere locally compatible.
2. Every rational prime inert in $K$ has **even valuation** in $|N|$.
3. There is an integral invertible $\mathcal O$-ideal of norm $|N|$ prime to $A$.

**Proof.** Every odd prime dividing $N$ is unramified: odd ramified primes divide $d$, hence $A$, while $\gcd(A,N)=1$. In the maximal order, inert primes contribute even exponents to ideal norms, split primes contribute arbitrary exponents, and the prime 2 (ramified because $d\equiv2\pmod4$) permits its actual exponent one. Thus 2 iff existence of an integral maximal-order ideal of norm $|N|$. Prime-to-conductor contraction proves 2 iff 3.

For the local equivalence, protected WP09-012 tests precisely the primes $p$ where the discriminant $\Delta=32H$ has odd valuation and the coefficient $(k-2)/2=A$ is a quadratic nonresidue. Any odd prime $p\mid H$ satisfies

$$
(A+3)^2=8H+8\equiv8\pmod p,
$$

so 2 is a quadratic residue modulo $p$. Therefore $(2A/p)=(A/p)$ at all such primes. If $p\mid(2A-1)$, then $2A\equiv1\pmod p$, so $p$ is split, not inert. Consequently the inert primes with odd valuation in $N=-2(2A-1)H$ are exactly the obstructing primes in WP09-012. QED.

**Interpretation:** in every everywhere-locally-compatible instance, an invertible norm-$|N|$ ideal **already exists**. Global anchor seed existence requires a stronger property: the correct oriented ray class must contain one.

## Theorem C — necessary-and-sufficient oriented order ray criterion

Let $\mathfrak m=A\mathcal O$ and define

$$
\rho=r(1+\sqrt D)\in\mathcal O,\qquad r=(A+1)/2.
$$

Its norm $r^2(1-D)$ is negative and coprime to $A$. Define the oriented ray class group $\operatorname{Cl}^{+}_{\mathfrak m}(\mathcal O)$ using invertible fractional $\mathcal O$-ideals prime to $\mathfrak m$ modulo principal ideals $(\gamma)$ with $\gamma$ totally positive at both real embeddings and $\gamma\equiv1\pmod{\mathfrak m}$ in the localized order. **Use the nonmaximal order $\mathcal O$**, not merely the maximal order.

Then the anchor admits an exact positive distinct seed iff there exists an integral invertible $\mathcal O$-ideal $\mathfrak a$ with

$$
N(\mathfrak a)=|N|,\qquad
[\mathfrak a]=[(\rho)]
\quad\text{in }\operatorname{Cl}^{+}_{\mathfrak m}(\mathcal O).
$$

**Necessity.** Given an exact anchor seed, the normalized solution $\alpha=x+y\sqrt D$ is in $\mathcal O$, has norm $N<0$, is positive in the chosen real embedding and negative in the conjugate. The element $\rho$ has the same signs. Consequently $\gamma=\alpha/\rho$ is totally positive. The coefficientwise ray $\alpha\equiv\rho\pmod{A\mathcal O}$, together with the invertibility of $\rho$ modulo $A$, gives $\gamma\equiv1\pmod{\mathfrak m}$ in the localized order. Thus the principal norm-$|N|$ ideal $(\alpha)$ lies in the ray class of $(\rho)$.

**Sufficiency.** Conversely, such an ideal equality of ray classes means $\mathfrak a/(\rho)=(\gamma)$ with $\gamma$ totally positive and $\gamma\equiv1\pmod{\mathfrak m}$. Put $\alpha=\rho\gamma$. Since $\mathfrak a=(\alpha)$ is integral, $\alpha\in\mathcal O$. Its norm has absolute value $|N|$ and its real signs equal those of $\rho$, so its norm is **exactly** $N<0$. Since both $\alpha$ and $\rho$ are integral and the congruence holds after localization, $\alpha\equiv\rho\pmod{A\mathcal O}$, meaning precisely $x\equiv y\equiv r\pmod A$. In the positive real embedding $\alpha>0$. A positive norm-one unit power preserving the ray eventually makes $x,y>0$ while keeping the norm and ray unchanged. Protected WP09-025 converts it into infinitely many exact positive distinct Type B triples. QED.

**Boundary:** existence of an ideal of norm $|N|$ is the local stage; ordinary or maximal-order principality is still insufficient. The needed equality is in the **oriented ray class group of the actual quadratic order**. This theorem is an iff criterion, not a computed classification of all $m$.

## Evidence and future computation

- Exact code: [conductor and inert-prime diagnostics](https://github.com/grandchallenge/MATHSOLVE/blob/main/research/figurate_wp09_ray_class_conductor_027.py).
- Independent tests: [WP09-027 regression suite](https://github.com/grandchallenge/MATHSOLVE/blob/main/tests/test_figurate_wp09_ray_class_conductor_027.py).
- Replay: python3 -m unittest -v tests.test_figurate_wp09_ray_class_conductor_027.

The source tests 500 conductor/discriminant cases, 250 all-place-versus-ideal-norm classifications against protected WP09-012, positive exact seed controls and examples of nonmaximal orders, with explicit negative prime-7 evidence. **The code does not calculate ray class groups or pretend that an ideal-norm YES is a global anchor YES.** Generalized-Pell arithmetic and quadratic-order ray class theory are classical background. See *Ray Classes for Orders*, Essential Number Theory 4 (2025), https://msp.org/ent/2025/4-1/ent-v4-n1-p01-p.pdf, for the congruence and invertible-ideal framework.

**Next actual mathematical obligation:** implement a rigorously tested ray-class calculator in the nonmaximal order (including its conductor and coefficientwise ray), enumerate the proper invertible ideals of norm $|N|$, and decide which meet the oriented class of $(\rho)$. Seek a parameter-uniform class criterion rather than simply solving more large Pell instances. Mathematical certification and external novelty comparison are distinct.
