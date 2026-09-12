---
layout: article
title: "The Same Tuning Exercise on ConvMLPMixer — FAct Falls"
permalink: /experiments/convmlpmixer-lr-wd-tuning/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Repeat the per-activation LR/WD tuning exercise on ConvMLPMixer instead of ViT, to see if the tuned ranking holds across architectures.

| | |
|---|---|
| **GPU(s)** | mixed fleet (A100/H200/V100/L4, similar split to the ViT tuning study) |
| **Dataset(s)** | FashionMNIST, CIFAR-10, CIFAR-100, Food-101 |
| **Model** | ConvMLPMixer-3M |

<img src="/images/Experiments-Attempted-But/convmlpmixer-lr-wd-tuning.png" alt="The Same Tuning Exercise on ConvMLPMixer — FAct Falls — result chart" style="max-width:100%">

## Result summary

- FFAct (`fact_fixed`) ranked 1-2 of 12 **untuned** on all 4 datasets — matching the architecture sweep.
- After tuning: FMNIST tuned means — GELU 93.39, SiLU 93.36, Mish 93.31, **FFAct 93.11 (rank 4)**.
- CIFAR-10 tuned means — GELU 84.70, LeakyReLU 84.51, Mish 83.92, ReLU 83.90 — FFAct fell further back here.
- CIFAR-100 tuned means — LeakyReLU 58.79, GELU 55.23, ReLU 55.12, **FFAct 54.28 (rank 4)**.
- FAct gains the *least* from tuning of all 12 activations, on every single dataset — the opposite of the ViT-100K result above.

## Insights

- This flatly contradicts the ViT tuning result and is one of the more important negative findings in the whole catalog: "untuned" leaderboards can flatter an activation that simply happens to work well at whatever default learning rate everyone shares. Root-caused two experiments later (the isotropic pilot) as a real architecture effect, not a depth/width confound.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
