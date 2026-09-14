# Forward regression observations

Six separate learner scenarios were executed with concrete English responses, five initial archive files, and a revised Interview response/archive after the reference update. No expected-output files or evaluation reports were consulted. No learner baseline or data was reused across scenarios. The evaluator read the relevant skill, AGENTS, task references, record template, and existing parser source. All work was confined to this evaluation directory.

| Scenario | Observed result |
|---|---|
| Email | Complete polite email with greeting/sign-off, specific urban-history interest, and conditional vacancy request. Conversational coaching accompanies exact four-field archive. Placeholder name is explicit. No invented human confirmation. |
| Academic Discussion | Connected prose, both supplied positions represented, and a new education/limited-trial contribution. Archive preserves supplied student summaries and explicitly identifies that full original posts were absent. |
| Interview, initial | Four continuous-prose illustrative answers in one session archive, grouped by field. Models clearly labelled, no actual learner speech, delivery score, or confirmation invented. However, this required resolving a conflict with the inherited instruction to state a confirmed 5/5 verdict. |
| Interview, revised | Reread the new evidence/model exception. Generated a separate revised conversation and archive with a new text-only rubric assessment and no full Speaking score. The exception now directly authorizes the observed behavior. All four model answers and required fields remain intact. |
| Buffer | Source-faithful one-sentence thesis, one domain, three pillars, four lexical pairs, T1 density calculation, and matching archive. Distinguishes intended heat reduction and planned comparison from achieved results. |
| Generic plan | Four-section weekly practice schedule delivered immediately without demanding score/profile data. Coaching synthesis and reference basis are identified. No automatic Buffer or practice archive. |
| Reading record | Original A and revised B remain separate; familiar and untimed conditions recorded; transcript marked inapplicable; permission feedback marked as reported. Missing passage/options prevent a fabricated correctness claim. No model learner history or official score created. |

## Issues

1. Resolved during this evaluation: `reference-response-archive.md` previously asserted that every Interview archive already had human-confirmed 5/5 responses and demanded a direct verdict. That conflicts with the explicit model-only scenario and the lack of audio. The new opening exception resolves this for the revised run. First and revised artifacts remain separate.
2. Remaining inherited tension, low priority: Buffer requires every pillar to be a causal chain even when the source provides purpose and chronological sequence without causal evidence. The actual output labels intended purpose and sequence, and explicitly declines unsupported cooling/survival outcomes. A future narrow statement that evidence boundaries outrank causal formatting would reduce pressure to invent mechanisms.
3. Remaining inherited source-quality concern, low priority: task-specific references still contain stronger claims that Markdown form alone loses scoring credit, even though the skill router correctly says formatting alone cannot establish a score. This did not affect these continuous-prose outputs, but remains an internal inconsistency.

## Verification

`node verify.js` loaded the existing parser functions into isolated VM contexts with `main()` removed; it did not run incoming-folder mutations. Email and Discussion each yielded all four required fields, both Interview versions yielded all ten fields, and Buffer yielded all eight fields. Every detected body exactly matched the corresponding input section, including every complete response. Details are in `parser-verification.json`.

The optional Reading record follows the practice-record template and is intentionally not passed through either archiver. Saves to local `exports/` are not presented as automatic GitHub archiving.

## Files

- `01-email-response.md` through `06-record-response.md`: initial learner-facing outputs.
- `exports/`: initial archive deliverables, arranged by task type.
- `revised/03-interview-response.md`: learner-facing rerun after the exception.
- `revised/exports/interview/reading-habits-demonstration.md`: revised model-only session archive.
- `source-buffer.txt`: exact supplied Buffer source.
- `parser-verification.json`: parser recognition and field-preservation results.
