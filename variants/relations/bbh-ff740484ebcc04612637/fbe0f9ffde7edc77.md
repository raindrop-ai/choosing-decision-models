# Misleading details · Add an unverified claim that conflicts with the evidence variant

[Original question](../../../questions/relations/bbh-ff740484ebcc04612637.md) · [Other versions of this question](README.md) · [All variants](../../README.md)

This version keeps the original reference answer. Its context, question instructions or answer choices were changed as described below.

**Changed fields:** context.

[How the edits were constructed](../../../docs/variant-methods.md)

## Context

> A reader thinks about the golf tournament: «Dan finished third.»

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
  "state": "A reader thinks about the golf tournament: «Dan finished third.»",
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
| Microsoft Decision-1 | `E` — Amy finished third | `C` — Eli finished third | Different answer |
| Clef | `D` — Mya finished third | `C` — Eli finished third | Different answer |
| Luna Decisions | `D` — Mya finished third | Refused | — |
| Clef Flash | `C` — Eli finished third | `C` — Eli finished third | Same answer |
| Strands Decider | `B` — Ana finished third | `A` — Dan finished third | Different answer |
| GLiNER2.5 Decide | `E` — Amy finished third | `A` — Dan finished third | Different answer |
| Laya | `E` — Amy finished third | `A` — Dan finished third | Different answer |
| CalDec v1 | `B` — Ana finished third | `A` — Dan finished third | Different answer |

<details>
<summary>Identifiers and recorded conditions</summary>

**Variant ID:** `bbh/ff740484ebcc04612637/misleading_summary/misleading/clean-source_first_ordinal_combined_contexts_full_0139`

**Input fingerprint:** `420c40285beef47ae2cad264a4be9c9de3509839ec8d38cc00cdbe7fe1b9fbb5`

| Change | Recorded version |
| --- | --- |
| Misleading details | Add an unverified claim that conflicts with the evidence |

</details>

Source attribution and dataset terms are linked from the [original question](../../../questions/relations/bbh-ff740484ebcc04612637.md).
