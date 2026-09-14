# Active Cognitive Buffer workflow

Extracted from the existing skill workflow on 2026-09-14; existing schema and archive destinations preserved. Apply only to the requested activity.

Preserve the source's evidential strength within the existing fields. When the source gives a purpose, sequence, or association rather than an established cause, label that relationship explicitly. The three-pillar schema never authorizes inventing a mechanism or result. This evidence rule governs the causal-language suggestions below.

## Active Cognitive Buffer: re-encoding raw input
This feature is for requested general study notes, separate from Reading/Listening exam notes and the Writing/Speaking practice tasks and from `polished-5-5-responses/` — it is **input-side** processing, not output drafting. Its premise: a universal note-taking system only works as an **Active Re-Encoding Pipeline**. Raw auditory or reading input — a lecture, a recording, a meeting, a conversation, in any source language — must be forced through a fixed schema that compels synthesis rather than transcription. The output is a TOEFL-ready L2 semantic map of the episode, archived to [`semantic-consolidation-buffer/`](../semantic-consolidation-buffer/) in this repo.

**Evidence boundary.** The mechanism labels below are inherited explanatory metaphors for the study-note exercise. They do not establish a learner diagnosis or experimental validation of this protocol, and references to Integrated tasks describe historical context, not current 2026 task types. Never impose this schema on live listening notes.

**Why the study-note schema is structured.** Each field below maps to a specific cognitive/neurolinguistic mechanism relevant to TOEFL Integrated Writing and Speaking. Understanding the mechanism is what prevents you from "softening" a field into a generic summary when the source material resists it — the constraint is the exercise:

- **Semantic Anchoring** (the `toefl_domain` field) primes the relevant English academic lexicon before any content is processed — tagging an episode "Economics" vs. "Biology" activates a different vocabulary network, the same top-down priming a TOEFL Integrated task relies on when it names its domain up front.
- **Prefrontal Abstraction** (Core Thesis) exercises the dlPFC's inhibitory control: capping the thesis at one sentence forces you to actively suppress tangential detail (neural noise) and raise the signal-to-noise ratio of the core semantic representation. The mandated subordinate clause additionally primes the complex syntax that high-scoring Integrated Writing responses require.
- **Associative Evidence Mapping** (the three pillars) mirrors how TOEFL academic lectures and reading passages are structured — hierarchical logic, not a flat list of facts. Decomposing an episode into Problem → Mechanism → Result trains your predictive-processing model to anticipate structural transitions, which lowers prediction error when you meet the same structure again on test day.
- **Lexical Binding** (the vocabulary pairs) directly targets L1 lateral inhibition: while consuming Chinese-language material, L1 semantic nodes are highly activated and suppress the weaker L2 lemma. Explicitly remapping each high-density term to its precise English academic equivalent immediately, while the concept is still active, trains faster L2 lexical selection under the time pressure of spontaneous speech — and forcing the whole note into English, with no source-language text retained anywhere, is what makes this remapping happen rather than deferring it.

### Length calibration: the Density Score and Expansion Tiers
The four-field count above is fixed for every episode, short or long — that part of the schema never changes. But a fixed field *count* rendered at a fixed *depth* breaks down on dense source material: a 5-minute reading passage and a 48-minute, 19-subtopic interview should not produce the same word count, yet a schema with no density awareness will flatten both to the same short note. The fix is not to add more pillars or more fields for long material — that would defeat the inhibitory-control purpose of the rigid field count. Instead, **only the depth allowed inside each field scales, gated by a Density Score computed from the source before you draft anything.**

**Step 1 — compute the Density Score (D).** Before drafting, estimate two numbers from the raw input:
- **S = segment count** — the number of distinct sub-topics or sub-arguments in the source. If the input already carries headers, bullets, or an existing summary with labeled sections (e.g. a transcript with a pre-existing "smart summary"), count those directly. If it's an unlabeled transcript, count topic shifts using speaker changes, timestamp jumps, and discourse markers (e.g. "moving on to...", "另外一个问题是...", a new named case or study introduced).
- **W = word count** — the total word count of the raw source material (count Chinese characters as words if the source is Chinese).

Compute `D = S + W / 1500`. (1,500 is an initial calibration constant — adjust it later if a Tier consistently feels miscalibrated against real source material.)

**Step 2 — map D to an Expansion Tier.** Tiers are discrete, not a continuous formula, so the scaling stays auditable rather than inviting word-count padding:

| Tier | D range | Typical source |
|---|---|---|
| T1 — Baseline | D < 5 | A single TOEFL-length reading passage or a short podcast clip |
| T2 — Moderate | 5 ≤ D < 12 | A single-topic lecture, 15–20 minutes |
| T3 — High | 12 ≤ D < 20 | A multi-turn interview or a podcast with 2–3 embedded cases |
| T4 — Very High | D ≥ 20 | A long, many-subtopic interview or panel (e.g. a 45+ minute conversation with a dozen or more distinct sub-arguments) |

**Step 3 — apply the Tier to each field's internal depth, never to field count:**
- **Semantic Anchoring** — unchanged at every Tier. Always exactly one dominant domain; priming a vocabulary network only works if there's one network to prime, regardless of source density.
- **Prefrontal Abstraction (Core Thesis)** — always exactly ONE sentence at every Tier (the dlPFC inhibitory-control constraint never relaxes). What scales is the permitted subordinate-clause depth: T1/T2 use a single subordinate clause (`Although X, Y`); T3/T4 permit a second embedded clause layering in the shifted mechanism or scope (`Although X, and even though the driver of X has shifted from A to B, Y`). This is still one sentence — the constraint is about sentence count, not word count.
- **Associative Evidence Mapping (the three pillars)** — always exactly three pillars at every Tier (never add a fourth for density — that breaks the hierarchical Problem → Mechanism → Result mapping this field trains). What scales is the causal-chain length permitted inside each pillar: T1/T2 keep each pillar a single-hop mechanism (X → Y); T3/T4 permit a two-hop chain (X → Y → Z) inside each pillar, which is how a many-subtopic source gets folded in — related sub-arguments scattered across the transcript get merged into one longer causal chain per pillar, not spread across more pillars. Each pillar must still read as a causal chain, never as a flat "A, B, and C happened" list — collapsing into a list at high Tiers defeats the field's purpose just as much as skipping the scaling would.
- **Lexical Binding** — the one field that scales by count, since it's a list by design rather than a compression exercise: the range extends from the base 3-5 up to `min(3 + Tier_number, 10)` pairs (T1/T2: 3-5, T3: up to 6, T4: up to 7-10). Prioritize terms that recur across multiple segments of the source over one-off mentions.

**Non-negotiable at every Tier:** exactly one domain, exactly one thesis sentence (however many clauses), exactly three pillars, and every pillar stated as a causal chain rather than a flat list. If you find yourself wanting to add a fourth pillar or split the thesis into two sentences to fit a dense source, that is a signal to increase the causal-chain depth inside the existing three pillars instead, not to loosen the field count.

**When the user gives you raw input and asks you to process, log, or take notes on it**, do not draft a plain summary. First compute the Density Score and Tier per the steps above, then produce exactly these four fields, in this order, holding to each constraint at the depth the Tier permits:

0. **Semantic Anchoring (Domain Metadata)** — classify the episode into one standard academic domain (e.g. Sociology, Economics, Biology, Humanities). State it plainly; this also becomes the note's `toefl_domain` frontmatter field. If the episode spans domains, name the dominant one — do not hedge with multiple domains.
1. **Prefrontal Abstraction (The Core Thesis)** — ONE complex English sentence synthesizing the entire episode, built on a subordinate clause (`Although...`, `While...`); at T3/T4 a second embedded clause is permitted per the Tier rules above, but it is still one sentence. This forces top-down compression before any supporting detail is recorded.
2. **Associative Evidence Mapping (Logical Architecture)** — exactly three pillars supporting the thesis, written strictly in English and framed as causal mechanisms (X → Y, or X → Y → Z at T3/T4 per the Tier rules above), not a list of facts:
   - Pillar A (Context/Problem)
   - Pillar B (Mechanism/Intervention)
   - Pillar C (Implication/Result)
3. **Lexical Binding (Academic Vocabulary)** — high-density concepts from the episode, count per the Tier rules above (base range 3-5, extending to a maximum of 10 at T4). Every concept is stated entirely in English: if the source term is L1 (Chinese, or any non-English source), translate it to its academic L2 equivalent and use only that English term as the entry — never keep the original-language word. If the source term is already L2 (English), redefine it using a TOEFL-register synonym. Format each as `` `[Plain/Original English Term]` → `[TOEFL Academic Equivalent]` ``.

The whole note is written entirely in English, regardless of the source language — no Chinese or other non-English text appears anywhere in the note, including inside the Lexical Binding entries. Translating fully into English at note-writing time is itself part of the re-encoding exercise, not a cosmetic formatting choice.

This is deliberately input-side comprehension material, not a speaking-output drill: the note is meant to become raw understanding you can call on across reading, listening, writing, and speaking tasks alike, so it stops at the synthesized semantic map and does not require a spoken-recall step to be complete.

State the computed Tier (e.g. "Tier: T3 (D≈14)") in one line before the note itself, so the user can see why the note is the length it is. Give the user the complete four-field note first, in full — same standard as the archive-ready copy block below: no shortening for the sake of the archive step.

### Archive-ready copy block for the Semantic Consolidation Buffer
After giving the complete note, append a single fenced markdown block formatted for direct upload to [`semantic-consolidation-buffer/incoming/`](../semantic-consolidation-buffer/incoming/) in this repo, ready to copy, paste into a `.md`/`.txt` file, and upload as-is. The archive unit is **one episode per block** — if the user processed several source episodes in one sitting, offer one block per episode, never pooled into one file. Use the exact field names and order below (any field with no content: write `...`, never invent content):

```markdown
## Title
<2-5 words naming the episode's actual topic, title case, no punctuation, e.g. "Urban Heat Islands">

## TOEFL Domain
<the domain named in Semantic Anchoring above, e.g. Sociology, Economics, Biology, Humanities>

## Tier
<the Expansion Tier computed above, e.g. "T3 (D≈14)" — carries the density calibration into the archive so the note's depth is auditable later>

## Core Thesis
<the one complex synthesizing sentence from section 1 above, verbatim>

## Pillar A
<Context/Problem pillar from section 2 above, verbatim>

## Pillar B
<Mechanism/Intervention pillar from section 2 above, verbatim>

## Pillar C
<Implication/Result pillar from section 2 above, verbatim>

## Lexical Bindings
<all 3-5 concept lines from section 3 above, one per line, verbatim>
```

Same content-fidelity rule as the separate polished-response archive reference: the copy block carries the SAME content as the full note already given, reorganized into fields — never a shortened digest of it. `Title` and `Tier` are the only fields not literally quoted from the four numbered sections in this workflow; `TOEFL Domain` is the Semantic Anchoring classification stated verbatim, `Tier` is the Density Score/Tier line stated verbatim, and everything else must match the corresponding section exactly — all in English, regardless of the source language.

The [`semantic-consolidation-buffer/`](../semantic-consolidation-buffer/) automation (unlike `polished-5-5-responses/`) has a single `incoming/` folder, not one per task type — every episode uses this same schema regardless of domain or source language, so there is no folder to choose.
