---
layout: article
title: "One Hinge, Fit to the Learned Curve"
permalink: /experiments/relu1-approx-of-fact/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Fit a single ReLU-shaped hinge ("ReLU-1") to approximate the shape FAct converges to, and see whether that much cheaper, piecewise-linear stand-in captures FAct's advantage.

| | |
|---|---|
| **GPU(s)** | mixed: A100 / L4 (a host-effect check between them found p=0.66, no detectable difference) |
| **Dataset(s)** | FashionMNIST, CIFAR-10, CIFAR-100 |
| **Model** | ViT-100K (part of the 12-activation zoo, Experiment-63) |

<img src="/images/Experiments-Attempted-But/relu1-approx-of-fact.png" alt="One Hinge, Fit to the Learned Curve — result chart" style="max-width:100%">

## Result summary

- 5 seeds × 3 datasets, the one-hinge fit: FMNIST **0.9065**, CIFAR-10 **0.7456**, CIFAR-100 **0.4733**.
- Beats GELU, SiLU, and Mish on all three datasets.
- Ties plain ReLU on FMNIST and CIFAR-10, but beats it — and beats trainable EFAct — on CIFAR-100.
- An A100-vs-L4 host-effect check found p=0.66: no detectable difference from which GPU ran the job.

## Insights

- A single well-placed hinge captures a meaningful fraction of what the full 5-coefficient Fourier curve is doing — you don't need the periodic machinery to get most of the benefit on the easier datasets, though CIFAR-100 is where the fuller curve starts to matter.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
