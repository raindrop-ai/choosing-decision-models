# Irrelevant details · Add a larger amount of irrelevant detail variant

[Original question](../../../questions/retrieval/boolq-b24921a0b83f87972235.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> The musical suite Merovan includes a refrain. Merovan uses a tonic cadence. Merovan includes rests. Merovan has sustained harmonies. Merovan has detached melodic notes. Merovan varies its accompaniment.
>
> On April 18, 2018, CBS renewed the series for a ninth season. As of May 11, 2018, 177 episodes of Blue Bloods have aired, concluding the eighth season.

## Question

> was this the last season of blue bloods

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "The musical suite Merovan includes a refrain. Merovan uses a tonic cadence. Merovan includes rests. Merovan has sustained harmonies. Merovan has detached melodic notes. Merovan varies its accompaniment.\n\nOn April 18, 2018, CBS renewed the series for a ninth season. As of May 11, 2018, 177 episodes of Blue Bloods have aired, concluding the eighth season.",
  "question": "was this the last season of blue bloods",
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
| Strands Decider | `no` — No | `no` — No | Same answer |
| GLiNER2.5 Decide | `yes` — Yes | `yes` — Yes | Same answer |
| Laya | `no` — No | `no` — No | Same answer |
| CalDec v1 | `no` — No | `no` — No | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `boolq/b24921a0b83f87972235/irrelevant_details/high/clean-source_first_boolq_music_contexts_full_0164`

**Input fingerprint:** `ec7c99d019be000fa9ac05aa0b13701297efe0b6ca4923c745da7aa75d3d08df`

| Change | Recorded version |
| --- | --- |
| Irrelevant details | Add a larger amount of irrelevant detail |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/boolq-b24921a0b83f87972235.md).
