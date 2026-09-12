---
layout: article
title: "What If the FFN Can Only Learn on the Diagonal?"
permalink: /experiments/ffn-structure-ablation/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** A 4-part series (Experiments 95-98) restricting the ViT-100K FFN's fc1/fc2 weights to a diagonal, a swept diagonal band, a fixed diagonal subset, and IIR-initialized bands — asking how much of the FFN's dense connectivity FAct's advantage actually needs.

| | |
|---|---|
| **GPU(s)** | not recorded individually (FMNIST, single-seed scale, shared GPU fleet) |
| **Dataset(s)** | FashionMNIST |
| **Model** | ViT-100K, FAct K=2 (global) vs. GELU, restricted-connectivity FFN |

<img src="/images/Experiments-Attempted-But/ffn-structure-ablation.png" alt="What If the FFN Can Only Learn on the Diagonal? — result chart" style="max-width:100%">

## Result summary

- An apparent "step" in accuracy between band-width 2 and band-width 4 (seen in an early pass) was later retracted: it was a seed-0 artifact, not a real effect.
- Once measured properly, the margin's standard deviation across this series is **3x the per-arm standard deviation** — the noise between arms dwarfs the noise within any one arm.

## Insights

- The retraction is the finding: single-seed margins in a series like this are actively misleading — a visually clean step-function result evaporated once seed variance was accounted for. A useful caution against reading structure into a one-seed sweep, including some of the earlier (frozen) results in this same series.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
