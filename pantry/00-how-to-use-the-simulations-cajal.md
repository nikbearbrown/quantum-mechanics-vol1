# CAJAL Figure Report — Chapter 0 — How to Use the Simulations

Recommended: 2 figures, Foundational density.

Chapter 0 is a procedural and conceptual chapter about a toolchain — not a physics derivation chapter. Most of its content is prose instructions, code listings, and mathematical results stated for future reference. Two genuine figure opportunities fire: one MC on the three-file system relationship (a structural claim hard to hold in the head), and one VG on the four-move prompt workflow (a sequential process whose order and dependency structure cannot be verified from enumerated prose alone). A third candidate — the wave packet physics (group vs. phase velocity) — is explicitly deferred to Chapters 1 and 2 and should be figured there, not here. No PQ material is present; every quantitative result (doubling time, group velocity) is a worked example with no distribution or comparison to plot.

---

## Figure 1 — The Three-File Architecture

**Heuristic:** VG (hierarchy / structural claim)
**Rank:** Critical

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a systems diagram showing three rectangular nodes arranged in a horizontal row: one node on the left labeled implicitly as the behavioral constitution, one node in the center as the visual constitution, and one node on the right as the project state memory. Below all three, a fourth rectangular node represents a single simulation prompt event. Draw a directed arrow from the left node down to the prompt node, a dashed reference arrow (arrowhead at prompt end) from the center node down to the prompt node — indicating the visual file is referenced by name but not quoted — and a directed arrow from the right node down to the prompt node. Above the three upper nodes, draw a single horizontal bracket spanning all three, indicating the overall governing apparatus. Between the left node and the center node, draw a labeled connector indicating the separation axis: "behavior vs. appearance." Between the center node and the right node, draw a labeled connector indicating "appearance vs. state." From the prompt node draw a single downward arrow to a fifth node representing the generated HTML simulation file. Keep all arrows flat or rectilinear; no diagonal strokes. The diagram must be blank and unannotated — no text labels baked in.

### BLOCK 2 — FULL SCOPE

**[S]** Single-column 89 mm, 300 DPI, vector, white background.

**[C]** Five nodes only — exactly as in chapter: CLAUDE.md (coding constitution: runtime, library, SVG, animation, normalization), DESIGN.md (visual constitution: colors, fonts, colormaps), PROJECT.md (project state: verified sims, open bugs, conventions), the prompt event (four-move prompt invocation), and the output HTML simulation file. Two relationships: full-load arrow (CLAUDE.md → prompt; PROJECT.md → prompt) vs. reference-only dashed arrow (DESIGN.md → prompt, label "referenced by name, not quoted"). One output arrow (prompt → HTML file). The bracket above the three file nodes encodes "the apparatus" as a unit. The separation connectors between adjacent file nodes encode the two design axes: behavior/appearance and appearance/state. Do not infer any relationship not stated in chapter text.

**[O]** Three file nodes in a horizontal row at top, vertically equidistant. Prompt event node centered below the row, connected from all three. Output node below prompt. Arrows: solid filled arrowhead for full-load; dashed line with open arrowhead for reference-only. Bracket above top row spans full width. Separation connectors appear as thin double-headed lines between adjacent top nodes with a perpendicular tick mark at midpoint. Overall flow direction: top → bottom.

**[P]** Flat vector, Okabe-Ito palette, 1 pt strokes, white background, no baked text. CLAUDE.md node: Sky Blue #56B4E9 (primary anchor — most loaded file). DESIGN.md node: Orange #E69F00 (secondary). PROJECT.md node: Reddish Purple #CC79A7 (transitional/memory role). Prompt event node: Bluish Green #009E73 (active/process). Output HTML node: Blue #0072B2 (dominant, final product). Full-load arrows: Blue #0072B2 solid, 1 pt. Reference-only arrow: light gray dashed, 1 pt. Bracket: neutral light gray, 1 pt. Separation connectors: neutral light gray, 0.5 pt.

**[E]** EXCLUSIONS: do not show the content of any file (no code snippets, no bullet lists inside nodes); do not show the LLM/Claude system itself as a node — it is implied by the prompt node; do not include any "Chapter N" labels or version numbers; do not show the extension prompt (Part F) as a separate workflow — this diagram covers the core three-file setup only; do not include a legend box.

### BLOCK 3 — NEGATIVE PROMPT

photographic LLM interface screenshots, chat bubble UI, terminal window chrome, filesystem folder icons, gear or settings icons, nested boxes suggesting containment hierarchy, circular nodes, cloud shapes, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 2 — The Four-Move Prompt Workflow

**Heuristic:** MC (mechanism/process — 4 sequential interdependent steps with defined inputs/outputs)
**Rank:** Important

### BLOCK 1 — ILLUSTRAE PASTE BLOCK

Draw a vertical process flowchart of four sequential rectangular step nodes connected by downward arrows, representing four moves in order: Show, Say, Constrain, Verify. To the right of each step node, draw a small annotation box connected by a horizontal arrow, indicating what that move contributes to the output: Show contributes the exact artifact (equation/formula); Say contributes the deliverable specification (format, audience); Constrain contributes the search-space boundary (named constraints); Verify converts the output into a testable rubric. Below the fourth step node, draw a downward arrow leading to an outcome node representing the verification rubric. From the outcome node, draw a feedback arrow looping left and upward, re-entering the flow between step 3 and step 4, indicating the iterative correction loop when a check fails. The diagram must be blank and unannotated — no text labels baked in.

### BLOCK 2 — FULL SCOPE

**[S]** Single-column 89 mm, 300 DPI, vector, white background.

**[C]** Exactly four process steps in order as specified in chapter: (1) Show — paste the exact artifact, (2) Say — state the deliverable in one sentence, (3) Constrain — name additional constraints beyond CLAUDE.md, (4) Verify — ask Claude what to check. Annotation boxes contain the contribution/output of each move — these are inferred summary relations, label as inferred. Outcome node: the verification rubric (four-item checklist). Feedback loop: from rubric back into the workflow when a check fails, targeting the Constrain-to-Verify transition — this is the "if a check fails, you know what to fix" loop from chapter text. No more than 8 labeled components total.

**[O]** Vertical flowchart, top to bottom. Step nodes are rectangles in a single center column. Annotation boxes float to the right of their parent step, connected by a short horizontal arrow (→). Outcome node at bottom, wider than step nodes. Feedback arrow: exits left of outcome node, travels up the left side, re-enters between steps 3 and 4 with an arrowhead. Flow progression: → downward arrows, 1 pt solid. Feedback: ⊣ style blockage/correction — Vermillion #D55E00 curved arrow, indicating the failure path.

**[P]** Flat vector, Okabe-Ito palette, 1 pt strokes, white background, no baked text. Step nodes 1–4: Sky Blue #56B4E9 (primary anchor). Annotation boxes: light gray fill, 0.5 pt gray stroke. Main flow arrows: Blue #0072B2, solid, 1 pt, filled arrowhead. Outcome/rubric node: Bluish Green #009E73 (active/positive result). Feedback/correction arrow: Vermillion #D55E00 (blocking/negative — failure path), 1 pt dashed, open arrowhead.

**[E]** EXCLUSIONS: do not show the three Markdown files as nodes in this diagram — file loading is captured in Figure 1; do not show the specific physics of any simulation prompt; do not add a "first try / second try" branch — the chapter mentions it but it is not a structural feature of the workflow; do not show a clock or time axis; do not show Claude as a box in the diagram — it is implicit in the process.

### BLOCK 3 — NEGATIVE PROMPT

speech bubble thought-cloud for AI, robot or avatar icons, branching decision diamonds, percentage success labels, star-rating icons, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Video Candidate Pass

**Figure 1 — Three-File Architecture:** STATIC SUFFICIENT. Criterion: the structural relationship is a fixed hierarchy with no transition mechanism as the learning target; all three connections are simultaneous and stable, not sequential.

**Figure 2 — Four-Move Prompt Workflow:** VIDEO CANDIDATE. Criterion: four sequential causal stages with a feedback loop — the correction cycle (verify → fail → constrain → re-verify) is a transition mechanism that is the learning target. A 20-second animation showing each move illuminating in sequence, the rubric generating, and the failure-path arrow activating in red would convey the iterative nature that a static diagram collapses into a single frozen state. RECOMMENDED VIDEO.
