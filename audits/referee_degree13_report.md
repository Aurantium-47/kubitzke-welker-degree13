# Independent audit of the degree-thirteen extension

**AI-only audit record.** This report was produced by a separate AI review process, not by an external human referee. It is not human peer review or formal proof-assistant verification.

Audit date: 2026-11-04. Reviewed `degree13_extension.md` and `verify_degree13.py`, using the separately audited degree-twelve argument only for its general analytic inequalities and the classical small-trace classification.

## Verdict

**The degree-thirteen extension passes the mathematical and independent computational audit. No gap was found.** Combined with the preceding proof, the conclusion is Question 4.4 for all positive-integer coefficient real-rooted polynomials of actual degree at most thirteen, with no coefficient-height restriction. This does not settle the unrestricted question, assert a maximal possible degree for this method, or establish publication priority. The Newton-only guaranteed range remains degree at most eleven; its degree-twelve obstruction is unchanged.

## Independent computation

The submitted `verify_degree13.py` was also rerun successfully. It checked 7,805,671 q values and scanned 46,442,223 p/q pairs, obtained exactly the claimed eight survivors, and verified their eliminations.

`referee_degree13_alternative.py` imports only the referee's separate quadratic-interval implementation, not either submitted verifier. It performs no power-bound pruning, does not use the submitted strict upper range for p, and does not scan that range. It solves the local Newton inequality by integer square root, checks its two integer boundary points, and locates the earlier normalized-ratio condition by monotone bisection. It additionally checks the lower-shadow/upper-operator direction for every survivor.

The complete run checked **7,805,671 q values in eleven (d,k) cases** with d=13 and 2≤k≤12. It reproduced all cutoff values:

- N: 36, 35, 33, 32, 30, 28, 27, 25, 23, 21, 18.
- Q=binom(N,k): 630, 6545, 40920, 201376, 593775, 1184040, 2220075, 2042975, 1144066, 352716, 18564.

Exactly these (k,q,p,v) tuples survived:

- (2,60,13,176), (2,61,13,181), (2,62,13,187), (2,63,13,194);
- (2,72,14,236), (2,73,14,242), (2,74,14,249);
- (3,245,86,537).

All candidate sets for k≥4 were empty. Complete output is in `referee_degree13_alternative.json`.

## Infinite tail and edge cases

The earlier degree-sensitive inequality, monotonicity of F_k, and existence of a finite cutoff use only d>k≥2, not d≤12. Therefore they apply unchanged to d=13. Every q≥Q is certified by the analytic tail, while the independent run includes every positive integer q<Q. There is no gap at equality, floating-point comparison, or unexamined coefficient-height tail. Index k=1 remains automatic from h_1≥d and Newton at index one. The existing degree-one and arbitrary-shorter-prefix treatments continue to apply.

## Exact exceptional-pair elimination

For the first four tuples, k=2 means p=h_1=13=d. Normalized Newton log-concavity together with h_d≥1 forces h_i=binom(13,i); thus q=78−13=65, excluding q=60,61,62,63. This exclusion uses no real-rootedness beyond Newton.

For the next three tuples, h_1=14=d+1. The already audited totally-positive-algebraic-integer classification allows only (1+t)^12(1+2t) and (1+t)^11(1+3t+t²). Their second coefficients are 90 and 89, giving q=76 and 75. None is a listed candidate. This step uses real-rootedness and integrality, as required.

For the last tuple, h_2=86 and h_3=331. Newton at index one gives

12h_1²≥26·86=2236.

Since 12·13²=2028<2236≤2352=12·14² and h_1 is a positive integer, h_1≥14. Newton at index two gives

36·331·h_1≤22·86²=162712.

But 36·331·14=166824>162712, so h_1≤13. This is a genuine contradiction, not a numerical approximation. The new elimination does not require the hypothesized value of h_4 or v; the earlier coefficients alone are impossible. For completeness, 245=binom(12,3)+binom(7,2)+binom(4,1), so K_3(245)=495+35+6=536 and v=537 is correct.

## Source/code presentation

The extension correctly preserves its bounded-degree scope and makes no prior-art claim. Its shared imported `local_survivors` function is already audited, but this means the extension is not a self-contained single-file verifier. Distribute `verify_degree12.py` together with `verify_degree13.py`, or describe the latter as an extension script rather than a standalone independent implementation. This is a reproducibility wording issue, not a mathematical gap.
