---
layout: article
title: "A Real 2D Manifold, Properly Embedded This Time"
permalink: /experiments/lowdim-manifold-highdim/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Follow up the constant-padding result with a cleaner design: put the same 2D toy patterns on a genuine manifold in R^D via a random orthonormal frame (isometric, general position), then add off-manifold noise, then curvature — controlling for init scale, which the padding study had left confounded with ambient dimension.

| | |
|---|---|
| **GPU(s)** | not recorded (small MLPs, R^D embeddings up to D=200) |
| **Dataset(s)** | 2D-Patterns toy suite, embedded in R^D via random orthonormal frames |
| **Model** | Small MLP, matched-init-scale control arm |

<img src="/images/Experiments-Attempted-But/lowdim-manifold-highdim.png" alt="A Real 2D Manifold, Properly Embedded This Time — result chart" style="max-width:100%">

## Result summary

- FAct's edge over GELU **survives isometric embedding**: +1.32pt for FAct vs. −3.05pt for GELU at D=200 (relative to D=2).
- The edge **peaks under off-manifold noise**: +12.3pt at noise σ=0.1 — substantially larger than on the clean manifold.
- The edge **vanishes on a curved manifold** — curvature erases the advantage entirely.
- A default-init measurement found the effective latent weight norm each unit applies collapses 10.8x from D=2 to D=200 — an earlier draft of this finding had mis-measured this as 20x; the corrected number is exactly what the theoretical fan-in rule (√(D/2)=10) predicts.

## Insights

- FAct's advantage is real on a properly isometric high-dimensional embedding (ruling out the earlier padding study's degenerate-subspace worry), gets *stronger* under realistic sensor-noise-like perturbation, but is not a universal law — curvature alone is enough to erase it. "Ambient dimension" and "init scale" have to be treated as separate controlled variables, not a shared confound.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
