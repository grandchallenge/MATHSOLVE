# FIGURATE WP09-034 — prime-general valuation and CRT criterion for an explicit oriented ray orbit

**Parent:** [FIGURATE-WP09 #3145](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145). **Protected dependencies:** WP09-025 (positive Type B Pell equivalence), WP09-027 (conductor-sensitive oriented ray), WP09-032 (powers of three), WP09-033 (3/5/7 mixed conductor construction).

**Precisely bounded claim:** For **every odd integer conductor f>1**, a complete finite prime-order, valuation, and generalized-CRT criterion determines whether the **specified explicit norm representative and its positive Pell-unit orbit** meet the oriented target ray of the actual conductor order. A positive answer yields an actual norm-|N| ray-class ideal and **infinitely many distinct positive Type B triples** for order k=2f²+2, offset 2 and first pair (1,2f²). A negative answer rules out **this particular explicit orbit only**, not any other norm representative, first pair, or all Type B triples. Computation guards report NOT COMPUTED, not a mathematical negative.

New unbounded single-prime-power sufficient families include f=11^e, 13^e, 17^e, 19^e, 23^e and 31^e for all e>=1. Higher unit-slope valuations at primes 13 and 31 change the exponent formula but do not block their prime-power families. Mixed successes include 33,39,65,93,155,365,403,1209. For f=219=3*73, an incompatibility blocks **only the explicit orbit**; claiming global nonexistence from it would be invalid.

## 1. Exact order, norm and target

For every odd f>1, set

$$
A=f^2,\quad k=2A+2,\quad
H=(A^2+6A+1)/8,\quad N=-2(2A-1)H<0,
$$

$$
\mathcal O_f=\mathbb Z[f\sqrt2],\quad
I=f^2\mathcal O_f=f^2\mathbb Z+f^3\mathbb Z\sqrt2,\quad
r=(A+1)/2,\quad \rho=r(1+f\sqrt2).
$$

Let

$$
u=3+2\sqrt2,\quad
\alpha=\frac{(1+f\sqrt2)(f^2+u)}2
=\frac{f^2+4f+3}2+\frac{f^3+3f+2}2\sqrt2.
$$

Both coefficients of alpha are integers and positive. Its norm is exactly

$$
N_{\mathbb Q(\sqrt2)/\mathbb Q}(\alpha)
=\frac{(1-2f^2)(f^4+6f^2+1)}4=N.
$$

Alpha need not lie in the nonmaximal order. The specific orbit studied here is beta_E=alpha*u^E for E>=0. The target requires beta_E in the *actual* order and beta_E≡rho (mod I).

## 2. Exact reduction to one unit congruence

**Lemma A.** With n=E+1>=1,

$$
\beta_E\equiv\rho\pmod I
\quad\Longleftrightarrow\quad
u^n\equiv1+2f^2\sqrt2\pmod{f^3\mathbb Z[\sqrt2]}.
$$

**Proof.** One has

$$
\beta_E-\rho
=\frac{1+f\sqrt2}{2}
\bigl(u^n+f^2u^{n-1}-1-f^2\bigr).
$$

The prefactor is invertible modulo the ideal I in the localization at the primes dividing f: its norm 1-2f², as well as 2, is coprime to f. Thus multiplication by it preserves membership in I, **without changing the conductor-order ray into a maximal-order ray**. Write u^n=X_n+Y_n sqrt(2). Requiring the bracket to lie in I means X_n≡1 (mod f²) and Y_n+f²Y_(n-1)≡0 (mod f³). The latter yields Y_n≡0 (mod f²), so u^n≡1 (mod f) and u^(n-1)≡u^(-1)=3-2sqrt(2) (mod f). Thus Y_n≡2f² (mod f³). Norm one gives

$$
(X_n-1)(X_n+1)=2Y_n^2.
$$

For odd f, X_n≡1 (mod f), hence X_n+1 is a unit at every p|f, and X_n-1 is divisible by f^4. In particular X_n≡1 (mod f³). This proves the forward implication. Conversely, the displayed congruence for u^n gives X_n≡1 mod f³ and Y_n≡2f² mod f³; with u^(n-1)≡3-2sqrt(2) mod f, the bracket's scalar belongs to f²Z and its radical to f³Z. Therefore beta_E-rho belongs to I. QED.

This is an if-and-only-if statement **for the selected alpha-unit orbit only**.

## 3. Prime-local primitive slopes

Let p^e||f for odd prime p and e>=1. The residue unit u has exact order t_p modulo p. Because it has norm one and 2 is unramified at p, t_p divides p-(2/p) (Legendre symbol) and p does not divide t_p. Write

$$
u^{t_p}=a_p+b_p\sqrt2,\qquad
\lambda_p=v_p(b_p)\ge1.
$$

The valuation is finite: a positive power of 3+2sqrt(2) is never a rational integer.

**Lemma B (uniform odd-prime lifting).** For all j>=0,

$$
v_p\!\left(\mathrm{rad}(u^{t_p p^j})\right)=\lambda_p+j,
\qquad
v_p\!\left(\mathrm{scal}(u^{t_p p^j})-1\right)=2(\lambda_p+j).
$$

More generally for positive integer h, the radical coefficient of u^(t_p h) has valuation lambda_p+v_p(h).

**Proof.** If z=a+b sqrt(2) has norm one, a≡1 mod p and v_p(b)=s>=1, the radical coefficient of z^p is p a^(p-1)b plus terms with at least three factors b. Intermediate binomial coefficients are p-divisible; the final b^p term has valuation ps>s+1 for odd p, including p=3. Thus the first term determines valuation s+1. Powers coprime to p preserve valuation s by the same binomial argument. The scalar stays 1 modulo p, and (a-1)(a+1)=2b², with a+1 p-adically invertible, gives v_p(a-1)=2v_p(b). Induction proves the assertions. QED.

If lambda_p>2e, every u^n congruent 1 modulo p has radical coefficient more highly divisible than p^(2e). It cannot equal 2f² (whose p-valuation is exactly 2e), so **this orbit** cannot hit the target.

If lambda_p<=2e, put

$$
L_p=t_p p^{2e-\lambda_p},\qquad
u^{L_p}\equiv1+p^{2e}B_p\sqrt2
\pmod{p^{3e}\mathbb Z[\sqrt2]},\quad p\nmid B_p.
$$

The scalar congruence follows from its valuation 4e>=3e. Define

$$
f_p=f/p^e,\qquad
h_p\equiv 2f_p^2B_p^{-1}\pmod{p^e},\qquad
r_p=L_ph_p,\qquad
M_p=t_p p^{3e-\lambda_p}.
$$

**Lemma C (full local exponent characterization).** For n>=1,

$$
u^n\equiv1+2f^2\sqrt2\pmod{p^{3e}\mathbb Z[\sqrt2]}
\quad\Longleftrightarrow\quad
n\equiv r_p\pmod{M_p}.
$$

**Proof.** Reduction modulo p forces t_p|n. Lemma B and the target's *exact* valuation 2e force n=t_p p^(2e-lambda_p)h. The base unit u^(L_p) has scalar 1 and radical p^(2e)B_p modulo p^(3e). Its h-th power has radical h p^(2e)B_p because the square of p^(2e) is divisible by p^(3e). Comparing with 2f²=2p^(2e)f_p² yields h≡h_p modulo p^e, and these are exactly the stated exponent classes. QED.

## 4. Generalized CRT gives an exact bounded-orbit decision

**Theorem D.** The explicit orbit beta_E=alpha*u^E contains a generator of the correct norm and coefficientwise oriented target ray **if and only if**:

1. Every p^e||f satisfies lambda_p<=2e; and
2. All local classes n≡r_p (mod M_p) are compatible:

$$
r_p\equiv r_q\pmod{\gcd(M_p,M_q)}
\qquad\text{for every }p,q\mid f.
$$

If compatible, generalized CRT constructs a positive solution n modulo the ray-preserving period T=lcm_(p|f) M_p. Put E=n-1>=0. Lemma A gives beta_E≡rho (mod I), *in the actual nonmaximal order*. The norm is N<0 and the first real embedding is positive, so (beta_E) is an integral invertible ideal of norm |N| and the correct oriented target ray class, by WP09-027. Since u^T≡1 modulo f³, all beta_E u^(qT) preserve the exact order ray and norm. WP09-025's inverse formulas give positive polygonal indices for sufficiently large q:

$$
s=\frac{y+(A-1)/2}{A},\quad
t=\frac{x+(A-1)/2}{A},\quad
d=P_k(s)-2,\quad
P_k(z)=Az(z-1)+z,
$$

where beta=x+fy sqrt(2). Thus infinitely many distinct positive triples (1,2A,d) satisfy

$$
P_k(2)=2A+2,\qquad P_k(s)=d+2,\qquad P_k(t)=2Ad+2.
$$

If either condition fails, there is **no target-ray generator in this alpha-unit orbit**. Generalized CRT and Lemmas A-C give both necessity and sufficiency within that scope. **Failure cannot certify nonexistence over all norm ideals, all Pell orbits, or all Type B first pairs.** QED.

## 5. Explicit prime-power and mixed-conductor consequences

The following local order and slope values are established with exact finite modular arithmetic and independent regressions:

| Prime p | Unit order t_p | lambda_p | Prime-power family f=p^e, all e>=1 |
|---:|---:|---:|:---|
| 3 | 4 | 1 | YES, predecessor |
| 5 | 6 | 1 | YES, predecessor |
| 7 | 3 | 1 | YES, predecessor |
| 11 | 12 | 1 | YES |
| 13 | 14 | 2 | YES, higher-slope case |
| 17 | 8 | 1 | YES |
| 19 | 20 | 1 | YES |
| 23 | 11 | 1 | YES |
| 31 | 15 | 2 | YES, higher-slope case |
| 73 | 36 | 1 | YES |

For **any fixed odd prime p with lambda_p<=2**, the theorem proves Type B anchor existence for **every exponent e>=1**, not merely the tested e=1,2. This does not assert all primes satisfy that bound.

Successful mixed conductors outside the previous 3/5/7 family include 33=3*11, 39=3*13, 65=5*13, 93=3*31, 155=5*31, 365=5*73, 403=13*31, and 1209=3*13*31.

**Important failure of the construction (not of Type B):** f=219=3*73. The p=3 local target forces n≡24 (mod 36), while the p=73 unit order is 36 and forces n≡0 (mod 36). The classes are incompatible. Thus the *specific alpha-unit orbit* misses the ray at conductor 219. No global anchor nonexistence or local-to-global counterexample has been established; other norm representatives might succeed.

## 6. Exact reproduction and genuine open boundaries

- [Executable prime-general exact orbit decision](https://github.com/grandchallenge/MATHSOLVE/blob/main/research/figurate_wp09_prime_general_crt_034.py): exact trial-factorization with resource guard, finite unit orders, coefficientwise p-adic valuations, invertible slope residues, generalized CRT, full conductor-ray and norm checks, and optional positive triples.
- [Independent exact test suite](https://github.com/grandchallenge/MATHSOLVE/blob/main/tests/test_figurate_wp09_prime_general_crt_034.py): brute mod-p orders, independent two-by-two unit matrices, exhaustive finite cyclic ray oracles, prime-power and mixed cases, full integer polygonal discriminant inversion, predecessor checks, and the f=219 counterexample to this method.
- Replay command: PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v tests.test_figurate_wp09_prime_general_crt_034.
- The outcome type OrbitObstruction is **orbit-scoped**; ResourceGuard is **not a mathematical verdict**. The mathematical theorem is valid independent of any configured computational cap.

**Next genuine obligations:** assess the *other* norm representatives/ideals when this orbit is blocked; determine whether a prime-general *all-orbit* realization theorem or a real everywhere-locally-compatible global obstruction can be proved; move beyond square conductors and fixed first pairs. External mathematical originality, independent MATHCERT certification, and wider Type A/C classification remain separate. Protected CI, merge and public MkDocs readback require independent evidence and are not inferred from creating this file.
