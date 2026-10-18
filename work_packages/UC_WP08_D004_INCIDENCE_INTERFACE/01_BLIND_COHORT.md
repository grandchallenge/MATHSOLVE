# UC-WP08-D004 blind cohort

Cohort: `UC-WP08-D004-BLIND-COHORT-001`

Members: WP01, WP02, WP03, WP04.

The four assignments are intentionally independently executable. Their task
packets may overlap in definitions, but no member may consume another member's
return before cohort closure.

Closure condition: every member has one durably preserved valid RESULT/1, or a
protected reconciliation explicitly records which member did not return.
Only after closure may GCL synthesize the four results. A returned result is
evidence, not an admitted theorem.

WP05 is an adversarial lane outside the blind cohort and must likewise avoid
reading blind returns before integration.
