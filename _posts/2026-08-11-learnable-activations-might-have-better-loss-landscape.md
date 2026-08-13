---
title: "One Activation for the Whole Network"
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

**What this study is and isn't.** This isn't a run at the state of the art.
The model here is a small ViT trained on a deliberately plain recipe, and its
absolute accuracy is nowhere near the top of the ImageNet-1K leaderboard —
that was never the target. The point is narrower and, I'd argue, more
interesting: to isolate what happens when a single learnable activation is
shared across an entire network, holding everything else fixed, and to
measure that difference cleanly enough to trust it. Every comparison below is
against a baseline identical in every respect but the activation.

Quick findings:

- It improves performance by **+2pp, at 498 of the 500 matched epoch
  checkpoints** — not just at the final one — now confirmed across
  **5 independent seeds**.
- It **might reshape the network's landscape geometry**: the FFN's
  up-projection weight matrices carry a lower spectral norm *and* a higher
  stable rank than the fixed activation's, in every one of the 6 transformer
  blocks (weight-space evidence, not a direct Hessian measurement — details
  below).
- Swap the optimizer from AdamW to SGD and the **Learnable-over-Fixed gap
  still holds** — at all 100 epochs, with a mean margin even larger than
  under AdamW (+3.78pt vs +2.57pt). That's evidence it's the *activation*,
  not the optimizer, doing the work — though on one seed, not five.

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
extra numbers, holding at 498 of the 500 matched epoch checkpoints, across
five independent seeds.**

| Test top-1 (official 50K val) | Fixed | Learnable | Δ |
|---|---|---|---|
| seed 1 | 62.50% | 65.12% | +2.62 |
| seed 2 | 62.56% | 64.33% | +1.77 |
| seed 3 | 62.49% | 63.96% | +1.47 |
| seed 4 | 62.23% | 64.24% | +2.01 |
| seed 5 | 62.49% | 64.27% | +1.78 |
| **mean ± s.d.** | 62.45 ± 0.13% | **64.38 ± 0.44%** | **+1.93 ± 0.43** |

Paired across all five seeds: t(4) = 10.02, p = 0.00056. Best-validation
accuracy tells the same story: 64.98% → 67.03%, +2.06 ± 0.54 pt,
t(4) = 8.45, p = 0.00108.

### It's not just a better final number — it's ahead the entire time

<img src="/images/Learnable-Activations-Might-Have-Better-Loss-Landscape/fig_curves.png" alt="Validation accuracy and training loss over 100 epochs, Fixed vs Learnable, mean of 5 seeds" style="max-width:100%">

Learnable tracks above Fixed from very early in training and stays there,
with two brief exceptions covered in the next section. It reaches Fixed's
*entire 100-epoch* validation accuracy at epoch 83 on average across the five
seeds (individually: 80, 82, 87, 81, 84) — the same final quality, with ~17%
of the training budget still on the table.

### The gap is negative at just 2 of 500 checkpoints — and recovers immediately

<img src="/images/Learnable-Activations-Might-Have-Better-Loss-Landscape/fig_gap.png" alt="Learnable minus Fixed validation accuracy gap at every matched epoch, 5 seeds" style="max-width:100%">

Five seeds × 100 epochs = 500 matched comparison points. With four seeds this
gap had never gone negative; the fifth seed breaks that streak, barely — seed
5 dips to −0.15 pt at epoch 23 and −0.11 pt at epoch 32, both early/mid
training, both gone by the next logged epoch. Every other point, 498 of 500,
favors Learnable. The gap is noisy epoch to epoch (a 10K validation split
will do that), and at this sample size two brief dips read as noise, not a
real regression.

### What did five numbers learn to do?

The three seeds below had their weights checkpointed every epoch; the fourth
and fifth seeds above confirm the accuracy gain but weren't checkpointed at
that resolution, so this section and the next two stay 3-seed.

<img src="/images/Learnable-Activations-Might-Have-Better-Loss-Landscape/fig_coeffs.png" alt="All five coefficients over training, mean of 3 seeds, band = min-max" style="max-width:100%">

The coefficients move a lot early — a sharp swing in the first ~5 epochs,
then a slower drift for the rest of training — and they land in essentially
the same place regardless of seed. The largest disagreement between any two
seeds, in any of the five coefficients, at any epoch, is 0.033. Three
independently-initialized runs converge to the same curve. That's not
noise; that's the training problem pulling on the activation the same way
every time.

That early swing is also where the accuracy gain is widest. Averaged over the
five seeds, Learnable's lead over Fixed is **+3.15pt across epochs 1–5** —
peaking at +3.95pt at epoch 3 — against **+2.01pt over epochs 21–100**, once
the coefficients have largely settled. The advantage is at its largest while
the activation is still visibly changing shape, then narrows to a smaller
margin that holds steady for the rest of training. Most of what the five
parameters are worth, they appear to be worth early.

<img src="/images/Learnable-Activations-Might-Have-Better-Loss-Landscape/fig_activation.png" alt="The learned activation curve at several epochs, compared to the fixed activation, weighted by where real pre-activations land" style="max-width:100%">

Panel A is the part that matters: zoomed to the range where the network's
actual pre-activations live (panel C shows that distribution directly), the
learned curve settles into something with a bit more curvature than the
fixed activation it started from — not a wild departure, but a real,
reproducible reshaping of the function every unit in the network is
computing.

## Questioning common assumptions about the shape of the activation

- **Monotonicity isn't load-bearing here.** Local max at t ≈ −0.87, local min
  at t ≈ +0.19 — two real, seed-independent inflections sitting right where
  the network's own pre-activations actually live (mean |t| ≈ 0.33, 99%
  within 1.21), not off in some rarely-visited tail.

- **The slope at zero didn't shrink toward the fixed activation's — it
  crossed to the other side and stayed there.** +0.5 (fixed) → **−0.35**
  (learned, epoch 100), landing within 0.02 of each other across all three
  seeds (−0.352, −0.356, −0.339).

- **The one feature credited with the fixed activation's edge over ReLU
  relocated instead of disappearing.** Its dip sat at t ≈ −0.75; in the
  learned curve that region is lifted to a small positive bump, and the dip
  reappears just past zero, at t ≈ +0.19.

- **A shape this specific, reproduced this exactly, argues against "any
  smooth default will do."** Three independent seeds, under active weight
  decay, land on the same non-monotonic, sign-flipped curve.

- **Getting the far field "wrong" costs next to nothing, because the far
  field is nearly empty.** The curves diverge sharply past |t| ≈ 2, but
  almost no real pre-activation ever lands there (0.013% outside ±π, none
  outside ±2π).

## Does FAct Reshape the Spectral Geometry of the Network?

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
a curvature measurement of the loss itself.

## Is it the activation, or just AdamW?

Everything above uses AdamW. The obvious challenge: maybe the +2pp gain is an
AdamW artifact — some interaction between the learnable coefficients and
Adam's per-parameter adaptive updates — rather than a property of the
activation itself. If that were true, swapping in a different optimizer
should shrink or erase the gap. So the same seed-1 comparison was re-run
under plain SGD (lr=0.05, momentum 0.9, Nesterov) instead, for both variants.
**Both legs have now finished all 100 epochs** — an earlier version of this
section reported them mid-flight, over the first 31 epochs; what follows is
the completed comparison.

<img src="/images/Learnable-Activations-Might-Have-Better-Loss-Landscape/fig_sgd_gap.png" alt="The Learnable-minus-Fixed validation accuracy gap, AdamW vs SGD, over all 100 matched epochs, seed 1" style="max-width:100%">

**The gap survives the optimizer swap, and it's larger, not smaller.** Across
all 100 epochs, Learnable beats Fixed at every single epoch under SGD too —
mean gap +3.78pt (min +0.24, max +6.43, never negative), against a +2.57pt
mean for AdamW over the identical epochs. Two optimizers with unrelated
update rules, different learning rates, different implicit biases — same
qualitative result, same direction, same "never negative" pattern the AdamW
comparison showed on 4 of its 5 seeds. That's the actual validation this
section is after: the advantage isn't riding on AdamW's adaptive moments,
it's coming from the shape of the nonlinearity itself. The partial-run
numbers held up: the mean SGD gap settled from +4.09pt over the first 31
epochs to +3.78pt over all 100, still comfortably above AdamW's.

Under SGD the crossover is earlier, too. Learnable reaches Fixed's *entire
100-epoch* best validation accuracy at **epoch 67** — a third of the schedule
left over, against the epoch-83 crossover the AdamW runs showed.

All four runs on one pair of axes — both variants, both optimizers, the full
100 epochs:

<img src="/images/Learnable-Activations-Might-Have-Better-Loss-Landscape/fig_optimizer_compare.png" alt="Validation accuracy and validation loss over 100 epochs for all four runs: Fixed and Learnable, each under AdamW and SGD, seed 1" style="max-width:100%">

Within each optimizer, Learnable sits above Fixed for the whole run — solid
above solid, dashed above dashed. Between optimizers, the two AdamW curves sit
well above the two SGD ones throughout.

However, SGD *converged more slowly than AdamW in absolute terms* for both
variants under these particular hyperparameters, and it never caught up.
Final validation accuracy: Fixed 53.01% (SGD) vs 65.18% (AdamW), Learnable
56.65% (SGD) vs 67.68% (AdamW). That's a statement about optimizer speed, not
about the activation, and it's orthogonal to the gap result above — a
slower-converging optimizer can still show a larger relative advantage for
Learnable at matched epochs. So the question this section used to leave open
now has both halves answered: the Learnable-over-Fixed gap holds all the way
to epoch 100, and SGD's absolute level does not close on AdamW's. These are
single-seed results, unlike the five-seed AdamW comparison above, so they
carry correspondingly less weight.

## Limitations

**The accuracy is bought with wall-clock time.** A fixed activation like GELU
is one cheap elementwise op. The learnable one is a truncated Fourier series,
so every activation site evaluates four transcendental functions — two sines
and two cosines — instead. Standard FLOP counters miss this entirely: they
tally matmuls and convolutions, so both variants score an identical 1.283
GFLOPs forward and 3.791 GFLOPs forward+backward per image. The cost is real
nonetheless, because sin/cos run on the GPU's special-function units, which
have far less throughput than the tensor cores doing the matmuls.

Measured back-to-back on two **idle** GPUs — nothing else running on either —
with 10 warmup + 50 timed iterations, AMP, batch 256, the actual training
configuration. Each machine was benchmarked twice; the repeat runs agreed to
within 1% on the A100 and to within 0.05% on the V100:

| | Fixed | Learnable | overhead |
|---|---|---|---|
| **A100-PCIE-40GB** | | | |
| training step (batch 256) | 59.7 ms | 132.3 ms | **2.2×** |
| training, per epoch (1.27M images) | 4.9 min | 11.0 min | **2.2×** |
| training, full 100-epoch run | ~8.2 h | ~18.3 h | **2.2×** |
| inference (batch 256) | 0.075 ms/img | 0.179 ms/img | **2.4×** |
| inference, full 50K test set | ~3.8 s | ~9.0 s | **2.4×** |
| **V100-PCIE-32GB** | | | |
| training step (batch 256) | 95.0 ms | 209.4 ms | **2.2×** |
| training, per epoch (1.27M images) | 7.9 min | 17.3 min | **2.2×** |
| training, full 100-epoch run | ~13.1 h | ~28.9 h | **2.2×** |
| inference (batch 256) | 0.112 ms/img | 0.272 ms/img | **2.4×** |
| inference, full 50K test set | ~5.6 s | ~13.6 s | **2.4×** |

Two GPU generations apart, the *ratio* lands in the same place: **~2.2× to
train, ~2.4× to run inference**, even though the absolute numbers differ by
around 60%. The overhead looks like a property of the method, not of a
particular machine.

One caveat on measurement, since it cuts the other way from what you might
expect. An earlier version of this benchmark, run on an H200, reported only
1.3× training overhead, and it was tempting to read that as newer hardware
handling the transcendentals better. That number could not be reproduced:
the H200 in question is a shared box, and re-checking it found another
tenant's job holding it at 74–100% utilization, so it could not be
re-measured cleanly. Contention inflates both arms of a comparison by a
shared amount, which pulls any ratio *toward* 1 — so a busy machine will
understate this overhead rather than overstate it. The two idle-GPU numbers
above are the ones to trust. Batch-1 latency is omitted entirely: it swung by
79% between identical runs, so it measures launch jitter rather than the
model.

This matters for how the epoch-83 crossover should be read. Matched *per
epoch*, Learnable reaches Fixed's final accuracy with ~17% of the schedule
unused. Matched on *wall-clock*, it does not, and not narrowly: 83 epochs at
2.2× is about 1.8× the wall-clock cost of the Fixed baseline's full 100. So
the honest summary is better final quality for more compute, not the same
quality sooner. Whether the Fixed baseline would close
some of the 1.93pt gap if simply given the extra compute instead is a control
this study hasn't run, and it's the obvious next experiment.

**Scope.** Everything here is one architecture (a depth-6 ViT-Ti/16) on one
dataset, at a size and training budget well below what modern ImageNet results
use. The five-seed evidence is solid at that scale; whether the gap survives
at greater depth, width, or training length is genuinely untested.
