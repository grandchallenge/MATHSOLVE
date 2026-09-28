Find six-state, two-symbol Turing machines that halt after long exact runs, giving checkable lower bounds for Busy Beaver 6.

## Task

The Busy Beaver problem asks for the longest-running halting program in a fixed tiny Turing-machine model. The six-state, two-symbol value is open. Your submission is one complete six-state transition table. The evaluator starts it on an all-zero tape, simulates it exactly, and accepts it only when it halts within the private safety limit after visiting all six non-halting states.

Every accepted submission is therefore a rigorous finite lower-bound witness for `S(6)`: its `steps` value is the exact number of transitions the submitted program executed before halting. The hill does not claim that a one-week team will determine the exact Busy Beaver 6 value. It rewards verified candidate discovery in the actual six-state model.

## Submission format

Submit a directory containing exactly one UTF-8 JSON file:

```json
{
  "transitions": {
    "A": {"0": [1, "R", "B"], "1": [1, "R", "H"]},
    "B": {"0": [1, "R", "C"], "1": [1, "R", "H"]},
    "C": {"0": [1, "R", "D"], "1": [1, "R", "H"]},
    "D": {"0": [1, "R", "E"], "1": [1, "R", "H"]},
    "E": {"0": [1, "R", "F"], "1": [1, "R", "H"]},
    "F": {"0": [1, "R", "H"], "1": [1, "R", "H"]}
  }
}
```

There are exactly six non-halting states, `A` through `F`, and the halting state `H`. Each of the twelve entries is `[write, move, next_state]`, where:

- `write` is integer `0` or `1`;
- `move` is string `"L"` or `"R"`;
- `next_state` is one of `"A"` through `"F"` or `"H"`.

The blank-tape start is state `A`, head position 0, and an all-zero bi-infinite tape. The sample is valid and halts after six steps. State labels and the symbols are deliberately not normalized: the requirement that every state be reached ensures the candidate genuinely uses all six states.

## Metrics

| metric | direction | meaning |
| --- | --- | --- |
| `steps` | max | Exact number of transitions before halting. |
| `ones` | max | Number of `1` symbols on the tape at halting. |
| `tape_span` | max | Number of tape cells from the leftmost to rightmost position visited. |

Scores are lexicographic. The evaluator computes every metric; do not include claimed scores in the JSON.

## Held-out split and limits

Both validation and final evaluation simulate the same blank-tape model, but use separate private execution budgets. A candidate that does not halt before the budget is rejected rather than receiving a capped score, so an infinite loop cannot masquerade as a lower bound. The final result is the test-split result.

## What counts as progress

Any accepted candidate is an exact, replayable lower-bound witness for the actual six-state Busy Beaver function. A high score is a candidate lower bound, not a proof that no longer halting machine exists. The transition table and resulting space-time diagram give the presentation artifact.
