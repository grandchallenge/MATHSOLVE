# Trust boundary

## Fixed components inherited from M0

The following are assumptions of the M1 theorem surface and are not candidates for replacement by the step they validate:

- certificate-checker semantics;
- evaluator/interpreter semantics used by the checker;
- admission policy;
- artifact/content identity rules;
- evaluation-context and metric binding;
- checker resource limits.

## Required theorem visibility

The one-step theorem must name, rather than hide, the assumptions that connect a certificate/checker decision to semantic preservation. At minimum:

- checker soundness for the admitted certificate language;
- certificate binding to the exact candidate artifact;
- fixed evaluation context and metric identity;
- validity of the declared refinement witness;
- fixed resource policy.

## Forbidden strengthening

M1 does not prove:

- that the checker proves its own soundness;
- that all semantic equivalence is decidable;
- that all improvements can be discovered;
- that the trust kernel can replace itself through the same gate;
- that bounded one-step preservation implies unbounded intelligence growth.

## Exact M0 binding

Upstream formal-object SHA-256:

`1fca7a5e5bba2f4b59ccf9288a6a01129652091f86071c7be70022ea076d0edc`

Any material theorem-target change requires a new upstream digest and review before this package proceeds.
