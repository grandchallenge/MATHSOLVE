import MathSolve.PNP.ProgrammeTM2RunInvariant

/-!
# Quantitative transfer of complete Programme runs to the reverse FinTM2

One Programme transition is one counted reverse-TM2 step.  This file composes
that local fact over an arbitrary bounded source run while carrying the exact
representation and stack-growth invariant.
-/

namespace MathSolve.PNP

noncomputable section

/-- Exact source iteration composes the strengthened reverse relation one step
for one step. -/
theorem programmeTM2_bounded_iterate
    (M : ProgrammeMachine) (input : List Bool) :
    ∀ (count : Nat)
      (source source' : ProgrammeConfig M)
      (target : (programmeTM2Machine M).Cfg)
      (spent : Nat),
      ProgrammeTM2BoundedRepresents M input source target spent →
      ((flip bind (M.step input))^[count]) (some source) = some source' →
      ∃ target',
        ProgrammeTM2BoundedRepresents M input source' target' (spent + count) ∧
        Nonempty
          (StateTransition.EvalsToInTime
            (programmeTM2Machine M).step
            target (some target') count) := by
  intro count
  induction count with
  | zero =>
      intro source source' target spent hrep hiter
      simp only [Function.iterate_zero_apply] at hiter
      cases Option.some.inj hiter
      exact ⟨target, by simpa using hrep,
        ⟨StateTransition.EvalsToInTime.refl
          (programmeTM2Machine M).step target⟩⟩
  | succ count ih =>
      intro source source' target spent hrep hiter
      rw [Function.iterate_succ_apply'] at hiter
      generalize hmid :
        ((flip bind (M.step input))^[count]) (some source) = mid at hiter
      cases mid with
      | none =>
          simp [flip] at hiter
      | some middle =>
          have hlast : M.step input middle = some source' := by
            simpa using hiter
          rcases ih source middle target spent hrep hmid with
            ⟨targetMiddle, hmiddle, ⟨hrun⟩⟩
          rcases programmeTM2_bounded_step hmiddle hlast with
            ⟨targetFinal, hfinalRaw, htargetStep⟩
          have hfinal :
              ProgrammeTM2BoundedRepresents M input source' targetFinal
                (spent + Nat.succ count) := by
            simpa [Nat.add_assoc, Nat.add_comm, Nat.add_left_comm] using hfinalRaw
          have hone := programmeTM2_one_step_in_time htargetStep
          refine ⟨targetFinal, hfinal, ⟨?_⟩⟩
          simpa [Nat.add_comm, Nat.add_left_comm, Nat.add_assoc] using
            StateTransition.EvalsToInTime.trans
              (programmeTM2Machine M).step
              count 1 target targetMiddle (some targetFinal)
              hrun hone

/-- Transfer one proof-carrying Programme run from the native Programme init
to the represented reverse-TM2 run state. -/
theorem programmeTM2_transfer_run
    (M : ProgrammeMachine) (input : List Bool)
    {terminal : ProgrammeConfig M} {bound : Nat}
    (run :
      StateTransition.EvalsToInTime
        (M.step input) (M.init input) (some terminal) bound) :
    ∃ target,
      ProgrammeTM2BoundedRepresents M input terminal target run.steps ∧
      Nonempty
        (StateTransition.EvalsToInTime
          (programmeTM2Machine M).step
          (programmeTM2ReadyInitCfg M input)
          (some target) run.steps) := by
  have hready := programmeTM2ReadyInitCfg_bounded M input
  rcases programmeTM2_bounded_iterate M input
      run.steps (M.init input) terminal
      (programmeTM2ReadyInitCfg M input) 0
      hready run.evals_in_steps with
    ⟨target, htarget, hrun⟩
  exact ⟨target, by simpa using htarget, hrun⟩

/-- A Programme configuration with no successor is one of the two terminals. -/
theorem programmeTerminal_of_step_none
    (M : ProgrammeMachine) (input : List Bool)
    (cfg : ProgrammeConfig M)
    (hnone : M.step input cfg = none) :
    cfg.state = M.accept ∨ cfg.state = M.reject := by
  by_cases haccept : cfg.state = M.accept
  · exact Or.inl haccept
  by_cases hreject : cfg.state = M.reject
  · exact Or.inr hreject
  have hsome :=
    M.step_eq_some_afterAction input cfg haccept hreject
  rw [hsome] at hnone
  contradiction

/-- A represented reverse state sees the same terminal Boolean as the Programme
output convention. -/
theorem programmeTM2_terminalResult_eq
    {M : ProgrammeMachine} {input : List Bool}
    {source : ProgrammeConfig M} {target : (programmeTM2Machine M).Cfg}
    (hrep : ProgrammeTM2Represents M input source target)
    (result : Bool)
    (hout : M.output source = some result) :
    programmeTM2TerminalResult M target.var = result := by
  have hcontrol : target.var.control = source.state := hrep.2.2.1
  unfold programmeTM2TerminalResult
  rw [hcontrol]
  by_cases haccept : source.state = M.accept
  · have hout' : some true = some result := by
      simpa [ProgrammeMachine.output, haccept] using hout
    have hresult : result = true := (Option.some.inj hout').symm
    subst result
    simp [haccept]
  · have hreject : source.state = M.reject := by
      by_contra hne
      have houtNone : M.output source = none := by
        simp [ProgrammeMachine.output, haccept, hne]
      rw [houtNone] at hout
      contradiction
    have hreject_ne_accept : M.reject ≠ M.accept := Ne.symm M.accept_ne_reject
    have hout' : some false = some result := by
      simpa [ProgrammeMachine.output, haccept, hreject, hreject_ne_accept] using hout
    have hresult : result = false := (Option.some.inj hout').symm
    subst result
    simp [haccept]

#print axioms programmeTM2_bounded_iterate
#print axioms programmeTM2_transfer_run
#print axioms programmeTerminal_of_step_none
#print axioms programmeTM2_terminalResult_eq

end

end MathSolve.PNP
