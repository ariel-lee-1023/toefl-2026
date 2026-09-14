# TOEFL 2026 Coach: Reading, Listening, Writing & Speaking

An agent skill for guided comprehension, precise meaning matching, listening notes and retrieval, and original practice, alongside the existing Writing/Speaking coaching and structured study-note workflow. The local folder and skill identifier are `toefl-2026`. The GitHub repository remains at its existing URL.

The default learning loop is one short task, your attempt, feedback, then a variation. You can start without wrong answers, a score report, or a personal profile. Ask for direct explanations, worked demonstrations, a batch, or the full answer whenever you prefer. Error analysis is available when requested or when reviewing an attempt; it is not the entry point to every session.

## Install

Clone into a skills root your agent reads (Claude Code shown):

```bash
git clone https://github.com/ariel-lee-1023/toefl-2026-writing-speaking.git \
  ~/.claude/skills/toefl-2026
```

Other roots: `~/.copilot/skills/`, `~/.agents/skills/`, `.claude/skills/`, `.agents/skills/`.

## What you can practise

| Area | Capabilities | Example request |
|---|---|---|
| Reading | Complete the Words, Read in Daily Life, Read an Academic Passage; guided rereading and evidence matching | “I have done every question. Help me study this passage again.” |
| Meaning matching | Paraphrases, reference links, conditions, scope, inference, example and paragraph functions | “Train me to spot the smallest meaning change in a paraphrase.” |
| Listening | Choose a Response, Conversation, Announcement, Academic Talk; intent, details, organization, and supported inference | “Give me a short announcement, then ask me what to do next.” |
| Listening notes | Selection, relationship labels, final decisions, cue retrieval, and timed choice comparison | “Here are my notes. I ran out of time searching them.” |
| Original practice | Existing material with new questions, new original material, or focused micro-exercises | “Make five new questions about this passage. Put the key in a separate file.” |
| Writing | Build a Sentence, Write an Email, Academic Discussion | “Help me write a clear, well-supported discussion response.” |
| Speaking | Listen and Repeat, Take an Interview | “Help me chunk this Listen and Repeat sentence.” |
| General study notes | Existing Active Cognitive Buffer and Flexible Mode | “Re-encode this lecture into a structured study note.” |

Familiar material remains useful for learning; success on it is not an independent proficiency measurement. Generated material is labelled original practice. Format-aligned tasks and broader skill exercises are distinguished, and difficulty labels are design estimates. Generated accuracy is never converted into an official section score.

## Library and routing

Only [SKILL.md](SKILL.md) is the entry point. Load the reference needed for the requested activity, not every file. A transcript does not automatically trigger the Buffer, and listening comprehension does not automatically trigger Speaking reproduction.

| Reference | Purpose |
|---|---|
| [ETS Reading/Listening specs](references/reference-ets-reading-listening-specs.md) | Verified task families, presentation, timing and scoring limits |
| [Reading course](references/reference-course-reading.md) | Exam-focused reading and slower learning-focused rereading |
| [Listening course](references/reference-course-listening.md) | Intention, relationships, academic organization and review |
| [Listening note-taking](references/reference-listening-note-taking.md) | Recording and finding useful cues |
| [Comprehension coaching](references/reference-comprehension-coaching.md) | Graduated help, meaning matching and optional error analysis |
| [Practice generation](references/reference-practice-generation.md) | Three modes, task constraints and question-quality checks |
| [Audio delivery](references/reference-audio-delivery.md) | Host discovery, playable local adapter and text-only fallback |
| [ETS Writing/Speaking task specs](references/reference-ets-task-specs.md) | Existing task mechanics, rubrics and rated examples |
| [ETS Writing/Speaking descriptors](references/reference-ets-cefr-descriptors.md) | Existing section performance descriptors |
| [Email](references/reference-magoosh-email-templates.md), [Discussion](references/reference-magoosh-discussion-templates.md), [Interview](references/reference-magoosh-interview-templates.md) | Existing Magoosh teaching frameworks |
| [Listen and Repeat lessons](references/reference-course-listen-repeat-lessons.md), [workflow](references/reference-listen-repeat-workflow.md) | Existing Speaking reproduction coaching |
| [Buffer workflow](references/reference-buffer-workflow.md), [archive formats](references/reference-response-archive.md) | Existing study-note and Writing/Speaking schemas |

## Audio boundaries

Discover host capabilities before promising playable listening. The supported [macOS adapter](references/reference-audio-delivery.md) uses installed English voices through `say` and `afconvert`, with Python 3. It renders a WAV locally without an account or paid service and checks input hashes, duration, format, and non-silence. Host-native audio generation is also usable when available.

A renderer success does not verify every spoken word. Inspect playback or ASR when available; if neither is available, disclose that acoustic correspondence review is pending. Keep the script, key, and explanatory cues out of an independent first attempt. The host may allow replay, so assisted attempts must be labelled honestly. The adapter does not provide ASR, a test timer, replay restrictions, or an adaptive test interface.

When playable audio cannot be generated, use a clearly labelled script-based exercise or guide practice with an accessible learner recording. A script alone is not completed listening practice. Transcripts cannot establish pronunciation, stress, actual audibility, or timestamps. Missing source audio is never reconstructed and presented as the original.

## Optional records and existing archives

[Practice records](practice-records/README.md) are lightweight and opt-in. They capture activity, provenance, familiarity, assistance, the actual attempt, feedback and a next target. Record notes and timing only when available. Local project records go under `exports/practice-records/`; they do not enter the existing archivers.

Existing Email, Discussion, Interview and Listen and Repeat archive fields remain unchanged. The project uses `exports/<task-type>/` for local deliverables. GitHub workflows process uploads to `polished-5-5-responses/incoming/<task-type>/`, and the [Buffer workflow](semantic-consolidation-buffer/README.md) processes `semantic-consolidation-buffer/incoming/`. Saving an export does not run these workflows. Existing locally deleted archive files are not recreated by this extension.

## Retrieval hosts

For a Gem, NotebookLM notebook, or ChatGPT Project, add the router rules to the host's instructions as well as uploading references. Retrieval can omit important routing context. A compact instruction block:

```text
Route by the learner's activity. Explicit comprehension, listening notes, new
practice, and error analysis take precedence over raw-input study-note routing.
Default to one short exercise, wait for the attempt, then give feedback and a
variation. Honor direct-answer and batch requests. Keep question sets and keys
separate; withhold listening transcripts and answer-specific cues before a first
attempt unless scaffolding is requested. Discover audio capabilities; scripts
alone are text-based work. Draft Email, Discussion and Interview answers in
connected prose. Choices, missing letters, evidence spans and exam notes may be
short. Records are optional for Reading/Listening. Use ETS for official rules,
the attributed courses for methods, and label original coaching designs.
```

## Sources and evidence limits

The original library draws on ETS Official Guide Chapters 4–5, ETS Writing/Speaking performance descriptors, three Magoosh template guides, and a third-party Listen and Repeat lesson series. This extension adds current ETS Reading/Listening pages, the 2026 blueprint and sample overview, the supplied Reading and Listening course transcripts, and the supplied 2026-09-14 note-taking guide. Each new reference records provenance, verification date, and coverage limits. The course documents contain missing slides, omitted choices, transcription errors, and unavailable audio. This release distils their methods rather than publishing the full transcripts.

ETS defines official mechanics. Course pacing and note routines are adjustable suggestions. The note guide's past learner difficulties are historical reports, not assumptions about every user. Cognitive-science language supplies possible explanations, not clinical diagnoses or evidence that this coaching protocol was experimentally validated. An optional companion [Cognitive-Neuroscience-Expert](https://github.com/ariel-lee-1023/Cognitive-Neuroscience-Expert) analysis must use actual supplied work and qualify its conclusions; it is not required for practice.

TOEFL and TOEFL iBT are registered trademarks of ETS. This project is unaffiliated with and unendorsed by ETS or Magoosh.

## Examples and validation

See [worked interactions](evals/reading-listening/worked-interactions.md), [original question set](evals/reading-listening/examples/questions.md), [separate reviewed key](evals/reading-listening/examples/answer-key.md), and [evaluation report](evals/reading-listening/REPORT.md). Illustrative learner replies in demonstrations are not real learner results. Behavioral evaluations inspect actual outputs; structural checks alone do not establish coaching quality or psychometric validity.

## Built with

[Books-to-Skill-Refs](https://github.com/ariel-lee-1023/Books-to-Skill-Refs): multi-source distillation into a cross-referenced knowledge library.
