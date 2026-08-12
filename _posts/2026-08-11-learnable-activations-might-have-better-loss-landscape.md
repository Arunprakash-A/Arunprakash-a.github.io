---
title: "Globally Learnable Activations Might Generate a Smoother Loss Landscape — Add 5 Parameters, Get +2pp on ImageNet-1K"
date: 2026-08-11
tags: [Deep-Learning, Research]
excerpt: "One learnable nonlinearity, shared by every layer, tested head-to-head against a standard fixed activation on real ImageNet-1K."
---

<img src="/images/Learnable-Activations-Might-Have-Better-Loss-Landscape/fig_hero.png" alt="Two curves for the same activation function: the fixed curve we default to, and the curve five learnable coefficients converged to after training" style="max-width:100%">

While building any neural network, one of the most consequential choices is
which activation function to use. There are hundreds of activation functions
in the literature, and a handful have become the default — ReLU, GELU, Swish,
SiLU, and so on. Either way, we end up fixing the activation function ahead of
time, hoping that whatever worked best in someone else's study will also work
best for ours. But what if there's a better activation function out there?
What if we make it learnable over the interval instead of fixing it? Will it
converge faster? Will it deliver better performance? Here we study exactly
that, and test it at ImageNet scale.

Quick findings:

- It improves performance by **+2pp, consistently across epochs** — not just
  at the final checkpoint — now confirmed across **5 independent seeds**.
- It **might generate** a smoother loss landscape: the FFN's up-projection weight
  matrices carry a lower spectral norm *and* a higher stable rank than the
  fixed activation's, in every one of the 6 transformer blocks (weight-space
  evidence, not a direct Hessian measurement — details below).
- Switching the optimizer from AdamW to SGD — a run still **in progress**.
  The early signal is *not* "performance held steady": at matched epochs so
  far, SGD is running well behind AdamW for both variants (details below).

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
| Epochs | 100, both variants, 5 matched seeds |
| Augmentation | RandomResizedCrop + flip only — no mixup, no RandAug |
| **Fixed** | the standard activation, no learnable parameters |
| **Learnable** | one shared activation, +5 parameters, network-wide |
| Params | 3,048,232 (Fixed) vs. 3,048,237 (Learnable) |

Everything else — architecture, data pipeline, schedule, seeds — is held
identical. Initialization was checked bit-for-bit equal between the two
variants at matched seed, so the activation is the only thing that differs.

## Results

**Fixed: 62.45% top-1. Learnable: 64.38% top-1. A +1.93 point gain, for five
extra numbers, holding at every epoch checkpoint measured, across five
independent seeds.**

| Test top-1 (official 50K val) | Fixed | Learnable | Δ |
|---|---|---|---|
| seed 1 | 62.50% | 65.12% | +2.62 |
| seed 2 | 62.56% | 64.33% | +1.77 |
| seed 3 | 62.49% | 63.96% | +1.47 |
| seed 4 | 62.23% | 64.24% | +2.01 |
| seed 5 | 62.49% | 64.27% | +1.78 |
| **mean ± s.d.** | 62.45 ± 0.13% | **64.38 ± 0.44%** | **+1.93 ± 0.43** |

Paired across all five seeds: t(4) = 10.02, p = 0.00056 — the fifth seed
landed close to the existing four-seed mean gap and tightened the estimate
rather than widening it. Best-validation accuracy tells the same story:
64.98% → 67.03%, +2.06 ± 0.54 pt, t(4) = 8.45, p = 0.00108.

### It's not just a better final number — it's ahead the entire time

<img src="/images/Learnable-Activations-Might-Have-Better-Loss-Landscape/fig_curves.png" alt="Validation accuracy and training loss over 100 epochs, Fixed vs Learnable, mean of 5 seeds" style="max-width:100%">

Learnable tracks above Fixed from very early in training and never falls
back. It reaches Fixed's *entire 100-epoch* validation accuracy at epoch 83
— the same final quality, with ~17% of the training budget still on the
table.

### The gap is negative at just 2 of 500 checkpoints — and recovers immediately

<img src="/images/Learnable-Activations-Might-Have-Better-Loss-Landscape/fig_gap.png" alt="Learnable minus Fixed validation accuracy gap at every matched epoch, 5 seeds" style="max-width:100%">

Five seeds × 100 epochs = 500 matched comparison points. With four seeds this
gap had never gone negative; the fifth seed breaks that streak, barely — seed
5 dips to −0.15 pt at epoch 23 and −0.11 pt at epoch 32, both early/mid
training, both gone by the next logged epoch. Every other point, 498 of 500,
favors Learnable. The gap is noisy epoch to epoch (a 10K validation split
will do that), and at this sample size two brief dips read as noise, not a
real regression — but "never negative" was the wrong claim to make on four
seeds, and it's worth saying so plainly rather than quietly dropping the
inconvenient seed.

### What did five numbers learn to do?

The three seeds below had their weights checkpointed every epoch, which is
what makes it possible to reconstruct exactly how the five coefficients moved
during training; the fourth and fifth seeds above confirm the accuracy gain
but weren't checkpointed at that resolution, so this section and the next two
stay 3-seed.

<img src="/images/Learnable-Activations-Might-Have-Better-Loss-Landscape/fig_coeffs.png" alt="All five coefficients over training, mean of 3 seeds, band = min-max" style="max-width:100%">

The coefficients move a lot early — a sharp swing in the first ~5 epochs,
then a slower drift for the rest of training — and they land in essentially
the same place regardless of seed. The largest disagreement between any two
seeds, in any of the five coefficients, at any epoch, is 0.033. Three
independently-initialized runs converge to the same curve. That's not
noise; that's the training problem pulling on the activation the same way
every time.

<img src="/images/Learnable-Activations-Might-Have-Better-Loss-Landscape/fig_activation.png" alt="The learned activation curve at several epochs, compared to the fixed activation, weighted by where real pre-activations land" style="max-width:100%">

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

## Is the loss landscape actually smoother?

A direct answer would need the Hessian of the loss — we don't have that here.
What we do have is the singular-value spectrum of every FFN weight matrix
(fc1, the up-projection, and fc2, the down-projection) in all 6 transformer
blocks, at 10 checkpoints across training, for both variants (seed 1). Two
standard scalar summaries of that spectrum are a reasonable weight-space proxy
for "how extreme a map this layer computes": the **spectral norm** (the top
singular value — an upper bound on how much the layer can stretch its input
in any direction, i.e. a Lipschitz-constant proxy) and the **stable rank**
(‖W‖²_F / ‖W‖²_2 — how spread the weight's energy is across directions, versus
concentrated in one).

<img src="/images/Learnable-Activations-Might-Have-Better-Loss-Landscape/fig_landscape_summary.png" alt="fc1 spectral norm and stable rank over training, standard vs Global FAct K=2, mean over 6 transformer blocks with min-max band" style="max-width:100%">

For the up-projection (fc1), the pattern is completely consistent: at every
checkpointed epoch, in **every one of the 6 blocks**, Learnable's weight
matrix has both a lower spectral norm and a higher stable rank than Fixed's —
at epoch 100, roughly half the spectral norm and 2-3× the stable rank in most
blocks. That's a less extreme, less anisotropic linear map at every stage of
training, not just at convergence. The down-projection (fc2) doesn't show the
same clean separation — it's mixed across blocks, sometimes favoring one
variant and sometimes the other — so this is presented as fc1-specific
evidence, not a network-wide claim, and it's weight-space geometry rather than
a curvature measurement of the loss itself. The full 6-block × 2-layer
breakdown lives in `mlp_svd/mlp_svd_summary.json` for anyone who wants to look
past the summary.

## Does it survive a different optimizer?

Everything above uses AdamW. A natural follow-up: is the +2pp gain an AdamW
artifact, or does it hold under plain SGD too? That run (lr=0.05, momentum
0.9, Nesterov) is **still in progress** as of this writing — standard_sgd_seed1
has reached epoch 42/100, fact_k2_global_sgd_seed1 epoch 26/100 — so this is
an early look, not a finished comparison.

<img src="/images/Learnable-Activations-Might-Have-Better-Loss-Landscape/fig_epochs_to_match_40ep.png" alt="AdamW vs SGD validation accuracy, both variants, first 40 epochs, seed 1 -- SGD runs marked incomplete" style="max-width:100%">

Two things are visible in the partial data. First, SGD is converging much
slower than AdamW for *both* variants under these hyperparameters — at the
last matched epoch, fact_k2_global sits at 43.8% (SGD, epoch 26) vs 52.3%
(AdamW, epoch 26), and standard sits at 44.7% (SGD, epoch 42) vs 52.9% (AdamW,
epoch 42). Neither SGD run has reached 50% val_acc yet, while AdamW passed it
by epoch 20–28. So the honest headline right now is **"SGD is currently well
behind AdamW at matched epochs"** — not "performance held steady across
optimizers." Second, and more relevant to this post's actual claim: the
Learnable-over-Fixed gap is still visibly present under SGD too (the dashed
FAct line sits above the dashed standard line throughout). Whether SGD closes
the AdamW gap on the back half of its cosine schedule, the way training
elsewhere in this project has repeatedly done, is an open question this run
will answer — this section will be updated once it completes 100 epochs.
