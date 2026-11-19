import PNPAbove.WP20Parity

namespace PNPAbove.WP20
open MIPRE MIPRE.CL MIPRE.Cost Matrix Finset
open scoped Classical

abbrev QMat := Matrix (Fin 2) (Fin 2) ℂ

/-- Center setting is the Z-basis rank-one projector. -/
def pCenter : QMat := !![1, 0; 0, 0]

/-- Rational Pythagorean qubit setting at Bloch vector (4/5,0,3/5). -/
noncomputable def pAlice : QMat :=
  !![(4:ℂ)/5, (2:ℂ)/5; (2:ℂ)/5, (1:ℂ)/5]

/-- Opposite rational qubit setting at Bloch vector (-4/5,0,3/5). -/
noncomputable def pBob : QMat :=
  !![(4:ℂ)/5, -(2:ℂ)/5; -(2:ℂ)/5, (1:ℂ)/5]

theorem pCenter_selfAdjoint : star pCenter = pCenter := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [pCenter, Matrix.star_apply]

theorem pAlice_selfAdjoint : star pAlice = pAlice := by
  ext i j
  fin_cases i <;> fin_cases j <;> norm_num [pAlice, Matrix.star_apply]

theorem pBob_selfAdjoint : star pBob = pBob := by
  ext i j
  fin_cases i <;> fin_cases j <;> norm_num [pBob, Matrix.star_apply]

theorem pCenter_projective : pCenter * pCenter = pCenter := by
  ext i j
  fin_cases i <;> fin_cases j <;> norm_num [pCenter, Matrix.mul_apply]

theorem pAlice_projective : pAlice * pAlice = pAlice := by
  ext i j
  fin_cases i <;> fin_cases j <;> norm_num [pAlice, Matrix.mul_apply]

theorem pBob_projective : pBob * pBob = pBob := by
  ext i j
  fin_cases i <;> fin_cases j <;> norm_num [pBob, Matrix.mul_apply]

/-- A source question is used as a center, Alice-private or Bob-private
setting. No supported source question ever requires both private settings. -/
noncomputable def selectedProjector (x : Questions) : QMat :=
  if x 0 = 1 then pAlice else if x 8 = 1 then pBob else pCenter

theorem selected_selfAdjoint (x : Questions) :
    star (selectedProjector x) = selectedProjector x := by
  unfold selectedProjector
  split_ifs <;> simp [pAlice_selfAdjoint, pBob_selfAdjoint, pCenter_selfAdjoint]

theorem selected_projective (x : Questions) :
    selectedProjector x * selectedProjector x = selectedProjector x := by
  unfold selectedProjector
  split_ifs <;> simp [pAlice_projective, pBob_projective, pCenter_projective]

/-- Actual two-outcome projective source measurement; answers are binary. -/
noncomputable def measured (x : Questions) (a : Bool) : QMat :=
  if a then 1 - selectedProjector x else selectedProjector x

theorem measured_selfAdjoint (x : Questions) (a : Bool) :
    star (measured x a) = measured x a := by
  cases a
  · exact selected_selfAdjoint x
  · simp [measured, map_sub, selected_selfAdjoint]

theorem measured_projective (x : Questions) (a : Bool) :
    measured x a * measured x a = measured x a := by
  cases a
  · exact selected_projective x
  · simp only [measured, if_true]
    have h := selected_projective x
    calc
      (1-selectedProjector x) * (1-selectedProjector x) =
        1 - selectedProjector x - selectedProjector x +
          (selectedProjector x * selectedProjector x) := by noncomm_ring
      _ = 1-selectedProjector x := by rw [h]; abel

theorem measured_normalized (x : Questions) :
    ∑ a : Bool, measured x a = (1 : QMat) := by
  simp [Fintype.sum_bool, measured]

/-- A genuine two-dimensional quantum synchronous measurement family, not
an independent scalar correlation table. -/
noncomputable def quantumMeasurement : ProjectiveMeasurement Questions Bool QMat where
  M := measured
  selfAdjoint := measured_selfAdjoint
  projective := measured_projective
  normalized := measured_normalized

/-- Native tracial winning probability of one pair of *arbitrary* 2x2
rank-one projectors under either parity (equal/unequal) decision. -/
noncomputable def matrixParityWin (P Q : QMat) (flip : Bool) : ℝ :=
  ∑ a : Bool, ∑ b : Bool,
    (if a.xor b = flip then (1:ℝ) else 0) *
    (((if a then (1:QMat)-P else P) *
      (if b then (1:QMat)-Q else Q)).trace.re / 2)

/-- With both questions at the center, equal answers win certainly. -/
theorem center_center_value :
    matrixParityWin pCenter pCenter false = 1 := by
  norm_num [matrixParityWin, Fintype.sum_bool, pCenter,
    Matrix.mul_apply, Matrix.trace]

/-- The center and either private setting have 4/5 equality probability. -/
theorem center_bob_value :
    matrixParityWin pCenter pBob false = 4/5 := by
  norm_num [matrixParityWin, Fintype.sum_bool, pCenter, pBob,
    Matrix.mul_apply, Matrix.trace]

theorem alice_center_value :
    matrixParityWin pAlice pCenter false = 4/5 := by
  norm_num [matrixParityWin, Fintype.sum_bool, pCenter, pAlice,
    Matrix.mul_apply, Matrix.trace]

/-- Two opposite private settings have 16/25 unequal-answer probability. -/
theorem alice_bob_value :
    matrixParityWin pAlice pBob true = 16/25 := by
  norm_num [matrixParityWin, Fintype.sum_bool, pAlice, pBob,
    Matrix.mul_apply, Matrix.trace, Matrix.vecMul, dotProduct,
    Matrix.sub_apply, Matrix.one_apply]

/-- Exact rational quantum CHSH payoff: 81/100 versus the deterministic
upper bound 3/4. No floating-point approximation or Tsirelson formula. -/
theorem rational_quantum_CHSH_gap :
    (matrixParityWin pCenter pCenter false +
     matrixParityWin pCenter pBob false +
     matrixParityWin pAlice pCenter false +
     matrixParityWin pAlice pBob true) / 4 = (81/100 : ℝ) ∧
     (3/4 : ℝ) < 81/100 := by
  rw [center_center_value, center_bob_value, alice_center_value, alice_bob_value]
  constructor <;> norm_num

end PNPAbove.WP20
