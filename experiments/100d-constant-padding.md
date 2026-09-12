---
layout: article
title: "Bury a 2D Pattern in 98 Dead Coordinates"
permalink: /experiments/100d-constant-padding/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Embed the project's 2D toy patterns into R^100 by padding with a constant, to test whether FAct's edge is really about the 2D geometry or survives being buried in high-dimensional dead weight.

| | |
|---|---|
| **GPU(s)** | A100 |
| **Dataset(s)** | 2D-Patterns toy suite, padded to R^100 |
| **Model** | Small MLP (2D-Patterns-Shape-of-Act series) |

<img src="/images/Experiments-Attempted-But/100d-constant-padding.png" alt="Bury a 2D Pattern in 98 Dead Coordinates — result chart" style="max-width:100%">

## Result summary

- Live padding (constant ≠ 0, so the padded coordinates carry a gradient even though they carry no signal) costs GELU **35 points** and ReLU **40 points** of accuracy — FAct loses **0**.
- Inert padding (constant = 0, no gradient at all) changes nothing for any activation.
- This was later shown (in the follow-up manifold study) to be an Adam optimizer artifact: 98 padding columns sharing one gradient injects a large, shared bias that GELU/ReLU can't route around and FAct's periodicity happens not to be perturbed by.

## Insights

- "Periodicity as bias-invariance" — FAct's advantage here isn't about the 2D structure surviving high dimensionality in some deep sense, it's a specific and fairly mundane robustness to a large shared additive bias that GELU and ReLU are sensitive to and FAct isn't. The gap shrinks a lot once the learning rate is tuned per arm.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
