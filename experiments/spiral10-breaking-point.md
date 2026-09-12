---
layout: article
title: "The Dataset That Breaks Every Activation Equally"
permalink: /experiments/spiral10-breaking-point/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Push a 2D toy-pattern study to its limit with a 10-arm spiral wound through two full rotations, specifically looking for the difficulty level where FAct's advantage finally disappears.

| | |
|---|---|
| **GPU(s)** | not recorded (2D toy dataset, single hidden-layer MLP — trivial compute) |
| **Dataset(s)** | Spiral10 (synthetic, turns=2.0, 10-class) |
| **Model** | Single hidden-layer MLP (width 10 or width 2) |

<img src="/images/Experiments-Attempted-But/spiral10-breaking-point.png" alt="The Dataset That Breaks Every Activation Equally — result chart" style="max-width:100%">

## Result summary

- At width 10: FAct 0.133, GELU 0.168, ReLU 0.158 final test accuracy — all barely above the 0.10 chance level.
- At width 2: FAct 0.118, GELU 0.130, ReLU 0.125 — same story, all three still stuck near chance.
- Training loss for every run barely moves off ln(10)=2.303 (the chance-level cross-entropy) — flat, noisy, no real descent.
- Root cause, found via a diagnostic in the dataset generator: two full rotations put different-class points as close as 0.0095 apart in raw coordinates — ~40x smaller than the same-radius arm spacing — creating genuine, unavoidable class overlap, not just visual density.

## Insights

- This is the useful negative result in the catalog: a pattern hard enough (genuinely overlapping classes, not just visually dense) makes GELU, ReLU, and FAct fail identically. FAct's edge on the earlier, easier 2D patterns isn't magic that survives any difficulty level — it needs the classes to actually be separable.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
