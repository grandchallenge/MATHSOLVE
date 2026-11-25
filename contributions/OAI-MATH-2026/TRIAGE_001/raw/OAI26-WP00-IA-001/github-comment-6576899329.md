GCL-CONTRIBUTION-RESULT/1
dispatch_id: OAI26-WP00-IA-001
agent_ref: GCL-INDEPENDENT-OAI26-WP00
assignment: GCL-OAI-26-WP00
disposition: SOURCE_INTERFACE_FOUND
context_class: ZERO_CONTEXT
external_sources: PRIMARY_SOURCES_REQUIRED
timebox_observed: NO

## Strongest exact statement
Independent deterministic inspection of three pinned MATHFORGE source-intake JSON objects at baseline 85c26cab0527045dd0305a878c8c563c87993375 establishes 372 distinct indexed family IDs, 719 manuscript links with 719 distinct PDF path strings, 173 indexed formalization source-paper rows, and 200 declaration/comparator records with 200 distinct declaration strings. All 200 records contain nonempty declaration, comparator_config and lean_source paths; their comparator paths number only 189 distinct strings, and their Lean paths 192 distinct strings, demonstrating legitimate many-to-one path reuse which must not be mistaken for missing declarations. The repository's “300 top-line results formalized” is publisher-reported, NOT a declaration cardinality; no 300-to-200 bijection is established.

An exact edition mismatch witness exists: source_papers references the September-23-2026 `Taming-implies-compatibility-on-four-manifolds` PDF, while indexed family 342 contains the October-6-2026 PDF. The crosswalk expressly records `REVISION_MISMATCH`, requiring statement-by-statement concordance. 172/173 source-paper path strings match manuscript-index PDF paths exactly; the September edition is the only unmatched string. This is not by itself a missing paper or proof. Family 337 contains two distinct indexed PDFs (Generalized-Cartan-Hadamard isoperimetry; Sharp integral fillings in CAT(0) spaces), so forcing one manuscript per family is incorrect.

## Derivation
Fetched and parsed at the frozen MATHFORGE commit: sources/OPENAI-MATH-2026/SOURCE_LOCK.json (Git blob e8732d71da4105aa88d63abaecfc74356853724c), MANUSCRIPT_INDEX.json (blob 7a0b00eb9bfdeb59b157a98ee6522fc685580152), FORMALIZATION_CROSSWALK.json (blob 5fc50adc9430a91f22f1c3913bdfec62fe75acda). Counted family_id uniqueness, flattened all families[*].manuscripts[*].pdf_path, compared each crosswalk source_papers[*].pdf_path against the exact path-keyed index, and separately counted distinct main_results[*].declaration, comparator_config and lean_source. The calculation was executed on complete fetched JSON objects, not a sample.

## Assumptions beyond bootstrap
Exact string-path equality is an indexing criterion, not proof of manuscript semantic equivalence. No upstream proof/Lean file contents were compiled. Work was limited to protected source-intake manifests; no sibling blind-cohort evidence was read.

## Verification / falsification hooks
Recompute counts by sorting family IDs and PDF path strings, checking uniqueness and joining crosswalk source_papers on exact pdf_path; expect 372, 719, 173, 200; 1 unmatched path (family 342 edition mismatch); 200 unique declaration strings; 189 distinct comparator paths; 192 distinct Lean paths; and zero records with missing three required declaration fields. Negative fixture: replace October-6 family 342 PDF path by September-23 edition and observe that exact-path unmatched count changes, but do not infer semantic concordance. The alternate family 337 two-paper shape must survive any normalization.

## Claim boundary
SOURCE_OR_FORMAL_EVIDENCE_ONLY. This is a genuine bounded source-interface and counting result, not completed WP00 full crosswalk, repository PR, Lean replay, manuscript theorem validation or certification. No 300↔200 reconciliation is claimed; current authoritative source leaves its denominator UNRECONCILED. No repository mutation is authorized or performed.

## Next residual
Implement and replay the full byte-stable 372-family/719-link/200-declaration mapping ledger including one-to-many edges and pinned upstream formalization.yaml; verify every comparator/Lean path at exact source commit, inspect family 337 path regression, withdrawn cases and family 342 theorem-edition concordance. Retain UNRECONCILED top-line 300 count until exact publisher accounting is obtained.