# Revised generation execution

The initial evaluation files remain unchanged. Only prompts 02-interactive and 16-batch were rerun, each as a fresh first turn without any learner attempt.

## Sources

Newly read for this rerun:

- `references/reference-build-a-sentence-workflow.md`, including the updated requirement to save structured objects and run the helper before delivery.
- `scripts/validate-build-a-sentence.py`, now explicitly authorized for generated objects.

Previously loaded source instructions retained in context:

- `AGENTS.md`
- `SKILL.md`
- `references/reference-course-build-a-sentence.md`
- `references/reference-ets-task-specs.md`
- The actual cases from `evals/build-a-sentence/prompts.json`

No fixture items, fixture keys, checks.py, engineering brief, or parent conclusions were read.

## Actual execution and artifacts

Saved version-1 JSON item and separate key objects in `artifacts/scratch/` before learner delivery:

- `02-item.json` and `02-key.json`
- `16-items.json` and `16-keys.json`

Invoked:

```text
python3 scripts/validate-build-a-sentence.py artifacts/scratch/02-item.json --keys artifacts/scratch/02-key.json
python3 scripts/validate-build-a-sentence.py artifacts/scratch/16-items.json --keys artifacts/scratch/16-keys.json
```

Exact helper standard output is saved in `artifacts/02-helper-output.json` and `artifacts/16-helper-output.json`. All three items report structure_valid=true and their accepted arrangements report mechanically_valid=true. The tool invocation completed with exit code 0 and no reported helper error.

Grammar, context, and competing-order judgments are documented separately in the retained keys. The helper is not an English grammar checker, uniqueness proof, or score converter.

The response for case 02 exposes no answer or key link. The response for case 16 links only the requested separate Markdown answer key. Scratch files and helper outputs are retained for evaluation rather than exposed as part of either exercise. No practice record was created, and no learner response was invented.
