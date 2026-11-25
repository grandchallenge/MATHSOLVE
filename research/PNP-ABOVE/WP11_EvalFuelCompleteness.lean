import PNPAbove.WP10

/-! WP11 — general source-native fuel completeness, cost-indexed. -/
namespace PNPAbove.WP11
open MIPRE MIPRE.Cost

theorem runFuel_complete_cost :
    ∀ {env : Env} {p : Prog} {r : Data} {t : Nat},
      Eval env p r t → ∀ fuel : Nat, t < fuel →
        WP09.runFuel fuel env p = some (r, t) := by
  intro env p r t h
  induction h with
  | var env i =>
      intro fuel hf
      cases fuel with
      | zero => omega
      | succ fuel => simp [WP09.runFuel]
  | nil env =>
      intro fuel hf
      cases fuel with
      | zero => omega
      | succ fuel => simp [WP09.runFuel]
  | const env d =>
      intro fuel hf
      cases fuel with
      | zero => omega
      | succ fuel => simp [WP09.runFuel]
  | cons h1 h2 ih1 ih2 =>
      intro fuel hf
      cases fuel with
      | zero => omega
      | succ fuel => simp [WP09.runFuel, ih1 fuel (by omega), ih2 fuel (by omega)]
  | elim_nil hget h1 ih1 =>
      intro fuel hf
      cases fuel with
      | zero => omega
      | succ fuel => simp [WP09.runFuel, hget, ih1 fuel (by omega)]
  | elim_cons hget h1 ih1 =>
      intro fuel hf
      cases fuel with
      | zero => omega
      | succ fuel => simp [WP09.runFuel, hget, ih1 fuel (by omega)]
  | let_ h1 h2 ih1 ih2 =>
      intro fuel hf
      cases fuel with
      | zero => omega
      | succ fuel => simp [WP09.runFuel, ih1 fuel (by omega), ih2 fuel (by omega)]
  | loop_nil h1 ih1 =>
      intro fuel hf
      cases fuel with
      | zero => omega
      | succ fuel => simp [WP09.runFuel, ih1 fuel (by omega)]
  | loop_stop h1 ih1 =>
      intro fuel hf
      cases fuel with
      | zero => omega
      | succ fuel => simp [WP09.runFuel, ih1 fuel (by omega)]
  | loop_step h1 h2 ih1 ih2 =>
      intro fuel hf
      cases fuel with
      | zero => omega
      | succ fuel => simp [WP09.runFuel, ih1 fuel (by omega), ih2 fuel (by omega)]


/-- The genuine upstream timed Eval relation is equivalent to the
    independent finite-fuel interpreter at the cost-indexed budget. -/
theorem eval_iff_runFuel (env : Env) (p : Prog) (r : Data) (t : Nat) :
    Eval env p r t ↔ WP09.runFuel (t + 1) env p = some (r, t) := by
  constructor
  · intro h
    exact runFuel_complete_cost h (t+1) (by omega)
  · intro h
    exact WP09.runFuel_sound (t+1) env p r t h

/-- This is a quantified, not just sampled, source-native acceptance bridge:
    accepting a typed input is equivalent to existence of a terminating
    successful run by the exact independent interpreter. -/
theorem accepts_iff_fuel_exists (n : Nat) (x y a b : BitStr) :
    WP08.identityDecider.Accepts n x y a b ↔
      ∃ fuel t, WP09.runFuel fuel [WP08.sample n x y a b]
        WP08.identityDeciderProg = some (encode true, t) := by
  constructor
  · intro h
    change ∃ t, Eval [WP08.sample n x y a b]
      WP08.identityDeciderProg (encode true) t at h
    obtain ⟨t, ht⟩ := h
    exact ⟨t + 1, t, runFuel_complete_cost ht (t+1) (by omega)⟩
  · rintro ⟨f, t, ht⟩
    exact WP10.accepts_of_fuel n x y a b f t ht


/-- Syntactic exclusion of unbounded source iteration. -/
def LoopFree : Prog → Prop
  | .var _ | .nil | .const _ => True
  | .cons a b => LoopFree a ∧ LoopFree b
  | .elim _ a b => LoopFree a ∧ LoopFree b
  | .let_ a b => LoopFree a ∧ LoopFree b
  | .loop _ => False

/-- Any loop-free program terminates in every source environment. -/
theorem loopfree_terminates : ∀ p : Prog, LoopFree p →
    ∀ env : Env, ∃ r t, Eval env p r t := by
  intro p
  induction p with
  | var i =>
      intro _ env
      exact ⟨env.get i, (env.get i).size + 1, Eval.var env i⟩
  | nil =>
      intro _ env
      exact ⟨.nil, 1, Eval.nil env⟩
  | const d =>
      intro _ env
      exact ⟨d, d.size, Eval.const env d⟩
  | cons a b iha ihb =>
      intro hp env
      obtain ⟨ra, ta, ha⟩ := iha hp.1 env
      obtain ⟨rb, tb, hb⟩ := ihb hp.2 env
      exact ⟨.cons ra rb, ta+tb+1, Eval.cons ha hb⟩
  | elim i a b iha ihb =>
      intro hp env
      cases hx : env.get i with
      | nil =>
          obtain ⟨r,t,h⟩ := iha hp.1 env
          exact ⟨r,t+1,Eval.elim_nil hx h⟩
      | cons x y =>
          obtain ⟨r,t,h⟩ := ihb hp.2 (x::y::env)
          exact ⟨r,t+1,Eval.elim_cons hx h⟩
  | let_ a b iha ihb =>
      intro hp env
      obtain ⟨v,s,ha⟩ := iha hp.1 env
      obtain ⟨r,t,hb⟩ := ihb hp.2 (v::env)
      exact ⟨r,s+t+1,Eval.let_ ha hb⟩
  | loop b ih =>
      intro hp env
      cases hp

/-- The recursive nine-bit parser contains no source loop. -/
theorem checkBits_loopfree (index k : Nat) :
    LoopFree (WP08.checkBits index k) := by
  induction k generalizing index with
  | zero => simp [WP08.checkBits, LoopFree, WP08.yes, WP08.no]
  | succ k ih => simp [WP08.checkBits, LoopFree, WP08.no, ih]

/-- Its native decider also contains no source loop. -/
theorem identityDecider_loopfree : LoopFree WP08.identityDeciderProg := by
  simp [WP08.identityDeciderProg, LoopFree, WP08.no, checkBits_loopfree]

/-- Every raw (even malformed) input to the identity-decider program halts
    in the *imported* native MIPRE.Cost.Eval relation. -/
theorem identityDecider_total (input : Data) :
    ∃ r t, Eval [input] WP08.identityDeciderProg r t :=
  loopfree_terminates _ identityDecider_loopfree [input]

/-- Consequential source-native interpreter completeness for every raw input:
    no additional facts about a well-formed question are used. -/
theorem identityDecider_fuel_total (input : Data) :
    ∃ fuel r t, WP09.runFuel fuel [input] WP08.identityDeciderProg = some (r,t) := by
  obtain ⟨r,t,h⟩ := identityDecider_total input
  exact ⟨t+1,r,t,runFuel_complete_cost h (t+1) (by omega)⟩


/-- A stronger syntactic fragment: no loops and no copying of unbounded input data. -/
def NoVarLoop : Prog → Prop
  | .var _ => False
  | .nil | .const _ => True
  | .cons a b => NoVarLoop a ∧ NoVarLoop b
  | .elim _ a b => NoVarLoop a ∧ NoVarLoop b
  | .let_ a b => NoVarLoop a ∧ NoVarLoop b
  | .loop _ => False

/-- A closed, input-independent bound for source-native evaluation costs in
    this loop-free and copy-free fragment. -/
def staticCost : Prog → Nat
  | .var _ => 0
  | .nil => 1
  | .const d => d.size
  | .cons a b => staticCost a + staticCost b + 1
  | .elim _ a b => max (staticCost a) (staticCost b) + 1
  | .let_ a b => staticCost a + staticCost b + 1
  | .loop _ => 0

/-- Uniform source-native time bound for any evaluation of such a program. -/
theorem noVarLoop_cost_bound {env : Env} {p : Prog} {r : Data}
    {t : Nat} (h : Eval env p r t) : NoVarLoop p → t ≤ staticCost p := by
  induction h with
  | var env i =>
      intro hp
      simp [NoVarLoop] at hp
  | nil env =>
      intro hp
      simp [staticCost]
  | const env d =>
      intro hp
      simp [staticCost]
  | cons h1 h2 ih1 ih2 =>
      intro hp
      simp only [NoVarLoop] at hp
      have hcost1 := ih1 hp.1
      have hcost2 := ih2 hp.2
      simp only [staticCost]
      omega
  | elim_nil he h1 ih1 =>
      intro hp
      simp only [NoVarLoop] at hp
      have hcost := ih1 hp.1
      simp only [staticCost]
      omega
  | elim_cons he h1 ih1 =>
      intro hp
      simp only [NoVarLoop] at hp
      have hcost := ih1 hp.2
      simp only [staticCost]
      omega
  | let_ h1 h2 ih1 ih2 =>
      intro hp
      simp only [NoVarLoop] at hp
      have hcost1 := ih1 hp.1
      have hcost2 := ih2 hp.2
      simp only [staticCost]
      omega
  | loop_nil h1 ih1 =>
      intro hp
      simp [NoVarLoop] at hp
  | loop_stop h1 ih1 =>
      intro hp
      simp [NoVarLoop] at hp
  | loop_step h1 h2 ih1 ih2 =>
      intro hp
      simp [NoVarLoop] at hp

/-- The nine-bit parser never reads/copied a variable as an output and
    never enters a source loop, for every input and every parser depth. -/
theorem checkBits_noVarLoop (index k : Nat) :
    NoVarLoop (WP08.checkBits index k) := by
  induction k generalizing index with
  | zero => simp [WP08.checkBits, NoVarLoop, WP08.yes, WP08.no]
  | succ k ih => simp [WP08.checkBits, NoVarLoop, WP08.no, ih]

theorem identityDecider_noVarLoop : NoVarLoop WP08.identityDeciderProg := by
  simp [WP08.identityDeciderProg, NoVarLoop, WP08.no, checkBits_noVarLoop]

/-- Every *raw* input is decided within the same explicit source-cost
    bound, including malformed data. No bound on its input Data.size is assumed. -/
theorem identityDecider_uniform_fuel (input : Data) :
    ∃ r t, t ≤ staticCost WP08.identityDeciderProg ∧
      WP09.runFuel (staticCost WP08.identityDeciderProg + 1)
        [input] WP08.identityDeciderProg = some (r, t) := by
  obtain ⟨r,t,h⟩ := identityDecider_total input
  have ht := noVarLoop_cost_bound h identityDecider_noVarLoop
  exact ⟨r,t,ht,runFuel_complete_cost h _ (by omega)⟩

/-- A single uniform, statically determined fuel suffices to decide native
    source acceptance for every typed identity-game question. -/
theorem accepts_iff_uniform_fuel (n : Nat) (x y a b : BitStr) :
    WP08.identityDecider.Accepts n x y a b ↔
      ∃ t, WP09.runFuel (staticCost WP08.identityDeciderProg + 1)
        [WP08.sample n x y a b] WP08.identityDeciderProg = some (encode true,t) := by
  constructor
  · intro h
    change ∃ t, Eval [WP08.sample n x y a b]
      WP08.identityDeciderProg (encode true) t at h
    obtain ⟨t, ht⟩ := h
    have hbound := noVarLoop_cost_bound ht identityDecider_noVarLoop
    exact ⟨t, runFuel_complete_cost ht _ (by omega)⟩
  · rintro ⟨t, ht⟩
    exact WP10.accepts_of_fuel n x y a b _ t ht


/-- Shape discipline guaranteeing that every native Eval output is
    a canonical encoded Boolean; let-binding expressions need only terminate. -/
def BooleanResult : Prog → Prop
  | .const d => d = encode true ∨ d = encode false
  | .elim _ n c => BooleanResult n ∧ BooleanResult c
  | .let_ _ b => BooleanResult b
  | _ => False

/-- Imported evaluation respects the source-level Boolean-output discipline. -/
theorem eval_boolean_result {env : Env} {p : Prog} {r : Data} {t : Nat}
    (h : Eval env p r t) (hp : BooleanResult p) :
    r = encode true ∨ r = encode false := by
  induction h with
  | var env i => simp [BooleanResult] at hp
  | nil env => simp [BooleanResult] at hp
  | const env d => exact hp
  | cons h1 h2 ih1 ih2 => simp [BooleanResult] at hp
  | elim_nil hget h1 ih1 => exact ih1 hp.1
  | elim_cons hget h1 ih1 => exact ih1 hp.2
  | let_ h1 h2 ih1 ih2 => exact ih2 hp
  | loop_nil h1 ih1 => simp [BooleanResult] at hp
  | loop_stop h1 ih1 => simp [BooleanResult] at hp
  | loop_step h1 h2 ih1 ih2 => simp [BooleanResult] at hp

/-- Both branches of the length-9 question parser return canonical Booleans. -/
theorem checkBits_boolean (index k : Nat) :
    BooleanResult (WP08.checkBits index k) := by
  induction k generalizing index with
  | zero => simp [WP08.checkBits, BooleanResult, WP08.yes, WP08.no]
  | succ k ih => simp [WP08.checkBits, BooleanResult, WP08.no, ih]

theorem identityDecider_boolean : BooleanResult WP08.identityDeciderProg := by
  simp [WP08.identityDeciderProg, BooleanResult, WP08.no, checkBits_boolean]

/-- Universal total Boolean decision evidence, now not just existence of some
    native output: all raw inputs produce exactly one of canonical true/false. -/
theorem identityDecider_uniform_boolean (input : Data) :
    (∃ t, WP09.runFuel (staticCost WP08.identityDeciderProg + 1)
        [input] WP08.identityDeciderProg = some (encode true,t)) ∨
    (∃ t, WP09.runFuel (staticCost WP08.identityDeciderProg + 1)
        [input] WP08.identityDeciderProg = some (encode false,t)) := by
  obtain ⟨r,t,ht,hrun⟩ := identityDecider_uniform_fuel input
  have he := WP09.runFuel_sound _ _ _ _ _ hrun
  rcases eval_boolean_result he identityDecider_boolean with hr | hr
  · left
    subst r
    exact ⟨t,hrun⟩
  · right
    subst r
    exact ⟨t,hrun⟩


/-- Completes the WP10 rejection bridge at a single fixed fuel for every
    *typed* question: failure of the upstream Accepts relation is equivalent
    to an actual canonical-false interpreter execution, not a timeout. -/
theorem rejects_iff_uniform_false (n : Nat) (x y a b : BitStr) :
    ¬ WP08.identityDecider.Accepts n x y a b ↔
      ∃ t, WP09.runFuel (staticCost WP08.identityDeciderProg + 1)
        [WP08.sample n x y a b] WP08.identityDeciderProg = some (encode false,t) := by
  constructor
  · intro hn
    rcases identityDecider_uniform_boolean (WP08.sample n x y a b) with ht | hf
    · exact False.elim (hn ((accepts_iff_uniform_fuel n x y a b).mpr ht))
    · exact hf
  · rintro ⟨t,hf⟩
    exact WP10.rejects_of_fuel n x y a b _ t hf

#guard decide (staticCost WP08.identityDeciderProg = 89)

end PNPAbove.WP11
