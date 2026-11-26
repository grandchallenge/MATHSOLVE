import MathSolve.PNP.ModelBridgeClosure

/-!
# NP verifier bridge: encoding and witness semantics
Source lock: Formal Conjectures 85f863718beeec7b58a3a1926ee92e3472bc2020,
PvsNP.lean and FormalConjecturesForMathlib/Computability/Encoding.lean.
The three-symbol upstream alphabet is not binary. The machine-level
transport and polynomial witness guard remain separate obligations.
-/
namespace MathSolve.PNP

abbrev BinaryPair := List Bool × List Bool
def importedPairEncode (z : BinaryPair) : List (Option Bool) :=
  z.1.map some ++ [none] ++ z.2.map some

def pairDataBits : List Bool → List Bool
  | [] => []
  | b :: bs => false :: b :: pairDataBits bs

/-- Fixed two-bit blocks: 00/01 data, 10 delimiter, 11 invalid. -/
def programmePairEncode (z : BinaryPair) : List Bool :=
  pairDataBits z.1 ++ [true, false] ++ pairDataBits z.2

def pairSymbolBits : Option Bool → List Bool
  | none => [true, false]
  | some b => [false, b]

theorem pairDataBits_length (xs : List Bool) :
    (pairDataBits xs).length = 2 * xs.length := by
  induction xs with
  | nil => rfl
  | cons b bs ih => simp [pairDataBits, ih]; omega

theorem pairDataBits_flatMap (xs : List Bool) :
    pairDataBits xs = (xs.map some).flatMap pairSymbolBits := by
  induction xs with
  | nil => rfl
  | cons b bs ih => simp [pairDataBits, pairSymbolBits, ih]

theorem programmePairEncode_from_imported (z : BinaryPair) :
    programmePairEncode z = (importedPairEncode z).flatMap pairSymbolBits := by
  simp [programmePairEncode, importedPairEncode, List.flatMap_append,
    pairDataBits_flatMap, pairSymbolBits]

theorem importedPairEncode_length (z : BinaryPair) :
    (importedPairEncode z).length = z.1.length + z.2.length + 1 := by
  simp [importedPairEncode]; omega

theorem programmePairEncode_length (z : BinaryPair) :
    (programmePairEncode z).length = 2 * (z.1.length + z.2.length + 1) := by
  simp [programmePairEncode, pairDataBits_length]; omega

def decodePairData : List Bool → Option (List Bool)
  | [] => some []
  | false :: b :: bs => (decodePairData bs).map (b :: ·)
  | _ => none

def decodePairRaw : List Bool → Option BinaryPair
  | true :: false :: bs => (decodePairData bs).map (fun y => ([], y))
  | false :: b :: bs => (decodePairRaw bs).map (fun z => (b :: z.1, z.2))
  | _ => none

theorem decodePairData_encode (xs : List Bool) :
    decodePairData (pairDataBits xs) = some xs := by
  induction xs with
  | nil => rfl
  | cons b bs ih => simp [pairDataBits, decodePairData, ih]

theorem decodePairRaw_encode (x y : List Bool) :
    decodePairRaw (programmePairEncode (x,y)) = some (x,y) := by
  induction x with
  | nil => simp [programmePairEncode, pairDataBits, decodePairRaw, decodePairData_encode]
  | cons b bs ih =>
    change (decodePairRaw (programmePairEncode (bs,y))).map
      (fun z => (b :: z.1, z.2)) = some (b :: bs,y)
    rw [ih]
    rfl

/-- Total decoder with explicit re-encoding validation. -/
def programmePairDecode (s : List Bool) : Option BinaryPair :=
  match decodePairRaw s with
  | none => none
  | some z => if programmePairEncode z = s then some z else none

theorem programmePairDecode_encode (z : BinaryPair) :
    programmePairDecode (programmePairEncode z) = some z := by
  rcases z with ⟨x,y⟩
  simp [programmePairDecode, decodePairRaw_encode]

theorem programmePairDecode_sound {s : List Bool} {z : BinaryPair}
    (h : programmePairDecode s = some z) : programmePairEncode z = s := by
  cases hr : decodePairRaw s with
  | none => simp [programmePairDecode, hr] at h
  | some q =>
    by_cases he : programmePairEncode q = s
    · have hq : q = z := by simpa [programmePairDecode, hr, he] using h
      exact hq ▸ he
    · simp [programmePairDecode, hr, he] at h

theorem programmePairDecode_none_iff (s : List Bool) :
    programmePairDecode s = none ↔ ¬ ∃ z, programmePairEncode z = s := by
  constructor
  · intro h ⟨z,hz⟩
    rw [← hz, programmePairDecode_encode] at h
    contradiction
  · intro h
    cases hd : programmePairDecode s with
    | none => rfl
    | some z => exact False.elim (h ⟨z,programmePairDecode_sound hd⟩)

theorem programmePairEncode_injective : Function.Injective programmePairEncode := by
  intro z q h
  have hh := congrArg programmePairDecode h
  rw [programmePairDecode_encode, programmePairDecode_encode] at hh
  exact Option.some.inj hh

def binaryPairVerifier (R : BinaryPair → Bool) (s : List Bool) : Bool :=
  match programmePairDecode s with
  | none => false
  | some z => R z

theorem binaryPairVerifier_encode (R : BinaryPair → Bool) (z : BinaryPair) :
    binaryPairVerifier R (programmePairEncode z) = R z := by
  simp [binaryPairVerifier, programmePairDecode_encode]

theorem binaryPairVerifier_rejects_malformed (R : BinaryPair → Bool)
    (s : List Bool) (h : programmePairDecode s = none) :
    binaryPairVerifier R s = false := by simp [binaryPairVerifier, h]

theorem binaryPairVerifier_roundtrip (V : List Bool → Bool)
    (h : ∀ s, programmePairDecode s = none → V s = false) :
    binaryPairVerifier (fun z => V (programmePairEncode z)) = V := by
  funext s
  unfold binaryPairVerifier
  cases hd : programmePairDecode s with
  | none => exact (h s hd).symm
  | some z => exact congrArg V (programmePairDecode_sound hd)

def ImportedPairVerifierPoly (R : BinaryPair → Bool) : Prop :=
  Nonempty (Turing.TM2ComputableInPolyTime importedPairEncode Computability.encodeBool R)

def ImportedNPDecision (L : List Bool → Bool) : Prop :=
  ∃ p : Polynomial Nat, ∃ R : BinaryPair → Bool,
    ImportedPairVerifierPoly R ∧
    ∀ x, L x = true ↔ ∃ w : List Bool, w.length ≤ p.eval x.length ∧ R (x,w) = true

/-- Fixed polynomial witness bound, total binary verifier, malformed-to-NO. -/
def ProgrammeNPDecision (L : List Bool → Bool) : Prop :=
  ∃ d c k : Nat, ∃ V : List Bool → Bool,
    ProgrammeComputableInPolyTime V ∧
    (∀ s, programmePairDecode s = none → V s = false) ∧
    ∀ x, L x = true ↔ ∃ w : List Bool,
      w.length ≤ d + c * x.length ^ k ∧ V (programmePairEncode (x,w)) = true

/-- Enlarging a witness cap without checking the original cap is unsound. -/
def guardPairWitness (p : Polynomial Nat) (R : BinaryPair → Bool) (z : BinaryPair) : Bool :=
  if z.2.length ≤ p.eval z.1.length then R z else false

theorem guardPairWitness_true (p : Polynomial Nat) (R : BinaryPair → Bool)
    (x w : List Bool) :
    guardPairWitness p R (x,w) = true ↔ w.length ≤ p.eval x.length ∧ R (x,w) = true := by
  unfold guardPairWitness
  by_cases h : w.length ≤ p.eval x.length <;> simp [h]

theorem witnessPolynomial_majorant (p : Polynomial Nat) (n : Nat) :
    p.eval n ≤ p.eval 0 + p.eval 1 * n ^ p.natDegree := by
  cases n with
  | zero => exact Nat.le_add_right _ _
  | succ n => exact (polynomial_eval_le_eval_one_mul_pow_natDegree p (by omega)).trans (Nat.le_add_left _ _)

/-- Still-open machine-level transport, not merely a coding identity. -/
def PairVerifierAlphabetBridge : Prop :=
  ∀ R : BinaryPair → Bool,
    ImportedPairVerifierPoly R ↔ ProgrammeComputableInPolyTime (binaryPairVerifier R)

/-- Still-open polynomial-time closure under the exact witness-length guard. -/
def PairVerifierGuardClosure : Prop :=
  ∀ (p : Polynomial Nat) (R : BinaryPair → Bool),
    ImportedPairVerifierPoly R → ImportedPairVerifierPoly (guardPairWitness p R)

theorem importedNP_iff_programmeNP_of_verifier_contracts
    (alphabet : PairVerifierAlphabetBridge) (guard : PairVerifierGuardClosure)
    (L : List Bool → Bool) : ImportedNPDecision L ↔ ProgrammeNPDecision L := by
  constructor
  · rintro ⟨p,R,hR,hL⟩
    refine ⟨p.eval 0,p.eval 1,p.natDegree,binaryPairVerifier (guardPairWitness p R),
      (alphabet _).mp (guard p R hR), binaryPairVerifier_rejects_malformed _, ?_⟩
    intro x
    rw [hL x]
    constructor
    · rintro ⟨w,hw,haccept⟩
      exact ⟨w,hw.trans (witnessPolynomial_majorant p x.length),
        (binaryPairVerifier_encode _ _).trans ((guardPairWitness_true p R x w).mpr ⟨hw,haccept⟩)⟩
    · rintro ⟨w,_,hw⟩
      rw [binaryPairVerifier_encode] at hw
      exact ⟨w,(guardPairWitness_true p R x w).mp hw⟩
  · rintro ⟨d,c,k,V,hV,hmal,hL⟩
    let R : BinaryPair → Bool := fun z => V (programmePairEncode z)
    refine ⟨Polynomial.C d + Polynomial.C c * Polynomial.X ^ k,R, ?_, ?_⟩
    · apply (alphabet R).mpr
      rw [binaryPairVerifier_roundtrip V hmal]
      exact hV
    · intro x
      simpa [R] using hL x

#print axioms programmePairEncode_from_imported
#print axioms programmePairEncode_length
#print axioms programmePairDecode_encode
#print axioms programmePairDecode_sound
#print axioms programmePairDecode_none_iff
#print axioms binaryPairVerifier_roundtrip
#print axioms guardPairWitness_true
#print axioms witnessPolynomial_majorant
#print axioms importedNP_iff_programmeNP_of_verifier_contracts

/-- The locked certificate definition permits an arbitrary fixed polynomial.
This is the primary Programme formulation; the earlier monomial-plus-constant
presentation is a further normalization, not an additional lock requirement. -/
def ProgrammeNPPolynomialDecision (L : List Bool → Bool) : Prop :=
  ∃ p : Polynomial Nat, ∃ V : List Bool → Bool,
    ProgrammeComputableInPolyTime V ∧
    (∀ s, programmePairDecode s = none → V s = false) ∧
    ∀ x, L x = true ↔ ∃ w : List Bool,
      w.length ≤ p.eval x.length ∧ V (programmePairEncode (x,w)) = true

/-- The remaining alphabet adapter can be proved wholly within FinTM2;
the admitted binary machine-model bridge then supplies Programme transfer. -/
def PairVerifierTM2AlphabetBridge : Prop :=
  ∀ R : BinaryPair → Bool,
    ImportedPairVerifierPoly R ↔ ImportedTM2ComputableInPolyTime (binaryPairVerifier R)

theorem pairVerifierAlphabetBridge_iff_tm2 :
    PairVerifierAlphabetBridge ↔ PairVerifierTM2AlphabetBridge := by
  constructor
  · intro h R
    exact (h R).trans (importedTM2_iff_programmePolyTime_constructive _).symm
  · intro h R
    exact (h R).trans (importedTM2_iff_programmePolyTime_constructive _)

theorem importedNP_iff_programmeNPPolynomial_of_alphabet
    (alphabet : PairVerifierAlphabetBridge) (L : List Bool → Bool) :
    ImportedNPDecision L ↔ ProgrammeNPPolynomialDecision L := by
  constructor
  · rintro ⟨p,R,hR,hL⟩
    refine ⟨p,binaryPairVerifier R,(alphabet R).mp hR,
      binaryPairVerifier_rejects_malformed R,?_⟩
    intro x
    simpa only [binaryPairVerifier_encode] using hL x
  · rintro ⟨p,V,hV,hmal,hL⟩
    let R : BinaryPair → Bool := fun z => V (programmePairEncode z)
    refine ⟨p,R,?_,?_⟩
    · apply (alphabet R).mpr
      rw [binaryPairVerifier_roundtrip V hmal]
      exact hV
    · intro x
      exact hL x

/-- A larger cap may admit a witness previously excluded, even when the
acceptance rule is unchanged. This is why widening alone is invalid. -/
theorem witness_cap_widening_counterexample :
    (¬ ∃ w : List Bool, w.length ≤ 0 ∧ w.length = 1) ∧
      (∃ w : List Bool, w.length ≤ 1 ∧ w.length = 1) := by
  constructor
  · rintro ⟨w,h0,h1⟩
    omega
  · exact ⟨[false],by decide, rfl⟩

#print axioms pairVerifierAlphabetBridge_iff_tm2
#print axioms importedNP_iff_programmeNPPolynomial_of_alphabet
#print axioms witness_cap_widening_counterexample

end MathSolve.PNP
