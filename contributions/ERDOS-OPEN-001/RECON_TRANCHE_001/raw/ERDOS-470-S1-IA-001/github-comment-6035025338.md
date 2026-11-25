GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-470-S1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-470-S1
assignment: ERDOS-470-S1
disposition: SOURCE_INTERFACE_FOUND
context_class: ZERO_CONTEXT
external_sources: PRIMARY_SOURCES_REQUIRED
timebox_observed: YES

## Strongest exact statement

The audited primary-source record separates the two protected open parts cleanly.

1. Odd weird numbers: Wenjie Fang, "Searching on the boundary of abundance for odd weird numbers", arXiv:2207.12906v1 (2022), Theorems 1.1 and 1.2, gives an exhaustive computational exclusion of odd weird numbers below 10^21, and separately excludes odd weird numbers below 10^28 under the additional hypothesis that abundance A(N)=sigma(N)-2N is <10^14. The unrestricted statement is therefore only the 10^21 bound. Fang Section 3 proves the search completeness claim for the stated upper bound (Theorem 3.4); Section 4 reports the implementation and roughly 80 core-years for Theorem 1.1 and 150 core-years for Theorem 1.2. This audit did not independently replay the computation.

2. Primitive weird numbers: Giuseppe Melfi, "On the conditional infiniteness of primitive weird numbers", Journal of Number Theory 147 (2015), 508-514, DOI 10.1016/j.jnt.2014.07.024, MR 3276337, Theorem 1 p.509 and conclusion pp.512-513, proves a large explicit family of primitive weird numbers and shows that if p_(n+1)-p_n < 0.1 sqrt(p_n) for all sufficiently large n, then there are infinitely many primitive weird numbers of the form 2^k p q. Melfi explicitly states that unconditional infinitude was not proved. Thus the audited source interface supports conditional infinitude, not unconditional resolution.

3. The original density result is semantically orthogonal to both open parts. S. J. Benkoski and P. Erdős, "On Weird and Pseudoperfect Numbers", Mathematics of Computation 28(126) (1974), 617-623, DOI 10.1090/S0025-5718-1974-0347726-9, MR 0347726, Theorem 5 p.622, proves positive density of weird numbers. The same page notes that if n is weird and p>sigma(n) is prime then pn is weird. This mechanism can generate many nonprimitive weird multiples, so positive density does not imply infinitely many primitive weird numbers and gives no odd example. Sidney Kravitz's corrigendum, Mathematics of Computation 29(130) (1975), p.673, DOI 10.1090/S0025-5718-1975-0360452-6, corrects only a Table I entry (539774 to 539744), not these theorem statements.

4. Structural restrictions are available. Douglas E. Iannucci, "On primitive weird numbers of the form 2^k p q", arXiv:1504.02761v1 (2015), Section 3, gives necessary and sufficient conditions for the 2^k p q family. If n=2^k p q is weird, p<q are odd primes, M=2^(k+1)-1, and a=sigma(n)-2n, then a>M, M<p<2M, 4 divides a, and M<a<M(M+1); moreover (p-M)(q-M)=M(M+1)-a. Conversely, factoring d e=[M(M+1)-a]/4 and taking p=M+2d, q=M+2e prime, together with the stated subset-sum obstruction, yields weirdness. Iannucci also notes that every weird number of this form is primitive weird.

5. A general primitive interface is explicit in Gianluca Amato, Maximilian F. Hasler, Giuseppe Melfi, Maurizio Parton, "Primitive abundant and weird numbers with many prime factors", Journal of Number Theory 201 (2019), 436-459, DOI 10.1016/j.jnt.2019.02.027, arXiv:1802.07178v2. Proposition 4.1 states: n is primitive weird iff n is weird and primitive abundant. Their Theorem 4.7 proves that no primitive weird number with a quadratic-or-higher odd prime factor has Omega<7; at Omega=7 there is no example with two squared odd prime factors and none with a cubic-or-higher odd prime factor. The paper exhibits primitive weird numbers with Omega up to 16, including a 14712-digit example, but does not prove infinitude.

The canonical Erdős Problems #470 registry page, last edited 2026-01-18 and audited here on 2026-10-06, agrees with this interface: it still presents both questions as open, cites Melfi's conditional infinitude, Fang's 10^21 exclusion, and the Liddy-Riedl six-prime-divisor restriction. This registry check is status evidence, not MATHCERT authority.

## Derivation

Primary-source dependency table:

| source claim | exact hypotheses | relevance to protected target | semantic match/conflict | confidence |
|---|---|---|---|---|
| Benkoski-Erdős 1974, Theorem 5 p.622: weird numbers have positive density | weird = abundant and not pseudoperfect; proof starts from an existing weird n and propagates to suitable multiples nt | establishes abundance of weird numbers globally | MATCH for weirdness; DOES NOT ADDRESS oddness or primitive infinitude | HIGH |
| Benkoski-Erdős 1974 p.622: if n weird and prime p>sigma(n), then pn weird | n weird; p prime; p>sigma(n) | explains why density/infinitude can come from nonprimitive multiples | CONFLICT with any inference "positive density => infinitely many primitive weird" | HIGH |
| Fang 2022, Theorem 1.1 | odd N; exhaustive search N<10^21 | strongest unrestricted odd exclusion established in this audit | MATCH | HIGH as source claim; computation not independently replayed |
| Fang 2022, Theorem 1.2 | odd N<10^28 and A(N)<10^14 | stronger bounded search only under an abundance restriction | MATCH only with the extra hypothesis; cannot be promoted to unrestricted 10^28 exclusion | HIGH |
| Fang 2022, Proposition 3.1 | N is the smallest odd weird number | then N is odd primitive abundant | narrows any minimal counterexample to primitive-abundant search | MATCH; primitive abundant is not itself primitive weird without weirdness | HIGH |
| Liddy 2018 Honors Research Project 728; AMS JMM abstract 1145-05-127 | odd weird number | must have at least 6 distinct prime divisors | direct necessary factorization restriction | MATCH; exact theorem/page in the thesis could not be inspected because the repository PDF transport returned 403, so claim is anchored to the author's repository abstract and AMS abstract | MEDIUM-HIGH |
| Melfi 2015, Theorem 1 p.509 | k positive; a,b positive odd; p=2^(k+2)-a and q=2^(k+2)+b prime; b+3<a<2^((k-1)/2) | explicit infinite-family template for primitive weird candidates | MATCH; sufficient, not necessary | HIGH |
| Melfi 2015 p.509 | eventual prime-gap bound p_(n+1)-p_n<0.1 sqrt(p_n) | implies infinitely many primitive weird 2^k p q | MATCH only conditionally | HIGH |
| Iannucci 2015, Section 3 equations (2)-(5) | n=2^k p q weird; p<q odd primes; M=2^(k+1)-1 | exact divisibility and size restrictions: 4|a, M<a<M(M+1), M<p<2M | MATCH for this factorization class only | HIGH |
| Amato-Hasler-Melfi-Parton 2019, Proposition 4.1 | arbitrary positive integer n | primitive weird iff weird and primitive abundant | clean semantic bridge between weirdness and primitive-abundant enumeration | MATCH | HIGH |
| Amato-Hasler-Melfi-Parton 2019, Theorem 4.7 | primitive weird m with restrictions on Omega and multiplicities | excludes nonsquarefree odd-part patterns at small Omega | MATCH; not a general odd-weird exclusion | HIGH |

Terminology separation:
- abundant: sigma(n)>2n in the modern audited sources; Benkoski-Erdős use sigma(n)>=2n, but a perfect number is pseudoperfect via all proper divisors, so the convention difference does not create a weird-number mismatch.
- pseudoperfect/semiperfect: expressible as a sum of distinct proper divisors.
- weird: abundant and not pseudoperfect.
- primitive abundant: abundant with every proper divisor deficient.
- primitive weird: weird with no proper divisor weird; equivalently, by Amato et al. Proposition 4.1, weird and primitive abundant.
- positive density of weird numbers therefore cannot be conflated with either existence of odd weird numbers or infinitude of primitive weird numbers.

## Assumptions beyond bootstrap

No mathematical assumptions were added to the unconditional statements above.

Melfi's infinitude implication is explicitly conditional on an eventual prime-gap hypothesis p_(n+1)-p_n<0.1 sqrt(p_n). The separate 10^28 Fang exclusion explicitly assumes abundance <10^14. Neither condition is discharged here.

For the Liddy-Riedl restriction, the source record was available through the University of Akron repository metadata/abstract and the authors' AMS Joint Mathematics Meetings abstract; the thesis PDF itself was not retrievable in this audit, so no unsupported theorem/page number is asserted.

No claim of "current best known" is made beyond the dated source record. The exact statement is: among primary sources audited, Fang 2022 supplies the strongest unrestricted odd exclusion located, and the canonical registry as edited in 2026 still cites that bound.

## Verification / falsification hooks

1. Fang arXiv:2207.12906v1: verify Theorem 1.1, Theorem 1.2, Proposition 3.1, Theorem 3.4, and Section 4 implementation notes. Replaying the published source/data is the direct falsification route for the computational bounds.
2. Melfi DOI 10.1016/j.jnt.2014.07.024: verify Theorem 1 on p.509, the prime-gap implication on p.509, and the explicit statement on p.512 that unconditional infinitude was not proved.
3. Benkoski-Erdős DOI 10.1090/S0025-5718-1974-0347726-9: verify Theorem 5 and the prime-multiple statement on p.622. Check Kravitz corrigendum DOI 10.1090/S0025-5718-1975-0360452-6 for the table-only correction.
4. Iannucci arXiv:1504.02761v1: verify Section 3 equations (2)-(5), especially 4|a and M<a<M(M+1), under n=2^k p q weird.
5. Amato et al. DOI 10.1016/j.jnt.2019.02.027 / arXiv:1802.07178v2: verify Proposition 4.1 and Theorem 4.7.
6. Liddy, "An algorithm to determine all odd primitive abundant numbers with d prime divisors", Williams Honors College Honors Research Projects 728 (2018), and AMS JMM abstract 1145-05-127: obtain the thesis PDF independently and pin the exact internal theorem/page for the at-least-six-distinct-prime-divisors statement before promoting it to theorem-grade source lock.

## Claim boundary

This return is source evidence only.

It does not certify either Erdős #470 open part, does not claim that no odd weird number exists, does not claim unconditional infinitude of primitive weird numbers, and does not infer either statement from positive density. The 10^21 odd exclusion is a published computational result not independently replayed here. The 10^28 exclusion has the additional abundance <10^14 hypothesis. The Melfi infinitude result is conditional. Iannucci's congruence/divisibility restrictions apply specifically to weird numbers of the form 2^k p q.

## Next residual

For the odd branch, turn Fang's completeness proof plus released search code/data into a replayable certificate for the unrestricted N<10^21 exclusion, while separately importing the Liddy-Riedl theorem body to source-lock the at-least-six-distinct-prime-divisors restriction. For primitive infinitude, isolate the prime-distribution obligation behind Melfi's construction and either improve the required prime-location input or replace the 2^k p q construction so current prime-gap technology suffices.