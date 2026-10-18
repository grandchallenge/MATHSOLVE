# ERDOS-241 — R1+A1 protected synthesis

Closure: contributions/ERDOS-OPEN-001/RECON_TRANCHE_001/closures/ERDOS-241-BLIND-COHORT-001.json  
Replay: contributions/ERDOS-OPEN-001/RECON_TRANCHE_001/replays/ERDOS-241-RA-REPLAY-001.json  
Successor: work_packages/ERDOS_OPEN/ERDOS_241_N1_LOCAL_DIFFERENCE_POWER.md

## Decision

The blind R1+A1 collection barrier is closed. Both returns were protected before comparison. S1 was not protected at closure, so no literature-dependent statement is promoted and no claim is made about the current best published upper constant.

The native replay confirms the finite R1 certificate at its full stated boundary:

- f(1)=1;
- f(N)=2 for 2<=N<=4;
- f(N)=3 for 5<=N<=11;
- f(N)=4 for 12<=N<=23;
- f(N)=5 for 24<=N<=45;
- f(N)=6 for 46<=N<=64;
- the R1 minimal-span extremizer lists for cardinalities 1 through 6 are reproduced exactly;
- an independent exhaustive search finds no 7-element strong-B3 set in [64].

The A1 small-N attacks are also reproduced. In particular the proposed simple bridges based on superadditivity, multiplicativity, monotonicity of f(N)/N^(1/3), greedy extension of an optimal predecessor, or adjacent-block union are not admissible routes.

The synthesis additionally accepts three elementary structural facts by direct proof. These are internal MATHSOLVE facts only; they do not settle the asymptotic problem.

## Direct adjudication of the structural claims

### 1. Strong B3 implies B2/Sidon uniqueness

Let M1 and M2 be two cardinality-2 multisets supported on A with equal sum. Pick any z in A. Then M1 plus {z} and M2 plus {z} are cardinality-3 multisets with equal sums. Strong B3 forces them equal. Cancelling the common singleton {z} gives M1=M2.

Consequently, if a>b and c>d are in A and a-b=c-d, then a+d=c+b. The two 2-multisets {a,d} and {c,b} have equal sums, hence are equal. The positive orientation forces (a,b)=(c,d). Thus every positive difference has a unique ordered-pair representation.

### 2. No positive difference is twice another

Suppose a-b=2(c-d) with a>b and c>d in A. Then

a+d+d = b+c+c.

Strong B3 would force the multisets {a,d,d} and {b,c,c} to be equal. The left multiset contains d with multiplicity at least two. Since c!=d, the right multiset can contain d only through b, hence at most once. This is impossible. Therefore

Delta(A) intersect 2 Delta(A) is empty.

This proves the R1 double-difference obstruction without relying on its supplied derivation.

### 3. Two vertex-disjoint differences cannot sum to a third difference

Let d1=a-b and d2=c-d with {a,b} disjoint from {c,d}. Suppose d1+d2=e-f is another positive difference. Then

a+c+f = b+d+e.

Strong B3 forces {a,c,f}={b,d,e}. Because the first two difference pairs are vertex-disjoint, a is neither b nor d, so equality of multisets forces a=e. Similarly c is neither b nor d, so c=e. Hence a=c, contradicting vertex-disjointness. Therefore d1+d2 is not in Delta(A).

The replay also searched every strong-B3 subset of [15] of cardinality at most 6 and found no counterexample to either structural obstruction; that finite sweep is corroboration, not the proof.

## A1 route eliminations retained

The following are accepted as exact counterexamples or safe boundaries:

- f(4)=2 < f(2)+f(2)=4, so superadditivity fails.
- f(4)=2 < f(2)f(2)=4, so the naive multiplicative lower bound fails.
- f(2)=f(3)=2, so f(N)/N^(1/3) decreases from N=2 to N=3.
- {1,3} is optimal in [4] but cannot be extended to a size-3 strong-B3 set in [5], while {1,2,5} works.
- {1,2} and {3,4} are each strong B3, while their union fails because 1+1+4=2+2+2.
- f(M+N)<=f(M)+f(N): split a strong-B3 set at M and translate the right piece by -M.

These eliminations constrain successor design but do not improve the asymptotic upper constant.

## Source gate

The protected pack states a Bose-Chowla lower asymptotic and a Green upper constant (7/2)^(1/3). The S1 primary-source audit is still absent. Therefore:

- the historical/literature identity of the strong-B3 definition is not newly promoted here;
- no statement is made that (7/2)^(1/3) is currently best known;
- no novelty claim is made for the finite values or structural lemmas;
- any later literature-dependent promotion still requires S1 and separate adjudication.

## Advancement decision

The finite certificate is useful evidence, but the smallest native next question is not another larger finite table. It is whether the confirmed local difference obstructions have enough quantitative force to improve the protected cubic upper-constant route at all.

The campaign therefore advances to:

ERDOS-241-N1-LOCAL-DIFFERENCE-POWER.

That successor must either derive a strict quantitative improvement from the local constraints or prove a no-go by constructing a family/model satisfying those constraints while violating the desired cubic-strength conclusion.

## Claim boundary

This synthesis adjudicates only the finite claims and elementary internal structural statements listed above. Erdős Problem 241 remains open. Literature currency remains source-gated. There is no MATHCERT effect, publication effect, prize effect, or assertion that GCL has improved the published asymptotic bound.
