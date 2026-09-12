---
layout: article
title: "How Steep Is This Curve, Exactly?"
permalink: /experiments/lipschitz-of-activations/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Work out the Lipschitz constant — analytically where possible — for sixteen standard fixed activations plus FAct and PAU, and measure how FAct's constant actually moves during real ImageNet-1K training.

| | |
|---|---|
| **GPU(s)** | analysis-only (uses an existing ImageNet-1K FAct checkpoint, itself trained on H200; the Lipschitz computation is CPU-side) |
| **Dataset(s)** | ImageNet-1K (existing FAct K=2 checkpoint, for the measured numbers) |
| **Model** | theory + measurement on existing checkpoints (no new training) |

<img src="/images/Experiments-Attempted-But/lipschitz-of-activations.png" alt="How Steep Is This Curve, Exactly? — result chart" style="max-width:100%">

## Result summary

- GELU/SiLU/Mish: L = 1.1289 / 1.0998 / 1.0885. ReLU family, Tanh, ELU, Softplus, Softsign, Identity: exactly 1.
- FAct, GELU-fit init, K harmonics: **L = K + o(1)**, attained exactly at the periodic seam t=±π.
- FAct, actually learned on ImageNet-1K, K=2: L = **2.2855** — up 10.7% from its 2.0652 init.
- A **bug found in PAU's own implementation**: `PAU.forward`'s pole-avoidance guarantee (`Q = 1 + Σ|b_k|t^k`) is neither of the two formulas its docstring claims, and for t<0 its odd powers go negative. Over 100 ImageNet-1K epochs, min(Q) erodes from 1.0000 to **0.8547** — and a spiral10 checkpoint (`pau_m3n1`) was found with a real pole.

## Insights

- FAct's Lipschitz constant is not a free capacity knob — because the GELU fit's sine coefficients are all `±1/k`, every harmonic contributes exactly unit slope to the derivative, so L scales as K almost by construction, worst-cased at the edge of the fit window. This is a concrete reason normalizing right before a periodic activation matters: on real ViT-100K runs, most preactivations reach only ~20% of L, but the tails reach 98.2%.
- The PAU finding is a genuine, previously-undocumented correctness bug in a rational-activation baseline this project uses for comparison — not a FAct result at all, but worth having found before citing PAU's numbers elsewhere.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
