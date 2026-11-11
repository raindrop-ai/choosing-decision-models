# Similar distractors · Add fewer similar but irrelevant items variant

[Original question](../../../questions/relations/bbh-ff740484ebcc04612637.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> At Alder Club's practice event, Hugo finished ahead of Inez. Kira finished behind Inez.

## Question

> The following paragraphs each describe a set of five objects arranged in a fixed order. The statements are logically consistent within each paragraph. In a golf tournament, there were five golfers: Dan, Ana, Eli, Mya, and Amy. Amy finished above Eli. Ana finished above Amy. Mya finished below Eli. Dan finished last.

## Answer choices

- **A.** Dan finished third
- **B.** Ana finished third
- **C.** Eli finished third
- **D.** Mya finished third
- **E.** Amy finished third

**Reference answer:** `C`.

<details>
<summary>Exact evaluated input as JSON</summary>

```text
{
  "state": "At Alder Club's practice event, Hugo finished ahead of Inez. Kira finished behind Inez.",
  "question": "The following paragraphs each describe a set of five objects arranged in a fixed order. The statements are logically consistent within each paragraph. In a golf tournament, there were five golfers: Dan, Ana, Eli, Mya, and Amy. Amy finished above Eli. Ana finished above Amy. Mya finished below Eli. Dan finished last.",
  "choices": {
    "A": "Dan finished third",
    "B": "Ana finished third",
    "C": "Eli finished third",
    "D": "Mya finished third",
    "E": "Amy finished third"
  }
}
```

</details>

## Recorded model answers

The original column uses the control response paired with this variant. Missing responses and inputs outside a model’s limit remain visible.

| Model | Original answer | Variant answer | Change |
| --- | --- | --- | --- |
| GLiDE v1.2 | `C` — Eli finished third | `C` — Eli finished third | Same answer |
| Decider v1.1 | `C` — Eli finished third | `C` — Eli finished third | Same answer |
| Jev | `C` — Eli finished third | `C` — Eli finished third | Same answer |
| Microsoft Decision-1 | `E` — Amy finished third | `E` — Amy finished third | Same answer |
| Clef | `D` — Mya finished third | `C` — Eli finished third | Different answer |
| Luna Decisions | `D` — Mya finished third | `C` — Eli finished third | Different answer |
| Clef Flash | `C` — Eli finished third | `C` — Eli finished third | Same answer |
| Strands Decider | `B` — Ana finished third | `B` — Ana finished third | Same answer |
| GLiNER2.5 Decide | `E` — Amy finished third | `E` — Amy finished third | Same answer |
| Laya | `E` — Amy finished third | `E` — Amy finished third | Same answer |
| CalDec v1 | `B` — Ana finished third | `A` — Dan finished third | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/ff740484ebcc04612637/similar_distractors/low/clean-source_first_ordinal_distractors_full_0140`

**Input fingerprint:** `5242a114608733db12c0e9d9c1a9a2f53ae3ea3aabc601a606aead04c456075d`

| Change | Recorded version |
| --- | --- |
| Similar distractors | Add fewer similar but irrelevant items |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/bbh-ff740484ebcc04612637.md).
