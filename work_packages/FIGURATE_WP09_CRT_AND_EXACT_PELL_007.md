# FIGURATE WP09-007 — all-place local assembly and exact integer Type B families

**Governance:** bounded internal mathematics under [WP09 #3145](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145). The theorem deliberately separates finite-modulus congruence solutions from **exact positive-integer** tuple constructions. Neither external novelty nor MATHCERT certification is asserted.

## I. Local compatibility at an arbitrary finite modulus

Let k>=3, c any integer, and

    P_k(t) = t + (k-2)t(t-1)/2.

For any M>=1 factor M=2^e product(p_i^n_i), with distinct odd primes p_i. A triple of entry remainders a,b,d with index remainders r,s,t solves

    ab+c=P_k(r), ad+c=P_k(s), bd+c=P_k(t) (mod M)

**if and only if** one triple exists for every prime-power component. This is a logical equivalence, not a statistical independence assumption: the forward direction is reduction, and the reverse uses ordinary coordinatewise Chinese remainder theorem (CRT) on each of the **six** residue variables. Equal entry residues are allowed, since representatives a+M, b+2M, d+3M can always be made distinct and positive. Polygonal index residues can likewise have positive representatives. All resulting equations are still only congruences.

The odd-prime-power component is determined **completely** by the previously protected [WP09-006 theorem](FIGURATE_WP09_ALL_ODD_PRIME_POWERS_COMPLETE_006.md): for odd p, set

    D=8(k-2)c+(k-4)^2.

A p^n obstruction exists precisely if p does not divide k-2, (k-2)/2 is a quadratic nonresidue modulo p, and the p-adic valuation of D is odd and <n. Otherwise the theorem produces a common entry residue and polygonal index residue.

The binary component is **not** silently replaced by the odd-prime theorem. If 4 does not divide k, WP08 proves every binary output is represented. If k is 4 mod16, WP08 constructs a **single fixed positive integer triple** passing every 2-power local test for each c. For the remaining orders, WP08's square normal form is a necessary-and-sufficient membership test at each finite binary exponent:

    k=4h: A=k/2-1, Q=k/4-1;
    z is k-gonal mod 2^e iff A*z+Q^2 is a square mod 2^e.

It decides a finite binary exponent by checking all three pair products; it is **not yet** a complete per-offset classification valid at all binary exponents for the nonuniform order classes. The executable constructor intentionally caps exhaustive binary exponent at 8; lack of a witness beyond that execution bound is never reported as mathematical nonexistence.

**Finite exceptional-prime sieve.** For fixed k,c, an odd prime can obstruct some power only if it divides nonzero D to odd valuation, is not a divisor of k-2, and has nonsquare (k-2)/2. Thus **all odd-prime obstructions are detected by factoring D** and testing finitely many primes. If D=0, no odd-prime obstruction exists. The binary component remains separately governed by WP08. An odd prime with odd valuation 2r+1 first blocks the modulus p^(2r+2), although every lower power remains locally compatible.

The executable CRT constructor [research/figurate_wp09_crt_exact_families.py](../research/figurate_wp09_crt_exact_families.py) verifies all three congruences after assembling entry and index residues. It gives a finite-modulus decision for any odd modulus and for even moduli with binary exponent at most 8.

## II. Exact Type B solutions for EVERY offset at square order k=4

Fix any integer c. Choose an integer t large enough that all following entries and indices are positive, with entries pairwise distinct:

    a=1, b=t^2-c, d=(t+1)^2-c.

Then, exactly in the ordinary integers,

    ab+c=t^2=P_4(t),
    ad+c=(t+1)^2=P_4(t+1),
    bd+c=(t(t+1)-c)^2=P_4(t(t+1)-c).

The last identity follows by expanding both sides. Taking t>=abs(c)+3 suffices for positivity and distinctness. Hence **for every integer offset c there are infinitely many exact square-output Type B triples**. The construction is the classical Euler regular extension and is NOT claimed as original.

This proves a strong positive-integer existence result, not merely everywhere-local compatibility.

## III. An infinite family of exact 20-gonal Type B triples at offset c=2

The protected WP08 work established that (k,c)=(20,2) has a fixed triple (1,242,375) passing all powers-of-two congruences but not the exact Type B equations. Here we exhibit genuine solutions for the **same** k and c, including infinitely many with a=1 and b=18.

For order 20 the polygonal polynomial is

    P_20(t)=9t^2-8t,

with square completion

    9P_20(t)+16=(9t-4)^2.

Fix a=1,b=18, and write d=P_20(s)-2. The first two pair equations are exact:

    ab+2=20=P_20(2),
    ad+2=P_20(s).

The third equation bd+2=P_20(t) becomes

    P_20(t)=18P_20(s)-34.

Set S=9s-4 and T=9t-4. Using the completed square, this is **equivalent** to the generalized Pell equation

    T^2-18S^2=-578,

together with S=T=-4 modulo 9 and positive indices s,t. The seed

    (S,T)=(347,1472), (s,t)=(39,164)

satisfies the Pell equation and the index congruences. Therefore

    (a,b,d)=(1,18,13375), (r,s,t)=(2,39,164)

is an exact positive-integer Type B triple, with three outputs

    20, 13377, 240752.

To construct infinitely many, apply the integral linear map

    T_next=17T+72S,
    S_next=4T+17S

**18 times** per family step. Its determinant equals 1, it preserves T^2-18S^2 because 17^2-18*4^2=1, and its 18th power is the identity matrix modulo 9. Consequently the seed congruences S=T=-4 mod9 persist. Every step strictly increases positive T and S, so it yields strictly increasing positive integral s,t and d. Every resulting triple satisfies all three exact equations.

This moves k=20,c=2 from *binary-only local consistency* to **infinite global exact realizability**. It is a genuine addition to the GCL programme evidence, but it does not establish newness over the literature: Pell recurrences and regular Diophantine constructions are classical.

## IV. Mathematical boundary and next frontier

- Every exact positive integer Type B triple is compatible at every finite modulus, by reduction.
- Compatibility modulo every finite modulus allows residue/index witnesses to **depend on the modulus**. CRT does not produce one fixed integer triple with all exact equations.
- The prime-power theorem and the binary component decide local existence; the exact Euler/Pell families establish global existence for specific order/offset classes.
- Nothing here proves that all everywhere-locally-compatible (k,c) admit an exact tuple. Nor does it give a global nonexistence counterexample (an everywhere-local pair with no exact integer triple). That question is the next substantive Diophantine obligation.
- The 2025 WP05 primary-source fidelity issue and external novelty/certification reviews remain independent of routine mathematical producer admission.

**Executable source:** research/figurate_wp09_crt_exact_families.py. The independent regression file publication for this tranche was explicitly platform-denied; retain that **operation-specific hold**, perform independent ephemeral tests, and do not mislabel the missing committed tests as green CI mathematical verification.
