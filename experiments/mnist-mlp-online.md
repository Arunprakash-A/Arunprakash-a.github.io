---
layout: article
title: "Rank-1 Is a Trap, Not a Wall"
permalink: /experiments/mnist-mlp-online/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Train a tiny 784→10→10 MLP online (batch_size=1, one pass) from an all-zero init and see whether the rank-1 symmetry that zero-init locks in can ever be escaped — with or without help.

| | |
|---|---|
| **GPU(s)** | not recorded (single pass, 784→10→10 online SGD — trivial compute) |
| **Dataset(s)** | MNIST |
| **Model** | MLP 784→10→10, zero-initialized, online (batch_size=1) |

<img src="/images/Experiments-Attempted-But/mnist-mlp-online.png" alt="Rank-1 Is a Trap, Not a Wall — result chart" style="max-width:100%">

## Result summary

- With no intervention, both GELU and FAct K=3 get stuck at a rank-1 (GELU: effectively rank-0) representation: final cumulative online accuracy 0.1099 (GELU) vs. 0.2931 (FAct K=3) — FAct's rank-1 subspace is at least live and trainable, GELU's collapses into a constant-class classifier.
- A one-time Gaussian noise kick injected into `fc1`'s pre-activation at epoch 5 of 10 rescues **both** variants decisively: GELU jumps to 0.9397 ± 0.0045 test accuracy, FAct K=3 to 0.9226 ± 0.0015 — both landing in the 92–94% range a normally-initialized run reaches.
- Longer training alone (FAct K=3, +10 more epochs, no kick) never breaks the rank-1 structure — exactly as the math predicts, since the constraint is structural, not a matter of not-enough-time.

## Insights

- Rank-1 collapse from zero-init isn't a capacity ceiling the network is straining against — it's unbroken symmetry, and unbroken symmetry can be broken by a single well-timed nudge, even most of the way through training.
- This directly informed the online CIFAR-10 study below, where the same even-K, phi'(0)=0 zero-init trap shows up again in a convolutional front end.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
