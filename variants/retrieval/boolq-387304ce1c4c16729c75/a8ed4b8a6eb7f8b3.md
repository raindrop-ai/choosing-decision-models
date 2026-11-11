# Paraphrasing · Change the sentence structure variant

[Original question](../../../questions/retrieval/boolq-387304ce1c4c16729c75.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Administrative leave is a temporary leave from a job assignment, with pay and benefits intact. Generally, the term is reserved for employees of non-business institutions such as schools, police, and hospitals.

## Question

> While you are on administrative leave, do you receive pay?

## Answer choices

- **yes.** Yes
- **no.** No

**Reference answer:** `yes`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Administrative leave is a temporary leave from a job assignment, with pay and benefits intact. Generally, the term is reserved for employees of non-business institutions such as schools, police, and hospitals.",
  "question": "While you are on administrative leave, do you receive pay?",
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
| GLiDE v1.2 | `yes` — Yes | `yes` — Yes | Same answer |
| Decider v1.1 | `yes` — Yes | `yes` — Yes | Same answer |
| Jev | `yes` — Yes | `yes` — Yes | Same answer |
| Microsoft Decision-1 | `yes` — Yes | `yes` — Yes | Same answer |
| Clef | `yes` — Yes | `yes` — Yes | Same answer |
| Luna Decisions | `yes` — Yes | `yes` — Yes | Same answer |
| Clef Flash | `yes` — Yes | `yes` — Yes | Same answer |
| Strands Decider | `yes` — Yes | `yes` — Yes | Same answer |
| GLiNER2.5 Decide | `yes` — Yes | `yes` — Yes | Same answer |
| Laya | `yes` — Yes | `yes` — Yes | Same answer |
| CalDec v1 | `yes` — Yes | `yes` — Yes | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `boolq/387304ce1c4c16729c75/paraphrasing/structural`

**Input fingerprint:** `0c4851028907d8aa83efba7f413156f9b79b3929b787e60baeb48f6e69a6d452`

| Change | Recorded version |
| --- | --- |
| Paraphrasing | Change the sentence structure |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/retrieval/boolq-387304ce1c4c16729c75.md).
