# H1-02 falsification ledger

| ID | Candidate shortcut | Disposition |
| --- | --- | --- |
| FC-F001 | Three pairwise-intersecting lines form a counted triangle. | FALSE: a fourth line can cross the open interior. |
| FC-F002 | Three distinct pairwise intersection points are sufficient. | FALSE: the same subdivided-triangle counterexample applies. |
| FC-F003 | Any line through a triangle vertex destroys the face. | FALSE: for x=0, y=0, x+y=2, the line x+y=0 touches only (0,0) and stays out of the open interior. |
| FC-F004 | Concurrency can be treated as an ordinary triangle. | FALSE: the pairwise intersections collapse and area is zero. |
| FC-F005 | Consecutive pairwise intersections on all three support lines are sufficient. | SURVIVES PROOF: this is the arrangement-edge criterion in `FACE_CRITERION.md`; executable falsification uses an independent direct-interior oracle. |

Random/property testing is a defect screen, not the primary proof.
