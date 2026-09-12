---
layout: article
title: "Initialize the FFN Weights With the Transferred Fourier Curve"
permalink: /experiments/fourier-init/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Use the frozen DFT weights that won the NMT transfer study to initialize the ViT-100K FFN's fc1/fc2 layers, to see whether that initialization helps any activation converge faster or further.

| | |
|---|---|
| **GPU(s)** | mixed: L4, A100, some V100/H200 |
| **Dataset(s)** | FashionMNIST, CIFAR-10, CIFAR-100, Food-101 |
| **Model** | ViT-100K, 12-activation zoo, Fourier-derived fc1/fc2 init |

<img src="/images/Experiments-Attempted-But/fourier-init.png" alt="Initialize the FFN Weights With the Transferred Fourier Curve — result chart" style="max-width:100%">

## Result summary

- Overall: a **null** result — 17 wins of 36 (activation, dataset) cells, mean −0.43pt versus standard init.
- No help to either of the project's own learned activations, EFAct or FFAct.
- Consistent, real **harm** to saturating activations: Tanh drops −4.59pt.

## Insights

- The transferable Fourier structure that helped elsewhere in this project (frozen NMT token embeddings, the activation itself) does not extend to weight initialization — it's neutral for most activations and actively bad for ones that saturate, presumably because a Fourier-shaped init pushes their preactivations into a range those activations weren't built for.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
