---
layout: article
title: "What If You Just Take the Max of GELU and FAct?"
permalink: /experiments/gelu-fact-hybrid-max/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Build a per-neuron max(GELU(x), FAct-K2(x)) hybrid activation and see whether it captures the best of both, on a depth-1 ViT on CIFAR-10.

| | |
|---|---|
| **GPU(s)** | A100 |
| **Dataset(s)** | CIFAR-10 |
| **Model** | ViT, depth 1 |

<img src="/images/Experiments-Attempted-But/gelu-fact-hybrid-max.png" alt="What If You Just Take the Max of GELU and FAct? — result chart" style="max-width:100%">

## Result summary

- 5-seed AdamW result: FAct-alone wins outright, **0.5805** test accuracy vs. the hybrid's 0.5754 — the hybrid lands *between* FAct-alone and GELU-alone, not above either.
- A plain-SGD ablation (momentum=0, seed 0 only) shows no rankable gap between the three variants at all — accuracies bunched around 0.42–0.44.

## Insights

- Taking the max of two activations doesn't inherit the better one's advantage — it dilutes it. Whatever FAct is doing that GELU isn't, `max()` throws part of it away rather than combining the two.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
