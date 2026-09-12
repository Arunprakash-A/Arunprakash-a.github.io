---
layout: article
title: "Freeze the Learned Curve, Train From Scratch Again"
permalink: /experiments/imagenet1k-learned-activation-fixed/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Take the K=2 curve FAct converges to on ImageNet-1K, freeze it into a fixed nonlinearity, and retrain a fresh network with no learnable activation at all — where does it land relative to GELU and to the fully trainable version?

| | |
|---|---|
| **GPU(s)** | H200 |
| **Dataset(s)** | ImageNet-1K |
| **Model** | ViT, depth 6 (embed_dim 384) |

<img src="/images/Experiments-Attempted-But/imagenet1k-learned-activation-fixed.png" alt="Freeze the Learned Curve, Train From Scratch Again — result chart" style="max-width:100%">

## Result summary

- Frozen learned curve: **0.6390** test top-1 — beats GELU's 0.6250 by +1.4pt, and stays ahead across all 100/100 epochs.
- Trainable FAct (the original, coefficients still learning): **0.6512** — 1.2pt further ahead of the frozen version.
- Ranking: trainable > frozen > GELU, with real daylight between each pair.

## Insights

- The shape alone is worth +1.4pt over GELU even with zero learning happening in the activation at train time — the curve FAct finds is doing something GELU's fixed shape doesn't, independent of adaptivity.
- But letting the coefficients keep moving during training is worth a further 1.2pt on top of that, so the shape and the adaptivity are both contributing, not one explaining all of the other.
- This is the result that made a *transferable* nonlinearity a serious idea worth its own follow-up work: a frozen 5-number object beating GELU means it can be lifted into other networks (see the transfer post on the main blog).

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
