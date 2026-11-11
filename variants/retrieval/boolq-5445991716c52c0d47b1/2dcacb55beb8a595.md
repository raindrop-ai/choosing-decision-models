# Invented names · Use invented names variant

[Original question](../../../questions/retrieval/boolq-5445991716c52c0d47b1.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context, question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> King Zevran is a fictional character introduced in Walt Disney's 1967 animated musical film, The Jungle Book. Unlike the majority of the adapted characters in the film, Zevran was not featured in Rudyard Kipling's original works. King Zevran was portrayed as an orangutan who was the leader of the other jungle primates, and who attempted to gain knowledge of fire from Mowgli, in order to become more human.

## Question

> is king zevran in the jungle book book

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `no`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "King Zevran is a fictional character introduced in Walt Disney's 1967 animated musical film, The Jungle Book. Unlike the majority of the adapted characters in the film, Zevran was not featured in Rudyard Kipling's original works. King Zevran was portrayed as an orangutan who was the leader of the other jungle primates, and who attempted to gain knowledge of fire from Mowgli, in order to become more human.",
  "question": "is king zevran in the jungle book book",
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
| Microsoft Decision-1 | `no` — No | `yes` — Yes | Different answer |
| Clef | `no` — No | `no` — No | Same answer |
| Luna Decisions | `no` — No | `no` — No | Same answer |
| Clef Flash | `no` — No | `no` — No | Same answer |
| Strands Decider | `no` — No | `no` — No | Same answer |
| GLiNER2.5 Decide | `no` — No | `no` — No | Same answer |
| Laya | `no` — No | `no` — No | Same answer |
| CalDec v1 | `no` — No | `no` — No | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `boolq/5445991716c52c0d47b1/unfamiliar_names/invented`

**Input fingerprint:** `819e86e636989156dff970b49660232332fa94e763f9a099a67cba2f367be580`

| Change | Recorded version |
| --- | --- |
| Invented names | Use invented names |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/boolq-5445991716c52c0d47b1.md).
