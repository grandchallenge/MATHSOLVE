import MIPRE.Foundations.Verifier

/-! PNP-ABOVE WP09: generic soundness of the WP08 fuel interpreter against actual
MIPRE.Cost.Eval at pinned upstream commit 5926bdff5db621f44682a101007ef2fe3ae8d970.
No copying of upstream types or Eval rules; no compressor execution. -/
namespace PNPAbove.WP09
open MIPRE
open MIPRE.Cost

def runFuel : Nat → Env → Prog → Option (Data × Nat)
  | 0, _, _ => none
  | fuel + 1, env, p =>
    match p with
    | .var i => some (env.get i, (env.get i).size + 1)
    | .nil => some (.nil, 1)
    | .const d => some (d, d.size)
    | .cons h t => do
        let (a,s) ← runFuel fuel env h
        let (b,u) ← runFuel fuel env t
        pure (.cons a b, s+u+1)
    | .elim i n c =>
        match env.get i with
        | .nil => do
            let (r,t) ← runFuel fuel env n
            pure (r,t+1)
        | .cons a b => do
            let (r,t) ← runFuel fuel (a :: b :: env) c
            pure (r,t+1)
    | .let_ e b => do
        let (v,s) ← runFuel fuel env e
        let (r,t) ← runFuel fuel (v :: env) b
        pure (r,s+t+1)
    | .loop b =>
        match runFuel fuel env b with
        | none => none
        | some (.nil,t) => some (.nil,t+1)
        | some (.cons flag v,s) =>
            match flag with
            | .nil => some (v,s+1)
            | .cons _ _ => do
                let (r,t) ← runFuel fuel (v :: env.tail) (.loop b)
                pure (r,s+t+1)



/-- Soundness of the interpreter against the actual pinned upstream evaluation
relation: successful fuel runs have exactly the reported source cost. -/
theorem runFuel_sound :
    ∀ (fuel : Nat) (env : Env) (p : Prog) (r : Data) (t : Nat),
      runFuel fuel env p = some (r,t) → Eval env p r t := by
  intro fuel
  induction fuel with
  | zero =>
      intro env p r t h
      simp [runFuel] at h
  | succ fuel ih =>
      intro env p r t h
      cases p with
      | var i =>
          simp only [runFuel] at h
          cases h
          exact Eval.var env i
      | nil =>
          simp only [runFuel] at h
          cases h
          exact Eval.nil env
      | const d =>
          simp only [runFuel] at h
          cases h
          exact Eval.const env r
      | cons p q =>
          cases hp : runFuel fuel env p with
          | none => simp [runFuel, hp] at h
          | some pair =>
              cases pair with
              | mk a s =>
                  cases hq : runFuel fuel env q with
                  | none => simp [runFuel, hp, hq] at h
                  | some pair2 =>
                      cases pair2 with
                      | mk b u =>
                          simp [runFuel, hp, hq] at h
                          rcases h with ⟨hr, ht⟩
                          subst r
                          subst t
                          exact Eval.cons (ih env p a s hp) (ih env q b u hq)
      | elim i n c =>
          cases hd : env.get i with
          | nil =>
              cases hn : runFuel fuel env n with
              | none => simp [runFuel, hd, hn] at h
              | some pair =>
                  cases pair with
                  | mk a s =>
                      simp [runFuel, hd, hn] at h
                      rcases h with ⟨hr, ht⟩
                      subst r
                      subst t
                      exact Eval.elim_nil hd (ih env n a s hn)
          | cons a b =>
              cases hc : runFuel fuel (a :: b :: env) c with
              | none => simp [runFuel, hd, hc] at h
              | some pair =>
                  cases pair with
                  | mk v s =>
                      simp [runFuel, hd, hc] at h
                      rcases h with ⟨hr, ht⟩
                      subst r
                      subst t
                      exact Eval.elim_cons hd (ih (a :: b :: env) c v s hc)
      | let_ e b =>
          cases he : runFuel fuel env e with
          | none => simp [runFuel, he] at h
          | some pair =>
              cases pair with
              | mk v s =>
                  cases hb : runFuel fuel (v :: env) b with
                  | none => simp [runFuel, he, hb] at h
                  | some pair2 =>
                      cases pair2 with
                      | mk w t2 =>
                          simp [runFuel, he, hb] at h
                          rcases h with ⟨hr, ht⟩
                          subst r
                          subst t
                          exact Eval.let_ (ih env e v s he) (ih (v :: env) b w t2 hb)
      | loop b =>
          cases hb : runFuel fuel env b with
          | none => simp [runFuel, hb] at h
          | some pair =>
              cases pair with
              | mk v s =>
                  cases v with
                  | nil =>
                      simp [runFuel, hb] at h
                      rcases h with ⟨hr, ht⟩
                      subst r
                      subst t
                      exact Eval.loop_nil (ih env b .nil s hb)
                  | cons flag v =>
                      cases flag with
                      | nil =>
                          simp [runFuel, hb] at h
                          rcases h with ⟨hr, ht⟩
                          subst r
                          subst t
                          exact Eval.loop_stop (ih env b (.cons .nil v) s hb)
                      | cons x y =>
                          cases hrec : runFuel fuel (v :: env.tail) (.loop b) with
                          | none => simp [runFuel, hb, hrec] at h
                          | some pair2 =>
                              cases pair2 with
                              | mk out t2 =>
                                  simp [runFuel, hb, hrec] at h
                                  rcases h with ⟨hr, ht⟩
                                  subst r
                                  subst t
                                  exact Eval.loop_step (ih env b (.cons (.cons x y) v) s hb)
                                    (ih (v :: env.tail) (.loop b) out t2 hrec)

end PNPAbove.WP09
