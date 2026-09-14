# Existing Writing and Speaking archive formats

Extracted from the existing skill workflow on 2026-09-14; existing schema and archive destinations preserved. Apply only to the requested activity.

## Evidence and model demonstrations

Keep these input fields unchanged. Confirmed-response instructions below apply only when that confirmation actually exists. A request for an illustrative model answer does not establish a learner's performance or human-confirmed score. If an archive is requested for a model, identify it as a model in `My Score Explained`, assess only supported text criteria, and leave unobserved speaking delivery unassessed. Never invent confirmation or an audio-based score to fill the schema.

## After answering: offer an archive-ready copy block
Whenever a user asks to diagnose, score, or polish a response for one of the four task types below, **first give the full, complete answer with substantive coaching and full examples**. Connected prose applies to composed test answers; coaching tables and archive fields may use structure. Only *after* that complete answer, **append a single fenced markdown block** formatted for direct upload to `polished-5-5-responses/incoming/<task-type>/` in the [toefl-2026-writing-speaking repo](https://github.com/ariel-lee-1023/toefl-2026-writing-speaking), ready to copy, paste into a `.md`/`.txt` file, and upload as-is. The archive unit is **one question per block** for Write an Email, Academic Discussion, and Listen and Repeat — but **one full 4-question session per block** for Take an Interview (see below). Use the exact field names and order below (any field with no content: write `...` or omit it, never invent content).

**None of the four task types use a `My Diagnosis` field anymore.** Write an Email, Academic Discussion, and Take an Interview all archive only confirmed-5/5 responses, so they use `My Score Explained` instead (see below), which always states the 5/5 verdict and the rubric criteria behind it, never a gap analysis. Listen and Repeat keeps its own separate shape (`My Self-Assessment`, etc. — see below) and was never part of the diagnosis pipeline in the first place.

**Every copy block starts with a `## Title` field.** This is the ONE field the archiving script does not try to extract from anything else — it uses your Title verbatim to name the archived file (e.g. `## Title\nReading Habits` archives as `00X-reading-habits.md`). Do not skip it and do not let the script guess: guessing from the first few words of the Prompt fails badly when the prompt opens with small talk or instructions ("Thank you for your participation...", "Before they leave, thank customers...") — the real topic gets buried past the words the script samples, producing meaningless filenames. Write 2-5 words naming the actual topic or scenario of the session (e.g. `Reading Habits`, `Retail Checkout`, `Requesting a Deadline Extension`), in title case, with no punctuation, and no restating of the task type itself (never `Interview Session` or `Email Prompt`).

**Critical: the copy block must carry the SAME content as the full answer above it, not a shortened summary of it.** Every field's content must be the substance already given in the full answer — reorganized/labeled into the right field, quoting or closely paraphrasing your own explanations, examples, and reasoning — never a compressed bullet stub that drops the specifics (concrete chunk examples, the exact words flagged for pronunciation, the reasoning behind each fix, etc.). If a field would otherwise come out shorter than the corresponding material in the full answer, that is a sign content was dropped — go back and carry it over instead. The two parts (full answer, then copy block) should read as the same information in two formats, not as an answer followed by a lossy digest of it. The only thing the block strips is prose connectors needed for spoken/written flow — not analytical content. Do not add extra commentary inside the block itself beyond the field content — it must match the repo's automated archiver output 1:1.

**Write an Email** — confirmed-5/5 record, one question per block. The human user has already confirmed the polished response IS a 5/5 answer before it gets archived, so there is no draft-vs-final diagnosis step and no "what changed" to explain — there is nothing being fixed. Never ask for or include a raw draft here, and never frame this as a before/after correction:
```markdown
## Title
<2-5 words naming this question's actual topic/scenario, e.g. "Requesting a Deadline Extension">

## Prompt
<the exact original question/prompt>

## My Polished Response
<the confirmed-5/5 response, upload-ready as-is>

## My Score Explained
<name each rubric criterion from references/reference-ets-task-specs.md the response satisfies — task fulfillment/all required content points addressed, appropriate register and tone for the recipient, clear organization, idiomatic/error-free language, sufficient length — quoting the exact phrase or sentence that demonstrates each one. State the 5/5 verdict directly; do not invent a flaw or hedge the score just to fill this field.>
```
Same content-fidelity rule as above: carry over the actual reasoning from the full answer into this field, don't compress it into a generic bullet.

**Academic Discussion** — confirmed-5/5 record, one question per block. Same shape as Write an Email above and for the same reason: the human user has already confirmed the polished response IS a 5/5 answer before it gets archived, so there is no draft-vs-final diagnosis step and no "what changed" to explain. Never ask for or include a raw draft here, and never frame this as a before/after correction:
```markdown
## Title
<2-5 words naming this question's actual topic/scenario, e.g. "Universal Basic Income Debate">

## Prompt
<the exact original prompt, including both student posts>

## My Polished Response
<the confirmed-5/5 response, upload-ready as-is>

## My Score Explained
<name each rubric criterion from references/reference-ets-task-specs.md the response satisfies — clear stance, engagement with both student posts by name/paraphrase, an original contribution beyond either student, coherent sequencing, sufficient length, idiomatic/error-free language — quoting the exact phrase or sentence that demonstrates each one. State the 5/5 verdict directly; do not invent a flaw or hedge the score just to fill this field.>
```
Same content-fidelity rule: carry over the actual reasoning from the full answer, don't compress it into a generic bullet.

**Take an Interview** — session-level template, NOT one block per question, and a confirmed-5/5 record like Write an Email and Academic Discussion above. The real Interview task presents 4 questions back-to-back in one sitting with zero prep time, so the archive unit is the whole session (Q1-Q4 together), never a single question. By the time a session gets archived, **the human user has already confirmed all 4 answers read as a 5/5 session** — so there is no `My Draft` and no `My What Changed & Why`, only one shared `My Score Explained` at the end. Whenever a user works through an interview session (whether they gave you all 4 up front or one at a time across the conversation), wait until all 4 are answered and confirmed, then emit exactly ONE block covering all of them. Group by field type, not by question — all four Prompts together, then all four Polished Responses together — so a reader can scan straight down each field type across the whole session:
```markdown
## Title
<2-5 words naming this session's actual topic, e.g. "Reading Habits" — never derived from Q1's opening small talk>

## Q1 Prompt
<question 1>

## Q2 Prompt
<question 2>

## Q3 Prompt
<question 3>

## Q4 Prompt
<question 4>

## Q1 My Polished Response
<confirmed-5/5 answer 1, upload-ready as-is>

## Q2 My Polished Response
<confirmed-5/5 answer 2, upload-ready as-is>

## Q3 My Polished Response
<confirmed-5/5 answer 3, upload-ready as-is>

## Q4 My Polished Response
<confirmed-5/5 answer 4, upload-ready as-is>

## My Score Explained
<name each rubric criterion from references/reference-ets-task-specs.md the session satisfies across all 4 answers — relevance/task fulfillment for each question, coherent and idiomatic delivery, appropriate development and detail, natural connectors between ideas — quoting the exact phrase or sentence from the polished responses above that demonstrates each one. State the 5/5 verdict directly; do not invent a flaw or hedge the score just to fill this field.>
```
The archiving script accepts any order for these labels internally (each field is independently detected by its own heading and regrouped into this Prompt/Polished layout regardless of the order the host AI wrote them in), but produce them in this order directly since it reads more naturally and avoids relying on the script's regrouping. Same content-fidelity rule as the other templates: carry over the actual reasoning and examples from the full answer, don't compress them into shorter generic bullets.

If the user only completed 1-3 questions of a session so far, do not emit the copy block yet — offer it only once the full 4-question session is done. If the session genuinely has fewer or more than 4 questions, adjust the Q-numbering accordingly, but still keep it as ONE block for the whole session, never split per question.

**Listen and Repeat** — different shape (sentence-level shadowing, not draft→polish), one sentence-set per block. **This block is the write-up of the six-step procedure in [the Speaking workflow](reference-listen-repeat-workflow.md)** — steps 1–5 become `Set Map`, and step 6 becomes `My Self-Assessment`. Do not re-derive anything here; transfer it.
```markdown
## Title
<2-5 words naming this sentence set's actual scenario, e.g. "Retail Checkout" — never derived from the sentences' opening words>

## Prompt
Scenario: <the one-line frame the task gave, e.g. "a supervisor training you at a hotel front desk">

1. <sentence 1>
2. <sentence 2>

## Set Map
<one table row per sentence, numbered to match the Prompt — the per-sentence layer that makes the archive reviewable later. Columns exactly as below.>
| # | Block | Chunks (type → text) | Shape & cues | Function words at risk | Endings at risk |
|---|---|---|---|---|---|
| 1 | short (7 w) | action → <text> · purpose → <text> | bare imperative | <word> (purpose chunk → to/for) | <word> (-s) |
| 7 | long (14 w) | <2-4 chunks, never more> | <and-serial / softened / front-loaded time-purpose / that-who or if-then> + the cue word | <words> | <words, or "none"> |

## My Chunking & Memory Strategy
<prose from the answer above: WHY the boundaries fall where they do, which cue word signalled each chunk type, and what generalizes to the next set. Not a bare chunk-label list.>

## My Pronunciation Focus
- Compressed function words: <which ones, each paired with the chunk type that reconstructs it>
- Word endings (-s / -ed / final t-d): <the specific words from THIS set, plus the content words that carry no ending>
- Rhythm & stress: <which syllables the speaker stressed; where the user substituted their own rhythm>
- Content words to say crisply: <the ones at risk of being blurred>

## My Self-Assessment
<per-sentence score, then the tally — this is what makes practice cumulative across sets>
| # | Score | What I lost | Cause category |
|---|---|---|---|
| 1 | 5/5 | <or "nothing"> | <function word / word ending / blurred content word / truncation / rhythm substitution> |

- Set score: <average>/5
- Error tally: function word ×_ · word ending ×_ · blurred content word ×_ · truncation ×_ · rhythm ×_
- Next drill: <ONE category plus a sentence length, not a list>
```
Rules for this block: **every sentence in the Prompt gets a Set Map row** — a pooled comma-separated list of chunks across all seven sentences destroys the review value, because you can no longer tell which chunk belonged to which sentence. Chunk counts stay at four or fewer per row. Endings are named word by word, never as a category. If the user did not attempt the sentences aloud, leave the score cells as `...` rather than inventing a score, but still fill the Set Map — the decomposition is valid without an attempt.

The two prose fields (`My Chunking & Memory Strategy`, `My Pronunciation Focus`) carry the actual analysis from the answer above, not a compressed digest of it.

Remind the user, briefly, that v1.0 of the archiver expects **one question per file for Write an Email / Academic Discussion / Listen and Repeat** — if they worked through multiple questions of one of those types in one sitting, they need one copy block (and one upload) per question. **Take an Interview is the opposite**: all 4 questions of one session go into a single file/upload — never split an interview session across multiple files.
