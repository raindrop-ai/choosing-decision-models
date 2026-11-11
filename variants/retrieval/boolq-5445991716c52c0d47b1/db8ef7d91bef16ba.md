# Paraphrasing · Change the sentence structure variant

[Original question](../../../questions/retrieval/boolq-5445991716c52c0d47b1.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> King Louie is a fictional character introduced in Walt Disney's 1967 animated musical film, The Jungle Book. Unlike the majority of the adapted characters in the film, Louie was not featured in Rudyard Kipling's original works. King Louie was portrayed as an orangutan who was the leader of the other jungle primates, and who attempted to gain knowledge of fire from Mowgli, in order to become more human.

## Question

> In the book The Jungle Book, is King Louie a character?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "King Louie is a fictional character introduced in Walt Disney's 1967 animated musical film, The Jungle Book. Unlike the majority of the adapted characters in the film, Louie was not featured in Rudyard Kipling's original works. King Louie was portrayed as an orangutan who was the leader of the other jungle primates, and who attempted to gain knowledge of fire from Mowgli, in order to become more human.",
  "question": "In the book The Jungle Book, is King Louie a character?",
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
| GLiNER2.5 Decide | `no` — No | `no` — No | Same answer |
| Laya | `no` — No | `yes` — Yes | Different answer |
| CalDec v1 | `no` — No | `yes` — Yes | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `boolq/5445991716c52c0d47b1/paraphrasing/structural`

**Input fingerprint:** `7d2ee9dfd9b9032020c2f1badf7d24e7da26ed7ff3e6316399e963076d1fd697`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change the sentence structure |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/boolq-5445991716c52c0d47b1.md).
