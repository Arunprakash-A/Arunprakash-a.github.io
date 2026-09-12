---
title: "Experiments Attempted But .."
date: 2026-09-12
tags: [Deep-Learning, Research]
key: "EAB260912"
pageview: true
comment: true
mathjax: false
excerpt: "A catalog of 34 experiments from this project's lab notebook — wins, losses, null results, and a few outright breaking points — each with its own result page."
---

> *This blog post is written by Claude as a single page summary of what I have been testing for the past 3 months.*

Not every experiment becomes a paper section or its own post. Most don't. This is the rest of them:
34 studies pulled from this project's running lab notebook, each one a real run (or a small series of
runs) with a real result — kept here because "attempted" is most of what research actually is, and
because a negative or inconclusive result is still information, not a wasted GPU-hour.

Two posts already cover the headline result this catalog sits around —
[thinking beyond localized activations](/2026/07/25/thinking-beyond-localized-activations.html) and
[learnable activations might have a better loss landscape](/2026/08/11/learnable-activations-might-have-better-loss-landscape.html),
with the [transfer follow-up](/2026/08/31/we-can-not-only-learn-but-also-transfer-activations.html) picking
up from there. What follows is everything that happened *around* that arc: the studies that confirmed it
more carefully, the ones that tried to break it, the ones that found a real limit, and the ones that just
didn't pan out.

Every number below is either a verified measurement from this project's own run logs, results files, and
reports, or (for GPU/dataset/model) checked directly against the experiment's own scripts and READMEs this
week. Where a result is partial, stopped early, or a single seed, the page says so.

**Scale, at a glance:** four GPUs did essentially all of this — an A100 (40GB, local), a V100 (32GB), and
two L4s (23GB each) — plus a fifth, an H200, that joined later and now carries most of the heaviest
ImageNet-1K-scale runs.

## The ImageNet-1K core

The result everything else in this catalog orbits: a single learnable activation, shared across the whole network, confirmed at real scale — and the studies that stress-tested exactly how that result holds up.

| Experiment | Objective | GPU | Dataset | Model |
|---|---|---|---|---|
| [The 5-Seed ImageNet-1K Confirmation](/experiments/imagenet1k-seed-study/) | Confirm, with enough seeds to trust a p-value, that a single learnable activation shared across the whole network beats a fixed GELU at ImageNet-1K scale. | H200 | ImageNet-1K | ViT, depth 6 (embed_dim 384) |
| [Does the Fourier-Coefficient Init Even Matter?](/experiments/imagenet1k-learned-coeff-init/) | Start FAct's 5 coefficients from a different initial guess (not the GELU fit) and see whether the network still finds its way to the same place on ImageNet-1K. | H200 | ImageNet-1K | ViT, depth 6 (embed_dim 384) |
| [Freeze the Learned Curve, Train From Scratch Again](/experiments/imagenet1k-learned-activation-fixed/) | Take the K=2 curve FAct converges to on ImageNet-1K, freeze it into a fixed nonlinearity, and retrain a fresh network with no learnable activation at all — where does it land relative to GELU and to the fully trainable version? | H200 | ImageNet-1K | ViT, depth 6 (embed_dim 384) |
| [The Five-Way Fixed-Activation Scorecard](/experiments/imagenet1k-fixed-act-baselines/) | Round out the ImageNet-1K comparison with the fixed activations everyone actually reaches for in practice — ReLU, LeakyReLU, SiLU — under the exact same recipe as the FAct/GELU runs. | H200 | ImageNet-1K | ViT, depth 6 (embed_dim 384) |
| [What Happens When You Let It Memorize 10 Images a Class](/experiments/imagenet1k-overfit10/) | Train FAct on a fixed 10-images-per-class subset of ImageNet-1K for 100 epochs — enough to memorize the training set outright — and watch what the learned activation does as it does so. | H200 | ImageNet-1K (10 images/class subset) | ViT, depth 6 (embed_dim 384) — FAct K=2, global |

## Small models, exact answers

Strip the network down far enough — one linear layer, one online pass, one tabular dataset — and some questions get answers precise enough to trust completely.

| Experiment | Objective | GPU | Dataset | Model |
|---|---|---|---|---|
| [The Simplest Possible Network: One Linear Layer](/experiments/svd-of-mlp/) | Strip the comparison down to the smallest model that can still carry an activation function — a single nn.Linear(784, 10) on MNIST, activation applied straight to the logits — so an SVD and an exact Hessian of the one weight matrix become tractable. | mixed (H200 references in logs; trivial compute — a single 7,850-parameter linear layer) | MNIST | Single nn.Linear(784, 10), no hidden layer |
| [Rank-1 Is a Trap, Not a Wall](/experiments/mnist-mlp-online/) | Train a tiny 784→10→10 MLP online (batch_size=1, one pass) from an all-zero init and see whether the rank-1 symmetry that zero-init locks in can ever be escaped — with or without help. | not recorded (single pass, 784→10→10 online SGD — trivial compute) | MNIST | MLP 784→10→10, zero-initialized, online (batch_size=1) |
| [The Same Online Protocol, Now With a Conv Front End — and a Batch-Size Flip](/experiments/online-cifar10-cnn/) | Extend the MNIST online-learning protocol to CIFAR-10 behind a small conv layer feeding the same 784-wide MLP, and check whether the GELU/FAct story holds as batch size grows off strict one-sample-at-a-time streaming. | not recorded (single pass, ~815K-param CNN+MLP — light compute) | CIFAR-10 | Conv(5×5) → 784→10→10 MLP, online (batch_size ∈ {1, 10, 20}) |
| [Do Nine Harmonics Beat Two, 90 Layers Deep?](/experiments/fact-k9-exp61-repeat/) | Repeat a 90-hidden-layer, width-10, LayerNorm MNIST MLP study (Experiment-61) with K=9 Fourier activations added to its 16-activation zoo, on the same host, same torch build, same MNIST cache — does more harmonic capacity help at extreme depth? | V100 | MNIST | 90-hidden-layer, width-10, LayerNorm residual MLP (19,550 FFN params) |
| [Fifteen Tiny Tabular Datasets, No Overall Winner — Except Two](/experiments/tabmini-lowdata/) | Test GELU vs. FAct on the TabMini/PMLBmini suite of real-world tabular datasets with N≤500 rows, where deep nets are usually a bad idea in the first place, and see if either activation has an edge. | not recorded (tabular MLPs, N≤500 rows — seconds per run) | TabMini / PMLBmini (15 real-world N≤500 tabular datasets) | MLP (width-16 config), logistic-regression baseline included |
| [What If You Just Take the Max of GELU and FAct?](/experiments/gelu-fact-hybrid-max/) | Build a per-neuron max(GELU(x), FAct-K2(x)) hybrid activation and see whether it captures the best of both, on a depth-1 ViT on CIFAR-10. | A100 | CIFAR-10 | ViT, depth 1 |
| [One Hinge, Fit to the Learned Curve](/experiments/relu1-approx-of-fact/) | Fit a single ReLU-shaped hinge ("ReLU-1") to approximate the shape FAct converges to, and see whether that much cheaper, piecewise-linear stand-in captures FAct's advantage. | mixed: A100 / L4 (a host-effect check between them found p=0.66, no detectable difference) | FashionMNIST, CIFAR-10, CIFAR-100 | ViT-100K (part of the 12-activation zoo, Experiment-63) |
| [The Dataset That Breaks Every Activation Equally](/experiments/spiral10-breaking-point/) | Push a 2D toy-pattern study to its limit with a 10-arm spiral wound through two full rotations, specifically looking for the difficulty level where FAct's advantage finally disappears. | not recorded (2D toy dataset, single hidden-layer MLP — trivial compute) | Spiral10 (synthetic, turns=2.0, 10-class) | Single hidden-layer MLP (width 10 or width 2) |

## Does it generalize beyond ViT?

Five architectures, a fair per-activation tuning budget, and one architecture that flips the story.

| Experiment | Objective | GPU | Dataset | Model |
|---|---|---|---|---|
| [Does It Generalize Beyond ViT? Five Architectures, One Answer](/experiments/fact-vs-rest-architecture-sweep/) | Check whether FAct's ImageNet-level edge is a ViT-specific artifact by running the full 11/12-activation zoo across ViT, ConvMLPMixer, ConvNeXt, a LayerNorm-MLP, and ResNet-18. | mixed fleet: H200, V100, L4, A100 (all four hosts used across the sweep) | FashionMNIST, CIFAR-10 (5-seed confirmed arms) | ViT / ConvMLPMixer / ConvNeXt / LayerNorm-MLP / ResNet-18 (~100K-param scale) |
| [Post-Training Quantization Doesn't Care Which Activation You Used](/experiments/fact-vs-rest-quantization-null/) | Check whether INT8/INT4 post-training quantization damages FAct's networks more or less than the other 10 activations in the zoo, across ViT, ConvMLPMixer, and ConvNeXt. | analysis of checkpoints already trained across the project's H200/A100/V100/L4 fleet; the PTQ simulation itself is lightweight | FashionMNIST, CIFAR-10, CIFAR-100, Food-101 | ViT / ConvMLPMixer / ConvNeXt (~100K-param scale), W4A8 and W4A32 simulated quantization |
| [Give Every Activation Its Own Tuned Learning Rate — Does FAct Still Win?](/experiments/vit100k-lr-wd-tuning/) | Re-run the 12-activation ViT-100K zoo with a per-activation learning-rate/weight-decay search (same tuning budget for every activation), instead of one shared setting for all — the obvious objection to the untuned Experiment-63 result. | all 5 hosts in the fleet: H200, A100 (local), V100, and both L4 GPUs, split by dataset | FashionMNIST, CIFAR-10, CIFAR-100, Food-101 | ViT-100K (embed_dim=64, depth=2, heads=4, mlp_ratio=4.0) |
| [The Same Tuning Exercise on ConvMLPMixer — FAct Falls](/experiments/convmlpmixer-lr-wd-tuning/) | Repeat the per-activation LR/WD tuning exercise on ConvMLPMixer instead of ViT, to see if the tuned ranking holds across architectures. | mixed fleet (A100/H200/V100/L4, similar split to the ViT tuning study) | FashionMNIST, CIFAR-10, CIFAR-100, Food-101 | ConvMLPMixer-3M |
| [Ruling Out the Depth/Width Confound](/experiments/convmlpmixer-isotropic-pilot/) | Rebuild ConvMLPMixer's backbone as a ViT-structured, constant-width, depth-3 isotropic network on CIFAR-10 only, to check whether the previous experiment's FAct loss was really about the convolutional mixer architecture, or just a side effect of its different depth/width shape. | V100 (a live shared-memory crash occurred mid-run, fixed by cutting DataLoader workers from 6 to 3) | CIFAR-10 | Isotropic ConvMixer (constant-width, depth=3, ViT-structured) |

## Taking the activation apart

Gate it, split its gradient, target it directly, initialize with it, restrict its FFN's connectivity, generate its weights structurally — six ways of opening the hood.

| Experiment | Objective | GPU | Dataset | Model |
|---|---|---|---|---|
| [Does Multiplying by z Before the Activation Help?](/experiments/fact-z-gated/) | Compare z·φ(z) (a GLU-style gate) against the ordinary φ(z) for FAct K=2 on the ViT-100K/FMNIST setup, to see if a multiplicative gate on top of the learned curve adds anything. | V100 (predominant), some A100/H200 | FashionMNIST | ViT-100K, FAct K=2 (global) |
| [The Network's Two Halves Disagree About the Curve's Shape](/experiments/efact-coeff-gradient-reductions/) | EFAct's 5 Fourier coefficients are shared across every block in the network; test 4 different ways of reducing their per-block gradients (all-sites vs. last-block-only, sum vs. max\|g\|) to see which, if any, changes accuracy. | V100 (predominant), some A100 | FashionMNIST (5 seeds), CIFAR-10 (1 seed) | ViT-100K, EFAct (trainable, 2-block) |
| [What If the Network Has to Emit a Sinusoid, Not a Class Label?](/experiments/structured-target-study/) | Replace the usual classification target with structured regression targets (sinusoid, DFT coefficients, phase) and a CE+DFT mixture loss, to see whether FAct's periodic structure gives it a home-field advantage when the target itself is periodic. | A100 | FashionMNIST | ViT-100K |
| [Initialize the FFN Weights With the Transferred Fourier Curve](/experiments/fourier-init/) | Use the frozen DFT weights that won the NMT transfer study to initialize the ViT-100K FFN's fc1/fc2 layers, to see whether that initialization helps any activation converge faster or further. | mixed: L4, A100, some V100/H200 | FashionMNIST, CIFAR-10, CIFAR-100, Food-101 | ViT-100K, 12-activation zoo, Fourier-derived fc1/fc2 init |
| [What If the FFN Can Only Learn on the Diagonal?](/experiments/ffn-structure-ablation/) | A 4-part series (Experiments 95-98) restricting the ViT-100K FFN's fc1/fc2 weights to a diagonal, a swept diagonal band, a fixed diagonal subset, and IIR-initialized bands — asking how much of the FFN's dense connectivity FAct's advantage actually needs. | not recorded individually (FMNIST, single-seed scale, shared GPU fleet) | FashionMNIST | ViT-100K, FAct K=2 (global) vs. GELU, restricted-connectivity FFN |
| [Weights Generated by a Filter, Not Randomly Sampled](/experiments/iir-generated-weights/) | Replace a layer's randomly-initialized weight rows with rows generated by an IIR filter's impulse response (varying the pole band), to see whether structured, filter-generated weights help or hurt, and whether pairing them with FAct produces any synergy. | local (CUDA_VISIBLE_DEVICES=0, host not separately logged) | FashionMNIST, CIFAR-10 | Small MLP with IIR-generated weight rows (bands: b2, b8, b32, Nyquist) |

## Geometry: dimension, width, depth

Same small 2D patterns, pushed along five different axes — ambient dimension, width, depth, block order, class count — to find where an activation's advantage actually lives.

| Experiment | Objective | GPU | Dataset | Model |
|---|---|---|---|---|
| [Bury a 2D Pattern in 98 Dead Coordinates](/experiments/100d-constant-padding/) | Embed the project's 2D toy patterns into R^100 by padding with a constant, to test whether FAct's edge is really about the 2D geometry or survives being buried in high-dimensional dead weight. | A100 | 2D-Patterns toy suite, padded to R^100 | Small MLP (2D-Patterns-Shape-of-Act series) |
| [A Real 2D Manifold, Properly Embedded This Time](/experiments/lowdim-manifold-highdim/) | Follow up the constant-padding result with a cleaner design: put the same 2D toy patterns on a genuine manifold in R^D via a random orthonormal frame (isometric, general position), then add off-manifold noise, then curvature — controlling for init scale, which the padding study had left confounded with ambient dimension. | not recorded (small MLPs, R^D embeddings up to D=200) | 2D-Patterns toy suite, embedded in R^D via random orthonormal frames | Small MLP, matched-init-scale control arm |
| [Can Width Substitute for Depth?](/experiments/width2-depth1-vit/) | Build a width=2, depth=1 ViT (parallel attention heads summed into a single FFN) and compare it against the standard deeper network, to see whether extra width at minimal depth can match it — and whether FAct's advantage survives the swap. | L4 | FashionMNIST | ViT, width=2/depth=1 (parallel-attention, single FFN) vs. standard depth |
| [Does FFN-First or Attention-First Matter — and For How Long?](/experiments/ffn-attn-block-order/) | Swap the order of the FFN and attention sublayers (FFN-first vs. the standard attention-first) across a d_ff sweep and 3 training-budget phases, on both FashionMNIST and CIFAR-10, to see whether block order is a convergence-speed effect or an accuracy-ceiling effect. | mixed: A100, V100, L4 | FashionMNIST, CIFAR-10 | ViT-100K, FFN-first vs. Attention-first block order |
| [Same 2D Patterns, Different Number of Classes](/experiments/class-count-series/) | Re-run the 2D-patterns width sweep at C=2, 3, and 10 classes, to see whether FAct's edge and its convergence-speed advantage depend on how many classes the toy problem has. | A100 (predominant across this series) | 2D-Patterns toy suite (circles, spirals, pinwheel, etc.), C ∈ {2, 3, 10} | Small MLP, width sweep |

## Theory and engineering

How steep is this curve, exactly — and how cheap can it be made to run.

| Experiment | Objective | GPU | Dataset | Model |
|---|---|---|---|---|
| [How Steep Is This Curve, Exactly?](/experiments/lipschitz-of-activations/) | Work out the Lipschitz constant — analytically where possible — for sixteen standard fixed activations plus FAct and PAU, and measure how FAct's constant actually moves during real ImageNet-1K training. | analysis-only (uses an existing ImageNet-1K FAct checkpoint, itself trained on H200; the Lipschitz computation is CPU-side) | ImageNet-1K (existing FAct K=2 checkpoint, for the measured numbers) | theory + measurement on existing checkpoints (no new training) |
| [Making FAct Cheap Enough to Actually Use](/experiments/fact-cuda-kernel-perf/) | Profile and optimize a custom CUDA kernel for FAct K=2, since the pure-PyTorch implementation is roughly 2x slower and uses substantially more memory than a fixed activation. | L4 (benchmarked); H200 too noisy at these shapes to benchmark reliably | n/a (microbenchmark, not a training run) | cuda_fact_k2 kernel vs. pure-PyTorch FourierActivation |

## Beyond vision: language

Autoregressive language modeling and machine translation, where the vision-side story meets new dynamics.

| Experiment | Objective | GPU | Dataset | Model |
|---|---|---|---|---|
| [Taking FAct Out of Vision and Into Language Modeling](/experiments/nanogpt-fact-vs-gelu/) | Drop the frozen, ImageNet-learned FAct K=2 curve into Karpathy's nanoGPT (autoregressive, decoder-only) trained on OpenWebText, to test whether the convergence-speed edge transfers to a new architecture family and modality. | H200 | OpenWebText | nanoGPT (GPT-2 scale, n_layer=6/n_head=6/n_embd=384 baby-GPT recipe for smoke tests; full OWT config for the live run) |
| [A Real Translation Benchmark, Not a Toy](/experiments/wmt14-fact-vs-paper-baseline/) | Test FAct against GELU on WMT14 English→German with a proper base Transformer (real BPE tokens, the actual "Attention Is All You Need" recipe) — the first FAct-vs-GELU comparison in this project on a benchmark anyone would call a real translation system. | H200 | WMT14 English→German | Base Transformer ("Attention Is All You Need" recipe, Pre-LN, BPE tokens) |
| [Let the Fourier Series Choose Its Own Frequency, Too](/experiments/wmt14-learnable-w/) | Add a learnable fundamental frequency w (started at 0.5, half the standard rate) to FAct's Fourier series on WMT14, on top of the usual learnable amplitude coefficients — testing 1-layer and 6-layer configurations. | A100 and H200 (a ~0.3 BLEU host effect between them swamps the arm effect at this scale) | WMT14 English→German | 1-encoder/1-decoder-layer and 6-layer Transformer, FAct K=2/K=3/K=5 with learnable w |

---

That's 34. Some of these will get their own deeper write-up eventually — most won't, and that's fine.
The point of keeping this list at all is that "attempted but didn't make the paper" is still a real answer
to a real question, and it's usually the answer that took the most GPU-hours to earn.
