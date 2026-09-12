---
layout: article
title: "A Real Translation Benchmark, Not a Toy"
permalink: /experiments/wmt14-fact-vs-paper-baseline/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Test FAct against GELU on WMT14 English→German with a proper base Transformer (real BPE tokens, the actual "Attention Is All You Need" recipe) — the first FAct-vs-GELU comparison in this project on a benchmark anyone would call a real translation system.

| | |
|---|---|
| **GPU(s)** | H200 |
| **Dataset(s)** | WMT14 English→German |
| **Model** | Base Transformer ("Attention Is All You Need" recipe, Pre-LN, BPE tokens) |

<img src="/images/Experiments-Attempted-But/wmt14-fact-vs-paper-baseline.png" alt="A Real Translation Benchmark, Not a Toy — result chart" style="max-width:100%">

## Result summary

- 2-seed, 50k-step **test**-set result: FAct beats GELU by **+0.639 BLEU** and **+0.471 chrF**.
- Within-arm seed spread is tiny: only 0.022 BLEU between GELU's two seeds — the FAct-GELU gap is well outside that noise.
- The earlier "all activations tie at 40k steps" finding held only on the **validation** set — val actually ranked the arms backwards from the real test-set result.
- A third arm (vReLU, 1 seed) lands between GELU and FAct — so the honest claim is "FAct beats GELU," not "FAct beats every activation tried."

## Insights

- The val-vs-test discrepancy is the real lesson here: this project's earlier read of this comparison ("ties at 40k") was an artifact of trusting the validation set, which ranked the arms in the wrong order relative to the test set that actually matters. On a benchmark with an established SOTA reference, FAct's edge over GELU replicates cleanly.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
