---
layout: article
title: "What Happens When You Let It Memorize 10 Images a Class"
permalink: /experiments/imagenet1k-overfit10/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Train FAct on a fixed 10-images-per-class subset of ImageNet-1K for 100 epochs — enough to memorize the training set outright — and watch what the learned activation does as it does so.

| | |
|---|---|
| **GPU(s)** | H200 |
| **Dataset(s)** | ImageNet-1K (10 images/class subset) |
| **Model** | ViT, depth 6 (embed_dim 384) — FAct K=2, global |

<img src="/images/Experiments-Attempted-But/imagenet1k-overfit10.png" alt="What Happens When You Let It Memorize 10 Images a Class — result chart" style="max-width:100%">

## Result summary

- train_acc reaches **99.6%** — essentially perfect memorization of 10 images per class.
- val/test accuracy sits at roughly **2%** the whole time — no generalization at all, as expected from that little data.
- The activation's amplitude keeps growing as memorization proceeds, especially outside the ±π window the GELU-fit coefficients were trained inside.
- Added a reusable `--train-samples-per-class` flag to the shared training/data scripts, since this kind of subset-size probe turned out useful enough to keep.

## Insights

- A learned activation isn't just shape-fitting the data distribution in some abstract sense — under pure memorization pressure it visibly deforms outside its original fitted range, which is a concrete, visible signature of overfitting living in the activation's own coefficients, not just in the weights.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
