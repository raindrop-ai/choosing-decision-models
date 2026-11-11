# Context-sensitivity results

[Browse variants](../variants/README.md) · [How they were made](variant-methods.md) · [Verify or rerun](variant-reproduction.md)

The study records answers from **11 decision models** on **24,563 altered versions of 1,005 original questions**. Results are organized by explicit comparisons, rather than an average over every kind of edit.

## Read a comparison

The [comparison table](../summaries/variants/comparisons.csv) contains one row per model, comparison and capability area, plus an `all` row over the included capabilities.

- `bases` is the number of original questions selected by the input design.
- `paired` is the number with successful answers to all inputs required for that comparison. `unavailable` is the difference.
- `before_correct` and `after_correct` count correct answers over that same valid set.
- `delta_pp` is the after accuracy minus the before accuracy, in percentage points.
- `changed` counts different answer keys, including wrong-to-different-wrong changes.
- `lost` is correct-to-wrong; `gained` is wrong-to-correct. Their difference accounts for the change in accuracy.
- `any_changed` counts questions with different answers anywhere across the required set. For position, that is across beginning, middle and end; for ordering, it includes original, reversed and shuffled evidence.
- `normalized` marks choice-order comparisons where Clef's input processing fixes the order before inference.

Accuracy fields are fractions from 0 to 1. Change fields ending in `_pct` are percentages; `delta_pp` is a percentage-point difference. Every row's label identifies its before and after versions. The [methods](variant-methods.md#which-versions-are-compared) explain the exact cohorts and their sizes.

## Examples worth inspecting

Stable accuracy can hide different judgments. On the 335-question ordering comparison, Clef Flash answered 235 correctly both in the original and reversed versions, while changing 47 individual answers: 17 correct-to-wrong, 17 wrong-to-correct and 13 wrong-to-different-wrong.

Across the 944 matched beginning/middle/end questions, Laya changed its answer somewhere across the three versions on 422 questions; GLiDE did so on 57. These are changes in judgment, rather than necessarily declines in accuracy.

Added assessments affected both stronger and weaker models. On the 1,004-question matched assessment set, GLiDE answered 953 originals correctly, 978 with an accurate assessment and 880 with a misleading one. Jev's corresponding counts were 891, 946 and 816. GLiNER2.5 Decide's accuracy moved from 42.7% on originals to 78.7% with accurate assessments and 18.3% with misleading ones. These original counts belong to the linked controls for this comparison, not necessarily the original 1,005-question baseline table.

Each [variant page](../variants/README.md) shows the original control answer and altered-input answer for every model. The exact comparison lists link the variants used in the aggregate statistics.

## Files to explore

| File | Contents |
| --- | --- |
| [Comparison summaries](../summaries/variants/comparisons.csv) | Overall and capability-level comparisons, including answer changes and coverage. |
| [Comparison sets](../data/variants/comparisons.json) | Exact original/variant membership at every compared level. |
| [Variant manifest](../data/variants/manifest.jsonl) | Input IDs, original links, reference keys, sharing status and page locations. |
| [Recorded answers](../results/variants/README.md) | One JSONL file per model, with exact original-control links. |
| [Study configuration](../configs/variant-study.json) | Model configurations, inventory sizes and coverage. |

## Verify the calculations

From a terminal in the repository root, with Python 3.10 or later:

```bash
python3 variants.py verify
python3 variants.py summarize
```

No model downloads, API keys or dataset recovery are required to check the saved scores. New summaries go to `.local/variant-summaries/comparisons.csv`, leaving the published values unchanged. The [fresh-run comparison command](variant-reproduction.md#compare-fresh-original-and-variant-answers) calculates the same contrasts from your own original and variant outputs.
