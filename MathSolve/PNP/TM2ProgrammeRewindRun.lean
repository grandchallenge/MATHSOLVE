import MathSolve.PNP.TM2ProgrammeStartupRun

/-!
# Exact rewind execution for the forward TM2 compiler

After copying the input, the compiler moves both the immutable input head and
the represented source-input-stack work head left in lockstep.  This file gives
a closed form for that phase and proves the exact linear transition count.
-/

namespace MathSolve.PNP

noncomputable section

/-- Head coordinate when exactly `remaining` input cells still need to be
crossed during rewind. -/
def tm2ProgrammeRewindHead : Nat → Int
  | 0 => -1
  | n + 1 => n

/-- Closed form for the Programme rewind phase. -/
def tm2ProgrammeRewindConfig {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool)
    (remaining : Nat) :
    ProgrammeConfig (tm2ProgrammeMachine source) where
  state := tm2ControlRewind source
  inputHead := tm2ProgrammeRewindHead remaining
  workHead := fun tape =>
    if tape = tm2TapeEquiv source source.tm.k₀
    then tm2ProgrammeRewindHead remaining
    else 0
  work := tm2ProgrammeReadyWork source input

/-- The blank transition leaving copy mode enters the closed-form rewind state
with every input bit still to be crossed. -/
theorem tm2ProgrammeCopyConfig_after_done {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool) :
    (tm2ProgrammeCopyConfig source input).afterAction
        (tm2CopyDoneAction source
          (tm2ProgrammeCopyConfig source input).readWork) =
      tm2ProgrammeRewindConfig source input input.length := by
  ext tape position <;>
    simp [tm2ProgrammeCopyConfig, tm2ProgrammeRewindConfig,
      tm2ProgrammeRewindHead, ProgrammeConfig.afterAction,
      tm2CopyDoneAction, tm2PreserveWork, tm2MoveSelected,
      ProgrammeConfig.readWork, HeadMove.apply, Function.update_eq_self]
  by_cases htape : tape = tm2TapeEquiv source source.tm.k₀
  · subst tape
    simp [tm2ProgrammeCopyConfig, tm2ProgrammeRewindConfig,
      tm2ProgrammeRewindHead, ProgrammeConfig.afterAction,
      tm2CopyDoneAction, tm2PreserveWork, tm2MoveSelected,
      ProgrammeConfig.readWork, HeadMove.apply, Function.update_eq_self]
  · simp [tm2ProgrammeCopyConfig, tm2ProgrammeRewindConfig,
      tm2ProgrammeRewindHead, ProgrammeConfig.afterAction,
      tm2CopyDoneAction, tm2PreserveWork, tm2MoveSelected,
      ProgrammeConfig.readWork, HeadMove.apply, htape,
      Function.update_eq_self]

/-- One rewind-bit action decrements the closed-form remaining-cell count. -/
theorem tm2ProgrammeRewindConfig_after_bit {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool)
    (remaining : Nat) :
    (tm2ProgrammeRewindConfig source input (remaining + 1)).afterAction
        (tm2RewindBitAction source
          (tm2ProgrammeRewindConfig source input (remaining + 1)).readWork) =
      tm2ProgrammeRewindConfig source input remaining := by
  cases remaining with
  | zero =>
      ext tape position <;>
        simp [tm2ProgrammeRewindConfig, tm2ProgrammeRewindHead,
          ProgrammeConfig.afterAction, tm2RewindBitAction,
          tm2PreserveWork, tm2MoveSelected, ProgrammeConfig.readWork,
          HeadMove.apply, Function.update_eq_self]
      by_cases htape : tape = tm2TapeEquiv source source.tm.k₀
      · subst tape
        simp [tm2ProgrammeRewindConfig, tm2ProgrammeRewindHead,
          ProgrammeConfig.afterAction, tm2RewindBitAction,
          tm2PreserveWork, tm2MoveSelected, ProgrammeConfig.readWork,
          HeadMove.apply, Function.update_eq_self]
      · simp [tm2ProgrammeRewindConfig, tm2ProgrammeRewindHead,
          ProgrammeConfig.afterAction, tm2RewindBitAction,
          tm2PreserveWork, tm2MoveSelected, ProgrammeConfig.readWork,
          HeadMove.apply, htape, Function.update_eq_self]
  | succ n =>
      ext tape position <;>
        simp [tm2ProgrammeRewindConfig, tm2ProgrammeRewindHead,
          ProgrammeConfig.afterAction, tm2RewindBitAction,
          tm2PreserveWork, tm2MoveSelected, ProgrammeConfig.readWork,
          HeadMove.apply, Function.update_eq_self]
      by_cases htape : tape = tm2TapeEquiv source source.tm.k₀
      · subst tape
        simp [tm2ProgrammeRewindConfig, tm2ProgrammeRewindHead,
          ProgrammeConfig.afterAction, tm2RewindBitAction,
          tm2PreserveWork, tm2MoveSelected, ProgrammeConfig.readWork,
          HeadMove.apply, Function.update_eq_self]
      · simp [tm2ProgrammeRewindConfig, tm2ProgrammeRewindHead,
          ProgrammeConfig.afterAction, tm2RewindBitAction,
          tm2PreserveWork, tm2MoveSelected, ProgrammeConfig.readWork,
          HeadMove.apply, htape, Function.update_eq_self]

/-- At rewind count `n+1`, the immutable input head scans exact input index
`n`. -/
theorem programmeInputRead_rewind_succ
    (input : List Bool) (n : Nat) (hn : n < input.length) :
    programmeInputRead input (tm2ProgrammeRewindHead (n + 1)) =
      some (input[n]'hn) := by
  simp [tm2ProgrammeRewindHead, programmeInputRead, hn]

/-- Rewind count zero is exactly the blank cell immediately left of input. -/
theorem programmeInputRead_rewind_zero (input : List Bool) :
    programmeInputRead input (tm2ProgrammeRewindHead 0) = none := by
  simp [tm2ProgrammeRewindHead, programmeInputRead]

/-- The final rewind blank transition restores both relevant heads to zero and
enters the exact ready configuration representing `FinTM2.initList`. -/
theorem tm2ProgrammeRewindConfig_after_done {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool) :
    (tm2ProgrammeRewindConfig source input 0).afterAction
        (tm2RewindDoneAction source
          (tm2ProgrammeRewindConfig source input 0).readWork) =
      tm2ProgrammeReadyConfig source input := by
  ext tape position <;>
    simp [tm2ProgrammeRewindConfig, tm2ProgrammeRewindHead,
      tm2ProgrammeReadyConfig, ProgrammeConfig.afterAction,
      tm2RewindDoneAction, tm2PreserveWork, tm2MoveSelected,
      ProgrammeConfig.readWork, HeadMove.apply, Function.update_eq_self]
  by_cases htape : tape = tm2TapeEquiv source source.tm.k₀
  · subst tape
    simp [tm2ProgrammeRewindConfig, tm2ProgrammeRewindHead,
      tm2ProgrammeReadyConfig, ProgrammeConfig.afterAction,
      tm2RewindDoneAction, tm2PreserveWork, tm2MoveSelected,
      ProgrammeConfig.readWork, HeadMove.apply, Function.update_eq_self]
  · simp [tm2ProgrammeRewindConfig, tm2ProgrammeRewindHead,
      tm2ProgrammeReadyConfig, ProgrammeConfig.afterAction,
      tm2RewindDoneAction, tm2PreserveWork, tm2MoveSelected,
      ProgrammeConfig.readWork, HeadMove.apply, htape,
      Function.update_eq_self]

/-- Starting at rewind count `remaining`, exactly `remaining` transitions
cross those input cells and reach the blank-left rewind configuration. -/
theorem tm2Programme_rewind_run_aux {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool) :
    ∀ remaining : Nat,
      remaining ≤ input.length →
      Nonempty
        (StateTransition.EvalsToInTime
          ((tm2ProgrammeMachine source).step input)
          (tm2ProgrammeRewindConfig source input remaining)
          (some (tm2ProgrammeRewindConfig source input 0))
          remaining) := by
  intro remaining hle
  induction remaining with
  | zero =>
      exact ⟨StateTransition.EvalsToInTime.refl
        ((tm2ProgrammeMachine source).step input)
        (tm2ProgrammeRewindConfig source input 0)⟩
  | succ n ih =>
      have hn : n < input.length := by omega
      let bit := input[n]'hn
      have hread :
          programmeInputRead input
              (tm2ProgrammeRewindConfig source input (n + 1)).inputHead =
            some bit := by
        simpa [tm2ProgrammeRewindConfig, bit] using
          programmeInputRead_rewind_succ input n hn
      have hstepRaw :=
        tm2ProgrammeMachine_step_rewind_some source input
          (tm2ProgrammeRewindConfig source input (n + 1))
          bit rfl hread
      have hstep :
          (tm2ProgrammeMachine source).step input
              (tm2ProgrammeRewindConfig source input (n + 1)) =
            some (tm2ProgrammeRewindConfig source input n) := by
        rw [tm2ProgrammeRewindConfig_after_bit] at hstepRaw
        exact hstepRaw
      rcases ih (by omega) with ⟨hrest⟩
      have hone := programme_one_step_in_time hstep
      refine ⟨?_⟩
      simpa using
        StateTransition.EvalsToInTime.trans
          ((tm2ProgrammeMachine source).step input)
          1 n
          (tm2ProgrammeRewindConfig source input (n + 1))
          (tm2ProgrammeRewindConfig source input n)
          (some (tm2ProgrammeRewindConfig source input 0))
          hone hrest

/-- The exact copied configuration reaches the ready root configuration in
`input.length + 2` further transitions: one copy-completion step, the rewind
scan, and one rewind-completion step. -/
theorem tm2Programme_rewind_from_copy {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool) :
    Nonempty
      (StateTransition.EvalsToInTime
        ((tm2ProgrammeMachine source).step input)
        (tm2ProgrammeCopyConfig source input)
        (some (tm2ProgrammeReadyConfig source input))
        (input.length + 2)) := by
  have hcopyRead :
      programmeInputRead input
        (tm2ProgrammeCopyConfig source input).inputHead = none := by
    simp [tm2ProgrammeCopyConfig, programmeInputRead]
  have hdoneRaw :=
    tm2ProgrammeMachine_step_copy_none source input
      (tm2ProgrammeCopyConfig source input) rfl hcopyRead
  have hdone :
      (tm2ProgrammeMachine source).step input
          (tm2ProgrammeCopyConfig source input) =
        some (tm2ProgrammeRewindConfig source input input.length) := by
    rw [tm2ProgrammeCopyConfig_after_done] at hdoneRaw
    exact hdoneRaw
  rcases tm2Programme_rewind_run_aux source input input.length le_rfl with
    ⟨hrewind⟩
  have hblank :
      programmeInputRead input
        (tm2ProgrammeRewindConfig source input 0).inputHead = none := by
    simpa [tm2ProgrammeRewindConfig] using
      programmeInputRead_rewind_zero input
  have hlastRaw :=
    tm2ProgrammeMachine_step_rewind_none source input
      (tm2ProgrammeRewindConfig source input 0) rfl hblank
  have hlast :
      (tm2ProgrammeMachine source).step input
          (tm2ProgrammeRewindConfig source input 0) =
        some (tm2ProgrammeReadyConfig source input) := by
    rw [tm2ProgrammeRewindConfig_after_done] at hlastRaw
    exact hlastRaw
  have hone := programme_one_step_in_time hdone
  have hlastOne := programme_one_step_in_time hlast
  have hprefix :=
    StateTransition.EvalsToInTime.trans
      ((tm2ProgrammeMachine source).step input)
      1 input.length
      (tm2ProgrammeCopyConfig source input)
      (tm2ProgrammeRewindConfig source input input.length)
      (some (tm2ProgrammeRewindConfig source input 0))
      hone hrewind
  refine ⟨?_⟩
  have htotal :=
    StateTransition.EvalsToInTime.trans
      ((tm2ProgrammeMachine source).step input)
      (input.length + 1) 1
      (tm2ProgrammeCopyConfig source input)
      (tm2ProgrammeRewindConfig source input 0)
      (some (tm2ProgrammeReadyConfig source input))
      (by simpa [Nat.add_comm, Nat.add_left_comm, Nat.add_assoc] using hprefix)
      hlastOne
  simpa [Nat.add_comm, Nat.add_left_comm, Nat.add_assoc] using htotal

/-- Native Programme initialization reaches the exact represented TM2
`initList` configuration in precisely `2 * input.length + 2` transitions. -/
theorem tm2Programme_startup_run {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool) :
    Nonempty
      (StateTransition.EvalsToInTime
        ((tm2ProgrammeMachine source).step input)
        ((tm2ProgrammeMachine source).init input)
        (some (tm2ProgrammeReadyConfig source input))
        (2 * input.length + 2)) := by
  rcases tm2Programme_copy_run source input with ⟨hcopy⟩
  rcases tm2Programme_rewind_from_copy source input with ⟨hrewind⟩
  refine ⟨?_⟩
  have hrun :=
    StateTransition.EvalsToInTime.trans
      ((tm2ProgrammeMachine source).step input)
      input.length (input.length + 2)
      ((tm2ProgrammeMachine source).init input)
      (tm2ProgrammeCopyConfig source input)
      (some (tm2ProgrammeReadyConfig source input))
      hcopy hrewind
  simpa [Nat.mul_comm, Nat.add_comm, Nat.add_left_comm, Nat.add_assoc] using hrun

#print axioms tm2ProgrammeCopyConfig_after_done
#print axioms tm2ProgrammeRewindConfig_after_bit
#print axioms programmeInputRead_rewind_succ
#print axioms tm2ProgrammeRewindConfig_after_done
#print axioms tm2Programme_rewind_run_aux
#print axioms tm2Programme_rewind_from_copy
#print axioms tm2Programme_startup_run

end

end MathSolve.PNP
