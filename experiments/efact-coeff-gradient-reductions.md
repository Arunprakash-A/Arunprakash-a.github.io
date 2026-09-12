---
layout: article
title: "The Network's Two Halves Disagree About the Curve's Shape"
permalink: /experiments/efact-coeff-gradient-reductions/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** EFAct's 5 Fourier coefficients are shared across every block in the network; test 4 different ways of reducing their per-block gradients (all-sites vs. last-block-only, sum vs. max|g|) to see which, if any, changes accuracy.

| | |
|---|---|
| **GPU(s)** | V100 (predominant), some A100 |
| **Dataset(s)** | FashionMNIST (5 seeds), CIFAR-10 (1 seed) |
| **Model** | ViT-100K, EFAct (trainable, 2-block) |

<img src="/images/Experiments-Attempted-But/efact-coeff-gradient-reductions.png" alt="The Network's Two Halves Disagree About the Curve's Shape — result chart" style="max-width:100%">

## Result summary

- All 4 gradient-reduction variants shift the learned curve's shape — but none of them resolves into a measurable accuracy difference.
- Curve change and accuracy cost are decoupled: max-within-last-block moves the learned curve 2–3x more than last-block-sum does, yet costs *less* accuracy.
- The real finding: the two blocks' own coefficient gradients actively **oppose** each other — cosine similarity −0.24 on FMNIST, −0.43 on CIFAR-10.

## Insights

- Sharing one set of coefficients across the whole network forces an average of two blocks that structurally want different curve shapes — the shared coefficients are a compromise, not a consensus, and the more layers disagree (CIFAR-10's −0.43 vs. FMNIST's −0.24) the more that compromise is doing.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
