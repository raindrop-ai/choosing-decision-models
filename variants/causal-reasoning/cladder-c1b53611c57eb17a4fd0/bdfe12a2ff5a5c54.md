# Extra events · Add 2 unrelated events variant

[Original question](../../../questions/causal-reasoning/cladder-c1b53611c57eb17a4fd0.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.
> Nolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue.
>
> Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Alice waking up has a direct effect on Alice arriving to school. Traffic has a direct effect on Alice arriving to school.
> We know that waking up late and heavy traffic causes arriving to school on time. We observed there is heavy traffic on the road.

## Question

> Would Alice arrives at school late if waking up late instead of waking up on time?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.\nNolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue.\n\nImagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Alice waking up has a direct effect on Alice arriving to school. Traffic has a direct effect on Alice arriving to school.\nWe know that waking up late and heavy traffic causes arriving to school on time. We observed there is heavy traffic on the road.",
  "question": "Would Alice arrives at school late if waking up late instead of waking up on time?",
  "choices": {
    "yes": "Yes",
    "no": "No"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `no` — No | `no` — No | Same answer |
| Decider v1.1 | `no` — No | `no` — No | Same answer |
| Jev | `no` — No | `no` — No | Same answer |
| Microsoft Decision-1 | `no` — No | `no` — No | Same answer |
| Clef | `no` — No | `no` — No | Same answer |
| Luna Decisions | `no` — No | `no` — No | Same answer |
| Clef Flash | `no` — No | `no` — No | Same answer |
| Strands Decider | `yes` — Yes | `yes` — Yes | Same answer |
| GLiNER2.5 Decide | `yes` — Yes | `yes` — Yes | Same answer |
| Laya | `no` — No | `no` — No | Same answer |
| CalDec v1 | `no` — No | `no` — No | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cladder/c1b53611c57eb17a4fd0/event_count/2/clean-source_first_cladder_short_contexts_full_0129`

**Input fingerprint:** `5192e2233b040f9540a4e22b6588732fb628ed526c7513857cf22de79773b780`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 2 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/causal-reasoning/cladder-c1b53611c57eb17a4fd0.md).
