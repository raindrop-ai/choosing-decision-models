# Extra events · Add 6 unrelated events variant

[Original question](../../../questions/uncertainty-monitoring/boolq-2a504c33bb7af95e1320.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Merovan is a fictional musical suite with a refrain. The refrain begins on the tonic. The refrain pauses. The refrain resumes on a dominant tone. The refrain changes to detached articulation. The refrain returns to the tonic. The refrain repeats its final interval.
>
> The Peacock Throne was a famous jeweled throne that was the seat of the Mughal emperors of India. It was commissioned in the early 17th century by emperor Shah Jahan and was located in the Diwan-i-Khas (Hall of Private Audiences) in the Red Fort of Delhi. The original throne was subsequently captured and taken as a war trophy in 1739 by the Persian emperor Nadir Shah, and has been lost since. A replacement throne based on the original was commissioned afterwards and existed until the Indian Rebellion of 1857.

## Question

> do you know the place where the peacock throne is now

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Merovan is a fictional musical suite with a refrain. The refrain begins on the tonic. The refrain pauses. The refrain resumes on a dominant tone. The refrain changes to detached articulation. The refrain returns to the tonic. The refrain repeats its final interval.\n\nThe Peacock Throne was a famous jeweled throne that was the seat of the Mughal emperors of India. It was commissioned in the early 17th century by emperor Shah Jahan and was located in the Diwan-i-Khas (Hall of Private Audiences) in the Red Fort of Delhi. The original throne was subsequently captured and taken as a war trophy in 1739 by the Persian emperor Nadir Shah, and has been lost since. A replacement throne based on the original was commissioned afterwards and existed until the Indian Rebellion of 1857.",
  "question": "do you know the place where the peacock throne is now",
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
| Luna Decisions | `yes` — Yes | `yes` — Yes | Same answer |
| Clef Flash | `no` — No | `no` — No | Same answer |
| Strands Decider | `no` — No | `no` — No | Same answer |
| GLiNER2.5 Decide | `yes` — Yes | `yes` — Yes | Same answer |
| Laya | `no` — No | `yes` — Yes | Different answer |
| CalDec v1 | `no` — No | `no` — No | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `boolq/2a504c33bb7af95e1320/event_count/6/clean-source_first_boolq_music_contexts_full_0164`

**Input fingerprint:** `cc092ddf92b68db18ddd1514750a646a81f7f7b8742f1120add6541a61381a25`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 6 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/uncertainty-monitoring/boolq-2a504c33bb7af95e1320.md).
