"""Third exact audit: independent KK search and quadratic-interval feasibility.

Does NOT import either submitted verifier, nor enumerate each p via its range.
For every q below the proven tail, the Newton inequality is solved exactly as a
quadratic. The preceding normalized-ratio condition is a monotone predicate, so
its feasible endpoint is found by bisection. No power-bound pruning is used.
"""
from math import comb, factorial, isqrt, prod
import json
from pathlib import Path


def upper(q,k):
    total=0
    n=k
    while comb(n+1,k)<=q:
        n+=1
    for j in range(k,0,-1):
        if not q: break
        while comb(n,j)>q: n-=1
        total+=comb(n,j+1)
        q-=comb(n,j)
        n-=1
    assert q==0
    return total


def shadow(q,k):
    total=0
    n=k
    while comb(n+1,k)<=q: n+=1
    for j in range(k,0,-1):
        if not q: break
        while comb(n,j)>q: n-=1
        total+=comb(n,j-1)
        q-=comb(n,j)
        n-=1
    assert q==0
    return total


def cutoff(d,k):
    # Factorials cancelled first; equivalent exact rational comparison.
    fall=prod(range(d-k+1,d+1))
    def good(n):
        denominator=prod(range(n-k+2,n+2))
        numerator=prod(range(n-k,n+1))
        return fall*numerator**k >= (d-k)**k*denominator**(k+1)
    n=k+1
    while not good(n): n+=1
    assert n==k+1 or not good(n-1)
    return n


def audit(d,k):
    N=cutoff(d,k)
    Q=comb(N,k)
    A=k*(d-k)
    C=d+1
    B=A+C
    ratio_left=(d-k+1)**(k-1)
    ratio_right=comb(d,k-1)*k**(k-1)
    ans=[]
    for q in range(1,Q):
        v=upper(q,k)+1
        # -C p^2 + E p + A q^2 >= 0 exactly characterizes Newton.
        E=(A-C)*q-B*v
        pmax=(E+isqrt(E*E+4*C*A*q*q))//(2*C)
        def slack(p): return -C*p*p+E*p+A*q*q
        assert slack(pmax)>=0 and slack(pmax+1)<0
        base=comb(d,k-1)
        if pmax<base: continue
        def allowed(p):
            return p**k*ratio_left >= ratio_right*(p+q)**(k-1)
        if not allowed(pmax): continue
        lo,hi=base-1,pmax
        while hi-lo>1:
            mid=(lo+hi)//2
            if allowed(mid): hi=mid
            else: lo=mid
        for p in range(hi,pmax+1):
            # Cross-check upper-operator orientation against the lower shadow.
            assert shadow(v,k+1)>q
            assert shadow(v-1,k+1)<=q
            ans.append([d,k,q,p,v])
    return {'d':d,'k':k,'N':N,'Q':Q,'survivors':ans}

if __name__=='__main__':
    records=[audit(d,k) for d in range(3,13) for k in range(2,d)]
    survivors=[s for r in records for s in r['survivors']]
    expected=[[11,2,41,11,95],[11,2,42,11,100],
              [12,2,50,12,131],[12,2,51,12,136],[12,2,52,12,142],
              [12,2,61,13,181],[12,2,62,13,187]]
    assert survivors==expected,survivors
    h=[1,13,74,255,575,921,1075,921,575,255,74,13,1]
    slacks=[i*(12-i)*h[i]**2-(i+1)*(13-i)*h[i-1]*h[i+1]
            for i in range(1,12)]
    assert min(slacks)>0
    gamma=[]
    for i in range(7):
        gamma.append(h[i]-sum(gamma[j]*comb(12-2*j,i-j) for j in range(i)))
    assert gamma==[1,1,-2,6,-20,21,-3]
    assert upper(h[2]-h[1],2)==180<h[3]-h[2]==181
    out={'method':'quadratic interval; no power-bound pruning; no p-loop scan',
         'q_values':sum(r['Q']-1 for r in records),'rows':records,
         'survivors':survivors,'newton_slacks':slacks,'gamma':gamma}
    path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
