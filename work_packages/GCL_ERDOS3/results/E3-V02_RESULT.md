GCL-CONTRIBUTION-RESULT/1
dispatch_id: GCL-ERDOS3-E3-V02-IA-001
assignment: E3-V02
agent_ref: INDEPENDENT-AGENT-E3-V02-001
disposition: VERIFIED
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY

## Strongest exact statement

At protected commit `bf9bc7f448f92d71afeae937fda133b0e1d4de80`, the reverse implication in E3-B02 is correct for every fixed `k >= 3`:

[
sum_{nge1}rac{r_k(2^n)}{2^n}=infty
quadLongrightarrowquad
exists Asubseteqmathbb N_{>0}
	ext{ that is }k	ext{-AP-free and }
sum_{ain A}rac1a=infty.
]

The immutable identities were verified exactly before replay: E3-V02 blob `98e17042c9f93010139f43d3788a4c5fc5316b5b`; E3-B02_RESULT blob `0c6a3192294f9017a2e6bb18fa1cd4063d78a818`; E3-S02_RESULT blob `bf52757797483b09b29292a326f0cecd3779ca9b`; FRONTIER blob `464574eb705c841e332035f35a4b44b83d57c296`.

## Derivation / evidence

Write
[
a_n:=rac{r_k(2^n)}{2^n}.
]

1. **Doubling bound and normalized monotonicity.**  
For any `k`-AP-free `A subseteq [1,2N]`, both `A cap [1,N]` and the translate of `A cap [N+1,2N]` into `[1,N]` are `k`-AP-free. Hence each has at most `r_k(N)` elements and
[
r_k(2N)le 2r_k(N).
]
Taking `N=2^n` gives
[
a_{n+1}=rac{r_k(2^{n+1})}{2^{n+1}}
le rac{2r_k(2^n)}{2^{n+1}}=a_n.
]

2. **Full-series divergence forces odd-subseries divergence.**  
Normalized monotonicity gives `a_{2d} <= a_{2d-1}`. Therefore, if (sum_d a_{2d-1}<infty), then
[
sum_{nge1}a_n
=sum_{dge1}(a_{2d-1}+a_{2d})
le 2sum_{dge1}a_{2d-1}<infty,
]
contradicting the hypothesis. Thus
[
sum_{dge1} a_{2d-1}=infty.
]

3. **No mixed three-term AP across the blocks.**  
Let
[
M_d:=4^d,qquad L_d:=M_d/2,qquad
B_d=[M_d,M_d+L_d)=[M_d,	frac32M_d).
]
Take a nontrivial three-term AP `x<y<z` in the union of the blocks, and let `y in B_d`.

If `x` is in an earlier block, every earlier point is (<rac32M_{d-1}=rac38M_d). Hence
[
y-x>rac58M_d,
qquad
z=2y-x>rac{13}{8}M_d>rac32M_d.
]
Also (z=2y-x<2y<3M_d<4M_d=M_{d+1}). Thus `z` lies in the gap after `B_d`, contradiction.

If `x,y in B_d`, then (y-x<L_d=M_d/2), so
[
z=y+(y-x)<2M_d<4M_d,
]
while `z>y`; hence `z` cannot lie in a later block. These two cases exhaust the possibilities according to whether the first two AP terms lie in the same block. Therefore every 3-AP in the union lies inside one block.

4. **Global `k`-AP-freeness for `k>=3`.**  
For each `d`, choose a `k`-AP-free
[
C_dsubseteq[1,L_d],qquad |C_d|=r_k(L_d),
]
and translate it to
[
A_d:={M_d-1+c:cin C_d}subseteq B_d.
]
Translation preserves arithmetic progressions, so each `A_d` is `k`-AP-free. If a `k`-term AP with `k>=3` crossed block boundaries, its consecutive triples would be 3-term APs; at least one such triple would be mixed. Step 3 excludes this. Thus
[
A:=igcup_{dge1}A_d
]
is globally `k`-AP-free.

5. **Reciprocal-mass lower bound.**  
Every `m in A_d` satisfies
[
m<M_d+L_d=rac32M_d=3L_d.
]
Therefore
[
sum_{min A_d}rac1m
>
rac{|A_d|}{3L_d}
=
rac{r_k(L_d)}{3L_d}
=
rac13,
rac{r_k(2^{2d-1})}{2^{2d-1}}
=
rac13 a_{2d-1}.
]
Summing over `d` and using Step 2 gives
[
sum_{min A}rac1m
ge rac13sum_{dge1}a_{2d-1}
=infty.
]

This proves exactly the requested reverse implication.

## Adversarial checks

- The inequality `r_k(2N) <= 2r_k(N)` uses only interval partition plus translation invariance; it does not assume any unproved density property.
- Divergence of the odd subseries is not inferred merely from monotonicity heuristically; it follows by the explicit domination (sum_n a_nle2sum_d a_{2d-1}).
- The mixed-3-AP argument covers both possible locations of the first two terms relative to the block containing the middle term. In the cross-block case the third term is forced strictly into the gap ((	frac32M_d,4M_d)).
- The passage from no mixed 3-AP to no mixed `k`-AP is valid only because `k>=3`; every consecutive triple of a nontrivial `k`-AP is itself a nontrivial 3-AP.
- The translated set starts at exactly `M_d` and ends at `M_d+L_d-1`, so it lies in the half-open block `B_d`. The reciprocal estimate uses only the strict upper bound `m<3L_d`.
- No outside mathematical source was used.

## First defect

NONE

## Frontier effect

The protected evidence supports marking verification node `E3-V-B02` as verified and the reverse block-construction implication in `E3-B02` as independently replayed under the declared ZERO_CONTEXT / PROTECTED_PACKET_ONLY contract. This verification has no effect on the status of the parent Erdős conjecture.

## Next residual

Within the protected frontier, `E3-Q4-SERIES` remains open: prove (sum_{nge1} r_4(2^n)/2^n<infty). E3-S02 records that the protected pointwise bound alone does not establish this convergence.
