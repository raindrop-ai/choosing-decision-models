# Repetition · Present the same evidence twice variant

[Original question](../../../questions/concepts-and-categorization/mmlu-9e0712072516d4553b64.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> «Jeanette locked the front door and then checked it by turning the knob. She checked it a second time. After walking halfway down the path to the street, Jeanette went back to the door and checked to make sure that it was locked. Her behavior appears to be»

## Question

> Jeanette locked the front door and then checked it by turning the knob. She checked it a second time. After walking halfway down the path to the street, Jeanette went back to the door and checked to make sure that it was locked. Her behavior appears to be

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
  "state": "«Jeanette locked the front door and then checked it by turning the knob. She checked it a second time. After walking halfway down the path to the street, Jeanette went back to the door and checked to make sure that it was locked. Her behavior appears to be»",
  "question": "Jeanette locked the front door and then checked it by turning the knob. She checked it a second time. After walking halfway down the path to the street, Jeanette went back to the door and checked to make sure that it was locked. Her behavior appears to be",
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
| GLiNER2.5 Decide | `D` — compulsive | `A` — psychotic | Different answer |
| Laya | `A` — psychotic | `A` — psychotic | Same answer |
| CalDec v1 | `A` — psychotic | `C` — obsessive | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mmlu/9e0712072516d4553b64/evidence_repetition/2/clean-source_first_parallel_b_position_repetition_orders_0315`

**Input fingerprint:** `554815c4ee4bc1e70b672e97b133b8150314e805330ca6c464a97b7f0f166170`

| Change | Recorded version |
| --- | --- |
| Repetition | Present the same evidence twice |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/concepts-and-categorization/mmlu-9e0712072516d4553b64.md).
