---
layout: article
title: "What If the Network Has to Emit a Sinusoid, Not a Class Label?"
permalink: /experiments/structured-target-study/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Replace the usual classification target with structured regression targets (sinusoid, DFT coefficients, phase) and a CE+DFT mixture loss, to see whether FAct's periodic structure gives it a home-field advantage when the target itself is periodic.

| | |
|---|---|
| **GPU(s)** | A100 |
| **Dataset(s)** | FashionMNIST |
| **Model** | ViT-100K |

<img src="/images/Experiments-Attempted-But/structured-target-study.png" alt="What If the Network Has to Emit a Sinusoid, Not a Class Label? — result chart" style="max-width:100%">

## Result summary

- An early positive result turned out to be a width artifact: whenever the target dimension D exceeds 2× the number of classes C, aliasing forces a wide readout head, and that head width — not the activation — was driving the first round's apparent win.
- The nearest-target readout convention was found to be norm-biased, and argmax(T[c]) turned out to be 4-to-1 non-injective — two separate evaluation bugs that had to be fixed before any comparison could be trusted.
- Once corrected: EFAct is **1.6x less noise-robust** than GELU under the noise sweep — the opposite of a home-field advantage.

## Insights

- Two rounds of "FAct wins on periodic targets" evaporated on closer inspection into evaluation artifacts, and what survived scrutiny was a mild point *against* FAct (worse noise robustness). A useful reminder that a structured-target setup can smuggle in confounds (aliasing, non-injective label maps) that look like a real effect until you check the evaluation harness itself.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
