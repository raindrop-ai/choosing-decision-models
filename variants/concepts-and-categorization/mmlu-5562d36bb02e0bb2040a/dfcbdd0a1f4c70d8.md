# Extra events · Add 12 unrelated events variant

[Original question](../../../questions/concepts-and-categorization/mmlu-5562d36bb02e0bb2040a.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.
> Nolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue. Nolan classifies Kesil as an elegy. Nolan classifies Nereth as a satire. Nolan classifies Pavrel as a fable. Nolan classifies Sovrin as a ballad. Nolan reclassifies Virel as a monologue. Nolan reclassifies Zorven as a dialogue. Nolan reclassifies Kesil as a ballad. Nolan reclassifies Nereth as a fable. Nolan reclassifies Pavrel as a satire. Nolan reclassifies Sovrin as an elegy.

## Question

> For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? Scenario 1 | I watched the nurse grab a box of crackers and put them in her purse at work. Scenario 2 | I was due to start work soon, so I went there.

## Answer choices

- **A.** Wrong, Wrong
- **B.** Wrong, Not wrong
- **C.** Not wrong, Wrong
- **D.** Not wrong, Not wrong

**Reference answer:** `D`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.\nNolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue. Nolan classifies Kesil as an elegy. Nolan classifies Nereth as a satire. Nolan classifies Pavrel as a fable. Nolan classifies Sovrin as a ballad. Nolan reclassifies Virel as a monologue. Nolan reclassifies Zorven as a dialogue. Nolan reclassifies Kesil as a ballad. Nolan reclassifies Nereth as a fable. Nolan reclassifies Pavrel as a satire. Nolan reclassifies Sovrin as an elegy.",
  "question": "For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? Scenario 1 | I watched the nurse grab a box of crackers and put them in her purse at work. Scenario 2 | I was due to start work soon, so I went there.",
  "choices": {
    "A": "Wrong, Wrong",
    "B": "Wrong, Not wrong",
    "C": "Not wrong, Wrong",
    "D": "Not wrong, Not wrong"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `D` — Not wrong, Not wrong | `D` — Not wrong, Not wrong | Same answer |
| Decider v1.1 | `D` — Not wrong, Not wrong | `D` — Not wrong, Not wrong | Same answer |
| Jev | `D` — Not wrong, Not wrong | `D` — Not wrong, Not wrong | Same answer |
| Microsoft Decision-1 | `D` — Not wrong, Not wrong | `D` — Not wrong, Not wrong | Same answer |
| Clef | `D` — Not wrong, Not wrong | `B` — Wrong, Not wrong | Different answer |
| Luna Decisions | `D` — Not wrong, Not wrong | `D` — Not wrong, Not wrong | Same answer |
| Clef Flash | `D` — Not wrong, Not wrong | `D` — Not wrong, Not wrong | Same answer |
| Strands Decider | `B` — Wrong, Not wrong | `D` — Not wrong, Not wrong | Different answer |
| GLiNER2.5 Decide | `A` — Wrong, Wrong | `A` — Wrong, Wrong | Same answer |
| Laya | `A` — Wrong, Wrong | `A` — Wrong, Wrong | Same answer |
| CalDec v1 | `A` — Wrong, Wrong | `A` — Wrong, Wrong | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `mmlu/5562d36bb02e0bb2040a/event_count/12/clean-source_first_mmlu_other_short_contexts_full_0100`

**Input fingerprint:** `2f17394d7e59639ad680baa15a98b541d72ee84918b576b89fc57b937ed519a9`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 12 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/concepts-and-categorization/mmlu-5562d36bb02e0bb2040a.md).
