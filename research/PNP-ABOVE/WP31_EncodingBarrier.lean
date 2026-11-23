import PNPAbove.WP30Classical
import MIPRE.Foundations.SAT.FmlProg

/-!
WP31: Representation-independent obstruction for faithful SAT source
formula encodings into ONE NUMERIC game index. This is finite counting,
not classical SAT hardness or P != NP.
-/
namespace PNPAbove.WP31
open MIPRE MIPRE.SAT MIPRE.Cost

/-- Two genuinely different signed occurrences of the same SAT input. -/
def signedAtom (b : Bool) : Fml :=
  if b then .inp 0 else .not (.inp 0)

/-- Every bitstring gives one syntactically different SAT source formula. -/
def signedConjunction : List Bool → Fml
  | [] => .const true
  | b :: bs => .and (signedAtom b) (signedConjunction bs)

/-- The formula encodes its bitstring without any collision. -/
theorem signedConjunction_injective : Function.Injective signedConjunction := by
  intro s t heq
  induction s generalizing t with
  | nil =>
      cases t with
      | nil => rfl
      | cons b bs =>
          simp [signedConjunction] at heq
  | cons b bs ih =>
      cases t with
      | nil =>
          simp [signedConjunction] at heq
      | cons c cs =>
          have ha : signedAtom b = signedAtom c := by
            exact (Fml.and.inj heq).1
          have ht : signedConjunction bs = signedConjunction cs := by
            simpa only [signedConjunction] using (Fml.and.inj heq).2
          have hb : b = c := by
            cases b <;> cases c <;> simp_all [signedAtom]
          subst c
          have hbc := ih ht
          simp [hbc]

/-- Exact source Fml node count is linear in the encoded bitstring. -/
theorem signedConjunction_size_le (bs : List Bool) :
    (signedConjunction bs).size ≤ 3 * bs.length + 1 := by
  induction bs with
  | nil => simp [signedConjunction, Fml.size]
  | cons b bs ih =>
      cases b <;> simp [signedConjunction, signedAtom, Fml.size] <;> omega

/-- Even the ORIGINAL full encoded source Data size has a uniform
linear bound, not only the number of abstract formula nodes. -/
theorem signedConjunction_source_size_le (bs : List Bool) :
    esize (signedConjunction bs) ≤
       (esize (Fml.inp 0) + 19) * bs.length + esize (Fml.const true) := by
  induction bs with
  | nil => simp [signedConjunction]
  | cons b bs ih =>
      cases b with
      | false =>
          change esize (Fml.and (Fml.not (Fml.inp 0)) (signedConjunction bs)) ≤
            (esize (Fml.inp 0) + 19) * (bs.length + 1) + esize (Fml.const true)
          rw [esize_and_fml, esize_not_fml, Nat.mul_succ]
          omega
      | true =>
          change esize (Fml.and (Fml.inp 0) (signedConjunction bs)) ≤
            (esize (Fml.inp 0) + 19) * (bs.length + 1) + esize (Fml.const true)
          rw [esize_and_fml, Nat.mul_succ]
          omega

/-- Exactly 2^r distinguishable original source SAT formulas of
O(r) binary-coded source length. -/
def formulaFamily (r : Nat) (xs : Fin r → Bool) : Fml :=
  signedConjunction (List.ofFn xs)

theorem formulaFamily_injective (r : Nat) :
    Function.Injective (formulaFamily r) := by
  intro a b h
  exact List.ofFn_injective (signedConjunction_injective h)

theorem formulaFamily_source_size_le (r : Nat) (xs : Fin r → Bool) :
    esize (formulaFamily r xs) ≤
      (esize (Fml.inp 0) + 19) * r + esize (Fml.const true) := by
  simpa [formulaFamily] using signedConjunction_source_size_le (List.ofFn xs)

/-- General finite pigeonhole barrier: any injection of a family of
2^r distinct inputs into Nat has an output >= 2^r-1. -/
theorem injective_index_exponential (r : Nat)
    (enc : (Fin r → Bool) → Nat) (hinj : Function.Injective enc) :
    ∃ xs, 2 ^ r ≤ enc xs + 1 := by
  by_contra h
  have hsmall : ∀ xs, enc xs < 2 ^ r - 1 := by
    intro xs
    have hn : ¬ 2 ^ r ≤ enc xs + 1 := by
      intro hb
      exact h ⟨xs, hb⟩
    omega
  let restricted : (Fin r → Bool) → Fin (2 ^ r - 1) :=
    fun xs => ⟨enc xs, hsmall xs⟩
  have hrestr : Function.Injective restricted := by
    intro xs ys heq
    exact hinj (congrArg Fin.val heq)
  have hc := Fintype.card_le_of_injective restricted hrestr
  have hpos : 0 < 2 ^ r := pow_pos (by omega : 0 < (2 : Nat)) _
  simp only [Fintype.card_fun, Fintype.card_bool, Fintype.card_fin] at hc
  omega

/-- An arbitrary faithful lossless encoder to ONE numeric native game
index must be exponentially large on some linearly sized source SAT
formula. This works for ALL encodings, not only WP29's serializer. -/
theorem faithful_index_exponential (r : Nat)
    (enc : Fml → Nat) (hinj : Function.Injective enc) :
    ∃ xs : Fin r → Bool, 2 ^ r ≤ enc (formulaFamily r xs) + 1 := by
  apply injective_index_exponential r (enc ∘ formulaFamily r)
  exact hinj.comp (formulaFamily_injective r)

/-- Recovering the original source formula from its numeric index
implies injectivity, so *every* lossless decoder faces the obstruction. -/
theorem lossless_decoder_exponential (r : Nat)
    (enc : Fml → Nat) (decode : Nat → Fml)
    (hroundtrip : ∀ f, decode (enc f) = f) :
    ∃ xs : Fin r → Bool, 2 ^ r ≤ enc (formulaFamily r xs) + 1 := by
  apply faithful_index_exponential r enc
  intro f g heq
  have h := congrArg decode heq
  simpa only [hroundtrip] using h

/-! ## Exact scope: a SAT-label-only encoding CAN use one bit.
This noncomputable construction illustrates why counting alone cannot
separate P from NP: the difficulty is in COMPUTING the label. -/

/-- A one-bit semantic SAT encoding. This is a mathematical definition,
NOT an original Cost.Prog/polytime algorithm for SAT. -/
noncomputable def satisfiableLabel (m : Nat) (f : Fml) : Nat := by
  classical
  exact if PNPAbove.WP24.Satisfiable m f then 1 else 0

theorem satisfiableLabel_le_one (m : Nat) (f : Fml) :
    satisfiableLabel m f ≤ 1 := by
  classical
  unfold satisfiableLabel
  split_ifs <;> omega

theorem satisfiableLabel_exact (m : Nat) (f : Fml) :
    satisfiableLabel m f = 1 ↔ PNPAbove.WP24.Satisfiable m f := by
  classical
  simp [satisfiableLabel]

end PNPAbove.WP31
