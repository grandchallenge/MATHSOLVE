GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-470-A1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-470-A1
assignment: ERDOS-470-A1
disposition: COUNTEREXAMPLE
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

Two tempting bridges are invalid, and one multiplicative construction already fails at the smallest protected example.

First, positive density of a divisibility-ordered class does not imply infinitely many primitive elements. Abstractly, the set
[
A={70m:mge 1}
]
has natural density (1/70), but under the usual divisibility notion of “primitive” (no smaller member of (A) properly divides it), its only primitive member is (70). Therefore any inference

“positive density of weird numbers (Rightarrow) infinitely many primitive weird numbers”

requires a theorem using special structure of weirdness, not density alone.

Second, multiplication does not preserve weirdness even at the first protected weird number. The protected packet allows use of the fact that (70) is weird. But
[
140=2cdot 70
]
is pseudoperfect because its proper divisors include
[
70,35,20,10,5
]
and
[
70+35+20+10+5=140.
]
Moreover (140) remains abundant:
[
sigma(140)=(1+2+4)(1+5)(1+7)=336>280.
]
Hence multiplying a weird number by (2) can keep abundance while destroying the non-pseudoperfect condition. Any primitive-producing or density-producing argument based on unrestricted multiplication is therefore unsafe.

Finally, parity does not follow from abundance. The odd number
[
945=3^3cdot 5cdot 7
]
is abundant since
[
sigma(945)=(1+3+9+27)(1+5)(1+7)=1920>1890.
]
It is nevertheless pseudoperfect: the sum of all proper divisors is (975), and (15+9+5+1=30), so the complementary set of proper divisors sums (975-30=945). Thus (945) is not weird, but it proves that a parity pruning rule cannot be justified from abundance alone. The absence of known odd examples is therefore not a mathematical exclusion criterion.

## Derivation

The density countermodel is purely logical. A set may have positive density because it contains all multiples of finitely many primitive seeds. Positive density supplies no lower bound on the number of divisibility-minimal elements.

For the multiplicative failure, the protected fact gives weirdness of (70). The displayed subset of proper divisors of (140) is an exact pseudoperfect certificate, so (140) is not weird regardless of any other property. The divisor-sum computation shows the failure is specifically in non-pseudoperfectness, not abundance.

For the parity stress test, the divisor-sum factorization for (945) is direct from its prime factorization. Its proper divisors sum to (1920-945=975). Since (1,5,9,15) are proper divisors totaling (30), all remaining proper divisors total (945), which is an explicit pseudoperfect certificate.

## Assumptions beyond bootstrap

Only the standard definitions:
- abundant: (sigma(n)>2n);
- pseudoperfect: some subset of proper divisors sums to (n);
- weird: abundant and not pseudoperfect;
- primitive in the divisibility sense: no proper divisor in the same target class.

No external literature, sibling return, unpublished project note, or later repository state was used.

## Verification / falsification hooks

1. Check the five divisors (70,35,20,10,5) of (140) and their sum (140).
2. Check (sigma(140)=336).
3. Check (sigma(945)=1920).
4. List the proper divisors of (945); their total is (975), and removing (1,5,9,15) leaves a subset summing (945).
5. Any proposed theorem “multiples of weird numbers are weird” is immediately falsified by (70mapsto140).
6. Any proposed theorem deriving infinitely many primitive members from positive density alone is falsified by the class of multiples of (70).

## Claim boundary

This does not resolve either registered open part. It does not prove existence or nonexistence of odd weird numbers, and it does not prove finiteness or infinitude of primitive weird numbers.

It eliminates three unsafe proof heuristics:
- density alone cannot force infinitely many primitive weird numbers;
- unrestricted multiplication does not preserve weirdness;
- odd candidates cannot be pruned merely from the abundance condition or from the empirical evenness of known examples.

## Next residual

For primitive weird numbers, the next safe question is to identify a structure theorem showing that positive density of weird numbers cannot be supported by multiples or descendants of finitely many primitive weird seeds. Without such a theorem, density is orthogonal to primitive infinitude.

For odd weird numbers, any valid pruning must use a proved necessary condition involving the non-pseudoperfect constraint, not parity of known examples and not abundance alone.