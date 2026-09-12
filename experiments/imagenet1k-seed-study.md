---
layout: article
title: "The 5-Seed ImageNet-1K Confirmation"
permalink: /experiments/imagenet1k-seed-study/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Confirm, with enough seeds to trust a p-value, that a single learnable activation shared across the whole network beats a fixed GELU at ImageNet-1K scale.

| | |
|---|---|
| **GPU(s)** | H200 |
| **Dataset(s)** | ImageNet-1K |
| **Model** | ViT, depth 6 (embed_dim 384) |

<img src="/images/Experiments-Attempted-But/imagenet1k-seed-study.png" alt="The 5-Seed ImageNet-1K Confirmation — result chart" style="max-width:100%">

## Result summary

- FAct (K=2, global, GELU-init) beat GELU at 498 of 500 matched epoch checkpoints across 5 seeds — not just at the final epoch.
- Mean margin: **+2 percentage points** top-1 test accuracy.
- 5-seed paired t-test: t(4)=10.02, p=0.00056.
- A later robustness pass (paired vs Welch, an RNG-desync check, a 120-pairing permutation test, unpaired/Mann-Whitney) all agreed, after a colleague raised the question at 3 seeds (p=0.029 back then).

## Insights

- This is the load-bearing result the whole project's other 33 experiments sit around: the underlying question in almost every study below is some variant of "does this still hold once you change X".
- A 5-seed t-test surviving four independent robustness checks is a rare thing to get to say about a deep-learning result — most of the value of doing this was building the checking machinery, not the extra seeds.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
