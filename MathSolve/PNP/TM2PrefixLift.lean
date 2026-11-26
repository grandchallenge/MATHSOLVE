import MathSolve.PNP.NPVerifierBridge

/-!
# Exact statement lifting for a finite-stack input adapter

The original machine runs on its original stacks and state. Added stacks and
auxiliary state belong to the input adapter. In run mode, the lifted statement
must simulate the original interpreter exactly, leaving every added stack and
the auxiliary state unchanged. Prefix initialization is a separate obligation.
-/
namespace MathSolve.PNP
namespace TM2PrefixLift
open Turing

variable {K E Λ μ σ δ : Type} {Γ : K → Type} {Δ : E → Type}

/-- Original and adapter stack alphabets are disjoint. -/
def alphabet (Γ : K → Type) (Δ : E → Type) : K ⊕ E → Type
  | .inl k => Γ k
  | .inr e => Δ e

abbrev StackFamily (Γ : K → Type) := ∀ k, List (Γ k)

def liftStacks (S : StackFamily Γ) (X : StackFamily Δ) :
    StackFamily (alphabet Γ Δ)
  | .inl k => S k
  | .inr e => X e

def cfg (c : TM2.Cfg Γ Λ σ) (X : StackFamily Δ) (d : δ) :
    TM2.Cfg (alphabet Γ Δ) (Λ ⊕ μ) (σ × δ) :=
  ⟨c.l.map Sum.inl, (c.var,d), liftStacks c.stk X⟩

def stmt : TM2.Stmt Γ Λ σ → TM2.Stmt (alphabet Γ Δ) (Λ ⊕ μ) (σ × δ)
  | .push k f q => .push (.inl k) (fun v => f v.1) (stmt q)
  | .peek k f q => .peek (.inl k) (fun v a => (f v.1 a,v.2)) (stmt q)
  | .pop k f q => .pop (.inl k) (fun v a => (f v.1 a,v.2)) (stmt q)
  | .load f q => .load (fun v => (f v.1,v.2)) (stmt q)
  | .branch f q r => .branch (fun v => f v.1) (stmt q) (stmt r)
  | .goto f => .goto (fun v => .inl (f v.1))
  | .halt => .halt

theorem stacks_update [DecidableEq K] [DecidableEq E]
    (S : StackFamily Γ) (X : StackFamily Δ) (k : K) (v : List (Γ k)) :
    Function.update (liftStacks S X) (.inl k) v =
      liftStacks (Function.update S k v) X := by
  funext j
  cases j with
  | inl j =>
    by_cases h : j = k
    · subst j
      simp [liftStacks]
    · have hn : (Sum.inl j : K ⊕ E) ≠ Sum.inl k := fun he => h (Sum.inl.inj he)
      rw [Function.update_of_ne hn]
      change S j = Function.update S k v j
      rw [Function.update_of_ne h]
  | inr e =>
    have hn : (Sum.inr e : K ⊕ E) ≠ Sum.inl k := by intro h; cases h
    rw [Function.update_of_ne hn]
    rfl

/-- Exact native execution of every lifted statement, including its continuation. -/
theorem stmt_stepAux [DecidableEq K] [DecidableEq E]
    (q : TM2.Stmt Γ Λ σ) (v : σ) (S : StackFamily Γ) (X : StackFamily Δ) (d : δ) :
    TM2.stepAux (stmt (μ := μ) (δ := δ) (Δ := Δ) q) (v,d) (liftStacks S X) =
      cfg (μ := μ) (TM2.stepAux q v S) X d := by
  induction q generalizing v S with
  | push k f q ih =>
    simp only [stmt, TM2.stepAux]
    rw [stacks_update]
    exact ih _ _
  | peek k f q ih =>
    simp only [stmt, TM2.stepAux]
    exact ih _ _
  | pop k f q ih =>
    simp only [stmt, TM2.stepAux]
    rw [stacks_update]
    exact ih _ _
  | load f q ih =>
    simp only [stmt, TM2.stepAux]
    exact ih _ _
  | branch f q r ihq ihr =>
    cases h : f v <;> simp [stmt, TM2.stepAux, h, ihq, ihr]
  | goto f => rfl
  | halt => rfl

def program (M : Λ → TM2.Stmt Γ Λ σ)
    (P : μ → TM2.Stmt (alphabet Γ Δ) (Λ ⊕ μ) (σ × δ)) :
    Λ ⊕ μ → TM2.Stmt (alphabet Γ Δ) (Λ ⊕ μ) (σ × δ)
  | .inl l => stmt (M l)
  | .inr p => P p

/-- The original machine's native outer step is unchanged in run mode. -/
theorem step [DecidableEq K] [DecidableEq E]
    (M : Λ → TM2.Stmt Γ Λ σ)
    (P : μ → TM2.Stmt (alphabet Γ Δ) (Λ ⊕ μ) (σ × δ))
    (c : TM2.Cfg Γ Λ σ) (X : StackFamily Δ) (d : δ) :
    TM2.step (program M P) (cfg c X d) =
      (TM2.step M c).map (fun c' => cfg c' X d) := by
  rcases c with ⟨l,v,S⟩
  cases l with
  | none => rfl
  | some l =>
    change some (TM2.stepAux (stmt (M l)) (v,d) (liftStacks S X)) =
      some (cfg (TM2.stepAux (M l) v S) X d)
    rw [stmt_stepAux]

#print axioms stacks_update
#print axioms stmt_stepAux
#print axioms step

/-- Option-valued form of the run-mode simulation, including absence of a next
configuration after halt. -/
theorem step_option [DecidableEq K] [DecidableEq E]
    (M : Λ → TM2.Stmt Γ Λ σ)
    (P : μ → TM2.Stmt (alphabet Γ Δ) (Λ ⊕ μ) (σ × δ))
    (c : Option (TM2.Cfg Γ Λ σ)) (X : StackFamily Δ) (d : δ) :
    (c.map (fun c' => cfg c' X d)).bind (TM2.step (program M P)) =
      (c.bind (TM2.step M)).map (fun c' => cfg c' X d) := by
  cases c with
  | none => rfl
  | some c => exact step M P c X d

theorem iterate_run [DecidableEq K] [DecidableEq E]
    (M : Λ → TM2.Stmt Γ Λ σ)
    (P : μ → TM2.Stmt (alphabet Γ Δ) (Λ ⊕ μ) (σ × δ))
    (n : Nat) (c : Option (TM2.Cfg Γ Λ σ)) (X : StackFamily Δ) (d : δ) :
    ((flip bind (TM2.step (program M P)))^[n]) (c.map (fun c' => cfg c' X d)) =
      (((flip bind (TM2.step M))^[n]) c).map (fun c' => cfg c' X d) := by
  induction n with
  | zero => rfl
  | succ n ih =>
    rw [Function.iterate_succ_apply', Function.iterate_succ_apply', ih]
    exact step_option M P _ X d

/-- Native steps are preserved exactly, including the run's full final state. -/
theorem bounded_run [DecidableEq K] [DecidableEq E]
    (M : Λ → TM2.Stmt Γ Λ σ)
    (P : μ → TM2.Stmt (alphabet Γ Δ) (Λ ⊕ μ) (σ × δ))
    (c c' : TM2.Cfg Γ Λ σ) (X : StackFamily Δ) (d : δ) (t : Nat)
    (h : StateTransition.EvalsToInTime (TM2.step M) c (some c') t) :
    Nonempty (StateTransition.EvalsToInTime (TM2.step (program M P))
      (cfg c X d) (some (cfg c' X d)) t) := by
  refine ⟨{ steps := h.steps, steps_le_m := h.steps_le_m, evals_in_steps := ?_ }⟩
  have hr := iterate_run M P h.steps (some c) X d
  rw [h.evals_in_steps] at hr
  exact hr

/-- Bundle the source machine with disjoint finite prefix stacks, labels and
auxiliary state. The source output alphabet is unchanged. -/
noncomputable def machine (tm : FinTM2) (E μ δ : Type)
    [DecidableEq E] [Fintype E] [Fintype μ] [Fintype δ]
    (Δ : E → Type) (raw : E) [Fintype (Δ raw)]
    (entry : μ) (d : δ)
    (P : μ → TM2.Stmt (alphabet tm.Γ Δ) (tm.Λ ⊕ μ) (tm.σ × δ)) :
    FinTM2 := by
  letI := tm.kFin
  letI := tm.ΛFin
  letI := tm.σFin
  exact {
    K := tm.K ⊕ E
    k₀ := .inr raw
    k₁ := .inl tm.k₁
    Γ := alphabet tm.Γ Δ
    Γk₀Fin := by change Fintype (Δ raw); infer_instance
    Λ := tm.Λ ⊕ μ
    main := .inr entry
    σ := tm.σ × δ
    initialState := (tm.initialState,d)
    m := program tm.m P }

#print axioms iterate_run
#print axioms bounded_run
#print axioms machine

section Bundle
variable (tm : FinTM2) {E μ δ : Type}
  [DecidableEq E] [Fintype E] [Fintype μ] [Fintype δ]
  (Δ : E → Type) (raw : E) [Fintype (Δ raw)]
  (entry : μ) (d : δ)
  (P : μ → TM2.Stmt (alphabet tm.Γ Δ) (tm.Λ ⊕ μ) (tm.σ × δ))

/-- The actual bundled machine retains the original run semantics. -/
theorem machine_step (c : tm.Cfg) (X : StackFamily Δ) (a : δ) :
    (machine tm E μ δ Δ raw entry d P).step (cfg c X a) =
      (tm.step c).map (fun c' => cfg c' X a) := by
  exact step tm.m P c X a

/-- If preprocessing empties the auxiliary stacks and restores the initial
auxiliary state, canonical original output is canonical wrapper output. -/
theorem machine_halt (out : List (tm.Γ tm.k₁)) :
    cfg (μ := μ) (haltList tm out) (fun _ : E => []) d =
      haltList (machine tm E μ δ Δ raw entry d P) out := by
  unfold cfg haltList
  simp only [Option.map_none]
  congr 1
  funext k
  cases k with
  | inl k =>
    by_cases h : k = tm.k₁
    · subst k
      simp [liftStacks, machine]
    · have hn : (Sum.inl k : tm.K ⊕ E) ≠ Sum.inl tm.k₁ := fun he => h (Sum.inl.inj he)
      simp [liftStacks, machine, h, hn] <;> rfl
  | inr e =>
    have hn : (Sum.inr e : tm.K ⊕ E) ≠ Sum.inl tm.k₁ := by intro h; cases h
    simp [liftStacks, machine, hn] <;> rfl

/-- Exact run after preprocessing, with the original step budget retained. -/
theorem machine_run (c c' : tm.Cfg) (X : StackFamily Δ) (a : δ) (t : Nat)
    (h : StateTransition.EvalsToInTime tm.step c (some c') t) :
    Nonempty (StateTransition.EvalsToInTime (machine tm E μ δ Δ raw entry d P).step
      (cfg c X a) (some (cfg c' X a)) t) :=
  bounded_run tm.m P c c' X a t h

end Bundle

#print axioms machine_step
#print axioms machine_halt
#print axioms machine_run

section PrefixComposition
variable (tm : FinTM2) {E μ δ : Type}
  [DecidableEq E] [Fintype E] [Fintype μ] [Fintype δ]
  (Δ : E → Type) (raw : E) [Fintype (Δ raw)]
  (entry : μ) (d : δ)
  (P : μ → TM2.Stmt (alphabet tm.Γ Δ) (tm.Λ ⊕ μ) (tm.σ × δ))

/-- Composing a checked input prefix and the lifted original run adds the
prefix cost and original time bound exactly. No source-verifier execution is
charged to the adapter or hidden in the initial configuration. -/
theorem machine_outputs_of_prefix
    (input : List (Δ raw)) (sourceInput : List (tm.Γ tm.k₀))
    (out : List (tm.Γ tm.k₁)) (s t : Nat)
    (hp : StateTransition.EvalsToInTime (machine tm E μ δ Δ raw entry d P).step
      (initList (machine tm E μ δ Δ raw entry d P) input)
      (some (cfg (initList tm sourceInput) (fun _ : E => []) d)) s)
    (h : TM2OutputsInTime tm sourceInput (some out) t) :
    Nonempty (TM2OutputsInTime (machine tm E μ δ Δ raw entry d P)
      input (some out) (s+t)) := by
  change StateTransition.EvalsToInTime tm.step (initList tm sourceInput)
    (some (haltList tm out)) t at h
  rcases machine_run tm Δ raw entry d P (initList tm sourceInput) (haltList tm out)
      (fun _ : E => []) d t h with ⟨hr⟩
  rw [machine_halt tm Δ raw entry d P out] at hr
  refine ⟨?_⟩
  change StateTransition.EvalsToInTime (machine tm E μ δ Δ raw entry d P).step
    (initList (machine tm E μ δ Δ raw entry d P) input)
    (some (haltList (machine tm E μ δ Δ raw entry d P) out)) (s+t)
  simpa only [Nat.add_comm t s] using
    (StateTransition.EvalsToInTime.trans (machine tm E μ δ Δ raw entry d P).step
      s t _ _ _ hp hr)

end PrefixComposition

#print axioms machine_outputs_of_prefix

end TM2PrefixLift
end MathSolve.PNP
