---
layout: article
title: "Same 2D Patterns, Different Number of Classes"
permalink: /experiments/class-count-series/
mathjax: false
pageview: true
comment: true
---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)

**Objective.** Re-run the 2D-patterns width sweep at C=2, 3, and 10 classes, to see whether FAct's edge and its convergence-speed advantage depend on how many classes the toy problem has.

| | |
|---|---|
| **GPU(s)** | A100 (predominant across this series) |
| **Dataset(s)** | 2D-Patterns toy suite (circles, spirals, pinwheel, etc.), C ∈ {2, 3, 10} |
| **Model** | Small MLP, width sweep |

<img src="/images/Experiments-Attempted-But/class-count-series.png" alt="Same 2D Patterns, Different Number of Classes — result chart" style="max-width:100%">

## Result summary

- FAct's accuracy edge is largest at **narrow width**: +18.1pt at H=2, shrinking to essentially 0 (−0.1pt) at the width where accuracy peaks.
- FAct converges 1.8–6.7x faster (fewer epochs to target accuracy) on 5 of 6 patterns tested.
- A width-2 network solves the 10-class circles pattern at **95.5%** accuracy — a striking result for a 2-unit hidden layer on a 10-way problem.
- A matched-per-class control shows the largest margins (spirals, pinwheel) are a **data-efficiency** effect, not a higher accuracy ceiling — FAct gets there with less data/width, not to a better final place.

## Insights

- FAct's advantage is concentrated exactly where capacity is scarce (narrow width) and where speed matters (fewer epochs) — once the network has enough width to solve the problem outright, the two activations converge to the same ceiling. This reframes FAct's edge as being about efficient use of limited capacity, not unlocking a higher ceiling.

---

[← Back to the full catalog](/2026/09/12/experiments-attempted-but.html)
