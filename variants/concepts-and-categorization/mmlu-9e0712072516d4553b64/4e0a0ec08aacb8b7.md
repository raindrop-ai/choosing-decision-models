# Option order · Move the first answer choice to the end variant

[Original question](../../../questions/concepts-and-categorization/mmlu-9e0712072516d4553b64.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> Jeanette locked the front door and then checked it by turning the knob. She checked it a second time. After walking halfway down the path to the street, Jeanette went back to the door and checked to make sure that it was locked. Her behavior appears to be

## Answer choices

- **B.** schizophrenic
- **C.** obsessive
- **D.** compulsive
- **A.** psychotic

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "Jeanette locked the front door and then checked it by turning the knob. She checked it a second time. After walking halfway down the path to the street, Jeanette went back to the door and checked to make sure that it was locked. Her behavior appears to be",
  "choices": {
    "B": "schizophrenic",
    "C": "obsessive",
    "D": "compulsive",
    "A": "psychotic"
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
| GLiNER2.5 Decide | `D` — compulsive | `B` — schizophrenic | Different answer |
| Laya | `A` — psychotic | `B` — schizophrenic | Different answer |
| CalDec v1 | `A` — psychotic | `A` — psychotic | Same answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mmlu/9e0712072516d4553b64/option_order/rotate_1`

**Input fingerprint:** `67b5ec7db90b0e2db69dc5b96e44a4d165ce7202783f779aebf8331128a4cca1`

| Change | Recorded version |
| --- | --- |
| Option order | Move the first answer choice to the end |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/concepts-and-categorization/mmlu-9e0712072516d4553b64.md).
