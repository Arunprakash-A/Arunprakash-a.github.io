---
layout: article
title: "Ruling Out the Depth/Width Confound"
permalink: /experiments/convmlpmixer-isotropic-pilot/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Rebuild ConvMLPMixer's backbone as a ViT-structured, constant-width, depth-3 isotropic network on CIFAR-10 only, to check whether the previous experiment's FAct loss was really about the convolutional mixer architecture, or just a side effect of its different depth/width shape.

| | |
|---|---|
| **GPU(s)** | V100 (a live shared-memory crash occurred mid-run, fixed by cutting DataLoader workers from 6 to 3) |
| **Dataset(s)** | CIFAR-10 |
| **Model** | Isotropic ConvMixer (constant-width, depth=3, ViT-structured) |

<img src="/images/Experiments-Attempted-But/convmlpmixer-isotropic-pilot.png" alt="Ruling Out the Depth/Width Confound — result chart" style="max-width:100%">

## Result summary

- FAct loses **both** untuned (rank 5/6 of 12 — the only architecture tested where it isn't top-2 untuned) and tuned (rank 8/10, p<0.004 vs. LeakyReLU).
- LeakyReLU tuned mean 86.11 vs. ReLU 85.33 in this pilot's own table — FAct trails both.
- This rules out the depth/width confound directly: same isotropic, constant-width shape as the earlier tuning study, same conclusion.

## Insights

- The ConvMLPMixer loss wasn't an artifact of that architecture's specific depth/width recipe — something about the convolutional-mixer *mechanism* itself, not its shape, is what disagrees with FAct. Not extended to the other 3 datasets, since the isotropic-pilot question was answered on CIFAR-10 alone.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
