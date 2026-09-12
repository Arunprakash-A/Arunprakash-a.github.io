---
layout: article
title: "Does the Fourier-Coefficient Init Even Matter?"
permalink: /experiments/imagenet1k-learned-coeff-init/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Start FAct's 5 coefficients from a different initial guess (not the GELU fit) and see whether the network still finds its way to the same place on ImageNet-1K.

| | |
|---|---|
| **GPU(s)** | H200 |
| **Dataset(s)** | ImageNet-1K |
| **Model** | ViT, depth 6 (embed_dim 384) |

<img src="/images/Experiments-Attempted-But/imagenet1k-learned-coeff-init.png" alt="Does the Fourier-Coefficient Init Even Matter? — result chart" style="max-width:100%">

## Result summary

- Stopped at epoch 17 of a planned 100 — not because it failed, but to free the GPU for its sibling study (the frozen-activation run below).
- val_acc = 0.4858 at the point it was stopped.
- Checkpoints and logs were rsynced to local disk before the run was torn down, so the partial result is real but not a finished comparison.

## Insights

- An honest partial result: this is here because "stopped early, kept the data" is a real and common outcome in this lab notebook, not because the number proves anything about coefficient init on its own.
- The decision to reallocate the GPU rather than let two studies fight over it is itself the operational lesson — a shared 4-6 GPU fleet means every run competes with every other live run.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
