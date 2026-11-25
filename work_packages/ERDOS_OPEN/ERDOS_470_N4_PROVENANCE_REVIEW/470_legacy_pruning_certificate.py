"""Exact falsification of a legacy code comment, not an odd-weird counterexample."""
import argparse,hashlib,json,math,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source',type=Path,default=ROOT/'weird-odd-engine')
parser.add_argument('--output',type=Path,default=ROOT/'470-legacy-pruning-certificate.json')
args=parser.parse_args()
LEGACY=args.source
PIN='6ba33a63217b60f8e2a8583929078eec3c454d8f'
assert subprocess.check_output(['git','-C',str(LEGACY),'rev-parse','HEAD']).decode().strip()==PIN
factors=[(5,3),(11,1),(13,1),(17,1),(19,1),(23,1),(29,1),(31,1),(37,1),(41,1),(43,1),(47,1)]
assert all(all(p%d for d in range(2,math.isqrt(p)+1)) for p,e in factors)
n=math.prod(p**e for p,e in factors)
sigma=math.prod(sum(p**k for k in range(e+1)) for p,e in factors)
abundance=sigma-2*n
witness=[707941630501625,13249079564501,3453874853,7043185,5945,41]
assert n==366005822969340125 and 10**17<n<10**18 and n<2**63
assert abundance==721194170990150 and abundance>0
assert n%3 and n%7 and n%30==5
assert len(set(witness))==len(witness) and sum(witness)==abundance
assert all(0<d<n and n%d==0 for d in witness)
source=subprocess.check_output(['git','-C',str(LEGACY),'cat-file','blob','HEAD:weirdodd.cpp'])
primes=subprocess.check_output(['git','-C',str(LEGACY),'cat-file','blob','HEAD:primes.txt'])
assert primes.split()[0]==b'7'
report={'record_type':'GCL_LEGACY_PRUNING_COMMENT_FALSIFICATION','legacy_commit':PIN,
        'legacy_source_sha256':hashlib.sha256(source).hexdigest(),'n':str(n),'prime_factorization':factors,
        'sigma':str(sigma),'abundance':str(abundance),'abundance_divisor_witness':[str(d) for d in witness],
        'semiperfect':True,'odd_weird_counterexample':False,'legacy_residue':5,'legacy_seven_divisibility_guard':False,
        'conclusion':'The claim that all abundant numbers in the advertised range are divisible by 3 or 7 is false. This explicit skipped number is semiperfect, so it does not refute odd-weird exclusion; a general safe-pruning justification is still needed.',
        'seven_field_historical_engine_recovered':False,'full_search_replayed':False,'certification':False}
args.output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
