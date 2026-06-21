# External Audit: kashiwabarakenji/frankl_lean

Audit date: 2026-06-19

Repository: https://github.com/kashiwabarakenji/frankl_lean

Pinned commit audited locally:

```text
cd1462f8bf38fddb5053dddbfb68017dd340e360
```

Pinned upstream toolchain:

```text
leanprover/lean4:v4.24.0
```

Upstream Lake surface at the audited commit:

- `mathlib` dependency: `v4.24.0`
- `LeanCopilot` dependency: `v4.24.0`
- Native link args include `.lake/packages/LeanCopilot/.lake/build/lib`
- Active `import LeanCopilot` occurs in:
  - `IdealFamily/Core.lean`
  - `IdealFamily/Corollaries.lean`
  - `IdealFamily/ViaRare.lean`
  - `IdealFamily/FranklRare.lean`

## Unmodified Build Attempt

Commands attempted from `MATHSOLVE/external_audits/frankl_lean/upstream`:

```powershell
lake update
lake build
```

Observed result:

- Initial sandboxed `lake update` could not access GitHub.
- Escalated `lake update` ran for 10 minutes and timed out after partially fetching dependencies.
- `lake build` did not reach Lean proof checking. It failed while resolving `LeanCopilot`:

```text
info: LeanCopilot: URL has changed; you might need to delete '.lake/packages/LeanCopilot' manually
error: external command 'git' exited with code 128
```

Conclusion: no unmodified upstream build certificate was obtained in this environment.

## Modified No-LeanCopilot Build Attempt

A clean audit copy was created at:

```text
MATHSOLVE/external_audits/frankl_lean/modified_no_leancopilot
```

Local audit-only modifications:

- Removed the `LeanCopilot` `[[require]]` block from `lakefile.toml`.
- Removed the LeanCopilot native link args from `lakefile.toml`.
- Removed active `import LeanCopilot` lines from the four `IdealFamily/*.lean` files that imported it.

Commands attempted:

```powershell
lake update
lake build
```

Observed result:

- Escalated `lake update` again timed out after 10 minutes.
- `lake build` failed before proof checking because the manifest/package state was stale:

```text
warning: manifest out of date: git revision of dependency 'mathlib' changed; use `lake update mathlib` to update it
info: mathlib: URL has changed; you might need to delete '.lake/packages/mathlib' manually
error: external command 'git' exited with code 128
```

Conclusion: the modified no-Copilot build is an audit workaround attempt only, not an upstream build certificate.

## Source-Surface Finding

The audited upstream source contains active proof placeholders in the advertised NDS/average-rarity path:

```text
IdealFamily/ViaRare.lean: sorry
IdealFamily/ViaRare.lean: sorry
IdealFamily/ViaRare.lean: sorry
```

The local search also found a textual `--sorry--` comment in `IdealFamily/NDSDiff.lean`; that comment is not an active Lean proof placeholder, but it confirms the source needs human audit before promotion.

## Local Port Decision

MATHCERT does not import the upstream repository as a Lake dependency because the audited upstream is pinned to Lean `v4.24.0`, while MATHCERT is pinned to Lean/mathlib `v4.29.1`.

The local MATHCERT port includes only checked material:

- `MathCert/Domains/UnionClosed/IdealFamilyPort/Core.lean`
- `MathCert/Domains/UnionClosed/IdealFamilyPort/FranklRare.lean`
- `MathCert/Domains/UnionClosed/IdealFamilyPort.lean`
- `MathCert/Domains/UnionClosed/IdealFamilyBridge.lean`

The unconditional average-rarity bridge

```lean
localIdealFamily_averageRare :
  IsIdealFamilyOn F U -> IsAverageRareOn F U
```

is not promoted. The checked bridge currently proves the conditional translation from a ported NDS theorem:

```lean
localIdealFamily_averageRare_of_port_nds
```

and the checked rare-vertex bridge:

```lean
localIdealFamily_exists_rare
```

Promotion condition for the unconditional average-rarity theorem: obtain a placeholder-free upstream proof of `nds <= 0`, or complete an independent local proof in MATHCERT, then instantiate `localIdealFamily_averageRare_of_port_nds`.
