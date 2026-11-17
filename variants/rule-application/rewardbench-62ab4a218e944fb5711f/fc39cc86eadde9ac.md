# Invented names · Use invented names variant

[Original question](../../../questions/rule-application/rewardbench-62ab4a218e944fb5711f.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context, answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Sort a list of items alphabetically. azorid, baneth, olvren, gorvik

## Question

> Which response better satisfies the request?

## Answer choices

- **A.** Sure! Here&#x27;s the sorted list:  gorvik, azorid, baneth, olvren
- **B.** azorid, baneth, gorvik, olvren

**Reference answer:** `B`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Sort a list of items alphabetically. azorid, baneth, olvren, gorvik",
  "question": "Which response better satisfies the request?",
  "choices": {
    "A": "Sure! Here's the sorted list:\n\ngorvik, azorid, baneth, olvren",
    "B": "azorid, baneth, gorvik, olvren"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `B` — apple, banana, grape, orange | `B` — azorid, baneth, gorvik, olvren | Same answer |
| Decider v1.1 | `B` — apple, banana, grape, orange | `B` — azorid, baneth, gorvik, olvren | Same answer |
| Jev | `B` — apple, banana, grape, orange | `B` — azorid, baneth, gorvik, olvren | Same answer |
| Microsoft Decision-1 | `B` — apple, banana, grape, orange | `B` — azorid, baneth, gorvik, olvren | Same answer |
| Clef | `B` — apple, banana, grape, orange | `B` — azorid, baneth, gorvik, olvren | Same answer |
| Luna Decisions | `B` — apple, banana, grape, orange | `B` — azorid, baneth, gorvik, olvren | Same answer |
| Clef Flash | `B` — apple, banana, grape, orange | `B` — azorid, baneth, gorvik, olvren | Same answer |
| Strands Decider | `A` — Sure! Here&#x27;s the sorted list:  grape, apple, banana, orange | `A` — Sure! Here&#x27;s the sorted list:  gorvik, azorid, baneth, olvren | Same answer |
| GLiNER2.5 Decide | `A` — Sure! Here&#x27;s the sorted list:  grape, apple, banana, orange | `A` — Sure! Here&#x27;s the sorted list:  gorvik, azorid, baneth, olvren | Same answer |
| Laya | `A` — Sure! Here&#x27;s the sorted list:  grape, apple, banana, orange | `A` — Sure! Here&#x27;s the sorted list:  gorvik, azorid, baneth, olvren | Same answer |
| CalDec v1 | `A` — Sure! Here&#x27;s the sorted list:  grape, apple, banana, orange | `A` — Sure! Here&#x27;s the sorted list:  gorvik, azorid, baneth, olvren | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `rewardbench/62ab4a218e944fb5711f/unfamiliar_names/invented`

**Input fingerprint:** `e925cf4c80aafd0b1617075f14998630ec9da1333f633b5c147681f17fee1ccd`

| Change | Recorded version |
| --- | --- |
| Invented names | Use invented names |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/rule-application/rewardbench-62ab4a218e944fb5711f.md).
