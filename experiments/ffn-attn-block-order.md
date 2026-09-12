---
layout: article
title: "Does FFN-First or Attention-First Matter — and For How Long?"
permalink: /experiments/ffn-attn-block-order/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Swap the order of the FFN and attention sublayers (FFN-first vs. the standard attention-first) across a d_ff sweep and 3 training-budget phases, on both FashionMNIST and CIFAR-10, to see whether block order is a convergence-speed effect or an accuracy-ceiling effect.

| | |
|---|---|
| **GPU(s)** | mixed: A100, V100, L4 |
| **Dataset(s)** | FashionMNIST, CIFAR-10 |
| **Model** | ViT-100K, FFN-first vs. Attention-first block order |

<img src="/images/Experiments-Attempted-But/ffn-attn-block-order.png" alt="Does FFN-First or Attention-First Matter — and For How Long? — result chart" style="max-width:100%">

## Result summary

- FashionMNIST: the block-order effect **decays to zero by 200 epochs** — a convergence-speed effect only, not a ceiling.
- CIFAR-10: the opposite pattern — the effect **grows from 20 to 100 epochs and then holds** at +3.2 to +3.5 percentage points all the way through 200 epochs — a real accuracy-ceiling effect, not just a head start.

## Insights

- The same architectural swap produces two qualitatively different kinds of effect on two different datasets — FashionMNIST treats block order as something training eventually trains around, CIFAR-10 treats it as a persistent structural advantage. A single dataset's convergence curve is not enough to tell which kind of effect you're looking at; you need to run it out to a stable budget.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
