---
title: "One Activation for the Whole Network — at ImageNet-1K Scale"
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

## Related work — the idea is not new

Learning the activation instead of fixing it is an old idea, reinvented
independently in several communities. Nothing here is a claim to have thought
of it first — the map, in one table:

| | What's learned | Shared across | Activation params | IN-1K |
|---|---|---|---|---|
| ReLU / GELU | nothing | — | 0 | ✓ |
| [PReLU](https://arxiv.org/abs/1502.01852), Swish-β, [ACON](https://arxiv.org/abs/2009.04759) | a knob on a known shape | channel | ~1 / channel | ✓ |
| [APL](https://arxiv.org/abs/1412.6830) | shape, from hinges | neuron | 2S / neuron | |
| [PAU](https://arxiv.org/abs/1907.06732), [rational nets](https://arxiv.org/abs/2004.01902) | whole shape, rational basis | layer | ~10 / layer | ✓ |
| [DeepLABNet](https://arxiv.org/abs/1911.09257) | whole shape, RBF basis | unit | per unit | |
| [KAN](https://arxiv.org/abs/2404.19756), [F-KAN](https://arxiv.org/abs/2409.09323), [KAF](https://arxiv.org/abs/2502.06018) | whole shape, spline / Fourier | **every edge** | scales with weight count | ✓ |
| [SIREN](https://arxiv.org/abs/2006.09661) | nothing — ω₀ is a hyperparameter | — | 0 | |
| [STAF](https://arxiv.org/abs/2502.00869) | amplitude, frequency, phase | neuron | 3 / harmonic / neuron | |
| [GAAF](https://arxiv.org/abs/1906.01170), [LAAF](https://royalsocietypublishing.org/doi/abs/10.1098/rspa.2020.0334) | a *scale* inside a fixed shape | **whole network** / layer | **1 total** | |
| **This post** | **whole shape, Fourier basis** | **whole network** | **5 total** | **✓** |

*IN-1K = reports ImageNet-1K results; blank means not to my knowledge.*

**How this differs.** Everything that learns the whole *shape* pays for it
per layer, per unit or per edge: the activation budget grows with the
network. The one method that shares network-wide, GAAF,
shares a single scale inside a shape that never changes, on PINNs — and it
already claims faster convergence especially early in training, so the
early-epoch result later in this post corroborates theirs rather than
discovering anything. What I could not find is the conjunction: **the whole
shape, learned, shared by every layer, in a transformer, at ImageNet-1K
scale, against a matched baseline over multiple seeds.** Corrections welcome.

**And sharing has a second consequence: there is a single curve to look at.**
At ImageNet scale nobody has shown one, because nobody has had one to show.
PAU does plot its learned shapes — from Fashion-MNIST on VGG-8; its ImageNet
figures are accuracy and loss only. KAF shows no learned activation curves at
all. ACON shows β *distributions* rather than shapes. DY-ReLU's ImageNet
figure is the closest thing that exists, and it's a per-block scatter of
input/output values over 50,000 validation images — a cloud, because the
function changes with every input and every channel. Here the entire
network's nonlinearity is five numbers in a fixed basis, so the curve is
exact at every step of training and its whole history is a path in 5-D —
[which is what the figures below plot](#what-did-five-numbers-learn-to-do).

**Why a Fourier basis.** Five numbers serving an entire network have to be
well-behaved, and that is mostly a property of the basis:

- **Bounded, nothing to divide by** — |φ| ≤ 2.43 at init, since sin and cos
  live in [−1, 1]. Rational bases carry a denominator that can approach zero
  (PAU needs a "safe" variant to fence off the poles); polynomial bases have
  the opposite failure and diverge as |t| grows.
- **No vanishing gradient in the tails** — |φ′| ≤ 2.23 at init, and being
  periodic it does not *decay* with |t| the way sigmoid and tanh saturate. A
  large pre-activation isn't a dead one.
- **The basis never amplifies gradient to the coefficients** — ∂φ/∂a_k =
  cos(kt) and ∂φ/∂b_k = sin(kt), in [−1, 1] for any input at all. That bound
  matters more here than it would per-layer: these five accumulate gradient
  from every activation site in the network, every step.
- **Orthogonal on [−π, π]** — the five parameters move along near-independent
  directions. Monomial bases are ill-conditioned by comparison; splines need
  a grid range to tune. There's no grid here.
- **Graceful truncation, exact init** — coefficients of a smooth reference
  decay fast, so K=2 already carries the shape, and GELU's true coefficients
  are integrated directly rather than fitted.

It holds up in practice too: independent seeds [land within 0.02 of each
other](#questioning-common-assumptions-about-the-shape-of-the-activation).

That leaves two things under test — whether the global version survives real
scale (sharing is where it's *most* likely to break: one curve now serves
every layer, and transformer layers aren't doing the same job), and whether
it holds under a controlled measurement (five matched seeds, bit-identical
init, all 500 epoch checkpoints, a paired test). And one thing this post does
**not** establish: it's a two-arm comparison against fixed GELU, with no
Padé, spline or per-layer arm. The one alternative basis I did try —
Chebyshev polynomials — failed the way the bullet above says a polynomial
basis should: pre-activations ran away (past ±550 in one run, against the
Fourier runs' single digits) and the forward pass hit NaNs — which is where
that runaway ends up. It was slow to train on top of that, and not worth
pushing further.

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

### How many epochs does it save?

Another way to read the same gain: how many epochs each variant needs to
*first* reach a given validation accuracy, meaned over the five seeds.

| val-acc threshold | Fixed | Learnable | epochs saved |
|---|---|---|---|
| 50% | 27.6 ± 1.0 (5/5) | 22.2 ± 1.7 (5/5) | 5.4 |
| 55% | 49.6 ± 1.6 (5/5) | 42.4 ± 2.3 (5/5) | 7.2 |
| 60% | 70.8 ± 1.3 (5/5) | 61.4 ± 1.9 (5/5) | 9.4 |
| 65% | 98.5 ± 1.5 (2/5) | 82.8 ± 1.6 (5/5) | 16.5 (n=2) |

The bracketed fraction is how many of the five seeds cleared that threshold
at all inside 100 epochs. The saving widens as the bar rises — 5 epochs at
50%, 9 at 60% — and by 65% it stops being a saving and turns into a
difference in kind: all five Learnable runs get there, with a schedule to
spare, while only two of five Fixed runs manage it at all, and those two only
at epochs 97 and 100. The other three finish at 64.8%, 64.9% and 64.8%,
short of the line. That's why the last row is an n=2 comparison and the
weakest of the four.

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
nonetheless, and the reason is worth stating plainly:

> **`sin` and `cos` execute on the GPU's special-function units, which have far
> less throughput than the tensor cores doing the matmuls.**

The activation isn't competing for the same hardware the rest of the network
runs on — it's queued for a much narrower lane.

Worth adding that this is an *implementation* cost, not a mathematical one,
and that what's measured above is the naive implementation. It builds a
(batch × features × K) tensor of angles and calls `cos` and `sin` across all
of it, so K=2 really does evaluate four transcendentals per activation and
write three intermediates out to memory. Neither is necessary. The
double-angle identities give cos 2t and sin 2t from a single sin/cos pair
almost for free, and a fused kernel could keep the whole series in registers
instead of round-tripping through memory.

Attention was in this exact position once. The mathematics never changed; an
implementation that respected the memory hierarchy turned it from the thing
you budget around into the thing you stop thinking about. There's no
FlashAttention for learnable activations yet — we'd like there to be. 🙂

