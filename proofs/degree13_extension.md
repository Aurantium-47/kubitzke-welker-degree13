# Extension of the complete-degree result to degree thirteen

**Status:** exact computer-assisted proof, independently reproduced using a second integer implementation. This is not external peer review. Together with degree12_proof.md this proves Kubitzke–Welker Question 4.4 for every degree 1≤d≤13, with no coefficient-height restriction. It does not resolve the unrestricted question. No publication-priority claim is made.

All definitions, the sharp power estimate, the monotone infinite-tail certificate, and necessary finite-pair inequalities are exactly those proved in degree12_proof.md. No new analytic assumption is used. The k=1 inequality is automatic as before.

## Exact finite output for d=13

For k=2,…,12, the certified leading-index cutoffs N are

36,35,33,32,30,28,27,25,23,21,18.

The corresponding q cutoffs binom(N,k) are

630,6545,40920,201376,593775,1184040,2220075,2042975,1144066,352716,18564.

The extension script verify_degree13.py imports the already audited local_survivors function from verify_degree12.py and performs only exact integer computations. The output is degree13_certificate.json. The completed run checks 7,805,671 q-values and 46,442,223 p-pairs across 11 indices, using only arbitrary-precision integer arithmetic. Every q above the displayed cutoff is ruled out by the monotone tail proof, not ignored.

There are exactly eight surviving local tuples (k,q,p,v), with q=g_k, p=h_{k−1}, and v=K_k(q)+1:

- (2,60,13,176)
- (2,61,13,181)
- (2,62,13,187)
- (2,63,13,194)
- (2,72,14,236)
- (2,73,14,242)
- (2,74,14,249)
- (3,245,86,537)

Every local candidate set for k≥4 is empty.

## Exclusion of all eight tuples

For the first four tuples, p=h₁=d=13 forces h(t)=(1+t)^13. Its q=h₂−h₁ equals binom(13,2)−13=65, not any listed value.

For the next three tuples, p=h₁=d+1=14. The classical small-trace classification proved in small_trace_case.md forces

h(t)=(1+t)^12(1+2t) or h(t)=(1+t)^11(1+3t+t²).

These have h₂=90 or 89, respectively, and hence q=76 or 75, not 72,73,74.

For the last tuple, k=3 gives h₂=p=86 and h₃=p+q=331. Newton at index 1 requires

12h₁²≥26·86=2236,

so integer h₁≥14. Newton at index 2 requires

36·331·h₁≤22·86²=162712,

so integer h₁≤13. This is impossible. Note that 12·13²=2028<2236≤12·14²=2352 and 36·331·14=166824>162712; no numerical approximation is needed.

Every possible violation is excluded, so Kruskal–Katona proves Question 4.4 in degree 13. Together with the degree-12 proof, this covers all positive integer coefficients in degrees at most 13.

## Scope and prior art

The primary-source and priority notes in degree12_proof.md remain applicable. In particular the verified Brenti source is https://arxiv.org/html/2410.09897v1 . The nearby d≤9 and h_i≤100 observation addresses Problem 2.9, not the Q4.4/Problem 2.10 target. The 2026 Macaulay theorem does not imply the simplicial conclusion proved here. No claim is made that degree 13 is the largest degree approachable by this method, or that the unrestricted conjecture is solved.
