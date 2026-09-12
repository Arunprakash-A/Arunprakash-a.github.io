---
layout: article
title: "Does It Generalize Beyond ViT? Five Architectures, One Answer"
permalink: /experiments/fact-vs-rest-architecture-sweep/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Check whether FAct's ImageNet-level edge is a ViT-specific artifact by running the full 11/12-activation zoo across ViT, ConvMLPMixer, ConvNeXt, a LayerNorm-MLP, and ResNet-18.

| | |
|---|---|
| **GPU(s)** | mixed fleet: H200, V100, L4, A100 (all four hosts used across the sweep) |
| **Dataset(s)** | FashionMNIST, CIFAR-10 (5-seed confirmed arms) |
| **Model** | ViT / ConvMLPMixer / ConvNeXt / LayerNorm-MLP / ResNet-18 (~100K-param scale) |

<img src="/images/Experiments-Attempted-But/fact-vs-rest-architecture-sweep.png" alt="Does It Generalize Beyond ViT? Five Architectures, One Answer — result chart" style="max-width:100%">

## Result summary

- FAct (frozen, learned K=2 curve) wins **8 of 8** confirmed 5-seed arms on ViT, ConvMLPMixer, ConvNeXt, and LayerNorm-MLP.
- ViT/FashionMNIST, for example: FAct 0.8732 vs. LeakyReLU 0.8634 vs. ReLU 0.8621 vs. GELU 0.8402 — a clean sweep of the field.
- ViT/CIFAR-10: FAct 0.7251 vs. LeakyReLU 0.7044 vs. ReLU 0.7034 vs. GELU 0.6758.
- Loses (or fails to help) on a **plain, unnormalized** MLP and on ResNet-18 — the two architectures that don't LayerNorm their residual stream.
- Hook-based diagnostics traced the ResNet failure to its unnormalized post-add residual connection; retrofitting full (not partial) LayerNorm onto ResNet partially rescues FAct's advantage there.

## Insights

- "FAct generalizes across architectures" needs a footnote: it generalizes across *normalized* architectures. The mechanism (bounding the pre-activation into the range the Fourier fit was built for) depends on something keeping the input to the activation from wandering off — LayerNorm does that job; an unnormalized residual stream doesn't.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
