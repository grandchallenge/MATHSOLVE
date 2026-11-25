GCL-CONTRIBUTION-RESULT/1
dispatch_id: RWP-003-NSPHERE-IA-001
agent_ref: CHATGPT-TASK-WORKER-RWP003
assignment: RWP-003-NSPHERE
disposition: PROVED_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

Put b=1-2a, with 0<a<1. For a != 1/2, F_a is defined on all of S^1, and its **exact global Lipschitz constant for intrinsic angular geodesic distance** is L(a)=1/|1-2a|. The constant is attained as a supremum of arbitrarily close pairs at u=(0,1) or (0,-1). For a=1/2 the domain is S^1 minus {(0,1),(0,-1)}. On each of the two open semicircles F_{1/2}(x,y)=(sgn x,0); there is no finite global Lipschitz constant on this punctured domain (using the ambient intrinsic circle distance). On each connected component separately the map is constant and has Lipschitz constant zero. For a approaching 1/2 from either side, L(a) diverges as 1/(2|a-1/2|). For a != 1/2 the two-sided angular derivative remains finite but becomes concentrated in a narrowing neighborhood of the vertical directions; at a=1/2 the image jumps between antipodal outputs across each deleted vertical point.

## Derivation

Since D=diag(1,-1), B_a=diag(1,b). For u(t)=(cos t,sin t), define F_a(u(t))=(cos phi(t),sin phi(t)) with phi(t)=atan2(b sin t,cos t), lifted continuously to a real-valued angle on the universal cover when b != 0. Direct differentiation of the argument gives

phi'(t)=b/(cos^2 t+b^2 sin^2 t).

Its absolute maximum is 1/|b| because 0<|b|<1; the denominator is at least b^2, with equality at cos t=0. The lift phi has degree +1 for b>0 and -1 for b<0, so phi(t+2pi)=phi(t)+2pi sgn(b). Given any two points, choose the shorter input arc of length d in [0,pi]. Integrating along that arc yields an output path of length at most (1/|b|)d. The geodesic distance between its output endpoints is no larger than the length of this output path. Thus the global intrinsic Lipschitz ratio is at most 1/|b|, including antipodal and cut-locus cases. Conversely, along arbitrarily short arcs centered at t=pi/2, the ratio of output to input geodesic distances tends to |phi'(pi/2)|=1/|b|. This proves global sharpness, rather than merely an upper bound on a derivative.

For b=0, B_a u=(cos t,0), nonzero precisely where cos t != 0. For epsilon>0, points u(pi/2-epsilon) and u(pi/2+epsilon) lie in the domain, are separated by input geodesic distance 2epsilon, and map to (1,0) and (-1,0), at output geodesic distance pi. Their ratio pi/(2epsilon) diverges. Thus no finite global bound exists. In particular the a=1/2 map does not admit a continuous extension across either deleted point. For fixed nonvertical u, as b approaches zero from either side F_a(u) tends to (sgn x,0); at vertical u, the outputs are (0,sgn(b)sgn(y)), so the two one-sided parameter limits differ. These are distinct phenomena: pointwise limits away from the deleted set do not imply uniform or Lipschitz convergence.

For invertible B_a, the Euclidean spectral condition number is kappa_2(B_a)=max(1,|b|)/min(1,|b|)=1/|b|. The usual matrix-conditioning derivative bound is therefore exactly sharp for this example. This equality is special to the diagonal two-dimensional map; it is not a general claim about nonlinear networks.

Explicit values: a=1/4 gives b=1/2 and L=2; a=1/2 gives b=0, deleted points and infinite global Lipschitz seminorm; a=3/4 gives b=-1/2 and L=2 (orientation reversing); a=49/100 gives b=1/50 and L=50; a=51/100 gives b=-1/50 and L=50.

## Assumptions beyond bootstrap

None. Distances are intrinsic shortest-arc distances on the unit circle. At the singular parameter the distance on the punctured domain is taken as the original ambient S^1 geodesic distance, as specified by the task; an intrinsic path metric restricted to each disconnected component would not define a finite distance between components and would not support the same global comparison.

## Verification / falsification hooks

Deterministic Python 3 standard-library finite spot check (adjacent angular grid points, N=4096; angular remainder avoids branch-cut artifacts):

```python
import math

def check(a, n=4096):
    b = 1 - 2*a
    if b == 0:
        return "singular"
    angles = [2*math.pi*j/n for j in range(n)]
    def phi(t):
        return math.atan2(b*math.sin(t), math.cos(t))
    best = 0.0
    for j in range(n):
        x, y = angles[j], angles[(j+1) % n]
        d = 2*math.pi/n
        q = abs(math.remainder(phi(y)-phi(x), 2*math.pi))/d
        best = max(best, q)
    return f"{best:.8f}"

for a in (0.25, 0.5, 0.75, 0.49, 0.51):
    print(a, check(a))
```

Actually executed output:

```
0.25 1.99999529
0.5 singular
0.75 1.99999529
0.49 49.90233790
0.51 49.90233790
```

Grid estimates are below the theoretical sharp constants because the narrow maximal-derivative region is sampled at finite spacing. The singular case is established analytically by cross-component pairs, not by the script. Further falsification: for each nonsingular a, directly check the derivative formula by symmetric finite differences near pi/2; compare all sampled pairwise geodesic ratios against L(a) allowing floating-point tolerance.

## Claim boundary

The statement concerns exactly the elementary one-block normalized residual map u -> ((1-a)I+aD)u/||((1-a)I+aD)u|| on S^1. It shows that normalization alone does not enforce a parameter-uniform Lipschitz bound: near a singular residual operator, angular sensitivity diverges. It does not imply instability of a full nGPT/RUNT model, nor give guarantees about training, optimization, learned weights, deep compositions, or practical improvements. This is a mathematical worker return, not independent certification, novelty, protected-source promotion or publication authority.

## Next residual

Protected intake should verify the single authenticated return, exact schema and source lock, and separately arrange independent mathematical scrutiny if any claim is promoted. In particular, distinguish the punctured-domain cross-component ratio from componentwise constancy and verify the global geodesic argument rather than accepting a local derivative bound as sufficient.