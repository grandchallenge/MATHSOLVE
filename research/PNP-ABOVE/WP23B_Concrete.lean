import PNPAbove.WP23BCharacterization
import MIPRE.TM.CookLevin.Assemble

/-!
Concrete instantiation of the universally proved WP23B source-SAT bridge
using the ACTUAL inhabited pinned original MIPRE succinct Cook--Levin
program (not a field of an assumed, uninhabited record).
-/
namespace PNPAbove.WP23B
open MIPRE MIPRE.Cost PNPAbove.WP21
open scoped Classical
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-- The source-native real polynomial-time succinct SAT circuit. -/
noncomputable def nativeCircuit (n T Q σ : Nat) (x y : BitStr) : SAT.Circuit :=
  nativeCircuitWith SAT.succinctCookLevin n T Q σ x y

/-- Actual pinned original generated 3CNF tape-prefix satisfiability. -/
def NativeSat (n T Q σ : Nat) (x y : BitStr)
    (A B : Fin (2 * T) → Bool) : Prop :=
  NativeSatWith SAT.succinctCookLevin n T Q σ x y A B

/-- The original Cook--Levin instance has an exact original
source-parameterized question and answer acceptance correspondence. -/
theorem native_sat_iff_timed_source (n T Q σ : Nat) (x y : BitStr)
    (hV : SAT.Valid maskedParityDecider.prog n T Q σ x y)
    (A B : Fin (2 * T) → Bool) :
    NativeSat n T Q σ x y A B ↔
      SAT.EncodesAccepted maskedParityDecider n x y T A B :=
  nativeSatWith_iff_timed_answers SAT.succinctCookLevin n T Q σ x y hV A B

/-- Original constructed describer has exact arity. -/
theorem native_real_circuit_arity (n T Q σ : Nat) (x y : BitStr) :
    (nativeCircuit n T Q σ x y).inputs =
      3 * SAT.succinctCookLevin.m T σ + 3 :=
  nativeCircuitWith_inputs SAT.succinctCookLevin n T Q σ x y

/-- Original constructed describer is a well-formed circuit. -/
theorem native_real_circuit_wellFormed (n T Q σ : Nat) (x y : BitStr) :
    (nativeCircuit n T Q σ x y).WellFormed :=
  nativeCircuitWith_wellFormed SAT.succinctCookLevin n T Q σ x y

/-- The size of the executable original construction obeys its
published, source-pinned polynomial gate bound under SAT.Valid. -/
theorem native_real_circuit_gate_bound (n T Q σ : Nat) (x y : BitStr)
    (hV : SAT.Valid maskedParityDecider.prog n T Q σ x y) :
    (nativeCircuit n T Q σ x y).size ≤
      SAT.succinctCookLevin.s n T Q σ :=
  nativeCircuitWith_gate_bound SAT.succinctCookLevin n T Q σ x y hV

/-- Main theorem: original source-native real succinct 3CNF satisfiable
iff five trivially decidable mask and format conditions. This is a
negative hardness-transfer result, NOT a SAT lower bound. -/
theorem native_cnf_sat_iff_mask (n : Nat) (x y : BitStr) :
    (∃ A B : Fin (2 * canonicalTime n x y) → Bool,
       NativeSat n (canonicalTime n x y) (max x.length y.length)
         (esize maskedParityDecider.prog) x y A B) ↔
      n ≠ 0 ∧ x.length = 9 ∧ y.length = 9 ∧
        x[8]! = false ∧ y[0]! = false :=
  native_cnf_sat_iff_mask_with SAT.succinctCookLevin n x y

end PNPAbove.WP23B
