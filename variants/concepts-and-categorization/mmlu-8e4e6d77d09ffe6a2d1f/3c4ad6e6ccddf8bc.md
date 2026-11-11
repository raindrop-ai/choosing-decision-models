# Option order · Reverse the answer choices variant

[Original question](../../../questions/concepts-and-categorization/mmlu-8e4e6d77d09ffe6a2d1f.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Question

> All of the following are modes of asexual reproduction EXCEPT

## Answer choices

- **D.** meiosis
- **C.** budding
- **B.** fission
- **A.** sporulation

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "",
  "question": "All of the following are modes of asexual reproduction EXCEPT",
  "choices": {
    "D": "meiosis",
    "C": "budding",
    "B": "fission",
    "A": "sporulation"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `D` — meiosis | `D` — meiosis | Same answer |
| Decider v1.1 | `D` — meiosis | `D` — meiosis | Same answer |
| Jev | `D` — meiosis | `D` — meiosis | Same answer |
| Microsoft Decision-1 | `D` — meiosis | `D` — meiosis | Same answer |
| Clef | `D` — meiosis | `D` — meiosis | Same answer |
| Luna Decisions | `D` — meiosis | `D` — meiosis | Same answer |
| Clef Flash | `D` — meiosis | `D` — meiosis | Same answer |
| Strands Decider | `D` — meiosis | `D` — meiosis | Same answer |
| GLiNER2.5 Decide | `A` — sporulation | `D` — meiosis | Different answer |
| Laya | `B` — fission | `C` — budding | Different answer |
| CalDec v1 | `D` — meiosis | `C` — budding | Different answer |

Clef and Clef Flash sort answer choices in their published input-processing code. Their choice-order results describe that preprocessing.

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mmlu/8e4e6d77d09ffe6a2d1f/option_order/reverse`

**Input fingerprint:** `bcc678f9eaa67320c637a12a881e1b112f6e2cf8830e5824e975eef806d363bc`

| Change | Recorded version |
| --- | --- |
| Option order | Reverse the answer choices |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/concepts-and-categorization/mmlu-8e4e6d77d09ffe6a2d1f.md).
