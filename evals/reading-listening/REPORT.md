# Reading and Listening extension: validation report

Date: 2026-09-14. Target skill: `toefl-2026` (renamed locally after the initial extension evaluation); the GitHub repository URL is unchanged. This report distinguishes executed behavior, authored examples, deterministic checks, and unverified audio properties.

## Delivered changes

- Expanded the skill router, displayed scope, README, and project instructions to all four sections. The router is now 127 lines; detailed existing Speaking, Buffer, and archive procedures load on demand from references.
- Added attributed Reading and Listening course syntheses, official ETS specifications, listening note-taking/retrieval, comprehension coaching, practice generation, and audio-delivery references.
- Added optional practice-record guidance/template, original reading and listening examples, separate reviewed keys, a macOS WAV adapter, and acceptance cases.
- Preserved the existing archive field names and scripts, export destinations, unrelated working-tree edits/deletions. The supplied transcripts were not copied into the repository.

## Executed behavioral evaluations

Independent evaluators were given realistic user prompts and minimum source material, without expected answers or previous conclusions. They loaded the staged skill and relevant references and wrote actual coach outputs. Each evaluator handled separately scoped scenarios within one agent context; these were not 23 isolated model sessions or repeated statistical samples. Parent review inspected the actual outputs and keys, not merely evaluator verdicts.

There were 23 distinct scenarios: seven Reading/summary cases, nine text-only Listening/Speaking cases, six regression/record cases, and one audio-capable announcement interaction. The Interview demonstration was rerun after a rule correction, giving 24 executions in total. Multi-turn audio completion and wrong-answer messages were explicitly illustrative test inputs, not real learner performance.

| Group | Observed behavior | Evidence |
|---|---|---|
| Reading, seven cases | Familiar rereading begins without intake; paraphrase task waits; word completion has ten alternating masks; five questions preserve the passage with separate key; direct answer, valid challenge, and explicit plain summary honored | [Actual Reading outputs and observations](runs/2026-09-14/reading/observed-issues.md) |
| Text-only Listening, nine cases | Notes use relationships and retrieval; original notes are preserved; announcements/response prompts are labelled script-only; next action is distinguished from a later plan; academic feedback offers transfer; replay success is not converted to a score | [Actual Listening outputs and observations](runs/2026-09-14/listening/observed-problems.md) |
| Existing workflows and records, six cases | Email, Discussion, Interview, Buffer, generic four-section plan, and optional Reading record produce applicable outputs; original/revised/model data stay distinct | [Regression outputs and observations](runs/2026-09-14/regression/observed-issues.md) |
| Audio-capable announcement | Real WAV generation, first response with audio only, questions after illustrative completion, then evidence-based feedback and an unanswered variation | [Executed audio sequence](runs/2026-09-14/listening/audio-case/rendering-and-sequencing-report.md) |

All behavioral groups produced the intended release behavior in these runs. This is limited forward-testing, not a learner trial, reliability estimate, official scoring calibration, or psychometric validation. Examples in [worked-interactions.md](worked-interactions.md) are authored demonstrations and are not counted as independent runs. Artifact links in captured outputs were normalized to relative repository paths; response prose is otherwise preserved.

## Failures found and changes made

1. **Silent macOS rendering inside the sandbox.** The renderer returned an audio container with zero frames despite exit success. The new adapter rejected it. Access through the host's normal permission mechanism to the local speech service produced usable PCM. The audio guide documents this boundary instead of treating voice discovery as proof of working synthesis.
2. **Inherited model-score conflict.** The archive workflow assumed human-confirmed 5/5 answers even for an illustrative Interview with no learner speech. A narrow exception now keeps the same fields while marking model provenance and leaving unobserved delivery unassessed. The [revised Interview run](runs/2026-09-14/regression/revised/03-interview-response.md) applied that exception successfully.
3. **Text chunking versus blind playback.** The inherited Speaking workflow was overly broad for a user who supplies text and requests only chunking. It now explicitly permits text-assisted decomposition without requiring a blind attempt or scoring.
4. **Residual format claims.** Review found task-specific paragraphs claiming bullet formatting alone loses rubric credit. The Email, Discussion, and Interview paragraphs now describe a scoped prose-coaching convention. Reading/Listening answers and notes are explicitly exempt. Existing sample answers and rubrics remain in place.
5. **Buffer causal wording.** An inherited requirement for causal chains could pressure the coach to invent a cause from a sequence. A source-evidence precedence statement now requires purposes, sequences, and associations to retain their actual status within the same fields. The observed Buffer output already respected this distinction; no schema change was needed.
6. **Validation environment and links.** The default Python lacked PyYAML; the skill validator ran successfully using an existing cached PyYAML package. The first link check reported the not-yet-written report and mistakenly interpreted an inline-code sample path as a real link. The report was completed and the checker now excludes code examples.

The historical evaluator reports retain concerns as observed at their evaluation time. The narrow source-format, Buffer, and text-chunking edits received static reinspection; the entire behavioral suite was not repeated after those clarifications. The Interview exception received an actual rerun.

## Deterministic and integration checks

Run from the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 evals/reading-listening/checks.py
```

The five checks cover word-completion round-trip reconstruction and mask positions, fixture audio hashes/duration/PCM, invalid audio inputs and speaker assignments, internal reference links, and isolated archive round trips for all four Writing/Speaking task types plus the Buffer. The archive test runs copied existing scripts in temporary folders, preserving every supplied field body and confirming incoming-file processing there. It does not run production archiving. The independent regression evaluator also checked exact parser recognition/body preservation on its actual generated archives; see [parser results](runs/2026-09-14/regression/parser-verification.json).

The standard skill-creator `quick_validate.py` passed for the final frontmatter/name. Existing archive scripts and workflows were not edited by this extension. No plugin manifest changed, so no manifest-specific validator was applicable.

## Audio evidence and remaining limitation

The delivered original announcement [WAV](examples/announcement-audio/audio.wav) is 23.580 seconds, mono 16-bit PCM at 16 kHz. Its [manifest](examples/announcement-audio/manifest.json) matches the source and audio hashes. An independent original announcement produced 21.724 seconds of non-silent WAV and exercised the playback-first sequence. A separate two-speaker adapter smoke test using Samantha and Daniel produced 6.701 seconds, with distinct role-to-voice assignments and a pause between segments.

No audio-inspection or ASR tool was available to verify the spoken content word by word. Script-to-key support, exact renderer input, hashes, duration, and non-silence were checked; these do not prove acoustic correspondence. **Content-level acoustic QA remains pending.** Playable original generation works on this macOS host after access to its speech service, but text-only hosts retain a clearly labelled fallback. No claim is made about enforcement of timing, replay restrictions, real learner performance, or calibrated adaptive delivery.

## Source verification

Current ETS Reading and Listening pages, the linked 2026 blueprint, current test-content page, and official sample-task material were checked on 2026-09-14. Titles, provenance, discrepancies, and limits are recorded in [the ETS reference](../../references/reference-ets-reading-listening-specs.md). Third-party module timing, missing visuals/options, and transcription defects were not promoted to official requirements. The supplied note guide's historical learner difficulties are not treated as a current baseline.

## Publication follow-up

The requested local folder and skill identifier were renamed to `toefl-2026`; the clone destination and project instructions were updated. Earlier forward-run artifacts record the original evaluation context. Preparing the Git commit revealed that the evaluated worktree included an uncommitted Listen and Repeat self-assessment parser field. The release includes only the field recognition and rendering needed to preserve that documented schema. Unrelated local citation-cleanup/numbering changes, archive deletions, and personal exports are excluded. The committed tree receives fresh deterministic validation.
