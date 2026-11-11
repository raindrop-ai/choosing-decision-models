# Variant inputs and comparison sets

[Browse readable pages](../../variants/README.md) · [Methods](../../docs/variant-methods.md) · [Recover inputs](../../docs/variant-reproduction.md#recover-the-remaining-variant-texts)

| File | Contents |
| --- | --- |
| [manifest.jsonl](manifest.jsonl) | One row per distinct variant, with original ID, capability, reference key, ordered choice keys, supported models, changed fields, sharing status, fingerprint and reading page. |
| [conditions.jsonl](conditions.jsonl) | Logical factor/level memberships and their representative evaluated input IDs. Several memberships can refer to the same input. |
| [comparisons.json](comparisons.json) | Exact comparison families, required levels, before/after contrasts and source construction strata. |
| `inputs/<capability>.jsonl` | Full evaluated inputs for the 20,961 shareable variants, split by capability. |
| [recovery-recipes.jsonl](recovery-recipes.jsonl) | Authored edits and original-text span references for reconstructing the remaining 3,602 variants from locally obtained source questions. |

JSONL means one JSON object per line. Choice order matters to the input fingerprint. `gold_choice` is the reference answer key, not a model output. Full inputs use `gold` for the same key.

`common_input_fit` marks inputs fitting all eleven recorded models. `supported_models` records the input-fit eligibility of each individual variant. This eligibility is determined from the complete inputs, not from whether predictions were correct.

`ordering_roles` distinguishes full-evidence permutations from local or coupled edits using the construction audit. The main ordering comparison uses the explicit original/reversed/shuffled families, not every input carrying an ordering label.
