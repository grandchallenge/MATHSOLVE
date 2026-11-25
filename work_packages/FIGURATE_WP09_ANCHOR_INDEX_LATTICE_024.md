# FIGURATE WP09-024 — uniform anchor index restrictions and a smaller exact Pell orbit

**Scope:** Two theorems. The first supplies a uniform *necessary* modulo-32 branch restriction for the frequent first pair $(a,b)=(1,k-2)$ at $(k,c,r)=(16m+4,2,2)$. The second improves WP09-023's complete fixed-first-pair Pell decision by proving a smaller sufficient modular period. This is internal producer research; global local-to-global existence, independent MATHCERT certification and external priority are not claimed. [Parent FIGURATE WP09](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145).

## Theorem A — uniform forced index classes

For integer $m\ge0$, put $k=16m+4$ and $q=k-2=16m+2$. Suppose a positive distinct exact Type B seed has $(a,b,c,r)=(1,q,2,2)$ and third entry $d>0$ at positive indices $s,t$:

$$
d+2=P_k(s),\qquad qd+2=P_k(t).
$$

Then necessarily

$$
s\equiv1\pmod2,\qquad d\equiv7\pmod8,\qquad t\equiv0\pmod4,
$$

and the sharper uniform condition is

$$
\frac{t}{4}\equiv m+\frac{s^2-1}{8}\pmod2.
$$

In particular, once $s\bmod8$ and $m\bmod2$ are specified, the permitted $t\bmod8$ is determined. These conditions are not sufficient for an exact seed.

**Proof.** The polygonal formula specializes to

$$
P_k(n)=n+\frac q2 n(n-1)=n^2+8m\,n(n-1).
$$

Since $n(n-1)$ is even, $P_k(n)\equiv n^2\pmod{16}$. The expression $qd+2$ is even, so $P_k(t)$ is even and $t$ is even. Thus $P_k(t)\equiv0\pmod4$; because $q\equiv2\pmod4$, the identity $qd+2=P_k(t)$ forces $d$ odd. Hence $P_k(s)=d+2$ odd, giving $s$ odd. An odd square is one modulo eight, so $d=P_k(s)-2\equiv7\pmod8$. Therefore $qd+2\equiv0\pmod{16}$, and $t^2\equiv0\pmod{16}$ forces $4\mid t$.

For odd $s$, the integer $(s^2-1)/8$ exists. Since $d\equiv s^2-2\pmod{16}$, $(d+1)/8$ has the same parity as $(s^2-1)/8$. With $q=16m+2$ and odd $d$,

$$
qd+2=2(d+1)+16md
\equiv16\left(\frac{d+1}{8}+m\right)\pmod{32}.
$$

For $4\mid t$, the term $8m\,t(t-1)$ is divisible by 32, so $P_k(t)\equiv t^2\equiv16(t/4)\pmod{32}$. Comparing both sides proves the final congruence. QED.

## Theorem B — uniform reduction of the complete Pell index-lattice modulus

Fix an arbitrary polygonal order $k\ge3$, integer offset $c$, and distinct positive first entries $a,b$ satisfying $ab+c=P_k(r)$ at positive index $r$, with nonsquare $Q=ab$. Set $R=2(k-2)$, $L=k-4$, $X=a(Rt-L)$ and $S=Rs-L$ as in WP09-023.

Define the **integer-polynomial period**

$$
h=\begin{cases}
a,&(k-2)(a-1)\equiv0\pmod2,\\
2a,&(k-2)(a-1)\equiv1\pmod2.
\end{cases}
$$

Then all WP09-023 integer-index and third-entry divisibility conditions depend **only on $(X,S)\bmod Rh$**. Therefore the WP09-023 complete positive-seed YES/NO theorem remains necessary and sufficient with modulus $M=Rh$ in place of $2aR$.

In particular, when $k$ is even or $a$ is odd, $h=a$ and the at-most-$M^2$ modular state bound decreases by a factor four. For the recurring anchor $a=1$, $M=R$ instead of the previous $2R$. For odd $k$ and even $a$, retain $h=2a$; the smaller period $a$ is generally invalid.

**Proof.** For integer $n$ and positive integer $h$,

$$
P_k(n+h)-P_k(n)=h+\frac{k-2}{2}h(2n+h-1).
$$

When $h=a$ and $(k-2)(a-1)$ is even, the right side is divisible by $a$, since $2n+a-1$ has the parity of $a-1$. In the remaining case, taking $h=2a$ again makes the difference divisible by $a$. Consequently $P_k(n)\bmod a$ is determined by $n\bmod h$ for all integer $n$.

The congruence $a\mid X$ and the positive-index integrality condition $(X/a+L)\equiv0\pmod R$ are determined modulo $aR$, which divides $Rh$. The condition $(S+L)\equiv0\pmod R$ is likewise determined. Whenever this holds, changing $S$ by $Rh$ changes $s$ by $h$, and the polynomial-period identity preserves $a\mid P_k(s)-c$. Therefore all admissibility conditions are residue functions modulo $Rh$.

The norm-one Pell multiplication matrix has determinant one, so its reduction modulo $Rh$ is invertible; every residue orbit is purely periodic. Exhausting those orbits produces precisely the same existence decision as WP09-023. At a compatible residue, further forward norm-one steps preserving the residue eventually produce positive distinct third entries and indices. The exact norm identity then supplies the third polygonal equation. Conversely any exact seed appears in a normalized representative orbit, and its residue is recognized. QED.

## Evidence, exact scopes and successor

The [integer-exact implementation](https://github.com/grandchallenge/MATHSOLVE/blob/main/research/figurate_wp09_anchor_index_lattice_024.py) supplies a modulo-32 necessary-branch check and an optimized fixed-pair decision. [Independent regressions](https://github.com/grandchallenge/MATHSOLVE/blob/main/tests/test_figurate_wp09_anchor_index_lattice_024.py) test 45 order classes and 79 index candidates, positive first-pair controls at orders 84, 100, 308, a complete negative first-pair control at order 68, comparisons with the protected WP09-023 original decision, integer-polynomial periods across even and odd orders and invalid domains. Resource guards continue to raise rather than report false mathematical absence.

Replay via the Python unittest module tests.test_figurate_wp09_anchor_index_lattice_024. Both theorems are **uniform in their stated parameters**. Neither establishes a universal seed for all locally compatible parameter pairs, and the first theorem is necessary only.

The next genuinely substantive obligation is a uniform proof determining which anchor first pairs have an integral norm-orbit representative (or an unbounded obstruction), and whether arbitrary candidate first pairs can be reduced to finitely many classes for a parameter family. Continuing isolated enormous seed discovery alone does not settle that question.
