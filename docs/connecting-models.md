# Connect a model

You can use the study's recorded model connections, call a provider directly, or send questions to a model running on your own server. Vercel AI Gateway was the service used for the hosted models in the study; it is one supported connection, rather than a requirement for testing other models.

## What you need

An **API** is a way for this repository's Python client to send a question to a running model and receive an answer. Three details identify the connection:

- **Endpoint:** the full web address that accepts requests, such as `https://your-provider.example/v1/chat/completions`.
- **Model ID:** the exact model name your provider or server expects. This may differ from its display name.
- **API key:** a secret issued by the provider to authorize requests. A server running only on your own machine may not require one.

An **OpenAI-compatible** endpoint uses the same request and response format as a chat-completions API. It can be run by another provider or by your own software; using that format does not require an OpenAI account. This client also supports the Evaluation v4 and Decisions v1 choice formats used in the study. APIs using other formats, such as a provider-specific messages endpoint, need a separate adapter; select that provider’s OpenAI-compatible endpoint if it offers one. A provider must actually support the selected format; changing an endpoint cannot translate between unrelated APIs.

The commands below run from the repository root and require Python 3.10 or later. Creating a connection file and inspecting a request are offline steps. The `run_api.py` command sends requests to the configured endpoint.

## Use a provider directly

Copy the example into the ignored local folder:

```bash
mkdir -p .local
cp configs/examples/provider-model.json .local/provider-model.json
```

Open `.local/provider-model.json` in a text editor. Replace `endpoint` with the full chat-completions URL from your provider's API documentation and `model_id` with its exact model identifier. The complete file has this shape:

```json
{
  "format": "openai-chat",
  "endpoint": "https://your-provider.example/v1/chat/completions",
  "model_id": "your-provider-model-id",
  "auth": "bearer",
  "api_key_env": "MODEL_API_KEY",
  "structured_output": "json_schema",
  "request_parameters": {"max_tokens": 1024, "temperature": 0}
}
```

Get an API key from that provider's dashboard. The client prompts for it without echoing it when you run interactively. For scripts, supply it through the environment variable named in `api_key_env`, using your shell or secret manager. Put the variable's **name**, not the key itself, in the connection file. No Vercel key is used for this connection.

Inspect one complete request without sending it:

```bash
python3 evaluation/request_specs.py --model my-model \
  --connection .local/provider-model.json \
  --case bbh/639b88b1fe80634a7d66
```

Send that question:

```bash
python3 evaluation/run_api.py --model my-model \
  --connection .local/provider-model.json \
  --case bbh/639b88b1fe80634a7d66 \
  --output .local/api/my-model-example
```

Here, `my-model` is a name for your run. Use a new name rather than one of the recorded baseline aliases, so its results stay identifiable. The provider receives the `model_id` from the file, not this run name.

To send all 1,005 original questions, replace `--case …` with `--all --local-questions .local/questions.complete.jsonl` after [recovering the complete inputs](recovering-inputs.md). To send only a chosen set, use `--cases-file` as explained in the [reproduction guide](reproduction.md).

## Connect to your own model server

A model server is a program that loads a model and keeps it running so it can answer API requests. If you already have an OpenAI-compatible server, copy the local example:

```bash
cp configs/examples/local-model.json .local/local-model.json
```

Set its endpoint and model ID to the values advertised by your server. The example uses `http://127.0.0.1:8000/v1/chat/completions`; `127.0.0.1` means the same machine running the Python client, and `8000` is the server's port. Set `auth` to `none` only if the server does not require a key. Use HTTPS and authentication when connecting to a remote server.

Then run:

```bash
python3 evaluation/run_api.py --model my-local-model \
  --connection .local/local-model.json \
  --case bbh/639b88b1fe80634a7d66 \
  --output .local/api/my-local-example
```

If you need to create a server, [vLLM's server guide](https://docs.vllm.ai/en/stable/serving/openai_compatible_server/) explains its OpenAI-compatible interface, and its [Docker guide](https://docs.vllm.ai/en/stable/deployment/docker/) covers running it on a Linux GPU host. Choose a model and serving configuration supported by that software. The eight decision models in this study use their own model-specific Python implementations; the [included GPU setup](reproduction.md#run-the-self-hosted-models) runs those directly, without needing an API server.

## Choose the request and answer format

| Field | What to enter |
| --- | --- |
| `format` | `openai-chat` for chat completions, `evaluation-v4` for the study's choice-evaluation protocol, or `decisions-v1` for its Decisions protocol. |
| `endpoint` | The complete URL accepting that format, including its path. HTTPS is required except for a server on localhost. |
| `model_id` | The exact identifier your server expects and reports. |
| `auth` | `bearer`, `x-api-key` or `none`, according to the provider. |
| `api_key_env` | The name of the environment variable holding your key. The interactive prompt also works. |
| `structured_output` | For chat completions, use `json_schema` when supported, `json_object` for JSON mode, or `none` when the server relies on the prompt alone. |
| `request_parameters` | Chat-completions settings accepted by your server, such as `max_tokens`, `temperature` or `reasoning_effort`. They cannot replace the question, model or output schema. |
| `reported_model_aliases` | Optional exact alternative identifiers the server can return for the configured model. Unknown identities stop the run. |
| `comparison_model` | Optional recorded baseline alias to compare against when scoring, such as `glide` or `jev`. |

For a choice endpoint, its required protocol headers and body are built automatically. That does not mean a provider's similarly named product necessarily uses the same protocol; check its API documentation.

Every successful chat answer must be a JSON object such as `{"answer": "A"}`, using one of the supplied choice keys. The client validates that answer even when structured output is disabled. Choice-format responses must provide the native choice probabilities. Errors, invalid outputs and refusals remain recorded; they are not silently turned into guesses or retried.

## Score your model

```bash
python3 evaluation/score_fresh.py \
  --input .local/api/my-model-example/predictions.jsonl \
  --job .local/api/my-model-example/run.json \
  --compare-to glide \
  --output-dir .local/api/my-model-example/comparison
```

The scorer uses the same reference answers as the study. `--compare-to glide` compares GLiDE's saved answers on exactly the questions you selected with your model's answers. Omit it to score a new model without choosing a baseline comparison. A full-dataset score requires all 1,005 questions; a one-question test is reported as one question.

The connection settings, model identity and input hashes are saved with the run. Testing a new model or a different serving configuration is an additional comparison; it does not replace the study's recorded results.
