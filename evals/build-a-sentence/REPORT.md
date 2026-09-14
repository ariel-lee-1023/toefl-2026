# Build a Sentence implementation evidence

Date: 2026-09-14. Base commit: `7646bcbd6c0903147151e63c018779056af42cdc`, with pre-existing local modifications and archive deletions. This feature is an uncommitted scoped update. [Source hashes](source-hashes.json) identify the exact final coaching, fixture, and validator contents and the earlier workflow used in the first behavioral pass. Existing archive scripts are hashed separately because one was already locally modified.

## What ran

| Check | Actual execution and result |
|---|---|
| Mechanical contract | `python3 evals/build-a-sentence/checks.py`: 18 test methods passed, both in staging and after initial delivery. The validator was unchanged by the later workflow clarification |
| Reviewed fixture keys | 11 original items, 13 accepted arrangements; all keys reconstructed, including multiword tiles and alternative orders. Identical tile-ID swaps passed; missing, reused, unknown, or malformed pieces failed clearly |
| Grammar boundary | A mechanically complete inverted embedded clause remained unresolved by key lookup; mechanical success did not become a grammar verdict |
| Skill frontmatter | The skill-creator `quick_validate.py` passed. System Python lacked PyYAML initially; PyYAML 6.0.3 was installed only in a temporary validation dependency directory, then the prescribed validator ran successfully |
| Existing content/audio/archive checks | Four existing Reading/Listening test methods passed: word-completion reconstruction, audio fixture integrity, audio input rejection, and all four Writing/Speaking plus Buffer archive schema round trips |
| Actual generated archive artifacts | Both the independent Email and Buffer exports passed the existing parsers in isolated temporary repositories, preserving every non-title input field. [Parser evidence](archive-verification.json) |
| Behavioral execution | A separate agent received the skill, relevant references, and [18 realistic prompts](prompts.json), without fixture keys or the engineering brief. It saved actual responses and requested synthetic artifacts. All 18 were inspected; two generation cases needed a retention repair and were rerun |
| Corrected generation | Revised cases 02 and 16 saved full JSON items and separate keys, ran the helper successfully on three newly generated items, and retained learner-facing question/key separation |
| Repository checks | `git diff --check` passed. Delivered files matched staging. New local links resolved; existing links into the user's locally deleted polished-response archive were treated as baseline gaps and not repaired by this feature |

The existing regression command selected `PracticeChecks.test_complete_words_round_trip`, `PracticeChecks.test_audio_fixture_integrity`, `PracticeChecks.test_audio_rejects_ambiguous_roles_and_control_markup`, and `PracticeChecks.test_archive_input_round_trip` from `evals/reading-listening/checks.py`. The whole old link test was not reported as passing: its archive destinations were already absent in this checkout.

## Behavioral evidence by case

Responses and synthetic artifacts are retained under [initial runs](runs/2026-09-14/initial/read-manifest.md). Paths in captured Markdown were converted from evaluation-local absolute paths to portable relative links; coaching text was preserved. Keys inside these evidence folders are for maintainers, not an independent learner's first turn.

| Cases | Observed result |
|---|---|
| [01 direct embedded](runs/2026-09-14/initial/01-direct-embedded.md), [03 subject question](runs/2026-09-14/initial/03-subject-question.md) | Answered immediately, distinguished clause order, preserved bank and unused pieces, and qualified auxiliary generalization |
| [04 agreement](runs/2026-09-14/initial/04-agreement.md), [05 that](runs/2026-09-14/initial/05-that.md) | Used the subject head across a modifier; explained relative, content-clause, and demonstrative roles without a reporting-verb keyword rule |
| [06 conjunction](runs/2026-09-14/initial/06-conjunction.md), [07 negator](runs/2026-09-14/initial/07-negator.md) | Eliminated extras by available syntax and meaning, without a verb-form frequency rule |
| [08 defensible challenge](runs/2026-09-14/initial/08-valid-challenge.md), [09 indefensible challenge](runs/2026-09-14/initial/09-invalid-challenge.md) | Accepted a natural final-adverb alternative; retained the justified embedded-order correction against an unsupported challenge |
| [10 missing layout](runs/2026-09-14/initial/10-missing-layout.md), [11 fixed text](runs/2026-09-14/initial/11-fixed-moved.md) | Did not fabricate the absent slide; distinguished a grammatical sentence from a violation of the fixed frame |
| [12 faulty explanation](runs/2026-09-14/initial/12-faulty-explanation.md) | Marked the arrangement correct while identifying the learner's incorrect explanation |
| [13 requested record](runs/2026-09-14/initial/13-record.md) | Preserved item/attempt IDs, original bank and frame, both orders, unused tile, unknown timing and first-attempt assistance, and the cued revision; did not invent transfer |
| [14 Reading](runs/2026-09-14/initial/14-reading-regression.md), [15 Listening notes](runs/2026-09-14/initial/15-listening-regression.md) | Waited on comprehension; labeled transcript-derived notes retrospectively without switching into Speaking or Buffer |
| [17 Email](runs/2026-09-14/initial/17-email-regression.md), [18 Buffer](runs/2026-09-14/initial/18-buffer-regression.md) | Preserved their separate coaching and archive formats. Email disclosed a timeline assumption and model-added detail; Buffer kept source purpose separate from measured results |
| [02 revised interactive](runs/2026-09-14/revised/02-interactive.md), [16 revised batch](runs/2026-09-14/revised/16-batch.md) | Fresh question delivery without invented attempts; retained item/key JSON and mechanical outputs; interactive key withheld and requested batch key separate |

## Failure found and repair

Initial cases [02](runs/2026-09-14/initial/02-interactive.md) and [16](runs/2026-09-14/initial/16-batch.md) respected the learner interaction but retained prose keys without complete schema objects. The workflow described the schema yet explicitly called for helper execution only for structured batches. It now requires retaining full item and key JSON even for one interactive item, and running the helper when execution tools are available. Text-only hosts retain structured objects in working context and disclose manual checking.

The first pass excluded validator scripts to keep coaching behavior separate; non-execution itself was therefore not counted as a skill failure. The rerun allowed only the helper on the evaluator's own generated items, still excluding fixture keys. Initial outputs were preserved. Revised [single-item helper output](runs/2026-09-14/revised/artifacts/02-helper-output.json) and [batch helper output](runs/2026-09-14/revised/artifacts/16-helper-output.json) both succeeded. The other 16 cases were not rerun because the repair changed only generation retention/execution.

Before fixture delivery, review also retained two room orders and two adverb positions instead of enforcing a single target. The source audit removed unsupported distractor-frequency and universal question-order inferences and scoped composition scoring away from arrangement.

## Limits

This is one independent agent pass, with scenarios treated separately inside one evaluator context, followed by two focused reruns in that evaluator. Some prompts overlap examples in the skill, so the pass is not fully blind grammar testing. Raw expected fixture keys were withheld; the implementing assistant authored and reviewed fixture language. Review-status fields document a judgment; the helper cannot verify that a reviewer is correct.

The evaluation covers first-turn coaching outputs, supplied synthetic attempt/revision records, and separate generation artifacts. It is not a longitudinal learner session, a timing study, proof of grammatical uniqueness, or evidence of improved TOEFL scores. Actual learner transfer and delayed retention remain unmeasured. The live ETS Writing page check confirms the basic arrangement task, not universal blank counts, distractor frequencies, or a detailed item-scoring policy. Existing personal exports, archive history, and unrelated changes were preserved.
