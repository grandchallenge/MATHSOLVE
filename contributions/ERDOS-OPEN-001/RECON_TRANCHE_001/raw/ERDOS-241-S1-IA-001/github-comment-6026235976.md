GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-241-S1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-241-S1
assignment: ERDOS-241-S1
disposition: SOURCE_INTERFACE_FOUND
context_class: ZERO_CONTEXT
external_sources: PRIMARY_SOURCES_REQUIRED
timebox_observed: YES

## Strongest exact statement

The protected Green upper constant is stale.

Primary-source audit establishes the following chain for the strong B3 problem encoded in the protected packet.

1. Bose–Chowla: R. C. Bose and S. Chowla, "Theorems in the additive theory of numbers," Commentarii Mathematici Helvetici 37 (1962/63), 141–147, DOI 10.1007/BF02566968, MR0144877. Their B_r definition treats ordered-index representatives with i1 <= ... <= ir, so repeated summands are allowed; equality is trivial exactly up to permutation/multiset identity. Their prime-power construction gives the standard (1+o(1)) N^(1/r) lower scale.

2. Green: Ben Green, "The number of squares and B_h[g] sets," Acta Arithmetica 100 (2001), no. 4, 365–390, DOI 10.4064/aa100-4-6. Green defines B_h[g] representations with a_i in A and identifies representations differing only by ordering, again allowing repetitions. Theorem 17 gives
A(3,1,N) <= (7/2)^(1/3) N^(1/3)(1+o(1)),
whose leading constant is approximately 1.51829448594.

3. White: Ethan Patrick White, "An optimal L^2 autoconvolution inequality," Canadian Mathematical Bulletin 67(1) (2024), 108–121, DOI 10.4153/S0008439523000565, published online 5 July 2023. Theorem 1.1 proves
0.574636066 <= mu_2^2 <= 0.574642912.
Corollary 1.2 explicitly gives
sigma_3(1) <= (2 / 0.574636066)^(1/3),
hence the published B3 upper constant is at most approximately 1.51546428275. White states this improves the previous best B_h[g] upper bounds including (g,h)=(1,3). Therefore the protected Green constant is not current.

4. Rechnitzer: Andrew Rechnitzer, "The first 128 digits of an autoconvolution inequality," arXiv:2602.07292, submitted 7 February 2026, revised 10 February 2026, arXiv DOI 10.48550/arXiv.2602.07292. The paper rigorously pins nu_2^2 to 128 digits; in particular the displayed lower-bound prefix is
0.574639607151519592727255427527052971437026369373156611630876...
with interval width at most 1.2e-129. Rechnitzer explicitly improves the prior White/Green/Martin–O'Bryant autoconvolution bounds.

Combining Rechnitzer's rigorous lower bound with the same explicit White Corollary 1.2 formula yields the immediate primary-source-derived bound
sigma_3(1) <= (2 / 0.5746396071515195927...)^(1/3) < 1.515461169787.
This numerical B3 consequence is a direct substitution into White's proved corollary framework; I did not find an explicit B3 theorem statement in Rechnitzer's paper itself and therefore do not attribute that B3 inequality to Rechnitzer as a stated theorem.

Constant-gap ledger:
- Bose–Chowla lower scale: 1 times N^(1/3), asymptotically, strong B3/repeated-summand semantics.
- Green 2001 upper: (7/2)^(1/3) approximately 1.51829448594.
- White 2024 published upper: at most 1.51546428275.
- White + Rechnitzer 2026 rigorous autoconvolution substitution: less than 1.515461169787.

## Derivation

Semantic match: Green and White both define B_h[g] by representations a_1+...+a_h=x with a_i in A, with two representations regarded as the same only when they differ by ordering. No distinctness condition is imposed on the a_i, so repeated summands are admitted. This matches the protected strong-B3 multiset semantics.

Green's Theorem 17 is the protected 7/2 result. White's proof of Corollary 1.2 explicitly says the sigma_3(1) bound is obtained by reusing Green's method and replacing Green's autoconvolution input with White's improved lower bound mu_2^2 >= 0.574636066. Thus White is a theorem-level primary-source replacement for the protected constant.

Rechnitzer's 2026 preprint rigorously improves the lower bound on the same autoconvolution constant. Since White's displayed sigma_3(1) corollary is monotone in that lower bound, substitution of Rechnitzer's certified lower endpoint immediately sharpens the numerical constant to below 1.515461169787. This last step is a derived consequence of two primary sources, not a quotation or theorem-number claim about Rechnitzer.

I searched current primary-source channels for a later explicit strong-B3 upper-constant theorem and found no stronger explicit B3 theorem than White, nor a later primary source invalidating the White-to-Rechnitzer substitution. This is a bounded source audit, not an assertion of exhaustive bibliographic completeness.

## Assumptions beyond bootstrap

Standard identification of A(3,1,N) / sigma_3(1) with the asymptotic strong-B3 maximum under the repeated-summand, permutation-only equivalence used by Green and White.

For the 2026 numerical update only: White Corollary 1.2 remains applicable when its rigorous lower bound on mu_2^2 is replaced by a later stronger rigorous lower bound on the same normalized autoconvolution constant.

## Verification / falsification hooks

- Bose–Chowla: Comment. Math. Helv. 37 (1962/63), 141–147; inspect the B_r definition and Theorem 3.
- Green: Acta Arith. 100 (2001), Theorem 17; verify A(3,1,N) <= (7/2)^(1/3) N^(1/3)(1+o(1)) and the representation convention in the introduction.
- White: Canad. Math. Bull. 67(1) (2024), Theorem 1.1 and Corollary 1.2; verify mu_2^2 >= 0.574636066 and sigma_3(1) <= (2/mu_lower)^(1/3).
- Rechnitzer: arXiv:2602.07292; verify the rigorous 128-digit interval for nu_2^2 and that it is the same unit-mass L^2 autoconvolution infimum used in White.
- Numerically evaluate the two displayed cube roots. Any mismatch in normalization between White's mu_2 and Rechnitzer's nu_2 would falsify the 2026 substitution and should be treated as an exact blocker.

## Claim boundary

This source audit establishes that the protected Green constant is historically superseded and identifies a peer-reviewed primary-source replacement from White. It also gives a sharper 2026 primary-source-derived numerical consequence from Rechnitzer plus White, while explicitly not claiming that Rechnitzer states a B3 theorem.

It does not prove the Erdős asymptotic conjecture, establish novelty for any GCL finite or structural result, certify mathematics through MATHCERT, or retroactively alter the already-completed R1+A1 blind adjudication. It does not claim exhaustive literature currency beyond the bounded primary-source search performed here.

## Next residual

Update the source ledger for ERDOS-241 so the protected upper-constant baseline distinguishes:
(1) Green 2001 historical bound;
(2) White 2024 explicit published B3 improvement;
(3) White+Rechnitzer 2026 derived autoconvolution refinement.

Any future claim of "current best known" should either cite an explicit post-2026 primary B3 statement or preserve the narrower wording "best bound established by this audited primary-source chain."