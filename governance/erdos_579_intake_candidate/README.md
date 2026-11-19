# Erdős #579 — governed intake candidate only

The source-locked replay evidence is already protected in MATHSOLVE merge `94d0bff64630b5592ae5d10e84b4d3eefa1860ee`. This directory is a **pre-registration draft**; it is intentionally excluded from active `campaign_manifests/`, `cert_handoffs/` and `contracts/programme_reference_registry.json`.

The current MATHSOLVE validator refuses to activate a new campaign while `contracts/mathcert_current_routes.json` lacks the corresponding protected MATHCERT route, and successor overlays require identical campaign sets. Accordingly `campaign_manifest.json` is **not** an executable manifest: references to the handoff awaiting a protected commit are marked unbound. `mathcert_handoff.json` likewise retains preparatory ledger commit identities that must be replaced with protected path+commit hashes before activation. Treat these files as blueprints only, never as admitted packets.

The `claim_ledger.json` distinguishes the proved negative statement at fixed density 3/2048 from claims not proved. `proof_obligation_dag.json` identifies outstanding non-author mathematical review, route admission and certificate readback. The historical MATHFORGE `ERDOS-OPEN-001` source lock must stay unmodified.

Activation sequence: (1) admit required claim-specific MATHCERT route and matching explicit reviewer provenance; (2) rebind candidate ledger/handoff identities on exact protected Solve commits; (3) atomically update Solve's route projection, programme campaign registry and applicable successor overlays; (4) run active manifest and Cert validators and protected admission; (5) independently adjudicate and only then produce a Level 5 MATHCERT certificate. Current candidate implies no certification.
