import MathSolve.PNP.TM2TokenDecode
import Mathlib.Data.Fintype.EquivFin

/-!
# Finite control carrier for the TM2-to-Programme compiler

This file fixes the finite administrative state used by the forward machine
simulation.  It deliberately contains no simulation claim yet.  The purpose is
to make the two finiteness obligations explicit before defining the transition
function:

* every source stack gets exactly one Programme work tape via the canonical
  finite equivalence with `Fin (card K)`;
* startup, rewind, statement execution, two-phase push, accept, and reject all
  live in one finite control carrier.
-/

namespace MathSolve.PNP

noncomputable section

/-- Number of Programme work tapes used by a fixed imported `FinTM2`. -/
def tm2WorkTapeCount {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) : Nat :=
  @Fintype.card source.tm.K source.tm.kFin

/-- Canonical bijection from source stack indices to Programme work-tape indices. -/
noncomputable def tm2TapeEquiv {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) :
    source.tm.K ≃ Fin (tm2WorkTapeCount source) := by
  letI : Fintype source.tm.K := source.tm.kFin
  exact Fintype.equivFin source.tm.K

/-- The work-tape assignment is injective and has a total inverse. -/
theorem tm2TapeEquiv_symm_apply {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (k : source.tm.K) :
    (tm2TapeEquiv source).symm (tm2TapeEquiv source k) = k := by
  exact (tm2TapeEquiv source).symm_apply_apply k

/--
Finite Programme-side control state for forward simulation.

The nested sum cases are, in order: copy input, rewind the copied input stack,
execute an accessible TM2 statement occurrence with the current source state,
complete the second half of a push, accept, reject.
-/
def TM2ProgrammeControl {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) :=
  Unit ⊕
    (Unit ⊕
      ((TM2StatementCode source.tm × source.tm.σ) ⊕
        ((TM2StatementCode source.tm × source.tm.σ × TM2ProvenanceToken source.tm) ⊕
          (Unit ⊕ Unit))))

noncomputable instance tm2ProgrammeControlFintype {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) : Fintype (TM2ProgrammeControl source) := by
  letI : Fintype source.tm.σ := source.tm.σFin
  unfold TM2ProgrammeControl
  infer_instance

noncomputable instance tm2ProgrammeControlDecidableEq {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) : DecidableEq (TM2ProgrammeControl source) :=
  Classical.decEq _

/-- Startup state: copy exact Boolean input into the source input-stack work tape. -/
def tm2ControlCopy {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) : TM2ProgrammeControl source :=
  Sum.inl ()

/-- Rewind state after the linear input copy. -/
def tm2ControlRewind {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) : TM2ProgrammeControl source :=
  Sum.inr (Sum.inl ())

/-- Execute one accessible statement occurrence at a fixed finite source state. -/
def tm2ControlRun {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (code : TM2StatementCode source.tm) (state : source.tm.σ) :
    TM2ProgrammeControl source :=
  Sum.inr (Sum.inr (Sum.inl (code, state)))

/-- Complete a two-transition push after moving into the new blank stack cell. -/
def tm2ControlPushWrite {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (nextCode : TM2StatementCode source.tm) (state : source.tm.σ)
    (token : TM2ProvenanceToken source.tm) : TM2ProgrammeControl source :=
  Sum.inr (Sum.inr (Sum.inr (Sum.inl (nextCode, state, token))))

/-- Programme accepting terminal state. -/
def tm2ControlAccept {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) : TM2ProgrammeControl source :=
  Sum.inr (Sum.inr (Sum.inr (Sum.inr (Sum.inl ()))))

/-- Programme rejecting terminal state. -/
def tm2ControlReject {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) : TM2ProgrammeControl source :=
  Sum.inr (Sum.inr (Sum.inr (Sum.inr (Sum.inr ()))))

/-- The two terminal control states are definitionally distinct. -/
theorem tm2ControlAccept_ne_reject {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) :
    tm2ControlAccept source ≠ tm2ControlReject source := by
  simp [tm2ControlAccept, tm2ControlReject]

/-- The first executable source statement has a canonical finite control code. -/
def tm2ControlInitialRun {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) : TM2ProgrammeControl source :=
  tm2ControlRun source (TM2StatementCode.root source.tm source.tm.main) source.tm.initialState

#print axioms tm2TapeEquiv_symm_apply
#print axioms tm2ControlAccept_ne_reject

end

end MathSolve.PNP
