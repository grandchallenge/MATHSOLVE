GCL-CONTRIBUTION-RESULT/1
dispatch_id: OM26-H5-WP05-IA-001
agent_ref: INDEPENDENT-AGENT-505
assignment: OM26-H5-WP05
disposition: REPLAY_CLOSURE_COUNTEREXAMPLE
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

The protected predecessor result cannot be promoted to replay closure as written. Its exact 3x3 exhaustive-enumeration statistics are false: after the standard row/column sign normalization, the 16 normalized 3x3 sign matrices split into 6 classes with classical sign optimum 5, 9 classes with optimum 7, and 1 class with optimum 9. The predecessor states 10, 5, and 1 respectively.

This is an exact finite counterexample to the claimed replay evidence, independent of any SDP solver. A second structural defect occurs in the 4x4 statement: the claimed equality witness described as the direct sum CHSH (+) CHSH has zero off-block entries, so it is not a valid {-1,+1} sign matrix. A valid 4x4 equality witness is instead a CHSH blow-up by row/column duplication, for example
A = [[1,1,1,1],[1,-1,-1,1],[1,1,1,1],[1,-1,-1,1]],
which has classical optimum 8 and vector optimum 8*sqrt(2), hence exact ratio sqrt(2).

The replay therefore falsifies material parts of the predecessor's strongest exact statement. It does not, by itself, falsify the narrower numerical claims that the maximal 3x3 ratio is 6/5 or that some 4x4 sign matrices attain sqrt(2).

## Derivation

For a normalized 3x3 sign matrix
A = [[1,1,1],[1,a,b],[1,c,d]]
with a,b,c,d in {-1,+1}, the classical optimum can be evaluated exactly without optimization software. Global sign symmetry permits fixing the first coordinate of the right sign vector to +1. For the four choices (1,s,t), s,t in {-1,+1}, the value after maximizing the left signs is
|1+s+t| + |1+a*s+b*t| + |1+c*s+d*t|.
Evaluating these four integers for each of the 16 choices of (a,b,c,d) gives exactly 6 normalized classes with optimum 5, 9 with optimum 7, and 1 with optimum 9. This directly contradicts the predecessor's reported 10/5/1 count.

A concrete normalized class from the nine-member optimum-7 set is
C = [[1,1,1],[1,-1,-1],[1,-1,-1]].
For right signs (1,s,t), the classical objective is |1+s+t| + 2|1-s-t|, whose four values are 5, 3, 3, and 7, so sign(C)=7 exactly.

Its vector optimum is also available in closed form. After maximizing the left unit vectors for fixed right unit vectors v1,v2,v3, the objective is
F = ||v1+v2+v3|| + 2||v1-v2-v3||.
Put w=v2+v3, x=||v1+w||, and y=||v1-w||. Since ||w||<=2,
x^2+y^2 = 2(1+||w||^2) <= 10.
Cauchy-Schwarz gives x+2y <= sqrt(5)*sqrt(x^2+y^2) <= 5*sqrt(2). Equality is attained by v2=v3=q and a unit v1 with <v1,q>=-3/4, for which x=sqrt(2) and y=2*sqrt(2). Thus the exact vector optimum is 5*sqrt(2), consistent with ratio 5*sqrt(2)/7 for this class but inconsistent with the predecessor's class count.

For the 4x4 matrix
B = [[1,1,1,1],[1,-1,-1,1],[1,1,1,1],[1,-1,-1,1]],
columns 1 and 4 are duplicates and columns 2 and 3 are duplicates; likewise the two row types are duplicated. For right signs define p=y1+y4 and q=y2+y3, each in {-2,0,2}. Maximizing left signs gives
2|p+q| + 2|p-q| <= 8,
and equality is attained, so sign(B)=8.

For right unit vectors define a=v1+v4 and b=v2+v3. Maximizing left unit vectors gives
2||a+b|| + 2||a-b||.
Because ||a||,||b||<=2,
(||a+b||+||a-b||)^2 <= 2(||a+b||^2+||a-b||^2) = 4(||a||^2+||b||^2) <= 32.
Hence the vector objective is at most 8*sqrt(2). Equality is attained by taking v1=v4 and v2=v3 as orthogonal unit vectors. Therefore B has exact vector-to-sign ratio sqrt(2). It is a 2-by-2 CHSH blow-up, not a direct sum; an actual direct sum has forbidden zero entries.

## Assumptions beyond bootstrap

The objective and admissible matrix/vector conventions are exactly those stated in the protected predecessor result: matrix entries are restricted to {-1,+1}, classical signs are in {-1,+1}, and vector variables are unit vectors in a real inner-product space. Row/column sign normalization is used only as an equivalence operation preserving both classical and vector optima.

No external literature, repository mutation, competition submission, numerical SDP solver, or unprotected source was used. The finite 3x3 counterexample is purely combinatorial, and the displayed vector bounds are closed-form inequalities.

## Verification / falsification hooks

The 3x3 count can be replayed deterministically by enumerating the 16 quadruples (a,b,c,d) in {-1,+1}^4 and, for each, taking the maximum of the four explicit quantities
|1+s+t| + |1+a*s+b*t| + |1+c*s+d*t|
over (s,t) in {-1,+1}^2. Any correct replay must return the count vector (6,9,1) for classical optima (5,7,9).

For C, direct substitution of the four sign pairs gives classical optimum 7, while the norm identity and Cauchy-Schwarz bound above certify vector optimum 5*sqrt(2). For B, the duplicate-group reductions certify sign(B)=8 and vector(B)=8*sqrt(2) exactly. A replay that obtains the predecessor's 10/5/1 split or treats a zero-containing direct sum as an admissible sign matrix falsifies its own implementation.

## Claim boundary

This counterexample invalidates the predecessor result as a complete deterministic replay artifact because two exact structural statements in its derivation are wrong. It does not establish a sign matrix of side at most 8 with ratio strictly greater than sqrt(2), and it does not determine the maximal ratios for non-circulant 5x5 through 8x8 matrices.

The predecessor's broader HOLD recommendation is therefore not replay-closed by the evidence supplied: its 3x3 enumeration needs correction, its 4x4 equality family needs correct characterization, and its circulant/sampled searches do not constitute an exhaustive proof for sizes 5 through 8.

## Next residual

Rebuild the finite replay with the corrected 3x3 class counts and an exact classification of the admissible 4x4 equality cases. Do not infer a universal side-at-most-8 bound from circulant or sampled families; any such claim requires exhaustive or otherwise certified treatment of the non-circulant 5x5 through 8x8 cases.