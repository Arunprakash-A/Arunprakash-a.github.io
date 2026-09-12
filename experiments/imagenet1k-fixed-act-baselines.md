---
layout: article
title: "The Five-Way Fixed-Activation Scorecard"
permalink: /experiments/imagenet1k-fixed-act-baselines/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Round out the ImageNet-1K comparison with the fixed activations everyone actually reaches for in practice — ReLU, LeakyReLU, SiLU — under the exact same recipe as the FAct/GELU runs.

| | |
|---|---|
| **GPU(s)** | H200 |
| **Dataset(s)** | ImageNet-1K |
| **Model** | ViT, depth 6 (embed_dim 384) |

<img src="/images/Experiments-Attempted-But/imagenet1k-fixed-act-baselines.png" alt="The Five-Way Fixed-Activation Scorecard — result chart" style="max-width:100%">

## Result summary

- ReLU and LeakyReLU tie at **0.609** test top-1.
- SiLU reached **0.515** best-so-far at epoch 42/100 before this arm was left in progress — not a finished number.
- Against the same table's GELU (0.625) and trainable FAct (0.6512): FAct leads every fixed activation tried.
- A documentation slip surfaced along the way: the "identical parameter count" claim in the write-up was wrong — FAct actually carries +5 parameters (its shared coefficients), and `train_one()` was found to return `result.json` rather than write it to disk directly.

## Insights

- None of the standard fixed activations close the gap to FAct — the comparison isn't "FAct vs one arbitrary baseline," it's FAct ahead of the whole familiar shortlist.
- The SiLU arm was never watched by a monitoring script and nobody caught it stalling — a small operational lesson repeated elsewhere in this catalog: an unattended long run needs a watchdog, not just a launch command.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
