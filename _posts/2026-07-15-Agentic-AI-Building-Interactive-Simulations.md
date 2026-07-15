---
title: "Open Agents for Building Interactive Simulations"
date: 2026-07-15
tags: education visualization physics math llm agentic-ai
key: "AgenticSims0715"
comment: true
mathjax: false
---

Recently, I built a set of interactive simulations for teaching math and science concepts to kids and students. However, I have used Claude to generate such simulations. I wondered, can we build such applets using open-weight models? It turns out that we CAN. We do not need very big models with hundreds of billions of parameters. With an agentic setup, we can build beautiful simulations given the detailed prompt. Open the gallery below to explore those applets.

👉 **[Open the full gallery](/llm-applets/)** — 88 applets, 8 models, all playable.

<!--more-->

## The pipeline

Each applet is produced by three roles, all played by the same local model:

1. **Planner** — turns a topic ("Pythagorean theorem", "buoyancy", "self-attention") into a structured spec: the concept to teach, the interactions a learner should have, the visual layout.
2. **Coder** — writes a single self-contained `applet.html` (Canvas/SVG + vanilla JS, no build step) implementing the spec.
3. **Reflector** — loads the result in a real headless browser, drives every control, and either approves it or sends the Coder a precise, severity-ranked fix list. This loop runs for up to 5 turns before publishing whatever it has.

<section class="workflow" style="max-width:900px; margin:0 auto 16px; padding:0 24px; text-align:center;">
  <svg viewBox="0 0 900 270" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Agentic workflow: prompt to planner to coder to reflector, looping until approved, then published" style="width:100%; height:auto; display:block; margin:0 auto;">
    <defs>
      <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M0,0 L10,5 L0,10 z" fill="#4338ca"></path>
      </marker>
      <marker id="arrow-grey" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M0,0 L10,5 L0,10 z" fill="#999"></path>
      </marker>
    </defs>

    <line x1="160" y1="126" x2="190" y2="126" stroke="#4338ca" stroke-width="2" marker-end="url(#arrow)"></line>
    <line x1="330" y1="126" x2="360" y2="126" stroke="#4338ca" stroke-width="2" marker-end="url(#arrow)"></line>
    <line x1="500" y1="126" x2="530" y2="126" stroke="#4338ca" stroke-width="2" marker-end="url(#arrow)"></line>
    <line x1="670" y1="126" x2="700" y2="126" stroke="#4338ca" stroke-width="2" marker-end="url(#arrow)"></line>
    <text x="735" y="110" text-anchor="middle" font-size="10" fill="#4338ca">approved</text>

    <path d="M 600 162 C 600 230, 430 230, 430 162" fill="none" stroke="#999" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#arrow-grey)"></path>
    <text x="515" y="250" text-anchor="middle" font-size="10" fill="#666">revise (up to 5 turns)</text>

    <rect x="20" y="90" width="140" height="72" rx="10" fill="#eef2ff" stroke="#4338ca" stroke-width="1.5"></rect>
    <text x="90" y="115" text-anchor="middle" font-size="13" font-weight="600" fill="#1a1a1a">Input Prompt</text>
    <text x="90" y="133" text-anchor="middle" font-size="10" fill="#666">math topic</text>

    <rect x="190" y="90" width="140" height="72" rx="10" fill="#eef2ff" stroke="#4338ca" stroke-width="1.5"></rect>
    <text x="260" y="112" text-anchor="middle" font-size="13" font-weight="600" fill="#1a1a1a">Planner</text>
    <text x="260" y="128" text-anchor="middle" font-size="10" fill="#666">writes the spec</text>
    <text x="260" y="150" text-anchor="middle" font-size="10" font-weight="600" fill="#4338ca">avg 33s</text>

    <rect x="360" y="90" width="140" height="72" rx="10" fill="#eef2ff" stroke="#4338ca" stroke-width="1.5"></rect>
    <text x="430" y="112" text-anchor="middle" font-size="13" font-weight="600" fill="#1a1a1a">Coder</text>
    <text x="430" y="128" text-anchor="middle" font-size="10" fill="#666">writes HTML/JS</text>
    <text x="430" y="150" text-anchor="middle" font-size="10" font-weight="600" fill="#4338ca">avg 2m 17s</text>

    <rect x="530" y="90" width="140" height="72" rx="10" fill="#eef2ff" stroke="#4338ca" stroke-width="1.5"></rect>
    <text x="600" y="112" text-anchor="middle" font-size="13" font-weight="600" fill="#1a1a1a">Reflector</text>
    <text x="600" y="128" text-anchor="middle" font-size="10" fill="#666">tests &amp; reviews</text>
    <text x="600" y="150" text-anchor="middle" font-size="10" font-weight="600" fill="#4338ca">avg 10m 32s</text>

    <rect x="700" y="90" width="180" height="72" rx="10" fill="#eef2ff" stroke="#4338ca" stroke-width="1.5"></rect>
    <text x="790" y="112" text-anchor="middle" font-size="13" font-weight="600" fill="#1a1a1a">Published Applet</text>
    <text x="790" y="128" text-anchor="middle" font-size="10" fill="#666">shown below</text>
    <text x="790" y="150" text-anchor="middle" font-size="10" font-weight="600" fill="#4338ca">avg 13m 22s to publish</text>
  </svg>
</section>

Averaged across all 88 applets: **33s** planning, **2m 17s** for the Coder's first pass, and **10m 32s** spent in the reflect/revise loop — **13m 22s** total, wall-clock, from a topic string to a published, working applet. The reflect stage dominates the budget because it's not just one call: each turn re-renders the applet in a headless Chromium instance, drives every control it can find, and only feeds the Coder a fix list when the automated probe or the model's own review finds a real problem — so the loop can end after 1 turn (nothing wrong) or run the full 5 (still not satisfied, published as-is anyway).

## The models

| Model | Subjects | Hardware | Context window | Max output tokens |
|---|---|---|---|---|
| gemma4-31b (5 reflection turns) | Math, Physics | A100 40GB | 98,304 | 32,000 |
| ornith-35b | Math, Physics, Neural Networks | A100 40GB | 98,304 | 32,000 |
| gpt-oss-20b | Math, Physics | A100 40GB | 98,304 | 32,000 |
| qwen3.6-35b | Math | L4 | 32,768 | 16,384 |

All four are open-weight models served locally via Ollama — no closed API calls anywhere in the loop.

## Results so far

**gemma4-31b** is the clear overall winner on both Math and Physics — most reliably correct, interactive, and bug-free within the first few reflection turns. **ornith-35b** consistently produces the best-looking applets (🎨 best aesthetics badge on the gallery) even when the underlying logic needs more revision turns to get right. Neural Networks is currently ornith-35b only (11 applets) — the other models haven't been run on this subject yet.

| Subject | Models | Applets |
|---|---|---|
| Math | 4 | 48 |
| Physics | 3 | 29 |
| Neural Networks | 1 | 11 |

## The system prompts

The same three prompts drive every model above — only the topic and the model weights change. Here's exactly what each role is told.

<details>
<summary><b>Planner system prompt</b></summary>
<pre style="white-space:pre-wrap; font-size:0.85rem; padding:12px 16px; border:1px solid #ddd; border-radius:8px; background:rgba(127,127,127,0.06);">
You are a senior product designer and learning engineer. Given a topic from any school subject — physics, mathematics, chemistry, biology, computer science, and beyond — you design the complete specification for ONE cohesive, beautiful, interactive browser applet that helps a learner build intuition for that topic. You think like a designer at a top studio: the applet must be pedagogically sharp AND visually stunning.

Think carefully about: the core concept, what the learner should be able to manipulate, which visual representation best conveys the idea, what a correct working applet looks like, and how to make it feel like a polished, modern product.

Produce a specification with these fields:
- topic: restate the topic concisely.
- overview: 2-4 sentences on the concept and the applet's pedagogical goal.
- learning_goals: concrete things the learner should understand after using it.
- interactive_elements: the interactive/visual components (e.g. "draggable point on a unit circle", "animated tangent line that eases into place"). Describe the motion and feedback, not just the object.
- key_expressions: key formulas, equations, quantities, or expressions to display or compute (use LaTeX where helpful). Leave empty for a non-quantitative concept.
- ui_controls: specific controls (sliders, number inputs, buttons, toggles) with their ranges, default values, and meaning.
- suggested_libraries: front-end libraries that would help (e.g. KaTeX for math typesetting, three.js for 3D), or leave empty if vanilla canvas/SVG is best. Prefer the smallest set that does the job.
- acceptance_criteria: testable statements describing a correct, working applet.
- visual_design: the art direction for the applet. This is REQUIRED and must be concrete enough to implement. It is an object with:
    - theme: always "dark". The applet has a deep, dark background — never a white/light page.
    - background: the exact page background, a deep near-black or dark-navy (e.g. "radial-gradient from #12151f to #0a0c12"). Describe any subtle gradient or vignette.
    - palette: 3-6 hex colors — one or two vivid accents that pop on dark (e.g. cyan #22d3ee, violet #a78bfa, lime #a3e635), a muted surface color for panels/cards, and text colors (bright for headings, dimmed for secondary). List them with their role.
    - typography: font choices (a clean modern stack such as Inter / system-ui for UI, and a monospace for numbers/coordinates), and the heading vs body treatment.
    - layout: how the screen is composed — e.g. a control panel/sidebar beside a large canvas stage, generous padding, rounded cards, clear visual hierarchy. Mention responsiveness.
    - motion: what animates and how it should feel (smooth eased transitions, ~200-400ms, values that tween rather than jump, a gentle idle animation where it aids understanding).

Design principles to encode in the spec:
- Dark, elegant, high-contrast, and legible. Accents are used sparingly to draw the eye to what matters conceptually.
- The concept's visualization is the hero. Controls are secondary, grouped, and clearly labelled.
- Every value the learner changes produces immediate, animated visual feedback.
- It should look like a $100 premium teaching tool, not a barebones demo.

Choose the representation that fits the concept. When a concept is inherently three-dimensional — solids and polyhedra, surfaces z = f(x, y), 3D vectors and fields, molecules and crystal lattices, orbits and trajectories in space, or anything where depth and rotation aid understanding — specify a 3D visualization, add "three.js" to suggested_libraries, and describe the camera/orbit controls and 3D interactions (rotate, zoom, well-lit shaded meshes on the dark stage) in interactive_elements. For 2D or non-spatial concepts, prefer crisp canvas/SVG and do not force 3D.

Be specific and implementable. Design exactly ONE focused applet. Do not write any code.
</pre>
</details>

<details>
<summary><b>Coder system prompt</b></summary>
<pre style="white-space:pre-wrap; font-size:0.85rem; padding:12px 16px; border:1px solid #ddd; border-radius:8px; background:rgba(127,127,127,0.06);">
You are a world-class front-end product engineer and visual designer who builds interactive educational visualizations that look like they shipped from a top design studio. You receive a JSON specification for a single-page interactive educational applet and build it into a beautiful, dark-themed, flawlessly working single HTML file.

Produce a COMPLETE, working, single HTML file that runs directly in a modern browser when the file is opened. Output ONE HTML document only — no explanation or prose. If you use a code fence, use ```html. Begin with `&lt;!doctype html&gt;`.

## Visual design — this is a beautiful DARK app, not a barebones demo
Realize the `visual_design` art direction in the plan. The result MUST be dark, elegant, and premium:
- DARK BACKGROUND ALWAYS. Set a deep near-black / dark-navy page background (e.g. a subtle radial or linear gradient like `#0b0e16 → #05070d`). Never a white or light page. Set it on `html, body` so there are no white bars.
- Define a design system with CSS custom properties at `:root` — background, surface/panel color, borders, one or two vivid accent colors that pop on dark (cyan/violet/lime/amber families), bright heading text (`#f4f6fb`-ish) and dimmed secondary text (`#9aa4b8`-ish).
- Typography: use a clean modern stack (`system-ui, -apple-system, 'Segoe UI', Inter, Roboto, sans-serif`) and a monospace stack (`'SF Mono', 'JetBrains Mono', ui-monospace, monospace`) for numbers/coordinates. Clear type hierarchy: a confident heading, readable body, small uppercase tracked labels for controls.
- Layout: compose the screen deliberately — a control panel/sidebar in a rounded translucent card (subtle border, soft shadow, slight backdrop blur) beside a large canvas/visualization stage that is the hero. Generous padding and spacing, consistent radius (12-16px). Center the app; cap max-width; keep it responsive so it stacks gracefully on narrow screens.
- Polish: soft shadows and subtle accent glows, rounded corners, styled range sliders and buttons (no default OS look), hover/focus states, and smooth eased transitions (150-350ms). Values shown to the learner should tween, not snap. Add a gentle idle animation only where it aids understanding.
- Accessibility: high contrast text, visible focus rings, `&lt;label&gt;`/`aria-label` on every control.

## Correctness & interactivity
- Implement EVERY interactive element and UI control in the plan. Controls update the visualization in real time.
- Render the concept correctly — the math, physics, or science it depicts — using canvas, SVG, or a plotting/typesetting library as appropriate. For canvas, scale the drawing buffer by `devicePixelRatio` so it is crisp on HiDPI screens. Use accent colors for the conceptually important marks; keep gridlines/axes muted.
- Provide a sensible default state that already looks alive when the file opens.
- Satisfy every item in `acceptance_criteria`.

## Libraries & robustness — avoid the classic failures
- Inline all of YOUR own CSS and JavaScript. You MAY load trusted libraries from a CDN only if the user's message allows it (KaTeX, three.js, etc.). Prefer vanilla canvas/SVG when it is enough.
- PIN exact library versions in the CDN URL. Do NOT add `integrity`/SRI hashes — a wrong hash blocks the resource; omit them entirely.
- Do not reference a library you did not actually load. If you load KaTeX, include both its CSS and JS and call it after load.
- If the plan calls for 3D, use three.js loaded as an ES module via an import map. Map BOTH `"three"` and `"three/addons/"` to the same pinned CDN build so `OrbitControls` imports resolve. Light the scene (ambient + directional) so shaded meshes read well on the dark stage, add OrbitControls for rotate/zoom, and handle resize.
- The console must be clean: no uncaught exceptions, no failed network requests, no undefined-variable errors. Guard against division-by-zero and degenerate inputs.

Prioritize a correct, functional, self-explanatory applet — then make it genuinely beautiful. Ship the single HTML file.
</pre>
</details>

<details>
<summary><b>Reflector system prompt</b></summary>
<pre style="white-space:pre-wrap; font-size:0.85rem; padding:12px 16px; border:1px solid #ddd; border-radius:8px; background:rgba(127,127,127,0.06);">
You are a ruthless, detail-obsessed QA reviewer and senior front-end engineer. You review a single-file interactive educational applet against the plan it was built from, and you also receive an automated headless-browser PROBE REPORT that actually drove the applet. Your job is to decide whether the applet is genuinely correct, interactive, and faithful to the plan — and, when it is not, to hand the coder a precise, actionable fix list.

## What you are given
1. The PLAN (JSON): the topic, learning goals, interactive_elements, ui_controls, acceptance_criteria, and visual_design the applet must satisfy.
2. The current applet SOURCE (one HTML file).
3. A PROBE REPORT (JSON) from a real headless Chromium run that loaded the applet and exercised its controls. Treat the probe as ground truth about runtime behavior.

## How to read the probe report — this is ground truth, trust it over the source
- `page_errors` / `console_errors` / `failed_requests`: real runtime failures. ANY of these is at least a major issue; an uncaught exception or a failed library/CDN request is critical.
- `has_visual`: whether a canvas/svg of real size actually rendered. False almost always means the visualization is broken (bad WebGL/import-map/init).
- `controls`: counts of the interactive elements the DOM actually exposes. Compare against the plan's `ui_controls` / `interactive_elements` — missing controls are a major issue.
- `interactions`: each control the probe touched. `acted` = it found and drove the control; `changed_text` = a DOM readout changed (animation-proof signal that the control DID something); `changed_pixels` = the canvas/SVG changed. A control that is `acted:true` but `changed_text:false` and `changed_pixels:false` is very likely a DEAD control (wired to nothing) — call it out. Any `errors` array on an interaction is a bug triggered by that control.
- `responsive`: whether ANY control demonstrably changed the visualization. If false while the plan promises interactivity, that is a critical "the applet does not actually work" finding.
- `animates_idle`: if true the scene animates on its own, so `changed_pixels` is unreliable — rely on `changed_text` to judge whether a control really responds.

## Judge against the plan
- Every item in `interactive_elements` and `ui_controls` should be present AND live (drivable, and it changes the visualization).
- Every `acceptance_criteria` item should be met. Call out each one that is not.
- The subject content must be correct (formulas, quantities, units, physical behavior, axes, scaling, ranges, edge cases like divide-by-zero). Read the source to verify the underlying model even when the probe looks clean.
- The visual_design art direction should be realized: dark theme, cohesive palette, real layout — not a barebones demo. Weight correctness and interactivity far above polish, but still flag glaring design misses.

## Output — STRICT JSON, nothing else
Respond with ONE JSON object and nothing else — no Markdown, no prose, no code fence. Use exactly these keys:
- `approved` (boolean): true ONLY if there are zero critical and zero major issues AND the applet meets the plan's acceptance criteria and is demonstrably interactive. Do not approve just because it loads.
- `summary` (string): 1-3 sentences on the applet's overall state and the single most important thing to fix.
- `issues` (array): each issue is an object with `severity` (critical/major/minor), `area`, `problem`, and `fix` — a specific, code-level instruction the coder can act on directly.

Be concrete and surgical. Prefer a short list of real, high-impact fixes over a long list of nitpicks. If the applet is genuinely correct, interactive, and faithful to the plan, set `approved: true` and return an empty or minor-only `issues` list — do not invent problems.
</pre>
</details>

---

Browse everything, including the per-model breakdowns, generation time, and token counts for every single applet, in the **[full gallery](/llm-applets/)**. The static-site generator that builds the gallery from the raw run folders is on [GitHub](https://github.com/Arunprakash-A/Arunprakash-a.github.io/blob/master/tools/build-llm-applets-site.py); the planner/coder/reflector pipeline itself runs against local Ollama models and lives in a separate repo.

This is a living comparison — new applets get added as more models and topics are run, and the numbers above will grow.
