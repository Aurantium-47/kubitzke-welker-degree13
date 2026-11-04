# Independent audit: extension to degree thirteen

**AI-only audit record.** This report was produced by a separate AI review process, not by an external human referee. It is not human peer review or formal proof-assistant verification.

Date: 2026-11-04. Reviewed `degree13_extension.md` and `verify_degree13.py`. Verdict: no mathematical or enumeration gap found. Together with the independently audited degree-12 proof, the certificate proves Q4.4 for all positive integer coefficients in actual degrees at most 13. No coefficient-height restriction is imposed. This does not settle the unrestricted conjecture or establish priority.

## Independent exact computation

`independent_degree13_certificate.py` extends the independently written binomial-block KK implementation, without importing any author routine. It examined exactly 7,805,671 integers q over all eleven indices 2≤k≤12. Its data are in `independent_degree13_certificate.json`.

Every cutoff N, cutoff Q, number passing the power bound, and final local survivor matches `degree13_certificate.json` field by field. The cutoffs are exactly

  N = 36,35,33,32,30,28,27,25,23,21,18,
  Q = 630,6545,40920,201376,593775,1184040,2220075,2042975,1144066,352716,18564.

The monotone-tail proof already audited in `independent_degree_referee.md` applies unchanged for each of these d=13 cases. Thus q≥Q is covered analytically, not omitted. The scan includes k=d−1=12, and k=1 remains automatic. All comparisons are exact, and equality in the strict power bound is correctly excluded.

## Complete survivors and exclusions

The only survivors (k,q,p,v) are

  (2,60,13,176), (2,61,13,181), (2,62,13,187), (2,63,13,194),
  (2,72,14,236), (2,73,14,242), (2,74,14,249),
  (3,245,86,537).

There are no surviving local pairs for k≥4.

For k=2, p=h_1. When p=13=d, Newton and integrality alone force h=(1+t)^13. Its q=binomial(13,2)−13=65 excludes all four p=13 tuples. When p=14=d+1, the independently audited classical trace classification permits only (1+t)^12(1+2t) and (1+t)^11(1+3t+t²). Their h_2 values are 90 and 89, so q is 76 or75, excluding all three p=14 tuples.

For the k=3 tuple, p=h_2=86 and h_3=p+q=331. The exact degree-13 Newton inequality at index 1 is

  12 h_1² ≥ 26·86 = 2236.

Because 12·13²=2028<2236, a positive integer h_1 must be at least 14. At index 2, the inequality is

  36·331·h_1 ≤ 22·86² = 162712.

But 36·331·14=166824>162712, so h_1 must be at most 13. This excludes the tuple. There is no need to choose or test a fourth coefficient, and v=537 need not enter this stronger contradiction.

Each filter used before these eliminations is necessary for a true violation, so exclusion does not assume local feasibility is sufficient. Every possible failed KK inequality is covered. The final use of Kruskal–Katona and passage to shorter initial prefixes by skeletons is valid.

## Source and claim scope

No new external theorem is needed beyond the already audited trace classification and the existing analytic reduction. The Brenti Problem 2.9 versus Problem 2.10 distinction remains correct. This audit makes no assertion that degree 13 is the largest reachable degree or that this bounded-degree result is new. This is an internally reproduced exact computer-assisted proof, not external peer review.
