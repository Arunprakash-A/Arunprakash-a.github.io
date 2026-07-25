---
title: "Thinking beyond localized activations"
date: 2026-07-25
tags: Deep-Learning Research
key: "TBLA2507"
pageview: true
comment: true
mathjax: false
---

Every network you've trained almost certainly leans on the same handful of
activation functions — ReLU, GELU, SiLU, tanh. They differ in shape, but they
share one quiet assumption: the nonlinearity itself is *fixed*. You pick one
function, wide enough to cover the whole range of inputs a neuron will ever
see, bolt it on after every layer, and let gradient descent do the rest with
the weights around it. The function itself never adapts.

<!--more-->

I've been running a long series of experiments that pokes at that assumption
directly: what if, instead of every layer reaching for its own fixed
function, the *entire network* shared one single nonlinearity — and that
nonlinearity's own shape were learned, right alongside the weights? Early
results say there's real substance here. But the road to that result has not
been a straight line, and that's most of what makes it worth writing about
before the destination is ready to publish.

I'm not naming the mechanism yet. What follows is just the evidence — the
promising part and the strange part both.

## The promising part

Swap a standard network's fixed activation for a single shared, adaptive one
and train both on the same toy classification problems, same architecture,
same optimizer. On the training data itself, the new approach matches or
beats the standard network every time — often driving the training loss
essentially to zero where the standard network levels off well above it.

## The strange part

Then you look at what each model predicts *away* from the training points —
and the two stop looking like variations on the same idea.

<img align="center" src="/images/Thinking-Beyond-Localized-Activations/fragmentation.png">

The standard network's boundary does what you'd hope: a single, smooth
dividing line that extrapolates sensibly into empty space. The new approach
fits the same points just as well, sometimes better — but tears the rest of
the plane into scattered, disconnected islands of high confidence, in places
with no training data anywhere nearby. It's a strange, unforced kind of
overfitting: not to noise in the labels, but to something structural in how
the new activation behaves once it's asked to generalize.

That's the honest state of this thread right now — a real capability with a
real, not-yet-fully-tamed side effect. Chasing down *why* it happens, and
which fixes actually address the cause rather than papering over the
symptom, has been most of the last few weeks of work.

## A genuine surprise, once the side effect is reined in

Not every result from taming that side effect was a wash. At a much smaller
network — just 2 units per hidden layer, a fraction of the usual size — one
tuned version of the new approach didn't just match the standard network. It
beat it outright, on a dataset the standard network visibly struggled to
separate at that size:

<img align="center" src="/images/Thinking-Beyond-Localized-Activations/narrow_width_win.png">

The standard network, squeezed down to two units per layer, can't quite
carve out the enclosed shape this problem needs and settles for a much
noisier boundary. The new approach, at the exact same size, gets it clean —
with the side effect from the previous section brought under control at the
same time. This is the first clear case in this line of work where the new
approach isn't just "as good, differently" — it's better, in a size regime
where the standard function structurally runs out of room.

## What actually changed

Here's the shape of the swap, without the mechanism behind it:

<img align="center" src="/images/Thinking-Beyond-Localized-Activations/network_config.png">

A standard network gives every hidden unit its own copy of one fixed
function. This configuration gives the *entire network* one function
instead — and lets that one function's shape be learned. It's a genuinely
different place to put a network's flexibility, and both of the results
above — the promising fit and the strange fragmentation — trace back to that
one change.

I'm keeping the "how" out of this post on purpose. There's a proper write-up
in progress, and it deserves to land in one piece, side effect and fix
included, rather than leaking out sideways. But there's enough here already
to say plainly that fixed, wide-range activation functions are leaving
something on the table — and that whatever replaces them won't be simple to
get right.

Extensive experimentation is underway. Some surprising results are being
cooked.
