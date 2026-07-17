---
title: "More Is Different"
date: 2026-07-17
tags: Deep-Learning AI Physics
key: "MID1707"
comment: true
---

When we scale a neural network to billions of parameters, new capabilities emerge. But we still lack a complete explanation of why certain capabilities emerge or how they arise. Well, this is not unique to neural networks!

I recently came across a beautiful essay, *"More Is Different,"* by Philip W. Anderson. Anderson argued that as systems become larger and more complex, new principles emerge. The fundamental laws remain valid, but they are often insufficient to explain behaviour at higher levels of organisation.

<figure class="essay-figure">
<svg viewBox="0 0 720 200" xmlns="http://www.w3.org/2000/svg">
  <style>
    .n  { fill: var(--ink); }
    .ns { fill: var(--ink-soft); }
    .ln { stroke: var(--rule); stroke-width: 1.5; fill: none; }
    .ar { stroke: var(--ink-faint); stroke-width: 1.6; fill: none; }
    .ac { fill: var(--accent); }
    .lbl{ fill: var(--ink-faint); font-family: Inter, -apple-system, sans-serif; font-size: 12px; text-anchor: middle; }
  </style>
  <defs>
    <marker id="mid-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" class="ar" style="fill: var(--ink-faint); stroke: none;"/>
    </marker>
  </defs>

  <!-- a single unit -->
  <circle cx="70" cy="115" r="9" class="n"/>
  <text x="70" y="150" class="lbl">a single unit</text>

  <line x1="95" y1="115" x2="185" y2="115" class="ar" marker-end="url(#mid-arrow)"/>

  <!-- a small circuit -->
  <g>
    <line x1="280" y1="88"  x2="303" y2="103" class="ln"/>
    <line x1="303" y1="103" x2="294" y2="131" class="ln"/>
    <line x1="294" y1="131" x2="266" y2="131" class="ln"/>
    <line x1="266" y1="131" x2="257" y2="103" class="ln"/>
    <line x1="257" y1="103" x2="280" y2="88"  class="ln"/>
    <line x1="280" y1="88"  x2="294" y2="131" class="ln"/>
    <line x1="303" y1="103" x2="266" y2="131" class="ln"/>
    <circle cx="280" cy="88"  r="6" class="ns"/>
    <circle cx="303" cy="103" r="6" class="ns"/>
    <circle cx="294" cy="131" r="6" class="ns"/>
    <circle cx="266" cy="131" r="6" class="ns"/>
    <circle cx="257" cy="103" r="6" class="ns"/>
  </g>
  <text x="280" y="150" class="lbl">a small circuit</text>

  <line x1="318" y1="115" x2="503" y2="115" class="ar" marker-end="url(#mid-arrow)"/>

  <!-- billions, connected -->
  <g>
    <line x1="602" y1="115" x2="594" y2="140" class="ln"/>
    <line x1="594" y1="140" x2="573" y2="155" class="ln"/>
    <line x1="573" y1="155" x2="547" y2="155" class="ln"/>
    <line x1="547" y1="155" x2="526" y2="140" class="ln"/>
    <line x1="526" y1="140" x2="518" y2="115" class="ln"/>
    <line x1="518" y1="115" x2="526" y2="90"  class="ln"/>
    <line x1="526" y1="90"  x2="547" y2="75"  class="ln"/>
    <line x1="547" y1="75"  x2="573" y2="75"  class="ln"/>
    <line x1="573" y1="75"  x2="594" y2="90"  class="ln"/>
    <line x1="594" y1="90"  x2="602" y2="115" class="ln"/>
    <line x1="560" y1="115" x2="602" y2="115" class="ln"/>
    <line x1="560" y1="115" x2="573" y2="155" class="ln"/>
    <line x1="560" y1="115" x2="526" y2="140" class="ln"/>
    <line x1="560" y1="115" x2="526" y2="90"  class="ln"/>
    <line x1="560" y1="115" x2="573" y2="75"  class="ln"/>
    <circle cx="602" cy="115" r="4.5" class="ns"/>
    <circle cx="594" cy="140" r="4.5" class="ns"/>
    <circle cx="573" cy="155" r="4.5" class="ns"/>
    <circle cx="547" cy="155" r="4.5" class="ns"/>
    <circle cx="526" cy="140" r="4.5" class="ns"/>
    <circle cx="518" cy="115" r="4.5" class="ns"/>
    <circle cx="526" cy="90"  r="4.5" class="ns"/>
    <circle cx="547" cy="75"  r="4.5" class="ns"/>
    <circle cx="573" cy="75"  r="4.5" class="ns"/>
    <circle cx="594" cy="90"  r="4.5" class="ns"/>
    <circle cx="560" cy="115" r="4.5" class="n"/>
    <circle cx="548" cy="125" r="3.5" class="ns"/>
    <circle cx="572" cy="105" r="3.5" class="ns"/>
  </g>
  <text x="612" y="66" class="ac" style="font-size:20px;">&#10022;</text>
  <text x="560" y="180" class="lbl">billions, connected</text>
</svg>
<figcaption>Figure 1 — simple units, combined at scale, start doing things none of them do alone.</figcaption>
</figure>

For example,

- We can often explain the behaviour of an individual, but understanding families, societies, nations, and humanity requires new concepts and models.
- We understand the laws governing individual atoms, yet explaining molecules, cells, living organisms, and even the universe requires additional levels of description.
- We understand how individual neurons function. However, when billions of artificial neurons are connected into a large neural network, new capabilities emerge. These capabilities are difficult to predict from the behaviour of a single neuron or a much smaller network.

We often use reductionism (breaking systems down into their smallest components). It has transformed physics, chemistry, biology,... but constructionism asks a different question. How do simple components, when combined, give rise to entirely new behaviour?

<figure class="essay-figure">
<svg viewBox="0 0 640 210" xmlns="http://www.w3.org/2000/svg">
  <style>
    .n  { fill: var(--ink); }
    .ns { fill: var(--ink-soft); }
    .ar { stroke: var(--ink-faint); stroke-width: 1.6; fill: none; }
    .rl { stroke: var(--rule); stroke-width: 1.5; stroke-dasharray: 4 4; }
    .ac { fill: var(--accent); }
    .lbl{ fill: var(--ink-faint); font-family: Inter, -apple-system, sans-serif; font-size: 13px; text-anchor: middle; }
  </style>
  <defs>
    <marker id="rc-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" style="fill: var(--ink-faint); stroke: none;"/>
    </marker>
  </defs>

  <!-- reductionism: whole -> parts -->
  <rect x="40" y="28" width="90" height="46" rx="14" class="n"/>
  <line x1="150" y1="51" x2="235" y2="51" class="ar" marker-end="url(#rc-arrow)"/>
  <circle cx="270" cy="35" r="7" class="ns"/>
  <circle cx="300" cy="58" r="7" class="ns"/>
  <circle cx="332" cy="38" r="7" class="ns"/>
  <circle cx="357" cy="60" r="7" class="ns"/>
  <text x="320" y="98" class="lbl">Reductionism — break the whole into its parts</text>

  <line x1="20" y1="108" x2="620" y2="108" class="rl"/>

  <!-- constructionism: parts -> whole (+ surprise) -->
  <circle cx="55"  cy="140" r="7" class="ns"/>
  <circle cx="85"  cy="160" r="7" class="ns"/>
  <circle cx="117" cy="142" r="7" class="ns"/>
  <circle cx="142" cy="162" r="7" class="ns"/>
  <line x1="170" y1="150" x2="255" y2="150" class="ar" marker-end="url(#rc-arrow)"/>
  <rect x="290" y="125" width="112" height="50" rx="16" class="n"/>
  <text x="388" y="122" class="ac" style="font-size:20px;">&#10022;</text>
  <text x="320" y="200" class="lbl">Constructionism — parts combine, but the whole surprises us</text>
</svg>
<figcaption>Figure 2 — the same parts, assembled, can behave in ways the parts never hinted at.</figcaption>
</figure>

That question remains open across many disciplines, from physics and biology to neuroscience and artificial intelligence. Perhaps AI is reminding us of a lesson nature has been teaching all along.

---

*P. W. Anderson, "More Is Different," Science, Vol. 177, No. 4047 (1972), pp. 393–396.*
