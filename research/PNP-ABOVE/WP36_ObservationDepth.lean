import MIPRE.Foundations.Cost.PolyTime

namespace PNPAbove.WP36
open MIPRE MIPRE.Cost

/-- Agreement on the first n levels of the actual source Data tree.
No restriction is imposed below the observation depth. -/
def Agree : Nat → Data → Data → Prop
  | 0, _, _ => True
  | _+1, .nil, .nil => True
  | n+1, .cons a b, .cons c d => Agree n a c ∧ Agree n b d
  | _+1, _, _ => False

theorem agree_refl (n : Nat) (d : Data) : Agree n d d := by
  induction n generalizing d with
  | zero => trivial
  | succ n ih => cases d <;> simp [Agree, ih]

theorem agree_down {n m : Nat} (h : n ≤ m) {a b : Data} (hab : Agree m a b) :
    Agree n a b := by
  induction n generalizing m a b with
  | zero => trivial
  | succ n ih =>
    cases m with
    | zero => omega
    | succ m =>
      cases a with
      | nil => cases b <;> exact hab
      | cons a c =>
        cases b with
        | nil => exact hab
        | cons b d => exact ⟨ih (by omega) hab.1, ih (by omega) hab.2⟩

theorem agree_eq_of_size {n : Nat} {a b : Data} (h : a.size ≤ n)
    (hab : Agree n a b) : a = b := by
  induction a generalizing n b with
  | nil =>
    cases n with
    | zero => simp at h
    | succ n => cases b <;> simp [Agree] at hab ⊢
  | cons a c iha ihc =>
    cases n with
    | zero => have := Data.size_pos (.cons a c); omega
    | succ n =>
      cases b with
      | nil => exact False.elim hab
      | cons b d =>
        have h' : a.size + c.size + 1 ≤ n+1 := h
        exact congrArg₂ Data.cons (iha (by omega) hab.1) (ihc (by omega) hab.2)

def EnvAgree (n : Nat) (e e' : Env) : Prop :=
  ∀ i, Agree n (e.get i) (e'.get i)

theorem env_down {n m : Nat} (h : n ≤ m) {e e' : Env} (he : EnvAgree m e e') :
    EnvAgree n e e' := fun i => agree_down h (he i)

theorem env_cons {n : Nat} {a a' : Data} {e e' : Env}
    (ha : Agree n a a') (he : EnvAgree n e e') :
    EnvAgree n (a::e) (a'::e') := by
  intro i
  cases i with
  | zero => simpa only [Env.get_cons_zero] using ha
  | succ i => simpa only [Env.get_cons_succ] using he i

theorem env_tail {n : Nat} {e e' : Env} (he : EnvAgree n e e') :
    EnvAgree n e.tail e'.tail := by
  intro i
  have h := he (i+1)
  cases e <;> cases e' <;> simpa only [List.tail_nil, List.tail_cons, Env.get_nil, Env.get_cons_succ] using h

/-- All source programs, including arbitrary loops and arbitrary hardcoded
constants, preserve exact result AND cost under depth-t input agreement
for a run of cost t. This is a bound on the full source evaluator. -/
theorem eval_agreement {e : Env} {p : Prog} {r : Data} {t : Nat}
    (h : Eval e p r t) :
    ∀ e', EnvAgree t e e' → Eval e' p r t := by
  induction h with
  | var e i =>
    intro e' he
    have hh := agree_eq_of_size (by omega : (e.get i).size ≤ (e.get i).size + 1) (he i)
    rw [hh]
    exact .var _ _
  | nil e => intro e' _; exact .nil _
  | const e d => intro e' _; exact .const _ _
  | @cons e hp tp a b s u h1 h2 ih1 ih2 =>
    intro e' he
    exact .cons (ih1 e' (env_down (by omega) he)) (ih2 e' (env_down (by omega) he))
  | @elim_nil e i n c r t hn hsub ih =>
    intro e' he
    have hi := he i
    rw [hn] at hi
    have hn' : e'.get i = .nil := by
      cases hg : e'.get i with
      | nil => rfl
      | cons a b => rw [hg] at hi; exact False.elim hi
    exact .elim_nil hn' (ih e' (env_down (by omega) he))
  | @elim_cons e i n c a b r t hc hsub ih =>
    intro e' he
    have hi := he i
    rw [hc] at hi
    cases hg : e'.get i with
    | nil => rw [hg] at hi; exact False.elim hi
    | cons a' b' =>
      rw [hg] at hi
      exact .elim_cons hg (ih _ (env_cons hi.1 (env_cons hi.2 (env_down (by omega) he))))
  | @let_ e ep bp v r s t h1 h2 ih1 ih2 =>
    intro e' he
    exact .let_ (ih1 _ (env_down (by omega) he))
      (ih2 _ (env_cons (agree_refl _ _) (env_down (by omega) he)))
  | loop_nil hsub ih =>
    intro e' he
    exact .loop_nil (ih _ (env_down (by omega) he))
  | loop_stop hsub ih =>
    intro e' he
    exact .loop_stop (ih _ (env_down (by omega) he))
  | @loop_step e b x y v r s t h1 h2 ih1 ih2 =>
    intro e' he
    exact .loop_step (ih1 _ (env_down (by omega) he))
      (ih2 _ (env_cons (agree_refl _ _) (env_tail (env_down (by omega) he))))

theorem runs_agreement {p : Prog} {a b r : Data} {t : Nat}
    (h : p.Runs a r t) (hab : Agree t a b) : p.Runs b r t := by
  exact eval_agreement h [b] (env_cons hab (fun i => agree_refl _ _))


theorem agree_symm {n : Nat} {a b : Data} (h : Agree n a b) : Agree n b a := by
  induction n generalizing a b with
  | zero => trivial
  | succ n ih =>
    cases a with
    | nil => cases b <;> exact h
    | cons a c =>
      cases b with
      | nil => exact h
      | cons b d => exact ⟨ih h.1, ih h.2⟩

end PNPAbove.WP36
