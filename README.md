# SpectralLift

Reference implementation of the **SpectralLift** verified lifting pipeline for
legacy C kernels.

## Repository layout

```
spectralift/
  compiler/
    passes.py
    verify.py
  ir/
    graph.py
  benchmarks/
    gemm_case.py
  scripts/
    run_gemm_bench.sh
  tests/
    test_passes.py
pyproject.toml
```

Training and evaluation drivers live under `scripts/` and `benchmarks/`; the
GEMM case-study inputs and the reported measurements are committed alongside the
code. The verification harness depends on `z3-solver`.

## Usage

`scripts/run_gemm_bench.sh` reproduces the GEMM experiment reported in the paper.

## Citation

> A. Evans, R. Okonkwo, J. Mbeki. SpectralLift: Verified Lifting of Legacy C
> Kernels to Tensor IR. Manuscript under review at TP '26.
