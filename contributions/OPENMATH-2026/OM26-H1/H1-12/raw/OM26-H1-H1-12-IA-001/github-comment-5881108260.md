GCL-CONTRIBUTION-RESULT/1
dispatch_id: OM26-H1-H1-12-IA-001
agent_ref: INDEPENDENT-AGENT-001
assignment: OM26-H1-H1-12
disposition: PROVED_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

**Theorem 1 (Exclusion of the Sole $q=5$ Nested-Triangle Equality Normal Form and Closure of $q=5$).**
Conditional on the source-scoped local fan and clean-line charging premises recorded in `H1_12_STATUS.json` and `CLAIM_LEDGER.json`, the sole surviving $q=5$ score-95 normal form for an $n=18$ pairwise-nonparallel line arrangement—namely, multiplicity profile `33333` with $D_2$-graph $K_3 \sqcup \{D\} \sqcup \{E\}$ and equality parameters $(D_2, D_1, U, \text{blocked}, \text{clean}, \text{capacity}, h) = (3, 10, 1, 6, 6, 6, 12)$—is geometrically unrealizable in the affine plane. Combined with the established $q \le 4$ exclusions and the exclusions of all other $q=5$ profiles and `33333` graph orbits, no normalized $n=18, T=95$ arrangement has $q \le 5$ finite multiple points; any such witness must satisfy $q \ge 6$.

**Theorem 2 (General $K_3$ Triple-Core $D_1$-Saturation Obstruction for Arbitrary $q$).**
In any pairwise-nonparallel affine line arrangement (for arbitrary $n, T, q$), let $A, B, C$ be three triple points (multiplicity $3$) whose pairwise segments $AB, BC, CA$ are elementary $D_2$ segments (each shared by two counted bounded triangular faces), with third incident arrangement lines $L_A, L_B, L_C$ respectively. Conditional on the triple-point no-consecutive-$D_1$ premise (no two cyclically adjacent radial segments with ordinary non-core endpoints are both $D_1$), at most one vertex $V \in \{A, B, C\}$ can have local counts $d_2(V) = 2$ and $d_1(V) = 2$. In particular, if $ABC$ is a $K_3$ connected component of triple points in the $D_2$ graph, then $d_1(A) + d_1(B) + d_1(C) \le 4$, and the state $d_1(A) = d_1(B) = d_1(C) = 2$ is impossible for every $q \ge 3$.

## Derivation

### 1. Local Definitions and Bootstrap Setup

Let $\mathcal{A}$ be an affine arrangement of $n=18$ pairwise-nonparallel straight lines (obtained via the H1-12 projective parallelism reduction while preserving all selected counted bounded triangular faces). Let $T=95$ be the number of counted bounded triangular faces. By claim `OM26-H1-THM-001`, a counted bounded triangular face of $\mathcal{A}$ is a nondegenerate $3$-cycle of the arrangement graph, meaning a bounded open triangle bounded by three lines of $\mathcal{A}$ whose three boundary sides are **elementary segments** (segments between consecutive arrangement vertices on their supporting lines, containing no arrangement vertex in their open interiors) and whose open interior is crossed by no line of $\mathcal{A}$.

An arrangement vertex has multiplicity $r \ge 2$ if exactly $r$ lines of $\mathcal{A}$ pass through it. Vertices with $r=2$ are **ordinary vertices**; vertices with $r \ge 3$ are **multiple points** (or **cores**), and $q$ denotes the number of finite multiple points. A bounded elementary segment of $\mathcal{A}$ is:
- a **$D_2$ segment** if it is shared by two counted bounded triangular faces and both of its endpoints are multiple points;
- a **$D_1$ segment** if it is shared by two counted bounded triangular faces and has **exactly one** multiple endpoint and **one** ordinary endpoint;
- a **$U$ segment** if it is incident to no counted bounded triangular face.

For each multiple point $V$ of multiplicity $r$, the $r$ incident lines divide a neighborhood of $V$ into $2r$ cyclic angular sectors $S_0, S_1, \dots, S_{2r-1}$ separated by $2r$ radial rays $\rho_0, \rho_1, \dots, \rho_{2r-1}$ originating at $V$. Write $t_i \in \{0, 1\}$ for the indicator that sector $S_i$ (between $\rho_i$ and $\rho_{i+1}$, indices modulo $2r$) is a counted bounded triangular face. A radial ray $\rho_i$ supports a shared elementary segment ($D_1$ or $D_2$) if and only if both adjacent sectors are counted bounded triangular faces:
$$\text{shared}(\rho_i) \iff t_{i-1} = 1 \text{ and } t_i = 1.$$
Write $d_2(V)$ and $d_1(V)$ for the number of $D_2$ and $D_1$ elementary segments incident to $V$. A $D_1$ ray $\rho_i$ at $V$ is **blocked** if $\rho_{i-1}$ or $\rho_{i+1}$ is a $D_2$ ray.

In `H1_12_STATUS.json` (`q5_equality_normal_form`, claim `OM26-H1-RED-022`), all $q \le 4$ cases and all other $q=5$ cases are excluded conditional on the source-scoped local fan and clean-line charging premises, leaving a single $q=5$ survivor: five triple cores $A, B, C, D, E$ (multiplicity $3$ at each core) where $A, B, C$ form a $D_2$ triangle ($d_2(A)=d_2(B)=d_2(C)=2$), $D$ and $E$ are isolated in the $D_2$ graph ($d_2(D)=d_2(E)=0$), $D_2=3$, $D_1=10$, $U=1$, $\text{blocked}=6$, $h=12$, and every core satisfies $d_1(V)=2$.

We prove Theorem 2 first, and then deduce Theorem 1 as an immediate corollary.

### 2. Unique Sector-Consistent Local Structure at a Triple Core with $d_2(V)=2$ and $d_1(V)=2$

Let $A, B, C$ be three triple cores whose pairwise segments $AB, BC, CA$ are elementary $D_2$ segments, and let $L_A, L_B, L_C$ denote the third arrangement lines through $A, B, C$ respectively.

**Lemma 1 (Central Face and Cyclic Ray Order).**
The triangle $\triangle ABC$ is a counted bounded triangular face of $\mathcal{A}$. At each vertex $V \in \{A, B, C\}$, the third line $L_V$ does not enter the open interior of $\triangle ABC$, so the two inward $D_2$ rays along the sides of $\triangle ABC$ are cyclically adjacent around $V$.

*Proof.* Because $AB, BC, CA$ are elementary $D_2$ segments, no arrangement line crosses the open segment $AB$, $BC$, or $CA$. If any arrangement line crossed the open interior of $\triangle ABC$, it would have to exit $\triangle ABC$ across two of its boundary segments or through a vertex and the opposite open boundary segment. Since $A, B, C$ have multiplicity $3$, the only arrangement lines through $A$ are $AB, AC, L_A$. If $L_A$ entered the open interior of $\triangle ABC$, it would cross the opposite open elementary segment $BC$, contradicting that $BC$ is an elementary segment. The same holds for $L_B$ and $L_C$, and no other line passes through $A, B, C$. Thus no line of $\mathcal{A}$ meets the open interior of $\triangle ABC$, so $\triangle ABC$ is a counted bounded triangular face and the two inward $D_2$ rays at each $V \in \{A, B, C\}$ are cyclically adjacent. $\square$

Fix $V \in \{A, B, C\}$, say $V = A$, and orient the cyclic order of the six rays $\rho_0, \dots, \rho_5$ around $A$ so that:
- $\rho_0 = r(A \to B)$ is the ray from $A$ through $B$ along line $AB$;
- $\rho_1 = r(A \to C)$ is the ray from $A$ through $C$ along line $AC$.

Since the three lines through $A$ are $AB, AC, L_A$ and $L_A$ does not enter the interior sector $S_0$ between $\rho_0$ and $\rho_1$ (nor the vertically opposite sector $S_3$), the two opposite rays of $L_A$ lie in the two side sectors separating $\{\rho_0, \rho_1\}$ from their opposite outward continuation rays:
- $\rho_3 = r_{\text{out}}(BA) = \{ A + t(A - B) : t > 0 \}$ (the open ray of line $AB$ starting at $A$ away from $B$, opposite to $\rho_0$);
- $\rho_4 = r_{\text{out}}(CA) = \{ A + t(A - C) : t > 0 \}$ (the open ray of line $AC$ starting at $A$ away from $C$, opposite to $\rho_1$).

Thus the six rays around $A$ in exact cyclic order are:
$$\rho_0 = r(A \to B), \quad \rho_1 = r(A \to C), \quad \rho_2 \subset L_A, \quad \rho_3 = r_{\text{out}}(BA), \quad \rho_4 = r_{\text{out}}(CA), \quad \rho_5 \subset L_A,$$
where $\rho_2$ and $\rho_5$ are the two opposite rays of line $L_A$ originating at $A$.

**Lemma 2 (Unique Sector-Consistent Local Word for $d_2(V)=2, d_1(V)=2$).**
Suppose a vertex $V \in \{A, B, C\}$ satisfies $d_2(V)=2$ and $d_1(V)=2$, and obeys the triple-point no-consecutive-$D_1$ premise. Then its cyclic sector indicator word and ray-label word are uniquely forced to be:
$$(t_0, t_1, t_2, t_3, t_4, t_5) = (1, 1, 1, 0, 1, 1), \qquad (\rho_0, \rho_1, \rho_2, \rho_3, \rho_4, \rho_5) \leftrightarrow (\text{D2}, \text{D2}, \text{D1}, 0, 0, \text{D1}).$$
In particular, both opposite rays $\rho_2, \rho_5$ of $L_V$ at $V$ are $D_1$ rays, and the four sectors $S_1, S_2, S_4, S_5$ are all counted bounded triangular faces.

*Proof.* Because $\rho_0$ and $\rho_1$ are shared $D_2$ rays, the shared-ray equivalence $\text{shared}(\rho_i) \iff t_{i-1} = t_i = 1$ forces $t_5 = t_0 = t_1 = 1$. Since $d_2(V) + d_1(V) = 4$, exactly four of the six rays $\rho_0, \dots, \rho_5$ are shared. In a $6$-cycle of sector bits with $t_5 = t_0 = t_1 = 1$:
- if all three of $t_2, t_3, t_4$ equal $1$, all $6$ rays are shared (giving $4 \ne 6$);
- if two or three of $t_2, t_3, t_4$ equal $0$, at most $3$ rays are shared (giving $4 \le 3$, impossible).
Hence **exactly one** of $t_2, t_3, t_4$ equals $0$, and the other five sectors equal $1$:
- If $t_2 = 0$ and $t_3 = t_4 = 1$, the shared rays are $\rho_0, \rho_1, \rho_4, \rho_5$, so the $D_1$ rays are $\rho_4, \rho_5$, which are cyclically consecutive—violating the no-consecutive-$D_1$ premise.
- If $t_4 = 0$ and $t_2 = t_3 = 1$, the shared rays are $\rho_0, \rho_1, \rho_2, \rho_3$, so the $D_1$ rays are $\rho_2, \rho_3$, which are cyclically consecutive—violating the no-consecutive-$D_1$ premise.
- Therefore $t_3 = 0$ and $t_2 = t_4 = 1$ is the unique admissible sector word, yielding $(t_0, \dots, t_5) = (1, 1, 1, 0, 1, 1)$ and $D_1$ rays at $\rho_2$ and $\rho_5$. $\square$

### 3. Outer Triangles and Ordinary Status of $X_{AB}, X_{BC}, X_{CA}$

Across each $D_2$ segment $XY \in \{AB, BC, CA\}$, one incident counted bounded triangular face is $\triangle ABC$ (in sector $S_0$ at $X$ and $Y$), and the second incident counted bounded triangular face lies on the opposite side of line $XY$.
- At $A$, the sector adjacent to $\rho_1 = r(A \to C)$ outside $\triangle ABC$ is $S_1$ (bounded by $\rho_1$ and $\rho_2 \subset L_A$), and the sector adjacent to $\rho_0 = r(A \to B)$ outside $\triangle ABC$ is $S_5$ (bounded by $\rho_5 \subset L_A$ and $\rho_0$).
- At $C$, the two rays of $L_C$ outside $\triangle ABC$ bound the outer sectors adjacent to $r(C \to A)$ and $r(C \to B)$ on opposite sides of $C$ along $L_C$.
- Thus the outer counted bounded triangular faces across $AB, BC, CA$ are $\triangle A B X_{AB}$, $\triangle B C X_{BC}$, and $\triangle C A X_{CA}$, where
  $$X_{AB} = L_A \cap L_B, \qquad X_{BC} = L_B \cap L_C, \qquad X_{CA} = L_C \cap L_A.$$
- Because $\triangle A B X_{AB}$, $\triangle B C X_{BC}$, and $\triangle C A X_{CA}$ are counted bounded triangular faces, their boundary sides
  $$A X_{AB},\; A X_{CA} \subset L_A, \qquad B X_{AB},\; B X_{BC} \subset L_B, \qquad C X_{BC},\; C X_{CA} \subset L_C$$
  are **elementary segments** of $\mathcal{A}$ (no line of $\mathcal{A}$ crosses their open interiors, and $X_{AB}, X_{BC}, X_{CA}$ are the first arrangement vertices along the respective rays of $L_A, L_B, L_C$ from $A, B, C$).
- Furthermore, because $X_{AB}$ and $X_{CA}$ lie on the opposite rays $\rho_5$ and $\rho_2$ of $L_A$ from $A$ (and cyclically for $B$ and $C$), the lines $L_A, L_B, L_C$ form an outer triangle $\triangle X_{AB} X_{BC} X_{CA}$ with:
  $$A \in \text{int}(X_{AB} X_{CA}), \qquad B \in \text{int}(X_{AB} X_{BC}), \qquad C \in \text{int}(X_{BC} X_{CA}).$$

Now suppose two vertices of $\triangle ABC$, without loss of generality $A$ and $B$, both satisfy $d_2(A)=d_1(A)=2$ and $d_2(B)=d_1(B)=2$.
- By Lemma 2 applied at $A$, the ray $\rho_2(A) = r(A \to X_{CA}) \subset L_A$ is a $D_1$ ray, so its elementary segment $A X_{CA}$ is a **$D_1$ segment**. By the definition of a $D_1$ segment, $A X_{CA}$ has **exactly one** multiple endpoint ($A$) and **one ordinary endpoint**. Hence $X_{CA} = L_C \cap L_A$ is an **ordinary arrangement vertex** of multiplicity $2$, incident **only** to the two arrangement lines $L_A$ and $L_C$.
- By Lemma 2 applied at $B$, the ray $r(B \to X_{BC}) \subset L_B$ is a $D_1$ ray, so its elementary segment $B X_{BC}$ is a **$D_1$ segment**. By the definition of a $D_1$ segment, its non-core endpoint $X_{BC} = L_B \cap L_C$ is an **ordinary arrangement vertex** of multiplicity $2$, incident **only** to the two arrangement lines $L_B$ and $L_C$.
*(Note: In the $q=5$ equality normal form, the ordinary status of $X_{AB}, X_{BC}, X_{CA}$ also follows independently from $h=12$, which forbids any line through $D$ or $E$ from passing through $A, B,$ or $C$ and forbids any extra core-pair line.)*

### 4. Proof of Theorem 2 and Theorem 1 (The Disjoint Outward-Ray Contradiction)

Continue under the hypothesis that $A$ and $B$ both have $d_2=2$ and $d_1=2$.

1. **Forced exterior triangle $F_{A,C}$ across $A X_{CA}$:**
   At vertex $A$, because the elementary segment $A X_{CA} \subset L_A$ is a $D_1$ segment, it is shared by two counted bounded triangular faces of $\mathcal{A}$:
   - on the inward side of $L_A$ (containing $B$ and $C$), the face $\triangle A C X_{CA}$ (in sector $S_1(A)$);
   - on the outward side of $L_A$, a second counted bounded triangular face $F_{A,C}$ (in sector $S_2(A)$, corresponding to $t_2(A) = 1$).
   Because $F_{A,C}$ is a counted bounded triangular face ($3$-cycle of the arrangement graph) containing the elementary segment $A X_{CA}$ as one of its three edges, two of the three vertices of $F_{A,C}$ are $A$ and $X_{CA}$. Let $Y_{A,C}$ denote the third vertex of $F_{A,C}$.
   - At vertex $A$, sector $S_2(A)$ is bounded by $\rho_2(A) = r(A \to X_{CA}) \subset L_A$ and $\rho_3(A) = r_{\text{out}}(BA) = \{ A + t(A - B) : t > 0 \} \subset AB$. Therefore, the edge $A Y_{A,C}$ of $F_{A,C}$ lies along the open ray $r_{\text{out}}(BA)$, so
     $$Y_{A,C} \in r_{\text{out}}(BA).$$
   - At the ordinary vertex $X_{CA} = L_C \cap L_A$ (multiplicity $2$), the **only** incident arrangement lines are $L_A$ and $L_C$. Since the edge $A X_{CA}$ lies on $L_A$ and $Y_{A,C} \notin L_A$, the third edge $X_{CA} Y_{A,C}$ of $F_{A,C}$ incident to $X_{CA}$ **must** lie on the line $L_C$. Therefore,
     $$Y_{A,C} \in L_C.$$
   Combining these two incidences gives:
   $$Y_{A,C} \in r_{\text{out}}(BA) \cap L_C \implies r_{\text{out}}(BA) \cap L_C \ne \emptyset.$$

2. **Forced exterior triangle $F_{B,C}$ across $B X_{BC}$:**
   At vertex $B$, the cyclic order of the six rays around $B$ places $r(B \to A)$ and $r(B \to C)$ as the two inward $D_2$ rays, $r(B \to X_{BC}) \subset L_B$ adjacent to $r(B \to C)$, and the open outward continuation ray
   $$r_{\text{out}}(AB) = \{ B + s(B - A) : s > 0 \} \subset AB$$
   (opposite to $r(B \to A)$) immediately adjacent to $r(B \to X_{BC})$ on the outward side of $L_B$.
   Because the elementary segment $B X_{BC} \subset L_B$ is a $D_1$ segment, it is shared by $\triangle B C X_{BC}$ (on the inward side of $L_B$) and a second counted bounded triangular face $F_{B,C}$ (on the outward side of $L_B$, bounded at $B$ by $r(B \to X_{BC})$ and $r_{\text{out}}(AB)$).
   Two of the three vertices of $F_{B,C}$ are $B$ and $X_{BC}$. Let $Y_{B,C}$ be the third vertex of $F_{B,C}$.
   - At $B$, the edge $B Y_{B,C}$ lies along the open ray $r_{\text{out}}(AB)$, so $Y_{B,C} \in r_{\text{out}}(AB)$.
   - At the ordinary vertex $X_{BC} = L_B \cap L_C$ (multiplicity $2$), the **only** incident arrangement lines are $L_B$ and $L_C$. Since $B X_{BC} \subset L_B$, the edge $X_{BC} Y_{B,C}$ of $F_{B,C}$ **must** lie on $L_C$, so $Y_{B,C} \in L_C$.
   Combining these two incidences gives:
   $$Y_{B,C} \in r_{\text{out}}(AB) \cap L_C \implies r_{\text{out}}(AB) \cap L_C \ne \emptyset.$$

3. **Affine Line-Intersection Contradiction:**
   - On the straight line $AB$, the two open outward rays $r_{\text{out}}(BA) = \{ A + t(A - B) : t > 0 \}$ and $r_{\text{out}}(AB) = \{ B + s(B - A) : s > 0 \}$ are strictly disjoint:
     $$r_{\text{out}}(BA) \cap r_{\text{out}}(AB) = \emptyset.$$
   - The line $AB$ is distinct from $L_C$: indeed, $A \in \text{int}(X_{AB} X_{CA}) \subset L_A \setminus \{X_{CA}\}$, and since $L_A \cap L_C = \{X_{CA}\}$, we have $A \notin L_C$, whereas $A \in AB$.
   - Two distinct straight lines $AB$ and $L_C$ in the affine plane intersect in at most one point (and in a unique point under pairwise nonparallelism). Therefore, $L_C$ cannot intersect both disjoint open rays $r_{\text{out}}(BA)$ and $r_{\text{out}}(AB)$:
     $$\bigl(r_{\text{out}}(BA) \cap L_C\bigr) \cap \bigl(r_{\text{out}}(AB) \cap L_C\bigr) = \emptyset \implies \text{at least one of } r_{\text{out}}(BA) \cap L_C,\; r_{\text{out}}(AB) \cap L_C \text{ is empty.}$$
   This contradiction proves that $A$ and $B$ cannot both have $(d_2, d_1) = (2, 2)$. By symmetry, at most one vertex of $\triangle ABC$ can have $(d_2, d_1) = (2, 2)$. At any triple core $V$ with $d_2(V)=2$, the triple fan refinement ($d_1(V)=3 \implies d_2(V)=3$) gives $d_1(V) \le 2$; since at most one of $A, B, C$ can attain $d_1(V)=2$, the other two satisfy $d_1 \le 1$, proving $d_1(A) + d_1(B) + d_1(C) \le 4$. This establishes **Theorem 2**. $\square$

4. **Deduction of Theorem 1 (Closure of $q=5$):**
   In the sole surviving $q=5$ normal form (`K3_PLUS_TWO_ISOLATED`, `H1_12_STATUS.json`), the three triple cores $A, B, C$ form a $K_3$ component in the $D_2$ graph with $d_2(A)=d_2(B)=d_2(C)=2$ and $d_1(A)=d_1(B)=d_1(C)=2$ (requiring all six exterior faces $F_{A,C}, F_{B,C}, F_{B,A}, F_{C,A}, F_{C,B}, F_{A,B}$ simultaneously). By Theorem 2, this configuration is impossible (indeed, it fails three times over, once across each side $AB, BC, CA$ of $\triangle ABC$). Therefore, no $q=5$ witness survives, and any normalized $n=18, T=95$ witness must satisfy $q \ge 6$. $\square$

### 5. Explicit Coordinate Verification on the Outer Triangle $\triangle X_{CA} X_{AB} X_{BC}$

To provide an independent algebraic cross-check of Step 4, choose an affine coordinate chart in which the outer triangle $\triangle X_{CA} X_{AB} X_{BC}$ has vertices:
$$X_{CA} = (0, 0), \qquad X_{AB} = (1, 0), \qquad X_{BC} = (0, 1),$$
so that $L_A$ is the line $y = 0$, $L_C$ is the line $x = 0$, and $L_B$ is the line $x + y = 1$. Since $A \in \text{int}(X_{CA} X_{AB})$, $B \in \text{int}(X_{AB} X_{BC})$, and $C \in \text{int}(X_{CA} X_{BC})$, there exist unique reals $\alpha, \beta, \gamma \in (0, 1)$ such that:
$$A = (\alpha, 0), \qquad B = (1 - \beta, \beta), \qquad C = (0, \gamma).$$
Now compute the ray-line intersection conditions for all six required exterior triangular faces:
- **Face $F_{A,C}$ ($r_{\text{out}}(BA) \cap L_C \ne \emptyset$):**
  A point on $r_{\text{out}}(BA)$ has the form $A + t(A - B) = \bigl(\alpha + t(\alpha + \beta - 1),\; -\beta t\bigr)$ with $t > 0$. It lies on $L_C$ ($x = 0$) if and only if $(1 - \alpha - \beta)t = \alpha$; since $\alpha > 0$, a solution $t > 0$ exists if and only if
  $$\alpha + \beta < 1.$$
- **Face $F_{B,C}$ ($r_{\text{out}}(AB) \cap L_C \ne \emptyset$):**
  A point on $r_{\text{out}}(AB)$ has the form $B + s(B - A) = \bigl(1 - \beta + s(1 - \alpha - \beta),\; \beta(1 + s)\bigr)$ with $s > 0$. It lies on $L_C$ ($x = 0$) if and only if $(\alpha + \beta - 1)s = 1 - \beta$; since $1 - \beta > 0$, a solution $s > 0$ exists if and only if
  $$\alpha + \beta > 1.$$
- **Face $F_{A,B}$ ($r_{\text{out}}(CA) \cap L_B \ne \emptyset$) vs. Face $F_{C,B}$ ($r_{\text{out}}(AC) \cap L_B \ne \emptyset$):**
  On $r_{\text{out}}(CA)$, $A + t(A - C) = \bigl(\alpha(1+t), -\gamma t\bigr)$ ($t > 0$) meets $L_B$ ($x + y = 1$) at $(\alpha - \gamma)t = 1 - \alpha > 0 \iff \alpha > \gamma$.
  On $r_{\text{out}}(AC)$, $C + s(C - A) = \bigl(-\alpha s, \gamma(1+s)\bigr)$ ($s > 0$) meets $L_B$ ($x + y = 1$) at $(\gamma - \alpha)s = 1 - \gamma > 0 \iff \alpha < \gamma$.
- **Face $F_{B,A}$ ($r_{\text{out}}(CB) \cap L_A \ne \emptyset$) vs. Face $F_{C,A}$ ($r_{\text{out}}(BC) \cap L_A \ne \emptyset$):**
  On $r_{\text{out}}(CB)$, $B + t(B - C) = \bigl((1-\beta)(1+t), \beta + t(\beta - \gamma)\bigr)$ ($t > 0$) meets $L_A$ ($y = 0$) at $(\gamma - \beta)t = \beta > 0 \iff \beta < \gamma$.
  On $r_{\text{out}}(BC)$, $C + s(C - B) = \bigl(-(1-\beta)s, \gamma + s(\gamma - \beta)\bigr)$ ($s > 0$) meets $L_A$ ($y = 0$) at $(\beta - \gamma)s = \gamma > 0 \iff \beta > \gamma$.

Thus the six exterior triangular sectors of the $q=5$ equality normal form require the simultaneous strict inequalities:
$$\begin{cases} \alpha + \beta < 1 \quad \text{and} \quad \alpha + \beta > 1, \\ \alpha > \gamma \quad \text{and} \quad \alpha < \gamma, \\ \beta < \gamma \quad \text{and} \quad \beta > \gamma, \end{cases}$$
each pair of which is individually inconsistent over $\mathbb{R}$.

## Assumptions beyond bootstrap

NONE

## Verification / falsification hooks

1. **Direct Falsification Hook (Single-Coordinate Challenge):**
   To falsify Theorem 1 or Theorem 2, it suffices to exhibit any three real numbers $\alpha, \beta, \gamma \in (0, 1)$ (or any three lines $L_A, L_B, L_C$ and interior side points $A, B, C$ in $\mathbb{R}^2$) for which the line $AB$ intersects the line $L_C$ on both the open ray $r_{\text{out}}(BA) = \{A + t(A-B) : t > 0\}$ and the open ray $r_{\text{out}}(AB) = \{B + s(B-A) : s > 0\}$, i.e., satisfying both $\alpha + \beta < 1$ and $\alpha + \beta > 1$. Because no such real numbers exist, the exclusion of the nested-triangle $D_1$-saturated core skeleton is unconditional with respect to the positions of the remaining lines of $\mathcal{A}$.

2. **Finite Replay Hook Extending `ci/validate_openmath_h1_12_q5_equality.py`:**
   Any verifier can reproduce the finite sector enumeration and the exact ray-intersection contradiction by running the following self-contained Python 3 verification procedure:
   - Enumerate all $2^6 = 64$ sector bit-tuples $(t_0, \dots, t_5) \in \{0, 1\}^6$ at a triple core $V$ with $d_2(V)=2$ at adjacent rays $0, 1$ (`shared[i] = t[i-1] & t[i]`, `shared[0] == shared[1] == 1`).
   - Filter to tuples with `d1 == 2` (`sum(shared) == 4`) and no two cyclically consecutive $D_1$ rays. Verify that `((1, 1, 1, 0, 1, 1), (2, 2, 1, 0, 0, 1))` is the unique surviving local word.
   - For each of the three central edges $(X, Y) \in \{(A, B), (B, C), (C, A)\}$ with third vertex $Z$, verify that $t_2 = 1$ and $t_4 = 1$ at $X$ and $Y$ require the open rays $r_{\text{out}}(YX)$ and $r_{\text{out}}(XY)$ on line $XY$ to both intersect line $L_Z$ at ordinary endpoint extensions of $X X_{ZX}$ and $Y X_{YZ}$, which forces the mutually exclusive affine sign conditions $\Phi_{XY} < 0$ and $\Phi_{XY} > 0$ (where $\Phi_{AB} = \alpha + \beta - 1$, $\Phi_{CA} = \gamma - \alpha$, $\Phi_{BC} = \beta - \gamma$).
   - Applying the Theorem 2 constraint `sum(d1(v) for v in K3) <= 4` to the $q=5$ profile `33333` orbit `K3_PLUS_TWO_ISOLATED` lowers the maximum possible total $D_1$ on that graph from $2+2+2+2+2 = 10$ to $4 + 2 + 2 = 8$, which forces $U = 3 - 15 + D_1 + 3 = D_1 - 9 \le -1 < 0$ and eliminates the sole $q=5$ survivor at the arithmetic level as well.

## Claim boundary

This result does not prove the hill-global upper bound $K_{\text{hill}}(18) \le 94$, does not exclude score-95 arrangements with $q \ge 6$ finite multiple points, does not remove the source-scoped dependency on the local fan and clean-line charging premises used to reach the $q=5$ normal form, and does not constitute GCL claim admission or MATHCERT certification.

## Next residual

Conditional on the named source-scoped local fan and clean-line charging premises, all $q \le 5$ normalized $n=18, T=95$ arrangements are now excluded and the remaining H1-12 frontier consists solely of arrangements with $q \ge 6$ finite multiple points. The immediate next mathematical target is the $q=6$ stratum, starting with its 14 coarse multiplicity profiles satisfying $\sum_{i=1}^6 r_i(r_i - 4) \le 0$ and applying sector-consistent local option enumeration, extreme-core saturation bounds, and the Theorem 2 $K_3$ component bound $d_1(A)+d_1(B)+d_1(C) \le 4$. Independently discharging the source-scoped local fan and clean-line charging premises from first principles remains a parallel obligation for an unconditional proof.

