---
title: "Learnable Activations Might Have Better Loss Landscape — Add 5 Parameters, Get +2pp on ImageNet-1K"
date: 2026-08-11
tags: Deep-Learning Research
key: "LALL1108"
pageview: true
comment: true
mathjax: false
---

<img align="center" src="/images/Learnable-Activations-Might-Have-Better-Loss-Landscape/fig_hero.png">

Every transformer block in every ViT you've trained calls `nn.GELU()` and never
thinks about it again. The nonlinearity is treated like a fact of nature —
fixed at design time, identical in every layer, never touched by the
optimizer. That's one assumption. Here's the experiment for dropping it:
replace GELU everywhere in the network with a **single, shared, learnable
curve** — one small set of numbers, the same ones used in every block — and
let gradient descent shape it along with everything else.

<!--more-->

## The idea, stripped to its core

A standard network picks an activation function once and fixes it. This
experiment instead gives the network **one activation module, shared by
reference across every layer**, and makes that curve itself a learnable
function: it's a linear combination of five coefficients, initialized to
closely approximate the shape of the fixed activation it replaces, and then
trained by ordinary backprop exactly like any other weight. The entire
network — six transformer blocks, millions of activations computed per
forward pass — is bottlenecked through the same five numbers.

Two things make this a clean test rather than a bigger model in disguise:

- **It's shared, not per-layer.** One activation object, passed by reference
  into every block. Five parameters for the whole network, not five per
  layer.
- **It's tiny.** Five extra scalars against three million weights — a
  parameter increase small enough to round to zero.

If this helps, the interesting claim isn't "bigger activation modules are
good" — it's that *what shape the nonlinearity takes* is doing more work
than we usually give it credit for, and handing that shape to gradient
descent is cheap.

## The setup

| | |
|---|---|
| Model | depth-6 ViT-Ti/16 (patch 16, 224×224, d_model=192, 6 heads) |
| Dataset | ImageNet-1K — 1.27M train / 10K val / 50K official test |
| Optimizer | AdamW, lr 1e-3, weight decay 0.05, cosine schedule, 5-epoch warmup |
| Epochs | 100, both variants, 4 matched seeds |
| Augmentation | RandomResizedCrop + flip only — no mixup, no RandAug |
| **Fixed** | the standard activation, no learnable parameters |
| **Learnable** | one shared activation, +5 parameters, network-wide |
| Params | 3,048,232 (Fixed) vs. 3,048,237 (Learnable) |

Everything else — architecture, data pipeline, schedule, seeds — is held
identical. Initialization was checked bit-for-bit equal between the two
variants at matched seed, so the activation is the only thing that differs.

## Results

**Fixed: 62.44% top-1. Learnable: 64.41% top-1. A +1.97 point gain, for five
extra numbers, holding at every epoch checkpoint measured, across four
independent seeds.**

| Test top-1 (official 50K val) | Fixed | Learnable | Δ |
|---|---|---|---|
| seed 1 | 62.50% | 65.12% | +2.62 |
| seed 2 | 62.56% | 64.33% | +1.77 |
| seed 3 | 62.49% | 63.96% | +1.47 |
| seed 4 | 62.23% | 64.24% | +2.01 |
| **mean ± s.d.** | 62.44 ± 0.15% | **64.41 ± 0.50%** | **+1.97 ± 0.48** |

Paired across all four seeds: t(3) = 8.13, p = 0.0039 — the fourth seed landed
almost exactly on the first three's mean gap and pulled the estimate tighter,
not weaker. Best-validation accuracy tells the same story: 65.02% → 67.09%,
+2.07 ± 0.63 pt, t(3) = 6.58, p = 0.0071.

### It's not just a better final number — it's ahead the entire time

<img align="center" src="/images/Learnable-Activations-Might-Have-Better-Loss-Landscape/fig_curves.png">

Learnable tracks above Fixed from very early in training and never falls
back. It reaches Fixed's *entire 100-epoch* validation accuracy at epoch 82
— the same final quality, with ~18% of the training budget still on the
table.

### The gap never goes negative — not once, across 400 checkpoints

<img align="center" src="/images/Learnable-Activations-Might-Have-Better-Loss-Landscape/fig_gap.png">

Four seeds × 100 epochs = 400 matched comparison points. The worst single
point across all of them is +0.09 pt. The gap is noisy epoch to epoch (a 10K
validation split will do that) but it is never in Fixed's favor.

### What did five numbers learn to do?

The three seeds below had their weights checkpointed every epoch, which is
what makes it possible to reconstruct exactly how the five coefficients moved
during training; the fourth seed above confirms the accuracy gain but wasn't
checkpointed at that resolution, so this section and the next two stay
3-seed.

<img align="center" src="/images/Learnable-Activations-Might-Have-Better-Loss-Landscape/fig_coeffs.png">

The coefficients move a lot early — a sharp swing in the first ~5 epochs,
then a slower drift for the rest of training — and they land in essentially
the same place regardless of seed. The largest disagreement between any two
seeds, in any of the five coefficients, at any epoch, is 0.033. Three
independently-initialized runs converge to the same curve. That's not
noise; that's the training problem pulling on the activation the same way
every time.

<img align="center" src="/images/Learnable-Activations-Might-Have-Better-Loss-Landscape/fig_activation.png">

Panel A is the part that matters: zoomed to the range where the network's
actual pre-activations live (panel C shows that distribution directly), the
learned curve settles into something with a bit more curvature than the
fixed activation it started from — not a wild departure, but a real,
reproducible reshaping of the function every unit in the network is
computing.

## Questioning common assumptions about the shape of the activation

- **Monotonicity isn't load-bearing.** Local max at t ≈ −0.87, local min at
  t ≈ +0.19 — two real, seed-independent inflections sitting right where the
  network's own pre-activations actually live (mean |t| ≈ 0.33, 99% within
  1.21), not off in some rarely-visited tail.

- **The slope at zero didn't shrink toward the fixed activation's — it
  crossed to the other side and stayed there.** +0.5 (fixed) → **−0.35**
  (learned, epoch 100), reproducible to the third decimal across all three
  seeds (−0.352, −0.356, −0.339).

- **The one feature credited with the fixed activation's edge over ReLU
  relocated instead of disappearing.** Its dip sat at t ≈ −0.75; in the
  learned curve that region is lifted to a small positive bump, and the dip
  reappears just past zero, at t ≈ +0.19.

- **A shape this specific, reproduced this exactly, argues against "any
  smooth default will do."** Three independent seeds, under active weight
  decay, land on the same non-monotonic, sign-flipped curve.

- **Getting the far field "wrong" costs nothing, because the far field is
  empty.** The curves diverge sharply past |t| ≈ 2, but essentially no real
  pre-activation ever lands there (0.013% outside ±π, none outside ±2π).
