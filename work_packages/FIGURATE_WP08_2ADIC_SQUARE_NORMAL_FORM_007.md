# FIGURATE WP08 — exact binary square normal form for every order divisible by four

**Programme:** [FIGURATE #3093](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3093) · [WP08 #3125](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3125). **Tranche 007, 4 November 2026.**

**Mathematical status:** elementary identity and its full necessary-and-sufficient modular consequence proved below and checked with exact arithmetic. This is not an originality claim or specialist mathematical certification.

## The structural theorem

Let $k\ge4$ be divisible by four. Define the **odd** positive integer $A=k/2-1$ and nonnegative integer $q=k/4-1$. For every integer index $t$,

$$
P_k(t)=At^2-2qt
\qquad\Longrightarrow\qquad
A P_k(t)+q^2=(At-q)^2.
$$

**Theorem (complete 2-power image).** For every integer output $z$ and every exponent $n\ge1$,

$$
z\in\{P_k(t)\bmod2^n:t\ge1\}
\quad\Longleftrightarrow\quad
Az+q^2\text{ is a square modulo }2^n.
\tag{1}
$$

*Proof.* The displayed integer identity gives the forward implication. Conversely, suppose $Az+q^2\equiv y^2\pmod{2^n}$. Since $A$ is odd, the affine map $t\mapsto At-q$ is bijective on $\mathbb Z/2^n\mathbb Z$. Choose $t\equiv A^{-1}(y+q)\pmod{2^n}$ and select a positive representative. Then $(At-q)^2\equiv y^2$, and because $A$ is invertible, $P_k(t)\equiv z\pmod{2^n}$. QED.

This is a **necessary and sufficient** congruence condition for polygonal output *residues*. It does not by itself determine whether a specific large integer $z$ equals $P_k(t)$ for an actual positive index $t$; the exact integer discriminant, index congruence and sign conditions remain relevant.

### Exact valuation criterion for the transformed output

Write $x=Az+q^2$, reduce it modulo $2^n$, and let $v=v_2(x)$ for the nonzero residue $x$. A square root modulo $2^n$ exists **if and only if** one of the following occurs:

- $x\equiv0\pmod{2^n}$; or
- $v$ is even and, for the odd unit $u=x/2^v$ and remaining precision $r=n-v$, $u\equiv1\pmod{2^{\min(3,r)}}$.

This includes the low-precision edge cases: at $r=1$, every odd unit is a square; at $r=2$, the unit must be $1$ modulo $4$; at $r\ge3$, it must be $1$ modulo $8$.

The necessity follows from the even valuation of an integer square and the well-known odd-square residues modulo $2^r$. Sufficiency at $r\ge3$ follows by lifting roots: every odd $u\equiv1\pmod8$ is a square modulo every $2^r$, and the low-precision cases are direct. Multiplication by $2^{v/2}$ reconstructs the square root for the original precision. Consequently the necessary polygonal-output test involves **one transformed 2-adic valuation and three low unit bits**, rather than a search over polygonal indices.

## Exact Type B tuple reformulation

For **Type B**, a triple of positive distinct entries $(a,b,d)$ has its three shifted pair products locally polygonal modulo $2^n$ **if and only if** all three transformed expressions

$$
A(ab+c)+q^2,\qquad
A(ad+c)+q^2,\qquad
A(bd+c)+q^2
$$

are quadratic residues modulo $2^n$. Thus the full *single-modulus* polygonal-output compatibility condition is a simultaneous square-residue condition. This is a precise algebraic bridge to Diophantine $D$-tuple methods, but it is **not** an equivalence between unrestricted integer Type B tuples and classical $D(c)$ tuples without extra index and sign restrictions.

The algebra explains the earlier infinite hierarchy: increasing the exponent progressively resolves the valuation and odd-unit bits of the same three transformed outputs. It also explains the order split established in [tranche 006](FIGURATE_WP08_2ADIC_SURJECTIVITY_MOD64_006.md): orders with $4\nmid k$ are 2-adically surjective, whereas orders with $4\mid k$ have the square-residue image described in (1).

### Consequence for image sizes

Because the map $z\mapsto Az+q^2$ is an invertible affine transformation modulo $2^n$, the number of distinct polygonal output residues is **exactly** the number of quadratic residues modulo $2^n$, independent of which order divisible by four is chosen. The *location* of these allowed residues depends on $k$, but their count does not.

This is stronger than the previously observed universal restriction to residues $\{0,1\}$ modulo $4$, and it holds for every exponent.

## Executable and adversarial verification

The source [`figurate_wp08_square_normal_form.py`](../research/figurate_wp08_square_normal_form.py) implements the exact odd-unit square criterion, the affine normal form, and the locally equivalent Type B triple test. Its companion [independent tests](../tests/test_figurate_wp08_square_normal_form.py) verify:

1. The polynomial completed-square identity for all orders divisible by four through 84 and 300 positive indices each.
2. The quadratic residue predicate against complete independently enumerated square images modulo $2^n$ through $n=10$.
3. The transformed polygonal image against independent direct enumeration for all such orders through 64 and $n\le9$.
4. The transformed Type B triple condition against direct polynomial membership, including repeated entry residues.
5. Exact agreement of first local triple witnesses with the protected modulo-64 classifier for multiple orders and all 64 offsets.
6. Positive actual Type B pairs in globally forbidden triple families, guarding against a vacuous pair argument.
7. Invalid-order and input rejection.

```sh
python3 -m research.figurate_wp08_square_normal_form --k 8 --exponent 6 --output 21
python3 -m research.figurate_wp08_square_normal_form --k 16 --exponent 6 --offset 5
python3 -m unittest discover -s tests -p test_figurate_wp08_square_normal_form.py -v
```

**Scope and priority:** The theorem is an elementary square-completion consequence of $k$-gonal number arithmetic; square-residue valuation criteria are classical. No novelty claim is justified without detailed source review, and a repository merge is not mathematical certification. An intellectually substantive successor is to exploit this normal form to obtain a *valuation-classification theorem for global Type B triple impossibility*, or to prove non-stabilization/stabilization of the local obstruction hierarchy, rather than extending tables mechanically.
