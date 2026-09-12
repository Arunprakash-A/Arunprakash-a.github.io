---
layout: article
title: "Let the Fourier Series Choose Its Own Frequency, Too"
permalink: /experiments/wmt14-learnable-w/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Add a learnable fundamental frequency w (started at 0.5, half the standard rate) to FAct's Fourier series on WMT14, on top of the usual learnable amplitude coefficients — testing 1-layer and 6-layer configurations.

| | |
|---|---|
| **GPU(s)** | A100 and H200 (a ~0.3 BLEU host effect between them swamps the arm effect at this scale) |
| **Dataset(s)** | WMT14 English→German |
| **Model** | 1-encoder/1-decoder-layer and 6-layer Transformer, FAct K=2/K=3/K=5 with learnable w |

<img src="/images/Experiments-Attempted-But/wmt14-learnable-w.png" alt="Let the Fourier Series Choose Its Own Frequency, Too — result chart" style="max-width:100%">

## Result summary

- The learnable-w treatment adds exactly **6 parameters** to the whole network (a0, a1, a2, b1, b2, w) — 26,302,470 vs. GELU's 26,302,464.
- Starting w at 0.5 means the model is deliberately **not** GELU-equivalent at step 0 — evaluating the GELU-fit coefficients at half frequency gives the fitted curve stretched 2x horizontally, a real, intentional design choice rather than a neutral initialization.
- Directory naming caught out even the study's own authors: despite being called "l1" throughout, the folder also holds a 6-layer arm (`L6_K3_w0.5`) — depth is carried by the result-tag suffix, not the directory name.

## Insights

- The headline engineering result here is really about hygiene, not accuracy: a shared codebase reused across depths needs its run identifiers to carry the configuration that actually varies (depth), not just live in a directory name nobody re-reads three studies later.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
