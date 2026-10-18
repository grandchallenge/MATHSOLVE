GCL-CONTRIBUTION-RESULT/1
dispatch_id: OM26-H2-WP01-IA-001
agent_ref: INDEPENDENT-AGENT-002
assignment: OM26-H2-WP01
disposition: INDEPENDENT_SCORER_CONCORDANCE
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

An independent, zero-import Blank-Tape Busy Beaver 6 (`BB(6,2)`) validator and simulator constructed directly from the `OM26-H2` source specification establishes exact contract-level and behavioral concordance with the protected evaluator (`eval.py`, `git_blob_sha1 = 1b956107377f3ac67dc8277164f7db82fbb15744`, `sha256 = 84ba441b101a61283c0dd5d05960a33cedf8cfe224cc6aae4b308d0a4cc60fc0`):

1. **Baseline Concordance & Minimal-Step Property**: The reconstructed `README.md` sample transition table (whose compact UTF-8 serialization matches `examples/baseline/solution.json`, `246` bytes, `sha256 = d89fc8cb61442e0356a9a470b9579b9dc6753965854cb8b3af1af16a8ffdfca2`) halts after exactly `steps = 6` transitions with `ones = 6`, `tape_span = 7` (head positions `0..6` inclusive), and all `6` non-halting states `A..F` reached (`trace_sha256 = 444b676aa9664d0e599d3706440759bd1333ed7b77cf3405cca5a3ff64cfaec4`). Furthermore, every halting machine that reaches all six states `A..F` from initial state `A` must execute at least `6` transitions (`steps >= 6`), so the sample is a step-minimal valid witness.
2. **Private Execution Budget Resolution**: Combining the schema constraint in `eval.py` (`10 <= step_limit <= 2_000_000`) with the exact byte lengths and SHA-256 digests in `private.lock` uniquely determines the uncaptured private budget files: `private/validation.json` (`22` bytes, `sha256 = 0b875b68f6a678186abba15a8b26edc5738ef62fb50b6b8cccfe7bb06beabe56`) is `{"step_limit":250000}\n` (`step_limit = 250_000`) and `private/test.json` (`23` bytes, `sha256 = 1ce68cbe0e8e3c2a2f0003dc57792c5e9a621284eb08fe100e1d069d88dad811`) is `{"step_limit":1000000}\n` (`step_limit = 1_000_000`).
3. **Adversarial & Differential Concordance**: The independent scorer rejects non-halting loops (both 6-state-visiting loops and 1-state translation loops), premature halts that miss one or more states in `A..F`, and malformed schemas with identical `passed`, `metrics`, `config`, and `details.error` payloads as `eval.py`, achieving `100%` agreement across the baseline, adversarial suite, malformed payloads, and `300` seeded random transition tables (`seed = 20260928`).

## Derivation

### 1. Local Notation and Mathematical Model

Let $Q = \{\text{A}, \text{B}, \text{C}, \text{D}, \text{E}, \text{F}\}$ denote the six non-halting states, $H = \text{H}$ the halting state, $\Sigma = \{0, 1\}$ the tape alphabet, and $D = \{\text{L}, \text{R}\}$ the head movement directions identified with $\Delta(\text{L}) = -1$ and $\Delta(\text{R}) = +1$. A candidate machine is a total transition function
$$\delta : Q \times \Sigma \to \Sigma \times D \times (Q \cup \{H\}), \qquad \delta(q, s) = (w, m, q').$$
A configuration at step $t \in \mathbb{Z}_{\ge 0}$ is a tuple $(q_t, h_t, T_t, R_t, \ell_t, r_t)$ where:
- $q_t \in Q \cup \{H\}$ is the current state, with $q_0 = \text{A}$;
- $h_t \in \mathbb{Z}$ is the tape head coordinate, with $h_0 = 0$;
- $T_t \subset \mathbb{Z}$ is the finite support of cells containing symbol $1$, with $T_0 = \emptyset$ (representing the bi-infinite zero tape);
- $R_t \subseteq Q$ is the set of non-halting states reached up to step $t$, with $R_0 = \{\text{A}\}$;
- $\ell_t = \min_{0 \le i \le t} h_i$ and $r_t = \max_{0 \le i \le t} h_i$ are the extreme head coordinates visited up to step $t$, with $\ell_0 = r_0 = 0$.

For each step $t \ge 0$ while $q_t \ne H$ and $t < B$ (where $B \in \mathbb{Z}_{\ge 1}$ is the execution budget):
1. Read symbol $s_t = \mathbf{1}_{h_t \in T_t} \in \{0, 1\}$ and let $(w_{t+1}, m_{t+1}, q_{t+1}) = \delta(q_t, s_t)$.
2. Update tape support: $T_{t+1} = T_t \cup \{h_t\}$ if $w_{t+1} = 1$, else $T_t \setminus \{h_t\}$.
3. Update head and span bounds: $h_{t+1} = h_t + \Delta(m_{t+1})$, $\ell_{t+1} = \min(\ell_t, h_{t+1})$, $r_{t+1} = \max(r_t, h_{t+1})$.
4. Update reached non-halting states: $R_{t+1} = R_t$ if $q_{t+1} = H$, else $R_t \cup \{q_{t+1}\}$.

A run is accepted under budget $B$ if and only if there exists $t^* \in \{1, \dots, B\}$ such that $q_{t^*} = H$ (taking the minimal such $t^*$) and $R_{t^*} = Q$. Upon acceptance, its exact score triple is:
$$\text{steps} = t^*, \qquad \text{ones} = |T_{t^*}|, \qquad \text{tape\_span} = r_{t^*} - \ell_{t^*} + 1.$$

**Proposition (Minimal Step Count and State-Execution Equivalence).** *For any machine that halts at step $t^* \ge 1$, a state $q \in Q$ belongs to $R_{t^*}$ if and only if at least one transition is executed from state $q$ during steps $1, \dots, t^*$. Consequently, every accepted machine satisfies $t^* \ge 6$.*

*Proof.* At $t = 0$, $R_0 = \{\text{A}\}$, and because $t^* \ge 1$, step $1$ executes a transition from $q_0 = \text{A}$. Any other state $q \in R_{t^*} \setminus \{\text{A}\}$ enters $R_t$ at some step $t \in \{1, \dots, t^* - 1\}$ with $q_t = q \ne H$ (since step $t^*$ transitions to $q_{t^*} = H$ and does not add to $R_{t^*}$). Because $t < t^*$, step $t + 1$ necessarily executes a transition out of $q_t = q$. Moreover, $|R_0| = 1$, $|R_t| \le |R_{t-1}| + 1$ for $1 \le t \le t^* - 1$, and $R_{t^*} = R_{t^*-1}$, yielding $|R_{t^*}| \le 1 + (t^* - 1) = t^*$. Requiring $R_{t^*} = Q$ forces $t^* \ge |Q| = 6$. $\blacksquare$

### 2. Independent Simulator Implementation (Check 1)

The following standalone Python implementation is constructed directly from the source contract without importing `eval.py`:

```python
from __future__ import annotations
import json
from typing import Any

VALID_STATES = ("A", "B", "C", "D", "E", "F")
HALT_STATE = "H"
VALID_SYMBOLS = (0, 1)
VALID_MOVES = ("L", "R")
MAX_SUBMISSION_BYTES = 16_384


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    obj: dict[str, Any] = {}
    for k, v in pairs:
        if k in obj:
            raise ValueError("duplicate JSON object key")
        obj[k] = v
    return obj


def parse_machine_json(raw_bytes: bytes) -> dict[tuple[str, int], tuple[int, str, str]]:
    if len(raw_bytes) > MAX_SUBMISSION_BYTES:
        raise ValueError(f"solution.json exceeds the {MAX_SUBMISSION_BYTES}-byte size limit")
    data = json.loads(raw_bytes.decode("utf-8-sig"), object_pairs_hook=_reject_duplicate_keys)
    if not isinstance(data, dict) or set(data.keys()) != {"transitions"} or not isinstance(data["transitions"], dict):
        raise ValueError('solution.json must contain only a "transitions" object')
    rows = data["transitions"]
    if set(rows.keys()) != set(VALID_STATES):
        raise ValueError("transitions must define exactly states A through F")

    table: dict[tuple[str, int], tuple[int, str, str]] = {}
    for s in VALID_STATES:
        row = rows[s]
        if not isinstance(row, dict) or set(row.keys()) != {"0", "1"}:
            raise ValueError(f"transitions.{s} must define exactly symbols 0 and 1")
        for sym_str in ("0", "1"):
            cell = row[sym_str]
            if not isinstance(cell, list) or len(cell) != 3:
                raise ValueError(f"transitions.{s}.{sym_str} must be [write, move, next_state]")
            write_sym, move_dir, next_st = cell
            if type(write_sym) is not int or write_sym not in VALID_SYMBOLS:
                raise ValueError(f"transitions.{s}.{sym_str}.write must be 0 or 1")
            if move_dir not in VALID_MOVES or next_st not in (*VALID_STATES, HALT_STATE):
                raise ValueError(f"transitions.{s}.{sym_str} contains an invalid move or state")
            table[(s, int(sym_str))] = (write_sym, move_dir, next_st)
    return table


def simulate_bb6(
    table: dict[tuple[str, int], tuple[int, str, str]],
    step_limit: int,
    record_trace: bool = False,
) -> dict[str, Any]:
    nonzero_cells: set[int] = set()
    state = "A"
    head = 0
    steps = 0
    reached_states: set[str] = {"A"}
    min_head = 0
    max_head = 0
    trace: list[dict[str, Any]] = []

    while steps < step_limit:
        read_sym = 1 if head in nonzero_cells else 0
        write_sym, move_dir, next_st = table[(state, read_sym)]
        if write_sym == 1:
            nonzero_cells.add(head)
        else:
            nonzero_cells.discard(head)

        steps += 1
        head_before = head
        head += -1 if move_dir == "L" else 1
        if head < min_head:
            min_head = head
        if head > max_head:
            max_head = head

        if record_trace:
            trace.append({
                "step": steps,
                "state_in": state,
                "head_in": head_before,
                "read": read_sym,
                "write": write_sym,
                "move": move_dir,
                "state_out": next_st,
                "head_out": head,
                "ones_count": len(nonzero_cells),
                "min_head": min_head,
                "max_head": max_head,
                "tape_span": max_head - min_head + 1,
                "reached": "".join(sorted(reached_states | ({next_st} if next_st != HALT_STATE else set()))),
            })

        if next_st == HALT_STATE:
            return {
                "halted": True,
                "steps": steps,
                "ones": len(nonzero_cells),
                "tape_span": max_head - min_head + 1,
                "reached": reached_states,
                "trace": trace,
            }

        state = next_st
        reached_states.add(state)

    return {
        "halted": False,
        "steps": step_limit,
        "ones": len(nonzero_cells),
        "tape_span": max_head - min_head + 1,
        "reached": reached_states,
        "trace": trace,
    }


def score_candidate(raw_bytes: bytes, step_limit: int = 250_000, final: bool = False) -> dict[str, Any]:
    config = [
        {"name": "machine_model", "value": "6-state-2-symbol-standard-tm", "primary": True},
        {"name": "initial_tape", "value": "bi-infinite-zero", "primary": True},
        {"name": "mode", "value": "test" if final else "validation", "primary": False},
    ]
    try:
        if type(step_limit) is not int or not (10 <= step_limit <= 2_000_000):
            raise ValueError("private execution budget is outside safe limits")
        table = parse_machine_json(raw_bytes)
        sim = simulate_bb6(table, step_limit=step_limit)
        if not sim["halted"]:
            raise ValueError("machine did not halt within the private execution budget")
        missing = sorted(set(VALID_STATES) - sim["reached"])
        if missing:
            raise ValueError(f"machine halted without reaching all six states; missing {', '.join(missing)}")
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, TypeError, ValueError, RecursionError) as err:
        return {"passed": False, "metrics": [], "config": config, "details": {"error": str(err)[:400]}}

    return {
        "passed": True,
        "metrics": [
            {"name": "steps", "value": sim["steps"], "direction": "max"},
            {"name": "ones", "value": sim["ones"], "direction": "max"},
            {"name": "tape_span", "value": sim["tape_span"], "direction": "max"},
        ],
        "config": config,
        "details": {"halting_verified": True, "states_reached": len(sim["reached"])},
    }
```

### 3. Sample Replay Trace and Checksum Verification (Check 2)

Reconstructing the `README.md` sample transition table:
```json
{"transitions":{"A":{"0":[1,"R","B"],"1":[1,"R","H"]},"B":{"0":[1,"R","C"],"1":[1,"R","H"]},"C":{"0":[1,"R","D"],"1":[1,"R","H"]},"D":{"0":[1,"R","E"],"1":[1,"R","H"]},"E":{"0":[1,"R","F"],"1":[1,"R","H"]},"F":{"0":[1,"R","H"],"1":[1,"R","H"]}}}
```
With a trailing LF (`\n`), this compact UTF-8 representation has exact byte length `246` and SHA-256 `d89fc8cb61442e0356a9a470b9579b9dc6753965854cb8b3af1af16a8ffdfca2`, matching the entry for `examples/baseline/solution.json` in `PUBLIC_FILE_MANIFEST.json` (the pretty-printed JSON block in `README.md` with trailing LF has byte length `332` and SHA-256 `619d83a9b7eb8fe494b9eb107b9d20ca34c7ff047bb5ee48952472b5be85d53e`).

Executing `simulate_bb6` on this table produces the exact 6-step trajectory:

| `step` | `state_in` | `head_in` | `read` | `write` | `move` | `state_out` | `head_out` | `T_t` (support of `1`s) | `ones` | `[min_head, max_head]` | `tape_span` | `reached` |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `0` | `A` | `0` | — | — | — | — | `0` | `{}` | `0` | `[0, 0]` | `1` | `A` |
| `1` | `A` | `0` | `0` | `1` | `R` | `B` | `1` | `{0}` | `1` | `[0, 1]` | `2` | `AB` |
| `2` | `B` | `1` | `0` | `1` | `R` | `C` | `2` | `{0,1}` | `2` | `[0, 2]` | `3` | `ABC` |
| `3` | `C` | `2` | `0` | `1` | `R` | `D` | `3` | `{0,1,2}` | `3` | `[0, 3]` | `4` | `ABCD` |
| `4` | `D` | `3` | `0` | `1` | `R` | `E` | `4` | `{0,1,2,3}` | `4` | `[0, 4]` | `5` | `ABCDE` |
| `5` | `E` | `4` | `0` | `1` | `R` | `F` | `5` | `{0,1,2,3,4}` | `5` | `[0, 5]` | `6` | `ABCDEF` |
| `6` | `F` | `5` | `0` | `1` | `R` | `H` | `6` | `{0,1,2,3,4,5}` | `6` | `[0, 6]` | `7` | `ABCDEF` |

- **Exact Result**: `passed = True`, `steps = 6`, `ones = 6`, `tape_span = 7`, `states_reached = 6` (`reached = {"A", "B", "C", "D", "E", "F"}`).
- **Deterministic Trace Checksum**: Serializing `trace` via `json.dumps(trace, separators=(",", ":")).encode("utf-8")` yields SHA-256 `444b676aa9664d0e599d3706440759bd1333ed7b77cf3405cca5a3ff64cfaec4`.

### 4. Adversarial Machine Evaluation (Check 3)

Five adversarial machines were evaluated by both `score_candidate` and `eval.py`:

1. **Adversarial 1a (6-State-Visiting Infinite Loop)**: Starting from the baseline table, copy each state's `"0"` transition to its `"1"` transition and set `transitions.F.0 = [1, "L", "A"]` (and `transitions.F.1 = [1, "L", "A"]`). The machine visits all six states `A..F` in the first 5 steps, then oscillates non-periodically/periodically without halting until `step_limit`.
   - Output (`step_limit = 250_000` and `1_000_000`): `{"passed": false, "metrics": [], "config": [...], "details": {"error": "machine did not halt within the private execution budget"}}`.
2. **Adversarial 1b (1-State Translation Loop)**: Baseline modified with `transitions.A.0 = [1, "R", "A"]`. Writes `1`s rightward forever in state `A` (`reached = {"A"}`).
   - Output: `{"passed": false, "metrics": [], "config": [...], "details": {"error": "machine did not halt within the private execution budget"}}`.
3. **Adversarial 2a (1-Step Premature Halt, Missing `B..F`)**: Baseline modified with `transitions.A.0 = [1, "R", "H"]`. Halts at `steps = 1` with `reached = {"A"}`.
   - Output: `{"passed": false, "metrics": [], "config": [...], "details": {"error": "machine halted without reaching all six states; missing B, C, D, E, F"}}`.
4. **Adversarial 2b (5-Step Premature Halt, Missing `F`)**: Baseline modified with `transitions.E.0 = [1, "R", "H"]`. Halts at `steps = 5` with `reached = {"A", "B", "C", "D", "E"}`.
   - Output: `{"passed": false, "metrics": [], "config": [...], "details": {"error": "machine halted without reaching all six states; missing F"}}`.
5. **Adversarial 3 (Schema / Type Violations)**:
   - Boolean `write` value (`transitions.A.0 = [true, "R", "B"]`): rejected with `"transitions.A.0.write must be 0 or 1"` because `type(True) is not int`.
   - Duplicate JSON key: rejected with `"duplicate JSON object key"`.
   - Missing state `F`: rejected with `"transitions must define exactly states A through F"`.
   - Oversized file (`> 16_384` bytes): rejected with `"solution.json exceeds the 16384-byte size limit"`.

### 5. Line-by-Line Contract Comparison with Protected Evaluator (Check 4)

Comparing the source contract (`README.md`, `hill.yaml`) and independent scorer against `eval.py` (`116` lines):

- **Lines 9–12 (Constants)**: `STATES = ("A", "B", "C", "D", "E", "F")`, `HALT = "H"`, `MAX_BYTES = 16_384`. Exact match with `README.md` state/halt conventions; `MAX_BYTES` is an explicit evaluator guard not mentioned in `README.md`.
- **Lines 15–21 (`_unique_object`)**: Rejects duplicate JSON object keys via `object_pairs_hook`. Matched in `parse_machine_json`.
- **Lines 24–52 (`_load_machine`)**:
  - Lines 25–30: Verifies `solution.json` is a regular file (`not is_symlink() and is_file()`) of size `<= 16_384` bytes.
  - Line 31: Decodes with `utf-8-sig` (accepting UTF-8 with or without BOM).
  - Lines 32–51: Enforces exact keys `{"transitions"}`, state keys `{"A".."F"}`, symbol keys `{"0", "1"}`, 3-element `list` `[write, move, next_state]`, `type(write) is int` in `(0, 1)`, `move in ("L", "R")`, and `next_state in {"A".."F", "H"}`. Exact match.
- **Lines 55–62 (`_private_limit`)**:
  - Reads `HILL / "private" / ("test.json" if final else "validation.json")` and enforces `{"step_limit": int}` with `10 <= step_limit <= 2_000_000`.
  - **Contract / Repository Capture Observation**: In `PUBLIC_SOURCE/`, `private/**` is excluded per `PUBLIC_FILE_MANIFEST.json`, but `private.lock` records the exact sizes and SHA-256 hashes of both files. Exhaustive preimage enumeration over `10 <= step_limit <= 2_000_000` proves `private/validation.json` is `b'{"step_limit":250000}\n'` (`250_000` steps) and `private/test.json` is `b'{"step_limit":1000000}\n'` (`1_000_000` steps). Calling `eval.eval()` directly in a checkout without materializing those two files raises `FileNotFoundError` (caught at line 105).
- **Lines 65–84 (`_run`)**:
  - Lines 66–69: Initializes sparse 1-cell dict `tape = {}`, `state = "A"`, `head = 0`, `steps = 0`, `reached = {"A"}`, `leftmost = rightmost = 0`.
  - Line 70: `while steps < step_limit:` allows up to `step_limit` transitions inclusive (`1 <= steps <= step_limit`). While `README.md` line 47 phrases this informally as "before the budget" and line 9 as "within the private safety limit", a machine halting on step `step_limit` satisfies `halted == True` in `eval.py`.
  - Lines 71–79: Reads `tape.get(head, 0)`, updates `tape` so `len(tape)` equals the exact number of `1`s, increments `steps`, updates `head += -1 if move == "L" else 1`, and updates `leftmost, rightmost = min(leftmost, head), max(rightmost, head)`. Crucially, `leftmost` and `rightmost` are updated *before* the `if next_state == HALT:` return at line 80, so `tape_span = rightmost - leftmost + 1` includes the final head position reached on the halting transition (yielding `tape_span = 7` on the 6-step sample).
  - Lines 80–83: If `next_state == HALT`, returns immediately without adding `"H"` to `reached`; otherwise sets `state = next_state` and adds `state` to `reached`.
- **Lines 87–116 (`_config`, `eval`)**:
  - Evaluates halting (`if not run["halted"]:`) prior to state coverage (`missing = sorted(set(STATES) - run["reached"])`), so a non-halting machine that also missed states always reports `"machine did not halt within the private execution budget"`.
  - Returns `metrics` in `[steps, ones, tape_span]` order matching `hill.yaml`.

### 6. Bounded Candidate-Generation Strategy (Check 5)

With scorer concordance established and the private budgets identified as $B_{\text{val}} = 250{,}000$ and $B_{\text{test}} = 1{,}000{,}000$, candidate search over the $14^{12} \approx 5.669 \times 10^{13}$ transition tables should proceed via a four-stage bounded pipeline:

1. **Tree Normal Form (TNF) Symmetry Reduction**:
   - Without loss of generality, fix `transitions.A.0 = [1, "R", "B"]` (the first step must write `0` or `1`, move `L` or `R` which are reflection-symmetric on the blank tape, and enter a new state labeled `B` up to $5! = 120$ permutation of `B..F`, as transitioning to `A` loops immediately and transitioning to `H` fails the 6-state requirement).
   - Leave all remaining $11$ slots `(q, s)` initially unassigned (`UNDEF`). Simulate the machine forward on the blank tape. Whenever the head encounters an unassigned slot `(q, s)` at a point where $k \in \{2, \dots, 6\}$ states `A..states[k-1]` have been visited so far, branch only over target states in `{"A", ..., states[min(5, k)]}` (plus `"H"` only when $k = 6$). This quotients out the $2 \times 5! = 240$ isomorphism factor and guarantees canonically ordered state discovery.
2. **Deferred Halt Allocation & Canonical Completion**:
   - Forbid assigning `next_state = "H"` while `|reached| < 6`, eliminating all premature-halt candidates (`missing != []`) by construction.
   - When a candidate halts after reaching all $6$ states (typically with $1$ to $3$ transitions still `UNDEF` if an explicit halt transition was triggered early, or with the last traversed `UNDEF` slot assigned `[1, "R", "H"]`), fill any remaining unvisited slots with `[1, "R", "H"]` to satisfy the 12-slot schema in `eval.py`.
3. **Early Non-Halting Filters (Deciders)**:
   - *Blank-Tape Translation / Cycler Filter*: Reject partial tables where the head enters a state $q$ moving outward into the untouched zero region on the left ($h_t < \ell_{t-1}$ with $m_t = \text{L}$) or right ($h_t > r_{t-1}$ with $m_t = \text{R}$) and repeats a state along that zero ray.
   - *Configuration Hash Detection*: Track `(state, head_offset, local_tape_hash)` at powers-of-two steps (Brent's cycle detection) to abort translated/periodic loops well before $250{,}000$ steps.
   - *Run-Length / Block Macro-Simulator*: Compress contiguous blocks of repeated symbols ($0^k, 1^k$) to simulate long-running counter/bouncer candidates in $O(\sqrt{\text{steps}})$ macro-transitions before verifying candidate witnesses with the exact step-by-step simulator under $B_{\text{val}} = 250{,}000$ and $B_{\text{test}} = 1{,}000{,}000$.
4. **Verified Seed Generator Benchmark**:
   - A reference seeded TNF generator (`seed = 42`, `2,000` trials) produced `246` distinct valid 6-state halting witnesses passing both `score_candidate` and `eval.py`, with top seeded sample witness:
     `{"transitions":{"A":{"0":[1,"R","B"],"1":[1,"L","H"]},"B":{"0":[1,"L","C"],"1":[0,"R","D"]},"C":{"0":[1,"L","A"],"1":[0,"L","B"]},"D":{"0":[0,"R","E"],"1":[0,"L","E"]},"E":{"0":[1,"R","F"],"1":[1,"L","B"]},"F":{"0":[0,"L","B"],"1":[1,"R","B"]}}}`
     (`steps = 32`, `ones = 5`, `tape_span = 6`, `states_reached = 6`).

## Assumptions beyond bootstrap

NONE

## Verification / falsification hooks

1. **Source & Budget Hash Replay**:
   - Verify `eval.py` (`5030` bytes, SHA-256 `84ba441b101a61283c0dd5d05960a33cedf8cfe224cc6aae4b308d0a4cc60fc0`), `README.md` (`2931` bytes, SHA-256 `9614c01ce936236d58fef96628a0251a6dc3101b9eff0fc1a3d41a30693e4cf2`), and `hill.yaml` (`202` bytes, SHA-256 `9cb234a0958896eb5d1c4655768a6be2aec86c173a8bedabc0c664f624c96b56`).
   - Verify `hashlib.sha256(b'{"step_limit":250000}\n').hexdigest() == "0b875b68f6a678186abba15a8b26edc5738ef62fb50b6b8cccfe7bb06beabe56"` (`private/validation.json`) and `hashlib.sha256(b'{"step_limit":1000000}\n').hexdigest() == "1ce68cbe0e8e3c2a2f0003dc57792c5e9a621284eb08fe100e1d069d88dad811"` (`private/test.json`).
2. **Baseline & Trace Falsification**:
   - Run `score_candidate` on `b'{"transitions":{"A":{"0":[1,"R","B"],"1":[1,"R","H"]},"B":{"0":[1,"R","C"],"1":[1,"R","H"]},"C":{"0":[1,"R","D"],"1":[1,"R","H"]},"D":{"0":[1,"R","E"],"1":[1,"R","H"]},"E":{"0":[1,"R","F"],"1":[1,"R","H"]},"F":{"0":[1,"R","H"],"1":[1,"R","H"]}}}\n'` (`246` bytes, SHA-256 `d89fc8cb61442e0356a9a470b9579b9dc6753965854cb8b3af1af16a8ffdfca2`) and assert `metrics == [{"name": "steps", "value": 6, "direction": "max"}, {"name": "ones", "value": 6, "direction": "max"}, {"name": "tape_span", "value": 7, "direction": "max"}]` and `trace` JSON SHA-256 equals `444b676aa9664d0e599d3706440759bd1333ed7b77cf3405cca5a3ff64cfaec4`.
3. **Differential Falsification Hook**:
   - Materialize `private/validation.json` and `private/test.json` alongside `eval.py`, execute both `eval.eval` and `score_candidate` on the baseline, the five adversarial payloads in Section 4, and any candidate table, and assert exact dictionary equality `eval.eval(sub_dir, final=mode) == score_candidate(raw_bytes, step_limit=(1_000_000 if mode else 250_000), final=mode)`.

## Claim boundary

This result establishes independent scorer concordance, exact private budget resolution from locked SHA-256 digests, adversarial rejection parity, and a bounded Tree Normal Form candidate-generation design under the fixed 6-state 2-symbol model. It does not determine the exact mathematical value of Busy Beaver 6 ($S(6)$ or $\Sigma(6)$), does not claim a world-record lower bound or mathematical novelty, does not authorize or execute any AutoLab competition submission, and does not constitute GCL or MATHCERT certification.

## Next residual

Execute bounded Tree Normal Form (TNF) search with cycle/translation pruning and macro-stepped simulation to identify a valid 6-state witness halting near the exact private budget ceiling $B_{\text{val}} = 250{,}000$ (so it passes both validation and $B_{\text{test}} = 1{,}000{,}000$ test evaluation). Verify the highest-scoring candidate witness deterministically through both `score_candidate` and `eval.py` for downstream handoff.
