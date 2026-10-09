GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-470-S2-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-470-S2
assignment: ERDOS-470-S2
disposition: SOURCE_INTERFACE_FOUND
context_class: ZERO_CONTEXT
external_sources: PRIMARY_SOURCES_REQUIRED
timebox_observed: YES

## Strongest exact statement
1. Reproducible Evidence Package for Unrestricted N < 10^21 Exclusion:
The computational exclusion of odd weird numbers below 10^21 established in Wenjie Fang (2022) is source-locked and reducible to a bounded, verifiable audit package:
- Primary Source: Wenjie Fang, "Searching on the boundary of abundance for odd weird numbers", arXiv:2207.12906v1 (2022).
- Primary Implementation: GitHub repository fwjmath/ows-data, pinned commit 88d22faf46400f0050287c3c32c9a807ca3b1340. The core engine is wobt-smart.cpp (GPL-3.0), utilizing MPIR/GMP, GCC __int128, and embedded Nicely (2012) primality routines.
- Published Workunit Data: The batch data-1e21/ in fwjmath/ows-data contains all partitioned workunit files, intermediate checkpoint logs, and result headers executed during the volunteer distributed search on yoyo@home (documented in Fang and Beckert, Journal of Grid Computing 16 (2018), 647-662, DOI 10.1007/s10723-017-9411-5).
- Completeness Theorem: Theorem 3.4 together with Proposition 3.1 in Fang (2022) proves that any minimal odd weird number must be an odd primitive abundant number (OPAN) and that the tree search over the boundary of abundance visits all potential OPANs below 10^21, safely pruning all subtrees whose root is pseudoperfect or whose deficiency cannot be overcome.
- Bounded Replay Protocol: Verification does not require repeating 80 core-years of volunteer compute. Instead, verification operates on three tiers:
  (a) Structural Cover Audit: Check that the union of prime-factor search prefixes in data-1e21/ forms an exact disjoint cover of the root search space below 10^21;
  (b) Deterministic Checksum Verification: Replay wobt-smart.cpp on a deterministic pseudo-random or boundary sample of workunits to match the published 8-field checksums and termination codes ("c");
  (c) Independent Subset-Sum Spot-Checking: For each pseudoperfect number encountered along sampled branches, independently verify that the certificate subset S of proper divisors sums to the candidate integer (O(|S|) integer operations).

2. Exact Source Lock for the Distinct Prime Divisors Restriction:
The necessary condition that any odd weird number must have at least 6 distinct prime divisors is source-locked to:
- Primary Academic Source: Jacob P. Liddy, "An algorithm to determine all odd primitive abundant numbers with d prime divisors", Williams Honors College Honors Research Projects, Report 728, University of Akron (Spring 2018), supervised by Jeffrey M. Riedl. IdeaExchange@UAkron report 728.
- Corroborating Abstract: Jacob P. Liddy and Jeffrey M. Riedl, AMS Joint Mathematics Meetings (JMM 2019), Abstract 1145-05-127.
- Mathematical Theorem: Dickson (1913) proved finiteness of OPANs for any fixed number of prime factors d. For d <= 2, odd abundant numbers do not exist because sigma(p^a)/p^a * sigma(q^b)/q^b < (3/2)(5/4) = 15/8 < 2. Diciunas (2017) and Liddy-Riedl (2018) enumerated all OPANs with d in {3, 4, 5} and proved each is pseudoperfect. Because any multiple of a pseudoperfect number is pseudoperfect, and any odd abundant number must have an OPAN divisor, any odd abundant number with at most 5 distinct prime factors is pseudoperfect and therefore cannot be weird. Consequently, every odd weird number must have at least 6 distinct prime factors.

## Derivation

1. Completeness Assumptions and Pruning Mechanics (Fang 2022):
- Let N be a positive integer. sigma(N) denotes the sum of positive divisors of N.
- Abundance index is I(N) = sigma(N)/N. N is abundant if I(N) > 2, deficient if I(N) < 2, and perfect if I(N) = 2.
- A number N is pseudoperfect if there exists a subset S of proper divisors of N such that sum_{d in S} d = N.
- N is weird if N is abundant and not pseudoperfect.
- Proposition 3.1: If N is the smallest odd weird number, then N is primitive abundant (i.e. every proper divisor of N is deficient).
  Proof: Suppose N has an abundant proper divisor M < N. Since N is the smallest odd weird number, M cannot be weird. Thus M is pseudoperfect: there exists S subseteq D(M) \\ {M} summing to M. Multiplying every element of S by N/M gives a set S' = {d * (N/M) : d in S} of proper divisors of N summing to M * (N/M) = N. Thus N would be pseudoperfect, contradicting weirdness.
- Tree Decomposition: Natural numbers are searched via prime-factorization trees T where edges correspond to appending prime powers p_k^{a_k} with p_k > p_{k-1}.
- Abundance Boundary Pruning:
  If a node M has I(M) >= 2, we test whether M is pseudoperfect via an exact subset-sum routine. If M is pseudoperfect, by the Proposition 3.1 argument no multiple or descendant of M can be a minimal odd weird number; hence the entire subtree rooted at M is pruned.
  If I(M) < 2, an upper bound on abundance index achievable by descendants is given by I(M) * prod_{p > p_k} (p / (p - 1)). If this upper bound is < 2, no descendant can be abundant; hence the subtree is pruned.
- Theorem 3.4: Under these pruning rules, the search visits every minimal OPAN candidate below the target bound (10^21). Since no unpruned candidate was weird, no odd weird number exists below 10^21.

2. Structure of the Reproducible Replay Package:
- The package requires:
  (1) Artifact repository fwjmath/ows-data at commit 88d22faf46400f0050287c3c32c9a807ca3b1340.
  (2) Source engine wobt-smart.cpp compiled with g++ -O3 against MPIR/GMP.
  (3) Verification of data-1e21/ workunit logs:
      Line 1: Upper bound 1000000000000000000000 (10^21)
      Line 2: Lower bound
      Line 4: Recursion depth
      Line 5: Candidates checked
      Line 6: Workpoint
      Line 7: Primepoint
      Line 8: Checksum
      Line 9: Remaining sections
      Prime factorization list: index, power, value
      Trailer: "c" indicating complete subtree verified with no odd weird witness.

3. Exact Mechanism of the Six-Prime-Factor Barrier (Liddy-Riedl 2018):
- Let Omega_distinct(N) denote the number of distinct prime factors of N.
- For odd N, if Omega_distinct(N) = 1, then N = p^a, so I(N) = (p^{a+1}-1)/(p^a(p-1)) < p/(p-1) <= 3/2 < 2.
- If Omega_distinct(N) = 2, then N = p^a q^b with odd primes 3 <= p < q, so I(N) < (p/(p-1))*(q/(q-1)) <= (3/2)*(5/4) = 15/8 = 1.875 < 2.
- Thus no odd abundant number exists with <= 2 distinct prime factors.
- For Omega_distinct(N) in {3, 4, 5}:
  Diciunas (2017) and Liddy-Riedl (2018) exhaustively determined all OPANs with 3, 4, and 5 distinct prime factors.
  In all cases, every such OPAN M satisfies pseudoperfection: there exists S subseteq D(M) \\ {M} with sum_{d in S} d = M.
- Multiplicative Heredity of Pseudoperfection:
  If M is pseudoperfect, any integer multiple kM is also pseudoperfect: sum_{d in S} (kd) = k * sum_{d in S} d = kM.
- If N is an odd weird number, N must be abundant, so N is a multiple of some OPAN M.
  If Omega_distinct(M) <= 5, M is pseudoperfect, which forces N to be pseudoperfect, contradicting that N is weird.
  Therefore, every OPAN divisor of N must have Omega_distinct >= 6.
  Since M divides N, Omega_distinct(N) >= Omega_distinct(M) >= 6.

## Assumptions beyond bootstrap
No ad hoc assumptions are introduced beyond standard ZFC arithmetic and the audited primary publications:
- Fang (arXiv:2207.12906v1, 2022) for the 10^21 boundary-of-abundance search algorithm and volunteer computing results.
- Liddy (Honors Project 728, University of Akron, 2018) and Liddy-Riedl (AMS Abstract 1145-05-127, 2019) for the classification of OPANs with up to 5 prime factors and the resulting 6-prime-factor obstruction.
- Dickson (Amer. J. Math. 35 (1913), 413-422) for finiteness of OPANs per fixed prime factor count d.
- No Continuum Hypothesis, large cardinal, or non-constructive axioms are invoked.

## Verification / falsification hooks
1. Fang Code and Data Source Lock:
   Inspect GitHub repository fwjmath/ows-data, tree commit 88d22faf46400f0050287c3c32c9a807ca3b1340.
   Verify that wobt-smart.cpp compiles cleanly under g++ with -D__USING_BOINC disabled for standalone CLI operation.
2. Workunit Integrity Audit:
   Run an automated script across all files in data-1e21/ to ensure:
   (a) Every result file ends with "c" (no "t" or anomaly);
   (b) The collection of initial factor prefixes partitions the search interval without gaps;
   (c) Re-run wobt-smart.cpp on sample input files (e.g. initial 5 workunits, 5 median workunits, 5 boundary workunits) and verify bit-exact agreement with published Checksum, Workpoint, and Primepoint values.
3. Liddy-Riedl Citation Pin:
   Verify Report 728 in IdeaExchange@UAkron: Jacob P. Liddy, "An algorithm to determine all odd primitive abundant numbers with d prime divisors" (2018), and AMS JMM Abstract 1145-05-127 (Baltimore, Jan 2019).
4. Falsification Criterion:
   Any valid odd integer N < 10^21 such that I(N) > 2 and no subset of proper divisors sums to N would immediately falsify Theorem 1.1 and the integrity of the search data.

## Claim boundary
This return designs and locks the reproducible verification interface and source references for the unrestricted N < 10^21 odd-weird exclusion and pins the 6-prime-factor theorem body.
It does not claim to have re-executed the entire 80 core-years of distributed computation, does not certify that no odd weird number exists globally, and does not assert unconditional infinitude of primitive weird numbers.

## Next residual
Implement a lightweight independent Python/Lean validator that executes the tier-(a) prefix cover check and tier-(c) subset-sum certificate spot-checks on the published fwjmath/ows-data data-1e21 batch.
