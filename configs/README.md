# Model and runtime configurations

- [`models.json`](models.json): the 13 model names, serving setups, configured API identifiers or pinned weight revisions, and the actual GPU type used for the selected worker timings.
- [`result_configurations.json`](result_configurations.json): configurations linked from individual saved results. Use these for exact provenance rather than assuming a model's current default settings.
- [`worker_sources.json`](worker_sources.json): model artifact paths and loader checksums for the native worker.
- [`worker_environment.json`](worker_environment.json): dependency-file paths, GPU types, isolated execution conditions, and versioned compiler packages.
- [`native_input_audits.json`](native_input_audits.json): token counts and encoding hashes for checking Decider and GLiDE input encodings.

API identifiers can be aliases. Weight revisions are pinned Git commits. See [methods](../docs/methods.md) before interpreting the saved timings or attempting fresh inference.

[`measurement_conditions.json`](measurement_conditions.json) records the shared physical GPU verification, resource settings, runtime versions, first-forward exclusion, API cost definitions, and measurement-provenance hashes.

[`recovery_provenance.json`](recovery_provenance.json) identifies the experiment code used for deterministic reconstruction of held inputs.

The [hosted-model setup table](../docs/reproduction.md#connect-the-hosted-models) maps model names to command aliases and Gateway IDs. The [self-hosted setup table](../docs/reproduction.md#2-build-the-two-pinned-environments) maps each native model to its dependency environment.

[`examples/local-model.json`](examples/local-model.json) and [`examples/provider-model.json`](examples/provider-model.json) are starting points for your own connections. Copy them into `.local/` and follow [Connect a model](../docs/connecting-models.md); they contain no credentials and do not alter the study's configurations.

## Variant study

[variant-study.json](variant-study.json) records the altered-input inventory, model configurations and coverage. [variant-labels.json](variant-labels.json) supplies readable condition names. Exact comparison input lists live in [comparisons.json](../data/variants/comparisons.json).
