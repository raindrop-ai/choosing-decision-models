# Unrelated examples · Add examples unrelated to the question variant

[Original question](../../../questions/spatial-cognition/spartqa-410361100e9bfd27460e.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Capitalization: harbor → Harbor
>
> We have two blocks, A and B. Three medium yellow squares are in block A. Medium yellow square number one is below medium yellow square number three and medium yellow square number two. Below medium yellow square number three there is medium yellow square number two. Block B is to the right of block A. It has a medium blue square. The medium blue square is touching the bottom edge of this block. This block also has a medium black square. The medium blue square is below the medium black square.

## Question

> What is to the left of the black thing? a medium yellow square or a blue object that is touching the bottom edge of a block?

## Answer choices

- **0.** medium yellow square 
- **1.** blue object that is touching the bottom edge of a block 
- **2.** both of them
- **3.** none of them

**Reference answer:** `0`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Capitalization: harbor → Harbor\n\nWe have two blocks, A and B. Three medium yellow squares are in block A. Medium yellow square number one is below medium yellow square number three and medium yellow square number two. Below medium yellow square number three there is medium yellow square number two. Block B is to the right of block A. It has a medium blue square. The medium blue square is touching the bottom edge of this block. This block also has a medium black square. The medium blue square is below the medium black square.",
  "question": "What is to the left of the black thing? a medium yellow square or a blue object that is touching the bottom edge of a block?",
  "choices": {
    "0": "medium yellow square ",
    "1": "blue object that is touching the bottom edge of a block ",
    "2": "both of them",
    "3": "none of them"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `0` — medium yellow square  | `0` — medium yellow square  | Same answer |
| Decider v1.1 | `0` — medium yellow square  | `0` — medium yellow square  | Same answer |
| Jev | `1` — blue object that is touching the bottom edge of a block  | `1` — blue object that is touching the bottom edge of a block  | Same answer |
| Microsoft Decision-1 | `0` — medium yellow square  | `0` — medium yellow square  | Same answer |
| Clef | `2` — both of them | `0` — medium yellow square  | Different answer |
| Luna Decisions | `0` — medium yellow square  | `1` — blue object that is touching the bottom edge of a block  | Different answer |
| Clef Flash | `0` — medium yellow square  | `3` — none of them | Different answer |
| Strands Decider | `0` — medium yellow square  | `0` — medium yellow square  | Same answer |
| GLiNER2.5 Decide | `2` — both of them | `2` — both of them | Same answer |
| Laya | `2` — both of them | `2` — both of them | Same answer |
| CalDec v1 | `1` — blue object that is touching the bottom edge of a block  | `1` — blue object that is touching the bottom edge of a block  | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/410361100e9bfd27460e/examples/irrelevant/clean-source_first_spartqa_short_contexts_full_0136`

**Input fingerprint:** `50f35f33af0b595dd831e4dac29578e6a929fbb64da56d78a06867a5db1b74e2`

| Change | Recorded version |
| --- | --- |
| Unrelated examples | Add examples unrelated to the question |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-410361100e9bfd27460e.md).
