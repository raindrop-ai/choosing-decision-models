# What these results measure

[Browse questions](../questions/README.md) · [Read results](results.md) · [Verify results](reproduction.md)

## The question set

The baseline contains **1,005 questions** sampled from public benchmarks, with **67 assigned to each of 15 capability areas**. The [question index](../questions/README.md) links to their sources, evaluated inputs and recorded model answers.

There are **802 native-choice** and **203 adapted-choice** inputs. The adaptations give free-response tasks answer choices that decision models can use. Released records preserve the complete evaluated context, question, answer descriptions and choice order. Adapted records also retain the source representation in [`data/questions.jsonl`](../data/questions.jsonl).

The experiment compares **11 decision models** with two general-purpose LLM baselines: **Astra** and **Opus 5.5**. Model identifiers, checkpoint revisions and runtime settings are in [`configs/`](../configs/README.md).

## Scoring

A prediction is correct when its answer-choice key matches the reference key. Accuracy is:

```text
correct successful answers / all successful answers
```

Errors and refusals are excluded from the accuracy denominator and reported in coverage. The result files contain an outcome for every one of the **13,065 question/model pairs**. Coverage is the number of answered questions divided by the number selected.

Capability scores use the same calculation within each area. With 67 questions per area, small leads describe this sample and need confirmation on fresh questions.

## Binary error analysis

The [binary subset](../questions/binary-subset.md) contains **214 questions** with two choices and an explicit positive label from the source. Fifteen use adapted answer choices.

A false alarm is a positive prediction when the reference answer is negative. A missed detection is a negative prediction when the reference answer is positive. Errors and refusals are excluded from these counts and reduce coverage.

```text
precision = true positives / (true positives + false positives)
recall    = true positives / (true positives + false negatives)
```

The [question manifest](../data/question_manifest.jsonl) records each source's positive label and its meaning. Precision and recall pool these source-defined labels across the subset.

## Inputs and model execution

API requests use `state`, `question` and ordered `choices`. Reference answers are excluded from the request. The two LLM baselines use the same system instruction, JSON-schema answer format, high reasoning effort and 8,192-token output limit. The [reproduction guide](reproduction.md) explains how to construct the requests.

Open-weight models use their native choice runtimes and pinned checkpoints. Inputs must include the full context and answer choices. Clef and Clef Flash's input processing fixes choice order, so their option-order results do not measure sensitivity to the reordered choices. Runtime code and dependency versions are documented in [`evaluation/`](../evaluation/README.md) and [`configs/`](../configs/README.md).

## Saved costs and timings

API request times run from client request preparation through response receipt, including network routing and provider processing.

All eight self-hosted models answered the same 1,005 questions on **one physical NVIDIA A100 80GB PCIe**, with two CPU cores, 64 GiB host memory, batch size one, seed zero and TF32 disabled. Each model ran in a fresh process with its pinned checkpoint and native runtime. Full settings are in [measurement conditions](../configs/measurement_conditions.json).

Self-hosted prediction times cover synchronized input encoding, the forward pass and probability extraction after model loading. They exclude downloads, model loading and network transport. Each model's first prediction is excluded from timing summaries because it includes kernel startup; it remains in the result files with `timing_included: false`, and its answer still counts toward accuracy. Timing summaries use the remaining **1,004 successful predictions** per model. The median is the middle measured time; p95 uses the nearest-rank 95th percentile.

API request times and GPU prediction times measure different portions of serving and should be interpreted accordingly.

API costs per 1,000 requests divide known reported charges by the number of requests with known prices; priced refusals are included and missing charges remain unknown.

The reported costs are hosted API charges. No per-prediction GPU cost is assigned.

## Context sensitivity

The context-sensitivity experiment examines whether answer-preserving changes to wording, framing and context affect model judgments. Each altered question is linked to its original and recorded condition. The [variant methods](variant-methods.md) explain the edits, exact comparison sets, response pairing and text recovery. Comparisons use the corresponding matched inputs; multiple versions of one original are related observations.
