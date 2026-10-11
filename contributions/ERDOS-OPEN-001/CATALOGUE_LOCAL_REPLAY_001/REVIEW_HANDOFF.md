# Erdős catalogue · bounded local certificates, critical-review handoff

STATUS: CANDIDATE_REPLAY_FOR_CRITICAL_REVIEW
EPISTEMIC_CLASS: EXACT_INTEGER_REPLAY_AND_ELEMENTARY_PROOFS
SOURCE_SEMANTIC_AUTHORITY: NOT_ACCEPTED
MATHSOLVE_DISPATCH_AUTHORIZED: NO
MATHCERT_CERTIFICATION: NO
GCL_EXTERNAL_WORKER_INDEPENDENCE_VERIFIED: NO

## Provenance / immutable return surfaces

These five checks inspect mathematical claims reported under the authenticated
GitHub transport actor `fyremael`. No distinct research-agent identity,
independent source referee or protected theorem acceptance is inferred.

| Problem | Original RESULT/1 | Critical-review issue | Source-bound target |
| --- | --- | --- | --- |
| 7 | MATH-PROGRAMME #1276 comment 6103364800 | #2515 | finite covering certificate / CRT noncover |
| 9 | MATH-PROGRAMME #1278 comment 6103585999 | #2516 | odd-prime/two-powers finite representations |
| 10 | MATH-PROGRAMME #1279 comment 6103628767 | #2517 | prime-plus-powers popcount / Grechuk finite boundary |
| 138 | MATH-PROGRAMME #1407 comment 6098796505 | #2508 | van der Waerden product colouring and 9-term obstruction |
| 241 | MATH-PROGRAMME #1510 comment 6098842021 | #2509 | sharp finite strong-B3 no-wrap modulus |

Run `python ci/erdos_catalogue_local_certificates.py --check` from the
repository root. This deterministic standard-library script fails closed on
any unexpected witness count/hash, failure to find primality/compositeness
witnesses, or finite counterexample. It performs **no remote fetches** or
unreviewed theorem admissions.

## 7 · complete finite-input criterion, not the global covering question

For a supplied nonempty list of m_i>=2, residue a_i modulo m_i, set
L=lcm(m_i). Since m_i divides L, every congruence is L-periodic.
Consequently the union of the congruences is Z if and only if every
r=0,...,L-1 satisfies at least one congruence. This is an iff: no assumption
that m_i are distinct or odd is required for periodicity itself.

If the m_i are pairwise coprime, the Chinese remainder isomorphism
Z/LZ ≅ ∏ Z/m_iZ implies exactly ∏(m_i-1)>0 residue vectors avoid each
specified class. Therefore such a finite list never covers Z. The script
checks all 3*5*7=105 residue assignments and 48 uncovered residue classes,
plus one distinct-modulus nonodd positive control.

The current problem is specifically an all-odd, distinct, m_i>1 cover,
not arbitrary covering systems. The result gives neither a constructive
example nor an impossibility theorem. Source/status comparison:
https://www.erdosproblems.com/7 and
Bispels–Cohen–Harrington–Lowrance–Pontes–Schaumann–Wong,
*A further investigation on covering systems with odd moduli*,
Discrete Mathematics 349(7) (2026), article 115013,
DOI 10.1016/j.disc.2026.115013. The latter allows a repeated modulus,
so must NOT be imported as resolving the distinct-moduli question.

## 9 · complete finite interval only

The original set A is the *unrepresented odd integers*, with
p prime and k,l>=0. For odd n the cases are: (i) p odd,
k=l=0; (ii) p odd, k,l>=1; or (iii) p=2, exactly one exponent is
zero. The script enumerates k<=l and n in {5,7,...,199999}, checks
all 99,998 lex-first witnesses by exact prime sieve and exact sum and
reproduces the raw ASCII n,p,k,l newline SHA-256:

`a6a8724d608717823af0703a033000e9170d1bf49058f80bb757e69f7f6fc464`

Exponents 0..17 are exhaustive for n<=200000. n=1,3 are not
representable; 5=3+1+1 is representable. This is **not** an upper-density
statement, and finite absence of exceptions beyond 3 in this range says
nothing about existence of infinitely many exceptions. Source/problem
definition: https://www.erdosproblems.com/9; Crocker 1971 and Pan 2011
remain external theorems and were not proved by the local checker.

## 10 · exact finite obstruction and four-power positive witness

For the even fixed integer N=1117175146, p=2 requires popcount(N-2)
powers and exceeds 3. An odd candidate prime p forces odd offset N-p.
The script exhausts all one-, two-, and three-power multisets with
repetitions and exponent 0; after exact integer canonicalization there
are 462 distinct allowable odd offsets. For each, N-offset has a
nontrivial divisor, so no at-most-three-power representation exists.

Canonical sorted offsets x and least-factors d serialize as x,p,d newline,
yielding SHA-256:
`a57128e0c303e60e159000f5896751864f6683ae339989b55bb89475c3cee37a`

The four-power representation
1117175146=1117175107+1+2+4+32 uses prime 1117175107
(exact integer trial division for all candidates through its square root).
Thus the **finite minimum for this particular N** is four. The global
uniform-k problem remains open. This was previously reported by Grechuk
at https://www.erdosproblems.com/10; no novelty is claimed.

## 138 · finite obstruction distinct from an asymptotic lower bound

The finite ternary word 001001122 has no monochromatic 3-AP among its
16 index triples (a,a+d,a+2d) in {0,...,8}. Every one of the 8 maps
from three labels to two labels creates a monochromatic 3-AP. Finite
word/enumeration checks are exact and do not imply that W_2(k) and W_3(k)
have comparable asymptotic root growth.

Separately, a purely combinatorial proof gives
W_(r*s)(k) <= W_r(W_s(k)) for r,s>=2: read an r*s-colouring as an
r-colour and an s-colour; first extract a length-W_s(k) AP with
constant first coordinate; then extract a k-AP in its positional
indices with constant second coordinate. Composition of the two affine
index maps is an AP. This is conditional on the standard definition
of the finite van der Waerden numbers, not a new solution of Problem
138 (https://www.erdosproblems.com/138).

## 241 · sharp no-wrap transfer for triple-sum uniqueness

Let A⊆{1,...,N}, and compare equality of unordered triples WITH
repetitions in integers versus ZMod M. Any triple sum lies in
[3,3N], and two distinct integer sums differ in absolute value by
at most 3N-3. If M>=3N-2, two distinct sums cannot differ by a nonzero
multiple of M. Therefore the strong-B3 property is equivalent in the
two groups under these exact hypotheses. This argument depends
critically on canonical [1,N] representatives and genuine
multiset, not ordered-tuple, uniqueness.

Sharpness at M=3N-3 follows from A={1,N}: two different triples
(1,1,1) and (N,N,N) differ by exactly M, although their integer
sums are different and the two mixed triple sums (1,1,N) and (1,N,N) are also distinct.
The script tests every A⊆[1,N] for N=2,...,9 and the sharp
counterexample at each N. This is a finite regression plus a
paper proof, NOT a checked Lean theorem or the asymptotic result.

## Conditions for further mathematical promotion

1. Obtain a *genuinely independent* attributable source/statement
   review on each linked Programme critical-review docket. Same
   GitHub transport actor does not supply independence by itself.
2. Source-lock exact primary theorem/page where historical claims
   are relied upon. External citations are not imported axioms.
3. For claims of formal proof, create a separately governed bounded
   work package with pinned Lean/Mathlib, source/statement matching,
   clean build, axiom report, and adversarial replay.
4. Avoid duplicate native MATHSOLVE residuals and do not mutate
   Forge/Solve/Cert or mathematical claims from this file.
5. Until the critical review is accepted, these scripts, tests,
   notes and candidate CI results are unadjudicated evidence only.
