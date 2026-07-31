---
title: "Training ImageNet-1K: Standard Activation vs Our Approach"
date: 2026-07-31
tags: Deep-Learning Research
key: "IN1K3107"
pageview: true
comment: true
mathjax: false
---

Toy datasets and small benchmarks are useful for iterating fast, but they
only tell you so much. ImageNet-1K — 1.28M training images across 1,000
classes — is the test that actually matters: it's large enough, and messy
enough, that shortcuts which work at small scale tend to fall apart here.
So that's where this round of testing went.

<!--more-->

## The setup

Two models, identical in every way except the activation function: a
**standard** network using the usual fixed activation (GELU), and a network
using the approach I've been developing, referred to here simply as
**Proposed**. Same architecture, same optimizer, same schedule, same data
pipeline, same 100 training epochs. The only thing that differs between the
two runs is the one component under test.

I'm keeping the "how" out of this post — that write-up is still in
progress. What follows is just the training behavior, plotted plainly.

## Loss

<img align="center" src="/images/Training-ImageNet1K-Standard-vs-Our-Approach/loss_curves.png">

Both models descend along a very similar curve for the first several
epochs, which is reassuring — nothing about the swap destabilizes early
training. Past roughly epoch 15, Proposed pulls slightly ahead and holds
that lead in validation loss for the rest of the run. The training-loss
gap between the two grows a bit more than the validation-loss gap does,
which is worth keeping an eye on but isn't dramatic at this scale.

## Accuracy

<img align="center" src="/images/Training-ImageNet1K-Standard-vs-Our-Approach/training_curves.png">

The accuracy picture tells the more interesting story. Proposed reaches
60% validation accuracy at epoch 48; the standard model doesn't get there
until epoch 61 — roughly a quarter fewer epochs to hit the same milestone.
That lead narrows somewhat by the end of training but never disappears:
final validation accuracy comes in at 65.1% for Proposed versus 64.1% for
the standard model, with Proposed's best epoch (65.4%) also beating the
standard model's best (64.1%, reached only at the very last epoch).

## Reading it honestly

A ~1-point final accuracy gap on ImageNet-1K is a real but modest
difference — not the kind of result that rewrites anything on its own. The
more consistent signal across both plots is the *shape* of the curves early
on: Proposed gets to a given loss or accuracy level sooner, not just a
better level eventually. That's the more useful property, if it holds up,
because faster convergence compounds at scale in a way a small final-metric
edge does not.

The training/validation gap is also slightly wider for Proposed than for
the standard model by the end of 100 epochs — train accuracy pulls further
ahead of validation accuracy for Proposed than it does for the standard
run. Nothing alarming yet, but it's the kind of detail that needs watching
as this moves to longer schedules and larger models rather than being
waved away.

This is one data point in a longer line of experiments, not a finish line.
The mechanism behind "Proposed" gets its own write-up once it's ready to
land in one piece — for now, this is just what the numbers on ImageNet-1K
say.
