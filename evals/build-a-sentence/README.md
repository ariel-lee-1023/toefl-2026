# Build a Sentence validation

These are original targeted skill exercises, not official or calibrated TOEFL items. [Items](items.json) contain frames and shuffled banks; [keys](keys.json) contain separately reviewed arrangements, grammatical constraints, contextual fit, and review limits. Keep keys out of independent learner delivery and blind generation contexts.

From the repository root, using Python 3 with no extra runtime dependency:

```sh
python3 scripts/validate-build-a-sentence.py evals/build-a-sentence/items.json --keys evals/build-a-sentence/keys.json
python3 evals/build-a-sentence/checks.py
```

The 11 fixtures cover embedded and subject questions, intervening agreement, an interrupting relative clause, three `that` uses, complements, conjunction/negator extras, repeated tile text, and multiple natural arrangements. Keys record 13 accepted arrangements; swapping indistinguishable tile IDs does not require enumerating further entries.

The 18 mechanical test methods exercise the public helper and CLI, including malformed inputs and the boundary between accounting and grammar. The helper reconstructs answers and checks tile accounting; it cannot validate English or certify uniqueness. A valid bank assignment absent from a reviewed key remains unresolved.

[Behavioral prompts](prompts.json) are executed against the skill and relevant references. They include direct answers, interactive and batch delivery, error explanations, key challenges, incomplete sources, optional records, and regression requests. Authored fixture keys are not behavioral test results. See [REPORT.md](REPORT.md) for actual runs, tested revision hashes, observed repairs, and remaining limits.
