# Evaluation reference

- [`request_specs.py`](request_specs.py) builds the exact API request shapes and native worker jobs **without sending or executing them**.
- [`run_api.py`](run_api.py) connects to the recorded Gateway models or a provider/model endpoint you configure, and saves fresh responses.
- [`connections.py`](connections.py) reads provider connection settings without reading credentials or making requests.
- [`prepare_native.py`](prepare_native.py) prepares the all-model download specification and validated GPU jobs offline.
- [`score_variants.py`](score_variants.py) compares fresh original and altered inputs using the exact manipulation sets.
- [`score_fresh.py`](score_fresh.py) scores fresh API answers or GPU worker receipts against the selected questions.
- [`reference/worker_entry.py`](reference/worker_entry.py) is the entrypoint for the native GPU worker package. Run it in an isolated Linux CUDA container.
- [`reference/provenance.json`](reference/provenance.json) records the copied source hashes and worker revision.
- The pinned dependency files are under [`workers/`](../workers/).
- [`workers/Dockerfile`](../workers/Dockerfile) builds the core and large-model environments from those dependency files.

For ordinary verification, use `python3 baseline.py verify`; no evaluation environment is needed. See [reproduction instructions](../docs/reproduction.md) for setup and fresh-run commands.

To use a provider directly or run another model, follow [Connect a model](../docs/connecting-models.md). Its example connection files describe the endpoint, request format and model ID; API keys are supplied separately.

Both fresh-run clients accept `--case`, `--all` or `--cases-file`. Use `data/binary_subset.csv` to select the 214-question subset, or an available-input JSONL to select only questions whose text you have. All selected inputs are validated before execution.

The scorer compares fresh answers with the saved baseline over the same selected IDs. Add `--output-dir .local/comparison` to save its report and a CSV of changed answers or statuses. It does not update the reference results.

