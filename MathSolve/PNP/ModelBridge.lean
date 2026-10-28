import MathSolve.PNP.ProgrammeMachine
import MathSolve.PNP.SimulationOverhead
import Mathlib.Computability.TuringMachine.Computable

/-!
# PNP machine-model bridge contract

This file states the exact quantitative compiler contracts for
`PNP-BRIDGE-MODEL-001` and proves the class consequence that follows once both
concrete compilers are constructed.

The imported side is replayed against the current mathlib spelling of the same
`FinTM2`/`TM2ComputableInPolyTime` interface used by the pinned Formal
Conjectures dependency.  The input encoder is the identity on `List Bool` and
the output encoder is the canonical one-bit Boolean encoding.

This file does not assert that either compiler exists.  The two construction
theorems remain the substantive obligations of the model bridge.
-/

namespace MathSolve.PNP

/-- Current-mathlib spelling of the imported finite-TM2 polynomial-time witness. -/
abbrev ImportedTM2Witness (decision : List Bool → Bool) :=
  Turing.TM2ComputableInPolyTime (fun input : List Bool => input)
    Computability.encodeBool decision

/-- Imported finite-TM2 polynomial-time class presentation for one decision problem. -/
def ImportedTM2ComputableInPolyTime (decision : List Bool → Bool) : Prop :=
  Nonempty (ImportedTM2Witness decision)

/-- Exact runtime cost induced by an imported TM2 polynomial-time witness. -/
def importedTM2Runtime {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) : BinaryRuntimeCost :=
  fun input => source.time.eval input.length

/-- Every imported TM2 witness carries a Programme-polynomial runtime majorant. -/
theorem importedTM2Runtime_programmePolynomialBound
    {decision : List Bool → Bool} (source : ImportedTM2Witness decision) :
    ProgrammePolynomialBound (importedTM2Runtime source) := by
  apply importedPolynomialBound_to_programmePolynomialBound
  exact ⟨source.time, fun _ => le_rfl⟩

/--
Quantitative imported-TM2 to Programme compiler contract.

The target is a total Programme decider for the same Boolean function, and its
runtime must be affine in exact input length and the source TM2 step bound.
-/
def TM2ToProgrammeCompiler : Prop :=
  ∀ {decision : List Bool → Bool} (source : ImportedTM2Witness decision),
    ∃ target : ProgrammeDecider decision,
      AffineSimulationOverhead (importedTM2Runtime source) target.runtime

/--
An imported finite-TM2 decider with an exact, input-dependent runtime budget.

This is the correct target of a machine-level Programme simulation: the
translated execution cost may depend on the full input, while polynomialization
belongs to the later class-transfer step.
-/
structure ImportedTM2TimedDecider (decision : List Bool → Bool) extends
    Turing.TM2ComputableAux Bool Bool where
  runtime : BinaryRuntimeCost
  outputsFun :
    ∀ input : List Bool,
      Turing.TM2OutputsInTime tm
        (List.map inputAlphabet.invFun input)
        (Option.some
          ((List.map outputAlphabet.invFun)
            (Computability.encodeBool (decision input))))
        (runtime input)

/-- A Programme-polynomial timed TM2 decider can be bundled into the pinned
imported `Polynomial Nat` witness without changing its machine. -/
noncomputable def ImportedTM2TimedDecider.toImportedPoly
    {decision : List Bool → Bool}
    (target : ImportedTM2TimedDecider decision)
    (hpoly : ProgrammePolynomialBound target.runtime) :
    ImportedTM2Witness decision := by
  let hbound : ImportedPolynomialBound target.runtime :=
    programmePolynomialBound_to_importedPolynomialBound hpoly
  let p : Polynomial Nat := Classical.choose hbound
  have hp : ∀ input, target.runtime input ≤ p.eval input.length :=
    Classical.choose_spec hbound
  refine
    { tm := target.tm
      inputAlphabet := target.inputAlphabet
      outputAlphabet := target.outputAlphabet
      time := p
      outputsFun := ?_ }
  intro input
  have hrun := target.outputsFun input
  exact
    { steps := hrun.steps
      evals_in_steps := hrun.evals_in_steps
      steps_le_m := hrun.steps_le_m.trans (hp input) }

/--
Quantitative Programme-to-TM2 compiler contract.

The compiler emits an exact timed TM2 execution whose runtime is affine in the
Programme runtime.  It does not assume the source runtime is polynomial.
Polynomialization is performed only by `programme_to_tm2_class_transfer`, where
the Programme class hypothesis supplies that premise.
-/
def ProgrammeToTM2Compiler : Prop :=
  ∀ {decision : List Bool → Bool} (source : ProgrammeDecider decision),
    ∃ target : ImportedTM2TimedDecider decision,
      AffineSimulationOverhead source.runtime target.runtime

/-- The forward compiler implies imported-TM2 polynomial time is Programme polynomial time. -/
theorem tm2_to_programme_class_transfer
    (compiler : TM2ToProgrammeCompiler) {decision : List Bool → Bool}
    (h : ImportedTM2ComputableInPolyTime decision) :
    ProgrammeComputableInPolyTime decision := by
  rcases h with ⟨source⟩
  rcases compiler source with ⟨target, hoverhead⟩
  exact ⟨target,
    affineSimulationOverhead_preserves_programmePolynomialBound
      (importedTM2Runtime_programmePolynomialBound source) hoverhead⟩

/-- The reverse compiler implies Programme polynomial time is imported-TM2 polynomial time. -/
theorem programme_to_tm2_class_transfer
    (compiler : ProgrammeToTM2Compiler) {decision : List Bool → Bool}
    (h : ProgrammeComputableInPolyTime decision) :
    ImportedTM2ComputableInPolyTime decision := by
  rcases h with ⟨source, hsource⟩
  rcases compiler source with ⟨target, hoverhead⟩
  have htarget : ProgrammePolynomialBound target.runtime :=
    affineSimulationOverhead_preserves_programmePolynomialBound
      hsource hoverhead
  exact ⟨target.toImportedPoly htarget⟩

/-- Both quantitative compilers yield exact class-extensional equivalence. -/
theorem importedTM2_iff_programmePolyTime
    (forward : TM2ToProgrammeCompiler) (reverse : ProgrammeToTM2Compiler)
    (decision : List Bool → Bool) :
    ImportedTM2ComputableInPolyTime decision ↔
      ProgrammeComputableInPolyTime decision :=
  ⟨tm2_to_programme_class_transfer forward,
    programme_to_tm2_class_transfer reverse⟩

#print axioms importedTM2Runtime_programmePolynomialBound
#print axioms ImportedTM2TimedDecider.toImportedPoly
#print axioms tm2_to_programme_class_transfer
#print axioms programme_to_tm2_class_transfer
#print axioms importedTM2_iff_programmePolyTime

end MathSolve.PNP
