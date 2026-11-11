# Extra events · Add 6 unrelated events variant

[Original question](../../../questions/spatial-cognition/spartqa-12df91f6e1630eeec74a.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.
> Nolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue. Nolan classifies Kesil as an elegy. Nolan classifies Nereth as a satire. Nolan classifies Pavrel as a fable. Nolan classifies Sovrin as a ballad.
>
> We have three blocks, A, B and C. Block A is below block C and above block B. Block A has two medium yellow squares. Medium yellow square number one is touching the bottom edge of this block. This shape is below medium yellow square number two. Block B contains one medium blue square. One medium yellow square is also in this block. The medium blue square is below the medium yellow square. And block C contains one medium blue square.

## Question

> Which blocks don't have any medium square that is below a medium square?

## Answer choices

- **A.** [&quot;A&quot;, &quot;C&quot;]
- **B.** [&quot;A&quot;, &quot;B&quot;, &quot;C&quot;]
- **C.** [&quot;B&quot;, &quot;C&quot;]
- **D.** [&quot;A&quot;]
- **E.** [&quot;C&quot;]
- **F.** [&quot;B&quot;]
- **G.** [&quot;A&quot;, &quot;B&quot;]
- **H.** []

**Reference answer:** `E`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "Nolan is the editor of a poetry catalog. Its entries are Virel, Zorven, Kesil, Nereth, Pavrel, and Sovrin.\nNolan classifies Virel as a dialogue. Nolan classifies Zorven as a monologue. Nolan classifies Kesil as an elegy. Nolan classifies Nereth as a satire. Nolan classifies Pavrel as a fable. Nolan classifies Sovrin as a ballad.\n\nWe have three blocks, A, B and C. Block A is below block C and above block B. Block A has two medium yellow squares. Medium yellow square number one is touching the bottom edge of this block. This shape is below medium yellow square number two. Block B contains one medium blue square. One medium yellow square is also in this block. The medium blue square is below the medium yellow square. And block C contains one medium blue square.",
  "question": "Which blocks don't have any medium square that is below a medium square?",
  "choices": {
    "A": "[\"A\", \"C\"]",
    "B": "[\"A\", \"B\", \"C\"]",
    "C": "[\"B\", \"C\"]",
    "D": "[\"A\"]",
    "E": "[\"C\"]",
    "F": "[\"B\"]",
    "G": "[\"A\", \"B\"]",
    "H": "[]"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `E` — \[&quot;C&quot;\] | `E` — \[&quot;C&quot;\] | Same answer |
| Decider v1.1 | `E` — \[&quot;C&quot;\] | `E` — \[&quot;C&quot;\] | Same answer |
| Jev | `E` — \[&quot;C&quot;\] | `E` — \[&quot;C&quot;\] | Same answer |
| Microsoft Decision-1 | `E` — \[&quot;C&quot;\] | `E` — \[&quot;C&quot;\] | Same answer |
| Clef | `E` — \[&quot;C&quot;\] | `E` — \[&quot;C&quot;\] | Same answer |
| Luna Decisions | `A` — \[&quot;A&quot;, &quot;C&quot;\] | `E` — \[&quot;C&quot;\] | Different answer |
| Clef Flash | `E` — \[&quot;C&quot;\] | `E` — \[&quot;C&quot;\] | Same answer |
| Strands Decider | `A` — \[&quot;A&quot;, &quot;C&quot;\] | `A` — \[&quot;A&quot;, &quot;C&quot;\] | Same answer |
| GLiNER2.5 Decide | `A` — \[&quot;A&quot;, &quot;C&quot;\] | `A` — \[&quot;A&quot;, &quot;C&quot;\] | Same answer |
| Laya | `B` — \[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;\] | `A` — \[&quot;A&quot;, &quot;C&quot;\] | Different answer |
| CalDec v1 | `A` — \[&quot;A&quot;, &quot;C&quot;\] | `A` — \[&quot;A&quot;, &quot;C&quot;\] | Same answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `spartqa/12df91f6e1630eeec74a/event_count/6/clean-source_first_spartqa_short_contexts_full_0136`

**Input fingerprint:** `e24a56f1cfcc66bf725db0b6b64c339f19fa0d72ef4ddef797a67472f083644f`

| Change | Recorded version |
| --- | --- |
| Extra events | Add 6 unrelated events |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/spatial-cognition/spartqa-12df91f6e1630eeec74a.md).
