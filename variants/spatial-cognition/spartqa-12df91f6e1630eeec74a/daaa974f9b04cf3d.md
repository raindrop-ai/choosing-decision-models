# Invented names · Use familiar names variant

[Original question](../../../questions/spatial-cognition/spartqa-12df91f6e1630eeec74a.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context, answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> We have three blocks, Apple, Bridge and Castle. Block Apple is below block Castle and above block Bridge. Block Apple has two medium yellow squares. Medium yellow square number one is touching the bottom edge of this block. This shape is below medium yellow square number two. Block Bridge contains one medium blue square. One medium yellow square is also in this block. The medium blue square is below the medium yellow square. And block Castle contains one medium blue square.

## Question

> Which blocks don't have any medium square that is below a medium square?

## Answer choices

- **A.** \[&quot;Apple&quot;, &quot;Castle&quot;\]
- **B.** \[&quot;Apple&quot;, &quot;Bridge&quot;, &quot;Castle&quot;\]
- **C.** \[&quot;Bridge&quot;, &quot;Castle&quot;\]
- **D.** \[&quot;Apple&quot;\]
- **E.** \[&quot;Castle&quot;\]
- **F.** \[&quot;Bridge&quot;\]
- **G.** \[&quot;Apple&quot;, &quot;Bridge&quot;\]
- **H.** \[\]

**Reference answer:** `E`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "We have three blocks, Apple, Bridge and Castle. Block Apple is below block Castle and above block Bridge. Block Apple has two medium yellow squares. Medium yellow square number one is touching the bottom edge of this block. This shape is below medium yellow square number two. Block Bridge contains one medium blue square. One medium yellow square is also in this block. The medium blue square is below the medium yellow square. And block Castle contains one medium blue square.",
  "question": "Which blocks don't have any medium square that is below a medium square?",
  "choices": {
    "A": "[\"Apple\", \"Castle\"]",
    "B": "[\"Apple\", \"Bridge\", \"Castle\"]",
    "C": "[\"Bridge\", \"Castle\"]",
    "D": "[\"Apple\"]",
    "E": "[\"Castle\"]",
    "F": "[\"Bridge\"]",
    "G": "[\"Apple\", \"Bridge\"]",
    "H": "[]"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `E` — \[&quot;C&quot;\] | `E` — \[&quot;Castle&quot;\] | Same answer |
| Decider v1.1 | `E` — \[&quot;C&quot;\] | `E` — \[&quot;Castle&quot;\] | Same answer |
| Jev | `E` — \[&quot;C&quot;\] | `E` — \[&quot;Castle&quot;\] | Same answer |
| Microsoft Decision-1 | `E` — \[&quot;C&quot;\] | `E` — \[&quot;Castle&quot;\] | Same answer |
| Clef | `E` — \[&quot;C&quot;\] | `E` — \[&quot;Castle&quot;\] | Same answer |
| Luna Decisions | `A` — \[&quot;A&quot;, &quot;C&quot;\] | `E` — \[&quot;Castle&quot;\] | Different answer |
| Clef Flash | `E` — \[&quot;C&quot;\] | `E` — \[&quot;Castle&quot;\] | Same answer |
| Strands Decider | `A` — \[&quot;A&quot;, &quot;C&quot;\] | `A` — \[&quot;Apple&quot;, &quot;Castle&quot;\] | Same answer |
| GLiNER2.5 Decide | `A` — \[&quot;A&quot;, &quot;C&quot;\] | `B` — \[&quot;Apple&quot;, &quot;Bridge&quot;, &quot;Castle&quot;\] | Different answer |
| Laya | `B` — \[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;\] | `A` — \[&quot;Apple&quot;, &quot;Castle&quot;\] | Different answer |
| CalDec v1 | `A` — \[&quot;A&quot;, &quot;C&quot;\] | `B` — \[&quot;Apple&quot;, &quot;Bridge&quot;, &quot;Castle&quot;\] | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/12df91f6e1630eeec74a/unfamiliar_names/familiar`

**Input fingerprint:** `8e6cafd463a0e2a3fa3f6239f8b2f2800f4ec69338f7447df93847a5a5148990`

| Change | Recorded version |
| --- | --- |
| Invented names | Use familiar names |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-12df91f6e1630eeec74a.md).
