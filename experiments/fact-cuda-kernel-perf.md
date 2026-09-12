---
layout: article
title: "Making FAct Cheap Enough to Actually Use"
permalink: /experiments/fact-cuda-kernel-perf/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Profile and optimize a custom CUDA kernel for FAct K=2, since the pure-PyTorch implementation is roughly 2x slower and uses substantially more memory than a fixed activation.

| | |
|---|---|
| **GPU(s)** | L4 (benchmarked); H200 too noisy at these shapes to benchmark reliably |
| **Dataset(s)** | n/a (microbenchmark, not a training run) |
| **Model** | cuda_fact_k2 kernel vs. pure-PyTorch FourierActivation |

<img src="/images/Experiments-Attempted-But/fact-cuda-kernel-perf.png" alt="Making FAct Cheap Enough to Actually Use — result chart" style="max-width:100%">

## Result summary

- The kernel is **DRAM-bound**: it sits at 80% of the theoretical memory-bandwidth floor for its shapes — there isn't much more to extract without changing the algorithm.
- Switching internal trig computation from fp64 to fp32 was the single biggest win measured: **5.7x** speedup on L4.
- sin/cos lookup tables were tried and rejected: no speed benefit, worse numerical accuracy, and zero memory saving — a plausible-sounding optimization that just didn't pay off.

## Insights

- The obvious-sounding optimization (LUTs) didn't work and the actual win (fp32 trig) was a much simpler, almost embarrassing fix — profile before optimizing, even for something as apparently well-understood as "make the trig faster."

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
