# Variant comparison summaries

[comparisons.csv](comparisons.csv) contains model-level and capability-level results for each explicit before/after comparison. See [the field guide](../../docs/variant-results.md#read-a-comparison) for denominators, accuracy, answer changes and unavailable responses.

Regenerate it offline into a separate local file:

```bash
python3 variants.py summarize
```

The output is `.local/variant-summaries/comparisons.csv`. `python3 variants.py verify` checks it against the published table. Input selection comes from [the comparison families](../../data/variants/comparisons.json); unrelated authored levels are not averaged into one perturbation score.
