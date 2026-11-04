"""Degree-13 extension of the referee's independent quadratic-interval audit.

No imports of verify_degree12.py or verify_degree13.py. No power-bound pruning,
no use of the author's strict p range, and no scanning of that p range.
"""
from math import comb, isqrt
from pathlib import Path
import json
from referee_degree12_alternative import audit

if __name__=='__main__':
    records=[]
    for k in range(2,13):
        row=audit(13,k)
        records.append(row)
        print(f'k={k}, N={row["N"]}, Q={row["Q"]}, survivors={row["survivors"]}',flush=True)
    survivors=[s for r in records for s in r['survivors']]
    expected=[[13,2,60,13,176],[13,2,61,13,181],
              [13,2,62,13,187],[13,2,63,13,194],
              [13,2,72,14,236],[13,2,73,14,242],
              [13,2,74,14,249],[13,3,245,86,537]]
    assert survivors==expected,survivors
    eliminations=[]
    for d,k,q,p,v in survivors:
        if k==2:
            if p==d:
                allowed=[comb(d,2)-d]
            else:
                assert p==d+1
                allowed=[comb(d-1,2)+2*(d-1)-p,
                         comb(d-2,2)+3*(d-2)+1-p]
            assert q not in allowed
            eliminations.append({'tuple':[d,k,q,p,v],'allowed_q':allowed})
        else:
            assert k==3
            # Newton at 1: h1 >= ceil(sqrt(2*d*p/(d-1))).
            lower=isqrt((2*d*p)//(d-1))
            if (d-1)*lower**2 < 2*d*p: lower+=1
            # Newton at 2: h1 <= floor(2*(d-2)*p^2/(3*(d-1)*(p+q))).
            upper=2*(d-2)*p*p//(3*(d-1)*(p+q))
            assert lower==14 and upper==13 and lower>upper
            eliminations.append({'tuple':[d,k,q,p,v],'h1_lower':lower,'h1_upper':upper})
    out={'q_values':sum(r['Q']-1 for r in records),'rows':records,
         'survivors':survivors,'eliminations':eliminations,'all_excluded':True}
    path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
