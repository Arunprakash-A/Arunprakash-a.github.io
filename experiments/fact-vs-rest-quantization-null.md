---
layout: article
title: "Post-Training Quantization Doesn't Care Which Activation You Used"
permalink: /experiments/fact-vs-rest-quantization-null/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Check whether INT8/INT4 post-training quantization damages FAct's networks more or less than the other 10 activations in the zoo, across ViT, ConvMLPMixer, and ConvNeXt.

| | |
|---|---|
| **GPU(s)** | analysis of checkpoints already trained across the project's H200/A100/V100/L4 fleet; the PTQ simulation itself is lightweight |
| **Dataset(s)** | FashionMNIST, CIFAR-10, CIFAR-100, Food-101 |
| **Model** | ViT / ConvMLPMixer / ConvNeXt (~100K-param scale), W4A8 and W4A32 simulated quantization |

<img src="/images/Experiments-Attempted-But/fact-vs-rest-quantization-null.png" alt="Post-Training Quantization Doesn't Care Which Activation You Used — result chart" style="max-width:100%">

## Result summary

- ViT/FMNIST, W4A8: FAct's accuracy drop under quantization is 0.264pp — statistically indistinguishable from the field's mean drop (0.287pp), p=0.47.
- ViT/CIFAR-100, W4A8: FAct drops 1.834pp vs. a field mean of 1.537pp — here FAct is *more* fragile, not less (p=0.013).
- ConvMLPMixer/FMNIST, W4A8: FAct drops only 1.228pp against a field mean of 7.118pp — the most robust arm on that architecture.
- No consistent direction: FAct is sometimes the most robust activation under quantization and sometimes among the least, depending on architecture and dataset.

## Insights

- This is a clean null result, and the project dropped this line of investigation afterward: whatever FAct is doing for accuracy, it isn't reliably making (or breaking) a network's tolerance for low-precision inference. Post-training quantization is simply not a lens that discriminates between these activations.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
