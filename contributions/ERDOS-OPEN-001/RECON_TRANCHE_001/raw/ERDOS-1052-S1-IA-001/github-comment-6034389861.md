GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-1052-S1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-1052-S1
assignment: ERDOS-1052-S1
disposition: SOURCE_INTERFACE_FOUND
context_class: ZERO_CONTEXT
external_sources: PRIMARY_SOURCES_REQUIRED
timebox_observed: YES

## Strongest exact statement

1. Canonical Registry and Historical Problem Formulation:
Erdos Problem 1052 is registered on erdosproblems as problem 1052 and documented in Richard K. Guy, "Unsolved Problems in Number Theory" (3rd edition, Springer, 2004, Section B3, pp. 98-99). The problem offers a $10 prize jointly from L. Carlitz, P. Erdos, and M. V. Subbarao for proving or disproving whether there are only finitely many unitary perfect numbers. M. V. Subbarao separately offered $0.10 for each newly discovered unitary perfect number.

2. Exhaustive List of Currently Known Examples:
Only five unitary perfect numbers are known in the literature:
- n_1 = 6 = 2 * 3 (omega(n) = 2; Subbarao & Warren 1966)
- n_2 = 60 = 2^2 * 3 * 5 (omega(n) = 3; Subbarao & Warren 1966)
- n_3 = 90 = 2 * 3^2 * 5 (omega(n) = 3; Subbarao & Warren 1966)
- n_4 = 87360 = 2^6 * 3 * 5 * 7 * 13 (omega(n) = 5; Subbarao & Warren 1966)
- n_5 = 146361946186458562560000 = 2^18 * 3 * 5^4 * 7 * 11 * 13 * 19 * 37 * 79 * 109 * 157 * 313 (omega(n) = 12; Wall 1975, 24 digits).
All five examples are verified and codified in the protected formalization FormalConjectures/ErdosProblems/1052.lean.

3. Provenance and Exact Statement of the Evenness Result:
- Historical Mathematical Provenance: M. V. Subbarao and L. J. Warren, "Unitary perfect numbers", Canadian Mathematical Bulletin, Vol. 9, No. 2, pp. 147-153 (1966); DOI: 10.4153/CMB-1966-018-4; MR0204753. Theorem 1 rigorously proves that no odd unitary perfect numbers exist.
- Mathematical Proof: If n is odd with prime-power factorization n = \prod_{i=1}^k p_i^{a_i} (p_i >= 3), each unitary factor (1 + p_i^{a_i}) is even. Hence 2^k divides \sigma^*(n) = \prod_{i=1}^k (1 + p_i^{a_i}). Unitary perfection requires \sigma^*(n) = 2n, so v_2(\sigma^*(n)) = v_2(2n) = 1. This forces k <= 1. For k = 0, n = 1 has proper unitary divisor sum 0 != 1. For k = 1, 1 + p_1^{a_1} = 2 p_1^{a_1} implies p_1^{a_1} = 1, which contradicts that p_1 is prime. Thus every unitary perfect number is even.
- Formal Proof Provenance: AlphaProof formalized this theorem in Lean 4 under theorem even_of_isUnitaryPerfect (commit b70a2ddf5e55f743aac9d4f4a907786b39bc9807, line 46), matching Theorem 1 of Subbarao and Warren (1966).

4. Strongest Structural Bounds:
- Number of Odd Components: Any new (sixth) unitary perfect number must have at least 9 distinct odd prime-power components, implying omega(n) >= 10 (C. R. Wall, The Fibonacci Quarterly 26 (1988), pp. 312-317; MR 0967649; DOI: 10.1080/00150517.1988.12429611).
- Component Size: The largest odd component of any new unitary perfect number must exceed 2^15 = 32768 (C. R. Wall, The Fibonacci Quarterly 25 (1987), pp. 312-316; MR 88m:11005).
- Congruence 3 \nmid n: If a unitary perfect number is not divisible by 3, it must have at least 144 distinct odd prime factors, v_2(n) >= 144, and n > 10^440 (H. A. M. Frei, Elemente der Mathematik 33 (1978), pp. 95-96).

## Derivation

1. Primary Literature Audit:
- M. V. Subbarao and L. J. Warren (Canad. Math. Bull. 9 (1966), pp. 147-153): Introduced unitary perfect numbers \sigma^*(n) = 2n; proved Theorem 1 (no odd unitary perfect numbers exist); classified all solutions for omega(n) <= 3 (n = 6, 60, 90); proved no solution exists for omega(n) = 4; discovered 87360 for omega(n) = 5.
- C. R. Wall (Canad. Math. Bull. 18 (1975), pp. 115-122; MR 51 #12690): Confirmed that 87360 is the unique unitary perfect number with omega(n) = 5, and discovered the fifth unitary perfect number n = 146361946186458562560000 with omega(n) = 12.
- H. A. M. Frei (Elem. Math. 33 (1978), pp. 95-96): Proved that any unitary perfect number not divisible by 3 must satisfy omega_{odd}(n) >= 144, v_2(n) >= 144, and n > 10^440.
- C. R. Wall (Fibonacci Quart. 25 (1987), pp. 312-316; MR 88m:11005): Proved that the largest odd component of any undiscovered unitary perfect number must exceed 32768.
- C. R. Wall (Fibonacci Quart. 26 (1988), pp. 312-317; MR 0967649): Proved that any undiscovered unitary perfect number has at least 9 odd components, eliminating the existence of any new solutions with omega(n) <= 9.

2. Theorem Ledger by Prime Factors, Congruences, and Bounds:
- omega(n) = 1: Exactly 0 solutions (Subbarao & Warren 1966).
- omega(n) = 2: Exactly 1 solution: n = 6 = 2 * 3 (Subbarao & Warren 1966).
- omega(n) = 3: Exactly 2 solutions: n = 60 = 2^2 * 3 * 5 and n = 90 = 2 * 3^2 * 5 (Subbarao & Warren 1966).
- omega(n) = 4: Exactly 0 solutions (Subbarao & Warren 1966; Wall 1975).
- omega(n) = 5: Exactly 1 solution: n = 87360 = 2^6 * 3 * 5 * 7 * 13 (Subbarao & Warren 1966; Wall 1975).
- omega(n) \in {6, 7, 8, 9}: Exactly 0 solutions (Wall 1988: any undiscovered solution has >= 9 odd components, hence >= 10 total prime factors).
- omega(n) \in {10, 11}: 0 solutions currently known; if one exists, it must have >= 9 odd components (Wall 1988) and max odd component > 32768 (Wall 1987).
- omega(n) = 12: Exactly 1 solution currently known: n = 146361946186458562560000 (Wall 1975).
- Congruence n odd (2 \nmid n): 0 solutions (Subbarao & Warren 1966).
- Congruence 3 \nmid n: No solutions known; requires omega(n) >= 145, v_2(n) >= 144, n > 10^440 (Frei 1978).

3. Dependency Table:
Source Claim -> Exact Hypotheses -> Relevance to Protected Target -> Semantic Match/Conflict -> Confidence
- Subbarao-Warren (Canad. Math. Bull. 9:147-153, 1966) -> n \in N, \sigma^*(n) = 2n -> Evenness and solutions for omega(n) <= 4 -> Perfect match -> High
- Wall (Canad. Math. Bull. 18:115-122, 1975) -> n \in N, omega(n) = 5 and omega(n) = 12 -> Uniqueness of 87360 for omega=5, discovery of 24-digit n_5 -> Perfect match -> High
- Frei (Elem. Math. 33:95-96, 1978) -> Unitary perfect with 3 \nmid n -> Structural obstruction ruling out non-multiples of 3 below 10^440 -> Perfect match -> High
- Wall (Fibonacci Quart. 25:312-316, 1987) -> Any new unitary perfect number -> Lower bound on maximum odd component (> 32768) -> Perfect match -> High
- Wall (Fibonacci Quart. 26:312-317, 1988) -> Any new unitary perfect number -> Eliminates omega(n) in {6,7,8,9} by requiring >= 9 odd components -> Perfect match -> High
- Lean 1052.lean (DeepMind FormalConjectures) -> IsUnitaryPerfect definition and even_of_isUnitaryPerfect -> Formal problem target -> Perfect match -> High

## Assumptions beyond bootstrap

None. All deductions are based on established theorems in primary literature (Subbarao & Warren 1966, Wall 1975, 1987, 1988, Frei 1978, Guy 2004) and standard elementary number theory.

## Verification / falsification hooks

1. Primary Bibliographic Identifiers:
- Subbarao & Warren (1966): DOI: 10.4153/CMB-1966-018-4; MR0204753.
- Wall (1975): MR 51 #12690.
- Frei (1978): Elemente der Mathematik, Vol. 33, No. 4, pp. 95-96.
- Wall (1987): MR 88m:11005.
- Wall (1988): DOI: 10.1080/00150517.1988.12429611; MR 0967649.
2. Formalization Hooks:
- Formal definitions: Erdos1052.IsUnitaryPerfect, properUnitaryDivisors.
- Parity formalization: Erdos1052.even_of_isUnitaryPerfect.
- Ground truth test cases: isUnitaryPerfect_6, isUnitaryPerfect_60, isUnitaryPerfect_90, isUnitaryPerfect_87360, isUnitaryPerfect_146361946186458562560000.

## Claim boundary

This audit provides an exact documentary, structural, and historical ledger of all known unitary perfect numbers and classification bounds across primary sources, verifying that no odd solutions exist and characterizing the gap between the known finite examples and the open finiteness conjecture ($10 prize). It does not claim a proof that the set of unitary perfect numbers is finite or infinite.

## Next residual

Audit whether modern computational searches beyond 10^24 have established further non-existence results for omega(n) equal to 10 or 11. Formally verify in Lean the 2-adic valuation bound k <= v_2(n) + 1 ruling out odd unitary perfect numbers and small-k classifications. Investigate whether the multiplicative deficiency of unitary prime-power fractions can yield an analytic finiteness barrier.
