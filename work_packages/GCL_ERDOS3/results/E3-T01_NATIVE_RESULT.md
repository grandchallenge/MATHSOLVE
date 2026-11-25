# E3-T01 — native template-cover obstruction for scalar U3 forcing

Disposition: **SMALLER_MISSING_LEMMA__PHASE_ALIGNMENT_REQUIRED**.

This result is native GCL work. It composes the exact D01 family geometry with the native Q02 labelled (U^3) forcing statement. It does not use any sibling independent-agent return.

## Strongest exact statement

Fix a four-fibre gluing with physical fibres
[
B_0,B_1,B_2,B_3subseteq[0,N-1]
]
all of density at least (eta), and suppose the gluing is globally 4-AP-free.

Let
[
eta_eta:=rac{eta^4}{15cdot16^4}.
]

For each physical fibre (j), define
[

u_j:=left|1_{B_j+s}-|B_j|/Pight|_{U^3(mathbb Z/Pmathbb Z)},
]
where (s) is any translation placing the fibre in the Q02 cyclic model. Translation invariance of (U^3) makes (
u_j) independent of (s).

For every D01 cross-fibre family (F), let (J(F)subseteq{0,1,2,3}) be the set of physical fibre indices used by its four labelled positions.

Q02 implies
[
max_{jin J(F)}
u_jge eta_eta
]
for every cross-fibre family (F).

Define the structured-fibre set
[
H_eta:={j:
u_jgeeta_eta}.
]

Then (H_eta) is a hitting set for the physical-fibre supports (J(F)).

For the exact (m=4) D01 compiler:

> **The minimum possible size of such a hitting set is exactly two.**

Moreover the three minimal two-fibre hitting sets are exactly
[
oxed{{0,2},quad{1,2},quad{1,3}.}
]

The same statement remains true if one keeps only the minimum 10-family E3-L01 finite core
[
{F_1,F_2,F_3,F_4,F_6,F_7,F_9,F_{10},F_{15},F_{16}}.
]

Therefore the entire family of scalar Q02 inequalities forces at least two structured physical fibres, but **cannot force more than two, cannot force any growth of the (U^3) magnitude beyond (eta_eta), and contains no phase/factor alignment information**.

This is an exact obstruction to the naive “apply Q02 across many carry templates and accumulate energy/rank” strategy.

## Derivation

### 1. Translation collapse

For a D01 family
[
F=(i,q,c_0c_1c_2c_3),
]
the physical block index at labelled position (t) is
[
j_t=i+tq+c_t.
]

Q02 uses translated labelled sets
[
C_t=c_tN+B_{j_t}.
]

Because (U^3) is translation invariant,
[
left|1_{C_t}-|C_t|/Pight|_{U^3}
=

u_{j_t}.
]

Thus the Q02 conclusion for a template depends only on the set of physical indices (J(F)), not on the carry translation itself.

### 2. Exact physical support table

For the 17 cross-fibre families at (m=4), the labelled block patterns are:

| family | labelled physical blocks | support (J(F)) |
|---|---|---|
| (F_0) | (0,0,0,1) | ({0,1}) |
| (F_1) | (0,0,1,1) | ({0,1}) |
| (F_2) | (0,1,1,1) | ({0,1}) |
| (F_3) | (1,1,1,2) | ({1,2}) |
| (F_4) | (1,1,2,2) | ({1,2}) |
| (F_5) | (1,2,2,2) | ({1,2}) |
| (F_6) | (2,2,2,3) | ({2,3}) |
| (F_7) | (2,2,3,3) | ({2,3}) |
| (F_8) | (2,3,3,3) | ({2,3}) |
| (F_9) | (0,1,1,2) | ({0,1,2}) |
| (F_{10}) | (1,2,2,3) | ({1,2,3}) |
| (F_{11}) | (0,0,1,2) | ({0,1,2}) |
| (F_{12}) | (0,1,2,2) | ({0,1,2}) |
| (F_{13}) | (1,1,2,3) | ({1,2,3}) |
| (F_{14}) | (1,2,3,3) | ({1,2,3}) |
| (F_{15}) | (0,1,2,3) | ({0,1,2,3}) |
| (F_{16}) | (0,1,2,3) | ({0,1,2,3}) |

The three adjacent two-block supports
[
{0,1},qquad{1,2},qquad{2,3}
]
already occur.

### 3. Lower bound two

No singleton physical fibre hits all three adjacent supports. Hence
[
|H_eta|ge2.
]

### 4. Exact two-fibre solutions

A two-element subset (Hsubseteq{0,1,2,3}) hits all three adjacent supports iff
[
Hcap{0,1}
earnothing,qquad
Hcap{1,2}
earnothing,qquad
Hcap{2,3}
earnothing.
]

Exhausting the six pairs gives exactly
[
{0,2},qquad{1,2},qquad{1,3}.
]

Each of these automatically hits every larger support in the table. Therefore the minimum is exactly two.

The E3-L01 10-family core contains families with supports
[
{0,1},quad{1,2},quad{2,3}
]
and the larger mixed supports, so the same minimum and the same three two-fibre solutions hold for that core alone.

## Why this blocks the naive accumulation strategy

The Q02 output is a scalar norm lower bound. Once two physical fibres lie in one of the three minimum covers above, all 17 per-template conclusions can be satisfied without any increase in:
- the number of structured fibres beyond two;
- the magnitude threshold beyond (eta_eta);
- quadratic-factor rank;
- energy;
- or the number of independent quadratic correlations.

Nothing in the scalar inequalities records *which quadratic phase/factor* witnesses the large (U^3) norm.

Therefore repeated use of Q02 across the carry system cannot justify a rank-accumulation or energy-increment argument.

## Smaller missing lemma

The next structural object must preserve witness identity.

A sufficient next statement would have the following form.

> **E3-B-PHASE-ALIGNMENT-INCOMPATIBILITY.** For the 10-family L01 core, choose for every structured occurrence a quantitative quadratic correlation witness supplied by an appropriate (U^3) inverse theorem. Show that no assignment of witnesses to the physical fibres can satisfy the translated carry relations for all core families unless at least
> [
> ceta^{1+	heta}N
> ]
> points are deleted, for some (	heta<1).

Equivalent formulations using bounded-complexity quadratic factors, nilsequences, or local quadratic phases are acceptable, but they must retain the *same witness across translated appearances of a physical fibre*.

## Adversarial checks

1. The conclusion is not that exactly two fibres are structured; only that the scalar inequalities permit a two-fibre cover and force at least two.
2. Large (U^3) norm by itself does not choose a canonical quadratic phase.
3. Translation invariance is the reason repeated carry translations do not create new scalar information.
4. The argument uses the exact D01 physical block patterns; no asymptotic extrapolation from (N=7) is used.
5. The 10-family L01 statement uses only which families are in the exact finite core, not the (N=7) local-set classification itself.

## Frontier effect

- E3-Q4-DENSITY-LOSS remains **OPEN**.
- E3-Q4-GLUING-RADIUS remains **unpromoted**.
- E3-B-FOUR-FIBRE-DEFICIT remains **OPEN**.
- The “repeat Q02 and accumulate scalar (U^3) energy” route is **CLOSED AS INSUFFICIENT**.
- The live T01 residual is phase/factor-alignment incompatibility across the 10-family L01 core.
