---
layout: article
title: "Fifteen Tiny Tabular Datasets, No Overall Winner — Except Two"
permalink: /experiments/tabmini-lowdata/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Test GELU vs. FAct on the TabMini/PMLBmini suite of real-world tabular datasets with N≤500 rows, where deep nets are usually a bad idea in the first place, and see if either activation has an edge.

| | |
|---|---|
| **GPU(s)** | not recorded (tabular MLPs, N≤500 rows — seconds per run) |
| **Dataset(s)** | TabMini / PMLBmini (15 real-world N≤500 tabular datasets) |
| **Model** | MLP (width-16 config), logistic-regression baseline included |

<img src="/images/Experiments-Attempted-But/tabmini-lowdata.png" alt="Fifteen Tiny Tabular Datasets, No Overall Winner — Except Two — result chart" style="max-width:100%">

## Result summary

- Across the 15-dataset suite, mean AUC is noise-level tied between GELU and FAct — no overall winner.
- On **mux6** (a 6-input multiplexer Boolean function, 128 rows): FAct K=2 test AUC **0.977** vs. GELU 0.941 vs. logistic regression 0.719.
- On **parity5** (5-bit parity, 32 rows — the hardest possible case for a linear model): FAct K=3 **0.664**, FAct K=2 0.627, vs. GELU 0.467, vs. logreg 0.200.
- Both are exactly the two datasets where logistic regression fails hardest — FAct's edge shows up precisely where the underlying function is least linearly separable.

## Insights

- FAct's advantage on tabular data isn't a blanket "deep learning beats logreg" story — it's concentrated on the two datasets whose ground-truth function is a genuine Boolean XOR-like structure, i.e. it's dataset-structure-dependent, not a simple extension of the MNIST/CIFAR image results.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
