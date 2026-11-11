# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/state-tracking-and-updating/babi-2f265669fdfd296e8814.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Sandra travelled to the office.
> Sandra travelled to the bathroom.
>
> Uppercase: comet → COMET.

## Question

> Where is Sandra? 

## Answer choices

- **A.** hallway
- **B.** office
- **C.** bedroom
- **D.** garden
- **E.** kitchen
- **F.** bathroom

**Reference answer:** `F`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Sandra travelled to the office.\nSandra travelled to the bathroom.\n\nUppercase: comet → COMET.",
  "question": "Where is Sandra? ",
  "choices": {
    "A": "hallway",
    "B": "office",
    "C": "bedroom",
    "D": "garden",
    "E": "kitchen",
    "F": "bathroom"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `F` — bathroom | `F` — bathroom | Same answer |
| Decider v1.1 | `F` — bathroom | `F` — bathroom | Same answer |
| Jev | `F` — bathroom | `F` — bathroom | Same answer |
| Microsoft Decision-1 | `F` — bathroom | `F` — bathroom | Same answer |
| Clef | `F` — bathroom | `F` — bathroom | Same answer |
| Luna Decisions | `F` — bathroom | `F` — bathroom | Same answer |
| Clef Flash | `F` — bathroom | `F` — bathroom | Same answer |
| Strands Decider | `F` — bathroom | `F` — bathroom | Same answer |
| GLiNER2.5 Decide | `F` — bathroom | `F` — bathroom | Same answer |
| Laya | `B` — office | `F` — bathroom | Different answer |
| CalDec v1 | `F` — bathroom | `F` — bathroom | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/2f265669fdfd296e8814/examples/irrelevant/clean-source_first_babi_qa1_full_0084`

**Input fingerprint:** `f965d75bb24b121687252c64687226cc2f1f3113780875dbcbace8b0520be34d`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/babi-2f265669fdfd296e8814.md).
