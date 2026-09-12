---
layout: article
title: "Does Multiplying by z Before the Activation Help?"
permalink: /experiments/fact-z-gated/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Compare z·φ(z) (a GLU-style gate) against the ordinary φ(z) for FAct K=2 on the ViT-100K/FMNIST setup, to see if a multiplicative gate on top of the learned curve adds anything.

| | |
|---|---|
| **GPU(s)** | V100 (predominant), some A100/H200 |
| **Dataset(s)** | FashionMNIST |
| **Model** | ViT-100K, FAct K=2 (global) |

<img src="/images/Experiments-Attempted-But/fact-z-gated.png" alt="Does Multiplying by z Before the Activation Help? — result chart" style="max-width:100%">

## Result summary

- Seed 0: plain FAct K=2 test accuracy 0.8787 vs. the z-gated variant 0.8667 — close, gated version trailing slightly.
- Across seeds, the two variants tie: p=0.31.
- A preactivation-statistics check found ViT's preactivations span only about 1/3 of one Fourier period at this scale — not enough range for a reparameterization like z-gating to have much room to express a different function.

## Insights

- The null result traces to a concrete cause rather than being unexplained: FAct's periodic machinery needs the preactivation to actually explore a meaningful chunk of its period, and at ViT-100K/FMNIST scale it doesn't, so any reparameterization of the curve gets blunted before it can matter.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
