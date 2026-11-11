# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/state-tracking-and-updating/babi-2c8f31be4745073a29a6.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Daniel went to the office.
> John travelled to the kitchen.
> Mary journeyed to the bedroom.
> John picked up the apple there.
> John put down the apple.
> Sandra travelled to the office.
> Sandra went to the bathroom.
> Daniel grabbed the milk there.
> John journeyed to the office.
> John travelled to the bedroom.
> Daniel left the milk.
> Daniel grabbed the milk there.
> John moved to the garden.
> Daniel moved to the kitchen.
> Virelan went to the bathroom.
> Virelan picked up the flute.

## Question

> Where is the milk? 

## Answer choices

- **A.** hallway
- **B.** bathroom
- **C.** kitchen
- **D.** office
- **E.** garden
- **F.** bedroom

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Daniel went to the office.\nJohn travelled to the kitchen.\nMary journeyed to the bedroom.\nJohn picked up the apple there.\nJohn put down the apple.\nSandra travelled to the office.\nSandra went to the bathroom.\nDaniel grabbed the milk there.\nJohn journeyed to the office.\nJohn travelled to the bedroom.\nDaniel left the milk.\nDaniel grabbed the milk there.\nJohn moved to the garden.\nDaniel moved to the kitchen.\nVirelan went to the bathroom.\nVirelan picked up the flute.",
  "question": "Where is the milk? ",
  "choices": {
    "A": "hallway",
    "B": "bathroom",
    "C": "kitchen",
    "D": "office",
    "E": "garden",
    "F": "bedroom"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — kitchen | `C` — kitchen | Same answer |
| Decider v1.1 | `C` — kitchen | `C` — kitchen | Same answer |
| Jev | `C` — kitchen | `C` — kitchen | Same answer |
| Microsoft Decision-1 | `C` — kitchen | `C` — kitchen | Same answer |
| Clef | `C` — kitchen | `C` — kitchen | Same answer |
| Luna Decisions | `C` — kitchen | `C` — kitchen | Same answer |
| Clef Flash | `C` — kitchen | `C` — kitchen | Same answer |
| Strands Decider | `C` — kitchen | `C` — kitchen | Same answer |
| GLiNER2.5 Decide | `C` — kitchen | `D` — office | Different answer |
| Laya | `D` — office | `D` — office | Same answer |
| CalDec v1 | `C` — kitchen | `B` — bathroom | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `babi/2c8f31be4745073a29a6/similar_distractors/low/clean-source_first_qa2_new_distractors_full_0156`

**Input fingerprint:** `cdc1bb1847b1538484b528afa09519f7209e0556a1971074715b450c5210a52e`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/state-tracking-and-updating/babi-2c8f31be4745073a29a6.md).
