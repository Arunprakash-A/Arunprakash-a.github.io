---
layout: article
title: "Give Every Activation Its Own Tuned Learning Rate — Does FAct Still Win?"
permalink: /experiments/vit100k-lr-wd-tuning/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Re-run the 12-activation ViT-100K zoo with a per-activation learning-rate/weight-decay search (same tuning budget for every activation), instead of one shared setting for all — the obvious objection to the untuned Experiment-63 result.

| | |
|---|---|
| **GPU(s)** | all 5 hosts in the fleet: H200, A100 (local), V100, and both L4 GPUs, split by dataset |
| **Dataset(s)** | FashionMNIST, CIFAR-10, CIFAR-100, Food-101 |
| **Model** | ViT-100K (embed_dim=64, depth=2, heads=4, mlp_ratio=4.0) |

<img src="/images/Experiments-Attempted-But/vit100k-lr-wd-tuning.png" alt="Give Every Activation Its Own Tuned Learning Rate — Does FAct Still Win? — result chart" style="max-width:100%">

## Result summary

- FFAct and EFAct take the **top two places on every one of the 4 datasets**, after a fair, identical-budget 15-cell search + 5-seed confirmation per activation.
- FashionMNIST: FFAct 91.17±0.15 vs. EFAct 91.17±0.14 vs. 3rd-place LeakyReLU 90.69±0.27 — margin over 3rd place only marginal, p_holm=0.071.
- CIFAR-10: FFAct 76.34±0.62 vs. EFAct 75.91±0.30 vs. GELU 74.91±0.11 (p=0.045).
- Food-101 gained the most from tuning of the 4 datasets: FFAct +3.33pt over its own untuned baseline, ending at 39.15±0.44 vs. 3rd-place GELU 37.13±0.37 (p=0.006).
- The LR grid had to be extended mid-study: a first-pass 3×3 grid railed against its own ceiling in 47 of 48 search cells, so 2 more (higher) learning rates were added and 288 more cells re-run.

## Insights

- FAct's advantage survives the most obvious objection to an "untuned" leaderboard — giving every activation the exact same fair shot at its own best learning rate doesn't erase the gap, though on FashionMNIST it does shrink to marginal.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
