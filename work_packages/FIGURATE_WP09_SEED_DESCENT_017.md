# FIGURATE WP09-017 — exact seed-existence and index-first descent

Parent [WP09 #3145](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145). **Primary target:** order 84, offset 2. **Comparison:** order 100, offset 2. **Positive control:** order 68, offset 6. This is bounded internal mathematical research, not a global existence theorem, independent MATHCERT certification, or literature-priority claim.

## 1. Exact three-product criterion

Let $A,B,C$ be arbitrary positive integers. There exist *pairwise distinct positive integers* $a,b,d$ with $A=ab$, $B=ad$, $C=bd$ if and only if $T=\sqrt{ABC}$ is an integer divisible by each of $A,B,C$, and the entries $T/C,T/B,T/A$ are pairwise distinct.

**Proof.** If the equations hold, $ABC=(abd)^2$, so $T=abd$, giving $a=T/C$, $b=T/B$, $d=T/A$. Conversely, divisibility and distinctness make those positive integers, and $ab=T^2/(BC)=A$, similarly for $B,C$. QED.

Equivalently, at *every* prime $p$, the three valuations $u=v_p(A)$, $v=v_p(B)$, $w=v_p(C)$ satisfy

$$
u+v+w\equiv0\pmod2,
$$

$$
u\le v+w,\qquad v\le u+w,\qquad w\le u+v.
$$

The square condition is the parity constraint; the triangle inequalities are precisely the necessary divisibilities. The separate distinctness check remains essential. For polygonal Type B, set $A=P_k(r)-c$, $B=P_k(s)-c$, $C=P_k(t)-c$. This is a complete criterion **for specified indices**, not a theorem ensuring suitable indices exist.

## 2. Two-index gcd descent

Fix $1\le r<s$, and suppose $A=P_k(r)-c>0$, $B=P_k(s)-c>0$. All exact seeds whose first two pair indices are $(r,s)$ occur among the divisors

$$
a\mid\gcd(A,B),\qquad b=A/a,\qquad d=B/a
$$

for which $a,b,d$ are positive and distinct and

$$
AB/a^2+c=P_k(t)
$$

for a positive integer index $t$. This follows immediately by solving $ab=A$ and $ad=B$; conversely each accepted divisor satisfies all three pair equations. The ordering $r<s$ is no substantive restriction for unordered triples: relabel the entries so that $b<d$.

For a positive candidate $y$, define $R=2(k-2)$ and $L=k-4$. The exact positive polygonal-index test is

$$
8(k-2)y+L^2=z^2,\qquad z+L\equiv0\pmod R,
$$

where $z$ is the nonnegative integer square root and $(z+L)/R$ must be positive. Both the discriminant and divisibility checks are mandatory. Thus the search uses **two indices and divisors of a gcd**, rather than a large three-entry cube. It is complete for a specified index window but does not turn finite absence into global impossibility.

## 3. Fixed-first-pair norm reduction

Fix $a,b,r$ with $a,b>0$, $a\ne b$ and $ab+c=P_k(r)$. Let

$$
R=2(k-2),\quad L=k-4,\quad
\Delta=8(k-2)c+L^2.
$$

Any exact extension by a third positive distinct entry $d$ at indices $s,t$ yields integers $S=Rs-L$ and $X=a(Rt-L)$ solving

$$
X^2-abS^2=a(a-b)\Delta.
$$

Indeed, $S^2=8(k-2)(ad+c)+L^2$ and $(X/a)^2=8(k-2)(bd+c)+L^2$; subtracting gives the norm identity.

**Important converse conditions.** A norm solution alone is not an exact seed. One must also verify $a\mid X$, positive integral indices $s=(S+L)/R$, $t=(X/a+L)/R$, and positive integral $d=(P_k(s)-c)/a$ distinct from $a,b$. Finally check $P_k(t)=bd+c$ exactly; it follows from the norm and first-pair identities once all integrality conditions hold. This isolates the remaining arithmetic question: does the norm equation admit a solution on the required integral lattice with positivity and distinctness?

## 4. Positive and negative controls

For $(k,c)=(68,6)$, the protected exact seed $(a,b,d)=(10,44033,128739)$, $(r,s,t)=(116,198,13107)$ satisfies the gcd descent: $A=440330$, $B=1287390$, and $a=10\mid\gcd(A,B)$. The third shifted product is $5668764393=P_{68}(13107)$. The nonsquare first-pair product $ab=440330$ allows the earlier WP09-013 Pell amplification theorem to produce infinitely many exact triples.

At $(84,2)$ and $(100,2)$, WP09-016 has already proved a complete **entry-bounded** absence of triples whose entries are all at most 300,000. The new code supplies a different index-window search and exact first-pair arithmetic; finite negative tests must remain expressly finite. Both parameter pairs pass the previously proved full local arithmetic sieve, so no global nonexistence statement is justified.

## 5. Research programme and acceptance criteria

The next mathematical obligations are to identify fixed first pairs where integral norm/lattice solubility can be decided; derive a nontrivial sufficient construction or an unbounded obstruction for a parameter family; and distinguish integer obstructions from rational/local norm solubility. Explore order 84 first, compare order 100, and require the order-68 positive control to survive each new filter. A computational search is useful only as a test of the proposed arithmetic mechanism, not as an end in itself.

Reproduce using the research module at [research/figurate_wp09_seed_descent_017.py](https://github.com/grandchallenge/MATHSOLVE/blob/main/research/figurate_wp09_seed_descent_017.py) and independent tests at [tests/test_figurate_wp09_seed_descent_017.py](https://github.com/grandchallenge/MATHSOLVE/blob/main/tests/test_figurate_wp09_seed_descent_017.py).

    python3 -m unittest -v tests.test_figurate_wp09_seed_descent_017
    python3 -m research.figurate_wp09_seed_descent_017 --order 84 --offset 2 --max-r 120 --max-s 220

No assertion of global local-to-global validity, counterexample, external originality or independent mathematical certification is made.