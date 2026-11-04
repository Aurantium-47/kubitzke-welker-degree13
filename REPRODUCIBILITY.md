# Reproducibility and certificate format

## Supported path

Use Python 3.8 or later. All six main programs require only the standard library. No network access, API keys, datasets, compiled tools, or package installation is needed.

From the repository root:

```sh
python tools/reproduce.py --quick
python tools/reproduce.py
```

The full command runs these programs in this order:

1. `src/verify_degree12.py`
2. `src/verify_degree13.py`
3. `src/independent_degree_certificate.py`
4. `src/independent_degree13_certificate.py`
5. `src/referee_degree12_alternative.py`
6. `src/referee_degree13_alternative.py`

Their source is copied to a fresh temporary directory. Scripts write their JSON beside themselves there; the runner compares parsed JSON against `certificates/` and leaves the committed data untouched. Each subprocess is isolated from unrelated packages and uses the same Python executable as the runner. Assertions must remain enabled. All stdout/stderr and per-stage wall times are saved in `build/`, which is ignored by Git.

The degree-13 submitted script imports `local_survivors` from its degree-12 companion. The degree-13 quadratic-interval script similarly imports its own degree-12 companion. Keep both files together when using either extension directly. The two block-table programs are independently executable.

A complete pass means that the current local machine regenerated all six certificates, matched their complete JSON content, matched the three implementations' cutoffs and survivors row by row, and passed the unit tests and checksum checks. It does not mean a proof assistant has verified the analytic proof.

## Exact arithmetic and boundaries

The main programs use arbitrary-precision integers, integer division, binomial coefficients, and integer square root. They do not infer real-rootedness from numerical roots. The hypothetical real-rooted polynomial is ruled out via necessary conditions plus the exact classifications in the written proof.

For each `(d,k)` row, the integer `N` certifies the infinite region `q >= Q`, where `Q = binom(N,k)`. Every integer `1 <= q < Q` is handled by the program. Equality belongs to the analytic tail. The proof establishes monotonicity past N and existence of a valid N; an isolated successful comparison without that proof would not suffice.

## Data fields

Submitted certificates:

- `d`, `k`: actual polynomial degree and tested transition.
- `N`, `Q`: leading-index and q tail thresholds.
- `q_checked`: exactly `Q-1`.
- `q_passing_power_bound`: q values not excluded by the strict analytic power bound.
- `pairs_checked`: candidate p values considered in the submitted scanning loop.
- `survivors`: dictionaries containing `q = g_k`, `p = h_(k-1)`, and `v = K_k(q)+1`.

The block-table audit uses `records`, `q_candidates`, and `local_pairs` for the equivalent row data. The quadratic-interval audit uses `rows` and full `(d,k,q,p,v)` tuples. It deliberately omits the power-pruning filter, so its intermediate work counts are not intended to match the scanning algorithm. All three implementations do match the final local candidates and the certified tail thresholds.

The committed JSON is data, not a substitute for rerunning the code. `SHA256SUMS` binds the full release file set, apart from itself and ignored build outputs. `tools/reproduce.py` rejects missing or unexpected files in that tracked release set and rejects checksum differences.

## Optional supplemental tests

```sh
python -m pip install -r requirements-optional.txt
python extras/independent_audit.py
```

These supplement the proof with rational-sequence checks, explicit face-set realizations, and exact rational Sturm checks of two non-real-rooted examples. SymPy is pinned only for this optional script and requires Python 3.9 or later. The main degree-13 theorem does not depend on SymPy or on the unrefereed Macaulay estimate discussed in the general note.

## Trust and limits

- The finite enumeration is exhaustive only after accepting the written analytic reduction.
- The small-trace exclusion uses classical Kronecker theory, not a scan of roots.
- AI audit agreement is useful error checking but is not human peer review. The auditors may share model-level blind spots.
- No proof-assistant formalization, unrestricted-degree conclusion, or publication-priority claim is supplied.
- If a check fails, preserve the logs and report the failing tuple, source version, and Python version. Do not silently replace a committed certificate with a new output.
