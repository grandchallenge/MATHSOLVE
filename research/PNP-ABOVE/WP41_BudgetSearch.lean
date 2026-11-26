import PNPAbove.WP41Weighted
import MIPRE.Foundations.CL.DetypingClock

namespace PNPAbove.WP41
open MIPRE MIPRE.SAT MIPRE.Cost Polynomial

def words : Nat → List BitStr
  | 0 => [[]]
  | n+1 => (words n).map (false :: ·) ++ (words n).map (true :: ·)

theorem words_length (n : Nat) : (words n).length = 2^n := by
  induction n with
  | zero => rfl
  | succ n ih => simp [words,ih,pow_succ]; omega

theorem mem_words (n : Nat) (b : BitStr) : b ∈ words n ↔ b.length = n := by
  induction n generalizing b with
  | zero => simp [words]
  | succ n ih =>
    cases b with
    | nil => simp [words]
    | cons bit b =>
      cases bit <;> simp [words,List.mem_map,ih]

def shortWords : Nat → List BitStr
  | 0 => words 0
  | n+1 => shortWords n ++ words (n+1)

theorem shortWords_length (n : Nat) : (shortWords n).length + 1 = 2^(n+1) := by
  induction n with
  | zero => rfl
  | succ n ih =>
    simp only [shortWords,List.length_append,words_length,pow_succ] at *
    omega

theorem mem_shortWords (n : Nat) (b : BitStr) :
    b ∈ shortWords n ↔ b.length ≤ n := by
  induction n with
  | zero => simp [shortWords,mem_words]
  | succ n ih =>
    simp only [shortWords,List.mem_append,ih,mem_words]
    omega

def codeWords (B : Nat) : List BitStr := shortWords B.log2

theorem codeWords_length (B : Nat) (hB : 0 < B) :
    (codeWords B).length < 2*B := by
  have h := shortWords_length B.log2
  have hp := (Nat.le_log2 (by omega : B ≠ 0)).1 (le_refl B.log2)
  unfold codeWords
  rw [pow_succ] at h
  omega

theorem candidate_present (c : Prog) (t B : Nat) (h : score c t ≤ B) :
    (encode c : Data).toBitsPost ∈ codeWords B := by
  have hb := (score_budget_bounds c t B h).1
  have hp : 0 < 2^(esize c) := by positivity
  have hB : B ≠ 0 := by omega
  apply (mem_shortWords _ _).2
  rw [Data.length_toBitsPost]
  exact (Nat.le_log2 hB).2 hb

/-- The clock for each code length. The +1 in the score is charged too. -/
def allowance (B n : Nat) : Nat := B / 2^n

theorem score_iff_allowance (c : Prog) (t B : Nat) :
    score c t ≤ B ↔ t+1 ≤ allowance B (esize c) := by
  unfold score allowance
  rw [Nat.le_div_iff_mul_le (by positivity)]
  rw [Nat.mul_comm]

theorem allowance_per_level (B n : Nat) :
    (words n).length * allowance B n ≤ B := by
  rw [words_length,allowance,Nat.mul_comm]
  exact Nat.div_mul_le_self B _

def totalAllowance (B : Nat) : Nat → Nat
  | 0 => (words 0).length * allowance B 0
  | n+1 => totalAllowance B n + (words (n+1)).length * allowance B (n+1)

theorem totalAllowance_le (B n : Nat) : totalAllowance B n ≤ B*(n+1) := by
  induction n with
  | zero => simpa [totalAllowance] using allowance_per_level B 0
  | succ n ih =>
    have h := allowance_per_level B (n+1)
    rw [totalAllowance,Nat.mul_succ]
    omega

/-- Finite budget test defined using the exact clocked result. Malformed
and noncanonical programs, invalid scope and rejected witnesses are ignored.
This is a mathematical search specification, not yet a native compiled PTF. -/
noncomputable def attempt (f : Fml) (B : Nat) (bits : BitStr) : Option BitStr := by
  classical
  exact match Prog.ofData (Data.parse bits) with
    | none => none
    | some c =>
      if (encode c : Data).toBitsPost = bits ∧ c.WellScoped 1 ∧
          2^(esize c) ≤ B then
        match evalWithin c (encode f) (allowance B (esize c)-1) with
        | none => none
        | some r =>
          match (SizedEncoding.decode r : Option BitStr) with
          | none => none
          | some w =>
            if r = encode w ∧ WP35.denseWitnessVerifier (f,w) = true then some w else none
      else none

theorem attempt_complete (f : Fml) (c : Prog) (w : BitStr) (t B : Nat)
    (hs : Successful f c w t) (hb : score c t ≤ B) :
    attempt f B (encode c : Data).toBitsPost = some w := by
  classical
  have hclock := (score_iff_allowance c t B).1 hb
  have hr : evalWithin c (encode f) (allowance B (esize c)-1) = some (encode w) :=
    (MIPRE.CL.Detyping.ClockProgram.evalWithin_eq_some_iff _ _ _ _).2 ⟨t,by omega,hs.2.1⟩
  simp [attempt,Data.parse_toBitsPost,
    show Prog.ofData (encode c) = some c from SizedEncoding.decode_encode c,
    hs.1,(score_budget_bounds c t B hb).1,hr,SizedEncoding.decode_encode,hs.2.2]

theorem attempt_sound (f : Fml) (B : Nat) (bits w : BitStr)
    (h : attempt f B bits = some w) :
    ∃ c t, Successful f c w t ∧ score c t ≤ B := by
  classical
  unfold attempt at h
  cases hc : Prog.ofData (Data.parse bits) with
  | none => simp [hc] at h
  | some c =>
    simp only [hc] at h
    split at h
    · rename_i hguard
      cases hr : evalWithin c (encode f) (allowance B (esize c)-1) with
      | none => simp [hr] at h
      | some r =>
        simp only [hr] at h
        cases hw : (SizedEncoding.decode r : Option BitStr) with
        | none => simp [hw] at h
        | some b =>
          simp only [hw] at h
          split at h
          · rename_i hv
            have he := Option.some.inj h
            subst b
            obtain ⟨t,ht,htRun⟩ := (MIPRE.CL.Detyping.ClockProgram.evalWithin_eq_some_iff _ _ _ _).1 hr
            have hpos : 0 < allowance B (esize c) :=
              Nat.lt_of_lt_of_le (by decide : 0 < 1)
                ((Nat.le_div_iff_mul_le (by positivity)).2 (by simpa using hguard.2.2))
            refine ⟨c,t,⟨hguard.2.1,?_,hv.2⟩,(score_iff_allowance _ _ _).2 (by omega)⟩
            simpa [hv.1] using htRun
          · simp at h
    · simp at h

noncomputable def candidates (f : Fml) (B : Nat) : List BitStr :=
  (codeWords B).filterMap (attempt f B)

theorem candidates_sound (f : Fml) (B : Nat) (w : BitStr)
    (hw : w ∈ candidates f B) :
    WP35.denseWitnessVerifier (f,w) = true ∧ capacity f ≤ B := by
  obtain ⟨bits,_,he⟩ := List.mem_filterMap.mp hw
  obtain ⟨c,t,hs,hb⟩ := attempt_sound f B bits w he
  exact ⟨hs.2.2,(capacity_le f c w t hs).trans hb⟩

theorem candidates_complete (f : Fml) (B : Nat) (hf : WP38.Sat f)
    (hB : capacity f ≤ B) :
    ∃ w, w ∈ candidates f B := by
  obtain ⟨c,w,t,hs,he⟩ := capacity_achieved f hf
  have hb : score c t ≤ B := he.symm ▸ hB
  exact ⟨w,List.mem_filterMap.mpr ⟨_,candidate_present c t B hb,
    attempt_complete f c w t B hs hb⟩⟩

theorem candidates_iff (f : Fml) (B : Nat) :
    (∃ w, w ∈ candidates f B) ↔ WP38.Sat f ∧ capacity f ≤ B := by
  constructor
  · rintro ⟨w,hw⟩
    obtain ⟨hv,hb⟩ := candidates_sound f B w hw
    exact ⟨WP35.denseWitnessVerifier_sound f w hv,hb⟩
  · rintro ⟨hf,hb⟩
    exact candidates_complete f B hf hb

end PNPAbove.WP41
