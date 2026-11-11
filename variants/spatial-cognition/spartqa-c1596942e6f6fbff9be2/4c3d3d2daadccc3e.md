# Invented names · Use invented names variant

[Original question](../../../questions/spatial-cognition/spartqa-c1596942e6f6fbff9be2.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context, answer choices or their order.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> There are three blocks, Varelin, Zorven and Kasel. There is one medium yellow square in block Varelin. To the right of block Varelin is block Zorven with one medium black square in it. There is also a medium blue square touching the bottom edge of this block. Below the medium black square is the medium blue square. Finally, we have block Kasel to the right of block Varelin. It has two medium yellow squares. There is also one medium black square in this block. It is below medium yellow square number two. Medium yellow square number one is touching the bottom edge of this block. This object is below medium yellow square number two and the medium black square.

## Question

> Which blocks don't have any medium square which is to the right of a yellow square?

## Answer choices

- **A.** [&quot;Varelin&quot;, &quot;Zorven&quot;]
- **B.** [&quot;Varelin&quot;, &quot;Zorven&quot;, &quot;Kasel&quot;]
- **C.** [&quot;Varelin&quot;]
- **D.** [&quot;Zorven&quot;, &quot;Kasel&quot;]
- **E.** [&quot;Kasel&quot;]
- **F.** []
- **G.** [&quot;Zorven&quot;]
- **H.** [&quot;Varelin&quot;, &quot;Kasel&quot;]

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "There are three blocks, Varelin, Zorven and Kasel. There is one medium yellow square in block Varelin. To the right of block Varelin is block Zorven with one medium black square in it. There is also a medium blue square touching the bottom edge of this block. Below the medium black square is the medium blue square. Finally, we have block Kasel to the right of block Varelin. It has two medium yellow squares. There is also one medium black square in this block. It is below medium yellow square number two. Medium yellow square number one is touching the bottom edge of this block. This object is below medium yellow square number two and the medium black square.",
  "question": "Which blocks don't have any medium square which is to the right of a yellow square?",
  "choices": {
    "A": "[\"Varelin\", \"Zorven\"]",
    "B": "[\"Varelin\", \"Zorven\", \"Kasel\"]",
    "C": "[\"Varelin\"]",
    "D": "[\"Zorven\", \"Kasel\"]",
    "E": "[\"Kasel\"]",
    "F": "[]",
    "G": "[\"Zorven\"]",
    "H": "[\"Varelin\", \"Kasel\"]"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — \[&quot;A&quot;\] | `C` — \[&quot;Varelin&quot;\] | Same answer |
| Decider v1.1 | `C` — \[&quot;A&quot;\] | `C` — \[&quot;Varelin&quot;\] | Same answer |
| Jev | `A` — \[&quot;A&quot;, &quot;B&quot;\] | `C` — \[&quot;Varelin&quot;\] | Different answer |
| Microsoft Decision-1 | `C` — \[&quot;A&quot;\] | `C` — \[&quot;Varelin&quot;\] | Same answer |
| Clef | `A` — \[&quot;A&quot;, &quot;B&quot;\] | `C` — \[&quot;Varelin&quot;\] | Different answer |
| Luna Decisions | `A` — \[&quot;A&quot;, &quot;B&quot;\] | `A` — \[&quot;Varelin&quot;, &quot;Zorven&quot;\] | Same answer |
| Clef Flash | `A` — \[&quot;A&quot;, &quot;B&quot;\] | `A` — \[&quot;Varelin&quot;, &quot;Zorven&quot;\] | Same answer |
| Strands Decider | `C` — \[&quot;A&quot;\] | `C` — \[&quot;Varelin&quot;\] | Same answer |
| GLiNER2.5 Decide | `H` — \[&quot;A&quot;, &quot;C&quot;\] | `B` — \[&quot;Varelin&quot;, &quot;Zorven&quot;, &quot;Kasel&quot;\] | Different answer |
| Laya | `A` — \[&quot;A&quot;, &quot;B&quot;\] | `A` — \[&quot;Varelin&quot;, &quot;Zorven&quot;\] | Same answer |
| CalDec v1 | `A` — \[&quot;A&quot;, &quot;B&quot;\] | `D` — \[&quot;Zorven&quot;, &quot;Kasel&quot;\] | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/c1596942e6f6fbff9be2/unfamiliar_names/invented`

**Input fingerprint:** `063911387c725287693b4bbd9290e9b4d38019c8e67f2ace312d466159c3ed68`

| Change | Recorded version |
| --- | --- |
| Invented names | Use invented names |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-c1596942e6f6fbff9be2.md).
