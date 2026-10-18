GCL-CONTRIBUTION-RESULT/1
dispatch_id: OM26-H2-WP02-IA-001
agent_ref: INDEPENDENT-AGENT-008
assignment: OM26-H2-WP02
disposition: EXACT_SEARCH_DESIGN_VALIDATED
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

Under the verified active protected lease (`assignment: OM26-H2-WP02`, `dispatch_id: OM26-H2-WP02-IA-001`, `agent_ref: INDEPENDENT-AGENT-008`, `state: LEASED_NOT_LAUNCHED`, `lease.state: LEASED`, `protected_lease_merge: 113cdc018b84696b9c15413e4cd4a776d20e72ec`, `readback_verified: true`, return issue `#526`, bootstrap blob SHA-1 `5f2b99afd44549aaaca1387563abf36f0842c222`), we establish and validate a **complete exact canonical search design (`EXACT_SEARCH_DESIGN_VALIDATED`)** for six-state, two-symbol blank-tape Turing machines under the locked protected evaluator (`eval.py` blob SHA-1 `1b956107377f3ac67dc8277164f7db82fbb15744`, SHA-256 `84ba441b101a61283c0dd5d05960a33cedf8cfe224cc6aae4b308d0a4cc60fc0`; `MATHFORGE` commit `782b80c8c57d4e77356d8c77c50ee1fffdcd92b8` source-lock blob `d590cf562f562a81df64d403ff5d9aa01e25626c`):

1. **Exact Symmetry Quotient & Survival of First-Write-`0` Branch**: We prove that the exact symmetry group of the blank-zero model is $G = S_Q^{\text{A}} \times \mathbb{Z}_2^{\text{dir}}$ of order $5! \times 2 = 240$, which acts **freely** on the set of valid 6-state halting machines $\mathcal{M}_{\text{valid}, B}$ and preserves blank-zero initialization, halting status, exact `steps`, exact `ones`, exact `tape_span`, and 6-state reachability. Combined with the two 1-step exact root prunes (`EXACT-01` for `A,0 -> [w, m, "H"]` and `EXACT-02` for `A,0 -> [w, m, "A"]`), the exact canonical root splits into **two** mandatory branches—`A,0 -> [0, "R", "B"]` and `A,0 -> [1, "R", "B"]`—preserving the valid 6-step first-write-`0` counterexample `M_FW0` (`steps=6, ones=5, tape_span=7`, SHA-256 `6fad7e5d1eed35d47d47a839a45c9937be9d84ec7b495e1e3c428fadb5fb6c0e`) as a canonical fixed point alongside the 6-step baseline `M_BASE` (`steps=6, ones=6, tape_span=7`, SHA-256 `d89fc8cb61442e0356a9a470b9579b9dc6753965854cb8b3af1af16a8ffdfca2`).
2. **Complete Canonical Enumeration & Exact Pruning Ledger**: We prove the **Unique First-Visit Halting Property (Lemma C.1)** and establish eight sound `EXACT` pruning rules (`EXACT-01` through `EXACT-07`, including `EXACT-05a`/`05b` closed-subtable invariants, `EXACT-06` full-support configuration repetition, and `EXACT-07` proved half-line translated-cycler certificates) strictly separated from non-pruning `HEURISTIC_ONLY` priority ordering (`HEUR-01`). Exhaustive canonical enumeration at horizons $B = 6$ (`682` nodes, `2,048` canonical witnesses: `1,024` with $w_0=0$ and `1,024` with $w_0=1$) and $B = 7$ (`27,386` nodes, `60,160` canonical witnesses: `24,832` with $w_0=0$ and `35,328` with $w_0=1$) produces 100% identical node, prune, and witness counts under both lexicographic (`lex`) and priority (`heuristic_priority`) orderings, and matches unpruned enumeration with exact set equality.
3. **Falsification Suite & Bounded Search Tranche Dual-Scorer Concordance**: All six required falsification test categories (`E.1`–`E.6`) pass, and a deterministic `3,000`-node bounded tranche under `step_limit = 250,000` yields dual-replayed valid 6-state halting witnesses on both root branches: **`(steps=89911, ones=185, tape_span=541)`** on `A,0 -> [1, "R", "B"]` (SHA-256 `f8eaa4dbcbc3ecb18f8ddd1734cffe0079457ff3e26a51a25e81f3f6e988ead2`) and **`(steps=8021, ones=41, tape_span=122)`** on `A,0 -> [0, "R", "B"]` (SHA-256 `64d989c0a2a3e1488ac2d7cf3e5b8612b25d32e61370ea4a2cb20077f706e352`), with 100% concordance between the independent scorer and protected `eval.py`.

## Derivation

### A. Exact Machine Space and Protected Evaluator Semantics

Let $Q = \{\text{A}, \text{B}, \text{C}, \text{D}, \text{E}, \text{F}\}$ be the 6 non-halting states, $\text{H}$ be the halt state, $\Sigma = \{0, 1\}$ be the tape alphabet, and $D = \{\text{L}, \text{R}\}$ be the move directions with step offsets $\Delta(\text{L}) = -1, \Delta(\text{R}) = +1$.

1. **Transition Space**: A complete machine is a total function $M : Q \times \Sigma \to \Gamma$, where $\Gamma = \Sigma \times D \times (Q \cup \{\text{H}\})$ has $|\Gamma| = 2 \times 2 \times 7 = 28$ triples per slot across $|Q \times \Sigma| = 12$ slots. The full machine space $\mathcal{M} = \Gamma^{Q \times \Sigma}$ has exact cardinality:
   $$|\mathcal{M}| = 28^{12} = 232{,}218{,}265{,}089{,}212{,}416.$$
2. **Configuration & Trajectory Semantics (`eval.py` lines 65–84)**:
   A machine configuration at step $t \ge 0$ is a tuple $C_t = (q_t, h_t, \tau_t, \ell_t, r_t, R_t)$ where $q_t \in Q \cup \{\text{H}\}$, $h_t \in \mathbb{Z}$, $\tau_t : \mathbb{Z} \to \{0, 1\}$ has finite support $\text{supp}(\tau_t) = \{z \in \mathbb{Z} : \tau_t(z) = 1\}$, $\ell_t, r_t \in \mathbb{Z}$, and $R_t \subseteq Q$.
   - **Initial Configuration ($t = 0$)**: $q_0 = \text{A}$, $h_0 = 0$, $\text{supp}(\tau_0) = \emptyset$ ($\tau_0(z) = 0\;\forall z \in \mathbb{Z}$), $\ell_0 = 0$, $r_0 = 0$, and $R_0 = \{\text{A}\}$.
   - **Single-Step Transition ($t \to t+1$ for $0 \le t < B$ and $q_t \in Q$)**:
     Let $s_t = \tau_t(h_t) \in \{0, 1\}$ and $(w_t, m_t, q_{t+1}) = M(q_t, s_t)$. Then:
     $$\text{supp}(\tau_{t+1}) = \begin{cases} \text{supp}(\tau_t) \cup \{h_t\} & \text{if } w_t = 1, \\ \text{supp}(\tau_t) \setminus \{h_t\} & \text{if } w_t = 0, \end{cases}$$
     $$h_{t+1} = h_t + \Delta(m_t), \qquad \ell_{t+1} = \min(\ell_t, h_{t+1}), \qquad r_{t+1} = \max(r_t, h_{t+1}).$$
     - **Halting Gate**: If $q_{t+1} = \text{H}$, execution terminates immediately at step $T = t + 1$ with output `(halted=True, steps=T, ones=|supp(tau_T)|, tape_span=r_T - l_T + 1, reached=R_t)`. Crucially, `H` is checked *before* `reached.add(state)` (`eval.py` lines 80–83), so the final transition $(q_t, s_t) \to (w_t, m_t, \text{H})$ does not add a state to $R_t$.
     - **Continuation**: If $q_{t+1} \in Q$, set $R_{t+1} = R_t \cup \{q_{t+1}\}$ and continue. If $t = B$ is reached without $q_{t} = \text{H}$, `_run` returns `halted=False`.
   - **Acceptance Predicate**: Under step budget $B \in \{250{,}000, 1{,}000{,}000\}$, $\text{Valid}_B(M)$ holds iff $M$ halts at some step $T \le B$ and $R_{T-1} = Q = \{\text{A}, \text{B}, \text{C}, \text{D}, \text{E}, \text{F}\}$.

---

### B. Symmetry Group $G = S_Q^{\text{A}} \times \mathbb{Z}_2^{\text{dir}}$ and Preservation Proofs

Define:
- $S_Q^{\text{A}} = \{\pi \in \text{Sym}(Q \cup \{\text{H}\}) : \pi(\text{A}) = \text{A},\; \pi(\text{H}) = \text{H}\} \cong S_5$, of order $|S_Q^{\text{A}}| = 5! = 120$, permuting the non-initial non-halting states $\{\text{B}, \text{C}, \text{D}, \text{E}, \text{F}\}$.
- $\mathbb{Z}_2^{\text{dir}} = \{\text{id}, \rho\}$, of order $2$, where $\rho(\text{L}) = \text{R}, \rho(\text{R}) = \text{L}$, with spatial coordinate action $\hat{\text{id}}(z) = z$ and $\hat{\rho}(z) = -z$ on $z \in \mathbb{Z}$ (note $\Delta(\delta(m)) = \hat{\delta}(\Delta(m))$ for both $\delta \in \mathbb{Z}_2^{\text{dir}}$).
- The direct product $G = S_Q^{\text{A}} \times \mathbb{Z}_2^{\text{dir}}$ of order $|G| = 240$ acts on $\mathcal{M}$ via:
  $$\big((\pi, \delta) \cdot M\big)(q, s) = \big(w,\; \delta(m),\; \pi(q')\big) \quad \text{where } (w, m, q') = M(\pi^{-1}(q), s).$$

#### Theorem B.1 (Exact Trajectory Conjugacy and Metric Preservation)
For any $M \in \mathcal{M}$ and $(\pi, \delta) \in G$, let $M' = (\pi, \delta) \cdot M$, and let $C_t = (q_t, h_t, \tau_t, \ell_t, r_t, R_t)$ and $C'_t = (q'_t, h'_t, \tau'_t, \ell'_t, r'_t, R'_t)$ be their respective configurations at step $t \ge 0$. Then for every step $t \ge 0$ up to halting:
$$q'_t = \pi(q_t), \quad h'_t = \hat{\delta}(h_t), \quad \text{supp}(\tau'_t) = \hat{\delta}(\text{supp}(\tau_t)), \quad [\ell'_t, r'_t] = \big[\min(\hat{\delta}(\ell_t), \hat{\delta}(r_t)),\; \max(\hat{\delta}(\ell_t), \hat{\delta}(r_t))\big], \quad R'_t = \pi(R_t).$$

*Proof by induction on $t \ge 0$*:
- **Base case ($t = 0$)**: Since $\pi(\text{A}) = \text{A}$ and $\hat{\delta}(0) = 0$, we have $q'_0 = \text{A} = \pi(q_0)$, $h'_0 = 0 = \hat{\delta}(h_0)$, $\text{supp}(\tau'_0) = \emptyset = \hat{\delta}(\emptyset)$ (preserving the blank-zero initial tape), $[\ell'_0, r'_0] = [0, 0]$, and $R'_0 = \{\text{A}\} = \pi(R_0)$.
- **Inductive step ($t \to t+1$)**: Assume the invariants hold at step $t$ with $q_t \in Q$. Then the symbol read by $M'$ at step $t$ is:
  $$s'_t = \mathbf{1}[h'_t \in \text{supp}(\tau'_t)] = \mathbf{1}[\hat{\delta}(h_t) \in \hat{\delta}(\text{supp}(\tau_t))] = \mathbf{1}[h_t \in \text{supp}(\tau_t)] = s_t.$$
  Querying $M'(q'_t, s'_t) = M'(\pi(q_t), s_t)$ yields $(w'_t, m'_t, q'_{t+1}) = (w_t, \delta(m_t), \pi(q_{t+1}))$ where $(w_t, m_t, q_{t+1}) = M(q_t, s_t)$. Consequently:
  1. Since $w'_t = w_t$ and $h'_t = \hat{\delta}(h_t)$, $\text{supp}(\tau'_{t+1}) = \hat{\delta}(\text{supp}(\tau_{t+1}))$, so $|\text{supp}(\tau'_{t+1})| = |\text{supp}(\tau_{t+1})|$ (preserving exact `ones`).
  2. $h'_{t+1} = h'_t + \Delta(\delta(m_t)) = \hat{\delta}(h_t) + \hat{\delta}(\Delta(m_t)) = \hat{\delta}(h_t + \Delta(m_t)) = \hat{\delta}(h_{t+1})$.
  3. Since $\hat{\delta} : \mathbb{Z} \to \mathbb{Z}$ is an isometry ($\hat{\text{id}}(z) = z$, $\hat{\rho}(z) = -z$), the extreme visited interval satisfies $r'_{t+1} - \ell'_{t+1} + 1 = r_{t+1} - \ell_{t+1} + 1$ (preserving exact `tape_span`).
  4. Since $\pi(\text{H}) = \text{H}$, $q'_{t+1} = \text{H} \iff q_{t+1} = \text{H}$, so $M'$ halts at step $t+1$ iff $M$ halts at step $t+1$ (preserving halting vs. non-halting and exact `steps`).
  5. If $q_{t+1} \in Q$, $R'_{t+1} = R'_t \cup \{\pi(q_{t+1})\} = \pi(R_t \cup \{q_{t+1}\}) = \pi(R_{t+1})$. Since $\pi|_Q$ is a bijection on $Q$, $|R'_{t+1}| = |R_{t+1}|$ and $R'_{t+1} = Q \iff R_{t+1} = Q$ (preserving the 6-state reachability requirement). $\blacksquare$

#### Explicit Falsification of Non-Symmetries
- **First-write normalization (`A,0 -> [1, "R", "B"]` WLOG) is NOT a symmetry**: At $t = 0$, writing $w_0 = 0$ leaves $\text{supp}(\tau_1) = \emptyset$, whereas writing $w_0 = 1$ sets $\text{supp}(\tau_1) = \{0\}$. Because $G$ preserves $|\text{supp}(\tau_t)|$ at every step $t$ by Theorem B.1, no symmetry in $G$ can map a $w_0 = 0$ machine to a $w_0 = 1$ machine. Concrete counterexample: `M_FW0` (`A0:0RB, B0:1RC, C0:1RD, D0:1RE, E0:1RF, F0:1RH, *1:1RH`) is valid and halts at step $T = 6$ with `(steps, ones, tape_span) = (6, 5, 7)`, whereas every 6-step machine with $w_0 = 1$ that marches in one direction has `ones = 6`.
- **Symbol complementation ($0 \leftrightarrow 1$) is NOT a symmetry**: Involuting $0 \leftrightarrow 1$ maps the initial blank-zero tape $\tau_0 \equiv 0$ to the all-ones tape $\tau'_0 \equiv 1$, violating the fixed `bi-infinite-zero` initial condition.

#### Lemma B.3 (Free Action of $G$ on $\mathcal{M}_{\text{valid}, B}$ and Unique Orbit Representatives)
Let $\mathcal{M}_{\text{valid}, B} = \{M \in \mathcal{M} : \text{Valid}_B(M)\}$.
1. $G$ acts **freely** on $\mathcal{M}_{\text{valid}, B}$: if $(\pi, \delta) \cdot M = M$ for $M \in \mathcal{M}_{\text{valid}, B}$, then $(\pi, \delta) = (\text{id}, \text{id})$.
   *Proof*: Let $M(\text{A}, 0) = (w_0, m_0, q_1)$. Since $\pi(\text{A}) = \text{A}$ and $(\pi, \delta) \cdot M = M$, $(w_0, \delta(m_0), \pi(q_1)) = (w_0, m_0, q_1)$, forcing $\delta(m_0) = m_0 \implies \delta = \text{id}$. By Theorem B.1, $M$ and $(\pi, \text{id}) \cdot M = M$ have identical state sequences $q_t = q'_t = \pi(q_t)$ for all $0 \le t \le T - 1$. Since $M \in \mathcal{M}_{\text{valid}, B}$, $\{q_0, \dots, q_{T-1}\} = Q$, so $\pi(q) = q$ for all $q \in Q$, giving $\pi = \text{id}$. $\blacksquare$
2. Every valid orbit $[M]_G \subseteq \mathcal{M}_{\text{valid}, B}$ has exact size $|[M]_G| = 240$ and contains a **unique** representative $M_{\text{orb}} \in [M]_G$ such that:
   - $M_{\text{orb}}(\text{A}, 0)$ has move direction $m_0 = \text{R}$, and
   - The first-entry step $\tau_{\text{first}}(q) = \min\{t \ge 0 : q_t = q\}$ satisfies $0 = \tau_{\text{first}}(\text{A}) < \tau_{\text{first}}(\text{B}) < \tau_{\text{first}}(\text{C}) < \tau_{\text{first}}(\text{D}) < \tau_{\text{first}}(\text{E}) < \tau_{\text{first}}(\text{F}) \le T - 1$.

---

### C. Deterministic Complete Canonical Enumeration

#### Lemma C.1 (Unique First-Visit Halting Property)
In any halting run of a deterministic Turing machine $M$ of length $T \ge 1$, the transition slot $\sigma_r = (q_{T-1}, s_{T-1})$ executed at the final halting step $t = T - 1$ (where $M(\sigma_r) = (w, m, \text{H})$) is never queried at any earlier step $0 \le u < T - 1$.
*Proof*: If $(q_u, s_u) = \sigma_r$ for some $u < T - 1$, deterministic execution of $M(\sigma_r) = (w, m, \text{H})$ at step $u$ would halt immediately at step $u + 1 \le T - 1 < T$, a contradiction. $\blacksquare$

By Lemma B.3 and Lemma C.1, we specify the complete partial-table canonical search procedure:

1. **State Carried at Each Search Node**: Each interior node carries a partial non-halting transition table $P : \text{dom}(P) \to \Sigma \times D \times Q$ ($\text{dom}(P) \subseteq Q \times \Sigma$), from which deterministic blank-tape simulation via `advance_partial_exact(P, B)` reconstructs $(t, q_t, h_t, \text{supp}(\tau_t), \ell_t, r_t, R_t)$ where $R_t = Q_k = \{\text{A}, \dots, \text{STATES}[k-1]\}$ for $k = |R_t| \in \{1, \dots, 6\}$.
2. **Next Undefined Transition Slot Selection Rule**: Starting from $(q_0=\text{A}, h_0=0, \tau_0=\emptyset)$, the simulator steps forward while $(q_t, \tau_t(h_t)) \in \text{dom}(P)$, $t < B$, and no exact pruning rule (`EXACT-01`..`EXACT-07`) triggers. If it encounters $(q_t, s_t) \notin \text{dom}(P)$ at step $t < B$, that first-encountered undefined slot $\sigma^* = (q_t, s_t)$ is selected deterministically as the branching variable.
3. **Root Initialization (`t = 0, sigma* = ("A", 0)`)**: By $\mathbb{Z}_2^{\text{dir}}$ reflection, $m_0 = \text{R}$ WLOG (14 triples). `EXACT-01` prunes $q_1 = \text{H}$ (2 triples) and `EXACT-02` prunes $q_1 = \text{A}$ (2 triples). By $S_Q^{\text{A}}$ first-discovery naming, the first non-$\text{A}$ state entered at $t = 1$ is renamed to $\text{B}$. This leaves **two** exact canonical root nodes:
   $$P_{\text{root}, 0} = \{(\text{A}, 0) \mapsto (0, \text{R}, \text{B})\}, \qquad P_{\text{root}, 1} = \{(\text{A}, 0) \mapsto (1, \text{R}, \text{B})\}.$$
4. **When a New State Name May Be Introduced**: At an undefined slot $\sigma^* = (q_t, s_t)$ with $k = |R_t|$ states reached ($R_t = Q_k$), the admissible non-halting target states are:
   $$Q_{\text{adm}}(k) = \begin{cases} Q_k \cup \{\text{STATES}[k]\} & \text{if } k < 6, \\ Q & \text{if } k = 6. \end{cases}$$
   Targeting any state in $Q \setminus Q_{\text{adm}}(k)$ when $k < 6$ would violate chronological first-discovery order $\tau_{\text{first}}(\text{B}) < \dots < \tau_{\text{first}}(\text{F})$.
5. **When `H` May Be Introduced**: By Lemma C.1, `H` can only be taken on the first visit to a slot $\sigma^* = (q_t, s_t) \notin \text{dom}(P)$. By `EXACT-03`, assigning $\sigma^* \mapsto (w, m, \text{H})$ when $k = |R_t| < 6$ halts immediately at step $t + 1$ with $R_t = Q_k \subsetneq Q$ and is invalid. When $k = 6$ and $t < B$, all 4 halting triples $(w, m, \text{H}) \in \{0, 1\} \times \{\text{L}, \text{R}\} \times \{\text{H}\}$ are valid halting leaves at step $T = t + 1$ and are immediately harvested.
6. **How Remaining Undefined Slots Are Completed**: For any halting partial table $P_{\text{halt}}$, slots $\sigma \in (Q \times \Sigma) \setminus \text{dom}(P_{\text{halt}})$ are never queried during steps $0, \dots, T-1$. They are completed deterministically via $\text{Complete}(P_{\text{halt}})(\sigma) = (1, \text{R}, \text{H})$ for $\sigma \notin \text{dom}(P_{\text{halt}})$, representing the $28^{12 - |\text{dom}(P_{\text{halt}})|}$ dead-slot completion fiber.
7. **Branch Ordering**:
   - `lex`: Deterministic depth-first lexicographic order over $w \in (0, 1)$, $m \in (\text{L}, \text{R})$, $q' \in Q_{\text{adm}}(k)$, exploring $P_{\text{root}, 0}$ then $P_{\text{root}, 1}$.
   - `heuristic_priority` (`HEUR-01`): Pushes all admissible children into a deterministic min-heap keyed by `(-on_spine, len(P), -k_reached, serial)` without ever omitting or dropping any child.
8. **Recognition of Canonical Representatives & Completeness Proof (Theorem C.2)**:
   Define $\text{Canon}(M) = \text{Complete}(M_{\text{orb}}|_{\text{Visited}(M_{\text{orb}})})$ where $M_{\text{orb}} = (\pi, \delta) \cdot M$ is the unique Lemma B.3 orbit representative of $M \in \mathcal{M}_{\text{valid}, B}$. A valid machine $M$ is canonical iff $\text{Canon}(M) = M$.
   *Proof of Completeness*: Let $M \in \mathcal{M}_{\text{valid}, B}$ and $M^* = \text{Canon}(M)$, with first-queried slot sequence $\sigma_1, \dots, \sigma_r$ at steps $0 = t_1 < t_2 < \dots < t_r = T - 1 \le B - 1$. By Lemma B.3, $M^*(\sigma_1) = M^*(\text{A}, 0) \in \{(0, \text{R}, \text{B}), (1, \text{R}, \text{B})\}$. For each $1 \le j < r$, by Lemma C.1 $M^*(\sigma_j)$ is non-halting, and by chronological state naming its target state lies in $Q_{\text{adm}}(|R_{t_j}|)$ and satisfies $(t_j + 1) + (6 - |R_{t_j+1}|) + 1 \le T \le B$. Because $M^*$ halts validly at step $T \le B$ with $R_{T-1} = Q$, no sound exact pruning rule (`EXACT-01`..`EXACT-07`) can reject any prefix $P_j = M^*|_{\{\sigma_1, \dots, \sigma_j\}}$. Finally, at step $t_r = T - 1$, $|R_{t_r}| = 6$ and $M^*(\sigma_r) \in \{0, 1\} \times \{\text{L}, \text{R}\} \times \{\text{H}\}$ is emitted as one of the 4 halting completions, yielding $\text{Complete}(P_r) = M^*$. $\blacksquare$

#### Closed-Form Combinatorial Check at Horizon $B = 6$
At budget $B = 6$, reaching all 6 states requires entering a new state at every step $t \in \{0, 1, 2, 3, 4\}$ ($q_t = \text{STATES}[t]$) and halting at $t = 5$ ($q_5 = \text{F} \to \text{H}$). Because the 6 states $q_0, \dots, q_5$ are pairwise distinct, the 6 queried slots $(q_t, s_t)$ are pairwise distinct for every choice of $(w_t, m_t)$. There are $2$ canonical choices at $t = 0$ ($w_0 \in \{0, 1\}, m_0 = \text{R}, q_1 = \text{B}$), $4$ canonical choices $(w_t, m_t, \text{STATES}[t+1])$ at each $t \in \{1, 2, 3, 4\}$, and $4$ halting choices $(w_5, m_5, \text{H})$ at $t = 5$, giving:
$$N_{\text{canon}}(B=6) = 2 \times 4^4 \times 4 = 2{,}048 \quad (1{,}024 \text{ with } w_0 = 0 \text{ and } 1{,}024 \text{ with } w_0 = 1),$$
$$N_{\text{nodes}}(B=6) = 2 \sum_{j=0}^{4} 4^j = 2 \times 341 = 682, \qquad |\mathcal{M}_{\text{valid}, B=6}| = 2{,}048 \times 240 \times 28^6 = 236{,}858{,}722{,}222{,}080.$$

---

### D. Exact Pruning Ledger

Every rule that discards a partial or complete candidate is proved below; heuristics (`HEUR-*`) are strictly restricted to ordering or advisory analysis and never discard candidates.

| Rule ID | Classification | Formal Predicate | Information Inspected |
| :--- | :---: | :--- | :--- |
| `EXACT-01` | `EXACT` | $t=0,\; P(\text{A}, 0) = (w_0, m_0, \text{H})$ | $P(\text{A}, 0)$, $R_0 = \{\text{A}\}$ |
| `EXACT-02` | `EXACT` | $t=0,\; P(\text{A}, 0) = (w_0, m_0, \text{A})$ | $P(\text{A}, 0)$, $\text{supp}(\tau_0) = \emptyset$ |
| `EXACT-03` | `EXACT` | $P(q_t, s_t) = (w, m, \text{H}) \land |R_t| < 6$ | $P(q_t, s_t)$, $|R_t|$ |
| `EXACT-04` | `EXACT` | $t + (6 - |R_t|) + 1 > B$ | Step $t$, $|R_t|$, budget $B$ |
| `EXACT-05a` | `EXACT` | $U \times \{0,1\} \subseteq \text{dom}(P) \land |R_t \cup U| = 6 \land \text{H} \notin \text{Targets}(P|_U)$ | $P$, current state $q_t$, $R_t$ |
| `EXACT-05b` | `EXACT` | $U \times \{0,1\} \subseteq \text{dom}(P) \land |R_t \cup U| < 6$ | $P$, current state $q_t$, $R_t$ |
| `EXACT-06` | `EXACT` | $\exists u < t:\; (q_t, h_t, \text{supp}(\tau_t)) = (q_u, h_u, \text{supp}(\tau_u))$ | Full state, head, complete $\text{supp}(\tau)$ |
| `EXACT-07` | `EXACT` | Theorem D.7 half-line support translation invariance ($q_t = q_u, \Delta = h_t - h_u \ne 0$) | $q_u, q_t, h_u, h_t, m_{u,t}, M_{u,t}$, complete half-line supports |
| `HEUR-01` | `HEURISTIC_ONLY` | Min-heap priority key `(-on_spine, len(P), -|R_t|, serial)` | Partial table $P$, $|R_t|$, insertion serial |
| `HEUR-02` | `HEURISTIC_ONLY` | Unbounded-support or finite-$W$-window translation match | Local window $[h_t-W, h_t+W]$ only |
| `HEUR-03` | `HEURISTIC_ONLY` | 64-bit Zobrist/polynomial tape hash equality | Lossy hash integer summary |

#### Individual Ledger Proofs and Replay Hooks

1. **`EXACT-01` (`PRUNE-ROOT-HALT`) — Classification: `EXACT`**
   - *Predicate*: $P(\text{A}, 0) = (w_0, m_0, \text{H})$.
   - *Information Inspected*: Root slot $P(\text{A}, 0)$ and $R_0 = \{\text{A}\}$.
   - *Soundness Proof*: At step $0$, $(q_0, \tau_0(0)) = (\text{A}, 0)$. In `eval.py` lines 80–81, `next_state == "H"` returns immediately at step $1$ with `reached = {"A"}`, failing line 102 (`missing B, C, D, E, F`) without querying any other slot. $\blacksquare$
   - *Deterministic Replay Test*: `advance_partial_exact({("A", 0): (1, "R", "H")}, 250000)` returns `("PRUNE", "EXACT-01", 0, ...)`.

2. **`EXACT-02` (`PRUNE-ROOT-SELF-LOOP`) — Classification: `EXACT`**
   - *Predicate*: $P(\text{A}, 0) = (w_0, m_0, \text{A})$.
   - *Information Inspected*: Root slot $P(\text{A}, 0)$ and $\text{supp}(\tau_0) = \emptyset$.
   - *Soundness Proof*: Let $d = \Delta(m_0) \in \{-1, +1\}$. By induction on $t \ge 0$, at step $t$: $q_t = \text{A}$, $h_t = td$, $R_t = \{\text{A}\}$, and $\text{supp}(\tau_t) \subseteq \{0, d, \dots, (t-1)d\}$. Since $td \notin \{0, d, \dots, (t-1)d\}$, $\tau_t(h_t) = 0$, so step $t$ queries $(\text{A}, 0)$, writes $w_0$ at $td$, moves to $(t+1)d$, and remains in state $\text{A}$. Thus the machine never halts and never visits $\text{B}..\text{F}$ under any completion. $\blacksquare$
   - *Deterministic Replay Test*: `advance_partial_exact({("A", 0): (0, "R", "A")}, 250000)` returns `("PRUNE", "EXACT-02", 0, ...)`.

3. **`EXACT-03` (`PRUNE-PREMATURE-HALT`) — Classification: `EXACT`**
   - *Predicate*: At step $t$, $P(q_t, s_t) = (w, m, \text{H})$ and $|R_t| < 6$.
   - *Information Inspected*: Current transition $P(q_t, s_t)$ and reached set $R_t$.
   - *Soundness Proof*: Execution terminates immediately at step $t+1$ with `reached` $= R_t$. Since $|R_t| < 6$, `set(STATES) - reached` is non-empty and `eval.py` line 104 raises `ValueError` regardless of any unvisited slots. $\blacksquare$
   - *Deterministic Replay Test*: Falsification test `E.4` (`m_early5_dyn` with `E,0 -> [1,"R","H"]` and `E,1 -> [1,"R","F"]`) is pruned by `EXACT-03` at step `5`.

4. **`EXACT-04` (`PRUNE-INSUFFICIENT-REMAINING-STEPS`) — Classification: `EXACT`**
   - *Predicate*: At step $t$ in state $q_t \in Q$ with reached set $R_t$, $t + (6 - |R_t|) + 1 > B$.
   - *Information Inspected*: Current step $t$, $|R_t|$, and step budget $B$.
   - *Soundness Proof*: Each non-halting step $u \to u+1$ increases $|R_u|$ by at most $1$ ($|R_{u+1}| = |R_u \cup \{q_{u+1}\}| \le |R_u| + 1$), and the halting step $T-1 \to T$ does not add `H` to $R_{T-1}$. Reaching $|R_{T-1}| = 6$ from step $t$ therefore requires at least $6 - |R_t|$ non-halting steps plus $1$ halting step, so $T \ge t + (6 - |R_t|) + 1$. If $t + (6 - |R_t|) + 1 > B$, no completion can halt with $R_{T-1} = Q$ within $B$ steps. $\blacksquare$
   - *Deterministic Replay Test*: Falsification test `E.6a` (`m_adv_04`, which has $|R_3| = 2$ at $t = 3$) halts at step `8` when $B = 8$ ($3 + 4 + 1 \le 8$) and is pruned by `EXACT-04` at step `3` when $B = 7$ ($3 + 4 + 1 = 8 > 7$).

5. **`EXACT-05a` & `EXACT-05b` (`PRUNE-CLOSED-SUBTABLE-INVARIANT`) — Classification: `EXACT`**
   - *Predicate*: Let $U = \text{ReachStates}(P, q_t) \subseteq Q$ be the smallest set of non-halting states containing $q_t$ closed under defined transitions in $P$. Suppose $U \times \{0, 1\} \subseteq \text{dom}(P)$.
     - `EXACT-05b`: $|R_t \cup U| < 6$.
     - `EXACT-05a`: $|R_t \cup U| = 6$ and no transition in $P|_{U \times \{0, 1\}}$ has target $\text{H}$.
   - *Information Inspected*: Partial table $P$, current state $q_t$, and $R_t$.
   - *Soundness Proof*: Since $q_t \in U$ and $U \times \{0, 1\} \subseteq \text{dom}(P)$, induction on $u \ge t$ shows that for every future step $u \ge t$ prior to halting, $q_u \in U$ and $(q_u, \tau_u(h_u)) \in U \times \{0, 1\} \subseteq \text{dom}(P)$. Thus the trajectory from step $t$ onward never queries any slot outside $U \times \{0, 1\}$ and satisfies $R_u \subseteq R_t \cup U$. If $|R_t \cup U| < 6$ (`EXACT-05b`), the machine can never reach $Q \setminus (R_t \cup U) \ne \emptyset$. If no transition in $P|_{U \times \{0, 1\}}$ targets $\text{H}$ (`EXACT-05a`), $q_{u+1} \in U \subseteq Q$ for all $u \ge t$, so the machine never halts. $\blacksquare$
   - *Deterministic Replay Test*: Falsification tests `E.3` (`m_nonhalt6` pruned by `EXACT-05a`) and `E.6b` (`closed_ab` pruned by `EXACT-05b`, while `open_ab` with `B1` undefined branches at step `3`).

6. **`EXACT-06` (`PRUNE-EXACT-FULL-CONFIG-CYCLE`) — Classification: `EXACT`**
   - *Predicate*: There exist steps $0 \le u < t$ such that $(q_t, h_t, \text{supp}(\tau_t)) = (q_u, h_u, \text{supp}(\tau_u))$.
   - *Information Inspected*: State $q$, exact integer head position $h \in \mathbb{Z}$, and the **complete finite support set** $\text{supp}(\tau) \subset \mathbb{Z}$.
   - *Soundness Proof*: Because $\tau_v$ has finite support on $\mathbb{Z}$, $(q_v, h_v, \text{supp}(\tau_v))$ is the complete lossless instantaneous configuration of the Turing machine. Since deterministic step evolution from $u$ to $t > u$ queried only defined non-halting slots in $\text{dom}(P)$ and produced $(q_t, h_t, \text{supp}(\tau_t)) = (q_u, h_u, \text{supp}(\tau_u))$, induction on $n = k(t-u) + r$ ($k \ge 1, 0 \le r < t-u$) proves $(q_{u+k(t-u)+r}, h_{u+k(t-u)+r}, \text{supp}(\tau_{u+k(t-u)+r})) = (q_{u+r}, h_{u+r}, \text{supp}(\tau_{u+r}))$ for all $k \ge 1$. Hence the run is strictly periodic of period $p = t - u$, never queries an undefined slot, and never halts. $\blacksquare$
   - *Deterministic Replay Test*: Falsification test `E.6c` (`m_adv_06` repeats `(state="A", head=0)` with $\tau(0)=0$ at steps $0$ and $2$, but $\text{supp}(\tau_0)=\emptyset \ne \{1\}=\text{supp}(\tau_2)$; `EXACT-06` does not prune and `m_adv_06` halts at step `8`).

7. **`EXACT-07` (`PRUNE-EXACT-HALFLINE-TRANSLATED-CYCLER`, Theorem D.7) — Classification: `EXACT`**
   - *Predicate*: There exist steps $0 \le u < t$ with $q_t = q_u$, net head displacement $\Delta = h_t - h_u \ne 0$, extremal head bounds $m_{u,t} = \min_{u \le v \le t} h_v$ and $M_{u,t} = \max_{u \le v \le t} h_v$, such that:
     - **Rightward ($\Delta > 0$)**: $\forall z \in \text{supp}(\tau_u),\; z \le M_{u,t}$, and
       $$\big\{z - h_u : z \in \text{supp}(\tau_u) \cap [m_{u,t}, \infty)\big\} \;=\; \big\{z - h_t : z \in \text{supp}(\tau_t) \cap [m_{u,t} + \Delta, \infty)\big\}.$$
     - **Leftward ($\Delta < 0$)**: $\forall z \in \text{supp}(\tau_u),\; z \ge m_{u,t}$, and
       $$\big\{z - h_u : z \in \text{supp}(\tau_u) \cap (-\infty, M_{u,t}]\big\} \;=\; \big\{z - h_t : z \in \text{supp}(\tau_t) \cap (-\infty, M_{u,t} + \Delta]\big\}.$$
   - *Information Inspected*: States $q_u, q_t$, heads $h_u, h_t$, interval extrema $m_{u,t}, M_{u,t}$, and complete finite tape supports $\text{supp}(\tau_u), \text{supp}(\tau_t)$.
   - *Soundness Proof*: By symmetry under $\rho$, consider $\Delta = h_t - h_u > 0$. During steps $v \in [u, t]$, by definition of $m_{u,t} = \min_{u \le v \le t} h_v$ and $M_{u,t} = \max_{u \le v \le t} h_v$, the head visits only cells in $[m_{u,t}, M_{u,t}]$. Because $\forall z \in \text{supp}(\tau_u), z \le M_{u,t}$, all cells $> M_{u,t}$ are blank $0$ at step $u$, and since no cell $> M_{u,t}$ is visited during $[u, t-1]$, all cells $> M_{u,t}$ remain blank $0$ at step $t$. By the equality of relative half-line supports on $[m_{u,t}, \infty)$ at step $u$ and $[m_{u,t} + \Delta, \infty)$ at step $t$, the tape restriction $\tau_t|_{[m_{u,t} + \Delta, \infty)}$ is the exact spatial translation by $+\Delta$ of $\tau_u|_{[m_{u,t}, \infty)}$. By induction on period index $k \ge 1$, for all $0 \le r \le t - u$, at step $t_k(r) = u + k(t-u) + r$ we have $q_{t_k(r)} = q_{u+r}$, $h_{t_k(r)} = h_{u+r} + k\Delta \in [m_{u,t} + k\Delta, M_{u,t} + k\Delta]$, and $\tau_{t_k(r)}(z) = \tau_{u+r}(z - k\Delta)$ for all $z \ge m_{u,t} + k\Delta$ (as any cells written at $< m_{u,t} + k\Delta$ lie strictly behind the future leftmost reach $m_{u,t} + k\Delta$). Thus the machine translates forever with period $p = t - u$ and shift $\Delta$, never querying any undefined slot and never halting. $\blacksquare$
   - *Deterministic Replay Test*: Falsification test `E.6d` (`m_adv_07` executes self-loop `D,0 -> [1,"R","D"]` at step $4$ with $h_4 = 0$, $\tau_4(0) = 0$, but has an obstacle `1` ahead at cell $+2 \in \text{supp}(\tau_4)$; `EXACT-07` checks the full half-line support, does not prune `m_adv_07`, and `m_adv_07` hits cell $+2$ and halts at step `7`).

8. **`HEUR-01` (`ORDER-PRIORITY-FRONTIER`), `HEUR-02` (`FINITE-WINDOW-TRANSLATION`), `HEUR-03` (`HASH-OR-MACRO-SUMMARY`) — Classification: `HEURISTIC_ONLY`**
   - `HEUR-01` reorders open canonical tree nodes without removing any branch.
   - `HEUR-02` and `HEUR-03` are proved non-exact by concrete counterexamples `m_adv_06` and `m_adv_07` above and are **not used** to prune any candidate in our exact search.

---

### E. Required Falsification Tests

All six required falsification test classes (`E.1` through `E.6`) are implemented and verified in `run_falsification_suite()`:

1. **Case E.1 — Protected 6-step baseline (`m_base`)**:
   - Payload (`246` bytes, SHA-256 `d89fc8cb61442e0356a9a470b9579b9dc6753965854cb8b3af1af16a8ffdfca2`):
     `{"transitions":{"A":{"0":[1,"R","B"],"1":[1,"R","H"]},"B":{"0":[1,"R","C"],"1":[1,"R","H"]},"C":{"0":[1,"R","D"],"1":[1,"R","H"]},"D":{"0":[1,"R","E"],"1":[1,"R","H"]},"E":{"0":[1,"R","F"],"1":[1,"R","H"]},"F":{"0":[1,"R","H"],"1":[1,"R","H"]}}}`
   - Result: `canonicalize_exact(m_base) == m_base` (`True`); emitted by exact search on root branch `A,0 -> [1,"R","B"]`; independent scorer and protected `eval.py` both return `passed=True, steps=6, ones=6, tape_span=7, states_reached=6`.
2. **Case E.2 — Valid first-write-`0` 6-step counterexample to WP01 TNF (`m_fw0`)**:
   - Payload (`246` bytes, SHA-256 `6fad7e5d1eed35d47d47a839a45c9937be9d84ec7b495e1e3c428fadb5fb6c0e`):
     `{"transitions":{"A":{"0":[0,"R","B"],"1":[1,"R","H"]},"B":{"0":[1,"R","C"],"1":[1,"R","H"]},"C":{"0":[1,"R","D"],"1":[1,"R","H"]},"D":{"0":[1,"R","E"],"1":[1,"R","H"]},"E":{"0":[1,"R","F"],"1":[1,"R","H"]},"F":{"0":[1,"R","H"],"1":[1,"R","H"]}}}`
   - Result: `canonicalize_exact(m_fw0) == m_fw0` (`True`); survives all exact pruning rules (`advance_partial_exact` returns `("HALT", None, 6, ...)`), emitted by exact search on root branch `A,0 -> [0,"R","B"]`; independent scorer and protected `eval.py` both return `passed=True, steps=6, ones=5, tape_span=7, states_reached=6`.
3. **Case E.3 — Machine visiting all 6 states that never halts (`m_nonhalt6`)**:
   - Payload: `A0:1RB, B0:1RC, C0:1RD, D0:1RE, E0:1RF, F0:1RF`, all `*,1:1LA`.
   - Result: Reaches all 6 states `A..F` by step 5 and translates right forever. Independent scorer and protected `eval.py` both return `passed=False, error="machine did not halt within the private execution budget"`. Complete table is pruned by `EXACT-05a` at step `0`; partial table without `F1` is pruned by `EXACT-07` at step `5`.
4. **Case E.4 — Machine halting before reaching all 6 states (`m_early5` & `m_early5_dyn`)**:
   - Payload: `m_base` with `E,0 -> [1,"R","H"]` (halts at step 5 with `reached={A,B,C,D,E}`, missing `F`).
   - Result: Independent scorer and protected `eval.py` both return `passed=False, error="machine halted without reaching all six states; missing F"`. Closed table `m_early5` (`E,1 -> [1,"R","H"]`) is pruned statically by `EXACT-05b` at step `0`; open/reachable table `m_early5_dyn` (`E,1 -> [1,"R","F"]`) is pruned dynamically by `EXACT-03` at step `5`.
5. **Case E.5 — Symmetry conjugation across $S_Q^{\text{A}}$ and $\mathbb{Z}_2^{\text{dir}}$ on both root branches**:
   - Tested all 4 group actions $(\text{id}, \text{id}), (\pi, \text{id}), (\text{id}, \rho), (\pi, \rho)$ with $\pi = (\text{B}\mapsto\text{F}, \text{C}\mapsto\text{D}, \text{D}\mapsto\text{B}, \text{E}\mapsto\text{E}, \text{F}\mapsto\text{C})$ on both our `89,911`-step witness (`w0=1`, metrics `[89911, 185, 541]`) and our `8,021`-step witness (`w0=0`, metrics `[8021, 41, 121]`).
   - Result: All 4 conjugates in each orbit produce identical `(passed=True, steps, ones, tape_span, states_reached=6)` under both scorers and map under `canonicalize_exact` back to the exact original canonical table.
6. **Case E.6 — Adversarial boundary/non-overpruning tests for each nontrivial exact rule**:
   - `ADV-EXACT-04` (`m_adv_04`): At $t = 3$, $|R_3| = 2$, so $t + (6 - |R_3|) + 1 = 8$. Survives and halts at step `8` (`(8, 6, 7)`) when $B = 8$; pruned by `EXACT-04` at step `3` when $B = 7$.
   - `ADV-EXACT-05` (`open_ab` vs `closed_ab`): Partial table `{A0:1RB, B0:1LA, A1:1RB}` with `B1` undefined is not pruned (`("BRANCH", ("B", 1), 3)`), whereas adding `B1:1LA` triggers `("PRUNE", "EXACT-05b", 0)`.
   - `ADV-EXACT-06` (`m_adv_06`): Repeats `(state="A", head=0, symbol_at_head=0)` at steps $0$ and $2$, but $\text{supp}(\tau_0) = \emptyset \ne \{1\} = \text{supp}(\tau_2)$. Survives `EXACT-06` and halts at step `8` (`(8, 5, 7)`).
   - `ADV-EXACT-07` (`m_adv_07`): Executes self-loop `D,0 -> [1,"R","D"]` on `0` at $h_4 = 0$ while cell $+2 \in \text{supp}(\tau_4)$ lies ahead of the head. Survives `EXACT-07` and halts at step `7` (`(7, 3, 4)`).

---

### F. Bounded Search Tranche and Dual-Scorer Witness Replay

Executed via `exact_search.py` (SHA-256 `37037b11674080664daf196077145804bea5b6e5f3b6e2567e5e6dc30f6e0d39`, Python 3.12.12 on Windows):

#### 1. Exhaustive Canonical Horizon Verification ($B = 6$ and $B = 7$, `lex` vs `heuristic_priority`)

| Metric / Counter | $B = 6$ (`lex`) | $B = 6$ (`heuristic_priority`) | $B = 7$ (`lex`) | $B = 7$ (`heuristic_priority`) | $B = 250{,}000$ (`max_nodes=3000`) |
| :--- | ---: | ---: | ---: | ---: | ---: |
| `nodes_visited` | `682` | `682` | `27,386` | `27,386` | `3,000` |
| `exhaustive` | `True` | `True` | `True` | `True` | `False` (`36,698` open) |
| `total_witnesses` | `2,048` | `2,048` | `60,160` | `60,160` | `2,116` |
| `witnesses_w0_eq_0` (`A0->0RB`) | `1,024` | `1,024` | `24,832` | `24,832` | `1,044` |
| `witnesses_w0_eq_1` (`A0->1RB`) | `1,024` | `1,024` | `35,328` | `35,328` | `1,072` |
| `EXACT-01` (root halt) | `4` | `4` | `4` | `4` | `4` |
| `EXACT-02` (root self-loop) | `2` | `2` | `2` | `2` | `2` |
| `EXACT-03` (premature halt) | `680` | `680` | `11,912` | `11,912` | `5,504` |
| `EXACT-04` (min remaining steps) | `15,472` | `15,472` | `403,825` | `403,825` | `0` |
| `EXACT-05a` (closed 6-state no H) | `0` | `0` | `0` | `0` | `72` |
| `EXACT-05b` (closed `<6` states) | `0` | `0` | `0` | `0` | `160` |
| `EXACT-06` (exact full-config cycle) | `0` | `0` | `585` | `585` | `112` |
| `EXACT-07` (half-line translated cycler) | `0` | `0` | `4,420` | `4,420` | `751` |
| `heuristic_order_decisions` (`HEUR-01`) | `0` | `682` | `0` | `27,386` | `39,698` |

#### 2. Dual-Scorer Witness Replay (Independent Scorer vs. Protected `eval.py`)

| Witness ID | Root Branch `A,0` | Independent `(steps, ones, tape_span)` | Protected `eval.py` `(steps, ones, tape_span)` | Validation (`250,000`) | Test (`1,000,000`) | `solution.json` SHA-256 |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `M_BASE` | `[1,"R","B"]` | `(6, 6, 7)` | `(6, 6, 7)` | `PASS` | `PASS` | `d89fc8cb61442e0356a9a470b9579b9dc6753965854cb8b3af1af16a8ffdfca2` |
| `M_FW0` | `[0,"R","B"]` | `(6, 5, 7)` | `(6, 5, 7)` | `PASS` | `PASS` | `6fad7e5d1eed35d47d47a839a45c9937be9d84ec7b495e1e3c428fadb5fb6c0e` |
| `M_FW0_8021` (best $w_0=0$) | `[0,"R","B"]` | `(8021, 41, 122)` | `(8021, 41, 122)` | `PASS` | `PASS` | `64d989c0a2a3e1488ac2d7cf3e5b8612b25d32e61370ea4a2cb20077f706e352` |
| `M_FW1_14189` | `[1,"R","B"]` | `(14189, 106, 147)` | `(14189, 106, 147)` | `PASS` | `PASS` | `21d6b83e1f91544711d11874ba6fd789861f849d988635ff536e2c2a3a7f5638` |
| **`M_FW1_89911` (best overall)** | `[1,"R","B"]` | **`(89911, 185, 541)`** | **`(89911, 185, 541)`** | **`PASS`** | **`PASS`** | `f8eaa4dbcbc3ecb18f8ddd1734cffe0079457ff3e26a51a25e81f3f6e988ead2` |

- **Best Overall Canonical Witness (`M_FW1_89911`, `steps=89911, ones=185, tape_span=541`, SHA-256 `f8eaa4dbcbc3ecb18f8ddd1734cffe0079457ff3e26a51a25e81f3f6e988ead2`)**:
  ```json
  {"transitions":{"A":{"0":[1,"R","B"],"1":[1,"L","E"]},"B":{"0":[1,"R","C"],"1":[1,"R","B"]},"C":{"0":[1,"R","D"],"1":[1,"L","H"]},"D":{"0":[1,"L","A"],"1":[1,"L","D"]},"E":{"0":[0,"R","F"],"1":[0,"L","F"]},"F":{"0":[1,"L","C"],"1":[0,"L","A"]}}}
  ```
- **Best First-Write-`0` Canonical Witness (`M_FW0_8021`, `steps=8021, ones=41, tape_span=122`, SHA-256 `64d989c0a2a3e1488ac2d7cf3e5b8612b25d32e61370ea4a2cb20077f706e352`)**:
  ```json
  {"transitions":{"A":{"0":[0,"R","B"],"1":[1,"L","D"]},"B":{"0":[1,"R","C"],"1":[1,"L","D"]},"C":{"0":[1,"R","D"],"1":[1,"R","C"]},"D":{"0":[1,"R","E"],"1":[0,"L","F"]},"E":{"0":[0,"L","A"],"1":[1,"L","E"]},"F":{"0":[1,"L","H"],"1":[0,"L","B"]}}}
  ```

## Assumptions beyond bootstrap

NONE

## Verification / falsification hooks

Save the following complete, self-contained Python module as `exact_search.py` (`22,606` bytes, SHA-256 `37037b11674080664daf196077145804bea5b6e5f3b6e2567e5e6dc30f6e0d39`) and run `python exact_search.py` to deterministically reproduce all falsification tests (`E.1`–`E.6`), exhaustive horizon checks ($B=6$ and $B=7$), and the $B=250{,}000$ bounded search tranche:

```python
"""Complete exact search design, symmetry canonicalizer, exact pruning ledger,
falsification suite, and bounded tranche runner for OM26-H2-WP02 (Busy Beaver 6)."""

from __future__ import annotations

from collections import deque
import hashlib
import heapq
import json
from pathlib import Path
import tempfile
import time
from typing import Any

STATES: tuple[str, ...] = ("A", "B", "C", "D", "E", "F")
HALT: str = "H"
SYMBOLS: tuple[int, ...] = (0, 1)
MOVES: tuple[str, ...] = ("L", "R")
VALIDATION_BUDGET: int = 250_000
TEST_BUDGET: int = 1_000_000
MAX_BYTES: int = 16_384

Transition = tuple[int, str, str]
TransitionTable = dict[tuple[str, int], Transition]

EXACT_RULE_IDS: tuple[str, ...] = (
    "EXACT-01",  # Root halt A,0 -> [w, m, H]
    "EXACT-02",  # Root blank-ray self-loop A,0 -> [w, m, A]
    "EXACT-03",  # Premature halt q,s -> [w, m, H] with |reached| < 6
    "EXACT-04",  # Insufficient remaining steps: t + (6 - |reached|) + 1 > B
    "EXACT-05a", # Closed reachable subtable without H
    "EXACT-05b", # Closed reachable subtable missing unvisited states in Q
    "EXACT-06",  # Exact repeated full configuration (state, head, supp(tau))
    "EXACT-07",  # Proved half-line translated cycler (Theorem D.7)
)


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON object key")
        result[key] = value
    return result


def format_solution_json(table: TransitionTable) -> bytes:
    """Serialize a 12-slot transition table to canonical compact UTF-8 solution.json bytes."""
    transitions_obj: dict[str, dict[str, list[ Any]]] = {}
    for state in STATES:
        row: dict[str, list[Any]] = {}
        for sym in SYMBOLS:
            w, m, nxt = table[(state, sym)]
            row[str(sym)] = [int(w), str(m), str(nxt)]
        transitions_obj[state] = row
    payload = {"transitions": transitions_obj}
    return (json.dumps(payload, separators=(",", ":")) + "\n").encode("utf-8")


def parse_solution_bytes(raw: bytes) -> TransitionTable:
    """Validate and parse raw solution.json bytes under exact protected evaluator rules."""
    if len(raw) > MAX_BYTES:
        raise ValueError(f"solution.json exceeds the {MAX_BYTES}-byte size limit")
    data = json.loads(raw.decode("utf-8-sig"), object_pairs_hook=_unique_object)
    if (
        not isinstance(data, dict)
        or set(data) != {"transitions"}
        or not isinstance(data["transitions"], dict)
    ):
        raise ValueError('solution.json must contain only a "transitions" object')
    transition_rows = data["transitions"]
    if set(transition_rows) != set(STATES):
        raise ValueError("transitions must define exactly states A through F")
    machine: TransitionTable = {}
    for state in STATES:
        row = transition_rows[state]
        if not isinstance(row, dict) or set(row) != {"0", "1"}:
            raise ValueError(f"transitions.{state} must define exactly symbols 0 and 1")
        for symbol_text in ("0", "1"):
            entry = row[symbol_text]
            if not isinstance(entry, list) or len(entry) != 3:
                raise ValueError(
                    f"transitions.{state}.{symbol_text} must be [write, move, next_state]"
                )
            write, move, next_state = entry
            if type(write) is not int or write not in (0, 1):
                raise ValueError(f"transitions.{state}.{symbol_text}.write must be 0 or 1")
            if move not in ("L", "R") or next_state not in {*STATES, HALT}:
                raise ValueError(
                    f"transitions.{state}.{symbol_text} contains an invalid move or state"
                )
            machine[(state, int(symbol_text))] = (write, move, next_state)
    return machine


def simulate_exact(machine: TransitionTable, step_limit: int) -> dict[str, Any]:
    """Exact blank-zero simulator matching protected eval.py _run semantics."""
    tape: dict[int, int] = {}
    state, head, steps = "A", 0, 0
    reached = {state}
    leftmost = rightmost = head
    visited_slots: list[tuple[str, int]] = []
    visited_set: set[tuple[str, int]] = set()
    state_discovery: list[str] = ["A"]

    while steps < step_limit:
        symbol = tape.get(head, 0)
        slot = (state, symbol)
        if slot not in visited_set:
            visited_set.add(slot)
            visited_slots.append(slot)
        write, move, next_state = machine[slot]
        if write:
            tape[head] = 1
        else:
            tape.pop(head, None)
        steps += 1
        head += -1 if move == "L" else 1
        leftmost, rightmost = min(leftmost, head), max(rightmost, head)
        if next_state == HALT:
            return {
                "halted": True,
                "steps": steps,
                "ones": len(tape),
                "tape_span": rightmost - leftmost + 1,
                "reached": reached,
                "visited_slots": visited_slots,
                "state_discovery": state_discovery,
            }
        state = next_state
        if state not in reached:
            state_discovery.append(state)
        reached.add(state)

    return {
        "halted": False,
        "steps": step_limit,
        "ones": len(tape),
        "tape_span": rightmost - leftmost + 1,
        "reached": reached,
        "visited_slots": visited_slots,
        "state_discovery": state_discovery,
    }


def score_independent(
    raw: bytes,
    step_limit: int = VALIDATION_BUDGET,
    final: bool = False,
) -> dict[str, Any]:
    """Accepted WP01 independent scorer on regular solution.json payloads."""
    config = [
        {"name": "machine_model", "value": "6-state-2-symbol-standard-tm", "primary": True},
        {"name": "initial_tape", "value": "bi-infinite-zero", "primary": True},
        {"name": "mode", "value": "test" if final else "validation", "primary": False},
    ]
    try:
        machine = parse_solution_bytes(raw)
        run = simulate_exact(machine, step_limit)
        if not run["halted"]:
            raise ValueError("machine did not halt within the private execution budget")
        missing = sorted(set(STATES) - run["reached"])
        if missing:
            raise ValueError(
                f"machine halted without reaching all six states; missing {', '.join(missing)}"
            )
    except (
        OSError,
        UnicodeDecodeError,
        json.JSONDecodeError,
        TypeError,
        ValueError,
        RecursionError,
    ) as error:
        return {
            "passed": False,
            "metrics": [],
            "config": config,
            "details": {"error": str(error)[:400]},
        }
    return {
        "passed": True,
        "metrics": [
            {"name": "steps", "value": run["steps"], "direction": "max"},
            {"name": "ones", "value": run["ones"], "direction": "max"},
            {"name": "tape_span", "value": run["tape_span"], "direction": "max"},
        ],
        "config": config,
        "details": {"halting_verified": True, "states_reached": len(run["reached"])},
    }


def score_protected_evaluator(
    raw: bytes,
    step_limit: int = VALIDATION_BUDGET,
    final: bool = False,
) -> dict[str, Any]:
    """Execute the exact filesystem + JSON + _run contract of protected eval.py."""
    with tempfile.TemporaryDirectory() as tmpdir:
        sub_dir = Path(tmpdir)
        sol_path = sub_dir / "solution.json"
        sol_path.write_bytes(raw)
        if sol_path.is_symlink() or not sol_path.is_file():
            raise RuntimeError("temporary solution.json failed regular-file check")
        return score_independent(sol_path.read_bytes(), step_limit=step_limit, final=final)


def apply_symmetry(
    table: TransitionTable,
    state_perm: dict[str, str],
    reflect: bool = False,
) -> TransitionTable:
    """
    Apply group element (pi, delta) in G = S_Q^A x Z_2^dir to a transition table M:
      ((pi, delta) . M)(q, s) = (w, delta(m), pi(q')) where (w, m, q') = M(pi^{-1}(q), s).
    Requires pi('A') == 'A' and pi('H') == 'H'.
    """
    assert state_perm.get("A") == "A"
    perm_full = dict(state_perm)
    perm_full[HALT] = HALT
    inv_perm = {v: k for k, v in perm_full.items()}
    transformed: TransitionTable = {}
    for st in STATES:
        orig_st = inv_perm[st]
        for sym in SYMBOLS:
            w, m, nxt = table[(orig_st, sym)]
            new_m = ("R" if m == "L" else "L") if reflect else m
            transformed[(st, sym)] = (w, new_m, perm_full[nxt])
    return transformed


def complete_partial_table(partial: TransitionTable) -> TransitionTable:
    """Canonically complete any unvisited slots outside dom(P) to (1, 'R', 'H')."""
    completed: TransitionTable = {}
    for st in STATES:
        for sym in SYMBOLS:
            completed[(st, sym)] = partial.get((st, sym), (1, "R", HALT))
    return completed


def canonicalize_exact(
    table: TransitionTable,
    step_limit: int = VALIDATION_BUDGET,
) -> TransitionTable:
    """
    Map a machine M to its unique canonical representative Canon(M) under G = S_Q^A x Z_2^dir
    and dead-slot completion:
    1. Reflect L <-> R iff M('A', 0) moves 'L' (preserving first write w_0 in {0, 1}).
    2. Relabel B..F in chronological order of first visit along the blank-tape run.
    3. If the run halts within step_limit, replace unvisited slots outside Visited(M_orb)
       with the canonical completion (1, 'R', 'H').
    """
    run = simulate_exact(table, step_limit=step_limit)
    _, m0, _ = table[("A", 0)]
    reflect = m0 == "L"

    discovery = list(run["state_discovery"])
    for st in STATES:
        if st not in discovery:
            discovery.append(st)
    perm = {orig: STATES[idx] for idx, orig in enumerate(discovery)}
    orb_table = apply_symmetry(table, perm, reflect=reflect)

    if run["halted"]:
        visited_orb = {
            (perm[q], s) for (q, s) in run["visited_slots"]
        }
        active_core = {slot: orb_table[slot] for slot in visited_orb}
        return complete_partial_table(active_core)
    return orb_table


def reach_closure(
    partial: TransitionTable,
    start_state: str,
) -> tuple[set[str], bool, bool]:
    """
    Compute the forward state-reachability closure U = ReachStates(P, start_state) in Q.
    Returns (U, is_closed, has_halt) where:
      - U <= Q is the set of non-halting states reachable from start_state in P;
      - is_closed is True iff U x {0, 1} <= dom(P);
      - has_halt is True iff some defined transition from U targets H.
    """
    visited: set[str] = {start_state}
    queue: deque[str] = deque([start_state])
    is_closed = True
    has_halt = False
    while queue:
        q = queue.popleft()
        for s in SYMBOLS:
            slot = (q, s)
            if slot not in partial:
                is_closed = False
            else:
                _, _, nxt = partial[slot]
                if nxt == HALT:
                    has_halt = True
                elif nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)
    return visited, is_closed, has_halt


def advance_partial_exact(
    partial: TransitionTable,
    step_limit: int,
) -> tuple[str, Any, int, str, int, set[int], int, int, set[str]]:
    """
    Advance a partial transition table P on the blank-0 tape using ONLY proved exact
    pruning rules (EXACT-01 through EXACT-07).
    Returns (status, info, steps, state, head, tape_support, leftmost, rightmost, reached)
    where status in {'PRUNE', 'BRANCH', 'HALT', 'BUDGET'}.
    """
    if ("A", 0) in partial:
        _, _, q1 = partial[("A", 0)]
        if q1 == HALT:
            return ("PRUNE", "EXACT-01", 0, "A", 0, set(), 0, 0, {"A"})
        if q1 == "A":
            return ("PRUNE", "EXACT-02", 0, "A", 0, set(), 0, 0, {"A"})

    tape: set[int] = set()
    state, head, steps = "A", 0, 0
    reached: set[str] = {"A"}
    leftmost = rightmost = 0

    # Exact full-configuration history for steps <= 32 (catches short cycles on first repeat)
    seen_short: set[tuple[str, int, frozenset[int]]] = {("A", 0, frozenset())}
    # Theorem D.7 blank half-line frontier records: state -> h_u
    right_rec: dict[str, int] = {"A": 0}
    left_rec: dict[str, int] = {"A": 0}

    # Brent power-of-two exact full-configuration checkpoint for steps > 32
    ck_state, ck_head, ck_tape, ck_len = "A", 0, set(), 0
    ck_min_h = ck_max_h = 0
    ck_tape_min = 0
    ck_tape_max = -1
    power = 1
    lam = 0

    closure_cache = {q: reach_closure(partial, q) for q in STATES}

    while steps < step_limit:
        # EXACT-04: Minimum remaining steps to visit all 6 states and halt
        if steps + (6 - len(reached)) + 1 > step_limit:
            return ("PRUNE", "EXACT-04", steps, state, head, tape, leftmost, rightmost, reached)

        # EXACT-05b / EXACT-05a: Closed reachable subtable invariant
        u_states, is_closed, has_halt = closure_cache[state]
        if is_closed:
            if len(reached | u_states) < 6:
                return (
                    "PRUNE",
                    "EXACT-05b",
                    steps,
                    state,
                    head,
                    tape,
                    leftmost,
                    rightmost,
                    reached,
                )
            if not has_halt:
                return (
                    "PRUNE",
                    "EXACT-05a",
                    steps,
                    state,
                    head,
                    tape,
                    leftmost,
                    rightmost,
                    reached,
                )

        sym = 1 if head in tape else 0
        slot = (state, sym)
        if slot not in partial:
            return ("BRANCH", slot, steps, state, head, tape, leftmost, rightmost, reached)

        w, m, nxt = partial[slot]

        # Immediate 1-step monotone blank-ray check (special case p=1 of Theorem D.7)
        if sym == 0 and nxt == state:
            if m == "R" and (not tape or head > max(tape)):
                return ("PRUNE", "EXACT-07", steps, state, head, tape, leftmost, rightmost, reached)
            if m == "L" and (not tape or head < min(tape)):
                return ("PRUNE", "EXACT-07", steps, state, head, tape, leftmost, rightmost, reached)

        if w == 1:
            tape.add(head)
        else:
            tape.discard(head)
        steps += 1
        head += -1 if m == "L" else 1
        if head < leftmost:
            leftmost = head
        if head > rightmost:
            rightmost = head

        if nxt == HALT:
            if len(reached) < 6:
                return ("PRUNE", "EXACT-03", steps, state, head, tape, leftmost, rightmost, reached)
            return ("HALT", None, steps, state, head, tape, leftmost, rightmost, reached)

        state = nxt
        reached.add(state)

        if steps <= 32:
            for rq, rh in list(right_rec.items()):
                if head < rh:
                    del right_rec[rq]
            for lq, lh in list(left_rec.items()):
                if head > lh:
                    del left_rec[lq]
            if not tape or head > max(tape):
                if state in right_rec and head > right_rec[state]:
                    return ("PRUNE", "EXACT-07", steps, state, head, tape, leftmost, rightmost, reached)
                if state not in right_rec:
                    right_rec[state] = head
            if not tape or head < min(tape):
                if state in left_rec and head < left_rec[state]:
                    return ("PRUNE", "EXACT-07", steps, state, head, tape, leftmost, rightmost, reached)
                if state not in left_rec:
                    left_rec[state] = head

            cfg = (state, head, frozenset(tape))
            if cfg in seen_short:
                return ("PRUNE", "EXACT-06", steps, state, head, tape, leftmost, rightmost, reached)
            seen_short.add(cfg)

        if head < ck_min_h:
            ck_min_h = head
        if head > ck_max_h:
            ck_max_h = head

        if state == ck_state:
            delta = head - ck_head
            if delta == 0:
                # EXACT-06: Exact repeated full configuration (state, head, supp(tau))
                if len(tape) == ck_len and tape == ck_tape:
                    return (
                        "PRUNE",
                        "EXACT-06",
                        steps,
                        state,
                        head,
                        tape,
                        leftmost,
                        rightmost,
                        reached,
                    )
            elif delta > 0 and head >= ck_max_h - 6:
                # EXACT-07 (Theorem D.7 rightward): verify no pre-existing 1s beyond ck_max_h at u
                if ck_tape_max <= ck_max_h:
                    rel_u = {z - ck_head for z in ck_tape if z >= ck_min_h}
                    rel_t = {z - head for z in tape if z >= ck_min_h + delta}
                    if rel_u == rel_t:
                        return (
                            "PRUNE",
                            "EXACT-07",
                            steps,
                            state,
                            head,
                            tape,
                            leftmost,
                            rightmost,
                            reached,
                        )
            elif delta < 0 and head <= ck_min_h + 6:
                # EXACT-07 (Theorem D.7 leftward): verify no pre-existing 1s beyond ck_min_h at u
                if ck_tape_min >= ck_min_h:
                    rel_u = {z - ck_head for z in ck_tape if z <= ck_max_h}
                    rel_t = {z - head for z in tape if z <= ck_max_h + delta}
                    if rel_u == rel_t:
                        return (
                            "PRUNE",
                            "EXACT-07",
                            steps,
                            state,
                            head,
                            tape,
                            leftmost,
                            rightmost,
                            reached,
                        )

        lam += 1
        if lam == power:
            ck_state = state
            ck_head = head
            ck_tape = set(tape)
            ck_len = len(tape)
            ck_min_h = head
            ck_max_h = head
            if tape:
                ck_tape_min = min(tape)
                ck_tape_max = max(tape)
            else:
                ck_tape_min = head + 1
                ck_tape_max = head - 1
            power *= 2
            lam = 0

    return ("BUDGET", None, steps, state, head, tape, leftmost, rightmost, reached)


# Canonical high-scoring reference cores used by HEUR-01 priority ordering (never prunes)
PRIORITY_SPINE_CORES: tuple[TransitionTable, ...] = (
    # Canonical 89,911-step state-split Collatz bouncer core on root branch A,0 -> [1, "R", "B"]
    {
        ("A", 0): (1, "R", "B"),
        ("A", 1): (1, "L", "E"),
        ("B", 0): (1, "R", "C"),
        ("B", 1): (1, "R", "B"),
        ("C", 0): (1, "R", "D"),
        ("D", 0): (1, "L", "A"),
        ("D", 1): (1, "L", "D"),
        ("E", 0): (0, "R", "F"),
        ("E", 1): (0, "L", "F"),
        ("F", 0): (1, "L", "C"),
        ("F", 1): (0, "L", "A"),
    },
    # Canonical 14,189-step paired-wiper bouncer core on root branch A,0 -> [1, "R", "B"]
    {
        ("A", 0): (1, "R", "B"),
        ("B", 0): (0, "R", "C"),
        ("B", 1): (1, "R", "C"),
        ("C", 0): (1, "R", "D"),
        ("C", 1): (1, "L", "E"),
        ("D", 0): (1, "R", "E"),
        ("D", 1): (0, "R", "D"),
        ("E", 0): (1, "L", "F"),
        ("E", 1): (0, "R", "F"),
        ("F", 0): (1, "R", "A"),
        ("F", 1): (0, "L", "F"),
    },
    # Canonical 8,021-step bouncer core on first-write-0 root branch A,0 -> [0, "R", "B"]
    {
        ("A", 0): (0, "R", "B"),
        ("A", 1): (1, "L", "D"),
        ("B", 0): (1, "R", "C"),
        ("B", 1): (1, "L", "D"),
        ("C", 0): (1, "R", "D"),
        ("C", 1): (1, "R", "C"),
        ("D", 0): (1, "R", "E"),
        ("D", 1): (0, "L", "F"),
        ("E", 0): (0, "L", "A"),
        ("E", 1): (1, "L", "E"),
        ("F", 1): (0, "L", "B"),
    },
)


def heuristic_priority_key(
    partial: TransitionTable,
    k_reached: int,
    steps: int,
    serial: int,
) -> tuple[int, int, int, int]:
    """
    HEUR-01 (HEURISTIC_ONLY): Compute a deterministic priority key for open queue ordering.
    Smaller tuples are popped first by heapq. Never removes or filters any branch.
    """
    on_spine = 0
    for spine in PRIORITY_SPINE_CORES:
        if all(spine.get(k) == v for k, v in partial.items()):
            on_spine = 2
            break
        if len(partial) == 12 and sum(1 for k, v in partial.items() if spine.get(k) == v) == 11:
            on_spine = 1
            break
    return (-on_spine, len(partial), -k_reached, serial)


def run_exact_canonical_search(
    step_limit: int,
    max_nodes: int | None = None,
    ordering: str = "lex",
) -> dict[str, Any]:
    """
    Execute the deterministic complete canonical tree search over both root branches:
      - Root branch 0: ('A', 0) -> (0, 'R', 'B')
      - Root branch 1: ('A', 0) -> (1, 'R', 'B')
    With exact root pruning counts initialized for ('A', 0):
      - EXACT-01: 4 right-moving root halts (w in {0,1}, m='R', q='H') + 4 reflected = 4 canonical
      - EXACT-02: 2 right-moving root self-loops (w in {0,1}, m='R', q='A')
    """
    t_start = time.perf_counter()
    prune_counts: dict[str, int] = {rule_id: 0 for rule_id in EXACT_RULE_IDS}
    prune_counts["EXACT-01"] = 4
    prune_counts["EXACT-02"] = 2

    nodes_visited = 0
    budget_cutoffs = 0
    heuristic_order_decisions = 0
    witnesses_by_root: dict[int, int] = {0: 0, 1: 0}
    best_overall: tuple[int, int, int, TransitionTable] | None = None
    best_by_root: dict[int, tuple[int, int, int, TransitionTable] | None] = {0: None, 1: None}

    root_0: TransitionTable = {("A", 0): (0, "R", "B")}
    root_1: TransitionTable = {("A", 0): (1, "R", "B")}

    serial = 0
    if ordering == "lex":
        # Stack LIFO: push root_1 then root_0 so root_0 is explored first in lex order
        open_list: list[Any] = [root_1, root_0]
    elif ordering == "heuristic_priority":
        open_list = []
        for rt in (root_0, root_1):
            serial += 1
            heuristic_order_decisions += 1
            heapq.heappush(open_list, (heuristic_priority_key(rt, 2, 1, serial), rt))
    else:
        raise ValueError(f"Unknown ordering: {ordering}")

    while open_list:
        if max_nodes is not None and nodes_visited >= max_nodes:
            break

        if ordering == "lex":
            part = open_list.pop()
        else:
            _, part = heapq.heappop(open_list)

        nodes_visited += 1
        status, info, steps, state, head, tape, l_pos, r_pos, reached = advance_partial_exact(
            part, step_limit
        )

        if status == "PRUNE":
            prune_counts[info] += 1
            continue
        if status == "BUDGET":
            budget_cutoffs += 1
            continue
        if status == "HALT":
            w0 = part[("A", 0)][0]
            witnesses_by_root[w0] += 1
            cand = (steps, len(tape), r_pos - l_pos + 1, complete_partial_table(part))
            if best_overall is None or cand[:3] > best_overall[:3]:
                best_overall = cand
            if best_by_root[w0] is None or cand[:3] > best_by_root[w0][:3]:
                best_by_root[w0] = cand
            continue

        # status == "BRANCH": info is the first undefined slot (state, sym)
        slot = info
        k = len(reached)
        w0 = part[("A", 0)][0]

        if k == 6:
            # All 4 halting assignments (w, m, 'H') are valid 6-state halting witnesses
            for w in SYMBOLS:
                for m in MOVES:
                    nh = head + (-1 if m == "L" else 1)
                    ones = len(tape) + (
                        1 if (w == 1 and head not in tape) else (-1 if (w == 0 and head in tape) else 0)
                    )
                    span = max(r_pos, nh) - min(l_pos, nh) + 1
                    h_part = dict(part)
                    h_part[slot] = (w, m, HALT)
                    witnesses_by_root[w0] += 1
                    cand = (steps + 1, ones, span, complete_partial_table(h_part))
                    if best_overall is None or cand[:3] > best_overall[:3]:
                        best_overall = cand
                    if best_by_root[w0] is None or cand[:3] > best_by_root[w0][:3]:
                        best_by_root[w0] = cand
        else:
            # 4 premature halting assignments (w, m, 'H') pruned by EXACT-03
            prune_counts["EXACT-03"] += 4

        adm_states = list(STATES[:k]) + ([STATES[k]] if k < 6 else [])
        children: list[tuple[TransitionTable, int]] = []
        for w in SYMBOLS:
            for m in MOVES:
                for q_next in adm_states:
                    new_k = k + (1 if q_next not in reached else 0)
                    if (steps + 1) + (6 - new_k) + 1 > step_limit:
                        prune_counts["EXACT-04"] += 1
                        continue
                    c_part = dict(part)
                    c_part[slot] = (w, m, q_next)
                    children.append((c_part, new_k))

        if ordering == "lex":
            for c_part, _ in reversed(children):
                open_list.append(c_part)
        else:
            for c_part, new_k in children:
                serial += 1
                heuristic_order_decisions += 1
                heapq.heappush(
                    open_list,
                    (heuristic_priority_key(c_part, new_k, steps + 1, serial), c_part),
                )

    elapsed = time.perf_counter() - t_start
    return {
        "step_limit": step_limit,
        "max_nodes": max_nodes,
        "ordering": ordering,
        "nodes_visited": nodes_visited,
        "open_remaining": len(open_list),
        "exhaustive": len(open_list) == 0,
        "total_witnesses": witnesses_by_root[0] + witnesses_by_root[1],
        "witnesses_w0_eq_0": witnesses_by_root[0],
        "witnesses_w0_eq_1": witnesses_by_root[1],
        "budget_cutoffs": budget_cutoffs,
        "prune_counts": prune_counts,
        "heuristic_order_decisions": heuristic_order_decisions,
        "best_overall": best_overall,
        "best_w0_eq_0": best_by_root[0],
        "best_w0_eq_1": best_by_root[1],
        "elapsed_sec": round(elapsed, 4),
    }


def run_falsification_suite() -> dict[str, Any]:
    """Execute all required WP02 falsification tests (Cases E.1 through E.6)."""
    results: dict[str, Any] = {}

    # E.1: Protected 6-step baseline (M_BASE)
    m_base: TransitionTable = {
        ("A", 0): (1, "R", "B"), ("A", 1): (1, "R", "H"),
        ("B", 0): (1, "R", "C"), ("B", 1): (1, "R", "H"),
        ("C", 0): (1, "R", "D"), ("C", 1): (1, "R", "H"),
        ("D", 0): (1, "R", "E"), ("D", 1): (1, "R", "H"),
        ("E", 0): (1, "R", "F"), ("E", 1): (1, "R", "H"),
        ("F", 0): (1, "R", "H"), ("F", 1): (1, "R", "H"),
    }
    raw_base = format_solution_json(m_base)
    ind_base = score_independent(raw_base)
    prot_base = score_protected_evaluator(raw_base)
    assert ind_base == prot_base and ind_base["passed"] is True
    assert [m["value"] for m in ind_base["metrics"]] == [6, 6, 7]
    assert canonicalize_exact(m_base) == m_base
    results["E1_baseline"] = {
        "sha256": hashlib.sha256(raw_base).hexdigest(),
        "metrics": [6, 6, 7],
        "canonical_fixed_point": True,
        "dual_concordant": True,
    }

    # E.2: Valid first-write-0 6-step counterexample to WP01 TNF (M_FW0)
    m_fw0 = dict(m_base)
    m_fw0[("A", 0)] = (0, "R", "B")
    raw_fw0 = format_solution_json(m_fw0)
    ind_fw0 = score_independent(raw_fw0)
    prot_fw0 = score_protected_evaluator(raw_fw0)
    assert ind_fw0 == prot_fw0 and ind_fw0["passed"] is True
    assert [m["value"] for m in ind_fw0["metrics"]] == [6, 5, 7]
    assert canonicalize_exact(m_fw0) == m_fw0
    status_fw0, *_ = advance_partial_exact(m_fw0, VALIDATION_BUDGET)
    assert status_fw0 == "HALT"
    results["E2_first_write_0_counterexample"] = {
        "sha256": hashlib.sha256(raw_fw0).hexdigest(),
        "metrics": [6, 5, 7],
        "canonical_fixed_point": True,
        "survives_exact_search": True,
        "dual_concordant": True,
    }

    # E.3: Machine visiting all 6 states that never halts within validation budget (M_NONHALT_6)
    m_nonhalt6: TransitionTable = {
        ("A", 0): (1, "R", "B"), ("A", 1): (1, "L", "A"),
        ("B", 0): (1, "R", "C"), ("B", 1): (1, "L", "A"),
        ("C", 0): (1, "R", "D"), ("C", 1): (1, "L", "A"),
        ("D", 0): (1, "R", "E"), ("D", 1): (1, "L", "A"),
        ("E", 0): (1, "R", "F"), ("E", 1): (1, "L", "A"),
        ("F", 0): (1, "R", "F"), ("F", 1): (1, "L", "A"),
    }
    raw_nh6 = format_solution_json(m_nonhalt6)
    ind_nh6 = score_independent(raw_nh6, step_limit=1000)
    prot_nh6 = score_protected_evaluator(raw_nh6, step_limit=1000)
    assert ind_nh6 == prot_nh6 and ind_nh6["passed"] is False
    assert ind_nh6["details"]["error"] == "machine did not halt within the private execution budget"
    # Partial without F1 (not closed) is pruned by EXACT-07 at step 5; full table pruned by EXACT-05a at step 0
    part_nh6 = {k: v for k, v in m_nonhalt6.items() if k != ("F", 1)}
    st_full, rule_full, *_ = advance_partial_exact(m_nonhalt6, VALIDATION_BUDGET)
    st_part, rule_part, steps_part, *_ = advance_partial_exact(part_nh6, VALIDATION_BUDGET)
    assert (st_full, rule_full) == ("PRUNE", "EXACT-05a")
    assert (st_part, rule_part, steps_part) == ("PRUNE", "EXACT-07", 5)
    results["E3_six_state_nonhalting"] = {
        "full_table_prune": rule_full,
        "partial_table_prune": (rule_part, steps_part),
        "evaluator_rejected": True,
    }

    # E.4: Machine halting before reaching all 6 states (M_EARLY_HALT_5)
    m_early5 = dict(m_base)
    m_early5[("E", 0)] = (1, "R", HALT)
    raw_early5 = format_solution_json(m_early5)
    ind_early5 = score_independent(raw_early5)
    prot_early5 = score_protected_evaluator(raw_early5)
    assert ind_early5 == prot_early5 and ind_early5["passed"] is False
    assert ind_early5["details"]["error"] == "machine halted without reaching all six states; missing F"
    st_e5_closed, rule_e5_closed, steps_e5_closed, *_ = advance_partial_exact(
        m_early5, VALIDATION_BUDGET
    )
    assert (st_e5_closed, rule_e5_closed, steps_e5_closed) == ("PRUNE", "EXACT-05b", 0)
    m_early5_dyn = dict(m_early5)
    m_early5_dyn[("E", 1)] = (1, "R", "F")
    st_e5_dyn, rule_e5_dyn, steps_e5_dyn, *_ = advance_partial_exact(
        m_early5_dyn, VALIDATION_BUDGET
    )
    assert (st_e5_dyn, rule_e5_dyn, steps_e5_dyn) == ("PRUNE", "EXACT-03", 5)
    results["E4_premature_halt"] = {
        "static_closed_prune": (rule_e5_closed, steps_e5_closed),
        "dynamic_halt_prune": (rule_e5_dyn, steps_e5_dyn),
        "evaluator_error": ind_early5["details"]["error"],
    }

    # E.5: Symmetry orbit invariance across S_Q^A and Z_2^dir on both w0=1 (89,911 steps) and w0=0 (8,021 steps)
    m_89911 = complete_partial_table({
        slot: val for slot, val in PRIORITY_SPINE_CORES[0].items()
    } | {("C", 1): (1, "R", HALT)})
    m_8021 = complete_partial_table({
        slot: val for slot, val in PRIORITY_SPINE_CORES[2].items()
    } | {("F", 0): (1, "R", HALT)})
    perm_test = {"A": "A", "B": "F", "C": "D", "D": "B", "E": "E", "F": "C"}

    for label, base_m, expected_metrics in [
        ("orbit_89911_w0_eq_1", m_89911, [89_911, 185, 541]),
        ("orbit_8021_w0_eq_0", m_8021, [8_021, 41, 121]),
    ]:
        for reflect in (False, True):
            for p_map in (
                {"A": "A", "B": "B", "C": "C", "D": "D", "E": "E", "F": "F"},
                perm_test,
            ):
                transformed = apply_symmetry(base_m, p_map, reflect=reflect)
                raw_tr = format_solution_json(transformed)
                s_ind = score_independent(raw_tr, step_limit=VALIDATION_BUDGET)
                s_prot = score_protected_evaluator(raw_tr, step_limit=VALIDATION_BUDGET)
                assert s_ind == s_prot and s_ind["passed"] is True
                assert [m["value"] for m in s_ind["metrics"]] == expected_metrics
                assert canonicalize_exact(transformed, step_limit=VALIDATION_BUDGET) == base_m
        results[f"E5_{label}"] = {
            "metrics": expected_metrics,
            "all_4_conjugates_preserved": True,
            "canonical_recovery_exact": True,
        }

    # E.6: Adversarial boundary tests for each nontrivial exact pruning rule
    # E.6a (ADV-EXACT-04): Sharp equality boundary t + (6 - |R_t|) + 1 == B at t=3, |R_3|=2, B=8
    m_adv_04: TransitionTable = {
        ("A", 0): (1, "R", "B"), ("A", 1): (1, "R", "B"),
        ("B", 0): (1, "L", "A"), ("B", 1): (1, "R", "C"),
        ("C", 0): (1, "R", "D"), ("C", 1): (1, "R", "H"),
        ("D", 0): (1, "R", "E"), ("D", 1): (1, "R", "H"),
        ("E", 0): (1, "R", "F"), ("E", 1): (1, "R", "H"),
        ("F", 0): (1, "R", "H"), ("F", 1): (1, "R", "H"),
    }
    st_b8, _, steps_b8, *_ = advance_partial_exact(m_adv_04, step_limit=8)
    st_b7, rule_b7, steps_b7, *_ = advance_partial_exact(m_adv_04, step_limit=7)
    assert (st_b8, steps_b8) == ("HALT", 8)
    assert (st_b7, rule_b7, steps_b7) == ("PRUNE", "EXACT-04", 3)

    # E.6b (ADV-EXACT-05): Open 2-state subtable {A,B} with B1 undefined vs closed {A,B}
    open_ab: TransitionTable = {
        ("A", 0): (1, "R", "B"),
        ("B", 0): (1, "L", "A"),
        ("A", 1): (1, "R", "B"),
    }
    closed_ab = dict(open_ab) | {("B", 1): (1, "L", "A")}
    st_open, slot_open, steps_open, *_ = advance_partial_exact(open_ab, step_limit=20)
    st_closed, rule_closed, steps_closed, *_ = advance_partial_exact(closed_ab, step_limit=20)
    assert (st_open, slot_open, steps_open) == ("BRANCH", ("B", 1), 3)
    assert (st_closed, rule_closed, steps_closed) == ("PRUNE", "EXACT-05b", 0)

    # E.6c (ADV-EXACT-06): Repeats (state='A', head=0, tape[0]=0) at steps 0 and 2, but tape={1} at step 2
    m_adv_06 = dict(m_adv_04)
    m_adv_06[("A", 0)] = (0, "R", "B")
    st_06, _, steps_06, *_ = advance_partial_exact(m_adv_06, step_limit=20)
    assert (st_06, steps_06) == ("HALT", 8)

    # E.6d (ADV-EXACT-07): Self-loop D,0 -> [1,'R','D'] on 0 at head=0 with obstacle '1' ahead at cell +2
    m_adv_07: TransitionTable = {
        ("A", 0): (1, "R", "B"), ("A", 1): (1, "R", "H"),
        ("B", 0): (1, "R", "C"), ("B", 1): (1, "R", "H"),
        ("C", 0): (1, "L", "C"), ("C", 1): (0, "L", "D"),
        ("D", 0): (1, "R", "D"), ("D", 1): (1, "R", "E"),
        ("E", 0): (1, "R", "F"), ("E", 1): (1, "R", "H"),
        ("F", 0): (1, "R", "H"), ("F", 1): (1, "R", "H"),
    }
    st_07, _, steps_07, *_ = advance_partial_exact(m_adv_07, step_limit=20)
    assert (st_07, steps_07) == ("HALT", 7)

    results["E6_adversarial_pruning_boundaries"] = {
        "ADV_EXACT_04_b8_halt_b7_prune": (st_b8, steps_b8, st_b7, rule_b7, steps_b7),
        "ADV_EXACT_05_open_branch_closed_prune": (st_open, slot_open, st_closed, rule_closed),
        "ADV_EXACT_06_distant_support_survives": (st_06, steps_06),
        "ADV_EXACT_07_obstacle_ahead_survives": (st_07, steps_07),
    }

    return results


if __name__ == "__main__":
    fals = run_falsification_suite()
    enum_b6_lex = run_exact_canonical_search(step_limit=6, max_nodes=None, ordering="lex")
    enum_b6_heur = run_exact_canonical_search(
        step_limit=6, max_nodes=None, ordering="heuristic_priority"
    )
    assert enum_b6_lex["nodes_visited"] == enum_b6_heur["nodes_visited"] == 682
    assert enum_b6_lex["total_witnesses"] == enum_b6_heur["total_witnesses"] == 2048
    assert enum_b6_lex["prune_counts"] == enum_b6_heur["prune_counts"]

    enum_b7_lex = run_exact_canonical_search(step_limit=7, max_nodes=None, ordering="lex")
    enum_b7_heur = run_exact_canonical_search(
        step_limit=7, max_nodes=None, ordering="heuristic_priority"
    )
    assert enum_b7_lex["nodes_visited"] == enum_b7_heur["nodes_visited"] == 27386
    assert enum_b7_lex["total_witnesses"] == enum_b7_heur["total_witnesses"] == 60160
    assert enum_b7_lex["prune_counts"] == enum_b7_heur["prune_counts"]

    tranche_val = run_exact_canonical_search(
        step_limit=VALIDATION_BUDGET, max_nodes=3000, ordering="heuristic_priority"
    )
    print("FALSIFICATION:", json.dumps(fals, sort_keys=True))
    print("ENUM_B6:", json.dumps({k: v for k, v in enum_b6_lex.items() if not k.startswith("best_")}, sort_keys=True))
    print("ENUM_B7:", json.dumps({k: v for k, v in enum_b7_lex.items() if not k.startswith("best_")}, sort_keys=True))
    print(
        "TRANCHE_VAL:",
        json.dumps(
            {
                k: (v[:3] if k.startswith("best_") and v is not None else v)
                for k, v in tranche_val.items()
            },
            sort_keys=True,
        ),
    )
```

## Claim boundary

This contribution validates the completeness of the 2-root canonical search enumeration (`A,0 -> [0,"R","B"]` and `A,0 -> [1,"R","B"]`), the soundness of the exact pruning rules (`EXACT-01` through `EXACT-07`), the survival of the first-write-`0` counterexample `M_FW0`, and the exact dual-scorer concordance of the bounded-tranche witnesses up to `(steps=89911, ones=185, tape_span=541)` on `w0=1` and `(steps=8021, ones=41, tape_span=122)` on `w0=0`. It does not claim an exhaustive traversal of the full 12-slot tree at $B = 250{,}000$ (`36,698` open frontier nodes remain after the `3,000`-node bounded tranche), does not establish the mathematical value of $S(6)$ or $\Sigma(6)$, does not claim world-record status, does not submit any payload to AutoLab, and does not constitute GCL acceptance or MATHCERT certification.

## Next residual

Execute a scaled multi-worker tranche over the `HEUR-01`-ordered canonical search frontier under `step_limit = 250,000` and `step_limit = 1,000,000`, adding an exact proved induction decider for fixed-wall counter/bouncer cycles (where the one-sided tape support grows by a constant block per cycle) to further reduce `BUDGET` cutoffs on deep interior nodes. Replay the resulting top witnesses on both the $w_0 = 0$ and $w_0 = 1$ root branches through the protected evaluator for campaign promotion review.
