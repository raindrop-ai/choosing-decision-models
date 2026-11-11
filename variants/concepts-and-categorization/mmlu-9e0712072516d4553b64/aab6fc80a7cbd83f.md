# Evidence order · Present the evidence in reverse order variant

[Original question](../../../questions/concepts-and-categorization/mmlu-9e0712072516d4553b64.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> After walking halfway down the path to the street, Jeanette went back to the door and checked to make sure that it was locked.
> Before that, She checked it a second time.
> Before that, Jeanette locked the front door and then checked it by turning the knob. Her behavior appears to be

## Answer choices

- **A.** psychotic
- **B.** schizophrenic
- **C.** obsessive
- **D.** compulsive

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "After walking halfway down the path to the street, Jeanette went back to the door and checked to make sure that it was locked.\nBefore that, She checked it a second time.\nBefore that, Jeanette locked the front door and then checked it by turning the knob. Her behavior appears to be",
  "choices": {
    "A": "psychotic",
    "B": "schizophrenic",
    "C": "obsessive",
    "D": "compulsive"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `D` — compulsive | `D` — compulsive | Same answer |
| Decider v1.1 | `D` — compulsive | `D` — compulsive | Same answer |
| Jev | `D` — compulsive | `D` — compulsive | Same answer |
| Microsoft Decision-1 | `D` — compulsive | `D` — compulsive | Same answer |
| Clef | `D` — compulsive | `D` — compulsive | Same answer |
| Luna Decisions | `D` — compulsive | `D` — compulsive | Same answer |
| Clef Flash | `D` — compulsive | `D` — compulsive | Same answer |
| Strands Decider | `D` — compulsive | `D` — compulsive | Same answer |
| GLiNER2.5 Decide | `D` — compulsive | `D` — compulsive | Same answer |
| Laya | `A` — psychotic | `A` — psychotic | Same answer |
| CalDec v1 | `A` — psychotic | `A` — psychotic | Same answer |

**Ordering comparison:** coupled wording reference chronology or representation. Only the exact matched comparison sets contribute to the reported ordering contrasts.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mmlu/9e0712072516d4553b64/presentation_order/reverse_presentation/clean-source_first_parallel_b_mmlu_reference_orders_0393`

**Input fingerprint:** `1b549452e6470d1ba9355c6b4578efa84495bef07bcb4b34f6dc6df839ddc14a`

| Change | Recorded version |
| --- | --- |
| Evidence order | Present the evidence in reverse order |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/concepts-and-categorization/mmlu-9e0712072516d4553b64.md).
