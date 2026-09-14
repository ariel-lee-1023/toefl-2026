# Forward-test observations

Seven independent learner scenarios were executed as separate first-turn outputs, using only the skill and its routing references. No existing evaluations, worked interactions, expected answers, or reports were read. Skill files were not edited.

Relevant references loaded: comprehension coaching, course reading, practice generation, ETS Reading/Listening specifications, and Buffer workflow. The Buffer reference was checked only for summary routing; scenario 7 follows the explicit plain-summary request.

Observed behavior:

- Scenario 1 starts a familiar-text paraphrase-repair exercise without requiring a previous mistake or explaining the answer first.
- Scenario 2 provides original practice without requiring the learner to supply a passage. It stops after one task.
- Scenario 3 produces an original 70–100-word academic paragraph with an intact first sentence and ten gaps at every second word of the next twenty words. Mask lengths were checked programmatically, and the retained key is separate from the learner output. No key is linked or exposed in the first-turn response.
- Scenario 4 provides exactly five questions, labels the short-text set as expanded learning, preserves the source verbatim, and delivers its key separately. Five questions on this short source inevitably reuse related information: the purpose item covers arrangements also used in detail items. They remain answerable, but are not five independent proficiency measurements.
- Scenario 5 directly answers the explicitly requested question and explanation without forcing an attempt.
- Scenario 6 accepts the learner's justified objection, withdraws the unsupported key, excludes it from progress judgments, and offers a replacement question without revealing the replacement key.
- Scenario 7 gives a plain summary with no Buffer fields or archive block.

No blocking behavioral issue was observed. This is one agent's forward run, not an empirical learner trial or a demonstration of reliability across repeated model samples. The retained Complete the Words key is an internal testing artifact, not a learner-facing first-turn attachment.
