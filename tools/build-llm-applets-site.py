#!/usr/bin/env python3
"""Builds a simple static gallery site: the landing page has one card per
subject (Math, Physics); clicking a subject shows a grid of playcards for
its models; clicking a model shows a grid of playcards for its applets;
clicking an applet opens it.

Each model's directory contains run folders (one per applet):
  <dir>/<timestamp>__<model>__<model>__<label>/
    applet.html, plan.json, meta.json, reflection.json

meta.json["topic"] is the input prompt given to the planner. plan.json["topic"]
is the short title the planner picked, plan.json["overview"] the description.
Total generation time (shown on each card) sums the initial planner + coder
wall-clock time plus every reflect-loop turn's reflector + coder wall-clock
time in reflection.json, so it reflects all turns, not just the first pass.

To add a model, add an entry to the relevant subject's model list in SUBJECTS
below, pointing at such a directory. To add a subject, add an entry to
SUBJECTS with an empty "models" list until its first model is ready.
"""
import html
import json
import os
import shutil
import subprocess
from pathlib import Path

SITE_ROOT = Path(os.environ.get("SITE_ROOT", "/var/www/math-applets"))
SITE_URL = os.environ.get("SITE_URL", "http://164.52.200.195")
# Prefix applied to every root-absolute link, e.g. "/llm-applets" when this
# site is embedded under a subpath of another domain instead of served at "/".
BASE_PATH = os.environ.get("SITE_BASE_PATH", "").rstrip("/")

MATH_MODELS = [
    {
        "name": "gemma4-31b (5 turns)",
        "slug": "gemma4-31b-5turns-no-think",
        "dir": Path("/root/math-applets-gemma4-31b-5turns-no-think"),
        "gpu": "A100 40GB",
        "winner": True,
    },
    {
        "name": "ornith-35b",
        "slug": "ornith-35b-no-think",
        "dir": Path("/root/math-applets-ornith-35b-no-think"),
        "gpu": "A100 40GB",
        "aesthetic": True,
    },
    {
        "name": "gpt-oss-20b",
        "slug": "gpt-oss-20b-no-think",
        "dir": Path("/root/math-applets-gpt-oss-20b-no-think"),
        "gpu": "A100 40GB",
    },
    {
        "name": "qwen3.6-35b",
        "slug": "qwen3-6-35b-no-think",
        "dir": Path("/root/math-applets-qwen3.6-35b-no-think"),
        "gpu": "L4",
    },
]

PHYSICS_MODELS = [
    {
        "name": "gemma4-31b (5 turns)",
        "slug": "physics-gemma4-31b-5turns-no-think",
        "dir": Path("/root/physics-applets-gemma4-31b-5turns-no-think"),
        "gpu": "A100 40GB",
        "winner": True,
    },
    {
        "name": "gpt-oss-20b",
        "slug": "physics-gpt-oss-20b-no-think",
        "dir": Path("/root/physics-applets-gpt-oss-20b-no-think"),
        "gpu": "A100 40GB",
    },
    {
        "name": "ornith-35b",
        "slug": "physics-ornith-35b-no-think",
        "dir": Path("/root/physics-applets-ornith-35b-no-think"),
        "gpu": "A100 40GB",
        "aesthetic": True,
    },
]

NN_MODELS = [
    {
        "name": "ornith-35b",
        "slug": "nn-ornith-35b-no-think",
        "dir": Path("/root/nn-applets-ornith-35b-no-think"),
        "gpu": "A100 40GB",
    },
]

SUBJECTS = [
    {"name": "Math", "slug": "math", "models": MATH_MODELS},
    {"name": "Physics", "slug": "physics", "models": PHYSICS_MODELS},
    {"name": "Neural Networks", "slug": "neural-networks", "models": NN_MODELS},
]

STYLE_CSS = """
:root { color-scheme: light; }
* { box-sizing: border-box; }
body {
  margin: 0;
  background: #ffffff;
  color: #1a1a1a;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
}
a { color: inherit; }
header { padding: 48px 24px 24px; text-align: center; }
header h1 { margin: 0 0 8px; font-size: 2rem; }
header p { margin: 0; color: #555; }
header h1.site-title { color: #dc2626; }
header p.site-subtitle {
  text-align: center;
  color: #2563eb;
  font-weight: 600;
  font-size: 1.1rem;
  margin: 0 0 16px;
}
header p.browser-tip {
  margin-top: 12px;
  font-size: 0.8rem;
  color: #888;
  font-style: italic;
}
.back-link {
  display: inline-block;
  margin-bottom: 12px;
  font-size: 0.85rem;
  font-weight: 600;
  color: #4338ca;
  text-decoration: none;
}
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 24px;
  max-width: 1200px;
  margin: 0 auto;
  padding: 24px 24px 64px;
}
.subject-grid {
  max-width: 700px;
}
.subject-grid .card h2 { font-size: 1.4rem; }
.card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  border: 1px solid #e2e2e2;
  border-radius: 12px;
  text-decoration: none;
  color: inherit;
  background: #fff;
  box-shadow: 0 1px 3px rgba(0,0,0,0.06);
  transition: transform 0.15s ease, box-shadow 0.15s ease;
  overflow: hidden;
}
.card:hover { transform: translateY(-4px); box-shadow: 0 8px 20px rgba(0,0,0,0.10); }
.card-body { padding: 24px 20px; text-align: center; }
.card h2 { margin: 0; font-size: 1.1rem; }
.card .count { color: #888; font-size: 0.85rem; margin-top: 8px; }
.card.winner {
  position: relative;
  overflow: visible;
  border: 2px solid #f59e0b;
  box-shadow: 0 4px 16px rgba(245, 158, 11, 0.25);
}
.trophy-badge {
  position: absolute;
  top: -18px;
  right: -14px;
  font-size: 2.5rem;
  line-height: 1;
  filter: drop-shadow(0 2px 3px rgba(0,0,0,0.25));
  transform: rotate(12deg);
}
.card.aesthetic {
  position: relative;
  overflow: visible;
  border: 2px solid #ec4899;
  box-shadow: 0 4px 16px rgba(236, 72, 153, 0.25);
}
.aesthetic-badge {
  position: absolute;
  top: -18px;
  left: -14px;
  font-size: 2.2rem;
  line-height: 1;
  filter: drop-shadow(0 2px 3px rgba(0,0,0,0.25));
  transform: rotate(-12deg);
}
.legend {
  max-width: 900px;
  margin: 0 auto 8px;
  padding: 0 24px;
  text-align: center;
  font-size: 0.8rem;
  color: #666;
}
.legend span { margin: 0 10px; white-space: nowrap; }
.gpu-badge {
  display: inline-block;
  margin-top: 10px;
  font-size: 0.7rem;
  font-weight: 600;
  color: #555;
  background: #f2f2f2;
  border-radius: 999px;
  padding: 3px 9px;
}
.model-stats {
  margin: 10px 0 0;
  font-size: 0.7rem;
  color: #888;
  line-height: 1.5;
}
.card-footer {
  padding: 12px 20px;
  font-size: 0.85rem;
  font-weight: 600;
  color: #4338ca;
  border-top: 1px solid #f0f0f0;
  text-align: center;
}
.applet-card .card-body { text-align: left; }
.applet-card h2 { font-size: 1.05rem; }
.description { margin: 8px 0 0; font-size: 0.85rem; color: #444; line-height: 1.4; }
.duration {
  display: inline-block;
  margin-top: 10px;
  margin-right: 6px;
  font-size: 0.75rem;
  font-weight: 600;
  color: #4338ca;
  background: #eef2ff;
  border-radius: 999px;
  padding: 3px 9px;
}
.stage-breakdown {
  margin: 8px 0 0;
  font-size: 0.7rem;
  color: #888;
  line-height: 1.5;
}
.context-info {
  margin: 4px 0 0;
  font-size: 0.7rem;
  color: #aaa;
  line-height: 1.5;
}
.prompt-toggle {
  border-top: 1px solid #f0f0f0;
  padding: 10px 20px;
}
.prompt-toggle summary {
  cursor: pointer;
  font-size: 0.8rem;
  font-weight: 600;
  color: #666;
  list-style: none;
}
.prompt-toggle summary::-webkit-details-marker { display: none; }
.prompt-toggle summary::before { content: "\\25B8  "; }
.prompt-toggle[open] summary::before { content: "\\25BE  "; }
.prompt-text {
  margin: 10px 0 0;
  font-size: 0.8rem;
  color: #333;
  background: #fafafa;
  border: 1px solid #eee;
  border-radius: 8px;
  padding: 10px 12px;
  white-space: pre-wrap;
  line-height: 1.4;
}
footer { text-align: center; color: #999; font-size: 0.8rem; padding: 24px; }
.workflow {
  max-width: 900px;
  margin: 0 auto 16px;
  padding: 0 24px;
  text-align: center;
}
.workflow h2 {
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.03em;
  color: #888;
  margin: 0 0 12px;
}
.workflow svg { width: 100%; height: auto; display: block; margin: 0 auto; }
""".strip()

WORKFLOW_FIGURE_TEMPLATE = """
<section class="workflow">
  <h2>How each applet gets built</h2>
  <svg viewBox="0 0 900 270" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Agentic workflow: prompt to planner to coder to reflector, looping until approved, then published">
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
    <text x="260" y="150" text-anchor="middle" font-size="10" font-weight="600" fill="#4338ca">avg {avg_planner}</text>

    <rect x="360" y="90" width="140" height="72" rx="10" fill="#eef2ff" stroke="#4338ca" stroke-width="1.5"></rect>
    <text x="430" y="112" text-anchor="middle" font-size="13" font-weight="600" fill="#1a1a1a">Coder</text>
    <text x="430" y="128" text-anchor="middle" font-size="10" fill="#666">writes HTML/JS</text>
    <text x="430" y="150" text-anchor="middle" font-size="10" font-weight="600" fill="#4338ca">avg {avg_coder}</text>

    <rect x="530" y="90" width="140" height="72" rx="10" fill="#eef2ff" stroke="#4338ca" stroke-width="1.5"></rect>
    <text x="600" y="112" text-anchor="middle" font-size="13" font-weight="600" fill="#1a1a1a">Reflector</text>
    <text x="600" y="128" text-anchor="middle" font-size="10" fill="#666">tests &amp; reviews</text>
    <text x="600" y="150" text-anchor="middle" font-size="10" font-weight="600" fill="#4338ca">avg {avg_reflect}</text>

    <rect x="700" y="90" width="180" height="72" rx="10" fill="#eef2ff" stroke="#4338ca" stroke-width="1.5"></rect>
    <text x="790" y="112" text-anchor="middle" font-size="13" font-weight="600" fill="#1a1a1a">Published Applet</text>
    <text x="790" y="128" text-anchor="middle" font-size="10" fill="#666">shown below</text>
    <text x="790" y="150" text-anchor="middle" font-size="10" font-weight="600" fill="#4338ca">avg {avg_total} to publish</text>
  </svg>
</section>
""".strip()

SITE_TITLE = "Building Interactive Simulations Using Agentic AI"

HOME_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{site_title}</title>
<meta name="description" content="Interactive math and physics simulations generated by local LLM agents (planner + coder + reflector), compared across models.">
<meta property="og:type" content="website">
<meta property="og:title" content="{site_title}">
<meta property="og:description" content="Interactive math and physics simulations generated by local LLM agents (planner + coder + reflector), compared across models.">
<meta property="og:url" content="{site_url}/">
<meta property="og:image" content="{site_url}/og-image.png">
<meta property="og:image:width" content="{og_image_width}">
<meta property="og:image:height" content="{og_image_height}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{site_title}">
<meta name="twitter:description" content="Interactive math and physics simulations generated by local LLM agents (planner + coder + reflector), compared across models.">
<meta name="twitter:image" content="{site_url}/og-image.png">
<link rel="stylesheet" href="{base}/style.css">
</head>
<body>
<header>
  <h1 class="site-title">{site_title}</h1>
  <p class="site-subtitle">With Open Models</p>
  <p>Pick a subject to see the models building simulations for it</p>
  <p class="browser-tip">Tip: if an applet's animations don't appear to run, try shrinking your browser window to about 80% width.</p>
</header>
{workflow_figure}
<div class="grid subject-grid">{cards}
</div>
<footer>{total} applets across {model_count} models</footer>
</body>
</html>
"""

SUBJECT_CARD_TEMPLATE = """
      <a class="card" href="{base}/{slug}/">
        <div class="card-body">
          <h2>{name}</h2>
          <p class="count">{count_text}</p>
        </div>
        <div class="card-footer">View models &rarr;</div>
      </a>"""

SUBJECT_PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{subject} &middot; {site_title}</title>
<link rel="stylesheet" href="{base}/style.css">
</head>
<body>
<header>
  <a class="back-link" href="{base}/">&larr; All subjects</a>
  <h1>{subject}</h1>
  <p>{count_text}</p>
</header>
{legend}
<div class="grid">{cards}
</div>
<footer><a class="back-link" href="{base}/">&larr; Back to all subjects</a></footer>
</body>
</html>
"""

MODEL_CARD_TEMPLATE = """
      <a class="card{winner_class}{aesthetic_class}" href="{base}/{subject_slug}/models/{slug}/">{trophy_badge}{aesthetic_badge}
        <div class="card-body">
          <h2>{model}</h2>
          <p class="count">{count} applet{plural}</p>
          <span class="gpu-badge">{gpu}</span>
          <p class="model-stats">avg {avg_time} to build &middot; avg {avg_tokens} tokens generated</p>
        </div>
        <div class="card-footer">View applets &rarr;</div>
      </a>"""

TROPHY_BADGE = """
        <span class="trophy-badge" title="Clear winner">&#127942;</span>"""

AESTHETIC_BADGE = """
        <span class="aesthetic-badge" title="Best aesthetics">&#127912;</span>"""

MODEL_PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{model} &middot; {site_title}</title>
<link rel="stylesheet" href="{base}/style.css">
</head>
<body>
<header>
  <a class="back-link" href="{base}/{subject_slug}/">&larr; {subject} models</a>
  <h1>{model}</h1>
  <p>{count} applet{plural} &middot; ran on {gpu}</p>
  <p class="browser-tip">Tip: if an applet's animations don't appear to run, try shrinking your browser window to about 80% width.</p>
</header>
<div class="grid">{cards}
</div>
<footer><a class="back-link" href="{base}/{subject_slug}/">&larr; Back to {subject} models</a></footer>
</body>
</html>
"""

APPLET_CARD_TEMPLATE = """
      <div class="card applet-card">
        <a href="{base}/applets/{slug}/">
          <div class="card-body">
            <h2>{title}</h2>
            <p class="description">{description}</p>
            <span class="duration">{duration}</span>
            <p class="stage-breakdown">{stage_breakdown}</p>
            <p class="context-info">{context_info}</p>
          </div>
        </a>
        <div class="card-footer"><a href="{base}/applets/{slug}/">Open applet &rarr;</a></div>{prompt_block}
      </div>"""

PROMPT_BLOCK_TEMPLATE = """
        <details class="prompt-toggle">
          <summary>View user's prompt</summary>
          <pre class="prompt-text">{prompt}</pre>
        </details>"""


def format_duration(seconds):
    if seconds is None:
        return "unknown"
    seconds = round(seconds)
    minutes, secs = divmod(seconds, 60)
    if minutes:
        return f"{minutes}m {secs}s to build"
    return f"{secs}s to build"


def format_stage_seconds(seconds):
    seconds = round(seconds)
    minutes, secs = divmod(seconds, 60)
    return f"{minutes}m {secs}s" if minutes else f"{secs}s"


def stage_breakdown(meta, reflection):
    """Returns per-stage wall-clock seconds and generated-token counts: the
    initial planner call, the initial coder call, and the full reflect loop
    (every reflector + coder call across all revision turns), plus how many
    reflect turns ran.
    """
    planner_metrics = meta.get("planner", {}).get("metrics", {}) or {}
    coder_metrics = meta.get("coder", {}).get("metrics", {}) or {}
    planner_secs = planner_metrics.get("wall_seconds") or 0
    coder_secs = coder_metrics.get("wall_seconds") or 0
    tokens = (planner_metrics.get("eval_count") or 0) + (coder_metrics.get("eval_count") or 0)
    reflect_secs = 0.0
    for turn in reflection:
        reflector_m = turn.get("reflector_metrics") or {}
        coder_m = turn.get("coder_metrics") or {}
        reflect_secs += reflector_m.get("wall_seconds") or 0
        reflect_secs += coder_m.get("wall_seconds") or 0
        tokens += (reflector_m.get("eval_count") or 0) + (coder_m.get("eval_count") or 0)
    return {
        "planner_seconds": planner_secs,
        "coder_seconds": coder_secs,
        "reflect_seconds": reflect_secs,
        "reflect_turns": len(reflection),
        "total_seconds": planner_secs + coder_secs + reflect_secs,
        "tokens_generated": tokens,
    }


def collect_run_dir_entries(source_dir, model_slug):
    """Collects entries from run folders: <source_dir>/<run>/{applet.html,
    plan.json,meta.json[,reflection.json]}. Non-run-folder items in
    source_dir (stray *.html files, metadata.json/csv, logs) are ignored.
    """
    entries = []
    if not source_dir.is_dir():
        return entries

    for run_dir in sorted(source_dir.iterdir()):
        if not run_dir.is_dir():
            continue
        applet_path = run_dir / "applet.html"
        plan_path = run_dir / "plan.json"
        meta_path = run_dir / "meta.json"
        reflection_path = run_dir / "reflection.json"
        if not (applet_path.exists() and plan_path.exists() and meta_path.exists()):
            continue

        plan = json.loads(plan_path.read_text())
        meta = json.loads(meta_path.read_text())
        reflection = json.loads(reflection_path.read_text()) if reflection_path.exists() else []
        label = meta.get("label", run_dir.name)
        stages = stage_breakdown(meta, reflection)

        entries.append({
            "slug": f"{model_slug}-{label}",
            "title": plan.get("topic", label),
            "description": plan.get("overview", ""),
            "prompt": meta.get("topic"),
            "stages": stages,
            "num_ctx": meta.get("num_ctx"),
            "num_predict": meta.get("num_predict"),
            "path": applet_path,
        })
    return entries


def format_tokens(n):
    if n is None:
        return "unknown"
    if n % 1024 == 0:
        return f"{n // 1024}k"
    return f"{n / 1024:.1f}k"


def render_applet_card(e):
    prompt_block = ""
    if e.get("prompt"):
        prompt_block = PROMPT_BLOCK_TEMPLATE.format(prompt=html.escape(e["prompt"]))

    stages = e["stages"]
    stage_breakdown_text = (
        f"Planner {format_stage_seconds(stages['planner_seconds'])} &middot; "
        f"Coder {format_stage_seconds(stages['coder_seconds'])} &middot; "
        f"Reflect {format_stage_seconds(stages['reflect_seconds'])} "
        f"({stages['reflect_turns']} turn{'' if stages['reflect_turns'] == 1 else 's'})"
    )
    context_text = (
        f"context window {format_tokens(e['num_ctx'])} tokens &middot; "
        f"max output {format_tokens(e['num_predict'])} tokens"
    )

    return APPLET_CARD_TEMPLATE.format(
        base=BASE_PATH,
        slug=html.escape(e["slug"]),
        title=html.escape(e["title"]),
        description=html.escape(e["description"]),
        duration=html.escape(format_duration(stages["total_seconds"])),
        stage_breakdown=stage_breakdown_text,
        context_info=context_text,
        prompt_block=prompt_block,
    )


def render_og_image(workflow_figure):
    """Rasterizes the workflow SVG to a PNG (og-image.png) for link-preview
    unfurling: Slack (and most other unfurlers) won't render a raw SVG
    referenced via og:image, so a PNG is needed. Uses rsvg-convert, with a
    white background since the source SVG has no opaque background of its
    own. Returns (width, height) of the rendered PNG for the og:image:width/
    height meta tags.
    """
    import re
    svg_markup = re.search(r"<svg.*?</svg>", workflow_figure, re.DOTALL).group(0)
    tmp_svg = SITE_ROOT / "_workflow.svg"
    tmp_svg.write_text(svg_markup)
    width = 1200
    height = round(width * 270 / 900)
    try:
        subprocess.run(
            ["rsvg-convert", "-w", str(width), "--background-color=white",
             "-o", str(SITE_ROOT / "og-image.png"), str(tmp_svg)],
            check=True,
        )
    finally:
        tmp_svg.unlink()
    return width, height


def build_subject(subject):
    """Builds /<subject_slug>/index.html (model playcards) and
    /<subject_slug>/models/<model_slug>/index.html (applet playcards) for
    every model in the subject, copying each applet's HTML into
    /applets/<slug>/index.html. Returns (model_cards_html, total_applets).
    """
    subject_slug = subject["slug"]
    subject_dir = SITE_ROOT / subject_slug
    subject_models_dir = subject_dir / "models"
    subject_models_dir.mkdir(parents=True, exist_ok=True)

    model_cards = []
    total = 0
    for model in subject["models"]:
        entries = collect_run_dir_entries(model["dir"], model["slug"])
        count = len(entries)
        total += count

        applet_cards = []
        for e in entries:
            dest_dir = SITE_ROOT / "applets" / e["slug"]
            dest_dir.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(e["path"], dest_dir / "index.html")
            applet_cards.append(render_applet_card(e))

        model_dir = subject_models_dir / model["slug"]
        model_dir.mkdir(parents=True, exist_ok=True)
        (model_dir / "index.html").write_text(MODEL_PAGE_TEMPLATE.format(
            base=BASE_PATH,
            model=html.escape(model["name"]),
            site_title=SITE_TITLE,
            subject=html.escape(subject["name"]),
            subject_slug=subject_slug,
            count=count,
            plural="" if count == 1 else "s",
            gpu=html.escape(model["gpu"]),
            cards="".join(applet_cards),
        ))

        if count:
            avg_time = format_stage_seconds(
                sum(e["stages"]["total_seconds"] for e in entries) / count
            )
            avg_tokens = format_tokens(
                round(sum(e["stages"]["tokens_generated"] for e in entries) / count)
            )
        else:
            avg_time = "n/a"
            avg_tokens = "n/a"

        model_cards.append(MODEL_CARD_TEMPLATE.format(
            base=BASE_PATH,
            subject_slug=subject_slug,
            slug=html.escape(model["slug"]),
            model=html.escape(model["name"]),
            count=count,
            plural="" if count == 1 else "s",
            gpu=html.escape(model["gpu"]),
            avg_time=avg_time,
            avg_tokens=avg_tokens,
            winner_class=" winner" if model.get("winner") else "",
            trophy_badge=TROPHY_BADGE if model.get("winner") else "",
            aesthetic_class=" aesthetic" if model.get("aesthetic") else "",
            aesthetic_badge=AESTHETIC_BADGE if model.get("aesthetic") else "",
        ))

    count_text = (
        f"{total} applet{'' if total == 1 else 's'} across "
        f"{len(subject['models'])} model{'' if len(subject['models']) == 1 else 's'}"
        if subject["models"] else "Coming soon"
    )

    has_winner = any(m.get("winner") for m in subject["models"])
    has_aesthetic = any(m.get("aesthetic") for m in subject["models"])
    legend_bits = []
    if has_winner:
        legend_bits.append("<span>&#127942; Overall winner</span>")
    if has_aesthetic:
        legend_bits.append("<span>&#127912; Best aesthetics</span>")
    legend = f'<div class="legend">{"".join(legend_bits)}</div>' if legend_bits else ""

    (subject_dir / "index.html").write_text(SUBJECT_PAGE_TEMPLATE.format(
        base=BASE_PATH,
        subject=html.escape(subject["name"]),
        site_title=SITE_TITLE,
        count_text=count_text,
        legend=legend,
        cards="".join(model_cards),
    ))

    return total, count_text


def main():
    for subdir in ("applets", "math", "physics"):
        path = SITE_ROOT / subdir
        if path.is_dir():
            shutil.rmtree(path)
    (SITE_ROOT / "applets").mkdir(parents=True)

    (SITE_ROOT / "style.css").write_text(STYLE_CSS)

    subject_cards = []
    total = 0
    model_count = 0
    for subject in SUBJECTS:
        subject_total, count_text = build_subject(subject)
        total += subject_total
        model_count += len(subject["models"])
        subject_cards.append(SUBJECT_CARD_TEMPLATE.format(
            base=BASE_PATH,
            slug=subject["slug"],
            name=html.escape(subject["name"]),
            count_text=count_text,
        ))

    all_entries = [
        e
        for subject in SUBJECTS
        for model in subject["models"]
        for e in collect_run_dir_entries(model["dir"], model["slug"])
    ]
    avg_planner = format_stage_seconds(
        sum(e["stages"]["planner_seconds"] for e in all_entries) / len(all_entries)
    )
    avg_coder = format_stage_seconds(
        sum(e["stages"]["coder_seconds"] for e in all_entries) / len(all_entries)
    )
    avg_reflect = format_stage_seconds(
        sum(e["stages"]["reflect_seconds"] for e in all_entries) / len(all_entries)
    )
    avg_total = format_stage_seconds(
        sum(e["stages"]["total_seconds"] for e in all_entries) / len(all_entries)
    )
    workflow_figure = WORKFLOW_FIGURE_TEMPLATE.format(
        avg_planner=avg_planner, avg_coder=avg_coder, avg_reflect=avg_reflect,
        avg_total=avg_total,
    )

    og_image_width, og_image_height = render_og_image(workflow_figure)

    (SITE_ROOT / "index.html").write_text(HOME_TEMPLATE.format(
        base=BASE_PATH,
        site_title=SITE_TITLE,
        workflow_figure=workflow_figure,
        cards="".join(subject_cards),
        total=total,
        model_count=model_count,
        site_url=SITE_URL,
        og_image_width=og_image_width,
        og_image_height=og_image_height,
    ))

    print(f"Built site with {total} applets across {model_count} models at {SITE_ROOT}")
    for subject in SUBJECTS:
        print(f"{subject['name']}:")
        for model in subject["models"]:
            n = len(collect_run_dir_entries(model["dir"], model["slug"]))
            print(f"  {model['name']}: {n} applets")


if __name__ == "__main__":
    main()
