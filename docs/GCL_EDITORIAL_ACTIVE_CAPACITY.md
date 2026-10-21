# GCL Editorial worker concurrency; serialized operational register

Status: protected implementation candidate for MATHSOLVE #1049, register #1096.
The policy allows **at most eight simultaneous acknowledged Editorial START runs**
across MATH-PROGRAMME, ADAPTIVE-INTELLIGENCE-ATLAS and COMPUTATIONAL-DIFFICULTY-ATLAS.
A mathematics task using `direct_editorial` mechanics is **not** Editorial.

The publicly readable MATHSOLVE #1096 register accepts authenticated worker
`EDITORIAL-START/1` requests, not Solve `/claim` reservations. A worker
must wait for a controller-authored `GCL-EDITORIAL-DECISION/1` **GRANTED**
receipt bound to that exact request-comment ID and GitHub actor **before**
beginning a newly governed Editorial task. A granted run is valid for four
hours; work beyond expiry requires a new bounded start. Release its slot with
an authenticated `EDITORIAL-END/1` from the same actor.

Example START on register #1096:

```
EDITORIAL-START/1
repository: grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS
issue: 407
run_id: 1234567890abcdef1234567890abcdef
source_head: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

Example END (same actual repository, issue and 32-digit run ID):

```
EDITORIAL-END/1
repository: grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS
issue: 407
run_id: 1234567890abcdef1234567890abcdef
```

The exact source commit must exist. Only OPEN, AVAILABLE, direct-issue
Editorial jobs are eligible. An existing active job, the ninth active START,
missing/wrong actor, spoofed controller receipt, unknown route, maths job,
malformed record, incomplete history or failed GitHub read is refused.
The GitHub Actions concurrency group serializes START and END transactions
and scans the complete authenticated register before each decision.
Controller receipt history, not Project AVAILABLE backlog or issue labels,
is the source of active occupancy. A crash or abandoned worker expires safely;
a returned result still requires normal issue-bound RESULT/1 and adjudication.

**Admission boundaries:** This is not a guarantee that independent workers
have obeyed the START requirement. Universal production enforcement also
requires each direct Editorial intake/projector and bootstrap to check for
the fresh grant before admitting new worker results, while preserving
historical pre-cutover valid returns. Neither the existence of register #1096
nor unit-test PASS establishes live nine-request saturation, a real positive
Editorial worker pickup, or worker-result intake; those are separate #1049
acceptance gates. No GitHub account multiplicity is required. Slots count
distinct role/run instances without treating shared actor as an independent
reviewer. No mathematical certification, protected merge or publication
authority arises from a grant.
