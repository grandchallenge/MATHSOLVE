import PNPAbove.WP36Eval

namespace PNPAbove.WP36
open MIPRE.Cost

def height : Prog → Nat
  | .var _ | .nil | .const _ => 1
  | .cons a b | .let_ a b | .elim _ a b => height a + height b + 1
  | .loop b => height b + 1

theorem height_pos (p : Prog) : 0 < height p := by
  cases p <;> simp [height]

def ResultAgree (H q D : Nat) (a b : Data) : Prop :=
  Agree (D-H*q) a b ∧ (q=0 → a=b)

theorem result_refl (H q D : Nat) (a : Data) : ResultAgree H q D a a :=
  ⟨agree_refl _ _, fun _ => rfl⟩

theorem subbudget {L A H q Q D : Nat} (hA : A ≤ H) (hq : q ≤ Q)
    (hD : L+H*(Q+1) ≤ D) : L+A*(q+1) ≤ D :=
  (Nat.add_le_add_left (Nat.mul_le_mul hA (by omega)) L).trans hD

theorem sequential_budget {L A H q v D : Nat} (hA : A ≤ H)
    (hD : L+H*(q+v+1) ≤ D) : L+A*(v+1) ≤ D-H*q := by
  have hh := Nat.mul_le_mul_right (v+1) hA
  rw [show q+v+1 = q+(v+1) by omega, Nat.mul_add] at hD
  apply Nat.le_sub_of_add_le
  omega

theorem depth_budget {L H q D : Nat} (hD : L+H*(q+1) ≤ D) :
    L ≤ D-H*q := by
  rw [Nat.mul_add, Nat.mul_one] at hD
  omega

theorem result_weaken {A H q Q D : Nat} {a b : Data} (hA : A ≤ H)
    (hq : q ≤ Q) (h : ResultAgree A q D a b) : ResultAgree H Q D a b := by
  have hm := Nat.mul_le_mul hA hq
  exact ⟨agree_down (by omega) h.1, fun h0 => h.2 (by omega)⟩

theorem result_after_seq {A H q v D : Nat} {a b : Data}
    (hA : A ≤ H) (h : ResultAgree A v (D-H*q) a b) :
    ResultAgree H (q+v) D a b := by
  have hm := Nat.mul_le_mul_right v hA
  refine ⟨agree_down ?_ h.1, fun h0 => h.2 (by omega)⟩
  rw [Nat.mul_add, ← Nat.sub_sub]
  omega

theorem result_after_descent {A H q D : Nat} {a b : Data} (hA : A+1 ≤ H)
    (h : ResultAgree A q (D-1) a b) : ResultAgree H q D a b := by
  by_cases hq : q=0
  · have he := h.2 hq
    subst b
    exact result_refl _ _ _ _
  · have hm := Nat.mul_le_mul_right q hA
    rw [Nat.add_mul, Nat.one_mul] at hm
    exact ⟨agree_down (by omega) h.1, fun h0 => False.elim (hq h0)⟩

theorem descent_budget {L A H q D : Nat} (hA : A+1 ≤ H)
    (hD : L+H*(q+1) ≤ D) : L+A*(q+1) ≤ D-1 := by
  have hm := Nat.mul_le_mul_right (q+1) hA
  rw [Nat.add_mul, Nat.one_mul] at hm
  omega

theorem result_cons_tail {A H q D : Nat} {a b c d : Data}
    (hA : A+1 ≤ H) (hD : H*q ≤ D)
    (h : ResultAgree A q D (.cons a b) (.cons c d)) : ResultAgree H q D b d := by
  by_cases hq : q=0
  · have he := Data.cons.inj (h.2 hq)
    have hh := he.2
    subst d
    exact result_refl _ _ _ _
  · have hm := Nat.mul_le_mul_right q hA
    rw [Nat.add_mul, Nat.one_mul] at hm
    have hd : D-H*q+1 ≤ D-A*q := by omega
    have hh := agree_down hd h.1
    exact ⟨hh.2, fun h0 => False.elim (hq h0)⟩

theorem result_depth_le {L H q D : Nat} {a b : Data}
    (hD : L+H*(q+1) ≤ D) (h : ResultAgree H q D a b) : Agree L a b :=
  agree_down (depth_budget hD) h.1

theorem eval_copy_budget {e : Env} {p : Prog} {r : Data} {t : Nat}
    (h : Eval e p r t) (L : Nat) (hL : 3 ≤ L) :
    ∃ q : Nat, q*L ≤ t ∧
      ∀ D e', L+height p*(q+1) ≤ D → EnvAgree D e e' →
      ∃ r' t', Eval e' p r' t' ∧ ResultAgree (height p) q D r r' := by
  induction h with
  | var e i =>
    by_cases hb : L ≤ (e.get i).size+1
    · refine ⟨1, by simpa using hb, ?_⟩
      intro D e' hD he
      refine ⟨e'.get i, _, .var _ _, ?_⟩
      exact ⟨agree_down (by omega) (he i), by omega⟩
    · refine ⟨0, by simp, ?_⟩
      intro D e' hD he
      have hs : (e.get i).size ≤ D := by simp [height] at hD; omega
      have hh := agree_eq_of_size hs (he i)
      exact ⟨e'.get i, _, .var _ _, by rw [hh]; exact result_refl _ _ _ _⟩
  | nil e =>
    exact ⟨0, by simp, fun D e' _ _ => ⟨.nil,1,.nil _,result_refl _ _ _ _⟩⟩
  | const e d =>
    exact ⟨0, by simp, fun D e' _ _ => ⟨d,d.size,.const _ _,result_refl _ _ _ _⟩⟩
  | @cons e hp tp a b s u h1 h2 ih1 ih2 =>
    obtain ⟨q,hq,Hq⟩ := ih1
    obtain ⟨v,hv,Hv⟩ := ih2
    let H := height (.cons hp tp)
    have hA : height hp ≤ H := by simp [H,height]; omega
    have hB : height tp ≤ H := by simp [H,height]; omega
    refine ⟨q+v, by rw [Nat.add_mul]; omega, ?_⟩
    intro D e' hD he
    obtain ⟨a',s',ha,ra⟩ := Hq D e' (subbudget hA (by omega) hD) he
    obtain ⟨b',u',hb,rb⟩ := Hv D e' (subbudget hB (by omega) hD) he
    refine ⟨.cons a' b',_,.cons ha hb,?_⟩
    have aa := (result_weaken hA (show q ≤ q+v by omega) ra).1
    have bb := (result_weaken hB (show v ≤ q+v by omega) rb).1
    refine ⟨?_, fun h0 => congrArg₂ Data.cons (ra.2 (by omega)) (rb.2 (by omega))⟩
    exact agree_down (Nat.le_succ _) (show Agree ((D-H*(q+v))+1) (.cons a b) (.cons a' b') from ⟨aa,bb⟩)
  | @elim_nil e i n c r t hn hsub ih =>
    obtain ⟨q,hq,Hq⟩ := ih
    let H := height (.elim i n c)
    have hA : height n ≤ H := by simp [H,height]; omega
    refine ⟨q,by omega,?_⟩
    intro D e' hD he
    have hd : 1 ≤ D := by omega
    have hi := agree_down hd (he i)
    rw [hn] at hi
    have hn' : e'.get i = .nil := by
      cases hg : e'.get i with
      | nil => rfl
      | cons a b => rw [hg] at hi; exact False.elim hi
    obtain ⟨r',t',hr,rr⟩ := Hq D e' (subbudget hA le_rfl hD) he
    exact ⟨r',_,.elim_nil hn' hr,result_weaken hA le_rfl rr⟩
  | @elim_cons e i n c a b r t hc hsub ih =>
    obtain ⟨q,hq,Hq⟩ := ih
    let H := height (.elim i n c)
    have hA : height c+1 ≤ H := by simp [H,height]
    refine ⟨q,by omega,?_⟩
    intro D e' hD he
    have hd : 1 ≤ D := by omega
    have hi := he i
    rw [hc] at hi
    cases hg : e'.get i with
    | nil =>
      have hz := agree_down hd hi
      rw [hg] at hz
      exact False.elim hz
    | cons a' b' =>
      rw [hg] at hi
      have hcut : Agree ((D-1)+1) (.cons a b) (.cons a' b') :=
        agree_down (by omega) hi
      obtain ⟨r',t',hr,rr⟩ := Hq (D-1) (a'::b'::e')
        (descent_budget hA hD)
        (env_cons hcut.1 (env_cons hcut.2 (env_down (by omega) he)))
      exact ⟨r',_,.elim_cons hg hr,result_after_descent hA rr⟩
  | @let_ e ep bp a r s t h1 h2 ih1 ih2 =>
    obtain ⟨q,hq,Hq⟩ := ih1
    obtain ⟨v,hv,Hv⟩ := ih2
    let H := height (.let_ ep bp)
    have hA : height ep ≤ H := by simp [H,height]; omega
    have hB : height bp ≤ H := by simp [H,height]; omega
    refine ⟨q+v,by rw [Nat.add_mul]; omega,?_⟩
    intro D e' hD he
    obtain ⟨a',s',ha,ra⟩ := Hq D e' (subbudget hA (by omega) hD) he
    have haa := (result_weaken hA le_rfl ra).1
    obtain ⟨r',t',hr,rr⟩ := Hv (D-H*q) (a'::e')
      (sequential_budget hB hD) (env_cons haa (env_down (by omega) he))
    exact ⟨r',_,.let_ ha hr,result_after_seq hB rr⟩
  | @loop_nil e b t hsub ih =>
    obtain ⟨q,hq,Hq⟩ := ih
    let H := height (.loop b)
    have hA : height b ≤ H := by simp [H,height]
    refine ⟨q,by omega,?_⟩
    intro D e' hD he
    have hb := subbudget hA le_rfl hD
    obtain ⟨a',s',ha,ra⟩ := Hq D e' hb he
    have hn := agree_down (show 1 ≤ L by omega) (result_depth_le hb ra)
    cases a' with
    | nil => exact ⟨.nil,_,.loop_nil ha,result_refl _ _ _ _⟩
    | cons a c => exact False.elim hn
  | @loop_stop e b r t hsub ih =>
    obtain ⟨q,hq,Hq⟩ := ih
    let H := height (.loop b)
    have hA : height b+1 ≤ H := by rfl
    have hA' : height b ≤ H := by omega
    refine ⟨q,by omega,?_⟩
    intro D e' hD he
    have hb := subbudget hA' le_rfl hD
    obtain ⟨a',s',ha,ra⟩ := Hq D e' hb he
    have hh := agree_down (show 2 ≤ L by omega) (result_depth_le hb ra)
    cases a' with
    | nil => exact False.elim hh
    | cons c d =>
      cases c with
      | nil =>
        have hm : H*q ≤ D := by
          change L+H*(q+1) ≤ D at hD
          rw [Nat.mul_add,Nat.mul_one] at hD
          omega
        exact ⟨d,_,.loop_stop ha,result_cons_tail hA hm ra⟩
      | cons x y => exact False.elim hh.1
  | @loop_step e b x y a r s t h1 h2 ih1 ih2 =>
    obtain ⟨q,hq,Hq⟩ := ih1
    obtain ⟨v,hv,Hv⟩ := ih2
    let H := height (.loop b)
    have hA : height b+1 ≤ H := by rfl
    have hA' : height b ≤ H := by omega
    refine ⟨q+v,by rw [Nat.add_mul]; omega,?_⟩
    intro D e' hD he
    have hb := subbudget hA' (show q ≤ q+v by omega) hD
    obtain ⟨a',s',ha,ra⟩ := Hq D e' hb he
    have hh := agree_down (show 2 ≤ L by omega) (result_depth_le hb ra)
    cases a' with
    | nil => exact False.elim hh
    | cons c d =>
      cases c with
      | nil => exact False.elim hh.1
      | cons x' y' =>
        have hm : H*q ≤ D := by
          change L+H*(q+v+1) ≤ D at hD
          have hle := Nat.mul_le_mul_left H (show q ≤ q+v+1 by omega)
          omega
        have rd := result_cons_tail hA hm ra
        obtain ⟨r',t',hr,rr⟩ := Hv (D-H*q) (d::e'.tail)
          (sequential_budget (A:=H) le_rfl hD)
          (env_cons rd.1 (env_tail (env_down (by omega) he)))
        exact ⟨r',_,.loop_step ha hr,result_after_seq (A:=H) le_rfl rr⟩


/-- A pure time bound for two genuinely distinct outputs. No space,
degree, communication, or strategy assumption is used. The static
height coefficient records the charged-copy model, not SAT hardness. -/
theorem different_runs_copy_lower {p : Prog} {a b r s : Data} {t u m : Nat}
    (hm : 3 ≤ m) (ha : Agree (2*m) a b) (hr : r.size ≤ m) (hne : r ≠ s)
    (hy : p.Runs a r t) (hn : p.Runs b s u) :
    m*m < height p * (t+m) := by
  obtain ⟨q,hq,h⟩ := eval_copy_budget hy m hm
  have hd : 2*m < m+height p*(q+1) := by
    by_contra hh
    have hbudget : m+height p*(q+1) ≤ 2*m := by omega
    obtain ⟨r',t',he,ha'⟩ := h (2*m) [b] hbudget
      (env_cons ha (fun i => agree_refl _ _))
    have hrr := agree_eq_of_size hr (result_depth_le hbudget ha')
    have hrs := (Eval.deterministic he hn).1
    exact hne (hrr.trans hrs)
  have hm' : m < height p*(q+1) := by omega
  calc m*m < (height p*(q+1))*m := Nat.mul_lt_mul_of_pos_right hm' (by omega)
    _ = height p*(q*m+m) := by rw [Nat.mul_assoc, Nat.add_mul, Nat.one_mul]
    _ ≤ height p*(t+m) := Nat.mul_le_mul_left _ (by omega)

end PNPAbove.WP36
