---
layout: article
title: "Taking FAct Out of Vision and Into Language Modeling"
permalink: /experiments/nanogpt-fact-vs-gelu/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Drop the frozen, ImageNet-learned FAct K=2 curve into Karpathy's nanoGPT (autoregressive, decoder-only) trained on OpenWebText, to test whether the convergence-speed edge transfers to a new architecture family and modality.

| | |
|---|---|
| **GPU(s)** | H200 |
| **Dataset(s)** | OpenWebText |
| **Model** | nanoGPT (GPT-2 scale, n_layer=6/n_head=6/n_embd=384 baby-GPT recipe for smoke tests; full OWT config for the live run) |

<img src="/images/Experiments-Attempted-But/nanogpt-fact-vs-gelu.png" alt="Taking FAct Out of Vision and Into Language Modeling — result chart" style="max-width:100%">

## Result summary

- The trainable-coefficient run **diverged** at iterations 23k–24k — val loss jumped from 3.16 to 6.64, no NaN, the activation's own coefficients ran away.
- The best checkpoint before divergence (21k iterations) was kept safely.
- Measuring the actual pre-activation distribution (std 0.544, not the textbook N(0,1) assumption) shrinks the apparent GPT-2-vs-ImageNet gap in behavior from 24x down to **4.1x** the seed-to-seed noise floor.
- By this measure, the two learned curves (the GPT-2 one and the ImageNet one) end up closer to each other than either is to GELU.
- The learned curve's trajectory through coefficient space is **95.9% one-dimensional** by PCA — despite having 5 coefficients, it's essentially learning along a single direction.

## Insights

- The clean win seen in vision doesn't transfer for free — language modeling's own dynamics can destabilize a trainable periodic activation in a way vision training didn't. But the divergence isn't evidence FAct "doesn't work" for language; it's a sign the same coefficients need different guardrails (gradient clipping, an LR schedule tuned for this loss landscape) in a new domain.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
