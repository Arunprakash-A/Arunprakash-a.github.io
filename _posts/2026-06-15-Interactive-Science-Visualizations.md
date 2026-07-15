---
title: "Building Interactive Simulations for My Daughter"
date: 2026-06-15
tags: education visualization physics ml
key: "SciViz0615"
comment: true
mathjax: false
---

My 6-year-old daughter asked me about the phases of the moon. I tried explaining it using pen and paper, hand-waving in the air — she got a bit of it. Like every kid, she watches space cartoons and videos on YouTube. Suddenly I thought of building an interactive simulation like in PhET. I searched PhET, and I didn't find any app for explaining moon phases. Then I turned to Claude. As usual, it built beautiful applets with a few rounds of feedback. Just imagine the impact this can have on the education sector. Here are some of the applets.

👉 **[Open Science Explorer](/apps/)** — the full hub with all four apps.

---

## 🌙 Moon Phases Explorer

Visualizes the Moon's real orbital mechanics in 3D — elliptical orbit, Kepler's second law (faster at perigee, slower at apogee), and the 5.1° orbital inclination. Drag to rotate the view, watch the phase diagram update live, and click Earth to look up at the sky from the surface.

**[Launch →](/apps/moon-phases/)**

---

## 🌿 Photosynthesis

An animated look at how plants convert sunlight, CO₂, and water into glucose and oxygen. Watch photons travel from the Sun to chloroplasts, water rise through the stem, and oxygen escape upward — all in a continuous particle simulation with the full chemical equation at the bottom.

**[Launch →](/apps/photosynthesis/)**

---

## 🏛️ Galileo's Tower — Free Fall

Drop a pebble, rubber ball, and leaf simultaneously from a 55 m tower — with air on one side and vacuum on the other. The results table fills in as each object lands. In vacuum, all three hit at the exact same time (Galileo's discovery). In air, the leaf takes over 20 seconds longer while drifting several metres sideways.

**[Launch →](/apps/free-fall/)**

---

## 📉 Gradient Descent Explorer

Step through gradient descent one iteration at a time on five different loss surfaces:

| Surface | What it teaches |
|---|---|
| Simple Bowl | Basic convergence, effect of learning rate |
| Narrow Valley | Oscillation when curvature is uneven |
| Banana Valley (Rosenbrock) | Why curved valleys are hard for optimizers |
| Double Well | Local minima — starting point determines the outcome |
| Saddle Point | Zero gradient that is not a minimum |

The red arrow shows the gradient ∇L (steepest ascent), the teal arrow shows the step −η∇L (where the optimizer actually moves). Click anywhere on the map to plant a new starting point and watch the path change. A live loss-vs-iteration curve appears in the corner.

**[Launch →](/apps/gradient-descent/)**

---

All apps run entirely in the browser (HTML + Canvas + Three.js). Source is on [GitHub](https://github.com/Arunprakash-A/Arunprakash-a.github.io/tree/master/apps).
