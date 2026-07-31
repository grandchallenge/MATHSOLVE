#!/usr/bin/env python3
"""Replicate the algebraic boundary data for Galashin Figure 16.

The source-vector boundary is extracted from a candidate 2026-06-03 PDF whose Forge provenance remains unverified. The
boundary is rounded to one micro-point and traversed counterclockwise from the
source anchor. The critical equations and divisor-filtered quintic were derived
with exact rational/Gaussian-integer elimination and are replayed here with only
the Python standard library.

This script produces algebraic witnesses and pair-level sign checks. It does
not reconstruct the five internal planar drawings from the witnesses.
"""
from __future__ import annotations
import argparse, cmath, json, math
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Sequence

TWO_PI=2*math.pi
C_MATRIX=((1,1,0,-6,0,3),(0,1,1,7,0,-2),(0,0,0,2,1,3))
LINES=((Fraction(1),Fraction(0),Fraction(1)),(Fraction(1),Fraction(0),Fraction(0)),(Fraction(7),Fraction(2),Fraction(-6)),(Fraction(0),Fraction(1),Fraction(0)),(Fraction(-2),Fraction(3),Fraction(3)))
# Figure 16 source-vector boundary in right-handed coordinates. Source order is
# clockwise. The canonical algebraic labeling keeps the first point fixed and
# traverses the same polygon counterclockwise.
SOURCE_BOUNDARY_CLOCKWISE=((0.0,0.0),(34.129578,20.239700),(68.854401,0.992180),(69.251343,-38.693344),(34.923126,-39.288589),(0.595245,-39.685532))
BOUNDARY=((0.0,0.0),(0.595245,-39.685532),(34.923126,-39.288589),(69.251343,-38.693344),(68.854401,0.992180),(34.129578,20.239700))
# Primitive Gaussian-integer coefficients, descending powers of x.
QUINTIC=(
 complex(483540693892620000,-264313923428829400),
 complex(1828863333844625820,2216795100985993022),
 complex(-4290971821226241732,3605280657884124497),
 complex(-2698133932258548966,-5029360426989542682),
 complex(2775911427357818274,-629469832931420958),
 complex(-11773047226564512,509002207288521984),
)
# Gaussian-integer coefficients for the two cleared chart equations.
F2_COEFF={
 (3,1):complex(483371280,-272241536),
 (2,2):complex(-1453484991,732395948),
 (2,1):complex(-981619989,1336408964),
 (1,3):complex(-209538756,235731534),
 (1,2):complex(-1024288314,-413721164),
 (1,1):complex(-808398486,-963764106),
 (0,3):complex(-205967286,-2381658),
 (0,2):complex(411934572,4763316),
 (0,1):complex(617901858,7144974),
}
F3_COEFF={
 (4,0):complex(1852396,-185199112),
 (3,1):complex(-291094055,358823616),
 (3,0):complex(-2513966,251341652),
 (2,2):complex(-1587096,119056578),
 (2,1):complex(-12500915,85786890),
 (2,0):complex(-1984710,198427620),
 (1,2):complex(-1587096,119056578),
 (1,1):complex(278593140,-273036726),
 (1,0):complex(2381652,-238113144),
}
DIVISOR_FACTORS={
 "x^3":{"factor":"x","arrangement_forms":["alpha_3"]},
 "(x+1)^3":{"factor":"x+1","arrangement_forms":["alpha_2"]},
 "2x-3":{"factor":"2*x-3","companion_y":"0","arrangement_forms":["alpha_5","alpha_6"]},
 "7x-6":{"factor":"7*x-6","companion_y":"0","arrangement_forms":["alpha_4","alpha_5"]},
 "25x-24":{"factor":"25*x-24","companion_y":"-9/25","arrangement_forms":["alpha_4","alpha_6"]},
}
@dataclass(frozen=True)
class Point: x:complex; y:complex

def c_record(z): return {"re":float(z.real),"im":float(z.imag)}
def poly_eval(cs,z):
 v=0j
 for c in cs:v=v*z+c
 return v

def bivariate_eval(coeff,x,y): return sum(c*x**i*y**j for (i,j),c in coeff.items())
def durand_kerner(coeff,tol=1e-13,max_iterations=600):
 n=len(coeff)-1; monic=[c/coeff[0] for c in coeff]; radius=1+max(abs(c) for c in monic[1:])
 roots=[0.45*radius*cmath.exp(2j*math.pi*(i+0.173)/n) for i in range(n)]
 for _ in range(max_iterations):
  nxt=[];mx=0.0
  for i,r in enumerate(roots):
   den=1+0j
   for j,o in enumerate(roots):
    if i!=j:den*=r-o
   step=poly_eval(monic,r)/den
   nxt.append(r-step);mx=max(mx,abs(step))
  roots=nxt
  if mx<tol:return roots
 raise RuntimeError('Durand-Kerner did not converge')
def intersection(l1,l2):
 a,b,d=l1;A,B,D=l2;det=a*B-A*b
 if det==0:return None
 return ((b*D-B*d)/det,(d*A-D*a)/det)
def bounded_region_count(lines):
 incid={}
 for i in range(len(lines)):
  for j in range(i+1,len(lines)):
   p=intersection(lines[i],lines[j])
   if p is not None:incid[p]=incid.get(p,0)+1
 contribution=0
 for pairs in incid.values():
  m=(1+math.isqrt(1+8*pairs))//2
  if m*(m-1)//2!=pairs:raise AssertionError('bad multiplicity')
  contribution+=m-1
 return 1-len(lines)+contribution,len(incid)
def edges(boundary):return tuple(complex(boundary[i][0]-boundary[i-1][0],boundary[i][1]-boundary[i-1][1]) for i in range(6))
def alpha_values(x,y):return (1+0j,1+x,x,-6+7*x+2*y,y,3-2*x+3*y)
def solve_y(x):
 # F3/x = A*y^2+B*y+C for retained roots (x != 0).
 A=F3_COEFF[(2,2)]*x+F3_COEFF[(1,2)]
 B=F3_COEFF[(3,1)]*x*x+F3_COEFF[(2,1)]*x+F3_COEFF[(1,1)]
 C=F3_COEFF[(4,0)]*x**3+F3_COEFF[(3,0)]*x*x+F3_COEFF[(2,0)]*x+F3_COEFF[(1,0)]
 disc=B*B-4*A*C
 ys=((-B+cmath.sqrt(disc))/(2*A),(-B-cmath.sqrt(disc))/(2*A))
 return min(ys,key=lambda y:abs(bivariate_eval(F2_COEFF,x,y))+abs(bivariate_eval(F3_COEFF,x,y)))
def adjacent_minors(vals):return [float((vals[i].conjugate()*vals[(i+1)%len(vals)]).imag) for i in range(len(vals))]
def positive_winding(vals):
 total=0.0
 for i,v in enumerate(vals):
  angle=cmath.phase(vals[(i+1)%len(vals)]/v)
  if angle<=0:angle+=TWO_PI
  total+=angle
 return total
def orthogonality(lam,tilde):
 rows=([z.real for z in lam],[z.imag for z in lam]);trs=([z.real for z in tilde],[z.imag for z in tilde])
 return max(abs(sum(a*b for a,b in zip(r,t))) for r in rows for t in trs)
def critical_points():
 return sorted([Point(x=r,y=solve_y(r)) for r in durand_kerner(QUINTIC)],key=lambda p:(round(p.x.real,12),round(p.x.imag,12)))
def report():
 beta,nint=bounded_region_count(LINES);zs=edges(BOUNDARY);sols=[]
 for i,p in enumerate(critical_points(),1):
  aa=alpha_values(p.x,p.y);mind=min(abs(v) for v in aa)
  if mind<=1e-10:raise AssertionError('retained witness on divisor')
  lam=tuple(v.conjugate() for v in aa);tilde=tuple(z/a for z,a in zip(zs,aa))
  sols.append({
   "id":f"FIG16-B3-{i:02d}","projective_chart":{"a1":1,"a2":c_record(p.x),"a3":c_record(p.y)},
   "quintic_residual":abs(poly_eval(QUINTIC,p.x))/max(abs(c) for c in QUINTIC),
   "critical_residual_f2_scaled":abs(bivariate_eval(F2_COEFF,p.x,p.y))/max(abs(c) for c in F2_COEFF.values()),
   "critical_residual_f3_scaled":abs(bivariate_eval(F3_COEFF,p.x,p.y))/max(abs(c) for c in F3_COEFF.values()),
   "minimum_arrangement_denominator":mind,"orthogonality_residual":orthogonality(lam,tilde),
   "lambda_adjacent_minors":adjacent_minors(lam),"tilde_lambda_adjacent_minors":adjacent_minors(tilde),
   "lambda_winding_over_pi":positive_winding(lam)/math.pi,"tilde_lambda_winding_over_pi":positive_winding(tilde)/math.pi,
   "pair_status":"M_PLUS_SIGN_AND_ORTHOGONALITY_CHECKED_NUMERICALLY",
   "pattern_correspondence":"NOT_RECONSTRUCTED","rigid_deployment_status":"NOT_ASSESSED","manufacturability_status":"NOT_ASSESSED"
  })
 return {
  "schema_version":"1.1.0","replication_id":"VGSE-B3-FIGURE16-BOUNDARY-001",
  "source":{"title":"Amplituhedra and Origami, I: Tree Level","author":"Pavel Galashin","candidate_pdf_date":"2026-06-03","candidate_pdf_sha256":"e513789426ae6247438920bfc80cfba6bd9c32dc6799a4f7873d806a865f95de","provenance_state":"unverified_candidate","provider_manifest":None,"target":"Appendix B, Example B.1, Proposition B.2, Example B.3, Figure 16"},
  "fixture":{"k":3,"n":6,"C":C_MATRIX,"kami_boundary_source":"Figure 16 PDF vector paths rounded to 1e-6 PDF point after translation and y-axis inversion","source_boundary_clockwise":SOURCE_BOUNDARY_CLOCKWISE,"canonical_boundary_labeling":{"anchor":"source boundary vertex 0","orientation":"counterclockwise","vertices":BOUNDARY},"projectivized_lines":["x=-1","x=0","7x+2y=6","y=0","-2x+3y=-3"]},
  "elimination":{"unsaturated_resultant_factor_degrees":[1,1,1,3,3,5],"excluded_divisor_factors":DIVISOR_FACTORS,"retained_factor_degree":5},
  "arrangement":{"distinct_finite_intersections":nint,"bounded_region_count_beta":beta,"expected_beta":5},
  "algebraic_witness_count":len(sols),"solutions":sols,
  "claim_boundary":{"exact_arrangement_count_replicated":beta==5,"source_boundary_algebraic_witness_replay_complete":len(sols)==5,"source_vector_five_pattern_geometry_replicated_in_separate_artifact":True,"algebraic_witness_to_pattern_correspondence_reconstructed":False,"continuous_rigid_foldability_established":False,"collision_free_deployment_established":False,"finite_thickness_structure_established":False,"manufacturable_product_established":False,"commercial_claim_authorized":False}
 }
def validate(r):
 assert r['arrangement']['bounded_region_count_beta']==5 and r['algebraic_witness_count']==5
 for s in r['solutions']:
  assert s['quintic_residual']<2e-12
  assert s['critical_residual_f2_scaled']<2e-12 and s['critical_residual_f3_scaled']<2e-12
  assert s['minimum_arrangement_denominator']>1e-6 and s['orthogonality_residual']<5e-10
  assert min(s['lambda_adjacent_minors'])>1e-8 and min(s['tilde_lambda_adjacent_minors'])>1e-8
  assert abs(s['lambda_winding_over_pi']-2)<1e-10 and abs(s['tilde_lambda_winding_over_pi']-4)<1e-10
 c=r['claim_boundary'];assert not c['algebraic_witness_to_pattern_correspondence_reconstructed'];assert not c['commercial_claim_authorized']
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path);p.add_argument('--check',action='store_true');a=p.parse_args();r=report()
 if a.check:validate(r)
 text=json.dumps(r,indent=2,sort_keys=True)+'\n'
 if a.output:a.output.write_text(text,encoding='utf-8')
 else:print(text,end='')
if __name__=='__main__':main()
