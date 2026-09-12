---
layout: article
title: "The Simplest Possible Network: One Linear Layer"
permalink: /experiments/svd-of-mlp/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Strip the comparison down to the smallest model that can still carry an activation function — a single nn.Linear(784, 10) on MNIST, activation applied straight to the logits — so an SVD and an exact Hessian of the one weight matrix become tractable.

| | |
|---|---|
| **GPU(s)** | mixed (H200 references in logs; trivial compute — a single 7,850-parameter linear layer) |
| **Dataset(s)** | MNIST |
| **Model** | Single nn.Linear(784, 10), no hidden layer |

<img src="/images/Experiments-Attempted-But/svd-of-mlp.png" alt="The Simplest Possible Network: One Linear Layer — result chart" style="max-width:100%">

## Result summary

- Seed-0, default init: GELU test accuracy **0.6688** vs. FAct (K=2, GELU-init) **0.9075** — a large gap on this minimal model.
- Across a 5-seed sweep (default + orthogonal init, Adam + plain SGD): GELU's accuracy is wildly seed-dependent while FAct K=2 stays tight seed-to-seed.
- A Hessian block-partition (weight block vs. FAct's 5-coefficient block) found `a0` is an exact gauge-flat direction, and a Schur complement reveals a weight-activation coupling that GELU's fixed shape simply hides (GELU has no activation-parameter block to couple through).
- Extended to 4 toy 2-neuron MLPs moved in from a separate scratch directory: the SVD finding generalizes across those architectures, but the Hessian sharpness/saddle-fraction story does **not** — the saddle ranking actually inverts relative to the MNIST case.

## Insights

- The cleanest possible activation-only comparison (one weight matrix, nothing else) already shows GELU is far more sensitive to initialization than FAct — the effect isn't an artifact of some more complicated architecture hiding it.
- Also found, separately: the polished report.pdf's own Hessian table had silently drifted out of sync with the checkpoints it was supposedly reporting on, for reasons never root-caused — a reminder to spot-check a report's own numbers against fresh checkpoints before citing them, even (especially) your own.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
