import PNPAbove.WP40Capacity
import MIPRE.Foundations.Halting.Descriptions

namespace PNPAbove.WP41
open MIPRE MIPRE.SAT MIPRE.Cost MIPRE.Cost.PolyTimeFun Polynomial

def Successful (f : Fml) (c : Prog) (w : BitStr) (t : Nat) : Prop :=
  c.WellScoped 1 ∧ c.Runs (encode f) (encode w) t ∧
    WP35.denseWitnessVerifier (f,w) = true

def score (c : Prog) (t : Nat) : Nat := 2^(esize c)*(t+1)

def Achieves (f : Fml) (n : Nat) : Prop :=
  ∃ c w t, Successful f c w t ∧ score c t = n

theorem const_success (f : Fml) (w : BitStr)
    (hw : WP35.denseWitnessVerifier (f,w) = true) :
    Successful f (.const (encode w)) w (esize w) :=
  ⟨trivial,Eval.const _ _,hw⟩

theorem achieved_iff_sat (f : Fml) : (∃ n, Achieves f n) ↔ WP38.Sat f := by
  constructor
  · rintro ⟨n,c,w,t,hw,_⟩
    exact WP35.denseWitnessVerifier_sound f w hw.2.2
  · intro hf
    obtain ⟨w,_,hw⟩ := (WP35.denseWitnessVerifier_source_length_iff f).2 hf
    exact ⟨_,_,_,_,const_success f w hw,rfl⟩

noncomputable def capacity (f : Fml) : Nat := by
  classical
  exact if h : ∃ n, Achieves f n then Nat.find h else 0

theorem capacity_achieved (f : Fml) (hf : WP38.Sat f) :
    Achieves f (capacity f) := by
  classical
  have h := (achieved_iff_sat f).2 hf
  simpa [capacity,h] using Nat.find_spec h

theorem capacity_le (f : Fml) (c : Prog) (w : BitStr) (t : Nat)
    (h : Successful f c w t) : capacity f ≤ score c t := by
  classical
  have hh : Achieves f (score c t) := ⟨c,w,t,h,rfl⟩
  have he : ∃ n, Achieves f n := ⟨_,hh⟩
  simpa [capacity,he] using Nat.find_min' he hh

theorem score_pos (c : Prog) (t : Nat) : 0 < score c t := by
  unfold score
  positivity

theorem capacity_pos (f : Fml) (hf : WP38.Sat f) : 0 < capacity f := by
  obtain ⟨c,w,t,_,he⟩ := capacity_achieved f hf
  rw [← he]
  exact score_pos c t

theorem capacity_zero_iff (f : Fml) : capacity f = 0 ↔ ¬ WP38.Sat f := by
  classical
  constructor
  · intro h hs
    exact (Nat.ne_of_gt (capacity_pos f hs)) h
  · intro h
    have hn : ¬ ∃ n, Achieves f n := fun he => h ((achieved_iff_sat f).1 he)
    simp [capacity,hn]

theorem esize_const (w : BitStr) :
    esize (Prog.const (encode w)) = esize w + 14 := by
  change (Prog.const (encode w)).toData.size = esize w + 14
  simp [Prog.toData,esize] <;> omega

theorem esize_let (c d : Prog) :
    esize (Prog.let_ c d) = esize c + esize d + 11 := by
  simp [Prog.esize_eq_size_toData,Prog.toData] <;> omega

/-- Charging only the sum of description length and runtime does not
prevent nonuniform hardcoding: every satisfiable input has a cheap run. -/
theorem additive_charge_collapses (f : Fml) (hf : WP38.Sat f) :
    ∃ c w t, Successful f c w t ∧ esize c+t ≤ 8*esize f+16 := by
  obtain ⟨w,hlen,hw⟩ := (WP35.denseWitnessVerifier_source_length_iff f).2 hf
  refine ⟨.const (encode w),w,esize w,const_success f w hw,?_⟩
  rw [esize_const]
  have h := esize_bitStr_le w
  omega

theorem successful_poly_bound (A : PolyTimeFun Fml BitStr) (f : Fml)
    (h : WP35.denseWitnessVerifier (f,A f) = true) :
    capacity f ≤ 2^(esize A.code)*(A.timeBound.eval (esize f)+1) := by
  obtain ⟨t,ht,hr⟩ := A.computes f
  exact (capacity_le f A.code (A f) t ⟨A.closed,hr,h⟩).trans
    (Nat.mul_le_mul_left _ (Nat.add_le_add_right ht 1))

theorem solver_capacity_polynomial (A : PolyTimeFun Fml BitStr)
    (hA : WP38.SolvesWitness A) :
    ∃ q : Polynomial Nat, ∀ f, WP38.Sat f → capacity f ≤ q.eval (esize f) := by
  refine ⟨C (2^(esize A.code)) * (A.timeBound + 1),?_⟩
  intro f hf
  simpa using successful_poly_bound A f (hA f hf)

theorem superpoly_excludes_solver
    (h : ∀ q : Polynomial Nat, ∃ f, WP38.Sat f ∧ q.eval (esize f) < capacity f) :
    ¬ ∃ A : PolyTimeFun Fml BitStr, WP38.SolvesWitness A := by
  rintro ⟨A,hA⟩
  obtain ⟨q,hq⟩ := solver_capacity_polynomial A hA
  obtain ⟨f,hf,hh⟩ := h q
  exact (Nat.not_lt_of_ge (hq f hf)) hh

theorem compose_success (f g : Fml) (c d : Prog) (w : BitStr) (s t : Nat)
    (hc : c.WellScoped 1) (hr : c.Runs (encode f) (encode g) s)
    (hd : Successful g d w t)
    (hlift : WP35.denseWitnessVerifier (g,w) = true →
      WP35.denseWitnessVerifier (f,w) = true) :
    Successful f (.let_ c d) w (s+t+1) := by
  refine ⟨⟨hc,hd.1.mono (by omega) d⟩,?_,hlift hd.2.2⟩
  exact Eval.let_ hr (Eval.append_of_wellScoped hd.2.1 hd.1 [encode f])

theorem score_compose (c d : Prog) (s t : Nat) :
    score (.let_ c d) (s+t+1) ≤ 2^(esize c+11)*(s+2)*score d t := by
  rw [score,esize_let,score]
  have hp : esize c + esize d + 11 = (esize c+11)+esize d := by omega
  rw [hp,pow_add]
  calc
    2^(esize c+11)*2^(esize d)*(s+t+1+1)
        ≤ 2^(esize c+11)*2^(esize d)*((s+2)*(t+1)) := by
      apply Nat.mul_le_mul_left
      nlinarith
    _ = _ := by ring

/-- Transport along an actual source execution, not mere equality of
truth functions. The witness lifting condition is explicit. -/
theorem capacity_transport (f g : Fml) (c : Prog) (s : Nat)
    (hc : c.WellScoped 1) (hr : c.Runs (encode f) (encode g) s)
    (hg : WP38.Sat g)
    (hlift : ∀ w, WP35.denseWitnessVerifier (g,w) = true →
      WP35.denseWitnessVerifier (f,w) = true) :
    capacity f ≤ 2^(esize c+11)*(s+2)*capacity g := by
  obtain ⟨d,w,t,hd,he⟩ := capacity_achieved g hg
  rw [← he]
  exact (capacity_le f _ w _ (compose_success f g c d w s t hc hr hd (hlift w))).trans
    (score_compose c d s t)

theorem tag_transport (f : Fml) (b : BitStr) (c : Prog) (s : Nat)
    (hc : c.WellScoped 1) (hr : c.Runs (encode f) (encode (WP40.tag f b)) s)
    (hf : WP38.Sat f) :
    capacity f ≤ 2^(esize c+11)*(s+2)*capacity (WP40.tag f b) := by
  apply capacity_transport f _ c s hc hr
  · obtain ⟨a,ha⟩ := hf
    exact ⟨a,(WP40.tag_eval f b a).trans ha⟩
  · intro w hw
    rwa [WP40.tag_verifier] at hw

theorem score_budget_bounds (c : Prog) (t B : Nat) (h : score c t ≤ B) :
    2^(esize c) ≤ B ∧ t+1 ≤ B := by
  unfold score at h
  have hp : 0 < 2^(esize c) := by positivity
  constructor
  · exact (Nat.le_mul_of_pos_right _ (by omega)).trans h
  · exact (Nat.le_mul_of_pos_left _ hp).trans h

end PNPAbove.WP41
