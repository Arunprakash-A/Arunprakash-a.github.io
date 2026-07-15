---
title: "Can Local LLMs Build Interactive Simulations? An Agentic Comparison"
date: 2026-07-15
tags: education visualization physics math llm agentic-ai
key: "AgenticSims0715"
comment: true
mathjax: false
---

I wanted to know whether a small local LLM, given nothing but a topic name, can autonomously build a working, pedagogically useful browser simulation — no human writing a line of the HTML/JS. So I set up an agentic pipeline and pointed four different open models at the same list of Math, Physics, and Neural Network topics.

👉 **[Open the full gallery](/llm-applets/)** — 88 applets, 8 models, all playable.

<!--more-->

## The pipeline

Each applet is produced by three roles, all played by the same local model:

1. **Planner** — turns a topic ("Pythagorean theorem", "buoyancy", "self-attention") into a short spec: the concept to teach, the interactions a learner should have, the visual layout.
2. **Coder** — writes a single self-contained `applet.html` (Canvas/SVG + vanilla JS, no build step) implementing the spec.
3. **Reflector** — loads the result, tests it, and either approves it or sends it back to the Coder with specific fixes. This loop runs for up to 5 turns before publishing whatever it has.

Averaged across all 88 applets: **33s** planning, **2m 17s** initial coding, **10m 32s** of reflection/revision — **13m 22s** total to go from a topic string to a published, working applet. The full breakdown (and a diagram of the loop) is on the [gallery home page](/llm-applets/).

## The models

| Model | Subjects | Hardware |
|---|---|---|
| gemma4-31b (5 reflection turns) | Math, Physics | A100 40GB |
| ornith-35b | Math, Physics, Neural Networks | A100 40GB |
| gpt-oss-20b | Math, Physics | A100 40GB |
| qwen3.6-35b | Math | L4 |

## Results so far

**gemma4-31b** is the clear overall winner on both Math and Physics — most reliably correct, interactive, and bug-free on the first few reflection turns. **ornith-35b** consistently produces the best-looking applets (🎨 best aesthetics badge on the gallery) even when the underlying logic needs more revision turns to get right. Neural Networks is currently ornith-35b only (11 applets) — the other models haven't been run on this subject yet.

| Subject | Models | Applets |
|---|---|---|
| Math | 4 | 48 |
| Physics | 3 | 29 |
| Neural Networks | 1 | 11 |

## A few favorites

**Math — gemma4-31b, Unit Circle Trigonometry Explorer**

<iframe src="/llm-applets/applets/gemma4-31b-5turns-no-think-g10/" style="width:100%; height:600px; border:1px solid #ddd; border-radius:8px;"></iframe>

**Physics — ornith-35b, Ray Optics: Lenses and Mirrors**

<iframe src="/llm-applets/applets/physics-ornith-35b-no-think-g10/" style="width:100%; height:600px; border:1px solid #ddd; border-radius:8px;"></iframe>

**Neural Networks — ornith-35b, Self-Attention Explorer**

<iframe src="/llm-applets/applets/nn-ornith-35b-no-think-n12/" style="width:100%; height:600px; border:1px solid #ddd; border-radius:8px;"></iframe>

---

Browse everything, including the per-model breakdowns, generation time, and token counts for every single applet, in the **[full gallery](/llm-applets/)**. The static-site generator that builds the gallery from the raw run folders is on [GitHub](https://github.com/Arunprakash-A/Arunprakash-a.github.io/blob/master/tools/build-llm-applets-site.py); the planner/coder/reflector pipeline itself runs against local Ollama models and isn't part of this repo.

This is a living comparison — new applets get added as more models and topics are run, and the numbers above will grow.
