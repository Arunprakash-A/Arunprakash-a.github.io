---
layout: article
title: "Do Nine Harmonics Beat Two, 90 Layers Deep?"
permalink: /experiments/fact-k9-exp61-repeat/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Repeat a 90-hidden-layer, width-10, LayerNorm MNIST MLP study (Experiment-61) with K=9 Fourier activations added to its 16-activation zoo, on the same host, same torch build, same MNIST cache — does more harmonic capacity help at extreme depth?

| | |
|---|---|
| **GPU(s)** | V100 |
| **Dataset(s)** | MNIST |
| **Model** | 90-hidden-layer, width-10, LayerNorm residual MLP (19,550 FFN params) |

<img src="/images/Experiments-Attempted-But/fact-k9-exp61-repeat.png" alt="Do Nine Harmonics Beat Two, 90 Layers Deep? — result chart" style="max-width:100%">

## Result summary

- Harness validation: Experiment-61's frozen `fact_fixed` (K=2) arm reproduced **bit-identically** — test_acc 0.9420 to all printed digits, same GPU (A100) as the original, confirming the ported harness is faithful.
- Frozen, parameter-free ranking (16 activations): K=9's analytic GELU fit lands **last of 13** parameter-free arms at 0.9374 — worse than K=2's 0.9432, and well behind the leader, ELU, at 0.9536.
- Trainable coefficients tell a different story: EFAct-K9 (0.9480) edges out EFAct-K2 (0.9468) and EFAct-K3 (0.9466) — a real but tiny +0.0012 gain over K2, and these aren't capacity-matched against the frozen table (19 vs 5 extra params).
- Matched pairs, same everything but harmonic count: frozen K9−K2 = −0.0058 (worse); trainable K9−K2 = +0.0012 (marginally better).

## Insights

- As a fixed nonlinearity, more harmonics is actively worse at this depth — K=9's extra wiggle is capacity the frozen network can't use and may be actively fighting.
- Letting the coefficients train recovers a small edge for K=9, but it's inside noise for a single seed, and the honest read is "K=2 remains the practical default," which is exactly what a separate K-choice sweep (K=2 for GELU-init, K=3 for random-init) had already suggested.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
