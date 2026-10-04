# E3-L01 — native lifted family certificate at N=7

Disposition: **FINITE_LIFTED_CERTIFICATE_PROVED**.

This result is native GCL work. It uses only the protected E3-C01 and E3-D01 finite data/definitions and an exact pure-Python replay.

## Strongest exact statement

At ((m,N)=(4,7)), consider all locally 4-AP-free labelled fibre profiles with one fibre of size (5=r_4(7)) and the other three of size (4). There are exactly
[
4cdot 9cdot30^3=972{,}000
]
such profiles.

Classify each cross-fibre 4-AP by the D01 coarse/carry family
[
F=(i,q,c_0c_1c_2c_3),
]
where (i) is the starting block, (q=lfloor d/Nfloor), and
[
c_t=leftlfloorrac{u+tv}{N}ightfloor.
]

Exactly 17 cross-fibre families occur at (m=4,N=7).

For a locally admissible profile (B=(B_0,B_1,B_2,B_3)), let
[
S(B)
]
be the set of those 17 families for which (B) contains at least one cross-fibre 4-AP belonging to that family.

Then:

> **The minimum number of D01 cross-fibre template families whose constraints alone exclude every locally admissible ((5,4,4,4)) profile is exactly 10.**

One minimum certificate is
[
oxed{{F_1,F_2,F_3,F_4,F_6,F_7,F_9,F_{10},F_{15},F_{16}}},
]
with the family indexing table below.

Those 10 families contain 69 of the 97 individual cross-fibre 4-APs at (N=7). Thus 28 individual AP constraints, belonging to seven entire D01 families, may be deleted without admitting any ((5,4,4,4)) gluing.

This is a strict compression of the finite C01 obstruction. It is **not** an asymptotic deficit theorem.

## Family table

The 17 cross-fibre families, in the exact enumeration order used by the replay, are:

| index | ((i,q,	ext{carry})) | number of APs |
|---:|---|---:|
| (F_0) | ((0,0,0001)) | 4 |
| (F_1) | ((0,0,0011)) | 8 |
| (F_2) | ((0,0,0111)) | 4 |
| (F_3) | ((1,0,0001)) | 4 |
| (F_4) | ((1,0,0011)) | 8 |
| (F_5) | ((1,0,0111)) | 4 |
| (F_6) | ((2,0,0001)) | 4 |
| (F_7) | ((2,0,0011)) | 8 |
| (F_8) | ((2,0,0111)) | 4 |
| (F_9) | ((0,0,0112)) | 8 |
| (F_{10}) | ((1,0,0112)) | 8 |
| (F_{11}) | ((0,0,0012)) | 4 |
| (F_{12}) | ((0,0,0122)) | 4 |
| (F_{13}) | ((1,0,0012)) | 4 |
| (F_{14}) | ((1,0,0122)) | 4 |
| (F_{15}) | ((0,0,0123)) | 5 |
| (F_{16}) | ((0,1,0000)) | 12 |

The final family is the carry-free (q=1) cross-block family. It includes the vertical progression constraints.

## Proof of the lower bound 10

### Step 1 — five families are individually mandatory

The exact replay finds locally admissible ((5,4,4,4)) profiles whose cross-fibre support is respectively the singleton
[
{F_2},quad
{F_6},quad
{F_9},quad
{F_{10}},quad
{F_{16}}.
]

Therefore every family-level certificate must contain all five:
[
M:={F_2,F_6,F_9,F_{10},F_{16}}.
]

Explicit witnesses are emitted by the replay script.

After imposing these five mandatory families, exactly 1,380 of the 972,000 profiles remain unhit, with 596 distinct family-support sets.

### Step 2 — nine residual support clauses force five more families

Among those residual profiles, the following nine support sets occur exactly:
[
egin{aligned}
C_1&={F_3,F_4},\
C_2&={F_4,F_5},\
C_3&={F_1,F_7,F_8},\
C_4&={F_7,F_{11}},\
C_5&={F_1,F_{11},F_{12},F_{13}},\
C_6&={F_1,F_{14}},\
C_7&={F_3,F_5,F_{13},F_{14}},\
C_8&={F_0,F_3,F_5,F_{15}},\
C_9&={F_{13},F_{14},F_{15}}.
end{aligned}
]

A certificate must hit each (C_j).

We show four additional families cannot suffice.

#### Case A: (F_4) is selected

Clause (C_6) forces (F_1) or (F_{14}).

- If (F_1) is selected, then (C_4) still requires (F_7) or (F_{11}). Only one family slot remains. But no single family hits all of (C_7,C_8,C_9), because
  [
  C_7cap C_8cap C_9=arnothing.
  ]
  Hence four selections fail.

- If (F_{14}) is selected, then (C_7) and (C_9) are hit. Two slots remain, but (C_3,C_4,C_5,C_8) cannot be hit by only two families:
  - choosing (F_7) simultaneously hits (C_3,C_4), but then (C_5cap C_8=arnothing);
  - without (F_7), hitting (C_3) and (C_4) already requires separate choices unless (F_{11}) is used for (C_4,C_5), in which case a separate choice is still required for both (C_3) and (C_8).
  Thus two remaining slots are insufficient.

Therefore no four-family residual certificate exists with (F_4).

#### Case B: (F_4) is not selected

Then (C_1) forces (F_3), and (C_2) forces (F_5). Two of the four available slots are consumed.

Again (C_6) forces (F_1) or (F_{14}).

- If (F_1) is selected, then one slot remains, but it would have to hit both
  [
  C_4={F_7,F_{11}}
  ]
  and
  [
  C_9={F_{13},F_{14},F_{15}},
  ]
  which are disjoint.

- If (F_{14}) is selected, then one slot remains, but it would have to hit all three
  [
  C_3, C_4, C_5.
  ]
  Their triple intersection is empty.

Thus four residual families never suffice.

Therefore any certificate needs at least
[
5+5=10
]
families.

## Proof of the upper bound 10

Take
[
K=
{F_1,F_2,F_3,F_4,F_6,F_7,F_9,F_{10},F_{15},F_{16}}.
]

The exact replay enumerates all 972,000 locally admissible profiles and verifies
[
Kcap S(B)
eqarnothing
]
for every one.

Equivalently, every ((5,4,4,4)) profile contains a forbidden cross-fibre 4-AP from one of those 10 families.

An alternative minimum certificate is
[
{F_1,F_2,F_4,F_5,F_6,F_7,F_9,F_{10},F_{15},F_{16}}.
]

Hence the minimum family-certificate size is exactly 10.

## Reproducibility

Pure-Python replay:

[
	exttt{work_packages/GCL_ERDOS3/tools/e3_l01_family_certificate.py}.
]

The script:
1. independently regenerates the 30 locally 4-AP-free 4-subsets and nine locally 4-AP-free 5-subsets of ([0,6]);
2. regenerates all 97 cross-fibre 4-APs in ([0,27]);
3. derives their D01 family keys directly from Euclidean division;
4. enumerates all 972,000 labelled profiles;
5. proves no support set is empty;
6. verifies the five singleton mandatory witnesses;
7. verifies the nine residual clauses occur;
8. exhaustively verifies that no subset of at most four residual families hits all nine clauses;
9. verifies the displayed 10-family certificate hits every profile.

No MIP or floating-point solver is used.

## What this changes mathematically

The C01 obstruction is not an undifferentiated consequence of all 97 cross-fibre AP constraints. At family level, its exact combinatorial core can be reduced to 10 of 17 D01 template families.

This is useful for tranche 04 because it narrows the asymptotic search: a scale-free proof need not necessarily control every carry family equally. In particular the following families appear in one minimum finite core:
- the (q=1), carry-free family (F_{16});
- both labelled (0112) families (F_9,F_{10});
- the full (0123) family (F_{15});
- a chain of (0011/0001/0111) boundary families.

However the exact minimum-10 statement is currently (N=7)-specific.

## First defect

The certificate still relies on the complete classification of locally 4-AP-free 4- and 5-subsets of ([0,6]). Nothing here proves that the same 10 families, or any bounded motif extracted from them, must obstruct four near-extremal fibres at large (N).

The next theorem-grade question is therefore smaller than before:

> Do the nine residual clause types above arise, with controlled positive mass, inside arbitrary sufficiently large near-extremal fibres after an appropriate configuration/structure decomposition?

A positive answer with polynomial mass would begin to amplify the finite obstruction into the required transversal deficit.

## Frontier effect

- E3-Q4-DENSITY-LOSS remains **OPEN**.
- E3-Q4-GLUING-RADIUS remains **FORMULATED_PENDING_VERIFY**.
- E3-B-FOUR-FIBRE-DEFICIT is **NOT PROVED**.
- E3-L01 advances from “972,000 configurations are incompatible” to an exact minimum family-level certificate with a compact lower-bound proof.
- The next native bridge is motif amplification / scale transfer, not further raw finite enumeration.
