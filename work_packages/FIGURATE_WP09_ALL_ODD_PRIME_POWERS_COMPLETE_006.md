# FIGURATE WP09-006 — complete odd-prime-power Type B local criterion

**Status:** internal research theorem; no independent certification, original-literature priority or global exact-integer existence claim. Continuing WP09 tracker: https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145.

## Main theorem (every odd prime, every exponent)

Let k>=3 and c be any integers, p any odd prime, n>=1, q=p^n, and
P_k(t)=t+(k-2)t(t-1)/2.
Define **local Type B compatibility modulo q** as the existence of residues a,b,d and polygonal index residues r,s,t modulo q with
ab+c=P_k(r), ad+c=P_k(s), bd+c=P_k(t) (mod q).
Residue repetitions are allowed: a,b,d can be lifted to distinct positive integers without changing their residues. The index residues also have positive integer representatives. This is strictly local, NOT an exact-integer Type B construction.

Write D=8(k-2)c+(k-4)^2. Then local compatibility **fails if and only if** all of the following hold:

1. p does not divide k-2;
2. A=(k-2)/2 is a nonzero quadratic nonresidue modulo p;
3. The truncated valuation e=min(v_p(D),n) is **odd and strictly smaller than n**.

In every other case, the three compatible entry residues can be chosen **equal to one residue x** with x²+c polygonal modulo q. The implementation constructs the polygonal index t as well.

Thus the WP09-005 p² obstruction is not merely sufficient: the *complete* local picture at all odd prime powers is controlled by the parity of a single discriminant valuation. The first obstructing modulus, whenever it exists, is p^(e+1), with e odd. For e=1 this is p²; for e=3 the first obstruction is p^4, etc. No odd-prime-power obstruction exists when D=0 as an integer.

## Proof: normal form

For p not dividing k-2, work modulo q with units 2 and k-2 and define
A=(k-2)/2, h=(k-4)/(2(k-2)), B=-(k-4)^2/(8(k-2)),
v=c-B=D/(8(k-2)).
The complete-square polynomial identity is P_k(t)=A(t-h)^2+B.
The three local equations are equivalent to xy+v=A z² for each of the three entry pairs. Multiplying D by a unit does not change its p-valuation, so e is the truncated valuation of v.

### Necessity: odd valuation + A nonsquare forbids every triple

Suppose e=2r+1<n, and A is a nonsquare modulo p. Let a,b,d be a hypothetical local triple. For any pair xy, set s=v_p(xy), using n as valuation for zero mod q.

- If s>e, then xy+v has valuation e, which is odd, whereas A z² has even valuation below n. Impossible.
- If s<e, then xy+v has valuation s. Therefore s is even, and its leading unit after dividing by p^s must be A times a square, hence a nonsquare modulo p.
- If s=e, for xy+v to have even valuation, the leading coefficients must cancel: xy/p^e = -v/p^e (mod p). Otherwise the sum has forbidden odd valuation e.

Consequently the three pair valuations s_ab,s_ad,s_bd are all <=e. Among those **strictly less than e**, the valuations are even. Since their sum is 2(v_p(a)+v_p(b)+v_p(d)), an even integer, the number of pairs with valuation e (which is odd) is even: either zero or two. (Three such pairs is also impossible by parity.)

If **zero** pairs have valuation e, all three pair values xy/p^s have nonsquare leading units. Multiplying these three units gives the square of the product of the three entry leading units, a square; multiplying three nonsquares gives a nonsquare. Contradiction.

If **two** pairs have valuation e, relabel entries so ad and bd have valuation e; the remaining pair ab has even valuation <e. Write a=p^u a0, b=p^u b0 (their valuations are equal because v_p(ad)=v_p(bd)), and d=p^w d0, with a0,b0,d0 units. The two cancellation equations imply a0*d0=b0*d0 (mod p), so a0=b0 (mod p). But ab/p^(2u)=a0*b0 is a nonzero square mod p; the ab equation with valuation <e requires a nonsquare. Contradiction.

For modular representatives where a,b,d vanish modulo p^n, any pair containing such an entry has valuation >=n>e and has already been ruled out, so the argument covers all residue classes.

Hence no local triple exists.

### Sufficiency: constructive diagonal residue witness

It suffices to find x,t modulo q with x²+c=P_k(t), then choose the **three equal entry residues x,x,x**. Their distinct positive integer representatives x+q,x+2q,x+3q establish coherent local triple compatibility; each pair output has the same polygonal index residue t.

**Case I, p divides k-2.** P_k(t)=t (mod p). Moreover for j>=1,
P_k(t+p^j)-P_k(t)=p^j(1+(k-2)t+(k-2)(p^j-1)/2),
whose coefficient is 1 modulo p. Therefore any output residue c has a unique index residue t lifted one p-adic digit at a time; take x=0.

**Case II, p does not divide k-2 and v=0 (mod q).** Take x=z=0 in x²+v=A z² and set t=h.

**Case III, A is a square modulo p, or v is a unit modulo p.** The equation x²+v=A z² has a nonsingular solution modulo p. When v is a unit, the sets {x²:x in F_p} and {A z²-v:z in F_p} each have (p+1)/2 members and therefore intersect; at any common point x,z are not both zero because v is nonzero. When v=0 mod p and A is a square, take any nonzero x with z²=A^(-1)x². A nonzero partial derivative (2x or -2Az) allows Hensel lifting the solution to every p^n. Finally take t=z+h.

**Case IV, A nonsquare, v nonzero with even valuation e=2r<n.** Divide v=p^(2r)u, with u a unit. The same pigeonhole construction solves X²+u=A Z² modulo p, with nonsingular lift to modulus p^(n-2r). Set x=p^r X and z=p^r Z; these solve x²+v=A z² mod p^n. Again t=z+h.

These cases exhaust all parameters outside the obstruction. QED.

## Consequences

1. **Full odd-prime-power completeness:** No further odd-prime-power parameter obstruction exists beyond the valuation/nonresidue criterion, irrespective of exponent.
2. **Higher-order first detection:** If v_p(D)=3 and A is nonsquare, local triples are permitted modulo p³ but impossible modulo p⁴. Example: k=3,c=64 gives D=513=3³·19, so 3³ is admissible and 3⁴ is not.
3. **CRT for finite odd moduli:** For an odd composite modulus M, compatibility at every prime-power factor is equivalent to compatibility modulo M by coordinatewise Chinese remainder lifting. This gives a complete decision procedure for any specified odd M.
4. **Exact positive-index integer solutions remain a separate question:** The constructed diagonal local triples have exact integer entries, but the pair outputs are only congruent to polygonal numbers; no global exact equations follow.
5. **No inference at p=2:** The 2-adic classification remains a separate WP08 result and must not be hidden inside an odd-prime argument.

## Executable evidence

Producer: research/figurate_wp09_odd_prime_power_complete.py

Independent tests: tests/test_figurate_wp09_odd_prime_power_complete.py

From repository root:

    python3 -m unittest -v tests.test_figurate_wp09_odd_prime_power_complete
    python3 -m research.figurate_wp09_odd_prime_power_complete --prime 3 --exponent 4 --audit
    python3 -m research.figurate_wp09_odd_prime_power_complete --prime 3 --exponent 4 --order 3 --offset 64

Producer returns an explicit modular entry/index witness when compatible, and no witness when obstructed. Tests include independent direct polynomial output and full **all-entry** congruence scans at small prime powers, exactly matching the diagonal constructor, plus higher-power cases, signed offsets, invalid inputs, period lifting, and exact positive distinct representatives.

**Boundary:** Internal proof and independently coded arithmetic controls are not external theorem certification. Novelty relative to the full literature has not been established; WP05 source-fidelity remains separate. Source proof does not claim local-to-global exact integer realization, arbitrary two-adic completion, or Types A/C.
