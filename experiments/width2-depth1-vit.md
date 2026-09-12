---
layout: article
title: "Can Width Substitute for Depth?"
permalink: /experiments/width2-depth1-vit/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Build a width=2, depth=1 ViT (parallel attention heads summed into a single FFN) and compare it against the standard deeper network, to see whether extra width at minimal depth can match it — and whether FAct's advantage survives the swap.

| | |
|---|---|
| **GPU(s)** | L4 |
| **Dataset(s)** | FashionMNIST |
| **Model** | ViT, width=2/depth=1 (parallel-attention, single FFN) vs. standard depth |

<img src="/images/Experiments-Attempted-But/width2-depth1-vit.png" alt="Can Width Substitute for Depth? — result chart" style="max-width:100%">

## Result summary

- Width does **not** substitute for depth: all 3 activations tested lose about 3 points of accuracy at width=2/depth=1, despite the width variant using 31.7% fewer parameters (a confound the study flags, not resolves).
- FAct's margin over GELU survives the swap but is roughly halved: +0.88/+0.79 (AdamW/SGD) at width=2/depth=1 vs. +1.42/+1.49 at standard depth.
- One seed only — the margin shrinkage is a real observation, but not resolvable as statistically significant at n=1.

## Insights

- Depth is doing real work that width alone can't replace, and FAct's edge shrinks (though doesn't vanish) when depth is traded for width — consistent with the idea that FAct's advantage compounds somewhat with the number of activation applications a signal passes through.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
