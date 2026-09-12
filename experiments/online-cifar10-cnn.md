---
layout: article
title: "The Same Online Protocol, Now With a Conv Front End — and a Batch-Size Flip"
permalink: /experiments/online-cifar10-cnn/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Extend the MNIST online-learning protocol to CIFAR-10 behind a small conv layer feeding the same 784-wide MLP, and check whether the GELU/FAct story holds as batch size grows off strict one-sample-at-a-time streaming.

| | |
|---|---|
| **GPU(s)** | not recorded (single pass, ~815K-param CNN+MLP — light compute) |
| **Dataset(s)** | CIFAR-10 |
| **Model** | Conv(5×5) → 784→10→10 MLP, online (batch_size ∈ {1, 10, 20}) |

<img src="/images/Experiments-Attempted-But/online-cifar10-cnn.png" alt="The Same Online Protocol, Now With a Conv Front End — and a Batch-Size Flip — result chart" style="max-width:100%">

## Result summary

- batch_size=1 (true one-sample streaming): GELU 0.4429 vs. FAct K=2 0.4418 final-weights test accuracy — **statistically tied**.
- batch_size=10: GELU 0.4199 vs. FAct K=2 **0.4576** — FAct decisively ahead, +3.8pt, seed-consistent.
- batch_size=20: GELU 0.4095 vs. FAct K=2 **0.4492** — same story, margin if anything slightly wider (+4.0pt).
- Multi-epoch prequential accuracy (letting the stream repeat) turned out to be untrustworthy as a metric here — it's contaminated by outright memorization once the same samples are seen more than once.

## Insights

- The tie-vs-win result flips exactly at the batch-size boundary between "one gradient sample" and "any batch averaging at all" — FAct's advantage seems to need the variance reduction a small batch provides, not just more wall-clock training.
- The K=2 zero-init collapse here is the same even-K, φ'(0)=0 trap found in the MNIST online study — the same structural symmetry, reproduced in a second architecture.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
