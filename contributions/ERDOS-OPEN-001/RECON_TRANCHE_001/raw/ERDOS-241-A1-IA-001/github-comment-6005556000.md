GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-241-A1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-241-A1
assignment: ERDOS-241-A1
disposition: COUNTEREXAMPLE
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

Several natural finite-to-asymptotic heuristics for the protected function
f(N) := f N 3 fail already for N <= 5.

The following exact small values/certificates suffice:

    f(2) = 2,
    f(3) = 2,
    f(4) = 2,
    f(5) >= 3.

Consequently:

1. Naive superadditivity is false:
       f(2+2) = f(4) = 2 < 4 = f(2)+f(2).

2. Naive multiplicative lower bounds are false:
       f(2*2) = f(4) = 2 < 4 = f(2)f(2).

3. The normalized ratio f(N)/N^(1/3) is not nondecreasing:
       f(2)/2^(1/3) > f(3)/3^(1/3),
   since f(2)=f(3)=2.

4. A naive extension lemma is false:
   A={1,3} is an optimal protected B3 set in {1,2,3,4}, but there is no
   x in {1,2,3,4,5}\A such that A∪{x} is a protected B3 set of size 3.
   Yet {1,2,5} is a protected B3 set, so the optimum can increase from 2
   to at least 3 without extending this optimal predecessor.

5. Naive adjacent-block union is false:
   {1,2} and {3,4} are individually protected B3 sets, but their union is
   not, because
       1+1+4 = 2+2+2.

A safe inequality does survive:

    f(M+N) <= f(M) + f(N).

Indeed, partition any protected B3 set A⊆{1,...,M+N} at M. Its left part is
a protected B3 set in {1,...,M}; translate its right part down by M, which
preserves equality/non-equality of 3-fold multiset sums, producing a protected
B3 set in {1,...,N}. Thus the two cardinalities are bounded by f(M), f(N).

Semantic audit of the protected Lean definition: it quantifies over multisets
m1,m2 of cardinality exactly 3, requires every entry to lie in A, and identifies
equal sums only when the multisets themselves are equal. Therefore permutations
are exactly the "trivial coincidences", while repeated summands are allowed.
This is the strong B3 notion encoded by the protected prose. It is NOT the
weaker "three distinct summands only" property. No internal semantic mismatch
was found within the protected packet; external-literature identity was not
asserted because external sources are forbidden in this lane.

## Derivation

For any 2-element set {a<b}, a 3-term multiset is determined by the number
j∈{0,1,2,3} of copies of b, and its sum is 3a+j(b-a). These four sums are
distinct. Hence every 2-element set is protected B3, so f(2)=2 and f(N)>=2
for N>=2.

For N=3, the only 3-element candidate is {1,2,3}, and

    1+1+3 = 1+2+2 = 5,

with distinct multisets. Hence f(3)=2.

For N=4, every 3-element subset fails:

    {1,2,3}: 1+1+3 = 1+2+2,
    {1,2,4}: 1+1+4 = 2+2+2,
    {1,3,4}: 1+4+4 = 3+3+3,
    {2,3,4}: 2+2+4 = 2+3+3.

Since all 2-element sets work, f(4)=2.

The set {1,2,5} is protected B3. Its 10 nondecreasing 3-fold multisets have
sums

    3,4,5,6,7,8,11,12,13,15

for
    111,112,122,222,115,125,225,155,255,555
respectively, all distinct. Thus f(5)>=3.

Now take the optimal N=4 set A={1,3}. The only possible new elements in
{1,...,5}\A are 2,4,5, and each destroys the B3 property:

    add 2: 1+1+3 = 1+2+2,
    add 4: 1+4+4 = 3+3+3,
    add 5: 1+3+5 = 3+3+3.

Therefore optimal sets cannot in general be grown through optimal-value jumps.

For subadditivity, if A is B3 in [1,M+N], write
A_L=A∩[1,M] and A_R=A∩[M+1,M+N].
Subsets of B3 sets remain B3. Translating A_R by -M preserves 3-multiset
sum collisions because every 3-fold sum is shifted by the same 3M. Hence
|A_L|<=f(M), |A_R|<=f(N), giving |A|<=f(M)+f(N); maximize over A.

## Assumptions beyond bootstrap

NONE. Only the protected Lean definition and elementary finite arithmetic were
used.

## Verification / falsification hooks

1. Inspect the protected snapshot
   google-deepmind/formal-conjectures@85f863718beeec7b58a3a1926ee92e3472bc2020,
   FormalConjectures/ErdosProblems/241.lean, definition Erdos241.f.

2. Verify the four displayed collisions for the four 3-subsets of [4].
   Together with the general 2-element argument this proves f(4)=2 exactly.

3. Enumerate the 10 multisets of cardinality 3 on {1,2,5}; the displayed
   sums are pairwise distinct.

4. Check the three attempted extensions of {1,3} to [5]; each has the
   displayed collision.

5. For the safe inequality, directly verify that translation by a constant
   preserves equality of r-fold multiset sums.

## Claim boundary

This does not improve the asymptotic upper constant and does not solve Erdős
Problem 241. It rules out several simple recurrence/product/greedy routes and
isolates one safe structural inequality. It also establishes only the semantic
identity visible inside the protected packet; it does not independently audit
the external historical literature.

## Next residual

Any productive finite-data route should avoid assuming superadditivity,
multiplicative product growth, monotonic normalized ratios, or extendability of
optimal sets. A safe starting point is monotonicity together with
f(M+N)<=f(M)+f(N), but that inequality alone is far too weak to close the
leading-constant gap. The next useful adversarial target is any proposed
stronger scaling inequality or product construction: it should first be tested
against the exact N<=5 certificates above.