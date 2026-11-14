# Small result tables

Recompute these tables with `python3 baseline.py summarize`. New CSVs go to `.local/summaries/`; the published files here stay unchanged. This uses saved outcomes and makes no model calls. Use `--output /path/to/output-folder` to choose another destination.

`python3 baseline.py verify` checks the recomputed values against the reference tables and verifies the published file checksums.

- [`overall.csv`](overall.csv): correct/answered accuracy, selected count, coverage, errors, and refusals.
- [`capabilities.csv`](capabilities.csv): the same accuracy and coverage breakdown for each capability.
- [`native_binary.csv`](native_binary.csv): confusion counts, precision, and recall on the 214 source-defined binary questions, including 15 with adapted choice representations.
- [`cost_timing.csv`](cost_timing.csv): saved timings and model inference charges excluding Vercel AI Gateway fees, with original charges and excluded fees retained for reconciliation. The shared GPU is recorded for self-hosted models. See [measurement definitions](../docs/methods.md#saved-costs-and-timings).

Accuracy is calculated over answered questions. Errors and refusals reduce coverage and are excluded from the binary confusion counts.


## Context-sensitivity comparisons

[Variant summaries](variants/README.md) report explicit before/after comparisons overall and by capability, with changed-answer counts and coverage.
