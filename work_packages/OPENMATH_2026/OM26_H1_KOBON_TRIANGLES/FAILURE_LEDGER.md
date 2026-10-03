# OM26-H1 failure ledger

| ID | Failure mode | Disposition / response |
| --- | --- | --- |
| H1-F001 | count a 3-cycle that is not an arrangement face | scorer bug; construct exact counterexample and stop promotion |
| H1-F002 | count a triangle crossed or subdivided by another line | scorer bug; reject candidate/result |
| H1-F003 | floating-point predicate changes incidence/order | prohibited for final score; replay in exact rational arithmetic |
| H1-F004 | proportional line triples slip through as distinct lines | invalid submission; canonicalize/reject |
| H1-F005 | continuous search improves a surrogate but rationalization loses score | record as route failure, do not report surrogate score |
| H1-F006 | high-scoring pseudoline arrangement is non-stretchable | useful negative result, not a candidate |
| H1-F007 | compare scores from different n | invalid comparison |
| H1-F008 | call campaign leader “best known” without literature audit | claim inflation; use `campaign-best-observed` |
| H1-F009 | infer optimality from score improvement | prohibited; requires independent upper-bound proof |
| H1-F010 | source/evaluator rules drift before submission | reopen Forge lock and replay surviving candidates |
| H1-F011 | external model/CAS/search output enters route without provenance | quarantine until evidence/receipt is preserved |
| H1-F012 | CEI result self-promotes on intake | prohibited; preserve raw result then adjudicate separately |

Dead routes remain evidence. A route may terminate with a precise obstruction rather than be kept alive for optics.
