# Invented names · Use invented names variant

[Original question](../../../questions/rule-application/cruxeval-dac9a78a4a34555b5ff0.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context, question instructions.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

```text
def varkel (tovrin ):
    tovrin =tovrin .upper ()
    nelarik =0 
    for zorven in tovrin :
        if zorven .isupper ():
            nelarik +=1 
        else :
            return 'no'
    return nelarik //2 
```

## Question

> What does varkel('ax') return?

## Answer choices

- **A.** 1
- **B.** 0
- **C.** -1
- **D.** 3

**Reference answer:** `A`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "def varkel (tovrin ):\n    tovrin =tovrin .upper ()\n    nelarik =0 \n    for zorven in tovrin :\n        if zorven .isupper ():\n            nelarik +=1 \n        else :\n            return 'no'\n    return nelarik //2 ",
  "question": "What does varkel('ax') return?",
  "choices": {
    "A": "1",
    "B": "0",
    "C": "-1",
    "D": "3"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `A` — 1 | `A` — 1 | Same answer |
| Decider v1.1 | `B` — 0 | `B` — 0 | Same answer |
| Jev | `A` — 1 | `A` — 1 | Same answer |
| Microsoft Decision-1 | `B` — 0 | `B` — 0 | Same answer |
| Clef | `B` — 0 | `A` — 1 | Different answer |
| Luna Decisions | `B` — 0 | `B` — 0 | Same answer |
| Clef Flash | `B` — 0 | `A` — 1 | Different answer |
| Strands Decider | `B` — 0 | `B` — 0 | Same answer |
| GLiNER2.5 Decide | `A` — 1 | `A` — 1 | Same answer |
| Laya | `A` — 1 | `A` — 1 | Same answer |
| CalDec v1 | `A` — 1 | `A` — 1 | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `cruxeval/dac9a78a4a34555b5ff0/unfamiliar_names/invented`

**Input fingerprint:** `8f1e63279ac420b2f281613b6efbb7b07bd5776f61633b24640ea3c5a0a8f490`

| Change | Recorded version |
| --- | --- |
| Invented names | Use invented names |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/rule-application/cruxeval-dac9a78a4a34555b5ff0.md).
