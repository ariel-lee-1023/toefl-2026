# Build a Sentence workflow

Status: original coaching and engineering design, 2026-09-14. Load [course methods](reference-course-build-a-sentence.md) and the Build a Sentence section of [ETS task specs](reference-ets-task-specs.md). ETS defines official mechanics; the course supplies attributed strategies. The schema, help sequence, difficulty labels, and progression below are local choices.

## Choose the requested interaction

| Request | Delivery |
|---|---|
| Interactive practice | Show context, immutable frame, identified slots, and shuffled tile bank. Wait for the learner. Do not append a key, explanation that gives the answer, or invented learner response |
| Direct solution/explanation | Give the arrangement immediately, unused pieces, and the decisive constraints. Do not impose a quiz |
| Worked demonstration | Label the answer and analysis as a model demonstration |
| Independent batch | Collect initial answers before explanations. A requested key goes in a separate artifact, not interleaved; otherwise retain it for feedback |
| Incomplete supplied item | Explain what is visible; request absent tiles/anchors only when necessary to solve that exact item. Never reconstruct a missing slide as an original |

A score report, error history, and cognitive profile are not prerequisites. Choose the smallest useful task. Preserve the original attempt before feedback, including omissions and uncertainty. If the learner uses text rather than IDs, map it to the supplied tile instances when unambiguous; ask for slot order only if needed. Text alone may not establish which identical instance was placed, but that distinction must not create a false rejection.

## Solve and explain

Inspect anchors, punctuation, bank, and context. Find candidate subjects and finite verbs; identify the outer structure and clause boundaries; assemble clauses; check agreement, complements, modifiers, and meaning; then verify every tile and fixed anchor. The learner need not narrate every step.

Keep four judgments separate: **task constraints**, **grammar**, **context**, and **uncertainty**. Use directing question → structural cue → worked explanation as needed. For an embedded-clause problem, first direct attention to the outer question; then identify the embedded boundary; reveal the full arrangement only when requested or further help is needed.

Original demonstration: context “I need somewhere to study.” Frame `Do you know [s1] [s2] [s3] [s4]?`; tiles `is`, `whether`, `open`, `are`, `the library`. Model answer: “Do you know whether the library is open?” Unused: `are`. In a supplied learner attempt “Do you know whether is the library open?”, the learner inverted the embedded clause. The outer question is `Do + you + know`; the embedded clause is `whether + the library + is + open`. Singular `the library` licenses `is`. This demonstration is not a recovered course or ETS item.

A correct arrangement with an incorrect explanation remains a successful arrangement plus unresolved structural understanding. Challenge keys on the evidence: preserve the proposed alternative, check anchors and pieces, then grammar and context. Accept defensible alternatives, retain the key when the challenge violates a real constraint, or flag a flawed item. Neither the first key nor the learner's insistence is proof. A mechanically valid answer absent from reviewed keys is **unresolved pending language review**, not automatically incorrect.

## Structured item and separate key

Use UTF-8 JSON, schema version `1`. See [items.json](../evals/build-a-sentence/items.json) and the separately stored [keys.json](../evals/build-a-sentence/keys.json). Keys are coach-only during independent delivery; repository separation is organizational, not access control. Do not load expected keys into blind generation/evaluation context.

An item contains `schema_version`, stable `id`, `context`, ordered `frame`, `tiles`, `target_skill`, `provenance`, `estimated_difficulty`, and `review_status`. Each frame element is exactly `{"text": "immutable text"}` or `{"slot": "unique-slot-id"}`. Each tile is exactly `{"id": "unique-tile-id", "text": "exact displayed phrase"}`. Frame text includes punctuation and spacing; a slot takes one intact tile. Bank array order is the displayed shuffle. Repeated text has distinct IDs.

`provenance` records `kind` (original/adapted/supplied/official), `source`, and `date`. For adaptations, record changes and source coverage in `source`; do not claim generated content is official. Difficulty is estimated and should state a reason. `review_status` is `draft`, `reviewed`, or `flawed`; `reviewed` means a documented language review was performed, not that validity was proved.

A key contains matching `item_id`, `accepted` arrangements, and `review`. Each accepted entry has `slots` mapping slot IDs to tile IDs, `answer`, `grammar`, `context_fit`, and optional `expected_unused` IDs. Review contains `reviewer`, `date`, `grammar`, `context`, and `uniqueness`; distinguish an observed alternative from an unproved uniqueness claim. A reviewed item needs reviewed grammar and context, and uniqueness must be assessed or marked uncertain. Keep explanations in the key, not in the learner-facing bank.

An attempt object has `slots`, optionally `answer` (the displayed complete attempt), and optionally `unused`. Retain attempt IDs, assistance and history in the optional record, not in the immutable item. If `answer` is supplied, it must reconstruct from the original frame; moved fixed words are a constraint failure even if the new sentence is grammatical.

Display normalization collapses whitespace only. Rendering concatenates frame strings and exact tile text, then collapses whitespace and trims the ends. Put spaces and punctuation in frame text explicitly. Capitalization, inflection, pronouns, wording, punctuation, and internal phrase boundaries are never changed. Identical displayed tile instances may swap IDs: compare each slot's exact displayed text after validating single use, rather than enforcing the first key's IDs.

Run the standard-library Python helper:

```sh
python3 scripts/validate-build-a-sentence.py evals/build-a-sentence/items.json --keys evals/build-a-sentence/keys.json
python3 scripts/validate-build-a-sentence.py item.json --keys key.json --attempt attempt.json
```

The first command accepts either a single object or lists of items and keys. Attempt mode requires one item. It reports mechanical validity, derived unused IDs and reconstructed answer. With a key it additionally reports `accepted` or `unresolved`; malformed constraints return exit code 1. Invalid JSON, duplicate JSON properties, unknown IDs, missing/reused tiles, altered answers, and inconsistent unused accounting are rejected. No English parser or score converter is implemented. A mechanically valid nonsense sentence can pass this helper, so conduct language review separately.

## Generate original practice

Start with a coherent complete sentence and exchange. Review grammar and contextual fit, choose the target structure and anchors, divide movable material into indivisible tiles, add any reviewed unused choices, and shuffle. Retain the complete item object and separate key object in the versioned JSON schema before learner delivery, including for a single interactive exercise. A learner-facing Markdown frame and a prose key alone are not the retained item model. With filesystem tools, save the item JSON and coach-only key JSON in the task scratch area and run the helper on every generated item or batch before delivery. Do not expose those answer-bearing scratch files during independent practice or create a learner record without a request. Without execution tools, retain the structured objects in working context and disclose that mechanical checks were manual. Review each item from the bank and context without treating its intended answer as authoritative. The reviewed fixtures are reusable examples; they are not sufficient fresh practice for a learner who has already seen them.

Cover direct questions including subject questions; embedded interrogatives; agreement across intervening material; interrupting relative clauses; the three introductory `that` roles; verb complements and multiword tiles; unused pieces from varied categories. Difficulty changes one meaningful dimension at a time: nesting, agreement distance, boundary-word ambiguity, fewer anchors, or a closer competing tile. Length alone is not the difficulty model.

Check competing orders, missing pieces, source grammar, answer-revealing clues, incompatible context, and distractors that also form natural replies. Record reviewed alternatives or revise the item before presenting it. If later challenged successfully, repair the key with a new reviewed arrangement or version the changed item, preserving the original attempt's item snapshot. An extra model review helps but does not establish uniqueness or calibrated difficulty.

Use verified current iBT mechanics before labeling a set exam-format practice. The fixtures and shorter transformations here are **original targeted skill practice using a textual tile interface**, not an official exam simulation.

## Progress and optional records

Use an adjustable progression: identify structure → arrange with a cue → fresh independent arrangement → mixed structures → later independent retest. Unclear clause distinctions call for a simpler contrast; success with a cue calls for fresh material without it; independent success with relevant understanding can justify increasing one difficulty dimension. If correct but slow, keep the language level stable and practise placement/checking. Do not equate immediate repetition with transfer or infer a stable deficit from a mistake. Timing must be measured or explicitly learner-reported, otherwise unknown.

Only when requested or accepted, use [practice records](../practice-records/README.md) and its Build a Sentence fields. In this project save under `exports/practice-records/`, never either archiver's incoming folder. Include original and revised arrangements, unused pieces, item/attempt IDs, assistance and model provenance, separate structural and contextual findings, uncertainty, and linked transfer/retest when available. Local outcomes are correct, incorrect, unresolved, or flawed item. Do not use the composed-response 0–5 rubric, create a polished-answer archive automatically, or convert results to a TOEFL section score.
