# Baseline data

[Browse questions](../questions/README.md) · [Sharing decisions](../docs/data-sharing.md)

| File | Contents |
| --- | --- |
| [`question_manifest.jsonl`](question_manifest.jsonl) | One metadata row for each of all 1,005 questions. Includes capability, source locator, ordered choice keys, reference choice, input hash, and sharing status. Contains no question/context/answer-description text. |
| [`binary_subset.csv`](binary_subset.csv) | The exact 214 question IDs used for binary error analysis, with capability, source, positive and reference choice keys, and links to their reading pages. |
| [`questions.jsonl`](questions.jsonl) | Full evaluated inputs for questions whose text is included in the collection, with attribution, per-source terms, and choice-format provenance. |
| [`sharing_decisions.csv`](sharing_decisions.csv) | A readable, per-question record of what is included or held, and why. |
| [`sources.json`](sources.json) | Original-source URLs, revisions, download hashes, checked notice evidence, and source-level decisions. |

Match each question’s `id` to `case_id` in the result files. `gold_choice` in the manifest and `gold` in a full input are the reference answer key; `prediction` is the model’s chosen key.

JSONL means one JSON object per line. Keep `choices` in their recorded insertion order: the input hash includes that order. Do not sort answer choices before making a request.

Recovered question text stays in the ignored `.local/` folder and is not added to Git. Omission of source text from the shared files does not remove those questions or their outcomes from scoring.

For adapted inputs, `native_before_formatting` preserves the source representation alongside the exact multiple-choice representation used for evaluation. That field is present only when the source text is included.

[`source_attributions.json`](source_attributions.json) records per-question Wikipedia attribution, OANC credits, BIG-bench source matches and component terms.

## Separately recovered inputs

The 148 question texts obtained separately have a [recovery guide](../docs/recovering-inputs.md). Their source identifiers, input fingerprints, answer keys and saved results are included.

To inspect recovered text and the saved answers together, run:

```bash
python3 baseline.py inspect --case QUESTION_ID \
  --local-questions .local/questions.complete.jsonl
```

Use the actual question ID and a file containing that question. The command validates the input before displaying it.

## Question variants

The [variant data](variants/README.md) contain altered inputs, their original-question links, recovery recipes and exact comparison sets. [Browse their readable pages](../variants/README.md).
